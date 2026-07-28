# HED-specification developer instructions

If a `.status/local-environment.md` file exists in the repository root, read it first. It contains machine-specific settings (OS, shell, virtual-environment activation) that override the defaults below.

Trust these instructions. Only search the repo for additional context when the information here is incomplete or appears incorrect.

## Repository overview

This is a **documentation-only** repository that manages the HED (Hierarchical Event Descriptors) ecosystem specification. It contains no runtime Python packages — only Sphinx/MyST markdown source files, official PDF releases, reference XML schemas, and JSON test cases for HED validators.

- **Specification version**: 4.0.0
- **Target HED schema versions**: ≥ 8.0.0 (HED-3G)
- **Documentation framework**: Sphinx 7+ with MyST parser, Furo theme
- **Python**: ≥ 3.10 (used only for building docs and running quality tools)
- **Output**: HTML (GitHub Pages via Sphinx) and PDF (in `hedspec/`)

## Project layout

| Path                 | Purpose                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| `docs/source/`       | Sphinx/MyST markdown spec chapters (`01_Introduction.md` … `Appendix_B.md`), `conf.py`, static assets |
| `hedspec/`           | Official PDF specification releases (do **not** modify)                                               |
| `hedxml/`            | Reference HED schema XML files (do **not** modify)                                                    |
| `tests/`             | JSON test cases keyed by error code                                                                   |
| `.status/`           | Local analysis scripts and summaries (gitignored)                                                     |
| `pyproject.toml`     | Project metadata and `[dev]` dependencies                                                             |
| `lychee.toml`        | Link-checker configuration                                                                            |
| `.github/workflows/` | CI pipelines (see below)                                                                              |

## Build and validation

### Line endings configuration

This repository is configured to use Unix-style line endings (`\n`, LF) across all platforms.

#### Git configuration

- **`.gitattributes`**: Explicitly sets `* text=auto eol=lf` to normalize all text files to LF line endings on commit
- **Global Git config**: `core.autocrlf=false` and `core.eol=lf` (prevents automatic CRLF conversion on Windows)

#### VS Code settings

The `.vscode/settings.json` is configured with:

```json
{
    "files.eol": "\n",
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true
}
```

This ensures:

- New files created in VS Code use LF line endings
- Files always end with a newline (required by CI checks)
- Trailing whitespace is automatically cleaned up

### Bootstrap (one time)

```bash
uv venv --clear .venv          # or: python -m venv .venv
# activate the venv (see local-environment.md for platform-specific command)
uv pip install -e ".[dev]"     # or: pip install -e ".[dev]"
```

### Build documentation

```bash
sphinx-build -b html docs/source docs/_build/html
```

### Local quality checks (run before pushing)

Always run these — they mirror the CI pipelines and catch failures early.

| Check               | Command                                                                            |
| ------------------- | ---------------------------------------------------------------------------------- |
| Spelling (typos)    | `uvx typos`                                                                        |
| Markdown formatting | `uvx --with mdformat-myst mdformat --check --wrap no --number docs/source *.md`    |
| Link checking       | Build docs first, then: `lychee --config lychee.toml 'docs/_build/html/**/*.html'` |

### CI pipelines (`.github/workflows/`)

Every push and PR to `main` runs these checks automatically:

| Workflow             | File              | What it checks                                                  |
| -------------------- | ----------------- | --------------------------------------------------------------- |
| Deploy documentation | `deploy-docs.yml` | Sphinx build succeeds                                           |
| Typos                | `typos.yaml`      | No typos (`uvx typos`, config in `pyproject.toml [tool.typos]`) |
| Mdformat             | `mdformat.yaml`   | Markdown formatting compliance                                  |
| Lychee link checker  | `links.yaml`      | No broken links (weekly schedule + manual)                      |

## Markdown style

- **Heading case**: Use sentence case — capitalize only the first letter of the first word (and proper nouns). Example: `## Build and validation`, not `## Build and Validation`.
- Use proper heading hierarchy (`#` for chapters, `##` for sections, `###` for subsections).
- Use code blocks with the `hed` language tag for HED annotation examples.
- Markdown files must pass `mdformat --check --wrap no --number`.

## HED annotation conventions

- Tags are case-sensitive and use `/` for hierarchy (e.g., `Sensory-event/Visual/Color/Red`).
- Groups use parentheses: `(Onset, Sensory-event, (Circle, Blue))`.
- Definitions allow reusable annotation patterns with placeholders.
- Library schemas extend the standard schema with domain-specific vocabulary.
- Use backticks for inline HED tags; use fenced code blocks for multi-line examples.
- Show both short form (`Red`) and long form when helpful.

## Key principles

### Documentation standards

- Write in clear, technical language for tool implementers and advanced users.
- Use precise terminology defined in `02_Terminology.md`.
- Cross-reference related sections using markdown links.
- Always specify which specification version introduces or modifies features.
- Distinguish between specification version (4.x.x) and schema version (8.x.x).

### Code and testing standards

- Python code follows PEP 8; use `ruff` for linting.
- Test files use JSON: `{"error_code": {"description": "...", "tests": {"valid": [...], "invalid": [...]}}}`.
- Use standardized error codes (e.g., `CHARACTER_INVALID`, `COMMA_MISSING`) as listed in `Appendix_B.md`. Add new error codes there following the existing format.
- Use `pathlib.Path` for file paths; use type hints and docstrings in Python scripts.

### Cross-references

- Link to other chapters: `[Chapter 4: Basic annotation](04_Basic_annotation.md)`
- Link to sections: `[See Definition syntax](#45-definition-syntax)`
- Link to external HED resources with full URLs

## Avoid

- Don't modify files in `hedspec/` or `hedxml/`.
- Don't introduce breaking changes to the test JSON format without discussion.
- Don't use ambiguous or informal language in specification documentation.
- Don't mix specification features with implementation details.

## Related resources

- [HED specification](https://www.hedtags.org/hed-specification)
- [HED resources](https://www.hedtags.org/hed-resources)
- [HED schemas repository](https://github.com/hed-standard/hed-schemas)
- [HED standard organization](https://github.com/hed-standard)
- [HED tags website](https://www.hedtags.org)
