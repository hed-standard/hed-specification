#!/usr/bin/env python3
"""Release the HED specification PDF; see docs/source/release_guide.md.

Three subcommands, run from the repository root with the dev environment active:

    python scripts/do_spec_release.py prepare 4.0.0   # before the PR: build, copy, check, stage
    python scripts/do_spec_release.py notes 4.0.0     # after the PR has merged
    python scripts/do_spec_release.py check           # the releases/ folder is consistent

``prepare`` builds ``releases/hed-specification-<version>.pdf`` with ``scripts/build_pdf.py``,
refreshes ``releases/hed-specification-latest.pdf``, runs ``check`` and stages the result (never
commits). ``notes`` checks that the release is on hed-standard main and prints the CHANGELOG entry
for pasting into the GitHub release (``--out FILE`` also writes it to a file); the release and the
Zenodo upload are always done by hand. ``check`` needs no browser; CI runs it
(.github/workflows/releases.yaml). The script never pushes, tags, or calls the GitHub API.

Every step prints what it does; the first failed command or check prints the reason and exits 1.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pdf  # the sibling script, found through the sys.path line above

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASES = "releases"
LATEST = "hed-specification-latest.pdf"
UPSTREAM = "hed-standard/hed-specification"
PDF_NAME = re.compile(r"hed-specification-(\d+\.\d+\.\d+)\.pdf")
MIN_BYTES = 100_000


class ReleaseError(Exception):
    """A step failed; the message says why."""


# ---------------------------------------------------------------------------------------------
# Printing and running
# ---------------------------------------------------------------------------------------------


def step(number: int, name: str) -> None:
    print(f"\n== Step {number}: {name}", flush=True)


def ok(message: str) -> None:
    print(f"   ok: {message}", flush=True)


def require(condition: bool, message: str) -> None:
    """Stop the release with ``message`` unless ``condition`` holds."""
    if not condition:
        raise ReleaseError(message)


def git(repo: Path, *args: str) -> str:
    """Run git, print it and its result, and stop on a non-zero exit."""
    print(f"   $ git {' '.join(args)}", flush=True)
    result = git_quiet(repo, *args)
    require(result.returncode == 0, f"git {' '.join(args)} failed:\n{(result.stdout + result.stderr).strip()}")
    ok("exit 0")
    return result.stdout


def git_quiet(repo: Path, *args: str) -> subprocess.CompletedProcess:
    """Run git without printing; the caller checks the result."""
    return subprocess.run(["git", *args], cwd=repo, check=False, capture_output=True, text=True, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------


def version_key(version: str) -> tuple[int, ...]:
    require(re.fullmatch(r"\d+\.\d+\.\d+", version) is not None, f"'{version}' is not a version of the form X.Y.Z")
    return tuple(int(part) for part in version.split("."))


def pyproject_version(text: str) -> str | None:
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return match.group(1) if match else None


def changelog_heading(version: str) -> str:
    """The start of a release heading: ``# Release 4.0.0 October 30, 2026`` (the date follows)."""
    return f"# Release {version}"


def extract_changelog_entry(text: str, version: str) -> str:
    """The lines under the version's ``# Release`` heading, up to the next ``# `` heading.

    The heading must carry a date, not ``(unreleased)``: the entry is the release notes.
    """
    lines = text.splitlines()
    heading = changelog_heading(version)
    starts = [i for i, line in enumerate(lines) if line == heading or line.startswith(heading + " ")]
    require(len(starts) == 1, f"CHANGELOG.md has {len(starts)} '{heading} ...' headings; expected one")
    title = lines[starts[0]]
    require(
        "unreleased" not in title.lower() and title != heading,
        f"CHANGELOG.md heading '{title}' has no release date; write it as '{heading} Month Day, Year'",
    )
    body = []
    for line in lines[starts[0] + 1 :]:
        if line.startswith("# "):
            break
        body.append(line)
    entry = "\n".join(body).strip("\n")
    require(entry.strip() != "", f"the CHANGELOG.md entry under '{title}' is empty")
    return entry + "\n"


def upstream_remote(repo: Path) -> str:
    """Name of the remote that points at hed-standard/hed-specification (names vary by checkout)."""
    for line in git_quiet(repo, "remote", "-v").stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and UPSTREAM in parts[1].replace(".git", ""):
            return parts[0]
    raise ReleaseError(f"no git remote points at {UPSTREAM}")


def released_versions(folder: Path) -> list[str]:
    found = [m.group(1) for f in folder.glob("*.pdf") if (m := PDF_NAME.fullmatch(f.name))]
    return sorted(found, key=version_key)


# ---------------------------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------------------------


