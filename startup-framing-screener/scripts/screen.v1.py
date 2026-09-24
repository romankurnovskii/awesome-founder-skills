#!/usr/bin/env python3
"""Startup Framing Screener - deterministic band diagnostics for startup text.

Implements the *published* thresholds, Exit Ratios, Exit Deltas, and the Hyping
Score formula from arXiv:2608.00045 (Saruggia & Germano, 2026).

This tool is deliberately NOT a predictive model. The paper does not publish
its trained logistic-regression coefficients, its probability threshold, or its
dictionaries. So this script reports which band each measured feature falls
into against the paper's published Tables VII and VIII, and how far the text
sits from the paper's BEST bands. It never outputs P(exit).

Changelog:
  - v1.0.0: Initial implementation. Dictionary-based densities + length
    measures + binary flags; POS-based densities computed only when spaCy is
    installed.

Usage:
    python3 screen.py --name "Etemaro" \
        --statement "Autonomous DLMM execution for Solana liquidity providers." \
        --website "https://etemaro.com"

    python3 screen.py --name X --statement Y --website Z --json
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.resolve() / '.logs'
MARKER_FILE = Path(__file__).parent.resolve().parent / 'references' / 'hyping-markers.md'

# ---------------------------------------------------------------------------
# Published thresholds - arXiv:2608.00045, Table VII and Table VIII (v4).
# Global Exit average = 10.38%. Deltas are percentage points vs that baseline.
# Bands are (low, high) in the feature's own unit: ratio (0-1) for densities,
# words for statement length, characters for name/website length.
# ---------------------------------------------------------------------------

# fmt: off
# The blocks in this region are transcribed data tables. They are kept in a
# compact, column-grouped layout so published bands can be compared by scanning a
# row across features. The formatter would explode each entry to one kwarg per
# line and destroy that readability, so formatting is disabled here only.
FEATURES = {
    "buzzword_density": dict(
        unit="ratio", min_band=(0.00, 0.03), min_delta=47.5,
        best_band=(0.30, 0.36), best_delta=None,
        max_band=(0.36, 0.45), max_delta=1.4,
        note="best band is mid-range, NOT the maximum",
    ),
    "jargon_density": dict(
        unit="ratio", min_band=(0.00, 0.03), min_delta=3.7,
        best_band=(0.21, 0.27), best_delta=89.9,
        max_band=(0.21, 0.27), max_delta=89.9,
        note="BEST == MAX",
    ),
    "acronym_density": dict(
        unit="ratio", min_band=(0.00, 0.01), min_delta=7.9,
        best_band=(0.00, 0.01), best_delta=7.9,
        max_band=(0.10, 0.12), max_delta=-0.3,
        note="BEST == MIN; technical density reads as static",
    ),
    "frequent_density": dict(
        unit="ratio", min_band=(0.00, 0.07), min_delta=80.9,
        best_band=(0.68, 0.82), best_delta=172.1,
        max_band=(0.68, 0.82), max_delta=172.1,
        note="BEST == MAX; highest single delta in the study",
    ),
    "adjective_density": dict(
        unit="ratio", min_band=(0.00, 0.04), min_delta=20.1,
        best_band=(0.29, 0.36), best_delta=119.6,
        max_band=(0.29, 0.36), max_delta=119.6,
        note="BEST == MAX",
    ),
    "noun_density": dict(
        unit="ratio", min_band=(0.12, 0.22), min_delta=125.8,
        best_band=(0.12, 0.22), best_delta=125.8,
        max_band=(1.00, 1.01), max_delta=100.2,
        note="BEST == MIN",
    ),
    "value_density": dict(
        unit="ratio", min_band=(0.00, 0.02), min_delta=4.9,
        best_band=(0.13, 0.17), best_delta=64.5,
        max_band=(0.13, 0.17), max_delta=64.5,
        note="BEST == MAX",
    ),
    "verb_density": dict(
        unit="ratio", min_band=(0.00, 0.05), min_delta=88.7,
        best_band=(0.45, 0.54), best_delta=122.4,
        max_band=(0.45, 0.54), max_delta=122.4,
        note="BEST == MAX",
    ),
    "statement_length": dict(
        unit="words", min_band=(2, 37), min_delta=11.7,
        best_band=(2, 37), best_delta=11.7,
        max_band=(151, 180), max_delta=-22.1,
        note="BEST == MIN; brevity wins",
    ),
    "name_length": dict(
        unit="chars", min_band=(3, 6), min_delta=7.2,
        best_band=(3, 6), best_delta=7.2,
        max_band=(15, 19), max_delta=-23.6,
        note="BEST == MIN",
    ),
    "website_length": dict(
        unit="chars", min_band=(3, 4), min_delta=9.8,
        best_band=(16, 17), best_delta=None,
        max_band=(18, 20), max_delta=-84.7,
        note="most punishing MAX band in the study",
    ),
}

# Binary features - Table VII. Value is the Exit Delta when the flag is TRUE.
BINARY_FEATURES = {
    "founding_year_mention": dict(
        delta=34.6, good=True, detail="a founding year in the statement helps"),
    "website_mention": dict(
        delta=22.7, good=True, detail="naming the website inside the statement helps"),
    "com_domain": dict(
        delta=20.9, good=True, detail="a .com domain outperforms other TLDs"),
    "website_name_equivalence": dict(
        delta=11.8, good=True, detail="matching website and name lengths is mildly positive"),
    "location_mention": dict(
        delta=-26.0, good=False, detail="naming a physical location hurts"),
}

# Feature-level importance from Table V (top 8), used as the `s` weights.
IMPORTANCE = {
    "statement_length": 0.0332,
    "noun_density": 0.0230,
    "verb_density": 0.0208,
    "frequent_density": 0.0205,
    "buzzword_density": 0.0187,
    "jargon_density": 0.0181,
    "adjective_density": 0.0178,
    "acronym_density": None,  # not in the paper's top-8; gets the mean weight
    "value_density": None,
}
# fmt: on

# Denominator normalising statement length into [0,1] for the Hyping Score.
STATEMENT_LENGTH_CAP = 180

# Densities that require POS tagging; unavailable when spaCy is absent.
POS_FEATURES = ('adjective_density', 'verb_density', 'noun_density', 'value_density')

# Small location lexicon. The paper does not publish its location list, so this
# is an approximation and is documented as such.
LOCATION_TERMS = {
    'us',
    'usa',
    'united',
    'states',
    'america',
    'american',
    'canada',
    'canadian',
    'germany',
    'german',
    'israel',
    'israeli',
    'uk',
    'britain',
    'british',
    'england',
    'london',
    'france',
    'french',
    'paris',
    'spain',
    'madrid',
    'italy',
    'milan',
    'india',
    'indian',
    'bangalore',
    'singapore',
    'australia',
    'sydney',
    'brazil',
    'china',
    'chinese',
    'japan',
    'tokyo',
    'korea',
    'seoul',
    'netherlands',
    'amsterdam',
    'berlin',
    'munich',
    'tel',
    'aviv',
    'jerusalem',
    'haifa',
    'york',
    'francisco',
    'boston',
    'austin',
    'seattle',
    'chicago',
    'toronto',
    'vancouver',
    'dubai',
    'uae',
    'zurich',
    'stockholm',
    'oslo',
    'copenhagen',
    'dublin',
    'lisbon',
    'warsaw',
    'prague',
    'vienna',
    'moscow',
    'kiev',
    'kyiv',
}

YEAR_RE = re.compile(r'\b(?:19|20)\d{2}\b')


# ---------------------------------------------------------------------------
# Dictionary loading
# ---------------------------------------------------------------------------


def load_markers(path: Path = MARKER_FILE) -> dict:
    """Parse references/hyping-markers.md into {section_name: [terms]}."""
    if not path.exists():
        raise FileNotFoundError(f'marker file not found: {path}. It ships with the skill at references/hyping-markers.md')
    sections = {}
    current = None
    for raw in path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if line.startswith('## '):
            current = line[3:].strip().lower().replace(' ', '_')
            sections.setdefault(current, [])
        elif line.startswith('- ') and current:
            term = line[2:].strip().lower()
            if term and term not in sections[current]:
                sections[current].append(term)
    return sections


def normalise(text: str) -> str:
    """Lowercase and flatten hyphens/slashes so 'API-first' == 'api first'."""
    return re.sub(r'[-/]', ' ', text.lower())


def tokenize(text: str) -> list:
    return re.findall(r'[a-z0-9]+', normalise(text))


class MarkerMatcher:
    """Counts dictionary hits in a normalised token stream."""

    def __init__(self, terms):
        self.single = set()
        self.phrases = []
        for term in terms:
            flat = normalise(term).strip()
            if not flat:
                continue
            if ' ' in flat:
                self.phrases.append(re.compile(rf'\b{re.escape(flat)}\b'))
            else:
                self.single.add(flat)

    def count(self, tokens, norm_text: str) -> int:
        hits = sum(1 for t in tokens if t in self.single)
        hits += sum(len(p.findall(norm_text)) for p in self.phrases)
        return hits


# ---------------------------------------------------------------------------
# Measurement
# ---------------------------------------------------------------------------


POS_INSTALL_HINT = 'pip install spacy && python -m spacy download en_core_web_sm'


def dependency_status() -> dict:
    """Report optional-capability status without raising or printing tracebacks.

    Call this - or ``screen.py --doctor`` - instead of probing with your own
    ``import`` statements. A bare ``python3 -c "import spacy"`` emits a
    traceback, which looks like a failure but is not one: those four features are
    optional, and the other seven always work without any third-party package.
    """
    status = {
        'spacy': {'installed': False, 'version': None, 'model': False},
        'pos_features_available': False,
    }
    try:
        import spacy  # type: ignore
    except ImportError:
        return status
    status['spacy']['installed'] = True
    status['spacy']['version'] = getattr(spacy, '__version__', 'unknown')
    try:
        spacy.load('en_core_web_sm')
    except OSError:
        return status
    status['spacy']['model'] = True
    status['pos_features_available'] = True
    return status


def doctor_report() -> dict:
    """Assemble a capability report: what works, what is optional, and why."""
    deps = dependency_status()
    try:
        markers = load_markers()
        dictionaries = {k: len(v) for k, v in sorted(markers.items())}
        marker_error = None
    except (FileNotFoundError, ValueError) as exc:
        dictionaries = {}
        marker_error = str(exc)

    return {
        'python': sys.version.split()[0],
        'script': str(Path(__file__).resolve()),
        'marker_file': str(MARKER_FILE),
        'marker_file_exists': MARKER_FILE.exists(),
        'dictionaries': dictionaries,
        'marker_error': marker_error,
        'core_features': 'always available - no third-party dependencies',
        'optional_features': list(POS_FEATURES),
        'optional_features_reason': (
            None if deps['pos_features_available'] else 'spaCy or en_core_web_sm is missing. Install with: ' + POS_INSTALL_HINT
        ),
        'dependencies': deps,
    }


def render_doctor(info: dict) -> str:
    out = []
    add = out.append
    add('=' * 70)
    add('STARTUP FRAMING SCREENER - CAPABILITY CHECK')
    add('=' * 70)
    add('python      : {}'.format(info['python']))
    add('script      : {}'.format(info['script']))
    add('')
    add('marker file : {}'.format(info['marker_file']))
    if info['marker_file_exists']:
        add('              OK')
    else:
        add('              MISSING - {}'.format(info['marker_error']))
    if info['dictionaries']:
        add('dictionaries:')
        for name, count in info['dictionaries'].items():
            add(f'              {name:<16} {count} terms')
    add('')
    deps = info['dependencies']
    add('-' * 70)
    add('CORE FEATURES')
    add('-' * 70)
    add('  {}'.format(info['core_features']))
    add('  statement_length, name_length, website_length, buzzword/jargon/')
    add('  acronym/frequent density, and all binary flags.')
    add('')
    add('-' * 70)
    add('OPTIONAL FEATURES')
    add('-' * 70)
    add('  {}'.format(', '.join(info['optional_features'])))
    if deps['pos_features_available']:
        add('  AVAILABLE - spaCy {} with en_core_web_sm'.format(deps['spacy']['version']))
    else:
        add('  NOT AVAILABLE')
        add('  spaCy installed : %s' % ('yes' if deps['spacy']['installed'] else 'no'))
        add('  model present   : %s' % ('yes' if deps['spacy']['model'] else 'no'))
        add('')
        add('  This is NOT an error. The screen runs fine without it; those four')
        add("  features simply report as 'not measured'.")
        add('')
        add(f'  To enable them: {POS_INSTALL_HINT}')
        add('  Ask the user before installing anything into their environment.')
    add('=' * 70)
    return '\n'.join(out)


def pos_densities(statement: str):
    """Adjective/Verb/Noun/Value densities via spaCy when available.

    The paper's POS pipeline is not published, so even with spaCy these are an
    approximation. Returns None when spaCy is unavailable.
    """
    try:
        import spacy  # type: ignore
    except ImportError:
        return None
    try:
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        return None

    doc = nlp(statement)
    total = sum(1 for t in doc if t.is_alpha or t.like_num)
    if total == 0:
        return None
    counts = {'adjective_density': 0, 'verb_density': 0, 'noun_density': 0, 'value_density': 0}
    for token in doc:
        if token.pos_ == 'ADJ':
            counts['adjective_density'] += 1
        elif token.pos_ in ('VERB', 'AUX'):
            counts['verb_density'] += 1
        elif token.pos_ in ('NOUN', 'PROPN'):
            counts['noun_density'] += 1
        elif token.pos_ == 'NUM':
            counts['value_density'] += 1
    return {k: v / total for k, v in counts.items()}


def website_host(website) -> str:
    """Normalise a website input to its bare host.

    The study does not state whether its "Website Length" feature measured the
    raw URL field or the bare domain. We measure the HOST only, so the value
    does not change depending on whether the caller typed the scheme, a path,
    a query string, or a trailing slash. Measuring the raw input would let the
    same domain score differently on formatting alone - which would turn a
    measurement into something a user could game by retyping the URL.
    """
    raw = (website or '').strip().lower()
    raw = re.sub(r'^[a-z][a-z0-9+.-]*://', '', raw)  # strip scheme
    raw = raw.split('/')[0].split('?')[0].split('#')[0]
    raw = raw.split('@')[-1]  # strip credentials
    raw = raw.removeprefix('www.')
    raw = raw.split(':')[0]  # strip port
    return raw


def measure(name, statement: str, website, markers: dict) -> dict:
    """Measure all features. ``name`` and ``website`` may be None when the user
    has not supplied them; the dependent features report as not measured rather
    than being guessed."""
    norm_text = normalise(statement)
    tokens = tokenize(statement)
    total = len(tokens)
    if total == 0:
        raise ValueError('statement contains no word tokens')

    values = {}

    for key, section in (
        ('buzzword_density', 'buzzwords'),
        ('jargon_density', 'jargon'),
        ('acronym_density', 'acronyms'),
        ('frequent_density', 'frequent_words'),
    ):
        terms = markers.get(section, [])
        if not terms:
            raise ValueError(f"dictionary section '{section}' is empty or missing")
        values[key] = MarkerMatcher(terms).count(tokens, norm_text) / total

    pos = pos_densities(statement)
    for key in ('adjective_density', 'verb_density', 'noun_density', 'value_density'):
        values[key] = pos[key] if pos else None

    values['statement_length'] = total

    name_clean = (name or '').strip()
    host = website_host(website)
    values['name_length'] = len(name_clean) if name_clean else None
    # Length of the bare host, not the raw input string - see website_host().
    values['website_length'] = len(host) if host else None
    values['_domain'] = host or None
    values['_website_raw'] = (website or '').strip() or None
    values['founding_year_mention'] = bool(YEAR_RE.search(statement))
    values['location_mention'] = any(t in LOCATION_TERMS for t in tokens)

    if host:
        values['com_domain'] = host.endswith('.com')
        values['website_mention'] = host.split('.')[0] in norm_text
    else:
        # No website supplied - unknown, not absent. Never guess a domain.
        values['com_domain'] = None
        values['website_mention'] = None

    if host and name_clean:
        values['website_name_equivalence'] = len(host) == len(name_clean)
    else:
        values['website_name_equivalence'] = None
    return values


# ---------------------------------------------------------------------------
# Band classification
# ---------------------------------------------------------------------------


def in_band(value: float, band) -> bool:
    low, high = band
    if high <= low:
        return value == low
    return low <= value < high


def fmt_value(unit: str, value: float) -> str:
    if unit == 'ratio':
        return '%.1f%%' % (value * 100)
    return f'{value:.0f} {unit}'


def fmt_band(unit: str, band) -> str:
    """Render a band as a compact range, e.g. '30%-36%' or '2-37 words'."""
    if unit == 'ratio':
        return f'{band[0] * 100:.0f}%-{band[1] * 100:.0f}%'
    return f'{band[0]:g}-{band[1]:g} {unit}'


def classify(key: str, value: float) -> dict:
    spec = FEATURES[key]
    result = {
        'feature': key,
        'value': value,
        'value_display': fmt_value(spec['unit'], value),
        'unit': spec['unit'],
        'note': spec['note'],
        'best_band_display': fmt_band(spec['unit'], spec['best_band']),
        'best_delta': spec['best_delta'],
        'in_best_band': in_band(value, spec['best_band']),
    }

    if result['in_best_band']:
        result['verdict'] = 'BEST'
        result['delta'] = spec['best_delta']
    elif in_band(value, spec['min_band']):
        result['verdict'] = 'MIN'
        result['delta'] = spec['min_delta']
    elif in_band(value, spec['max_band']):
        result['verdict'] = 'MAX'
        result['delta'] = spec['max_delta']
    else:
        result['verdict'] = 'OUT_OF_BAND'
        result['delta'] = None
    return result


def hyping_score(values: dict) -> dict:
    """Reconstructed Hyping Score = (1/N) * sum(h_i * s_i).

    h_i = min-max normalised marker value in [0,1].
    s_i = Table V feature importance, normalised to sum 1.

    The paper publishes the formula but not the exact s_i vector, so this is a
    reconstruction. Treat it as a relative index, not an absolute figure.
    """
    keys = [k for k in IMPORTANCE if values.get(k) is not None]
    if not keys:
        return {'score': None, 'reason': 'no computable markers'}

    weights = {k: IMPORTANCE[k] for k in keys}
    known = [w for w in weights.values() if w is not None]
    if known:
        mean_w = sum(known) / len(known)
        for k, w in weights.items():
            if w is None:
                weights[k] = mean_w
    total_w = sum(weights.values())
    weights = {k: w / total_w for k, w in weights.items()}

    contributions = {}
    for k in keys:
        v = float(values[k])
        if FEATURES[k]['unit'] == 'ratio':
            h = max(0.0, min(1.0, v))
        else:
            h = max(0.0, min(1.0, v / STATEMENT_LENGTH_CAP))
        contributions[k] = {'h': h, 's': weights[k], 'h_times_s': h * weights[k]}

    return {
        'score': sum(c['h_times_s'] for c in contributions.values()),
        'n_markers': len(keys),
        'contributions': contributions,
        'reconstructed': True,
        'caveat': (
            'Reconstructed weighting. The paper publishes the formula but not the s_i vector or its dictionaries, so this is a relative index.'
        ),
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def build_report(name, statement: str, website, markers: dict) -> dict:
    values = measure(name, statement, website, markers)

    banded = [classify(k, float(values[k])) for k in FEATURES if values.get(k) is not None]
    unavailable = [k for k in FEATURES if values.get(k) is None]

    binaries = []
    for key, spec in BINARY_FEATURES.items():
        raw = values.get(key)
        if raw is None:
            state = 'unknown'
        else:
            state = 'present' if raw else 'absent'
        binaries.append(
            {
                'feature': key,
                'state': state,
                'present': None if raw is None else bool(raw),
                'delta': spec['delta'] if state == 'present' else None,
                'good': spec['good'],
                'verdict': state,
                'detail': spec['detail'],
            }
        )

    actionable = []
    for row in banded:
        if row['in_best_band']:
            continue
        spec = FEATURES[row['feature']]
        actionable.append(
            {
                'feature': row['feature'],
                'current': row['value_display'],
                'verdict': row['verdict'],
                'target': fmt_band(spec['unit'], spec['best_band']),
                'note': spec['note'],
            }
        )

    negatives = [b for b in binaries if b['state'] == 'present' and not b['good']]
    missing_inputs = [label for label, val in (('name', name), ('website', website)) if not (val or '').strip()]

    return {
        'input': {
            'name': name,
            'statement': statement,
            'website': website,
            'domain': values.get('_domain'),
        },
        'missing_inputs': missing_inputs,
        'hyping_score': hyping_score(values),
        'banded_features': banded,
        'unavailable_features': unavailable,
        'binary_flags': binaries,
        'actionable': actionable,
        'warnings': [b['detail'] for b in negatives],
        'paper': {
            'id': 'arXiv:2608.00045',
            'title': ('Predicting Startup Exit from Textual Descriptors: A Computational Linguistics Framework'),
            'authors': 'Saruggia, A.M.G. & Germano, S. (2026)',
            'global_exit_average': 10.38,
            'precision_1_0_recall_range': '0.005-0.017',
        },
        'disclaimer': (
            'Band diagnostics only. The paper does not publish trained '
            'coefficients or its dictionaries, so no calibrated exit '
            "probability is produced. At the paper's precision-1.0 operating "
            "point recall is 0.005-0.017: a clean screen means 'not flagged', "
            "never 'will succeed'. Do not use as the sole basis for an "
            'investment or application decision.'
        ),
    }


def run_screen(name, statement: str, website, markers: dict | None = None) -> dict:
    """Public entry point: screen one startup and return the report dict.

    Use this for programmatic or batch screening instead of reaching into
    ``measure`` or ``build_report`` directly. ``markers`` is loaded once and can
    be reused across calls to avoid re-parsing the dictionary file.

    Example:
        from screen import run_screen
        report = run_screen("Etemaro", "Autonomous DLMM execution ...", "etemaro.com")
        report["banded_features"]        # list of per-feature verdicts
        report["hyping_score"]["score"]  # reconstructed relative index
    """
    return build_report(name, statement, website, markers if markers is not None else load_markers())


def feature_row(name, value, verdict, best_band, delta) -> str:
    """Format one row of the banded-feature table.

    Kept as a helper so the column widths live in exactly one place, and so the
    render loop stays readable without nesting quotes inside an f-string.
    """
    return f'  {name:<20} {value:>10}  {verdict:<12} {best_band:<16} {delta:>8}'


def render(report: dict) -> str:
    out = []
    add = out.append
    inp = report['input']
    add('=' * 70)
    add('STARTUP FRAMING SCREEN')
    add('=' * 70)
    add('name      : %s' % (inp['name'] or '(not supplied)'))
    add('statement : {}'.format(inp['statement']))
    add(
        'website   : {}{}'.format(
            inp['website'] or '(not supplied)',
            '  (domain: {})'.format(inp['domain']) if inp['domain'] else '',
        )
    )
    add('')

    if report.get('missing_inputs'):
        add('-' * 70)
        add('MISSING INPUT - ASK THE USER, DO NOT INVENT')
        add('-' * 70)
        add('  not supplied: {}'.format(', '.join(report['missing_inputs'])))
        add('  Dependent features report as unknown/not measured.')
        add('')

    hs = report['hyping_score']
    add('-' * 70)
    add('HYPING SCORE (reconstructed)')
    add('-' * 70)
    if hs.get('score') is None:
        add('  unavailable: {}'.format(hs.get('reason')))
    else:
        score = hs['score']
        n_markers = hs['n_markers']
        add(f'  score = {score:.4f}   (N markers = {n_markers})')
        for k, c in sorted(hs['contributions'].items(), key=lambda kv: -kv[1]['h_times_s']):
            h, s, contribution = c['h'], c['s'], c['h_times_s']
            add(f'    {k:<20} h={h:.3f}  s={s:.4f}  h*s={contribution:.5f}')
        add('  note: {}'.format(hs['caveat']))
    add('')

    add('-' * 70)
    add('BANDED FEATURES vs PAPER (Table VIII)')
    add('-' * 70)
    add(feature_row('feature', 'value', 'verdict', 'best band', 'delta'))
    for row in report['banded_features']:
        delta_value = row['delta']
        delta = 'n/a' if delta_value is None else f'{delta_value:+.1f}%'
        add(
            feature_row(
                row['feature'],
                row['value_display'],
                row['verdict'],
                row['best_band_display'],
                delta,
            )
        )
    add('')

    if report['unavailable_features']:
        add('-' * 70)
        add('NOT MEASURED')
        add('-' * 70)
        pos_missing = [f for f in report['unavailable_features'] if f in POS_FEATURES]
        input_missing = [f for f in report['unavailable_features'] if f not in POS_FEATURES]
        if input_missing:
            add('  {}'.format(', '.join(input_missing)))
            add('  reason: the user did not supply the input. ASK - do not guess.')
        if pos_missing:
            add('  {}'.format(', '.join(pos_missing)))
            add('  reason: optional POS tagging is not installed (not an error).')
            add('  This is NOT a failure - the rest of the screen is complete.')
            add('  Do not estimate these by hand and do not run your own import probe.')
            add(f'  To enable: {POS_INSTALL_HINT}')
            add('  Ask the user before installing; run --doctor for full status.')
        add('')

    add('-' * 70)
    add('BINARY FLAGS vs PAPER (Table VII)')
    add('-' * 70)
    for b in report['binary_flags']:
        feat, detail, state = b['feature'], b['detail'], b['state']
        if state == 'unknown':
            add(f'  [?  ] {feat:<26} delta    n/a   not measured: {detail}')
        elif state == 'present':
            delta = b['delta']
            add(f'  [yes] {feat:<26} delta {delta:+.1f}%   {detail}')
        else:
            add(f'  [no ] {feat:<26} delta    n/a   {detail}')
    add('')

    if report['actionable']:
        add('-' * 70)
        add("MOVES TOWARD THE PAPER'S BEST BANDS")
        add('-' * 70)
        for a in report['actionable']:
            add('  * {}: {} ({}) -> target {}'.format(a['feature'], a['current'], a['verdict'], a['target']))
            add('      {}'.format(a['note']))
        add('')

    if report['warnings']:
        add('-' * 70)
        add('FLAGS')
        add('-' * 70)
        for w in report['warnings']:
            add(f'  ! {w}')
        add('')

    add('-' * 70)
    add('LIMITS')
    add('-' * 70)
    add('  {}'.format(report['disclaimer']))
    add('')
    add('  Source: {} - {}'.format(report['paper']['id'], report['paper']['authors']))
    add('=' * 70)
    return '\n'.join(out)


def setup_logger() -> logging.Logger:
    """Configure file logging to .logs/<tool>_<timestamp>.log."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime('%Y%m%d_%H%M%S')
    log_file = LOG_DIR / (f'screen_{timestamp}.log')

    logger = logging.getLogger('screen')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(fh)
    logger.info('log file: %s', log_file)
    return logger


