#!/usr/bin/env python3
"""
Local link checker for Sphinx documentation.
This script builds the Sphinx docs and then checks all links in the generated HTML files.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return None

def main():
    """Main function to build docs and check links."""
    # Get the current directory
    root_dir = Path(__file__).parent
    docs_dir = root_dir / "docs"
    build_dir = docs_dir / "_build" / "html"

    print("=" * 60)
    print("HED Specification - Local Link Checker")
    print("=" * 60)

    # Step 1: Build Sphinx documentation
    print("\n1. Building Sphinx documentation...")
    build_result = run_command(
        ["sphinx-build", "-b", "html", "source", "_build/html"],
        cwd=docs_dir
    )

    if not build_result:
        print("❌ Failed to build documentation!")
        return 1

    print("✅ Documentation built successfully!")

    # Step 2: Check if build directory exists
    if not build_dir.exists():
        print(f"❌ Build directory not found: {build_dir}")
        return 1

    # Step 3: Run link checker
    print("\n2. Checking links in built documentation...")

    # Check if linkchecker is available
    try:
        subprocess.run(["linkchecker", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ linkchecker not found. Install it with: pip install linkchecker")
        return 1

    # Run linkchecker on the built HTML
    index_file = build_dir / "index.html"
    if not index_file.exists():
        print(f"❌ Index file not found: {index_file}")
        return 1

    print(f"Checking links starting from: {index_file}")

    # Run linkchecker - check both internal and external links
    try:
        link_check_result = subprocess.run([
            "linkchecker",
            "--check-extern",  # Check external links
            "--check-html",    # Check HTML syntax and internal links
            "--recursion-level=10",  # Follow internal links recursively
            "--no-warnings",   # Suppress warnings for cleaner output
            "--output", "text",  # Text output format
            str(index_file)
        ], capture_output=True, text=True)

        print("✅ Link checking completed!")
        print("\nLink checker output:")
        print("-" * 40)
        print(link_check_result.stdout)

        if link_check_result.stderr:
            print("\nProgress details:")
            print(link_check_result.stderr)

        # Check the return code to determine success
        if link_check_result.returncode == 0:
            print("🎉 All links are working!")
        else:
            print("⚠️  Some broken links were found (see output above)")

    except FileNotFoundError:
        print("❌ linkchecker not found. Install it with: pip install linkchecker")
        return 1

    print("\n" + "=" * 60)
    print("Link checking process completed!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())
