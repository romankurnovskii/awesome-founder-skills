---
name: startup-landing-screener
description: "Audit and screen a startup website or landing page against acceptance criteria before public launch. Evaluates all '30 reasons your AI startup looks vibe-coded' anti-patterns across copywriting, visual design, product reality, social proof, commercial clarity, and market differentiation. Computes Launch Readiness Score, Vibe-Coded Index, and strict Launch Gate Verdict (READY TO PUSH, NEEDS WORK, or BLOCKED). Produces a complete 30-criteria comparison matrix and actionable before-and-after suggestions for every flagged item. Use when reviewing a landing page, auditing website copy or design, checking if a site is ready to push or launch, screening for vibe-coded clichés, or asking 'is my landing page ready to launch?' or 'review my startup website'."
metadata:
  version: 1.0.0
---

# Startup Landing Screener: Launch Gate & Anti-Vibe Protocol

Perform an unsparing, high-rigor acceptance audit of a startup landing page or website to determine whether it is genuinely **Ready to Push** to production, Hacker News, Product Hunt, and paid acquisition.

This skill screens against the **30 Vibe-Coded Anti-Patterns** that signal a generic AI wrapper, vaporware, or template clone. Every audit produces a complete 30-criteria comparison matrix, an objective Launch Gate verdict, and concrete, founder-level remediation suggestions for every flagged criterion.

---

## The Launch Gate Philosophy

1. **Zero Flattery, Maximum Conversion Protection**: A premature public launch burns brand credibility and wastes irreplaceable first-visit attention.
2. **The 30 Red Flags as Non-Negotiable Acceptance Tests**: Each of the 30 criteria is evaluated as `PASS`, `WARN`, or `FAIL` with verifiable evidence.
3. **Every Flag Gets a Fix**: Do not just tell the founder their copy sounds like an LLM; write the replacement copy. Do not just complain about purple gradients; specify the exact color palette or layout alternative.
4. **Binary Launch Gate Authority**: The audit outputs one of three clear states:
   - 🟢 **READY TO PUSH**: Score $\ge 85\%$, 0 Critical blockers, $\le 2$ Major flags.
   - 🟡 **NEEDS WORK**: Score $65\%–84\%$, $\le 1$ Critical blocker. Pre-push fixes required.
   - 🔴 **BLOCKED**: Score $< 65\%$, $> 1$ Critical blocker, or Vibe Index $> 40\%$.

---

## 30 Acceptance Criteria Across 6 Dimensions

The 30 criteria are organized into 6 core dimensions:

1. **Copywriting & Messaging**:
   - `#1` AI-generated landing page copy
   - `#2` Generic "revolutionize" messaging
   - `#6` "Built for the future"
   - `#11` "Powered by AI" as the headline
   - `#15` "10x your productivity"
   - `#21` "The future of X"
   - `#25` Buzzwords everywhere
2. **Visual Design & Layout**:
   - `#3` 3 feature cards in a row
   - `#7` Purple + black everything
   - `#8` Too many gradients
   - `#9` Bento grids everywhere
   - `#20` Generic AI-generated illustrations
   - `#24` Too many animations
3. **Product Reality & Technical Depth**:
   - `#5` No real product demo *(Critical)*
   - `#14` Chatbot as the entire product
   - `#16` No technical details
   - `#17` No API docs
   - `#19` No screenshots of the actual product *(Critical)*
   - `#29` No proof it actually works *(Critical)*
4. **Social Proof, Trust & Founder Voice**:
   - `#4` Fake testimonials *(Critical)*
   - `#13` No real customer stories
   - `#18` No visible users
   - `#23` No proof of ROI
   - `#26` No founder perspective
5. **ICP & Commercial Viability**:
   - `#10` No clear ICP *(Critical)*
   - `#12` No pricing clarity
   - `#27` No clear use case *(Critical)*
   - `#28` No reason to switch *(Critical)*
6. **Market Differentiation & Positioning**:
   - `#22` No differentiation *(Critical)*
   - `#30` It looks like every other AI startup

