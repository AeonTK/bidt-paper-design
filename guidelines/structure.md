# Guideline: Paper Structure

## Paper sections overview

| Section | Purpose | Primary audience | Core content |
|---|---|---|---|
| **Title** | Attract the right readers | Everyone | 10±3 words; topic + method/contribution |
| **Abstract** | Decide whether to read | Skimmers, reviewers | Rationale → Objective → Methods → Results → Implications |
| **Keywords** | Discoverability | Search engines, indexers | 4–6 terms not already in the title |
| **Introduction** | Orient and motivate | General readers | Context → gap → purpose → preview |
| **Related Work** | Position the paper | Experts in the field | What exists, what it lacks, how this work differs |
| **Methods** | Enable replication | Practitioners, reviewers | Study design, materials, procedure — enough to reproduce |
| **Results** | Report findings | All readers | Data, figures, tables — no interpretation yet |
| **Figures & Tables** | Support results visually | All readers | See `figures.md` |
| **Discussion** | Interpret findings | Specialists | What results mean, limitations, relation to prior work |
| **Conclusion** | Summarize and project | Skimmers, future readers | Summary → implications → open questions |
| **Acknowledgements** | Credit support | Institutional readers | Funding, collaborators, tools |
| **References** | Support claims | Anyone following up | Formatted per venue style |

## Conference paper anatomy (Simon Peyton Jones model)

A tight conference paper allocates space roughly as follows. The reader counts show how many of the ~1000 people who see the title actually read each section — write accordingly.

| Part | Approx. length | Goal | Typical reach |
|---|---|---|---|
| Title | — | Sell the work in a phrase | ~1000 readers |
| Abstract | 4 sentences | Problem → existing approaches → your idea → implications | ~100 readers |
| Introduction | ~1 page | Broad context, gap, contribution list, paper map | ~100 readers |
| The Problem | ~1 page | Precise problem statement with an example | ~10 readers |
| The Idea | ~2 pages | Key insight — can be understood without full details | ~10 readers |
| The Details | ~5 pages | Full technical content | ~3 readers |
| Related Work | ~1–2 pages | Honest comparison with alternatives | ~10 readers |
| Conclusions | ~0.5 pages | One-paragraph summary + future work | — |

Write the introduction last — it is the hardest section and is best written once the paper is stable.

## Title

- **Length:** 10 ± 3 words. Shorter titles get more citations on average.
- **Reach:** The title is the only part that appears in tables of contents, databases, and reference lists — it is the most frequently read part of any paper. Every word choice matters.
- **No** periods, dashes as separators, or unnecessary punctuation.
- **Colon** is acceptable for subtitle: `Main claim: elaboration or scope`.
- **Capitalization (title case):**
  - *Capitalize:* nouns, pronouns, verbs, adjectives, adverbs, subordinate conjunctions (*As*, *Because*, *Although*), and prepositions that are part of a phrasal verb (*Brush Up* Your English).
  - *Do not capitalize:* articles (*a*, *an*, *the*), coordinate conjunctions (*and*, *but*, *or*, *for*, *nor*), *to* in infinitives, or prepositions — unless they are the first or last word.
  - *Style guide note:* IEEE and APA capitalize prepositions of more than three letters; Chicago keeps all prepositions lowercase. Follow your venue's style guide when in doubt.
- Make the topic and contribution identifiable from the title alone.

## Typical paper structures by research type

Three section-order patterns cover most academic papers:

| Pattern | Section order | Typical for |
|---|---|---|
| **Empirical (IMRD)** | Abstract → Introduction → Methods → Results → Discussion | All disciplines; reproducibility is the primary concern |
| **Methodology / Application** | Abstract → Introduction → Results → Discussion → Methods | Chemistry, biochemistry; application-oriented research; contribution is the result, not the procedure |
| **Comparative / Review** | Abstract → Introduction → Methods → [Results + Discussion] × n → Conclusions | Comparative studies, review papers; each topic gets its own Results + Discussion block |

Choose the pattern your venue and research type expect. Within the Comparative/Review pattern, each Results+Discussion pair covers one thematic cluster before a unified Conclusions section draws them together.

## Introduction — functional steps (funnel structure)

