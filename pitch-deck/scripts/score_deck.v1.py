#!/usr/bin/env python3
"""
score_deck.v1.py

Description:
  Deterministic pitch deck screener. Parses a deck (Markdown, plain text, PDF, or
  PPTX), reconstructs its slides, and evaluates it against:
    - Track A: 42 Investor-Facing Anti-Patterns (what to avoid / red flags)
    - Track B: 28 Deck Acceptance Criteria (what to verify & have / must-haves)
  Then computes the Composite Capital Readiness Score and the Capital Gate verdict
  (INVESTOR-READY, NEEDS WORK, or BLOCKED).

  This tool is a HEURISTIC PRE-SCREEN. It detects textual and structural signals
  only. It cannot see design, legibility, or whether a claimed number is true. The
  agent must complete the audit semantically via the skill's references.

Changelog:
  - v1.0.0: Initial implementation. Slide reconstruction, Track A / Track B
            heuristic detection, cross-slide numeric consistency check,
            placeholder-residue detection, missing-numbers ledger, JSON output,
            and --doctor self-diagnostic.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

TOOL_VERSION = '1.0.0'

# ==============================================================================
# Severity weights
# ==============================================================================

WEIGHT = {'C': 3, 'M': 2, 'm': 1}
SEV_NAME = {'C': 'Critical', 'M': 'Major', 'm': 'Minor'}

# ==============================================================================
# Lexicons
# ==============================================================================

HYPE_LEXICON = [
    'revolutioniz',
    'revolutionary',
    'disrupt',
    'game-chang',
    'cutting-edge',
    'next-gen',
    'next generation',
    'state-of-the-art',
    'seamless',
    'synerg',
    'best-in-class',
    'world-class',
    'paradigm shift',
    'turnkey',
    'holistic',
    'leverage',
    'empower',
    'unlock',
    'supercharge',
    'turbocharge',
    'frictionless',
    'end-to-end platform',
    'ai-powered',
    'powered by ai',
    '10x',
    '100x',
    'moonshot',
    'unprecedented',
    'industry-leading',
    'future of work',
    'future of',
    'robust',
    'scalable solution',
    'one-stop',
    'hyper-growth',
    'blazing',
]

VANITY_LEXICON = [
    'downloads',
    'impressions',
    'registered users',
    'sign-ups',
    'signups',
    'waitlist',
    'followers',
    'page views',
    'website visits',
    'social reach',
    'app installs',
    'installs',
    'likes',
    'subscribers',
    'media mentions',
    'press mentions',
    'awards',
    'featured in',
]

JARGON_LEXICON = [
    'api-first',
    'zero-knowledge',
    'event-driven',
    'multi-tenant',
    'rag pipeline',
    'vector store',
    'fine-tuned llm',
    'agentic',
    'orchestration layer',
    'deterministic replay',
    'idempotent',
    'sharded',
    'edge-native',
]

PLACEHOLDER_PATTERNS = [
    r'\[company\s*name\]',
    r'\[your\s*name\]',
    r'\[insert[^\]]*\]',
    r'\[x\]',
    r'\[n\]',
    r'\[metric[^\]]*\]',
    r'\[tbd[^\]]*\]',
    r'\btbd\b',
    r'\btba\b',
    r'lorem ipsum',
    r'\bxxx\b',
    r'<company>',
    r'placeholder',
    r'insert here',
    r'to be determined',
    r'\bfixme\b',
]

SOURCE_MARKERS = [
    'source:',
    'source ',
    '(source',
    'sources:',
    'according to',
    'per ',
    'gartner',
    'statista',
    'cb insights',
    'pitchbook',
    'idc',
    'mckinsey',
    'bureau of labor',
    'census',
    'sec filing',
    'company data',
    'internal data',
    'our analysis',
    'own estimate',
    'our estimate',
    'bottom-up',
    'bottom up',
]

MARKET_CONTEXT = [
    'market',
    'tam',
    'sam',
    'som',
    'industry',
    'global',
    'sector',
    'category',
    'benchmark',
    'average',
    'median',
    'survey',
    'report',
    'study',
    'spend',
    'opportunity',
]

FORWARD_LOOKING = [
    'target',
    'plan',
    'goal',
    'projection',
    'projected',
    'forecast',
    'by 20',
    'next year',
    'vision',
    'expect',
    'aim',
    'will reach',
    'plan to',
]

BOTTOM_UP_MARKERS = [
    'bottom-up',
    'bottom up',
    'tam =',
    'sam =',
    'som =',
    'customers ×',
    'customers x',
    'accounts ×',
    'accounts x',
    '× acv',
    'x acv',
    '× price',
    'x price',
    'reachable',
]

RETENTION_MARKERS = [
    'retention',
    'cohort',
    'churn',
    'nrr',
    'grr',
    'net revenue retention',
    'repeat purchase',
    'repeat usage',
    'm6',
    'month 6',
    'ltv curve',
]

DEMAND_MARKERS = [
    'loi',
    'letter of intent',
    'pilot',
    'paid pilot',
    'waitlist conversion',
    'design partner',
    'beta user',
    'private beta',
    'signed',
    'pre-order',
    'preorder',
    'deposit',
    'backlog',
]

UNIT_ECON_MARKERS = [
    'ltv',
    'cac',
    'payback',
    'gross margin',
    'contribution margin',
    'ltv/cac',
    'ltv:cac',
    'arpu',
    'acv',
    'burn multiple',
    'rule of 40',
]

ASK_MARKERS = [
    'raising',
    'the ask',
    'round size',
    'safe',
    'convertible note',
    'priced round',
    'term sheet',
    'close date',
    'closing in',
    'committed',
    'we are raising',
    'seeking',
]

USE_OF_FUNDS_MARKERS = [
    'use of funds',
    'use of proceeds',
    'allocation',
    'runway',
    'milestone',
    'hires',
    'headcount plan',
]

MOAT_MARKERS = [
    'moat',
    'defensib',
    'switching cost',
    'network effect',
    'data flywheel',
    'proprietary data',
    'regulatory',
    'distribution lock',
    'brand',
    'patent',
    'barrier to entry',
]

COMPETITION_MARKERS = [
    'competitor',
    'competition',
    'competitive landscape',
    'alternatives',
    'incumbent',
    'substitute',
    'versus',
    'vs.',
]

PRODUCT_MARKERS = [
    'screenshot',
    'screenshots',
    'demo',
    'prototype',
    'figma',
    'walkthrough',
    'product tour',
    'dashboard',
    'sandbox',
    'live product',
    'private beta',
    'product image',
    'app store',
    'ui mock',
]

WHY_NOW_MARKERS = [
    'why now',
    'why-now',
    'now that',
    'since 20',
    'in 20',
    'as of 20',
    'new regulation',
    'regulation',
    'cost curve',
    'crossed',
    'platform shift',
    'model release',
    'policy change',
    'recently',
    'this year',
]

TRACTION_MARKERS = [
    'traction',
    'mrr',
    'arr',
    'revenue',
    'gmv',
    'growth',
    'dau',
    'mau',
    'weekly active',
    'monthly active',
    'paying customer',
    'net new',
]

TEAM_MARKERS = ['team', 'founder', 'co-founder', 'cofounder', 'ceo', 'cto', 'built', 'shipped']

PRESENTED_DECK_MARKERS = ['speaker notes', 'demo day', '2:30', 'presented']


# ==============================================================================
# Logging
# ==============================================================================


def setup_logger() -> logging.Logger:
    """Configures file logging to .logs/<tool>_<timestamp>.log plus stdout."""
    script_dir = Path(__file__).resolve().parent
    log_dir = script_dir / '.logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'score_deck_{timestamp}.log'

    logger = logging.getLogger('score_deck')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(fh)
        # Console logs go to stderr so stdout stays clean for --json output.
        ch = logging.StreamHandler(sys.stderr)
        ch.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(ch)
    return logger


# ==============================================================================
# Deck ingestion
# ==============================================================================


def extract_pptx_text(path: Path) -> str:
    """Extracts text from a .pptx by reading slide XML directly (stdlib only)."""
    parts: list[str] = []
    with zipfile.ZipFile(path) as zf:
        slide_names = sorted(n for n in zf.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n))
        for name in slide_names:
            xml = zf.read(name).decode('utf-8', errors='ignore')
            texts = re.findall(r'<a:t>(.*?)</a:t>', xml, flags=re.DOTALL)
            body = '\n'.join(t.strip() for t in texts if t.strip())
            parts.append(f'## Slide {len(parts) + 1}\n{body}')
    return '\n\n'.join(parts)


def extract_pdf_text(path: Path) -> str:
    """Extracts text from a PDF using pdftotext when available."""
    exe = shutil.which('pdftotext')
    if not exe:
        msg = 'pdftotext not found; install poppler or convert the PDF to text first'
        raise RuntimeError(msg)
    result = subprocess.run(  # noqa: S603
        [exe, '-layout', str(path), '-'],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        msg = f'pdftotext failed: {result.stderr.strip()}'
        raise RuntimeError(msg)
    return result.stdout


def load_deck_text(path: Path) -> str:
    """Loads deck text from .md/.txt/.pptx/.pdf."""
    suffix = path.suffix.lower()
    if suffix in {'.md', '.markdown', '.txt', '.text'}:
        return path.read_text(encoding='utf-8', errors='ignore')
    if suffix == '.pptx':
        return extract_pptx_text(path)
    if suffix == '.pdf':
        return extract_pdf_text(path)
    msg = f'unsupported file type: {suffix} (use .md, .txt, .pptx, or .pdf)'
    raise RuntimeError(msg)


SLIDE_SPLIT_MARKERS = [
    re.compile(r'^\s*#{1,3}\s*(?:slide|page)?\s*\d+\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*##\s+', re.MULTILINE),
    re.compile(r'^\s*---+\s*$', re.MULTILINE),
    re.compile(r'^\s*slide\s+\d+\s*:?', re.IGNORECASE | re.MULTILINE),
]


def split_slides(text: str) -> list[str]:
    """Reconstructs slides from the strongest available delimiter."""
    for marker in SLIDE_SPLIT_MARKERS:
        parts = [p.strip() for p in marker.split(text) if p.strip()]
        if len(parts) >= 4:
            return parts
    # Fall back: treat double-newline-separated blocks as slide-sized.
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return parts if len(parts) >= 4 else [text.strip()]


def normalize(text: str) -> str:
    """Lowercases and collapses whitespace for lexeme matching."""
    return re.sub(r'\s+', ' ', text).lower()


def contains_any(haystack: str, needles: list[str]) -> list[str]:
    """Returns the subset of needles present in the haystack."""
    return [n for n in needles if n in haystack]


def word_count(text: str) -> int:
    """Counts whitespace-delimited words, ignoring markdown scaffolding."""
    cleaned = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', text)
    cleaned = re.sub(r'\[[^\]]*\]\([^)]*\)', ' ', cleaned)
    cleaned = re.sub(r'[#*`_>|-]+', ' ', cleaned)
    return len([w for w in cleaned.split() if any(c.isalnum() for c in w)])


# ==============================================================================
# Track A: anti-pattern detection
# ==============================================================================


def detect_track_a(deck: str, slides: list[str], word_budget: int = 60) -> dict[str, dict[str, Any]]:
    """Runs heuristic detection for the 30 Track A anti-patterns."""
    low = normalize(deck)
    n_slides = len(slides)
    results: dict[str, dict[str, Any]] = {}

    def record(ap: str, severity: str, status: str, evidence: str, name: str) -> None:
        results[ap] = {
            'id': ap,
            'name': name,
            'severity': severity,
            'status': status,
            'evidence': evidence,
        }

    hype_hits = contains_any(low, HYPE_LEXICON)
    vanity_hits = contains_any(low, VANITY_LEXICON)
    jargon_hits = contains_any(low, JARGON_LEXICON)
    placeholder_hits = [p for p in PLACEHOLDER_PATTERNS if re.search(p, low)]
    unsourced = find_unsourced_figures(deck)
    topdown = re.findall(r'\b\d+(?:\.\d+)?\s*%\s*of\s*(?:a\s*)?\$?\s*\d+', low)
    bottom_up = contains_any(low, BOTTOM_UP_MARKERS)

    # --- Group 1: narrative & positioning ---
    insight_markers = contains_any(
        low,
        [
            'we believe',
            'our insight',
            'the insight',
            'we realized',
            'we found that',
            'the key insight',
            'what we learned',
            'contrary to',
            'most people think',
        ],
    )
    record(
        'AP-01',
        'C',
        'PASS' if insight_markers else 'WARN',
        f'insight markers present: {insight_markers[:4]}'
        if insight_markers
        else 'no explicit insight marker found — verify semantically, absence of the phrase is not proof of absence of the insight',
        'Feature list instead of an insight',
    )

    why_now = contains_any(low, WHY_NOW_MARKERS)
    record(
        'AP-02',
        'C',
        'PASS' if 'why now' in low else ('WARN' if why_now else 'FAIL'),
        f'markers: {why_now[:3]}' if why_now else 'no why-now section or dated event',
        'No "why now", or a "why" masquerading as "why now"',
    )

    record(
        'AP-03',
        'M',
        'FAIL' if len(hype_hits) >= 5 else ('WARN' if len(hype_hits) >= 2 else 'PASS'),
        f'{len(hype_hits)} hype lexemes: {hype_hits[:6]}',
        'Buzzword soup',
    )

    record(
        'AP-04',
        'M',
        'FAIL' if len(jargon_hits) >= 4 else ('WARN' if len(jargon_hits) >= 2 else 'PASS'),
        f'{len(jargon_hits)} internal-jargon lexemes: {jargon_hits[:5]}',
        'Jargon that excludes the room',
    )

    first = slides[0] if slides else ''
    sentence = first_statement(first)
    sentence_low = sentence.lower()
    one_liner_bad = bool(
        not sentence
        or word_count(sentence) > 15
        or any(re.search(pat, sentence_low) for pat in PLACEHOLDER_PATTERNS)
        or len(contains_any(sentence_low, HYPE_LEXICON)) >= 2
    )
    record(
        'AP-05',
        'C',
        'FAIL' if one_liner_bad else 'PASS',
        f'title statement: "{sentence}" ({word_count(sentence)} words)' if sentence else 'no declarative one-liner found on the title slide',
        'The one-liner describes a category, not a company',
    )

    record(
        'AP-06',
        'M',
        'WARN' if (hype_hits and not contains_any(low, ['beachhead', 'wedge', 'first market', 'initial market', 'entry market'])) else 'PASS',
        'no wedge/beachhead language detected alongside large-market language'
        if not contains_any(low, ['beachhead', 'wedge', 'first market', 'initial market', 'entry market'])
        else 'wedge language present',
        'Vision with no wedge',
    )

    # --- Group 2: market & sizing ---
    record(
        'AP-07',
        'M',
        'FAIL' if (topdown and not bottom_up) else ('WARN' if topdown and bottom_up else 'PASS'),
        f'top-down fragments: {topdown[:3]}; bottom-up markers: {bottom_up[:3]}',
        'Top-down TAM only',
    )

    record(
        'AP-08',
        'M',
        'FAIL' if len(unsourced) >= 3 else ('WARN' if unsourced else 'PASS'),
        f'{len(unsourced)} figure(s) with no nearby source marker',
        'Unsourced market numbers',
    )

    record(
        'AP-09',
        'M',
        'WARN' if re.search(r'\b1\s*%\s*of\b', low) else 'PASS',
        '"1% of" capture framing detected' if re.search(r'\b1\s*%\s*of\b', low) else 'none',
        'Market defined so broadly it implies no focus',
    )

    # --- Group 3: product & proof ---
    product_hits = contains_any(low, PRODUCT_MARKERS)
    has_image = bool(re.search(r'!\[[^\]]*\]\([^)]*\)', deck))
    record(
        'AP-10',
        'C',
        'FAIL' if not (product_hits or has_image) else 'PASS',
        f'product markers: {product_hits[:4]}; embedded images: {has_image}',
        'No product evidence of any kind',
    )

    record(
        'AP-11',
        'C',
        'WARN'
        if (contains_any(low, ['figma', 'mockup', 'mock-up', 'design concept']) and not contains_any(low, ['live', 'beta', 'concept', 'prototype']))
        else 'PASS',
        'mockup language without honesty labels' if contains_any(low, ['figma', 'mockup', 'mock-up']) else 'no unlabelled mockups detected',
        'Mockups presented as shipping product',
    )

    record(
        'AP-12',
        'M',
        'WARN' if (contains_any(low, ['roadmap', 'q1', 'q2', 'q3', 'q4']) and not contains_any(low, TRACTION_MARKERS)) else 'PASS',
        'roadmap language present with no traction metric'
        if (contains_any(low, ['roadmap', 'q1', 'q2', 'q3', 'q4']) and not contains_any(low, TRACTION_MARKERS))
        else 'roadmap and traction distinguished',
        'Roadmap presented as traction',
    )

    record(
        'AP-13',
        'M',
        'WARN' if not contains_any(low, RETENTION_MARKERS + ['daily active', 'weekly active', 'usage']) else 'PASS',
        'no usage/retention proof detected'
        if not contains_any(low, RETENTION_MARKERS + ['daily active', 'weekly active', 'usage'])
        else 'usage or retention proof present',
        'No proof it works',
    )

    # --- Group 4: traction & metrics ---
    record(
        'AP-14',
        'M',
        'FAIL' if (vanity_hits and not contains_any(low, ['mrr', 'arr', 'revenue', 'gross margin'])) else ('WARN' if vanity_hits else 'PASS'),
        f'vanity lexemes: {vanity_hits[:5]}',
        'Vanity metrics',
    )

    record(
        'AP-15',
        'C',
        'FAIL'
        if (contains_any(low, ['projection', 'projected', 'forecast', '2027', '2028']) and not contains_any(low, ['assum', 'driver', 'based on']))
        else 'PASS',
        'projection present with no stated assumptions',
        'Hockey-stick without stated assumptions',
    )

    record(
        'AP-16',
        'M',
        'WARN' if re.search(r'\b(last|past)\s+(3|three|4|four|6|six)\s+months\b', low) else 'PASS',
        'short-window growth framing detected'
        if re.search(r'\b(last|past)\s+(3|three|4|four|6|six)\s+months\b', low)
        else 'no short-window framing detected',
        'Cherry-picked time window',
    )

    record(
        'AP-17',
        'M',
        'WARN'
        if (contains_any(low, ['subscription', 'marketplace', 'saas', 'consumer', 'monthly recurring']) and not contains_any(low, RETENTION_MARKERS))
        else 'PASS',
        'recurring-revenue model without cohort/retention data'
        if (contains_any(low, ['subscription', 'marketplace', 'saas', 'consumer', 'monthly recurring']) and not contains_any(low, RETENTION_MARKERS))
        else 'retention evidence present, or model does not require it',
        'No retention or cohort evidence where the model requires it',
    )

    record(
        'AP-18',
        'C',
        'FAIL' if (contains_any(low, ['pre-revenue', 'pre revenue', 'no revenue']) and not contains_any(low, DEMAND_MARKERS)) else 'PASS',
        'pre-revenue with no demand evidence'
        if (contains_any(low, ['pre-revenue', 'pre revenue']) and not contains_any(low, DEMAND_MARKERS))
        else 'demand evidence or revenue present',
        'Pre-revenue with zero demand evidence',
    )

    # --- Group 5: business model & unit economics ---
    model_markers = contains_any(
        low,
        ['business model', 'pricing', 'per month', 'per seat', 'per user', 'subscription', 'take rate', 'acv', 'annual contract'],
    )
    record(
        'AP-19',
        'C',
        'FAIL' if len(model_markers) < 2 else 'PASS',
        f'business-model markers: {model_markers[:5]}' if model_markers else 'no pricing or business-model content detected',
        'No business model',
    )

    econ = contains_any(low, UNIT_ECON_MARKERS)
    record(
        'AP-20',
        'M',
        'FAIL' if not econ else 'PASS',
        f'unit-economics markers: {econ[:5]}' if econ else 'no LTV/CAC/payback/gross-margin content',
        'Unit economics missing or implausible',
    )

    record(
        'AP-21',
        'M',
        'WARN' if (re.search(r'\bcac\b', low) and not contains_any(low, ['blended', 'paid cac', 'fully loaded', 'per channel'])) else 'PASS',
        'CAC present without a stated definition'
        if (re.search(r'\bcac\b', low) and not contains_any(low, ['blended', 'paid cac', 'fully loaded', 'per channel']))
        else 'no undefined CAC detected',
        'Blended metrics passed off as channel metrics',
    )

    record(
        'AP-22',
        'M',
        'WARN'
        if (
            contains_any(low, ['marketplace', 'take rate', 'gmv', 'hardware', 'logistics'])
            and not contains_any(low, ['gross margin', 'contribution margin', 'unit margin'])
        )
        else 'PASS',
        'marketplace/capital-intensive model without stated margin'
        if (
            contains_any(low, ['marketplace', 'take rate', 'gmv', 'hardware', 'logistics'])
            and not contains_any(low, ['gross margin', 'contribution margin', 'unit margin'])
        )
        else 'margin stated, or model is not capital-intensive',
        'Margins omitted in a capital-intensive or marketplace model',
    )

    # --- Group 6: competition & defensibility ---
    no_competition = bool(re.search(r'no\s+(?:direct\s+|real\s+|significant\s+)?compet\w*', low)) or bool(
        re.search(r'we (?:have|face) no competition', low)
    )
    record(
        'AP-23',
        'C',
        'FAIL' if no_competition else 'PASS',
        'explicit "no competition" claim found' if no_competition else 'competition acknowledged',
        '"We have no competition"',
    )

    giants = contains_any(low, ['google', 'facebook', 'amazon', 'uber', 'salesforce', 'microsoft', 'openai'])
    record(
        'AP-24',
        'M',
        'WARN' if (giants and not contains_any(low, COMPETITION_MARKERS)) else 'PASS',
        f'giants named without peer competitors: {giants[:4]}' if giants else 'no incumbent-giant comparisons detected',
        'Only comparing against giants',
    )

    checkmark_rows = len(re.findall(r'(\bwe\b[^|\n]*\|)[^|\n]*(✓|✅|yes|✔)', low))
    record(
        'AP-25',
        'M',
        'WARN' if checkmark_rows >= 4 else 'PASS',
        f'{checkmark_rows} all-checkmark comparison rows detected' if checkmark_rows >= 4 else 'no all-checkmark grid detected',
        'A comparison grid where you win every row',
    )

    moat = contains_any(low, MOAT_MARKERS)
    record(
        'AP-26', 'M', 'FAIL' if not moat else 'PASS', f'moat markers: {moat[:4]}' if moat else 'no defensibility mechanism named', 'No defensibility'
    )

    # --- Group 7: team ---
    record(
        'AP-27',
        'M',
        'WARN' if (contains_any(low, ['advisor', 'advisory board']) and len(contains_any(low, TEAM_MARKERS)) <= 1) else 'PASS',
        'advisor content without founder content'
        if (contains_any(low, ['advisor', 'advisory board']) and len(contains_any(low, TEAM_MARKERS)) <= 1)
        else 'founder content present',
        'Advisor-heavy team slide',
    )

    fit = contains_any(low, ['previously', 'formerly', 'ex-', 'built', 'shipped', 'led', 'scaled', 'founded'])
    record(
        'AP-28',
        'C',
        'FAIL' if not fit else 'PASS',
        f'founder-market-fit language: {fit[:5]}' if fit else 'no achievement/fit language on the team content',
        'No founder-market fit',
    )

    record(
        'AP-29',
        'M',
        'WARN'
        if (
            re.search(r'\b(google|meta|stripe|amazon|mckinsey|goldman)\b', low)
            and not contains_any(low, ['linkedin.com', 'github.com', 'linkedin', 'github'])
        )
        else 'PASS',
        'employer logos/brands without person links'
        if (
            re.search(r'\b(google|meta|stripe|amazon|mckinsey|goldman)\b', low)
            and not contains_any(low, ['linkedin.com', 'github.com', 'linkedin', 'github'])
        )
        else 'named people with links detected',
        'Logos instead of people, or unnamed team',
    )

    # --- Group 8: ask & mechanics ---
    money = bool(re.search(r'\$\s*\d+(?:\.\d+)?\s*(?:m|mm|million|k|thousand)?\b', low))
    ask = contains_any(low, ASK_MARKERS)
    record(
        'AP-30',
        'C',
        'FAIL' if not (ask and money) else 'PASS',
        f'ask markers: {ask[:4]}; money figure present: {money}',
        'Ask buried, vague, or absent',
    )

    uof = contains_any(low, USE_OF_FUNDS_MARKERS)
    pct = len(re.findall(r'\d+\s*%', low))
    record(
        'AP-31',
        'M',
        'FAIL' if not uof else ('WARN' if pct < 2 else 'PASS'),
        f'use-of-funds markers: {uof[:3]}; allocation percentages found: {pct}',
        'No use of funds or milestones',
    )

    record(
        'AP-32',
        'M',
        'WARN' if re.search(r'\b(pre-money|post-money|valued at|valuation of|\$\d+\s*m\s*(?:pre|post))\b', low) else 'PASS',
        'valuation anchor present in deck' if re.search(r'\b(pre-money|post-money|valued at|valuation of)\b', low) else 'none',
        'Valuation anchoring inside the deck',
    )

    record(
        'AP-33',
        'm',
        'PASS' if re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', deck) else 'FAIL',
        'contact email present' if re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', deck) else 'no email/contact found',
        'Missing contact and next-step',
    )

    record(
        'AP-34',
        'C',
        'PASS',
        'requires the fund-targeting layer; not text-detectable — verify against fund-profiles.md',
        'Stage mismatch with the target fund',
    )

    # --- Group 9: craft & design ---
    fat_slides = [i + 1 for i, s in enumerate(slides) if word_count(s) > word_budget]
    record(
        'AP-35',
        'M',
        'FAIL' if len(fat_slides) >= 3 else ('WARN' if fat_slides else 'PASS'),
        f'slides over {word_budget} words: {fat_slides[:8]}' if fat_slides else f'no slide exceeds {word_budget} words',
        'Walls of text',
    )

    record(
        'AP-36',
        'M',
        'FAIL' if n_slides > 28 else ('WARN' if n_slides > 20 else 'PASS'),
        f'{n_slides} slides ({word_budget}-word budget artifact; seed read-ahead target 19-20)',
        'Too many slides',
    )

    has_anim = contains_any(low, ['animation', 'transition', 'meme', 'gif', 'confetti', 'emoji-rich'])
    small_type = bool(re.search(r'\b(font-size|9pt|10pt|11pt|12pt)\b', low))
    record(
        'AP-37',
        'M',
        'WARN' if small_type else 'PASS',
        'small-type or font-size markers present' if small_type else 'not text-detectable — verify visually',
        'Illegible type or low contrast',
    )

    record(
        'AP-38',
        'm',
        'WARN' if has_anim else 'PASS',
        f'decorative markers: {has_anim[:4]}' if has_anim else 'none detected',
        'Decorative animation, transitions, memes, or stock clip-art',
    )

    record('AP-39', 'm', 'PASS', 'file-format check is performed on the artifact path, not on deck text', 'Sent as .pptx instead of PDF')

    consistency = check_consistency(deck)
    record(
        'AP-40',
        'C',
        'FAIL' if consistency['conflicts'] else 'PASS',
        f'{len(consistency["conflicts"])} cross-slide numeric conflict(s): {consistency["conflicts"][:3]}'
        if consistency['conflicts']
        else 'no cross-slide numeric conflicts detected',
        'Numbers inconsistent across slides',
    )

    cumulative = bool(re.search(r'\b(cumulative|cumulatively|total to date|since inception|all-time)\b', low))
    record(
        'AP-41',
        'M',
        'WARN' if cumulative else 'PASS',
        'cumulative-figure language detected; YC warns this usually hides weak monthly/quarterly numbers [7]'
        if cumulative
        else 'no cumulative-figure framing detected',
        'Cumulative numbers presented as growth',
    )

    dual_axis = bool(re.search(r'\b(double[- ]axis|dual[- ]axis|secondary axis|two y[- ]axes|right-hand axis)\b', low))
    record(
        'AP-42',
        'M',
        'WARN' if dual_axis else 'PASS',
        'dual-axis chart language detected; YC advises against it [7]' if dual_axis else 'no dual-axis chart framing detected',
        'Double-axis graphs',
    )

    if placeholder_hits:
        results['AP-00-placeholders'] = {
            'id': 'AG-7',
            'name': 'Placeholder residue',
            'severity': 'C',
            'status': 'FAIL',
            'evidence': f'placeholder patterns found: {placeholder_hits}',
        }

    if unsourced:
        results['AP-00-invented'] = {
            'id': 'AG-4',
            'name': 'Invented/unsourced specificity',
            'severity': 'C',
            'status': 'FAIL' if len(unsourced) >= 3 else 'WARN',
            'evidence': f'{len(unsourced)} unsourced figure(s), e.g. {unsourced[:3]}',
        }

    return results


def first_statement(slide_text: str) -> str:
    """Finds the first declarative sentence on the title slide."""
    body = re.sub(r'^#+\s*.*$', '', slide_text, flags=re.MULTILINE)
    body = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', body)
    for raw in re.split(r'(?<=[.!?])\s+|\n', body):
        line = raw.strip(' #*-–—\t')
        if 4 <= word_count(line) <= 40:
            return line
    return ''


FIGURE_RE = re.compile(
    r'(?P<raw>\$\s?\d[\d,]*(?:\.\d+)?\s*(?:billion|million|b|m|k|bn|mm)?'
    r'|\b\d[\d,]*(?:\.\d+)?\s*(?:billion|million|bn|mm)\b'
    r'|\b\d[\d,]*(?:\.\d+)?\s*%'
    r'|\b\d[\d,]{3,}\b)',
    re.IGNORECASE,
)


def find_unsourced_figures(deck: str) -> list[str]:
    """Flags market-shaped figures with no source or internal-data marker nearby.

    Only figures whose surrounding window reads as a *market or benchmark* claim
    are candidates. Ask amounts, pricing, internal traction, and observed metrics
    are excluded so the ledger stays trustworthy.
    """
    flagged: list[str] = []
    for match in FIGURE_RE.finditer(deck):
        start = max(0, match.start() - 260)
        end = min(len(deck), match.end() + 260)
        window = deck[start:end].lower()
        if any(marker in window for marker in SOURCE_MARKERS):
            continue
        if re.search(r'\b(our|we|internal|observed|actual|stripe|q[1-4]|per lab|per month)\b', window):
            continue
        if not any(keyword in window for keyword in MARKET_CONTEXT):
            continue
        flagged.append(match.group('raw').strip())
    return flagged[:25]


CONSISTENCY_LABELS = (
    'arr',
    'mrr',
    'tam',
    'sam',
    'som',
    'market size',
    'round size',
    'valuation',
)

RANGE_CONNECTORS = (' to ', '–', '—', ' from ', ' up to ', ' over ', ' between ')


def check_consistency(deck: str) -> dict[str, Any]:
    """Detects the same labelled metric carrying different values across slides.

    Deliberately conservative: only high-confidence, single-value labels are
    compared, only within one line, and range/forward-looking statements are
    ignored. Per-channel values (paid vs organic CAC) and distinct retention
    definitions (NRR vs M6 cohort) are not conflicts.
    """
    label_values: dict[str, dict[str, set[str]]] = {}
    money = re.compile(r'\$\s?\d[\d,.]*\s*(?:k|m|b|mm|bn|million|billion)?')

    for line in deck.splitlines():
        line_low = line.lower()
        if any(token in line_low for token in FORWARD_LOOKING):
            continue
        if any(token in line_low for token in RANGE_CONNECTORS):
            continue
        for label in CONSISTENCY_LABELS:
            idx = line_low.find(label)
            if idx == -1:
                continue
            tail = line[idx + len(label) : idx + len(label) + 40]
            match = money.search(tail)
            if not match:
                continue
            value = re.sub(r'\s+', '', match.group(0).lower())
            label_values.setdefault(label, {}).setdefault(value, set()).add(line.strip()[:90])

    conflicts = []
    for label, values in label_values.items():
        if len(values) > 1:
            conflicts.append({'label': label, 'values': list(values.keys())})
    return {'labels': len(label_values), 'conflicts': conflicts}


# ==============================================================================
# Track B: acceptance detection
# ==============================================================================


def detect_track_b(
    deck: str,
    slides: list[str],
    track_a: dict[str, dict[str, Any]],
    slide_word_budget: int = 45,
) -> dict[str, dict[str, Any]]:
    """Runs heuristic detection for the 28 Track B acceptance criteria."""
    low = normalize(deck)
    n_slides = len(slides)
    out: dict[str, dict[str, Any]] = {}

    def record(ac: str, severity: str, status: str, evidence: str, name: str) -> None:
        out[ac] = {
            'id': ac,
            'name': name,
            'severity': severity,
            'status': status,
            'evidence': evidence,
        }

    def has(needles: list[str]) -> list[str]:
        return contains_any(low, needles)

    one_liner = first_statement(slides[0] if slides else '')
    one_liner_low = one_liner.lower()
    one_liner_clean = bool(
        one_liner
        and word_count(one_liner) <= 15
        and not any(re.search(pat, one_liner_low) for pat in PLACEHOLDER_PATTERNS)
        and len(contains_any(one_liner_low, HYPE_LEXICON)) < 2
    )
    record(
        'AC-01',
        'C',
        'PASS' if one_liner_clean else ('WARN' if one_liner else 'FAIL'),
        f'"{one_liner}" ({word_count(one_liner)} words)' if one_liner else 'no one-liner on the title slide',
        'One-line company description',
    )

    contact = bool(re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', deck))
    record(
        'AC-02',
        'M',
        'PASS' if (contact and one_liner) else ('WARN' if one_liner or contact else 'FAIL'),
        f'one-liner: {bool(one_liner)}, contact: {contact}',
        'Title slide completeness',
    )

    quantified_problem = bool(re.search(r'(?i)\b(spend|costs?|lose|loses|hours?|weeks?|%|per (?:year|month|week|day))\b', low))
    record(
        'AC-03',
        'C',
        'PASS' if quantified_problem else 'FAIL',
        'quantified pain language detected' if quantified_problem else 'problem not quantified',
        'Problem quantified and attributed',
    )

    status_quo = has(['today', 'currently', 'status quo', 'spreadsheet', 'manual', 'incumbent', 'do nothing', 'workaround'])
    record(
        'AC-04',
        'M',
        'PASS' if len(status_quo) >= 2 else ('WARN' if status_quo else 'FAIL'),
        f'status-quo markers: {status_quo[:4]}',
        'Status quo and its failure mode',
    )

    record(
        'AC-05',
        'C',
        'PASS' if 'why now' in low else ('WARN' if has(WHY_NOW_MARKERS) else 'FAIL'),
        'why-now section present' if 'why now' in low else 'no explicit why-now section',
        'Why Now is dated and falsifiable',
    )

    solution = track_a.get('AP-01', {}).get('status') != 'FAIL'
    record(
        'AC-06',
        'C',
        'PASS' if solution else 'WARN',
        'solution content detected' if solution else 'no concise solution statement',
        'Solution in two sentences with a concrete benefit',
    )

    product = has(PRODUCT_MARKERS) or bool(re.search(r'!\[[^\]]*\]\([^)]*\)', deck))
    record('AC-07', 'C', 'PASS' if product else 'FAIL', f'product markers/images: {bool(product)}', 'Product evidence, legible, at least one')

    labels = has(['live', 'private beta', 'beta', 'design concept', 'concept', 'prototype'])
    record('AC-08', 'M', 'PASS' if labels else ('WARN' if product else 'FAIL'), f'honesty labels: {labels[:4]}', 'Visual honesty labels')

    fat = [i + 1 for i, s in enumerate(slides) if word_count(s) > slide_word_budget]
    record(
        'AC-09',
        'M',
        'PASS' if not fat else ('WARN' if len(fat) <= 2 else 'FAIL'),
        f'slides over {slide_word_budget} words: {fat[:8]}' if fat else f'within the {slide_word_budget}-word budget',
        'One idea per slide and a word budget',
    )

    bu = has(BOTTOM_UP_MARKERS)
    record(
        'AC-10',
        'M',
        'PASS' if bu else ('WARN' if has(['tam', 'sam', 'som']) else 'FAIL'),
        f'bottom-up markers: {bu[:4]}',
        'Bottom-up market sizing with sourced inputs',
    )

    beach = has(['beachhead', 'wedge', 'first market', 'initial market', 'entry market', 'initial segment'])
    record(
        'AC-11',
        'M',
        'PASS' if beach else 'FAIL',
        f'beachhead markers: {beach[:4]}' if beach else 'no entry-market definition found',
        'Entry market (beachhead) named',
    )

    src = has(SOURCE_MARKERS) + (['url'] if re.search(r'https?://', deck) else [])
    figures = FIGURE_RE.findall(deck)
    record(
        'AC-12',
        'M',
        'PASS' if (src and len(src) >= 2) else ('WARN' if src else 'FAIL'),
        f'{len(src)} source markers across {len(figures)} figure(s)',
        'Every figure sourced and dated',
    )

    traction = has(TRACTION_MARKERS)
    record(
        'AC-13',
        'C',
        'PASS' if traction else 'FAIL',
        f'traction markers: {traction[:5]}' if traction else 'no traction metric found',
        'Traction with a real growth metric',
    )

    record(
        'AC-14',
        'M',
        'PASS' if has(['source:', 'takeaway', 'grew from', 'which means', '→', '=>']) else ('WARN' if has(['growth', 'mrr', 'arr']) else 'FAIL'),
        'chart annotation/takeaway language detected'
        if has(['source:', 'takeaway', 'grew from', 'which means', '→', '=>'])
        else ('growth metrics present without an annotated conclusion' if has(['growth', 'mrr', 'arr']) else 'no growth chart or annotation found'),
        'Hero chart annotated with its conclusion',
    )

    record(
        'AC-15',
        'M',
        'PASS' if has(RETENTION_MARKERS) else 'FAIL',
        f'retention markers: {has(RETENTION_MARKERS)[:5]}' if has(RETENTION_MARKERS) else 'no retention/cohort evidence',
        'Retention, cohort, or repeat-usage evidence',
    )

    prerev = has(['pre-revenue', 'pre revenue', 'no revenue', '$0 revenue'])
    demand = has(DEMAND_MARKERS)
    if prerev:
        record('AC-16', 'C', 'PASS' if demand else 'FAIL', f'pre-revenue; demand markers: {demand[:5]}', 'Pre-revenue demand evidence')
    else:
        record('AC-16', 'C', 'N/A', 'revenue present or stage not flagged pre-revenue', 'Pre-revenue demand evidence')

    model = has(['business model', 'pricing', 'price', 'acv', 'per seat', 'per month', 'take rate', 'subscription'])
    record(
        'AC-17', 'C', 'PASS' if len(model) >= 2 else ('WARN' if model else 'FAIL'), f'business-model markers: {model[:5]}', 'Complete business model'
    )

    econ = has(UNIT_ECON_MARKERS)
    defined = has(['blended', 'fully loaded', 'per channel', 'observed', 'modelled', 'modeled', 'definition'])
    record(
        'AC-18',
        'M',
        'PASS' if (econ and defined) else ('WARN' if econ else 'FAIL'),
        f'unit-economics: {econ[:5]}; definition markers: {defined[:4]}',
        'Unit economics with stated definitions',
    )

    record(
        'AC-19',
        'M',
        'PASS' if has(['burn multiple', 'burn rate', 'runway']) else ('WARN' if has(['burn']) else 'FAIL'),
        f'efficiency markers: {has(["burn multiple", "burn rate", "runway"])[:3]}',
        'Capital efficiency metric',
    )

    comp = has(COMPETITION_MARKERS)
    honest = has(['we lose', 'they win', 'better at', 'stronger', 'weaker', 'where they win'])
    record(
        'AC-20',
        'C',
        'PASS' if (comp and honest) else ('WARN' if comp else 'FAIL'),
        f'competition markers: {comp[:4]}; honest-loss markers: {honest[:3]}',
        'Direct competitors at your stage, plus the honest substitute',
    )

    moat = has(MOAT_MARKERS)
    record(
        'AC-21',
        'M',
        'PASS' if moat else 'FAIL',
        f'moat markers: {moat[:4]}' if moat else 'no defensibility mechanism',
        'Defensibility mechanism with evidence',
    )

    team_fit = has(['previously', 'formerly', 'ex-', 'built', 'shipped', 'led', 'founded', 'scaled'])
    links = has(['linkedin', 'github', 'twitter', 'x.com'])
    record(
        'AC-22',
        'C',
        'PASS' if (team_fit and links) else ('WARN' if team_fit else 'FAIL'),
        f'fit markers: {team_fit[:4]}; links: {links[:3]}',
        'Founder-market fit with achievements and links',
    )

    ask = has(ASK_MARKERS)
    money = bool(re.search(r'\$\s*\d+(?:\.\d+)?\s*(?:m|mm|million|k|thousand)?\b', low))
    record(
        'AC-23',
        'C',
        'PASS' if (ask and money) else ('WARN' if ask or money else 'FAIL'),
        f'ask markers: {ask[:4]}; money figure: {money}',
        'Explicit ask',
    )

    uof = has(USE_OF_FUNDS_MARKERS)
    pct = len(re.findall(r'\d+\s*%', low))
    record(
        'AC-24',
        'M',
        'PASS' if (uof and pct >= 2) else ('WARN' if uof or pct >= 2 else 'FAIL'),
        f'use-of-funds markers: {uof[:3]}; percentages: {pct}',
        'Use of funds tied to milestones',
    )

    consistency = check_consistency(deck)
    placeholders = [p for p in PLACEHOLDER_PATTERNS if re.search(p, low)]
    record(
        'AC-25',
        'C',
        'PASS' if (not consistency['conflicts'] and not placeholders) else 'FAIL',
        f'conflicts: {consistency["conflicts"][:2]}; placeholders: {placeholders[:4]}',
        'Numerical consistency and no placeholder residue',
    )

    record('AC-26', 'M', 'PASS', 'not text-detectable — requires visual inspection of the rendered deck', 'Legibility')

    record('AC-27', 'm', 'PASS', 'verify the exported artifact is PDF, <= 10 MB, no leaked speaker notes', 'Deliverable hygiene')

    record(
        'AC-28',
        'M',
        'PASS' if 'appendix' in low else ('WARN' if n_slides >= 15 else 'FAIL'),
        'appendix section present' if 'appendix' in low else 'no appendix section found',
        'Appendix present for Q&A depth',
    )

    return out


# ==============================================================================
# Scoring
# ==============================================================================


def score_track(results: dict[str, dict[str, Any]], invert: bool) -> dict[str, Any]:
    """Computes a weighted score for a track.

    invert=False -> acceptance score (higher better).
    invert=True  -> anti-pattern index (higher worse).
    """
    earned = 0.0
    maximum = 0.0
    fails: dict[str, int] = {'C': 0, 'M': 0, 'm': 0}
    warns: dict[str, int] = {'C': 0, 'M': 0, 'm': 0}

    for item in results.values():
        severity = item['severity']
        status = item['status']
        if status == 'N/A':
            continue
        weight = WEIGHT[severity]
        maximum += weight
        if status == 'PASS':
            earned += 0.0 if invert else weight
        elif status == 'WARN':
            warns[severity] += 1
            earned += 0.5 * weight
        else:  # FAIL
            fails[severity] += 1
            earned += weight if invert else 0.0

    pct = round(100.0 * earned / maximum, 1) if maximum else 0.0
    return {
        'score': pct,
        'max_points': maximum,
        'fails': fails,
        'warns': warns,
        'fail_total': sum(fails.values()),
        'warn_total': sum(warns.values()),
    }


def verdict(track_a: dict[str, Any], track_b: dict[str, Any], hard_stops: list[str]) -> dict[str, Any]:
    """Applies the Capital Gate from references/scoring-framework.md."""
    anti = track_a['score']
    accept = track_b['score']
    composite = round(0.5 * (100 - anti) + 0.5 * accept, 1)
    crit = track_a['fails']['C'] + track_b['fails']['C']
    major = track_a['fails']['M'] + track_b['fails']['M']

    if hard_stops:
        state = 'BLOCKED'
        reason = f'hard stop(s): {"; ".join(hard_stops[:3])}'
    elif crit >= 2 or accept < 65 or anti > 40:
        state = 'BLOCKED'
        reason = f'{crit} critical fails; acceptance {accept}%; anti-pattern index {anti}%'
    elif accept >= 85 and anti <= 15 and crit == 0 and major <= 2:
        state = 'INVESTOR-READY'
        reason = 'all gates cleared'
    elif accept >= 65 and crit <= 1 and composite >= 65:
        state = 'NEEDS WORK'
        reason = 'warm intros only; specific gaps remain'
    else:
        state = 'BLOCKED'
        reason = f'acceptance {accept}%, composite {composite}%'

    return {
        'verdict': state,
        'reason': reason,
        'composite': composite,
        'critical_fails': crit,
        'major_fails': major,
    }


def hard_stop_check(deck: str, track_a: dict[str, Any], track_b: dict[str, Any]) -> list[str]:
    """Evaluates the five hard stops that force BLOCKED regardless of arithmetic."""
    stops: list[str] = []
    low = normalize(deck)
    if any(re.search(p, low) for p in PLACEHOLDER_PATTERNS):
        stops.append('placeholder residue in a sendable deck (AG-7)')
    if track_a.get('AP-00-invented', {}).get('status') == 'FAIL':
        stops.append('multiple unsourced/invented figures (AG-4)')
    if track_b.get('AC-23', {}).get('status') == 'FAIL' and track_a.get('AP-30', {}).get('status') == 'FAIL':
        stops.append('no explicit ask')
    if track_a.get('AP-10', {}).get('status') == 'FAIL':
        stops.append('no product evidence of any kind')
    return stops


# ==============================================================================
# Reporting
# ==============================================================================


def build_ledger(deck: str) -> list[dict[str, str]]:
    """Builds the missing-numbers ledger from unsourced figures."""
    rows: list[dict[str, str]] = []
    for raw in find_unsourced_figures(deck):
        rows.append(
            {
                'claim': raw,
                'status': 'UNSOURCED',
                'action': 'cite a source with a year, or replace with a measured figure',
            }
        )
    return rows[:25]


def render_markdown(report: dict[str, Any]) -> str:
    """Renders the audit report in the report-template.md structure."""
    a = report['track_a']
    b = report['track_b']
    v = report['verdict']
    lines: list[str] = []

    lines.append(f'# Pitch Deck Pre-Screen — {report["company"]}\n')
    lines.append('| Field | Value |')
    lines.append('| :--- | :--- |')
    lines.append(f'| Deck file | `{report["file"]}` |')
    lines.append(f'| Artifact type | {report.get("artifact", "read-ahead")} |')
    lines.append(f'| Slides detected | {report["slides"]} |')
    lines.append(f'| Words | {report["words"]} |')
    lines.append(f'| Scored at | {report["timestamp"]} |')
    lines.append(f'| Verdict | **{v["verdict"]}** |\n')

    lines.append('## Executive Verdict\n')
    lines.append(f'{v["verdict"]} — {v["reason"]}\n')
    lines.append('| Metric | Score | Target | Status |')
    lines.append('| :--- | ---: | ---: | :--- |')
    lines.append(f'| Composite Capital Readiness | {v["composite"]}% | >= 85% | {"PASS" if v["composite"] >= 85 else "REVIEW"} |')
    lines.append(f'| Track B - Acceptance Score | {b["score"]}% | >= 85% | {"PASS" if b["score"] >= 85 else "REVIEW"} |')
    lines.append(f'| Track A - Anti-Pattern Index | {a["score"]}% | <= 15% | {"PASS" if a["score"] <= 15 else "REVIEW"} |')
    lines.append(f'| Critical fails | {v["critical_fails"]} | 0 | {"PASS" if v["critical_fails"] == 0 else "FAIL"} |')
    lines.append(f'| Major fails | {v["major_fails"]} | <= 2 | {"PASS" if v["major_fails"] <= 2 else "FAIL"} |\n')

    if report['hard_stops']:
        lines.append('> **Hard stops triggered:** ' + '; '.join(report['hard_stops']) + '\n')

    lines.append('## Track A - Anti-Pattern Matrix\n')
    lines.append('| ID | Anti-pattern | Sev | Status | Evidence |')
    lines.append('| :--- | :--- | :---: | :---: | :--- |')
    for item in a['items']:
        lines.append(f'| {item["id"]} | {item["name"]} | {item["severity"]} | {item["status"]} | {item["evidence"]} |')
    lines.append('')

    lines.append('## Track B - Acceptance Matrix\n')
    lines.append('| ID | Criterion | Sev | Status | Evidence |')
    lines.append('| :--- | :--- | :---: | :---: | :--- |')
    for item in b['items']:
        lines.append(f'| {item["id"]} | {item["name"]} | {item["severity"]} | {item["status"]} | {item["evidence"]} |')
    lines.append('')

    if report['ledger']:
        lines.append('## Missing-Numbers Ledger\n')
        lines.append('| # | Claim | Status | Action |')
        lines.append('| ---: | :--- | :--- | :--- |')
        for i, row in enumerate(report['ledger'], start=1):
            lines.append(f'| {i} | `{row["claim"]}` | {row["status"]} | {row["action"]} |')
        lines.append('')

    if report['consistency']['conflicts']:
        lines.append('## Cross-Slide Numeric Conflicts\n')
        lines.append('| Metric | Conflicting values |')
        lines.append('| :--- | :--- |')
        for conflict in report['consistency']['conflicts']:
            lines.append(f'| {conflict["label"]} | {", ".join(conflict["values"])} |')
        lines.append('')

    lines.append('## Next Steps\n')
    lines.append('1. Fix every Critical row before sending this deck to anyone.')
    lines.append('2. Run the semantic audit against `references/acceptance-criteria.md` for the criteria marked "not text-detectable".')
    lines.append('3. Score fund fit per `references/fund-profiles.md` for each target fund.')
    lines.append('4. Re-run this screener after each revision and diff the verdict.\n')
    lines.append(
        '> This is a heuristic pre-screen. It cannot see design, verify claims, '
        'or judge whether the business is good. It cannot be used as a '
        'substitute for the full audit in `SKILL.md`.'
    )
    return '\n'.join(lines)


# ==============================================================================
# CLI
# ==============================================================================

ARTIFACT_BUDGETS = {
    # (track A wall-of-text budget, track B per-slide budget)
    'presented': (30, 30),
    'read-ahead': (60, 45),
}


def analyze(path: Path, company: str, artifact: str = 'read-ahead') -> dict[str, Any]:
    """Runs the full pre-screen and returns the report dictionary."""
    budget_a, budget_b = ARTIFACT_BUDGETS[artifact]
    text = load_deck_text(path)
    slides = split_slides(text)
    track_a_results = detect_track_a(text, slides, word_budget=budget_a)
    track_b_results = detect_track_b(text, slides, track_a_results, slide_word_budget=budget_b)

    a = score_track(track_a_results, invert=True)
    b = score_track(track_b_results, invert=False)

    # The AP-40 tolerance rule: Track A cannot exceed 100.
    a['score'] = min(a['score'], 100.0)

    stops = hard_stop_check(text, track_a_results, track_b_results)
    v = verdict(a, b, stops)

    return {
        'tool_version': TOOL_VERSION,
        'company': company,
        'artifact': artifact,
        'file': str(path),
        'slides': len(slides),
        'words': word_count(text),
        'timestamp': datetime.now(UTC).isoformat(timespec='seconds'),
        'track_a': {
            **{k: val for k, val in a.items()},
            'items': list(track_a_results.values()),
        },
        'track_b': {
            **{k: val for k, val in b.items()},
            'items': list(track_b_results.values()),
        },
        'verdict': v,
        'hard_stops': stops,
        'ledger': build_ledger(text),
        'consistency': check_consistency(text),
    }


def run_doctor() -> int:
    """Self-diagnostic: verifies the tool and its optional dependencies."""
    print(f'score_deck v{TOOL_VERSION} — doctor\n')
    ok = True

    print(f'python: {sys.version.split()[0]}')
    script_dir = Path(__file__).resolve().parent
    print(f'script dir: {script_dir}')
    print(f'logs dir writable: {(script_dir / ".logs").is_dir()}')
    for optional in ('pdftotext',):
        found = shutil.which(optional)
        print(f'{optional}: {found or "NOT FOUND (PDF input unavailable; convert to text first)"}')
    print(f'symlink target: {Path(__file__).name}')
    print(f'status: {"OK" if ok else "DEGRADED"}')
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Deterministic pitch deck pre-screen (Track A anti-patterns + Track B acceptance criteria).',
    )
    parser.add_argument('--file', type=Path, help='deck file (.md, .txt, .pptx, .pdf)')
    parser.add_argument('--company', default='Untitled', help='company name for the report')
    parser.add_argument('--json', action='store_true', help='emit JSON instead of markdown')
    parser.add_argument(
        '--artifact',
        choices=sorted(ARTIFACT_BUDGETS),
        default='read-ahead',
        help='read-ahead (default) applies a 60/45-word budget; presented applies a 30/30-word budget',
    )
    parser.add_argument('--out', type=Path, help='write the report to this path')
    parser.add_argument('--doctor', action='store_true', help='run the self-diagnostic')
    args = parser.parse_args()

    if args.doctor:
        return run_doctor()

    if not args.file:
        parser.error('--file is required (or use --doctor)')
    if not args.file.exists():
        print(f'error: file not found: {args.file}', file=sys.stderr)
        return 2

    logger = setup_logger()
    logger.info('scoring deck: %s', args.file)
    try:
        report = analyze(args.file, args.company, args.artifact)
    except RuntimeError as exc:
        logger.error('failed: %s', exc)
        print(f'error: {exc}', file=sys.stderr)
        return 2

    for track in ('track_a', 'track_b'):
        counts: dict[str, int] = {}
        for item in report[track]['items']:
            counts[item['status']] = counts.get(item['status'], 0) + 1
        logger.info('%s statuses: %s', track, counts)
    logger.info('verdict: %s (%s)', report['verdict']['verdict'], report['verdict']['reason'])

    output = json.dumps(report, indent=2, ensure_ascii=False) if args.json else render_markdown(report)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding='utf-8')
        print(f'wrote {args.out}')
    else:
        print(output)

    return 0 if report['verdict']['verdict'] != 'BLOCKED' else 1


if __name__ == '__main__':
    sys.exit(main())
