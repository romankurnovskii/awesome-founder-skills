---
name: startup-competitors
description: "Conduct investment-grade competitive intelligence and verification for startups and business ideas under a Radical Honesty protocol. Classifies input (idea-only, real company, or hybrid), scopes decision mandate, verifies target ICP and problem, maps competitor universe (direct, indirect, substitutes, incumbents, adjacent) with weighted relevance scoring, executes 3-lens deep research (pricing reverse-engineering, customer sentiment and language mining, GTM signals), triangulates claims across tiered sources (T1-T4, requiring 2+ independent sources for material claims), scores confidence, and produces comparative matrices, 1-page battlecards with 'when they win over you' assessments, and strategic reports. Use when evaluating startup competitors, researching market landscapes, preparing investor memos or pitch decks, doing win/loss analysis, or asking 'who are my competitors', 'compare my startup to X', or 'analyze competitor pricing and GTM'."
metadata:
  version: 1.1.0
---

# Startup Competitors: Investment-Grade Intelligence & Verification

Execute investment-grade competitive intelligence, multi-source verification, and strategic vulnerability mapping for startups and business ideas. Operates under a non-negotiable **Radical Honesty Protocol**: no cheerleading, objective assessment of competitor strengths, explicit 4-tier claim labeling, multi-source triangulation, and mandatory Red/Yellow Flags.

---

## The Radical Honesty Protocol

This skill exists to help founders make sound resource-allocation decisions—not to flatter them:
1. **No Cheerleading**: If a competitor is objectively superior at a feature, compliance tier, or scale, say so directly. Never soften bad news.
2. **The "When They Win Over You" Rule**: Every battlecard must state where the competitor wins and in which deal scenarios they defeat the founder.
3. **Challenge Confirmation Bias**: Deliberately hunt for disconfirming evidence when research appears to validate founder preconceptions.
4. **Treat Inertia as the Primary Competitor**: Recognize that "doing nothing" and manual spreadsheets are usually the largest competitor. Identify the switching trigger.
5. **Standardized 4-Tier Claim Labels**:
   - `[Data]` — Sourced fact with explicit citation.
   - `[Estimate]` — Calculated proxy with stated assumptions (must be a range, never false precision).
   - `[Assumption]` — Unverified belief requiring empirical testing.
   - `[Opinion]` — Analytical or strategic judgment.
6. **Mandatory Flags**: Every deliverable ends with a **Red Flags** (dealbreaker risks) and **Yellow Flags** (monitoring items) section.

---

## High-Level Sequence

```
Stage 0: Input Classification (Idea vs. Real Company vs. Hybrid)
   │
Stage 1: Mandate & Decision Context (1-Page Research Brief)
   │
Stage 1.5: Research Depth Assessment (Light / Standard / Deep)
   │
Stage 2: Subject Definition (Hypothesis Profile vs. Verified Profile)
   │
Stage 3: Target Audience / ICP & Problem Triad
   │
Stage 4: Competitor Universe Definition (Relevance Metric -> 5–10 Shortlist)
   │
Stage 5: Deep Research across 3 Sequential Lenses:
         - Lens 1: Profiles & Pricing Reverse-Engineering
         - Lens 2: Customer Sentiment & Language Mining
         - Lens 3: GTM & Strategic Growth Signals
   │
Checkpoint: Post-Research Alignment Check (1-Message User Validation)
   │
Stage 6: Multi-Source Verification & Triangulation (2+ Independent Sources)
   │
Stage 7: Synthesis & Strategic Pattern-Matching (Connecting the 3 Lenses)
   │
Stage 7.5: Automated Verification Pass (V1 Cross-Deliverable Audit)
   │
Stage 8: Delivery, Battlecards & Continuous Monitoring
```

---

## Procedure

### 1. Classify the Input First (Stage 0)
Competitor identification happens **only after** defining the subject and target audience:

- **Case A: Input is only an Idea / Concept**
  - Do NOT hallucinate a corporate profile.
  - Build a **Hypothesis Profile** with all assumptions labeled `[Assumption]`.
  - Hypothesize target audience, willingness-to-pay, and primary pain point.
  - Competitors are defined primarily as: manual workarounds, spreadsheets, internal tools, and adjacent platforms that could ship the feature.
  - Mark baseline confidence as **LOW** or **MEDIUM** until primary validation occurs.