def main(argv=None) -> int:
    default_data_dir = Path(__file__).parent.resolve() / 'data'
    parser = argparse.ArgumentParser(description='Screen startup name/statement/website framing against arXiv:2608.00045 thresholds.')
    parser.add_argument(
        '--name',
        help='startup name. Ask the user for it; omit only if '
        'they cannot supply it - dependent features then '
        'report as not measured rather than guessed',
    )
    parser.add_argument('--statement', help='one-line statement / pitch sentence')
    parser.add_argument(
        '--doctor',
        action='store_true',
        help='report capability and dependency status, then exit. Use this '
        'instead of probing for optional packages with your own import '
        'statement, which emits a misleading traceback.',
    )
    parser.add_argument(
        '--website',
        help='website URL. Ask the user for it; omit only if '
        'they cannot supply it - dependent features then '
        'report as not measured rather than guessed',
    )
    parser.add_argument('--json', action='store_true', help='emit JSON')
    parser.add_argument('--output', help='write output to this file')
    parser.add_argument(
        '--output-dir',
        '-o',
        default=str(default_data_dir),
        help='target output directory (defaults to scripts/data/)',
    )
    args = parser.parse_args(argv)

    if args.doctor:
        info = doctor_report()
        print(json.dumps(info, indent=2) if args.json else render_doctor(info))
        return 0

    if not (args.statement or '').strip():
        parser.error('--statement is required (or pass --doctor to check capabilities)')

    logger = setup_logger()
    logger.info('name=%r website=%r', args.name, args.website)

    try:
        markers = load_markers()
        report = build_report(args.name, args.statement, args.website, markers)
    except (FileNotFoundError, ValueError) as exc:
        logger.error('failed: %s', exc)
        print(f'error: {exc}', file=sys.stderr)
        return 2

    text = json.dumps(report, indent=2) if args.json else render(report)
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text + '\n', encoding='utf-8')
        logger.info('wrote %s', target)
        print(f'wrote {target}')
    else:
        print(text)
    logger.info('done')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
