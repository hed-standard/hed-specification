#!/usr/bin/env python3
"""Generate the section 2.2 character table from docs/source/_static/character_sets.json.

The table between ``<!-- character-sets:begin -->`` and ``<!-- character-sets:end -->`` in
``docs/source/02_Terminology.md`` is rewritten from the JSON file, so the prose and the file that
validators load cannot disagree. The script also checks the file itself: every regex compiles in
Python and, when ``node`` is on the path, in JavaScript; every name that ``value_class_defaults`` and
``hed_string`` use resolves to a set, an alias or a single character; and each set's ``excludes`` and
``tests`` behave as stated in both languages.

Usage (from the repository root, standard library only):

    python scripts/generate_character_table.py           # rewrite the table
    python scripts/generate_character_table.py --check   # exit 1 if the table or the file is off

CI runs ``--check`` (.github/workflows/character-sets.yaml).
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "docs" / "source" / "_static" / "character_sets.json"
MARKDOWN_PATH = REPO_ROOT / "docs" / "source" / "02_Terminology.md"
BEGIN = "<!-- character-sets:begin -->"
END = "<!-- character-sets:end -->"

NODE_CHECK = r"""
const data = JSON.parse(require('fs').readFileSync(process.argv[1], 'utf8'));
let failures = 0;
function full(regex) { return new RegExp('^(?:' + regex + ')$'); }
for (const [name, entry] of Object.entries(data.sets)) {
  let rx;
  try { rx = full(entry.regex); } catch (e) { console.log(`node: ${name}: regex does not compile: ${e.message}`); failures++; continue; }
  for (const ch of entry.excludes || []) { if (rx.test(ch)) { console.log(`node: ${name}: excludes ${JSON.stringify(ch)} but regex matches it`); failures++; } }
  for (const ch of (entry.tests || {}).valid || []) { if (!rx.test(ch)) { console.log(`node: ${name}: ${JSON.stringify(ch)} should match`); failures++; } }
  for (const ch of (entry.tests || {}).invalid || []) { if (rx.test(ch)) { console.log(`node: ${name}: ${JSON.stringify(ch)} should not match`); failures++; } }
}
for (const [name, entry] of Object.entries(data.value_class_words)) {
  try { new RegExp(entry.regex); } catch (e) { console.log(`node: value_class_words.${name}: ${e.message}`); failures++; }
}
try { new RegExp(data.hed_string.forbidden.regex); } catch (e) { console.log(`node: hed_string.forbidden: ${e.message}`); failures++; }
process.exit(failures ? 1 : 0);
"""


def load_data():
    with open(JSON_PATH, encoding="utf-8") as fp:
        return json.load(fp)


def resolve_name(data, name):
    """Return the regex for an allowedCharacter name, or None when the name is unknown."""
    if name in data["sets"]:
        return data["sets"][name]["regex"]
    if name in data["aliases"]:
        return data["sets"][data["aliases"][name]]["regex"]
    if len(name) == 1:
        return re.escape(name)
    return None


def check_file(data):
    """Return a list of problems with the JSON file (empty when it is sound)."""
    problems = []
    for name, entry in data["sets"].items():
        try:
            rx = re.compile(f"^(?:{entry['regex']})$")
        except re.error as exc:
            problems.append(f"{name}: regex does not compile in Python: {exc}")
            continue
        for ch in entry.get("excludes", []):
            if rx.match(ch):
                problems.append(f"{name}: excludes {ch!r} but its regex matches it")
        for ch in entry.get("tests", {}).get("valid", []):
            if not rx.match(ch):
                problems.append(f"{name}: {ch!r} should match")
        for ch in entry.get("tests", {}).get("invalid", []):
            if rx.match(ch):
                problems.append(f"{name}: {ch!r} should not match")
    for alias, target in data["aliases"].items():
        if alias in data["sets"]:
            problems.append(f"alias {alias} is also a set")
        if target not in data["sets"]:
            problems.append(f"alias {alias} points to unknown set {target}")
    for class_name, entries in data["value_class_defaults"].items():
        for entry in entries:
            for name in entry["sets"]:
                if resolve_name(data, name) is None:
                    problems.append(f"value_class_defaults.{class_name}: unknown name {name}")
    for name in data["hed_string"]["tag_chars"]["sets"]:
        if resolve_name(data, name) is None:
            problems.append(f"hed_string.tag_chars: unknown name {name}")
    for name, entry in data["value_class_words"].items():
        try:
            re.compile(entry["regex"])
        except re.error as exc:
            problems.append(f"value_class_words.{name}: {exc}")
    try:
        re.compile(data["hed_string"]["forbidden"]["regex"])
    except re.error as exc:
        problems.append(f"hed_string.forbidden: {exc}")
    return problems


def check_javascript(data_path):
    """Run the JavaScript checks with node when it is available. Returns (ran, problems)."""
    node = shutil.which("node")
    if not node:
        return False, []
    result = subprocess.run([node, "-e", NODE_CHECK, str(data_path)], capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    return True, [line for line in output.split("\n") if line] if result.returncode else []


def render_table(data):
    """Render the markdown table, aligned the way mdformat aligns it."""
    rows = [(f"`{name}`", entry["description"]) for name, entry in data["sets"].items()]
    rows += [(f"`{alias}`", f"Alias of `{target}`.") for alias, target in data["aliases"].items()]
    rows.sort(key=lambda row: row[0])
    header = ("Name", "Description")
    width_name = max(len(header[0]), *(len(r[0]) for r in rows))
    width_desc = max(len(header[1]), *(len(r[1]) for r in rows))
    lines = [
        f"| {header[0].ljust(width_name)} | {header[1].ljust(width_desc)} |",
        f"| {'-' * width_name} | {'-' * width_desc} |",
    ]
    lines += [f"| {name.ljust(width_name)} | {desc.ljust(width_desc)} |" for name, desc in rows]
    return "\n".join(lines)


def render_markdown(data, text):
    """Return the markdown with the block between the markers regenerated."""
    begin = text.index(BEGIN) + len(BEGIN)
    end = text.index(END)
    return text[:begin] + "\n\n" + render_table(data) + "\n\n" + text[end:]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--check", action="store_true", help="do not write; fail if anything is stale or unsound")
    args = parser.parse_args(argv)

    data = load_data()
    problems = check_file(data)
    ran, js_problems = check_javascript(JSON_PATH)
    problems += js_problems
    for problem in problems:
        print(problem)
    if not ran:
        print("note: node not found, JavaScript regex check skipped")

    current = MARKDOWN_PATH.read_text(encoding="utf-8")
    if BEGIN not in current or END not in current:
        print(f"{MARKDOWN_PATH}: markers {BEGIN} / {END} not found")
        return 1
    rendered = render_markdown(data, current)
    stale = rendered != current
    if args.check:
        if stale:
            print(f"{MARKDOWN_PATH.relative_to(REPO_ROOT)}: table is stale; run scripts/generate_character_table.py")
        ok = not stale and not problems
        print("character sets: OK" if ok else "character sets: FAILED")
        return 0 if ok else 1
    if stale:
        MARKDOWN_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {MARKDOWN_PATH.relative_to(REPO_ROOT)}")
    else:
        print("table already current")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