Write the introduction as a narrowing funnel:

1. **General context** — broad field or domain; why it matters to society or science.
2. **Theoretical background** — concepts the reader needs to follow the argument.
3. **State of the art** — what has already been done; key prior work.
4. **Relevance** — why this area is active/important right now.
5. **Gap in knowledge** — what is missing, unsolved, or poorly understood.
6. **Purpose / Research question** — what this paper does to address the gap.
7. **Approach / Delimitations** — how, and what is deliberately out of scope.
8. **Preview** — brief map of the paper sections.

> The gap (5) and purpose (6) are the pivot of the introduction — everything before leads to them, everything after follows from them.

## Conclusion — functional steps (trapezoid structure)

1. **Review** — briefly restate the problem and approach.
2. **Summary of results** — what was found.
3. **Coupling to research question** — explicitly answer the RQ stated in the introduction.
4. **CONCLUSION** — the main claim; the single most important takeaway.
5. **Comparison with prior studies** — how results relate to existing work.
6. **Possible conflicts / limitations** — honest acknowledgement of constraints.
7. **Further work** — what remains open or should be done next.
8. **Outlook** — broader implications or vision.

Do not introduce new results in the conclusion.

## Aristotle's pillars of persuasion

Every persuasive text — including a scientific paper — rests on three pillars:

| Pillar | Mode | In academic writing |
|---|---|---|
| **Logos** | Logical appeal | Coherent structure, rigorous data, sound methodology, valid inference |
| **Ethos** | Credibility appeal | Proper citation, positioning against prior work, transparent limitations, expertise |
| **Pathos** | Narrative/emotional appeal | Compelling motivation, concrete examples, engaging storytelling |

All three must be present. A paper strong only in Logos (data-heavy, no narrative) loses readers. A paper relying on Pathos without Logos is unscientific. Ethos is built through citation practice, honest acknowledgement of limitations, and a clear related work section.

## Argumentation: the Toulmin model

Every scientific claim should be supportable with this structure:

A **Claim** is supported by **Data** (the evidence), connected via a **Warrant** (the logical bridge "because X, therefore Y"), which is itself grounded by **Backing** (established theory or principles). The claim's certainty is limited by a **Qualifier** ("probably", "in most cases"), and a **Rebuttal** states the conditions under which the claim does not hold.

- **Claim** — the assertion being made.
- **Data** — evidence that supports it (measurements, citations, examples).
- **Warrant** — the logical bridge from data to claim ("because X, therefore Y").
- **Backing** — support for the warrant itself (theory, established principles).
- **Qualifier** — hedging language that limits the claim's certainty.
- **Rebuttal** — acknowledged exceptions or counter-conditions.

A paragraph that makes a claim without a warrant is an assertion, not an argument.

## Paragraph argumentative structure

A well-structured paragraph follows this sequence:

1. **Topic sentence** — states the paragraph's claim or main point.
2. **Definition** — defines key terms if necessary.
3. **Focus** — narrows to the specific aspect being argued.
4. **Theory / Evidence** — presents supporting data, citations, or reasoning.
5. **Example** — concrete illustration of the point.
6. **Exception** — acknowledges limits or counter-cases (builds credibility).
7. **Closing sentence** — restates the point and provides a transition.

Every sentence in the paragraph should serve the topic sentence. If a sentence does not, move or delete it.

## Storytelling: narrative structure

Scientific papers are persuasive narratives, not just reports. Use narrative structure to hold the reader's attention.

### ABT structure (And–But–Therefore)

Frame any argument or abstract as:

> "[Context] **And** [more context]… **But** [problem/tension/gap]… **Therefore** [your work/solution/contribution]."

This is the minimal narrative unit. If you cannot state your paper in ABT form, the argument is not clear yet.

### Three-act structure

| Act | Label | Content |
|---|---|---|
| 1 | Situation | Context, background, state of the art — the world as it is |
| 2 | Complication | The problem, gap, conflict — why the situation is unsatisfactory |
| 3 | Resolution | Your contribution — what you did and what it means |

The introduction maps naturally onto Act 1 + Act 2; the body and conclusion map onto Act 3.

Apply this structure not just to the paper as a whole but to individual sections and arguments.
