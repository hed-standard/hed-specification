#!/usr/bin/env python3
"""Generate the section 3.2.8 reserved-tag tables from docs/source/_static/reserved_tags.json.

The block between ``<!-- reserved-tags:begin -->`` and ``<!-- reserved-tags:end -->`` in
``docs/source/03_HED_formats.md`` is rewritten from the JSON file, so the prose and the file that
validators load cannot disagree. The script also checks the file itself: every row has every key
with the right type, each row's name matches its key, the subgroup limits are consistent, every
``otherAllowedNonDefTags`` name is another row, every ``ERROR_CODE`` is a heading of
``Appendix_B.md``, every row field is documented in the Appendix A.6 field table and nothing else
is, every ``secondaryWith`` name is an allowed companion that is not secondary in turn, every
``fromSchema`` is a version string, and every ``valueForms`` entry names a known form.

Usage (from the repository root, standard library only):

    python scripts/generate_reserved_table.py           # rewrite the tables
    python scripts/generate_reserved_table.py --check   # exit 1 if the tables or the file are off

CI runs ``--check`` (.github/workflows/reserved-tags.yaml).
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "docs" / "source" / "_static" / "reserved_tags.json"
MARKDOWN_PATH = REPO_ROOT / "docs" / "source" / "03_HED_formats.md"
APPENDIX_A_PATH = REPO_ROOT / "docs" / "source" / "Appendix_A.md"
APPENDIX_B_PATH = REPO_ROOT / "docs" / "source" / "Appendix_B.md"
APPENDIX_A_SECTION = "## A.6. Reserved tags file"
BEGIN = "<!-- reserved-tags:begin -->"
END = "<!-- reserved-tags:end -->"

BOOLEAN_KEYS = (
    "noExtension",
    "requireValue",
    "tagGroup",
    "topLevelTagGroup",
    "requiresDef",
    "requiresTimeline",
    "allowSpliceInGroup",
)
OPTIONAL_KEYS = ("fromSchema", "secondaryWith")
REQUIRED_KEYS = (
    "name",
    *BOOLEAN_KEYS,
    "minNonDefSubgroups",
    "maxNonDefSubgroups",
    "otherAllowedNonDefTags",
    "ERROR_CODE",
)
SECOND_PARTS = {
    "placeholder": ("`name` or `name/#`", "only `#`, present exactly when the definition's contents hold one `#`"),
    "placeholderValue": (
        "`name` or `name/value`",
        "the value of the definition's placeholder, checked against that placeholder tag's value class "
        "and units; present exactly when the definition has a placeholder",
    ),
}
VERSION = re.compile(r"^\d+\.\d+\.\d+$")


def load_data():
    with open(JSON_PATH, encoding="utf-8") as fp:
        return json.load(fp)


def check_file(data):
    """Return a list of problems with the JSON file (empty when sound)."""
    problems = []
    codes = set(re.findall(r"^#+ ([A-Z_]+)\\?\*?\s*$", APPENDIX_B_PATH.read_text(encoding="utf-8"), re.M))
    tags = data.get("tags", {})
    for key, row in tags.items():
        where = f"tags.{key}"
        missing = [k for k in REQUIRED_KEYS if k not in row]
        extra = [k for k in row if k not in REQUIRED_KEYS and k not in OPTIONAL_KEYS]
        if missing:
            problems.append(f"{where}: missing {missing}")
        if extra:
            problems.append(f"{where}: unknown keys {extra}")
        if missing:
            continue
        if row["name"] != key:
            problems.append(f"{where}: name {row['name']!r} differs from its key")
        for k in BOOLEAN_KEYS:
            if not isinstance(row[k], bool):
                problems.append(f"{where}.{k}: not a boolean")
        low, high = row["minNonDefSubgroups"], row["maxNonDefSubgroups"]
        if not isinstance(low, int) or low < 0:
            problems.append(f"{where}.minNonDefSubgroups: not a non-negative integer")
        if high is not None and (not isinstance(high, int) or high < low):
            problems.append(f"{where}.maxNonDefSubgroups: not null or an integer >= the minimum")
        for other in row["otherAllowedNonDefTags"]:
            if other not in tags:
                problems.append(f"{where}.otherAllowedNonDefTags: {other!r} is not a row")
        if row["ERROR_CODE"] not in codes:
            problems.append(f"{where}.ERROR_CODE: {row['ERROR_CODE']!r} is not a heading of Appendix_B.md")
        for other in row.get("secondaryWith", []):
            if other not in row["otherAllowedNonDefTags"]:
                problems.append(f"{where}.secondaryWith: {other!r} is not in otherAllowedNonDefTags")
            elif key in tags.get(other, {}).get("secondaryWith", []):
                problems.append(f"{where}.secondaryWith: {other!r} is also secondary with {key!r}")
        if "fromSchema" in row and not VERSION.match(str(row["fromSchema"])):
            problems.append(f"{where}.fromSchema: {row['fromSchema']!r} is not a version x.y.z")
    for key, form in data.get("valueForms", {}).items():
        if form.get("secondPart") not in SECOND_PARTS:
            problems.append(f"valueForms.{key}.secondPart: expected one of {sorted(SECOND_PARTS)}")
    problems += check_documented()
    return problems


def check_documented():
    """Every row field must have a row in the Appendix A.6 field table, and no other field may."""
    text = APPENDIX_A_PATH.read_text(encoding="utf-8")
    if APPENDIX_A_SECTION not in text:
        return [f"Appendix_A.md: section {APPENDIX_A_SECTION!r} not found"]
    section = text[text.index(APPENDIX_A_SECTION) :]
    following = re.search(r"^## ", section[len(APPENDIX_A_SECTION) :], re.M)
    if following:
        section = section[: len(APPENDIX_A_SECTION) + following.start()]
    documented = set(re.findall(r"^\| `([A-Za-z_]+)` +\|", section, re.M))
    fields = set(REQUIRED_KEYS) | set(OPTIONAL_KEYS)
    problems = [f"Appendix_A.md A.6: field {f!r} is not documented" for f in sorted(fields - documented)]
    problems += [f"Appendix_A.md A.6: documents {f!r}, which the file does not have" for f in sorted(documented - fields)]
    return problems


def yes_no(value):
    return "yes" if value else "no"


def tag_list(names):
    return ", ".join(f"`{t}`" for t in names) or "none"


def join_words(items):
    """Join items as English prose: a, b, and c."""
    if len(items) <= 2:
        return " and ".join(items)
    return ", ".join(items[:-1]) + ", and " + items[-1]


def render_table(header, rows):
    """Render a markdown table, aligned the way mdformat aligns it."""
    widths = [max(len(header[i]), *(len(r[i]) for r in rows)) for i in range(len(header))]
    lines = [
        "| " + " | ".join(h.ljust(w) for h, w in zip(header, widths)) + " |",
        "| " + " | ".join("-" * w for w in widths) + " |",
    ]
    lines += ["| " + " | ".join(c.ljust(w) for c, w in zip(row, widths)) + " |" for row in rows]
    return "\n".join(lines)


def render_block(data):
    tags = data["tags"]
    rows = []
    for key, row in tags.items():
        high = row["maxNonDefSubgroups"]
        rows.append(
            (
                f"`{key}`",
                f">= `{row['fromSchema']}`" if "fromSchema" in row else "all",
                yes_no(row["requireValue"]),
                yes_no(row["requiresDef"]),
                tag_list(row["otherAllowedNonDefTags"]),
                str(row["minNonDefSubgroups"]),
                "no limit" if high is None else str(high),
                tag_list(row.get("secondaryWith", [])),
                yes_no(row["requiresTimeline"]),
                yes_no(row["allowSpliceInGroup"]),
            )
        )
    header = ("Tag", "Schemas", "Value", "Anchor", "Others", "Min", "Max", "Secondary", "Timeline", "{ }")
    parts = []
    common = []
    if all(r["noExtension"] for r in tags.values()):
        common.append("MUST NOT be extended")
    if all(r["tagGroup"] and r["topLevelTagGroup"] for r in tags.values()):
        common.append("MUST appear in a top-level tag group")
    if common:
        parts.append("Every tag in the following table " + " and ".join(common) + ".")
    parts.append(render_table(header, rows))
    by_code = {}
    for key, row in tags.items():
        by_code.setdefault(row["ERROR_CODE"], []).append(f"`{key}`")
    clauses = [
        f"[{code}](./Appendix_B.md#{code.lower()}) for {join_words(names)}" for code, names in sorted(by_code.items())
    ]
    parts.append("A violation of a rule in this table is reported as " + join_words(clauses) + ".")
    forms = data.get("valueForms", {})
    if forms:
        form_rows = [
            (f"`{key}`", SECOND_PARTS[f["secondPart"]][0], SECOND_PARTS[f["secondPart"]][1])
            for key, f in forms.items()
        ]
        parts.append("Tags whose value has two parts:")
        parts.append(render_table(("Tag", "Value", "After the name"), form_rows))
    return "\n\n".join(parts)


def render_markdown(data, text):
    """Return the markdown with the block between the markers regenerated."""
    begin = text.index(BEGIN) + len(BEGIN)
    end = text.index(END)
    return text[:begin] + "\n\n" + render_block(data) + "\n\n" + text[end:]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--check", action="store_true", help="do not write; fail if anything is stale or unsound")
    args = parser.parse_args(argv)

    data = load_data()
    problems = check_file(data)
    for problem in problems:
        print(problem)

    current = MARKDOWN_PATH.read_text(encoding="utf-8")
    if BEGIN not in current or END not in current:
        print(f"{MARKDOWN_PATH}: markers {BEGIN} / {END} not found")
        return 1
    if problems:
        print("reserved tags: FAILED")
        return 1
    rendered = render_markdown(data, current)
    stale = rendered != current
    if args.check:
        if stale:
            print(f"{MARKDOWN_PATH.relative_to(REPO_ROOT)}: tables are stale; run scripts/generate_reserved_table.py")
        print("reserved tags: FAILED" if stale else "reserved tags: OK")
        return 1 if stale else 0
    if stale:
        MARKDOWN_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {MARKDOWN_PATH.relative_to(REPO_ROOT)}")
    else:
        print("tables already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