👉 **Detailed Criteria Rubric**: See [`references/criteria-rubric.md`](references/criteria-rubric.md) for full detection signals, fail/pass examples, and remediation rules.  
👉 **Scoring & Gating Math**: See [`references/scoring-framework.md`](references/scoring-framework.md).  
👉 **Report Template**: See [`references/report-template.md`](references/report-template.md).

---

## Operational Execution Sequence

```
Stage 0: Input Capture & Ingestion (URL, local file, or raw pitch copy)
   │
Stage 1: Automated Pre-Screen (Execute screen_landing.py CLI)
   │
Stage 2: Deep Semantic & Multimodal Inspection (Agent review of layout/copy/proof)
   │
Stage 3: Scoring & Launch Gate Verdict (Pass/Warn/Fail per criterion)
   │
Stage 4: Detailed Comparison & Suggestion Authoring (Before vs After fixes)
   │
Stage 5: Final Delivery (Markdown Audit Report following report-template.md)
```

---

### Stage 0: Input Capture & Ingestion

Identify the landing page input provided by the user:
- **Live URL**: e.g., `https://example.com`
- **Local File**: HTML, JSX/TSX, Astro, or Markdown landing page draft
- **Pasted Text**: Hero copy, feature list, pricing, and testimonial draft

---

### Stage 1: Automated Pre-Screening

Run the deterministic CLI screener located in `scripts/`:

```bash
# For a live URL:
python3 scripts/screen_landing.py --url "https://example.com" --name "ExampleApp"

# For a local file:
python3 scripts/screen_landing.py --file "path/to/page.html" --name "ExampleApp"

# Emit JSON for structured programmatic handling:
python3 scripts/screen_landing.py --url "https://example.com" --json
```

The script parses DOM elements, text content, hex colors, and keyword heuristics to populate the baseline status for all 30 criteria.

---

### Stage 2: Deep Semantic & Multimodal Audit

Supplement the automated pre-screen with direct analytical inspection:
1. **The Hero 5-Second Test**: Does the page explicitly state *who* uses this and *what acute pain* disappears?
2. **Product Tangibility**: Can a visitor see the real interface and actual workflow within 10 seconds? Or are there only abstract 3D shapes and fake browser mockups?
3. **Testimonial Veracity**: Are quotes attributed to real, verifiable people with real companies? Or are they stock avatars labeled "John D."?
4. **Status Quo Friction**: Does the page articulate why someone should abandon manual spreadsheets, Notion, or generic ChatGPT to pay for this tool?

---

### Stage 3: Scoring & Launch Gate Determination

Calculate metrics per [`references/scoring-framework.md`](references/scoring-framework.md):
- **Weights**: Critical = 3 pts, Major = 2 pts, Minor = 1 pt.
- **Launch Readiness Score**: Percentage of total applicable points earned.
- **Vibe-Coded Index**: Weighted penalty ratio of detected anti-patterns.
- **Verdict Gate**:
  - `READY TO PUSH`: Score $\ge 85\%$, 0 Critical fails, $\le 2$ Major fails.
  - `NEEDS WORK`: Score $65\%–84\%$, $\le 1$ Critical fail.
  - `BLOCKED`: Score $< 65\%$, $> 1$ Critical fail, or Vibe Index $> 40\%$.

---

### Stage 4: Authoring Detailed Comparisons & Suggestions

For every criterion marked `FAIL` or `WARN`:
1. **Document Current State**: Quote the exact copy or cite the observed visual pattern.
2. **Compare to Launch-Ready Standard**: Explain why the current approach triggers skepticism.
3. **Provide Concrete Fix**: Deliver the exact replacement copy or specific UI adjustment.
   ```text
   BEFORE: "Revolutionizing modern workflows with next-gen AI cognitive fabric."
   AFTER:  "Reconciles 500 bank transactions against Xero invoices in 3 minutes."
   ```

---

### Stage 5: Final Delivery

Format the deliverable strictly using [`references/report-template.md`](references/report-template.md):
- Executive Launch Verdict badge & summary table.
- Complete 30-criteria comparison matrix (no missing rows).
- Dimension-grouped deep dives with actionable before/after suggestions.
- Top 5 prioritized fixes before pushing to production.
- Final launch push checklist.
