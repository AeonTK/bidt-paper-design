# scientific-writing

A Copier template for academic paper writing. Provides a structured workspace with writing guidelines, a working LaTeX build, and Python figure generation — all kept up to date across papers via `copier update`.

## Creating a new paper

Install Copier once (requires [uv](https://docs.astral.sh/uv/)):

```bash
uv tool install copier
```

Generate a new paper:

```bash
copier copy gh:AeonTK/scientific-writing my-paper --trust
cd my-paper
git add .
git commit -m "Initial paper from template"
git remote add origin <your-paper-repo-url>
git push -u origin main
```

Edit `submissions/draft/main.tex` to fill in your title, author, and institution.

## Updating a paper when the template changes

From inside your paper repo:

```bash
git add . && git commit -m "Checkpoint before template update"
copier update --trust --defaults
```

Copier fetches the latest template version, diffs it against the version your paper was generated from, and applies only what changed. Your content (`paper/sections/`, `paper/bibliography.bib`, etc.) is never touched.

If there are conflicts, Copier marks them inline (like `git merge`). Review and resolve them, then commit.

### Opting out of a specific file update

Some files are always synced from the template (e.g. `CLAUDE.md`, `SKILLS.md`, `guidelines/`). If you want to keep your own version of one of them in a specific paper — for example, you've added project-specific writing notes to `guidelines/style.md` — you can undo just that file after the update:

```bash
copier update --trust --defaults
git checkout -- guidelines/style.md   # restore your version of this file
git commit -m "Apply template update, keep local style guidelines"
```

This is manual — you'll need to repeat it each time you update. There is no set-and-forget per-file opt-out; the opt-out lives in the template's `_skip_if_exists` list, which applies to all papers.

## What gets updated vs. what stays yours

| Path | On `copier update` |
|---|---|
| `guidelines/` | Updated |
| `templates/` | Updated |
| `CLAUDE.md`, `SKILLS.md` | Updated |
| `submissions/draft/llncs.cls`, `splncs04.bst` | Updated |
| `submissions/draft/main.tex` | Created once, never overwritten (edit manually) |
| `paper/sections/` | Never touched |
| `paper/bibliography.bib` | Never touched |
| `paper/figures/` | Never touched |
| `assets/python/fig_example.py`, `pyproject.toml`, `.python-version` | Never touched |
| `notes/`, `reviews/` | Never touched |

## Updating the template itself

```bash
# Make your changes, then:
git add .
git commit -m "describe the change"
git tag v0.X.0
git push origin main v0.X.0
```

**Always tag before testing.** Copier copies from the latest tag, not the latest commit. Untagged commits are invisible to `copier copy` and `copier update`.

## Creating a conference submission

1. Copy style files from `templates/<style>/` into `submissions/<conference-year>/`
2. Write `submissions/<conference-year>/main.tex` using the pattern in `CLAUDE.md`
3. Compile with LaTeX Workshop (`Ctrl+Alt+B`)

The working draft (`submissions/draft/`) uses LNCS and is always up to date. Use it whenever the target venue is not yet decided.
