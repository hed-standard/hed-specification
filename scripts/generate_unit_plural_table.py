#!/usr/bin/env python3
"""Generate the Appendix A.1.1 table of unit plurals from docs/source/_static/unit_plurals.json.

The table between ``<!-- unit-plurals:begin -->`` and ``<!-- unit-plurals:end -->`` in
``docs/source/Appendix_A.md`` is rewritten from the JSON file, so the prose and the file that
validators load cannot disagree. The script also checks the file itself: the top-level keys are
exactly those that the Appendix A.8.1 layout lists, ``file_version`` has the form X.Y.Z,
``specification_version`` equals the version in ``pyproject.toml``, and ``plurals`` is a non-empty
object of strings whose keys are in ascending order of character code, whose keys and values are
non-empty ASCII without a blank, in which no two keys have the same plural, and in which no plural
is a different key.

Usage (from the repository root, standard library only):

    python scripts/generate_unit_plural_table.py           # rewrite the table
    python scripts/generate_unit_plural_table.py --check   # exit 1 if the table or the file is off

CI runs ``--check`` (.github/workflows/unit-plurals.yaml).
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "docs" / "source" / "_static" / "unit_plurals.json"
MARKDOWN_PATH = REPO_ROOT / "docs" / "source" / "Appendix_A.md"
PYPROJECT_PATH = REPO_ROOT / "pyproject.toml"
APPENDIX_A_SECTION = "## A.8. Unit plurals file"
APPENDIX_A_LAYOUT = "### A.8.1. File layout"
TOP_KEYS = ("title", "description", "specification_version", "file_version", "plurals")
BEGIN = "<!-- unit-plurals:begin -->"
END = "<!-- unit-plurals:end -->"
PAIRS_PER_ROW = 2


def no_duplicate_keys(pairs):
    """Object hook that rejects a JSON object with a repeated key, which json.load would silently merge."""
    keys = [key for key, _ in pairs]
    repeated = sorted({key for key in keys if keys.count(key) > 1})
    if repeated:
        raise ValueError(f"repeated keys {repeated}")
    return dict(pairs)


def load_data():
    with open(JSON_PATH, encoding="utf-8") as fp:
        return json.load(fp, object_pairs_hook=no_duplicate_keys)


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


def check_documented(text):
    """The first bullet list of A.8.1 lists exactly the top-level keys."""
    if APPENDIX_A_SECTION not in text:
        return [f"Appendix_A.md: section {APPENDIX_A_SECTION!r} not found"]
    section = text[text.index(APPENDIX_A_SECTION) :]
    if APPENDIX_A_LAYOUT not in section:
        return [f"Appendix_A.md: subsection {APPENDIX_A_LAYOUT!r} not found"]
    layout = section[section.index(APPENDIX_A_LAYOUT) + len(APPENDIX_A_LAYOUT) :]
    following = re.search(r"^##+ ", layout, re.M)
    if following:
        layout = layout[: following.start()]
    # Only the first bullet list of the subsection is the key list; a later list states the properties.
    first_list = re.search(r"(?:^- .*\n)+", layout, re.M)
    heads = re.findall(r"^- (.*?):", first_list.group(0), re.M) if first_list else []
    listed = {name for head in heads for name in re.findall(r"`([A-Za-z_]+)`", head)}
    problems = [f"Appendix_A.md A.8.1: key {k!r} is not listed" for k in TOP_KEYS if k not in listed]
    problems += [f"Appendix_A.md A.8.1: lists {k!r}, which the file does not have" for k in sorted(listed - set(TOP_KEYS))]
    return problems


def check_plurals(plurals):
    """Return a list of problems with the plurals object (empty when it is sound)."""
    if not isinstance(plurals, dict) or not plurals:
        return ["plurals: must be a non-empty object"]
    problems = []
    for name, plural in plurals.items():
        for label, value in (("unit name", name), ("plural", plural)):
            if not isinstance(value, str) or not value:
                problems.append(f"plurals: {label} {value!r} of entry {name!r} is not a non-empty string")
            elif not value.isascii():
                problems.append(f"plurals: {label} {value!r} is not ASCII")
            elif not value.isprintable() or " " in value:
                problems.append(f"plurals: {label} {value!r} contains a blank or a control character")
    names = list(plurals)
    if names != sorted(names):
        first = next(a for a, b in zip(names, sorted(names)) if a != b)
        problems.append(f"plurals: keys are not in ascending order of character code (first out of place: {first!r})")
    owners = {}
    for name, plural in plurals.items():
        if isinstance(plural, str):
            owners.setdefault(plural, []).append(name)
    for plural, sharing in owners.items():
        if len(sharing) > 1:
            problems.append(f"plurals: {plural!r} is the plural of more than one unit name: {sharing}")
        if plural in plurals and sharing != [plural]:
            problems.append(f"plurals: {plural!r}, the plural of {sharing}, is itself a different unit name")
    return problems


def check_file(data, text):
    """Return a list of problems with the JSON file (empty when it is sound)."""
    if not isinstance(data, dict):
        return ["top level: must be an object"]
    return check_versions(data) + check_documented(text) + check_plurals(data.get("plurals"))


def render_table(plurals):
    """Render the markdown table, PAIRS_PER_ROW pairs to a row, reading down each pair of columns.

    The cells are padded the way mdformat pads them, so the generated table passes the format check.
    """
    pairs = [(f"`{name}`", f"`{plural}`") for name, plural in plurals.items()]
    height = -(-len(pairs) // PAIRS_PER_ROW)
    header = ["Unit name", "Plural"] * PAIRS_PER_ROW
    rows = []
    for index in range(height):
        row = []
        for column in range(PAIRS_PER_ROW):
            position = column * height + index
            row.extend(pairs[position] if position < len(pairs) else ("", ""))
        rows.append(row)
    widths = [max(len(header[i]), 3, *(len(row[i]) for row in rows)) for i in range(len(header))]

    def line(cells):
        return "| " + " | ".join(cell.ljust(width) for cell, width in zip(cells, widths)) + " |"

    return "\n".join([line(header), line(["-" * width for width in widths])] + [line(row) for row in rows])


def render_markdown(plurals, text):
    """Return the markdown with the block between the markers regenerated."""
    begin = text.index(BEGIN) + len(BEGIN)
    end = text.index(END)
    return text[:begin] + "\n\n" + render_table(plurals) + "\n\n" + text[end:]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--check", action="store_true", help="do not write; fail if anything is stale or unsound")
    args = parser.parse_args(argv)

    try:
        data = load_data()
    except ValueError as exc:
        print(f"{JSON_PATH.relative_to(REPO_ROOT)}: {exc}")
        print("unit plurals: FAILED")
        return 1
    current = MARKDOWN_PATH.read_text(encoding="utf-8")
    problems = check_file(data, current)
    for problem in problems:
        print(problem)
    if BEGIN not in current or END not in current:
        print(f"{MARKDOWN_PATH}: markers {BEGIN} / {END} not found")
        return 1
    plurals = data.get("plurals") if isinstance(data, dict) else None
    if not isinstance(plurals, dict) or not plurals:
        print("unit plurals: FAILED")
        return 1
    rendered = render_markdown(plurals, current)
    stale = rendered != current
    if args.check:
        if stale:
            print(f"{MARKDOWN_PATH.relative_to(REPO_ROOT)}: table is stale; run scripts/generate_unit_plural_table.py")
        ok = not stale and not problems
        print("unit plurals: OK" if ok else "unit plurals: FAILED")
        return 0 if ok else 1
    if problems:
        # An unsound file can render a broken table (a newline in a plural), so nothing is written.
        print(f"{MARKDOWN_PATH.relative_to(REPO_ROOT)}: not written; fix the problems above first")
        return 1
    if stale:
        MARKDOWN_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {MARKDOWN_PATH.relative_to(REPO_ROOT)}")
    else:
        print("table already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
