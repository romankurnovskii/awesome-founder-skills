---
name: startup-framing-screener
description: "Audit how a startup describes itself: measure its pitch text and report where each feature sits against published benchmark bands, with the edits that move it toward the best band. Measures four marker densities in the statement (buzzwords, jargon, acronyms, common words) plus adjective, verb, noun, and value density when spaCy is installed; lengths of the name, statement, and website; and binary signals including a .com domain, founding-year mention, and location mention. Use when someone wants their pitch, one-liner, tagline, name, or website checked before applying to an accelerator such as YC, Antler, or Techstars; asks 'is my pitch too hyped', 'does this read too technical', 'review my one-liner', 'screen this startup', or 'check my positioning'; or wants two candidate taglines or names compared. Audits wording only: it does not judge the business, market, traction, team, or odds of success, and never outputs a success probability."
metadata:
  version: 1.0.0
  license: MIT
  research: arXiv:2608.00045
---

# Startup Framing Screener

Measure how a startup words its pitch, and report where each measurement sits
against published benchmark bands.

## What it measures

| Group | Features |
| :--- | :--- |
| Marker density in the statement | buzzwords, jargon, acronyms, common words |
| POS density (needs spaCy) | adjectives, verbs, nouns, values |
| Length | name, statement, website (bare host) |
| Binary signals | `.com` domain, founding-year mention, website mention, location mention, name/website length match |

Each feature has a published **best band**, plus lower and upper bands with a
directional delta. The screen reports which band the text lands in and how far
it is from the best one.

## Procedure

1. **Collect all three inputs before running anything.** Required: `--name`,
   `--statement` (the pitch sentence), `--website`.

   - **If any is missing, stop and ask for it.** Name exactly which fields you
     need, in one short message. Do not run the script first, and do not proceed
     on a guess.
   - **Never invent or substitute an input.** No placeholder names, no guessed
     domains (`example.com`, `<name>.com`, `<name>.ai`), no tidied-up wording.
     A guessed domain silently corrupts every website feature.
   - **Only exception:** if the user says a field does not exist yet — no site
     registered, no name chosen — run without it. The script marks the dependent
     features *not measured*, and you must report which ones and why.
   - Use the founder's **raw** wording, exactly as written in the pitch.

2. **Run the script. Do not estimate any feature by hand.**

   ```bash
   python3 scripts/screen.py \
     --name "<name>" \
     --statement "<one-line pitch>" \
     --website "<https://...>"
   ```

   Add `--json` for machine-readable output, `--output <file>` to save a report.

3. **Read the report's three sections in order** — Hyping Score, banded features,
   binary flags. `NOT MEASURED` lists features the script could not compute;
   carry that through as unknown rather than filling it in.

4. **Lead the answer with the biggest band gaps.** Rank by the largest upside
   first, then by the most damaging upper-band overshoot. Name the feature, its
   current value, its verdict, its best band, and the delta where one is
   published.

5. **Give concrete rewrites.** For each gap from step 4, propose the specific
   edit — cut acronyms, compress a 40-word statement toward 2–37 words, move
   buzzword density up into the 30–36% band, shorten the domain. Then re-run the
   script on the rewrite and show the before/after band movement.

6. **Close with the ceiling sentence, verbatim:**

   > These are benchmark bands from one accelerator dataset, not success
   > predictors. At the study's precision-1.0 operating point, recall is
   > 0.005–0.017 — a clean screen means "not flagged", never "will succeed".

## Output contract

Every answer contains all four:

1. A table of every measured feature: current value, verdict (`BEST` / `MIN` /
   `MAX` / `OUT_OF_BAND`), best band, delta.
2. The ranked list of edits from largest impact.
3. The rewritten pitch text, if the user supplied text to improve.
4. Any feature you could not measure, and why — missing input, or no POS tagger.
5. The ceiling sentence above.

## Rules

- **Never probe for optional packages yourself.** Do not run
  `python3 -c "import spacy"` or any ad-hoc dependency check. A missing optional
  package is **not an error** — a bare import emits a traceback that looks like a
  failure and wastes context. Run `python3 scripts/screen.py --doctor` instead: it
  reports exactly what is and is not available and exits 0. Then carry on with the
  screen; the core features are unaffected.
- **Never install anything without asking.** If the user wants the four POS
  features, offer the one-line install from `--doctor` output and let them decide.
- **Never recommend retyping an input to change a score.** Inputs are normalised
  before measurement — a website is reduced to its bare host, so
  `https://etemaro.com`, `etemaro.com`, and `http://www.etemaro.com/` all measure
  identically at 11 characters. An edit must change something real about the
  startup's wording or its actual domain, never the formatting of the string you
  feed in. Advising "write your URL without `https://` to escape a penalty band"
  is measurement-gaming and is forbidden.
- **Rule out measurement artifacts before calling something a gap.** If a feature
  is off-band, first confirm the value is not an artifact of how the input was
  typed or how the dictionary happens to tokenise it. Say "not applicable" rather
  than inventing an edit.
- **Ask for missing inputs; never fabricate them.** A missing `--name` or
  `--website` is a question to put to the user, not a gap to fill. If you had to
  run without one, state which features went unmeasured.
- **Never output a success probability.** The underlying study does not publish
  its trained coefficients, so no calibrated probability can be computed. Produce
  band verdicts and deltas only.
- **Never fill in a `NOT MEASURED` feature.** If spaCy is absent, the four POS
  densities stay unknown. Say so.
- **Say "benchmark band", not "optimal value".** These are correlations observed
  in one dataset, not prescriptions.
- **Call the marker lists a reconstruction.** Their source paper does not publish
  its dictionaries, so the shipped lists approximate them. Use the wording
  "within the benchmark band", never "the study's exact value".
- **Decline business questions.** Market size, unit economics, pricing, team, and
  traction are out of scope. Say the screen audits wording only.
- **Do not read the script's log files into context.** They are for debugging.

## Reference files

- `references/paper-thresholds.md` — every band, delta, and benchmark figure,
  with the source tables. Load this when a user asks where a number comes from.
- `references/hyping-markers.md` — the marker lists. Edit these to tune for a
  sector or a specific application process.
- `references/attribution.md` — citation and redistribution requirements.

## Scripts

- `scripts/screen.py` — symlink to `screen.v1.py`. Deterministic, stdlib only,
  no network calls, no LLM calls. Logs to `scripts/.logs/`.
- **Capability check.** `python3 scripts/screen.py --doctor` reports Python
  version, dictionary counts, and which optional features are available. It exits
  0 whether or not the optional POS tagger is installed. This is the only
  supported way to check dependencies.
- **Programmatic use.** For batch or repeated screening use the supported entry
  point rather than reaching into internals:

  ```python
  from screen import run_screen, load_markers

  markers = load_markers()  # parse dictionaries once
  for name, stmt, site in candidates:
      report = run_screen(name, stmt, site, markers)
      report['banded_features']  # per-feature verdicts
      report['hyping_score']['score']  # reconstructed relative index
  ```

  Do **not** call `measure` or `build_report` directly — `run_screen` is the
  stable interface.
