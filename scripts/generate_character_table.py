#!/usr/bin/env python3
"""Generate the section 2.2 character table from docs/source/_static/character_sets.json.

The table between ``<!-- character-sets:begin -->`` and ``<!-- character-sets:end -->`` in
``docs/source/02_Terminology.md`` is rewritten from the JSON file, so the prose and the file that
validators load cannot disagree. The script also checks the file itself: every regex compiles in
Python and, when ``node`` is on the path, in JavaScript; every name that ``value_class_defaults`` and
``hed_string`` use resolves to a set, an alias or a single character; and each set's ``excludes`` and
``tests`` behave as stated in both languages, as do the whole-value ``tests`` of ``value_class_words``.
It also checks that the top-level keys are exactly those that the Appendix A.7.1 layout lists, that
every field of the nested objects is a row, under its own object, of the field table of its own
Appendix A.7 subsection and nothing else is, that ``file_version`` has the form X.Y.Z, and that
``specification_version`` equals the version in ``pyproject.toml``.

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
APPENDIX_A_PATH = REPO_ROOT / "docs" / "source" / "Appendix_A.md"
PYPROJECT_PATH = REPO_ROOT / "pyproject.toml"
APPENDIX_A_SECTION = "## A.7. Character sets file"
APPENDIX_A_LAYOUT = "### A.7.1. File layout"
TOP_KEYS = (
    "title",
    "description",
    "specification_version",
    "file_version",
    "sets",
    "aliases",
    "literal_names",
    "declaration_wins_from",
    "value_class_defaults",
    "value_class_words",
    "hed_string",
)
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
  let rx;
  try { rx = new RegExp(entry.regex); } catch (e) { console.log(`node: value_class_words.${name}: ${e.message}`); failures++; continue; }
  for (const v of (entry.tests || {}).valid || []) { if (!rx.test(v)) { console.log(`node: value_class_words.${name}: ${JSON.stringify(v)} should match`); failures++; } }
  for (const v of (entry.tests || {}).invalid || []) { if (rx.test(v)) { console.log(`node: value_class_words.${name}: ${JSON.stringify(v)} should not match`); failures++; } }
}
try { new RegExp(data.hed_string.forbidden.regex); } catch (e) { console.log(`node: hed_string.forbidden: ${e.message}`); failures++; }
process.exit(failures ? 1 : 0);
"""


def load_data():
    with open(JSON_PATH, encoding="utf-8") as fp:
        return json.load(fp)


