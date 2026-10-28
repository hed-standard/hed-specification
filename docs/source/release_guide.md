# Specification release guide

This guide is for HED maintainers. It describes how a new version of the HED specification goes from `main` to a published release with its PDF. It is not part of the specification and is left out of the PDF.

A release is done in three parts:

1. **`prepare`** - on a branch made from hed-standard `main`, `scripts/do_spec_release.py prepare` builds the release PDF, checks it, and leaves the result staged for review.
2. **Pull request** - you review, commit and push, open a pull request against hed-standard `main`, and merge it when CI is green.
3. **`notes` and the GitHub release** - after the merge, `scripts/do_spec_release.py notes` checks `main` and prints the CHANGELOG entry to paste as the release description; you create the tag and the GitHub release by hand in the GitHub web interface, then update the Zenodo record by hand.

The script never commits, pushes, tags, or calls the GitHub API. The final look over everything, and the release itself, stay with a person.

## What is published where

| Site path                                | Built from                                            | Changes                                   |
| ---------------------------------------- | ----------------------------------------------------- | ----------------------------------------- |
| `/` (the specification)                  | the newest release tag                                | when a release is published               |
| `/prerelease/`                           | `main`, with an "Unreleased draft" banner and its PDF | on every push to `main` (every merged PR) |
| `/releases/hed-specification-X.Y.Z.pdf`  | the committed `releases/` folder                      | once, in the release pull request         |
| `/releases/hed-specification-latest.pdf` | a copy of the newest committed release PDF            | in each release pull request              |

The workflow `.github/workflows/deploy-docs.yml` assembles all of it. The prerelease PDF is never committed. Until a tag `v4.0.0` or later exists, the root is built from `main` as before; older tags predate the PDF tooling.

The sidebar of every page links to `releases/hed-specification-latest.pdf` and to the `releases/` folder on GitHub.

## Before you start

- The version being released is the `version` in `pyproject.toml`; `docs/source/conf.py` reads it from there. Do not change it in the release pull request: the release tag is made on the merged release commit, and the site root is built from that tag, so the tagged tree must name the released version.
- `CHANGELOG.md` has a `# Release X.Y.Z Month Day, Year` heading for the version (the `(unreleased)` heading replaced by the release date), with the entry that becomes the release notes.
- Chrome or Edge is installed. `scripts/build_pdf.py` looks in the usual install locations; otherwise pass `--browser` or set `CHROME_BIN`.
- Your checkout has a git remote pointing at `hed-standard/hed-specification` (any name).

## Step 1: prepare

The following example assumes that you are in the root of your local repository with its venv activated, on a branch made from hed-standard `main`, and that you are releasing 4.0.0.

```bash
python scripts/do_spec_release.py prepare 4.0.0
```

It checks that the working tree is clean, that the branch contains hed-standard `main`, that `pyproject.toml` says `4.0.0`, that `CHANGELOG.md` has its entry, that the tag `v4.0.0` does not exist, and that `releases/` has no 4.0.0 PDF and nothing newer. It then builds `releases/hed-specification-4.0.0.pdf`, copies it to `releases/hed-specification-latest.pdf`, runs the `check` below, stages `releases/`, and prints the commit command. Every step prints what it does; the first failure prints `FAILED:` with the reason and exits with status 1.

Open the new PDF and look it over before you commit.

## Step 2: pull request

Commit with the printed command, push, and open a pull request against hed-standard `main`. CI runs `scripts/do_spec_release.py check` (`.github/workflows/releases.yaml`) and builds the site and the prerelease PDF (`.github/workflows/deploy-docs.yml`). Merge when it is green.

## Step 3: notes, the GitHub release and Zenodo

After the merge, print the release notes:

```bash
python scripts/do_spec_release.py notes 4.0.0
```

It checks that hed-standard `main` has `releases/hed-specification-4.0.0.pdf`, that the latest copy matches it, that `pyproject.toml` on `main` says `4.0.0`, and that the tag does not exist yet. It prints the tag, target and title, and the CHANGELOG entry between `----- release notes -----` and `----- end of release notes -----`. With `--out notes.md` it also writes the entry to that file.

Then, by hand:

1. Create the release at [github.com/hed-standard/hed-specification/releases/new](https://github.com/hed-standard/hed-specification/releases/new): tag `v4.0.0` (created on publish), target `main`, title `HED specification v4.0.0`, the printed notes as the description, and `releases/hed-specification-4.0.0.pdf` attached.
2. Publishing the release runs `deploy-docs.yml`, which rebuilds the site root from the new tag.
3. Add `releases/hed-specification-4.0.0.pdf` to the new version of the hed-specification Zenodo record.

## After the release

Move `main` to the next version in a separate pull request: the `version` in `pyproject.toml` and a new `# Release X.Y.Z (unreleased)` heading at the top of `CHANGELOG.md`. From then on `/prerelease/` shows the new version with the banner.

## Building a PDF locally

**Build the PDF of the working tree** into `docs/_build/pdf/hed-specification-<version>.pdf`.

```bash
python scripts/build_pdf.py
```

**Build the prerelease PDF** with the "Unreleased draft" banner, into `docs/_build/pdf/prerelease/`.

```bash
python scripts/build_pdf.py --prerelease
```

**Check the `releases/` folder** (no browser needed): every file is `hed-specification-X.Y.Z.pdf` or `hed-specification-latest.pdf`, every file is a PDF, and the latest copy is the newest version.

```bash
python scripts/do_spec_release.py check
```

The PDF is the Sphinx `singlehtml` build (`sphinx-build -t pdf`) printed by headless Chrome. The print layout is the `@media print` block of `docs/source/_static/custom.css`; `docs/source/_static/pdf_print.js`, loaded only in this build, shrinks long code lines to fit and marks a line that still has to wrap with a gray `   >` at the start of each continuation.
