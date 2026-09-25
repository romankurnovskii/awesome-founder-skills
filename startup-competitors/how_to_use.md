# How to Use: Startup Competitors

## What This Skill Does

Conducts investment-grade competitive intelligence and verification for startups and business ideas.
Operates under a strict **Radical Honesty Protocol** (no cheerleading; objective assessment of competitor strengths).
It classifies inputs (idea vs. real company vs. hybrid), maps the competitor universe, executes multi-lens research (pricing reverse-engineering, sentiment/language mining, GTM signals), enforces a 2-source verification rule, and generates actionable battlecards, customer language maps, and strategic reports.

## When to Use

- Mapping and verifying the real competitors for a startup or business idea.
- Preparing investor memos, pitch decks, or board strategy reviews.
- Building tactical sales battlecards and objection-handling guides.
- Uncovering customer switching triggers and competitor churn signals.
- Reverse-engineering competitor pricing psychology and switching costs.

## Prompt Examples

```
Who are the real competitors for my startup? Name: MarketMan, Website: https://www.marketman.com.

Evaluate competitors for an idea: "AI-driven automated inventory forecasting for boutique bakeries."

Compare my startup against linear.app and jira across features, pricing, and moats.

Build sales battlecards for the top 3 direct competitors in our space.
```

## Running the CLI Tools Directly

```bash
# Check tool readiness and environment (v2.0.0)
python3 scripts/score_competitors.py --doctor

# Calculate Competitor Relevance Score (0-100)
python3 scripts/score_competitors.py relevance \
  --name "Competitor X" \
  --customer 85 --problem 90 --geography 100 --model 75 --product 80

# Calculate Competitor Threat Level (High/Medium/Low)
python3 scripts/score_competitors.py threat \
  --name "Competitor X" \
  --relevance 85 --funding 4.5 --growth 4.0 --satisfaction 4.5

# Assess claim confidence level (1.0-5.0)
python3 scripts/score_competitors.py confidence \
  --credibility 4.5 --corroboration 4.0 --recency 5.0 --completeness 4.0

# Audit a deliverable file for Radical Honesty and claim label compliance
python3 scripts/score_competitors.py audit-markdown -f report.md
```

## What You Get

1. **Competitor Relevance Rankings**: Quantitative categorization into Direct, Indirect/Adjacent, or Substitute.
2. **Customer Language Map**: Verbatim customer phrases describing problems, frustrations, and switching triggers.
3. **Competitor Battlecards**: 1-page tactical teardowns including "When They Win Over You" and switching cost analyses.
4. **Evidence Log & Verification Matrix**: Explicit tagging of facts (`[Data]`), estimates (`[Estimate]`), assumptions (`[Assumption]`), and opinions (`[Opinion]`).
5. **Red & Yellow Flags**: Mandatory risk warnings attached to every deliverable.

## Tips

- **No Cheerleading**: If a competitor is objectively superior at a feature or scale, it is stated up front.
- **No False Precision**: Private company metrics must always be reported as ranges, never point numbers.
- **2-Source Rule**: Every material fact must be corroborated by at least 2 independent sources.
