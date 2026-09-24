# Verified Thresholds from arXiv:2608.00045

Source: Saruggia, A.M.G. & Germano, S. (2026). *Predicting Startup Exit from Textual Descriptors: A Computational Linguistics Framework.* arXiv:2608.00045v4.

Every number below was transcribed from the published PDF (v4, 23 Sep 2026). Do not substitute numbers from memory or from a secondary summary.

> **Global Exit average = 10.38%.** Every `Exit Delta` below is measured against this baseline:
> `Exit Delta = Exit Ratio(feature value) − 10.38%`

---

## 1. Continuous density measures — TABLE VIII

Each feature is normalised to [0,1], then binned. MIN = lowest band, MAX = highest band, BEST = the band with the highest Exit Delta.

| Density measure | MIN band | Exit Ratio | Exit Delta | MAX band | Exit Ratio | Exit Delta | BEST |
| :--- | :--- | ---: | ---: | :--- | ---: | ---: | :--- |
| Acronym Density | 0–1% | 11.2% | **+7.9%** | 10–12% | 10.3% | −0.3% | **MIN** |
| Buzzword Density | 0–3% | 15.3% | +47.5% | 36–45% | 10.5% | +1.4% | **30–36%** |
| Jargon Word Density | 0–3% | 10.8% | +3.7% | 21–27% | 19.7% | **+89.9%** | **MAX** |
| Frequent Word Density | 0–7% | 18.8% | +80.9% | 68–82% | 28.2% | **+172.1%** | **MAX** |
| Adjective Density | 0–4% | 12.5% | +20.1% | 29–36% | 22.8% | **+119.6%** | **MAX** |
| Noun Density | 12–22% | 23.4% | **+125.8%** | 100.0% | 20.8% | +100.2% | **MIN** |
| Value Density | 0–2% | 10.9% | +4.9% | 13–17% | 17.1% | +64.5% | **MAX** |
| Verb Density | 0–5% | 19.6% | +88.7% | 45–54% | 23.1% | **+122.4%** | **MAX** |

**Reading this table:** high-exit narratives do *not* maximise every marker. Acronyms and nouns do best at their MINIMUM; buzzwords peak in a mid band (30–36%), not at the extreme. This is the paper's central "selective optimisation" finding.

## 2. Continuous length measures — TABLE VIII

| Length measure | MIN band | Exit Ratio | Exit Delta | MAX band | Exit Ratio | Exit Delta | BEST |
| :--- | :--- | ---: | ---: | :--- | ---: | ---: | :--- |
| Statement Length | 2–37 words | 11.6% | **+11.7%** | 151–180 words | 8.1% | −22.1% | **MIN** |
| Name Length | 3–6 chars | 11.1% | **+7.2%** | 15–19 chars | 7.9% | −23.6% | **MIN** |
| Website Length | 3–4 chars | 11.4% | +9.8% | 18–20 chars | 1.6% | −84.7% | **16–17 chars** |

Brevity wins on every length measure. Website Length has the single most punishing MAX band in the study (−84.7%).

> **Implementation note — Website Length.** The paper does not state whether this
> feature measured the raw URL field or the bare domain. This skill measures the
> **bare host** — scheme, `www.`, path, query, credentials, and port removed — so
> the value cannot change with input formatting. `https://etemaro.com`,
> `etemaro.com`, and `http://www.etemaro.com/` all measure **11 characters**.
> Treat the 16–17 character best band as being in host characters. Measuring the
> raw string instead would make the same domain score differently on typing
> alone, which would let a user "fix" a band by reformatting a URL.

## 3. Binary features — TABLE VII

Counts are for feature = 1.

| Feature (statement / URL variable) | Sample size | Exit Ratio | Exit Delta |
| :--- | ---: | ---: | ---: |
| Location Mention = 1 | 625 | 7.7% | **−26.0%** |
| Location Mention = 0 | 6,794 | 10.6% | +2.4% |
| Founding Year Mention = 1 | 136 | 14.0% | **+34.6%** |
| Website Mention in statement = 1 | 267 | 12.7% | **+22.7%** |
| Website/Name Length equivalence = 1 | 5,110 | 11.6% | +11.8% |
| Website with `.com` = 1 | 4,542 | 12.6% | **+20.9%** |

Mentioning a physical location *hurts*; mentioning the founding year, the website, or using a `.com` helps.

## 4. Selective vs linear optimisation