def check_versions(data):
    """The top-level keys are TOP_KEYS; file_version is X.Y.Z; specification_version is pyproject's."""
    problems = []
    missing = [k for k in TOP_KEYS if k not in data]
    extra = [k for k in data if k not in TOP_KEYS]
    if missing:
        problems.append(f"top level: missing {missing}")
    if extra:
        problems.append(f"top level: unknown keys {extra}")
    file_version = data.get("file_version")
    if not isinstance(file_version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", file_version):
        problems.append(f"file_version: {file_version!r} is not of the form X.Y.Z")
    match = re.search(r'^version\s*=\s*"([^"]+)"', PYPROJECT_PATH.read_text(encoding="utf-8"), re.M)
    expected = match.group(1) if match else None
    if data.get("specification_version") != expected:
        problems.append(
            f"specification_version: {data.get('specification_version')!r} differs from pyproject.toml {expected!r}"
        )
    return problems


def expected_fields(data):
    """For each Appendix A.7 field table, the (field, object) pairs it must document.

    The object is None for a table without an Object column, whose rows all describe one kind of entry.
    """
    sets_fields = {(f, None) for entry in data.get("sets", {}).values() for f in entry}
    names = {(f, "literal_names") for f in data.get("literal_names", {})}
    names |= {(f, "declaration_wins_from") for f in data.get("declaration_wins_from", {})}
    names |= {
        (f, "value_class_defaults")
        for entries in data.get("value_class_defaults", {}).values()
        for entry in entries
        for f in entry
    }
    words = {(f, None) for entry in data.get("value_class_words", {}).values() for f in entry}
    hed_string = {(key, "hed_string") for key in data.get("hed_string", {})}
    hed_string |= {(f, key) for key, obj in data.get("hed_string", {}).items() for f in obj}
    return {"A.7.2": sets_fields, "A.7.3": names, "A.7.4": words, "A.7.5": hed_string}


def documented_fields(subsection):
    """The (field, object) pairs of the field table in one subsection's text.

    The field is the code span of the first column; the object is the first code span of the Object column,
    or None when the table has no Object column.
    """
    rows = [line for line in subsection.split("\n") if line.startswith("|")]
    if len(rows) < 2:
        return set()
    header = [cell.strip() for cell in rows[0].strip("|").split("|")]
    has_object = len(header) > 1 and header[1] == "Object"
    pairs = set()
    for line in rows[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        field = re.fullmatch(r"`([A-Za-z_]+)`", cells[0])
        if not field:
            continue
        obj = re.search(r"`([A-Za-z_]+)`", cells[1]) if has_object else None
        pairs.add((field.group(1), obj.group(1) if obj else None))
    return pairs


def check_documented(data):
    """A.7.1 lists exactly the top-level keys, and the A.7 field tables exactly the nested fields."""
    text = APPENDIX_A_PATH.read_text(encoding="utf-8")
    if APPENDIX_A_SECTION not in text:
        return [f"Appendix_A.md: section {APPENDIX_A_SECTION!r} not found"]
    section = text[text.index(APPENDIX_A_SECTION) :]
    following = re.search(r"^## ", section[len(APPENDIX_A_SECTION) :], re.M)
    if following:
        section = section[: len(APPENDIX_A_SECTION) + following.start()]
    problems = []
    for number, expected in expected_fields(data).items():
        heading = re.search(rf"^### {re.escape(number)}\. .*$", section, re.M)
        if not heading:
            problems.append(f"Appendix_A.md: subsection {number} not found")
            continue
        body = section[heading.end() :]
        following = re.search(r"^### ", body, re.M)
        if following:
            body = body[: following.start()]
        documented = documented_fields(body)

        def label(pair):
            return pair[0] if pair[1] is None else f"{pair[1]}.{pair[0]}"

        for pair in sorted(expected - documented, key=label):
            problems.append(f"Appendix_A.md {number}: field {label(pair)!r} is not documented")
        for pair in sorted(documented - expected, key=label):
            problems.append(f"Appendix_A.md {number}: documents {label(pair)!r}, which the file does not have")
    if APPENDIX_A_LAYOUT not in section:
        return problems + [f"Appendix_A.md: subsection {APPENDIX_A_LAYOUT!r} not found"]
    layout = section[section.index(APPENDIX_A_LAYOUT) + len(APPENDIX_A_LAYOUT) :]
    following = re.search(r"^### ", layout, re.M)
    if following:
        layout = layout[: following.start()]
    # Only the first bullet list of the subsection is the key list; later lists define fields.
    first_list = re.search(r"(?:^- .*\n)+", layout, re.M)
    heads = re.findall(r"^- (.*?):", first_list.group(0), re.M) if first_list else []
    listed = {name for head in heads for name in re.findall(r"`([A-Za-z_]+)`", head)}
    problems += [f"Appendix_A.md A.7.1: key {k!r} is not listed" for k in TOP_KEYS if k not in listed]
    problems += [f"Appendix_A.md A.7.1: lists {k!r}, which the file does not have" for k in sorted(listed - set(TOP_KEYS))]
    return problems


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
    problems = check_versions(data) + check_documented(data)
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
            word = re.compile(entry["regex"])
        except re.error as exc:
            problems.append(f"value_class_words.{name}: {exc}")
            continue
        for value in entry.get("tests", {}).get("valid", []):
            if not word.match(value):
                problems.append(f"value_class_words.{name}: {value!r} should match")
        for value in entry.get("tests", {}).get("invalid", []):
            if word.match(value):
                problems.append(f"value_class_words.{name}: {value!r} should not match")
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
