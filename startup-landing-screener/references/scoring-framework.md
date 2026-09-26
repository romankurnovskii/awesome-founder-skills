# Launch Gate Scoring Framework & Readiness Thresholds

Defines the scoring mathematics, weighting hierarchy, and launch decision thresholds for evaluating landing pages against the 30 Vibe-Coded Acceptance Criteria.

---

## 1. Severity Levels & Criterion Weighting

Each of the 30 criteria is assigned a severity tier reflecting its negative impact on conversion, user trust, and investor/customer credibility:

| Severity Level | Weight | Description | Failure Consequence |
| :--- | :---: | :--- | :--- |
| **Critical** | **3 pts** | Fatal credibility or conversion dealbreaker (e.g. no real demo, fake testimonials, no clear ICP, no proof it works). | Disqualifies from public launch; burns ad spend / launch momentum. |
| **Major** | **2 pts** | High-friction conversion killer (e.g. generic AI copy, no pricing clarity, no technical details, purple+black clone). | Degrades conversion rate by 40–70%; creates visitor skepticism. |
| **Minor** | **1 pt** | Aesthetic or layout polish flaw (e.g. 3 feature cards, excessive gradients, too many animations). | Weakens distinctiveness and polish; easily remediated. |

---

## 2. Criterion Status Definitions

For every criterion evaluated, assign one of four statuses:

- **`PASS` (100% of points earned)**:
  - The criterion is cleanly met with visible evidence, domain specificity, and authentic presentation.
- **`WARN` (50% of points earned)**:
  - Partial compliance, mild ambiguity, or minor trace of the anti-pattern present.
  - Generates an actionable suggestion before pushing.
- **`FAIL` (0% of points earned)**:
  - Clear presence of the red flag / anti-pattern, or total absence of the required authentic element.
  - Must include concrete remediation recommendations.
- **`N/A` (Excluded from calculation)**:
  - Criterion does not apply to this specific product type (e.g., API docs requirement for a consumer mobile app). The maximum possible points are adjusted accordingly.

---

## 3. Mathematical Metrics

### 1. Launch Readiness Score (0% – 100%)
Measures positive adherence to launch-ready standards:

$$\text{Launch Readiness Score} = \left( \frac{\sum \text{Points Earned}}{\sum \text{Max Applicable Points}} \right) \times 100$$

- **High (> 85%)**: High conversion readiness, authentic positioning, defensible value proposition.
- **Moderate (65% – 84%)**: Promising foundation but requires targeted copy, proof, or layout fixes before launch.
- **Low (< 65%)**: Severe anti-patterns present; page appears vibe-coded and will underperform.

### 2. Vibe-Coded Index (0% – 100%)
Measures the density of AI-startup cliches and anti-patterns:

$$\text{Vibe-Coded Index} = \left( \frac{\sum (\text{Critical Fails} \times 3) + \sum (\text{Major Fails} \times 2) + \sum (\text{Minor Fails} \times 1) + 0.5 \times \text{Warns}}{\text{Total Possible Penalty Points}} \right) \times 100$$

- **0% – 15% (Clean)**: Original, grounded, human, and professional.
- **16% – 35% (Mild Hype)**: Contains isolated template tropes; easily cleaned up.
- **36% – 60% (Vibe-Coded)**: Noticeable clone characteristics; reads like an LLM wrapper.
- **> 60% (Vibe-Coded Trap)**: Total aesthetic and copy clone; urgent rebuild required.

---

## 4. The "Ready to Push" Launch Gates

Before a founder pushes their landing page to production, Hacker News, Product Hunt, or paid ads, evaluate against these strict gating rules:

```
┌──────────────────────────────────────────────────────────┐
│                   LAUNCH DECISION GATE                   │
└──────────────────────────────────────────────────────────┘
                             │
     ┌───────────────────────┴───────────────────────┐
     │ Any Critical Failures (Severity = Critical)?  │
     └───────────────────────┬───────────────────────┘
                            / \
                          YES  NO
                          /     \
                         ▼       ▼
             ┌───────────────┐  ┌─────────────────────────────────┐
             │ BLOCKED (🔴)  │  │ Launch Readiness Score >= 85%?  │
             └───────────────┘  └────────────────┬────────────────┘
                                                / \
                                              YES  NO
                                              /     \
                                             ▼       ▼
                              ┌──────────────────┐  ┌───────────────────┐
                              │ READY TO PUSH 🟢 │  │  NEEDS WORK 🟡    │
                              └──────────────────┘  └───────────────────┘
```

### Gate 1: 🟢 READY TO PUSH (Full Approval)
- **Conditions**:
  - Launch Readiness Score $\ge 85\%$
  - **Zero (0) Critical Fails**
  - $\le 2$ Major Fails
  - Vibe-Coded Index $\le 20\%$
- **Verdict**: The page communicates authentic value, displays concrete product proof, targets a sharp ICP, and avoids generic AI cliches. Safe to push to production and public distribution.

### Gate 2: 🟡 CONDITIONAL / NEEDS WORK (Pre-Push Remediation)
- **Conditions**:
  - Launch Readiness Score between $65\%$ and $84\%$
  - $\le 1$ Critical Fail
  - $\le 5$ Major Fails
  - Vibe-Coded Index between $21\%$ and $40\%$
- **Verdict**: Do NOT launch paid traffic or high-stakes announcements yet. Execute the prioritized remediation plan (top 3–5 suggestions) first to prevent conversion leakage.

### Gate 3: 🔴 BLOCKED - VIBE-CODED (Do Not Push)
- **Conditions**:
  - Launch Readiness Score $< 65\%$
  - **$\ge 2$ Critical Fails**
  - Vibe-Coded Index $> 40\%$
- **Verdict**: **DO NOT PUSH**. The landing page exhibits multiple systemic vibe-coded anti-patterns (e.g. no real demo, fake testimonials, generic AI copy, purple/black template clone). Launching in this state will damage founder reputation and waste user attention.
