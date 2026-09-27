# How to Use: Startup Landing Screener

## What This Skill Does

Audits a startup landing page or website through a **Two-Track Acceptance Protocol** to determine whether it is genuinely ready for public launch:
1. **Track 1: 30 Vibe-Coded Anti-Patterns (What to Avoid / Red Flags)**: Evaluates copywriting, layout, product proof, social proof, and positioning to ensure you don't look like a generic AI wrapper or vaporware template.
2. **Track 2: 20 Web QA Acceptance Criteria (What to Verify & Have / Must-Haves)**: Enforces responsive viewports, no horizontal scroll, unbroken links, working buttons, SEO metadata, accessible contact schemes, and content hygiene.

Generates a dual comparison matrix (50 criteria total), an objective Launch Gate Verdict (`🟢 READY TO PUSH`, `🟡 NEEDS WORK`, or `🔴 BLOCKED`), and concrete before/after copy & code remediation suggestions.

## When to Use

- Auditing a landing page before launching on Hacker News, Product Hunt, X/Twitter, or paid acquisition.
- Reviewing pitch drafts, hero copy, and visual mockups to avoid generic AI clichés.
- Running a pre-flight technical checklist: checking for broken buttons, horizontal scrolling, missing favicon, or placeholder text.
- Testing whether your value proposition, ICP, and pricing are clear to technical buyers.
- Evaluating whether your site looks like an authentic software product or an unpolished template clone.

## Prompt Examples

```
Review my landing page at https://example.com. Is it ready to push?
Audit our startup homepage against the 30 anti-patterns and 20 web QA criteria.
Here is my landing page HTML / copy. Run an acceptance review and give me specific before-and-after fixes.
Check if our website has mobile overflow, broken buttons, or generic AI copy.
```

## Running the CLI Directly

```bash
# Audit a live URL
python3 startup-landing-screener/scripts/screen_landing.py --url "https://example.com" --name "MyStartup"

# Audit a local file (HTML or Markdown)
python3 startup-landing-screener/scripts/screen_landing.py --file "path/to/index.html"

# Output structured JSON for CI/CD or automation
python3 startup-landing-screener/scripts/screen_landing.py --url "https://example.com" --json

# Run doctor self-diagnostic
python3 startup-landing-screener/scripts/screen_landing.py --doctor
```

## What You Get

1. **Executive Launch Verdict**: `🟢 READY TO PUSH`, `🟡 NEEDS WORK`, or `🔴 BLOCKED`.
2. **Readiness Metrics**:
   - **Composite Launch Readiness Score** (0–100%)
   - **Track 1 Vibe-Coded Index** (0–100%, lower is better)
   - **Track 2 Technical QA Score** (0–100%, higher is better)
   - Blocker Counts (Critical, Major, Minor) across both tracks.
3. **Track 1 Comparison Matrix**: Complete line-by-line status (`PASS`, `WARN`, `FAIL`) and observed evidence for all 30 anti-patterns.
4. **Track 2 Acceptance Checklist Matrix**: Verification status for all 20 technical & functional criteria.
5. **Actionable Suggestions & Fixes**: Before-and-after copy rewrites, HTML/CSS snippets, and layout fixes for every flagged item.
6. **Prioritized Launch Checklist**: Top high-impact fixes ranked by conversion and launch gate clearing impact.

## Tips

- If you don't have customers yet, delete the testimonial section rather than using vague or placeholder quotes.
- Show raw, authentic product UI and short video walkthroughs early—abstract 3D art is the #1 signal of vaporware.
- Test at 375px mobile width: if a user has to pinch-zoom or scroll sideways, that is an immediate launch blocker.
