# HED specification release guide (maintainers)

The release guide is [`docs/source/release_guide.md`](docs/source/release_guide.md), published at [https://www.hedtags.org/hed-specification/release_guide.html](https://www.hedtags.org/hed-specification/release_guide.html).

In short, run `prepare` on a branch made from hed-standard `main`. The following examples assume that you are in the root of your local repository with its venv activated and that you are releasing 4.0.0, the version in `pyproject.toml`.

**Prepare the release PDF.**

```bash
python scripts/do_spec_release.py prepare 4.0.0
```

Review the staged `releases/` folder, commit, push and open a pull request. After it merges, print the release notes:

```bash
python scripts/do_spec_release.py notes 4.0.0
```

Then create the tag and the GitHub release by hand in the GitHub web interface, pasting the release notes it prints as the description and attaching `releases/hed-specification-4.0.0.pdf`. Finally, a HED maintainer adds the same PDF to the hed-specification Zenodo record by hand; Zenodo does not do this automatically.