def check_releases(repo: Path) -> list[str]:
    """Problems with releases/: names, PDF headers, sizes, and the latest copy."""
    folder = repo / RELEASES
    if not folder.is_dir():
        return [f"{RELEASES}/ does not exist"]
    problems = []
    for f in sorted(folder.iterdir()):
        if f.name != LATEST and not PDF_NAME.fullmatch(f.name):
            problems.append(f"{RELEASES}/{f.name}: not hed-specification-X.Y.Z.pdf or {LATEST}")
            continue
        data = f.read_bytes()
        if not data.startswith(b"%PDF-"):
            problems.append(f"{RELEASES}/{f.name}: not a PDF (no %PDF- header)")
        if len(data) < MIN_BYTES:
            problems.append(f"{RELEASES}/{f.name}: only {len(data)} bytes")
    versions = released_versions(folder)
    if not versions:
        problems.append(f"{RELEASES}/ holds no hed-specification-X.Y.Z.pdf")
    elif not (folder / LATEST).is_file():
        problems.append(f"{RELEASES}/{LATEST} is missing")
    elif (folder / LATEST).read_bytes() != (folder / f"hed-specification-{versions[-1]}.pdf").read_bytes():
        problems.append(f"{RELEASES}/{LATEST} is not a copy of hed-specification-{versions[-1]}.pdf, the newest")
    return problems


def check(repo: Path) -> int:
    problems = check_releases(repo)
    for problem in problems:
        print(problem)
    versions = released_versions(repo / RELEASES) if (repo / RELEASES).is_dir() else []
    if not problems:
        print(f"releases: {len(versions)} versions, {versions[0]} to {versions[-1]}; {LATEST} = {versions[-1]}")
    print("releases: OK" if not problems else "releases: FAILED")
    return 1 if problems else 0


# ---------------------------------------------------------------------------------------------
# prepare
# ---------------------------------------------------------------------------------------------


