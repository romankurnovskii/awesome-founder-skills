# How to Use: Startup Framing Screener

## What This Skill Does

Measures how a startup words its pitch — its name, one-line statement, and
website URL — and reports where each measurement sits against published
benchmark bands. It does **not** judge the business.

## Where the numbers come from

> Saruggia, A. M. G., & Germano, S. (2026). *Predicting Startup Exit from Textual
> Descriptors: A Computational Linguistics Framework.* arXiv:2608.00045.
> <https://arxiv.org/abs/2608.00045> · DOI: 10.48550/arXiv.2608.00045

The study analysed **7,419 startups over 20 years** (Techstars + Y Combinator),
**770 exits (10.38% baseline)**, engineering **850 features**. Logistic
Regression reached F1 0.48 / recall 0.55 on all features. It found that
*optimised* densities of hyping markers — especially common words, nouns, verbs,
and adjectives — associate with higher exit probability, while excessive
statement or name length associates with lower probability.

This skill is an **independent implementation**, not the authors' software. The
study does not publish its dictionaries, its trained coefficients, or its
probability threshold, so the shipped marker lists are a reconstruction and the
skill reports band membership rather than a probability.

## Limitations

1. Validated only on US accelerator cohorts (Techstars + YC) — may not transfer
   to other regions or sectors.
2. Dictionary-based; misses emerging or sector-specific hype language.
3. Low recall by design — roughly 0.5–1.7% at precision 1.0. High specificity.
4. Correlation, not causation. Hype may signal investor preference rather than
   startup quality; the study says this explicitly.
5. Purely textual — no financials, team, or market data.
6. **Not investment advice**, and not a substitute for professional judgement.

## When to Use

- Checking a one-liner or name before an accelerator application.
- Auditing whether a pitch reads as over-hyped or under-powered.
- Deciding whether a statement is too technical or too long.
- Comparing two candidate taglines or names.
- Triaging many startup descriptions by narrative framing.

## Prompt Examples

```
Screen my startup framing. Name: Etemaro.
Statement: "Autonomous DLMM execution for Solana liquidity providers."
Website: https://etemaro.com

Is my pitch too hyped? Here is my one-liner: "..."

Compare these two taglines against the benchmark bands: A) ... B) ...
```

## Running It Directly

```bash
python3 scripts/screen.py \
  --name "Etemaro" \
  --statement "Autonomous DLMM execution for Solana liquidity providers." \
  --website "https://etemaro.com"

python3 scripts/screen.py --name X --statement Y --website Z --json
python3 scripts/screen.py --name X --statement Y --website Z --output report.txt

# capability check - what works, what is optional, and how to enable it
python3 scripts/screen.py --doctor
```

## What You Get

1. **Hyping Score (reconstructed)** — a relative index, with per-marker
   contributions. Compare across candidate texts, never against a fixed cutoff.
2. **Banded features** — value, verdict (`BEST` / `MIN` / `MAX` / `OUT_OF_BAND`),
   the best band, and the delta where one is published.
3. **Binary flags** — `.com`, founding-year mention, website mention, location
   mention, name/website length match.
4. **Moves toward the best bands** — concrete edits with targets.

## Tips

- Use the **exact** text from the application. Tidying it defeats the purpose.
- Common-word density is best at its maximum (68–82%), so plain language scores
  well; jargon-heavy text trades that away.
- Acronyms and nouns are the exception — both are best at their **minimum**.
- Buzzword density peaks in a **mid** band (30–36%), not at the extreme. More
  hype is not better.
- Without `spacy` installed, the four POS densities report as *not measured*.
  That is **expected and not an error** — the other seven features are complete.
  Run `--doctor` to confirm status; never probe with a bare import, which just
  prints a traceback. To enable them without installing anything globally, ask
  the user first:
  `pip install spacy && python -m spacy download en_core_web_sm`.
- `Frequent Word Density` uses a standard English frequency list, since the study
  does not publish its own. Treat it as an approximation.
- **Website length is measured on the bare host**, not on the string you typed.
  `https://etemaro.com`, `etemaro.com`, and `http://www.etemaro.com/` all measure
  **11 characters**. You cannot move this band by reformatting a URL — only by
  changing the actual domain.
- For batch or repeated screening, use `from screen import run_screen` and load
  the dictionaries once with `load_markers()`. See `SKILL.md`.

## License

MIT for the code. The study is CC BY-NC-ND 4.0; see
[`references/attribution.md`](references/attribution.md) before redistributing.
