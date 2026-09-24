# Research Attribution & Licensing

This skill is a **derived work**. Read this before redistributing or commercialising it.

## The paper

> Saruggia, A. M. G., & Germano, S. (2026). *Predicting Startup Exit from Textual Descriptors: A Computational Linguistics Framework.* arXiv:2608.00045 (v4, 23 Sep 2026).
> https://arxiv.org/abs/2608.00045 · DOI: [10.48550/arXiv.2608.00045](https://doi.org/10.48550/arXiv.2608.00045)

```bibtex
@misc{saruggia2026startupexit,
  title  = {Predicting Startup Exit from Textual Descriptors: A Computational Linguistics Framework},
  author = {Saruggia, Alberto M.G. and Germano, S{\'e}bastien},
  year   = {2026},
  eprint = {2608.00045},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi    = {10.48550/arXiv.2608.00045}
}
```

The paper's own license, as displayed on arXiv, is **CC BY-NC-ND 4.0** — Attribution-NonCommercial-NoDerivatives.

## What this skill takes from the paper

| Item | Nature | Status |
| :--- | :--- | :--- |
| Thresholds, Exit Ratios, Exit Deltas | Published numeric results (Table VII, Table VIII) | Facts reported from the paper, cited |
| Feature importance weights | Published numeric results (Table V) | Facts reported from the paper, cited |
| Model benchmark scores | Published numeric results (Table IX, Table X) | Facts reported from the paper, cited |
| Hyping Score formula | A published mathematical formula | Implemented as described, cited |
| Acronym / buzzword / jargon dictionaries | **Not published by the paper** | Independently reconstructed — see `hyping-markers.md` |
| Frequent-word list | **Not published by the paper** | Standard English frequency list, an approximation |
| Trained model coefficients | **Not published** | Not implemented — cannot be reproduced |

**No text from the paper is reproduced verbatim.** Only numeric results and the mathematical formula are restated, with citation.

## Licensing consequence — decide before shipping

The short answer: **you can build and ship this skill, and MIT is appropriate for it.**

Copyright protects *expression* — the paper's prose, its figures, its specific
wording and layout. It does **not** protect:

| Not protected by copyright | In this skill |
| :--- | :--- |
| Ideas, methods, systems, procedures | The computational-linguistics screening method |
| Facts and data | Exit Ratios, Exit Deltas, F1 / recall / AUC figures |
| Mathematical formulas | The Hyping Score formula |
| Your independent reimplementation | Everything in `scripts/` — original code |

Reimplementing a published method and reporting its published numbers **with
citation** is standard scientific practice. It does not create a derivative work
of the paper. CC BY-NC-ND governs the paper's *material*; it does not reach your
independent implementation of its method.

**So no licence change is required**, provided the repository:

- ships only original code and original prose,
- presents the figures as facts **with citation**,
- does not reproduce the paper's text, figures, or table layouts verbatim.

### Where NC and ND would actually bite

| Action | Status |
| :--- | :--- |
| Writing your own implementation of the method | ✅ Fine — methods are not copyrightable |
| Reporting published figures with citation | ✅ Fine — facts |
| Quoting a short passage for commentary | ✅ Fine — subject to attribution |
| Copying the paper's tables wholesale into a file | ⚠️ Reproduces expression — keep minimal, quote, attribute |
| Redistributing the paper or a modified version of it | ❌ ND and NC apply directly |
| Selling the paper's content | ❌ NC applies directly |

`references/paper-thresholds.md` restates figures in its own structure with
citation; it does not reproduce the paper's tables or prose verbatim, which keeps
it on the safe side of that line.

### Recommended posture

1. **Keep MIT.** Add a short `NOTICE` crediting the paper. CC BY requires
   attribution if any material is reproduced, and it is correct practice anyway.
2. **Never copy the paper's text, figures, or table layouts verbatim.**
3. **Never present the reconstructed dictionaries as the authors' instrument.**
4. If you ever reproduce substantial excerpts, apply a `LICENSE-CC-BY-NC-ND`
   notice to that single file and document the split.

> This is practical guidance, not legal advice. The authors' arXiv licence could
> change if the paper is later published in a journal, and a patent — unlikely for
> this kind of work — would be a separate question.

## Required attribution in any redistribution

Any copy, fork, or packaged distribution of this skill must keep:

1. The paper citation above, with the arXiv ID `2608.00045`.
2. A statement that this is an independent implementation, not the authors' software.
3. A statement that the dictionaries are a reconstruction, not the paper's original lists.
4. The limitations section from `how_to_use.md`, unaltered.

## Academic integrity note

If this skill is used in a paper, thesis, or accelerator application, cite **the paper** for the methodology and **this skill** only for the implementation. Do not present the reconstructed dictionaries as the paper's own instrument — that would misattribute the research contribution.