def preflight(repo: Path, version: str, browser: str | None) -> str:
    step(0, "Preflight checks")
    require((repo / "docs" / "source" / "conf.py").is_file(), f"{repo} is not a hed-specification checkout")
    ok(f"hed-specification checkout at {repo}")

    branch = git_quiet(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    require(branch not in ("main", "HEAD"), f"on '{branch}': prepare a release on a branch made from main")
    ok(f"on branch {branch}")

    dirty = git_quiet(repo, "status", "--porcelain").stdout.strip()
    require(not dirty, "working tree is not clean:\n" + dirty)
    ok("working tree is clean")

    remote = upstream_remote(repo)
    git(repo, "fetch", remote)
    require(
        git_quiet(repo, "merge-base", "--is-ancestor", f"{remote}/main", "HEAD").returncode == 0,
        f"HEAD does not contain {remote}/main; rebase the branch on it first",
    )
    ok(f"HEAD contains {remote}/main")

    version_key(version)
    found = pyproject_version((repo / "pyproject.toml").read_text(encoding="utf-8"))
    require(found == version, f"pyproject.toml says version {found}, not {version}")
    ok(f"pyproject.toml says version {version} (conf.py reads it from there)")

    extract_changelog_entry((repo / "CHANGELOG.md").read_text(encoding="utf-8"), version)
    ok(f"CHANGELOG.md has an entry under '{changelog_heading(version)}'")

    tags = git(repo, "ls-remote", "--tags", remote, f"v{version}").strip()
    require(not tags, f"tag v{version} already exists on {remote}")
    ok(f"tag v{version} does not exist yet")

    folder = repo / RELEASES
    require(not (folder / f"hed-specification-{version}.pdf").exists(), f"{RELEASES}/ already has {version}")
    versions = released_versions(folder)
    last = versions[-1] if versions else None
    if last:
        require(version_key(last) < version_key(version), f"last released {last} is not older than {version}")
    ok(f"last released PDF: {last or 'none'}")

    path = build_pdf.find_browser(browser)
    require(path is not None, "no Chrome or Edge found; pass --browser or set CHROME_BIN")
    ok(f"browser: {path}")
    return path


def prepare(repo: Path, version: str, browser: str | None) -> None:
    print(f"Preparing the HED specification {version} release PDF in {repo}")
    path = preflight(repo, version, browser)
    pdf = repo / RELEASES / f"hed-specification-{version}.pdf"

    step(1, f"Build {RELEASES}/{pdf.name}")
    try:
        size = build_pdf.build_pdf(pdf, browser=path, repo=repo)
    except (RuntimeError, subprocess.CalledProcessError) as e:
        raise ReleaseError(f"PDF build failed: {e}") from e
    ok(f"{pdf.name}: {size:,} bytes")

    step(2, f"Copy it to {RELEASES}/{LATEST}")
    shutil.copyfile(pdf, repo / RELEASES / LATEST)
    require((repo / RELEASES / LATEST).read_bytes() == pdf.read_bytes(), f"{LATEST} differs from {pdf.name}")
    ok(f"{LATEST} is a copy of {pdf.name}")

    step(3, f"Check {RELEASES}/")
    problems = check_releases(repo)
    require(not problems, "\n".join(problems))
    ok(f"{RELEASES}/ is consistent")

    print("\n== Done: staging the release PDF (nothing is committed)")
    git(repo, "add", "--", RELEASES)
    leftover = git_quiet(repo, "status", "--porcelain").stdout
    # porcelain "XY path": X is the staged state, Y the unstaged one; only "X " lines are fully staged
    require(
        not [line for line in leftover.splitlines() if line[0] == "?" or line[1] != " "],
        "unstaged or untracked changes remain after staging:\n" + leftover,
    )
    print(git_quiet(repo, "status", "--short").stdout.rstrip())
    print(f"\nOpen {pdf} and look it over, then commit and push:")
    print(f'   git commit -m "Release the HED specification {version} PDF"')
    print(f"After the pull request merges, run: python scripts/do_spec_release.py notes {version}")


# ---------------------------------------------------------------------------------------------
# notes
# ---------------------------------------------------------------------------------------------


def notes(repo: Path, version: str, out: Path | None) -> None:
    pdf = f"{RELEASES}/hed-specification-{version}.pdf"
    print(f"Release notes for HED specification {version} from hed-standard main")
    step(1, "Check the release is on hed-standard main")
    remote = upstream_remote(repo)
    git(repo, "fetch", remote)
    ref = f"{remote}/main"
    blob = git_quiet(repo, "rev-parse", f"{ref}:{pdf}")
    require(blob.returncode == 0, f"{ref} has no {pdf}; is the PR merged?")
    latest = git_quiet(repo, "rev-parse", f"{ref}:{RELEASES}/{LATEST}")
    require(latest.stdout.strip() == blob.stdout.strip(), f"{ref}: {RELEASES}/{LATEST} is not a copy of {pdf}")
    ok(f"{ref} has {pdf} and {LATEST} is a copy of it")
    found = pyproject_version(git_quiet(repo, "show", f"{ref}:pyproject.toml").stdout)
    require(found == version, f"{ref}: pyproject.toml says {found}; the tagged tree must say {version}")
    ok(f"{ref}: pyproject.toml says {version}")
    tags = git(repo, "ls-remote", "--tags", remote, f"v{version}").strip()
    require(not tags, f"tag v{version} already exists on {remote}")
    ok(f"tag v{version} does not exist yet")

    step(2, "Extract the CHANGELOG entry")
    changelog = git_quiet(repo, "show", f"{ref}:CHANGELOG.md")
    require(changelog.returncode == 0, f"cannot read CHANGELOG.md on {ref}")
    entry = extract_changelog_entry(changelog.stdout, version)
    ok(f"{len(entry.splitlines())} lines, printed between the markers below")
    if out:
        out.write_bytes(entry.encode("utf-8"))
        ok(f"also wrote them to {out}")

    print("\nCreate the release in the GitHub web interface:")
    print(f"   https://github.com/{UPSTREAM}/releases/new")
    print(f"   Tag:    v{version}   (create it on publish)")
    print("   Target: main")
    print(f"   Title:  HED specification v{version}")
    print("   Notes:  paste the text between the markers" + (f" (or the contents of {out})" if out else ""))
    print(f"   Attach: {pdf}")
    print("Publishing the release rebuilds the site from the tag (deploy-docs.yml).")
    print(f"Then add {pdf} to the new version of the hed-specification Zenodo record.")
    print("\n----- release notes -----")
    print(entry.rstrip("\n"))
    print("----- end of release notes -----")


# ---------------------------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare", help="build the release PDF, refresh the latest copy, check, and stage")
    p.add_argument("version", help="the version being released, e.g. 4.0.0 (must match pyproject.toml)")
    p.add_argument("--browser", help="Chrome or Edge executable (default: CHROME_BIN or the usual locations)")
    p.add_argument("--repo", default=str(REPO_ROOT), help="hed-specification checkout (default: this one)")
    n = sub.add_parser("notes", help="after the merge: check main and print the release notes")
    n.add_argument("version")
    n.add_argument("--repo", default=str(REPO_ROOT))
    n.add_argument("--out", help="also write the CHANGELOG entry to this file (default: print it only)")
    c = sub.add_parser("check", help=f"check that {RELEASES}/ is consistent (no browser needed)")
    c.add_argument("--repo", default=str(REPO_ROOT))
    args = parser.parse_args(argv)

    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
    repo = Path(args.repo).resolve()
    try:
        if args.command == "check":
            return check(repo)
        if args.command == "prepare":
            prepare(repo, args.version, args.browser)
        else:
            notes(repo, args.version, Path(args.out) if args.out else None)
    except ReleaseError as e:
        print(f"\nFAILED: {e}", file=sys.stderr, flush=True)
        print("Stopped; nothing after this step ran.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