| Scope | All MIN | All MAX | Optimised (BEST bands) |
| :--- | ---: | ---: | ---: |
| Density measures | 47.4% | 83.7% | **94.4%** |
| Length measures | 9.6% | **−43.5%** | 16.6% |
| Statement variable | 0.3% (all 0) | 10.4% (all 1) | **19.9%** |
| Website URL variable | −29.6% (all 0) | 16.4% (all 1) | 16.4% |

A fully maximised hyped narrative is suboptimal. Balanced brevity beats both extremes.

## 5. Model performance — TABLE IX

Logistic Regression was the best model overall and the one used for Exit prediction.

| Subset | F1 | Precision | Recall | ROC AUC |
| :--- | ---: | ---: | ---: | ---: |
| All Features excl. Embeddings | **0.4830** | 0.4286 | 0.5545 | 0.8576 |
| Context | 0.4703 | 0.3776 | 0.6247 | 0.8603 |
| All Features incl. Embeddings | 0.4306 | 0.3646 | 0.5286 | 0.8379 |
| Descriptors incl. Embeddings | 0.2623 | 0.1686 | 0.5935 | 0.6789 |
| Descriptors excl. Embeddings | 0.2607 | 0.2213 | 0.3182 | 0.6581 |

Adding embeddings *helps* text-only subsets but *harms* hybrid subsets — the paper calls this "semantic dilution".

## 6. High-precision operating point — TABLE X

Threshold selected on validation to target precision = 1.0, then applied to test.

| Subset | Exit precision | Exit recall | Exit F1 |
| :--- | ---: | ---: | ---: |
| All Features excl. Embeddings | 1.0 | 0.017 | 0.032 |
| Context | 1.0 | 0.014 | 0.027 |
| Descriptors incl. Embeddings | 1.0 | 0.010 | 0.020 |
| All Features incl. Embeddings | 1.0 | 0.008 | 0.015 |
| Descriptors excl. Embeddings | 1.0 | 0.005 | 0.010 |

**Read the recall column carefully.** At the paper's precision-1.0 operating point the model finds roughly **0.5%–1.7% of actual exits**. A "clean" screen therefore means "not flagged", never "will succeed".

## 7. Feature importance — TABLE V

| Level | Subset | Feature share | Importance |
| :--- | :--- | ---: | ---: |
| Narrative | Descriptors | 86.3% | 0.7959 |
| Narrative | Context | 13.7% | 0.2041 |
| Variable | Statement | 79.8% | 0.5484 |
| Variable | Industry | 13.3% | 0.0759 |
| Variable | Name | 5.8% | 0.2214 |
| Variable | Website URL | 0.6% | 0.0261 |
| Variable | Country | 0.4% | 0.0178 |
| Semantics | Hyping markers | 79.2% | 0.5454 |
| Semantics | Non-hyping markers | 20.8% | 0.4546 |

Feature-level (top 8, used as `s` weights for the Hyping Score):

| Feature | Importance |
| :--- | ---: |
| Age | 0.1104 |
| Statement Length | 0.0332 |
| Noun Density | 0.0230 |
| Verb Density | 0.0208 |
| Frequent Words Density | 0.0205 |
| Buzzwords Density | 0.0187 |
| Jargon Word Density | 0.0181 |
| Adjective Density | 0.0178 |

## 8. Dataset (for calibration context)

- **7,419 startups**, 20 years, **770 exits (10.38%)**
- 93 countries, 60 industries
- Source: VC-curated datasets (Techstars + Y Combinator) via Kaggle
- 850 features incl. embeddings; **466 excl. embeddings**
  - Descriptors 402 · Context 64 · Statement 372 · Industry 62 · Name 27 · Website URL 3 · Country 2 · Age 1
  - Hyping marker dictionaries: **Acronyms 88 · Buzzwords 145 · Jargon words 127**

## 9. What the paper does NOT publish

These absences constrain what any honest implementation can claim:

| Missing | Consequence |
| :--- | :--- |
| **The three dictionaries** (88/145/127 terms) | The paper describes them as "custom-built" and customisable. Any bundled list is a *reconstruction*, not the paper's list. |
| **Trained logistic-regression coefficients** | No calibrated `P(exit)` can be reproduced. Only band diagnostics are defensible. |
| **The validation-derived probability threshold** | The precision-1.0 operating point cannot be recreated exactly. |
| **The frequent-word list** | "Frequent Word Density" cannot be reproduced exactly; a standard common-word list is an approximation. |
| **POS tagger / embedding model identity** | Adjective, Verb, Noun, and Value densities are not exactly reproducible without the original pipeline. |
| **The unit of "Website Length"** (raw URL vs bare domain) | This skill normalises to the bare host and documents that choice — see the implementation note in §2. |