- **Case B: Input is a Real Company / Startup**
  - Extract the operating profile from verified public records, pricing pages, and customer case studies.
  - Infer the Ideal Customer Profile (ICP) from observed evidence (logos, review profiles, pricing tiers).
  - Define competitors based on actual market positioning.

- **Case C: Hybrid (Company + New Bet / Pivot)**
  - Separate the core business profile from the new bet. Define competitors for both separately.

- **Ambiguous Input**:
  If the input is unclear, ask the user immediately:
  1. Is this an early idea or an operating company?
  2. If an operating company: what is the company name or URL?
  3. If an idea: what is the core job-to-be-done, target customer, geography, and expected business model?
  4. What specific decision will this report support?

### 2. Mandate, Scope & Depth Assessment (Stages 1–1.5)
- Clarify the decision mandate (e.g., investor memo, pricing redesign, sales battlecard).
- Score market complexity (breadth 1–3, competitor volume 1–3, geographic scope 1–3) to determine the **Research Depth Tier**:
  - **Light (3–4)**: 3–5 competitors, pricing tiers, review platforms.
  - **Standard (5–7)**: 5–8 competitors, full 3-lens research, GTM & hiring signals.
  - **Deep (8–9)**: 8–10 competitors, exhaustive forum mining, language maps, channel maps.

### 3. Establish ICP & Problem Triad (Stages 2–3)
Confirm the buyer persona, firmographic parameters, the acute trigger pain point, and the existing budget line item being displaced.

### 4. Map the Competitor Universe (Stage 4)
Categorize candidates into Direct, Indirect, Adjacent/Emerging, Incumbents, and Substitutes/Status Quo.
Score candidates using the **Competitor Relevance Metric** via the CLI tool:
```bash
python3 scripts/score_competitors.py relevance \
  --name "<Competitor>" \
  --customer <0-100> \
  --problem <0-100> \
  --geography <0-100> \
  --model <0-100> \
  --product <0-100>
```
Select a focused shortlist of **5 to 10 priority competitors** (Relevance $\ge 40$).

### 5. Execute 3-Lens Deep Research (Stage 5)
- **Lens 1: Competitor Profiles & Pricing Reverse-Engineering**:
  - Value metric (per seat vs. usage vs. flat).
  - Pricing psychology (anchoring, decoys, freemium gates).
  - 3-tier switching costs: Technical (data migration), Contractual (annual lock-in), Emotional (retraining).
- **Lens 2: Customer Sentiment & Language Mining**:
  - Review mining (G2, Capterra, App Stores) for praise themes, complaint themes, and churn reasons.
  - Forum mining (Reddit, Indie Hackers, Hacker News) for verbatim quotes. Build the **Language Map**.
  - Identify **Cross-Competitor Structural Pains** shared across 3+ players (the optimal entrant wedge).
- **Lens 3: Go-To-Market & Strategic Trajectory Signals**:
  - Sales motion (self-serve PLG vs. sales-led) and signup friction.
  - Hiring signal ratios: Engineering-heavy (rebuilding/R&D) vs. Sales-heavy (scaling) vs. CS-heavy (churn firefighting).
  - Content pillars owned vs. underexploited content whitespace.

### 6. Post-Research Alignment Checkpoint
Before synthesizing, send a **single alignment message** to the user:
> *"Research complete across [X] competitors. Top direct competitors are [A, B, C]; primary shared pain point is [P]; dominant pricing model is [M]. Does this align with your view, or should any competitors be added/removed before final synthesis?"*

### 7. Verification & Triangulation (Stage 6)
- **2-Source Corroboration Rule**: Every material fact requires at least 2 independent sources.
- **Duplicate-Source Check**: Ensure multiple articles are not merely syndicating the exact same press release.
- **No False Precision**: Private ARR and metrics must be expressed as calibrated ranges with underlying proxies shown.
- Audit evidence logs using:
  ```bash
  python3 scripts/score_competitors.py verify-log --file <evidence_log.json>
  ```

