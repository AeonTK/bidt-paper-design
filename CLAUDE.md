# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Writing guidelines

Always read the relevant guideline(s) before acting:

| Task | Read before starting |
|---|---|
| Writing or editing the abstract | `guidelines/abstract.md` |
| Writing or editing any paper section | `guidelines/style.md` + `guidelines/structure.md` |
| Creating or editing a figure script | `guidelines/figures.md` |
| Reviewing or giving feedback on writing | `guidelines/style.md` + `guidelines/structure.md` |

**Guideline contents:**
- `guidelines/abstract.md` — structure (5 elements), tense rules, acronym rules, common mistakes
- `guidelines/figures.md` — file format, typography, review loop, captions, accessibility, data storytelling (5D)
- `guidelines/structure.md` — paper sections, title, intro/conclusion steps, argumentation (Toulmin), narrative (ABT/three-act)
- `guidelines/style.md` — sentence structure (SVOA, topic/stress), emphasis, verb tenses, voice, paragraph rules, punctuation, golden rules

## Project purpose

Academic paper writing workspace. Content is written once in `paper/` and submitted to conferences by creating self-contained builds in `submissions/`.

## Structure

```
paper/                      ← paper content, template-agnostic
  sections/                 ← one .tex file per section
    abstract.tex
    introduction.tex
  figures/                  ← all images (EPS, PDF, PNG)
  bibliography.bib

assets/                     ← source materials for figures
  python/                   ← Python scripts that generate figures (uv project)
  diagrams/                 ← source files for diagrams (draw.io, Inkscape, etc.)

notes/                      ← informal notes, ideas, related work summaries

reviews/                    ← feedback received, named as <source>-<date>/
  draft-supervisor-2026-03/
  conference-name-2026/

templates/                  ← unmodified official templates for reference
  lncs/
  ieee/                     ← add as needed
  acm/

submissions/                ← one folder per conference submission
  draft/                    ← permanent working build (LNCS, always up to date)
    main.tex
    llncs.cls
    splncs04.bst
    out/                    ← build artifacts (gitignored)
  <conference-year>/        ← created when targeting a specific venue
    main.tex
    <style files>
    out/
```

## Day-to-day writing

Open `submissions/draft/main.tex` in VS Code and compile with LaTeX Workshop (`Ctrl+Alt+B`). This is the permanent working build using LNCS — use it whenever the target conference is not yet decided.

When adding a new section: create the file in `paper/sections/` and add a corresponding `\input` line in `submissions/draft/main.tex` (and later in any conference submission).

## Creating a conference submission

1. Create `submissions/<conference-year>/`
2. Copy the relevant style files from `templates/<style>/` into it
3. Write `main.tex` using the pattern below
4. Open `main.tex` in VS Code and compile with LaTeX Workshop

### main.tex pattern

```latex
\documentclass[runningheads]{llncs}

\usepackage[T1]{fontenc}
\usepackage{graphicx}
\graphicspath{{../../paper/figures/}}

\begin{document}

\title{Paper Title}
\author{...}
\maketitle

\begin{abstract}
\input{../../paper/sections/abstract}
\end{abstract}

\input{../../paper/sections/introduction}
% \input{../../paper/sections/...}

\bibliographystyle{splncs04}
\bibliography{../../paper/bibliography}

\end{document}
```

## Key LNCS conventions

- `\author{}` uses `\inst{N}` for institution index and `\orcidID{}` for ORCID
- `\authorrunning{}`: abbreviate to "F. Author et al." for 3+ authors
- Heading levels: `\section`, `\subsection` are numbered; `\subsubsection` and `\paragraph` are unnumbered run-in headings. Max 4 levels.
- Figure captions below; table captions above
- Math environments: `theorem`, `proof`, `definition`, `lemma`, `proposition`, `corollary`, `remark`, `example`
- End matter: `\begin{credits}` with `\subsubsection{\ackname}` and `\subsubsection{\discintname}` (both required by Springer)
- Bibliography: prefer `\bibliographystyle{splncs04}` + `\bibliography{...}` over inline `thebibliography`

## Adapting to a new conference template

When asked to adapt the paper to a new template:
1. Read the conference's `samplepaper.tex` from `templates/<style>/` to understand required structure and commands
2. Read all files in `paper/sections/` for current content
3. Create `submissions/<conference-year>/main.tex` that bridges them, adjusting only formatting/metadata — not content
