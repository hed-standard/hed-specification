# hed-specification

Purpose: source of the HED (Hierarchical Event Descriptors) specification - Sphinx/MyST markdown chapters published as HTML via GitHub Pages. Not in scope: no runtime Python package, no test suite, and no schema files - HED schemas live in the `hed-schemas` repository.

## Commands

Test framework: none (documentation-only repository; no test suite).

- Install dev env: `uv venv --clear .venv` then `uv pip install -e ".[dev]"` (or the plain `python -m venv` / `pip install` equivalents)
- Build docs: `sphinx-build -b html docs/source docs/_build/html`
- Spelling: `uvx typos`
- Markdown format check: `uvx --with mdformat-myst mdformat --check --wrap no --number docs/source *.md`
- Link check (after building docs): `lychee --config lychee.toml 'docs/_build/html/**/*.html'`

CI runs the same checks on every push and PR to `main` (`.github/workflows/`): deploy-docs.yml (Sphinx build), typos.yaml, mdformat.yaml, and links.yaml (weekly schedule plus manual).

## Layout

- `docs/source/` - the spec chapters (`01_Introduction.md` ... `Appendix_B.md`), `conf.py`, and static assets. This is the content of the repository.
- `.github/workflows/` - CI pipelines listed above.
- `pyproject.toml` - project metadata, `[dev]` dependencies, typos config.
- `lychee.toml` - link-checker configuration.
- `.status/` - working notes. Gitignored; local to each machine.

## Conventions that differ from defaults

- **ASCII only** in prose, code, comments, and filenames: `-` not em or en dashes, `->` not arrows, `...` not an ellipsis character, straight quotes. Exception: genuine data (author names, dataset titles, recorded API responses) keeps whatever characters it actually contains.
- Markdown headers in sentence case: capitalize the first word, proper nouns, and acronyms only (`## Build and validation`, not `## Build and Validation`).
- Line endings are LF everywhere; `.gitattributes` normalizes on commit and `.vscode/settings.json` on save. Files always end with a newline.
- Markdown must pass `mdformat --check --wrap no --number`.
- Use proper heading hierarchy: `#` chapters, `##` sections, `###` subsections.

## HED annotation conventions

- Tags are case-sensitive and use `/` for hierarchy (`Sensory-event/Visual/Color/Red`); groups use parentheses: `(Onset, Sensory-event, (Circle, Blue))`.
- Use backticks for inline HED tags and fenced code blocks with the `hed` language tag for multi-line examples; show short form (`Red`) and long form together when helpful.
- Use precise terminology as defined in `docs/source/02_Terminology.md`, and distinguish the specification version (owned by `pyproject.toml`) from the HED schema version (8.x.x).
- Always state which specification version introduces or modifies a feature.
- Use standardized error codes (`CHARACTER_INVALID`, `COMMA_MISSING`, ...) as listed in `docs/source/Appendix_B.md`; add new codes there in the existing format.

## Rules that are easy to get wrong

- Cross-reference chapters with relative markdown links (`[Chapter 4: Basic annotation](04_Basic_annotation.md)`) and sections with anchors (`[See Definition syntax](#45-definition-syntax)`).
- Write for tool implementers: no ambiguous or informal language, and keep specification statements separate from implementation details.

## Related repositories

- `hed-schemas` - the HED schema XML/mediawiki sources this spec describes. Not vendored here; a session that needs it must be granted access to that checkout.
- `hed-resources` - user-facing documentation and tutorials.

## Where the thinking lives

`.status/` is gitignored, so it exists only on the machine that wrote it and never in a fresh clone or worktree.

- `.status/README.md` - the index. Read this first; it lists what is active.
- `.status/decisions.md` - why things are the way they are. Read before proposing structural changes. Append entries; never rewrite one.
- `.status/plans/*.md` - active plans. Check the `Status:` header and the `[ ]` / `[x]` markers before starting work.
- `.status/local-environment.md` - this machine's paths, interpreter, and quirks. Tool-agnostic. Never copy its contents into a committed file.
- IMPORTANT: do not read `.status/archive/` unless a file is named for you. Nothing new is created at the `.status/` root.

## Working agreements

- IMPORTANT: every file written to `.status/` opens with a `For humans:` summary - three or four sentences, at the very top: what the file is and what a person needs to take from it. The same applies to a long answer in a session: lead with the conclusion.
- IMPORTANT: temporary scripts, experiments, and one-off test files go in `.status/scratch/` - **never the repository root**. Delete them when the experiment ends; anything in `scratch/` may be deleted unread.
- IMPORTANT: never delete or rewrite a file under `.status/` without asking first. Appending is fine.
- For a change spanning more than three files, write a plan to `.status/plans/` and stop for review before editing.
- When you are guessing about an external API or data format, say so explicitly rather than assuming.
- Show evidence, not assertions: the command you ran and its actual output.
- Do not commit, push, or create branches unless asked.