### 8. Synthesis & Strategic Pattern-Matching (Stage 7)
Connect findings across lenses (pricing gap + customer complaint + hiring void = strategic wedge). Evaluate threat level via:
```bash
python3 scripts/score_competitors.py threat \
  --name "<Competitor>" \
  --relevance <0-100> --funding <1-5> --growth <1-5> --satisfaction <1-5>
```

### 9. Deliverable Verification Pass (Stage 7.5)
Run the automated Radical Honesty and formatting audit on generated deliverables:
```bash
python3 scripts/score_competitors.py audit-markdown -f <deliverable.md>
```

---

## Output Contract

Every comprehensive competitive engagement delivers:

1. **Research Brief & Hypothesis Summary**: Input classification, mandate, and depth tier.
2. **Competitor Priority Matrix**: Scored ranking table with classifications (`DIRECT`, `INDIRECT_ADJACENT`, `SUBSTITUTE_WATCHLIST`).
3. **Customer Language Map**: Verbatim quotes capturing problem descriptions, complaints, desired solutions, and switching triggers.
4. **Competitor Battlecards**: 1-page tactical teardowns with explicit **"When They Win Over You"** scenarios and switching cost breakdowns.
5. **Evidence Log & Verification Matrix**: Explicit claim labels (`[Data]`, `[Estimate]`, `[Assumption]`, `[Opinion]`), source tiers, and confidence scores.
6. **Red Flags & Yellow Flags**: Mandatory risk disclosures trailing every deliverable file.

---

## Core Guardrails & Verification Rules

- **Never invent or assume private metrics.** ARR, burn, and churn must never be presented as single-point facts. Always report calibrated ranges with proxy math shown.
- **Never rely on marketing copy for verified facts.** Self-reported claims ("50,000 customers") are Tier 3 marketing disclosures. Verify via review volumes, case studies, and traffic.
- **Never skip input classification.** Ideas are hypothesis-driven; operating companies are evidence-driven.
- **Never omit competitor strengths.** Battlecards that omit competitor strengths will cause sales teams to lose live deals.
- **Do not read tool execution logs into context.** Tool logs in `scripts/.logs/` are for debugging.
- **Stdlib deterministic tooling.** `scripts/score_competitors.py` (v2.0.0) is self-contained with standard Python libraries. Check status via `--doctor`.

---

## Reference Documentation

- [`references/workflow-stages.md`](references/workflow-stages.md): Complete procedural guide for all stages (Stage 0 to Stage 8), research lenses, and checkpoints.
- [`references/scoring-and-rubrics.md`](references/scoring-and-rubrics.md): Mathematical formulas for Relevance, Confidence, Threat Index, and Research Depth Matrix.
- [`references/source-tiers-and-verification.md`](references/source-tiers-and-verification.md): Source tiers (T1–T4), Radical Honesty Protocol, 4-tier claim labeling, and anti-patterns.
- [`references/report-and-battlecard-templates.md`](references/report-and-battlecard-templates.md): Production templates for briefs, language maps, battlecards, and executive reports.

---

## CLI Tooling (v2.0.0)

- `python3 scripts/score_competitors.py --doctor` — Environment and readiness check.
- `python3 scripts/score_competitors.py relevance --customer C --problem P --geography G --model M --product F` — Calculates 0–100 relevance score.
- `python3 scripts/score_competitors.py threat --name N --relevance R --funding F --growth G --satisfaction S` — Evaluates threat level (`HIGH`, `MEDIUM`, `LOW`).
- `python3 scripts/score_competitors.py confidence --credibility S --corroboration K --recency R --completeness Q` — Calculates 1.0–5.0 confidence score.
- `python3 scripts/score_competitors.py verify-log --file <claims.json>` — Validates evidence log entries against the 2-source rule.
- `python3 scripts/score_competitors.py audit-markdown --file <report.md>` — Audits deliverable markdown for Radical Honesty and claim label compliance.
- `python3 scripts/score_competitors.py matrix --file <competitors.json>` — Batch scores competitors and outputs a priority ranking table.
