# How to Use: Startup Landing Screener

## What This Skill Does

Audits a startup landing page or website against the **30 Vibe-Coded AI Startup Anti-Patterns** to determine whether it is ready for public launch. Generates a 30-point acceptance matrix, a Launch Gate Verdict (READY TO PUSH, NEEDS WORK, or BLOCKED), and concrete before/after remediation suggestions.

## When to Use

- Auditing a landing page before launching on Hacker News, Product Hunt, or X/Twitter.
- Reviewing pitch drafts, hero copy, and visual mockups to avoid generic AI cliches.
- Testing whether your value proposition, ICP, and pricing are clear to technical buyers.
- Evaluating whether your site looks like an authentic software product or a vibe-coded template clone.

## Prompt Examples

```
Review my landing page at https://example.com. Is it ready to push?
Audit our startup homepage copy against the 30 vibe-coded anti-patterns.
Here is my landing page HTML / copy. Run an acceptance review and give me specific suggestions.
Is our AI devtool website too generic? Check if it looks vibe-coded.
```

## Running the CLI Directly

```bash
# Audit a live URL
python3 startup-landing-screener/scripts/screen_landing.py --url "https://example.com" --name "MyStartup"

# Audit a local file (HTML or Markdown)
python3 startup-landing-screener/scripts/screen_landing.py --file "path/to/index.html"

# Output structured JSON for automation
python3 startup-landing-screener/scripts/screen_landing.py --url "https://example.com" --json

# Run doctor self-diagnostic
python3 startup-landing-screener/scripts/screen_landing.py --doctor
```

## What You Get

1. **Executive Launch Verdict**: `🟢 READY TO PUSH`, `🟡 NEEDS WORK`, or `🔴 BLOCKED`.
2. **Readiness Metrics**: Launch Readiness Score (0–100%) and Vibe-Coded Index (0–100%).
3. **Full 30-Criteria Comparison Matrix**: Complete line-by-line status (`PASS`, `WARN`, `FAIL`) and observed evidence for all 30 acceptance criteria.
4. **Actionable Suggestions & Fixes**: Before-and-after copy rewrites, layout swaps, and proof requirements for every flagged item.
5. **Prioritized Launch Checklist**: Top 5 high-impact fixes ranked by conversion impact.

## Tips

- If you don't have customers yet, delete the testimonial section rather than using vague or placeholder quotes.
- Show raw, authentic product UI and short video walkthroughs early—abstract 3D art is the #1 signal of vaporware.
