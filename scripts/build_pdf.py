#!/usr/bin/env python3
"""Build the specification as a PDF: Sphinx singlehtml printed by headless Chrome or Edge.

Printing the HTML keeps what HTML readers see (the bold short forms inside long-form examples,
which the LaTeX builder drops) and needs no TeX. The print layout lives in the ``@media print``
block of ``docs/source/_static/custom.css``; ``docs/source/_static/pdf_print.js`` fits long code
lines and is loaded only by this build (``sphinx-build -t pdf``, see ``docs/source/conf.py``).

Usage (from the repository root, with the dev environment active):

    python scripts/build_pdf.py                 # docs/_build/pdf/hed-specification-<version>.pdf
    python scripts/build_pdf.py --prerelease    # docs/_build/pdf/prerelease/..., with the banner
    python scripts/build_pdf.py --out FILE.pdf

The version comes from ``pyproject.toml``. The browser is ``--browser``, else ``CHROME_BIN``, else
the usual install locations. CI on Linux passes ``--no-sandbox``. Releases use
``scripts/do_spec_release.py prepare``, which calls this script.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "docs" / "source"
BUILD_ROOT = REPO_ROOT / "docs" / "_build"
MIN_BYTES = 100_000
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "google-chrome-stable",
    "chromium-browser",
    "chromium",
    "microsoft-edge",
]


def spec_version():
    text = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    return re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE).group(1)


def find_browser(explicit=None):
    """Path of Chrome or Edge, or None."""
    for candidate in [explicit, os.environ.get("CHROME_BIN"), *BROWSERS]:
        if not candidate:
            continue
        found = shutil.which(candidate) or (candidate if Path(candidate).is_file() else None)
        if found:
            return found
    return None


def build_pdf(out, prerelease=False, browser=None, no_sandbox=False, skip_build=False):
    """Build the singlehtml page and print it to ``out``; return the PDF size in bytes."""
    out = Path(out).resolve()  # Chrome resolves relative paths against its own working directory
    html_dir = BUILD_ROOT / ("pdf-html-prerelease" if prerelease else "pdf-html")
    tags = ["-t", "pdf"] + (["-t", "prerelease"] if prerelease else [])
    if not skip_build:
        cmd = [sys.executable, "-m", "sphinx", "-q", "-b", "singlehtml", *tags, str(SOURCE_DIR), str(html_dir)]
        print("$ " + " ".join(cmd), flush=True)
        subprocess.run(cmd, check=True)
    index = html_dir / "index.html"
    if not index.is_file():
        raise RuntimeError(f"{index} does not exist; run without --skip-build")

    path = find_browser(browser)
    if path is None:
        raise RuntimeError("no Chrome or Edge found; pass --browser or set CHROME_BIN")
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    cmd = [
        path,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        f"--user-data-dir={(html_dir / 'chrome-profile').resolve()}",
        "--no-pdf-header-footer",
        "--generate-pdf-document-outline",
        f"--print-to-pdf={out}",
        index.resolve().as_uri(),
    ]
    if no_sandbox:
        cmd.insert(1, "--no-sandbox")
    print(f"$ {Path(path).name} --print-to-pdf={out} {index.resolve().as_uri()}", flush=True)
    result = subprocess.run(cmd, check=False, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if not out.is_file():
        tail = "\n".join((result.stdout + result.stderr).strip().splitlines()[-20:])
        raise RuntimeError(f"the browser wrote no PDF (exit {result.returncode})\n{tail}")
    size = out.stat().st_size
    if size < MIN_BYTES:
        raise RuntimeError(f"{out} is only {size} bytes; the print failed")
    return size


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--out", help="PDF to write (default docs/_build/pdf/[prerelease/]hed-specification-<version>.pdf)")
    parser.add_argument("--prerelease", action="store_true", help='add the "Unreleased draft" banner')
    parser.add_argument("--browser", help="Chrome or Edge executable")
    parser.add_argument("--no-sandbox", action="store_true", help="pass --no-sandbox to the browser (CI on Linux)")
    parser.add_argument("--skip-build", action="store_true", help="print the existing singlehtml build")
    args = parser.parse_args(argv)

    default_dir = BUILD_ROOT / "pdf" / ("prerelease" if args.prerelease else "")
    out = Path(args.out) if args.out else default_dir / f"hed-specification-{spec_version()}.pdf"
    try:
        size = build_pdf(out, args.prerelease, args.browser, args.no_sandbox, args.skip_build)
    except (RuntimeError, subprocess.CalledProcessError) as e:
        print(f"build_pdf: FAILED: {e}", file=sys.stderr)
        return 1
    print(f"wrote {Path(out).resolve()} ({size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
