# awesome-founder-skills

Skills I use as a founder to verify startup ideas before committing months to them. Skills I use to review accelerator requirements and decide whether a program is worth applying to.

```bash
npx skills add romankurnovskii/awesome-founder-skills
```

## Skills

### [`startup-framing-screener`](startup-framing-screener)

Screens a startup's name, one-line statement, and website URL against the framing thresholds published in **[arXiv:2608.00045](https://arxiv.org/abs/2608.00045)** — *"Predicting Startup Exit from Textual Descriptors: A Computational Linguistics Framework"* (Saruggia & Germano, 2026).

**This skill is a research-based implementation, not an original methodology.** The thresholds, Exit Deltas, feature-importance weights, and the Hyping Score formula all come from that paper, which analysed 7,419 startups and 770 exits (10.38% baseline) across 20 years of Techstars and Y Combinator data.

The caveats matter as much as the method, so they are stated up front:

- The paper does **not** publish its dictionaries. The word lists shipped with this skill are an independent **reconstruction**, not the authors' original instrument.
- The paper does **not** publish its trained model coefficients. The skill therefore reports band membership against published thresholds — it never outputs a probability of success.
- At the paper's precision-1.0 operating point, recall is **0.005–0.017**. A clean screen means "not flagged", never "will succeed".
- It scores narrative framing only. It cannot judge market size, unit economics, team, or product-market fit.
- **Not investment advice.**

If you use this in academic work, cite the paper for the methodology and this repository only for the implementation. Full citation, licensing, and redistribution duties: [`references/attribution.md`](startup-framing-screener/references/attribution.md).

### [`startup-competitors`](startup-competitors)

Conducts investment-grade competitive intelligence and verification under a Radical Honesty protocol. Maps competitor universes (direct, indirect, substitutes, incumbents, adjacent), reverse-engineers pricing, mines customer sentiment, analyzes GTM signals, triangulates claims across 4 source tiers, and generates 1-page battlecards with explicit "when they win over you" assessments.

### [`startup-landing-screener`](startup-landing-screener)

Audits a startup website or landing page through a dual-track acceptance protocol before public launch. Evaluates **Track 1: 30 Vibe-Coded Anti-Patterns** (what to avoid / red flags across copy, design, product proof, social trust, and positioning) alongside **Track 2: 20 Web QA Acceptance Criteria** (what to verify & have across responsive viewports, unbroken links, working CTAs, SEO metadata, contact schemes, and content hygiene). Computes Launch Readiness Score, Vibe-Coded Index, and Technical QA Score to determine an objective Launch Gate Verdict (`🟢 READY TO PUSH`, `🟡 NEEDS WORK`, or `🔴 BLOCKED`). Produces dual comparison matrices and actionable before-and-after suggestions for every flagged item.
