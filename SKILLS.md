# SKILLS.md

Reusable prompts for Claude Code in this repository.

---

## Skill: Create a figure script

Use this prompt when you need a new Python figure script.

```
Create a figure script called `<name>.py` in `assets/python/` that generates <description of figure>.

- Output the figure to `../../paper/figures/<name>.pdf`
- Use matplotlib with figsize appropriate for a single-column or double-column LNCS page
- Run it with: cd assets/python && uv run <name>.py
```

---

## Skill: Compile PDF

Compile `submissions/draft/main.tex` into `main.pdf`.

**Preferred — latexmk (handles reruns and bibliography automatically):**

```bash
cd submissions/draft && latexmk -pdf main.tex
```

**Alternative — manual pdflatex + bibtex sequence:**

```bash
cd submissions/draft && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

**Clean build artifacts (without deleting the PDF):**

```bash
cd submissions/draft && latexmk -c
```

**Notes:**

- VSCode LaTeX Workshop uses the same `latexmk` binary under the hood; the CLI commands above are equivalent to the "Build LaTeX project" action (`Ctrl+Alt+B`) in LaTeX Workshop.
- To find where `latexmk` is installed: `where latexmk` (Windows) or `which latexmk` (Mac/Linux).
- Must `cd` into the submission folder before compiling — section and figure paths in `main.tex` are relative to that folder.
- Output: `submissions/draft/main.pdf`
- On compile errors, check `submissions/draft/main.log` for details.
- A bibtex warning about empty bibliography is expected while `paper/bibliography.bib` has no entries — the PDF still compiles.

---

## Skill: Review a paper section

Use this prompt when you want feedback on a section's writing quality.

```
Review `paper/sections/<section>.tex` against the writing guidelines.

1. Read `guidelines/style.md` and `guidelines/structure.md` first.
2. Read the section.
3. Give concrete, prioritized feedback on:
   - Argument structure (topic sentences, warrants, transitions)
   - Sentence-level issues (stress position, passive overuse, filler words)
   - Tense consistency
   - Any structural problems specific to this section type
4. Suggest specific rewrites for the worst offenders — do not rewrite the whole section unless asked.
```

---

## Create or adapt a conference submission

Use this prompt when you want to create a new submission folder for a specific conference, or adapt an existing one to a different template.

```
Create a submission for <conference-name-year> using the template in `templates/<style>/`.

Steps:
1. Read `templates/<style>/samplepaper.tex` (and any readme or PDF in that folder) to extract
   the conference requirements: document class options, required packages, author/affiliation
   format, anonymous submission rules, page limits, bibliography style, any forbidden packages
   or mandatory sections.
2. Read all files in `paper/sections/` to understand the current content.
3. Create `submissions/<conference-name-year>/` and copy the required style files from
   `templates/<style>/` into it.
4. Write `submissions/<conference-name-year>/main.tex` that:
   - Uses the correct document class and options for this conference
   - Inputs all sections from `../../paper/sections/`
   - Points figures to `../../paper/figures/`
   - Points bibliography to `../../paper/bibliography`
   - Applies any conference-specific formatting (anonymous mode, page limit hints, etc.)
5. Report any requirements that could not be satisfied automatically and need manual attention
   (e.g. page limit exceeded, required sections missing from paper/sections/).
```
