#!/usr/bin/env python3
"""Health-check the Keycloak/RHBK LLM Wiki — stdlib only, no network.

Reports broken links, wanted (not-yet-written) pages, orphans, missing
provenance/summary, provenance drift, link hubs, and stale pages. With --status
it also prints the delta-manifest audit (ingested-vs-pending). See wiki/CLAUDE.md
for the schema this enforces.

Only the content dirs (paths.PAGE_DIRS — topics/ entities/ questions/ outputs/) are
scanned; `_meta/` (this script's home + the manifest) is tooling, not content, and is
never scanned.

Usage:
    python3 -m wikikb lint            # health check
    python3 -m wikikb lint --status   # + delta-manifest audit
    python3 -m wikikb lint --strict   # exit 1 on any *error*
    python3 -m wikikb lint --stale-days 365   # stale threshold (default 365)
"""
import argparse
import datetime
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
PAGE_DIRS = paths.PAGE_DIRS
TAXONOMY = str(paths.TAXONOMY)
LINK_RE = paths.PAGELINK_RE   # shared grammar: bare slug + optional |display
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


_SECTION_RE = None


def crosslink_section_re():
    """crosslink.py's OWN anchored `## Sources` regex, imported lazily so lint keeps working
    (scanning the block, as before) if the import ever fails. Reusing it — rather than
    re-deriving the markers here — is why the two can never drift apart."""
    global _SECTION_RE
    if _SECTION_RE is None:
        try:
            from wikikb.build import crosslink
            _SECTION_RE = crosslink.SECTION_RE
        except Exception:                       # noqa: BLE001 — degrade, never crash the linter
            _SECTION_RE = re.compile(r"(?!x)x")   # matches nothing
    return _SECTION_RE


def page_files():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield d, fn[:-3], os.path.join(full, fn)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    fm = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    fm["_has_sources"] = "sources:" in block
    fm["_provenance"] = parse_provenance(block)
    fm["_block"] = block
    return fm


def parse_provenance(block):
    """Return ('needs-review'|'unknown'|None) or dict(extracted/inferred/ambiguous)."""
    lines = block.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^provenance:\s*(\S.*)?$", line)
        if not m:
            continue
        inline = (m.group(1) or "").strip()
        if inline:
            return inline  # e.g. "needs-review"
        counts = {}
        for sub in lines[i + 1:]:
            sm = re.match(r"^\s+(\w+):\s*(\d+)", sub)
            if sm:
                counts[sm.group(1)] = int(sm.group(2))
            elif not sub.startswith((" ", "\t")):
                break
        return counts or None
    return None  # provenance: absent


def flat_provenance(fm):
    """Read the native FLAT provenance keys (provenance_extracted/inferred/ambiguous)
    introduced by the migrate-to-native flatten. parse_frontmatter already captured them
    into `fm` as top-level scalars; coerce to ints. Returns a dict or None."""
    out = {}
    for k in ("extracted", "inferred", "ambiguous"):
        v = fm.get("provenance_" + k)
        if v is not None and str(v).strip().lstrip("-").isdigit():
            out[k] = int(str(v).strip())
    return out or None


def provenance_of(fm):
    """The page's provenance: FLAT keys preferred (native schema), else the nested
    `provenance:` block (back-compat). dict | 'needs-review'|'unknown' | None."""
    flat = flat_provenance(fm)
    return flat if flat is not None else fm.get("_provenance")


_REVIEW_MOCS = None


def review_moc_slugs():
    """Slugs declared as a domain's `review-moc:` in taxonomy.md. These are synthesis
    Maps-of-Content — navigation pages whose 'claims' are [[wikilinks]], not facts — so
    `extracted == 0` is CORRECT for them, not a defect; they are exempt from H2.
    Computed from the SCHEMA (every domain declares its review-moc per ADD-DOMAIN step 2),
    so it generalizes to the next MOC and is NOT a hardcoded page-name allowlist. The
    kebab `[a-z]…` pattern skips the `<domain>` template placeholder."""
    global _REVIEW_MOCS
    if _REVIEW_MOCS is not None:
        return _REVIEW_MOCS
    mocs, in_comment = set(), False
    try:
        with open(TAXONOMY, encoding="utf-8") as fh:
            for line in fh:
                if in_comment:
                    if "-->" in line:
                        in_comment = False
                    continue
                if "<!--" in line:
                    in_comment = "-->" not in line
                    continue
                m = re.match(r"^\s*-\s*review-moc:\s*([a-z][a-z0-9-]+)\s*$", line)
                if m:
                    mocs.add(m.group(1))
    except OSError:
        pass
    _REVIEW_MOCS = mocs
    return mocs


def page_gate_verdict(fm):
    """SINGLE SOURCE of the page-level Confidence-gate rule (CLAUDE.md, Operation:
    QUERY → Confidence gate). Returns the list of HARD-FAIL reasons (empty == clean).
    gate_page_probe.py imports this so the probe asserts the SAME rule lint enforces
    (faithfulness, as eval.py imports kb.py). `status` is ADDITIVE-ONLY: it can only
    ADD H3 — it can NEVER suppress H2. Synthesis MOCs (review_moc_slugs) are exempt from
    H2 ONLY — a MOC makes no source-grounded claims, so extracted==0 is correct for it;
    H3 still applies to everyone.

    A page with NO provenance keys at all (`prov is None` — neither the flat
    `provenance_extracted/inferred/ambiguous` keys nor a nested `provenance:` block) is NOT
    gate-exempt: CLAUDE.md's contract reads "extracted = provenance_extracted (0 if absent)",
    so fully-missing provenance IS extracted==0 — the strongest ungrounded signal there is, not
    a free pass. It is treated exactly like an explicit `extracted: 0` for the H2/H3 arms below.

    An entirely EMPTY `fm` (no keys at all — not even `title`/`domain`/`slug`) is a different
    case: it is not "a real page missing its provenance", it is "no page frontmatter was
    supplied" (e.g. `graph.nodes.gate_node`'s default `state.get('page_fm') or {}` when the
    QUERY pipeline isn't threading a specific candidate page). H2/H3 are checks over a PAGE's
    frontmatter and have nothing to evaluate there, so they stay silent — only H1 (the
    tier-coverage arm, computed separately in `gate_banner`) applies to a page-less query."""
    if not fm:
        return []
    prov = provenance_of(fm)
    if prov is None:
        prov = {"extracted": 0, "inferred": 0}
    reviewed = fm.get("status") == "reviewed"
    is_moc = fm.get("slug") in review_moc_slugs()
    reasons = []
    if isinstance(prov, dict):
        ext, inf = prov.get("extracted", 0), prov.get("inferred", 0)
        if ext == 0 and not is_moc:                   # H2 — ungrounded (MOCs exempt: navigation, no claims)
            reasons.append("extracted==0 (ungrounded — no claim lifted from a source)")
        if reviewed and inf >= ext and (ext or inf):  # H3 — reviewed but synthesis-dominant (unchanged)
            reasons.append(f"status: reviewed but inferred>=extracted ({inf}>={ext})")
    elif isinstance(prov, str) and prov in ("needs-review", "unknown") and reviewed:
        reasons.append(f"status: reviewed but provenance: {prov}")
    return reasons


def gate_banner(fm, question_tier=None, covered=None):
    """The FULL Confidence gate (CLAUDE.md, Operation: QUERY) in ONE place, so the runtime/LangGraph
    node, lint, and the CI probes all share IDENTICAL code (the faithfulness invariant, BF-4). Returns
    the list of banner reasons (empty == clean). It WRAPS page_gate_verdict (H2 ungrounded + H3
    reviewed-incoherent — left UNCHANGED so gate_page_probe.py stays valid) and ADDS the two arms it
    omits plus, when a question tier is supplied, the coverage arm:
      H4  — status == needs-review (explicit; fires ALONE, regardless of provenance)
      L   — Provisional: status != reviewed AND inferred >= extracted (low-precision, in-combination)
      H1  — out-of-coverage: question_tier not in the routed domain's tiers-covered (only when both
            question_tier and covered are passed). INLINED below (identical to gate_probe.gate_verdict,
            which stays the CI probe of the same rule) so there is NO import that can fail-open: a
            swallowed import would silently drop the H1 banner — serving out-of-coverage inference as
            fact, the exact failure the gate exists to prevent.
    `status` is ADDITIVE-ONLY: it can raise H3/H4/L, never suppress H2. The H2 MOC-exemption stays
    scoped to H2 (H4/L/H1 have no MOC carve-out — H4 'fires regardless')."""
    reasons = list(page_gate_verdict(fm))                 # H2 + H3 (MOC-exempt H2), unchanged
    status = fm.get("status")
    if status == "needs-review":                          # H4 — explicit; alone
        reasons.append("status: needs-review (H4)")
    if status == "retracted":                             # H4 — withdrawn; alone (see Operation: RETRACT)
        reasons.append("status: retracted (H4) — this page was withdrawn; do not serve as current")
    prov = provenance_of(fm)                               # L — provisional, only in combination
    if status != "reviewed" and isinstance(prov, dict):
        ext, inf = prov.get("extracted", 0), prov.get("inferred", 0)
        if inf >= ext and (ext or inf):
            reasons.append(f"provisional: status!=reviewed and inferred>=extracted ({inf}>={ext}) (L)")
    if question_tier is not None and covered is not None:  # H1 — out-of-coverage; inlined, no import (B1)
        if question_tier not in covered:                  # == gate_probe.gate_verdict (the CI probe)
            reasons.append(f"out-of-coverage: {question_tier} not in {covered} (H1)")
    return reasons


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def bold_definition(text):
    """Leading bold one-line definition, multi-line aware; mirrors backfill.py."""
    body = FM_RE.sub("", text, count=1)
    b = re.sub(r"^\s*#.*\n", "", body.lstrip(), count=1).lstrip()
    if not b.startswith("**"):
        return None
    m = re.match(r"\*\*(.+?)\*\*", b, re.DOTALL)
    if not m:
        return None
    return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")


# ---- CITATION-GROUNDING gate: a cited source must actually CONTAIN the distinctive claim ----
# The page-level provenance gate (page_gate_verdict) checks the provenance COUNTS; this checks the
# provenance CONTENT — the gap that let a `reviewed` page cite a real note for an env var the note
# never mentions (the SSO_HTTPS_CIPHER_SUITES fabrication). It flags distinctive, fabrication-prone
# tokens — ENV/CONST identifiers and `--cli-flags` — that appear in the body but in NONE of the
# page's offline-readable cited sources. Lexical, stdlib, conservative: skips `(inferred)`/
# `(ambiguous)` lines (declared synthesis), crypto cipher-suite constants (domain vocab that varies in
# punctuation), and pages whose only sources are `web:`/unresolved (can't verify offline).
# ENV/CONST identifiers only (FOO_BAR_BAZ) — the high-precision, fabrication-prone shape. CLI flags
# (`--x`) are deliberately NOT matched: too many are tooling/wikikb flags or markdown-anchor fragments.
_DISTINCTIVE_RE = re.compile(r"\b[A-Z][A-Z0-9]{2,}(?:_[A-Z0-9]+)+\b")
# A line is "grounded/declared" — and skipped — if it carries an inline provenance tag in any form:
# (inferred) / (inferred: …) / (ambiguous …), or an inline source cite (web:/ref:/kb:/guide:/note:).
_INFERRED_RE = re.compile(r"\((?:inferred|ambiguous)\b|\((?:web|ref|kb|guide|note):", re.I)
_CIPHERish = ("AES", "SHA", "GCM", "CHACHA", "POLY", "ECDHE", "ECDSA", "_RSA", "CBC", "_TLS_")
_domain_token_cache = {}
_domain_flag_cache = {}
# CLI-flag shape (`--foo-bar`) — matched for QUERY guarding only (identifier_guard); page-body
# grounding deliberately skips flags (too many tooling/markdown false positives — see note above).
_FLAG_RE = re.compile(r"--[a-z][a-z0-9]*(?:-[a-z0-9]+)+\b")
# hyphenated-word shape WITHOUT the -- prefix — corpus prose often names options bare
# ("configurable via the tracing-sampler-ratio option"); membership-only, never for suggestions.
_HYPHENWORD_RE = re.compile(r"\b[a-z][a-z0-9]*(?:-[a-z0-9]+)+\b")
_domain_hyphen_cache = {}


def _strip_fm_body(text):
    return FM_RE.sub("", text, count=1)


def _is_distinctive_artifact(t):
    """Skip crypto cipher-suite constants — domain vocab that varies in punctuation across sources."""
    return any(c in t for c in _CIPHERish)


def domain_corpus_tokens(domain):
    """The set of distinctive tokens (env-vars/flags) that appear ANYWHERE in `reference/<domain>/`.
    Empty for a notes-first / corpus-less domain (⇒ grounding is unverifiable, so we don't flag)."""
    if domain in _domain_token_cache:
        return _domain_token_cache[domain]
    toks = set()
    dd = os.path.join(WIKI, "reference", domain or "")
    if os.path.isdir(dd):
        for fn in os.listdir(dd):
            if not fn.endswith(".md"):
                continue
            try:
                body = open(os.path.join(dd, fn), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for m in _DISTINCTIVE_RE.finditer(body):
                toks.add(m.group(0).lower())
            _domain_flag_cache.setdefault(domain, set()).update(
                m.group(0)[2:] for m in _FLAG_RE.finditer(body))
            _domain_hyphen_cache.setdefault(domain, set()).update(
                m.group(0) for m in _HYPHENWORD_RE.finditer(body))
    _domain_token_cache[domain] = toks
    _domain_flag_cache.setdefault(domain, set())
    _domain_hyphen_cache.setdefault(domain, set())
    return toks

def identifier_guard(query, domain):
    """The QUERY-side anti-fabrication gate (deterministic, model-independent).

    Extract distinctive identifiers from the *question* — env/CONST names and `--cli-flags` — and
    check each against the domain's ENTIRE reference corpus in both spellings (KC_FOO_BAR <-> foo-bar).
    Returns a list of {token, nearest} for identifiers that exist NOWHERE in the ground truth: the
    caller must lead the answer with "does not exist" + the nearest real options instead of letting a
    model define the token from its parametric memory (the adjacent-real-substitution failure mode:
    retrieval surfaces the real neighbor, and a weak model silently transfers its semantics to the
    asked-about name). [] when the domain has no corpus (notes-first) — unverifiable, so no claim."""
    corpus = domain_corpus_tokens(domain)          # also fills the flag/hyphen caches
    flags = _domain_flag_cache.get(domain, set())
    hyphens = _domain_hyphen_cache.get(domain, set())
    if not corpus and not flags:
        return []
    known = corpus | flags | hyphens | {t[3:].replace("_", "-") for t in corpus if t.startswith("kc_")} \
        | {"kc_" + f.replace("-", "_") for f in flags} | {"kc_" + h.replace("-", "_") for h in hyphens}
    # query-side env shape allows a 2-char first segment (KC_..., MS_...) — the page-body regex
    # requires 3+ to stay high-precision over prose, but a *question* naming KC_FOO is deliberate.
    env_q = re.compile(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b")
    suspects = [m.group(0) for m in env_q.finditer(query)] \
        + [m.group(0) for m in _FLAG_RE.finditer(query)]
    import difflib
    out = []
    for s in suspects:
        if _is_distinctive_artifact(s):
            continue
        norm = s.lower().lstrip("-")
        forms = {norm, norm.replace("_", "-"), norm.replace("-", "_"),
                 ("kc_" + norm.replace("-", "_")) if not norm.startswith("kc_") else norm[3:].replace("_", "-")}
        if forms & known:
            continue
        pool = list(flags) + [t.replace("_", "-") for t in corpus] \
            + [h for h in hyphens if "-" in h[1:]]
        near = difflib.get_close_matches(norm.replace("_", "-"), pool, n=3, cutoff=0.6)
        out.append({"token": s, "nearest": near})
    return out



def extract_distinctive(text):
    """RAW extraction step shared by every distinctive-identifier consumer (page-level
    `ungrounded_citations` below, the QUERY-side `identifier_guard` above, and the ANSWER-time
    fabrication check `validate_answer_grounding` — graph/nodes.py's synthesize_node). Distinctive
    ENV/CONST-shaped tokens (`_DISTINCTIVE_RE`), in first-occurrence order, minus crypto cipher-suite
    constants (`_is_distinctive_artifact`) and any token on a line that already carries an inline
    provenance tag or cite (`_INFERRED_RE` — declared synthesis, not a bare claim). No corpus/context
    comparison here — callers decide what "grounded" means for their own ground truth."""
    out = []
    for line in text.splitlines():
        if _INFERRED_RE.search(line):
            continue
        for m in _DISTINCTIVE_RE.finditer(line):
            t = m.group(0)
            if _is_distinctive_artifact(t):
                continue
            if t not in out:
                out.append(t)
    return out


def ungrounded_citations(text, fm):
    """Distinctive tokens asserted as fact in the body but absent from the page's ENTIRE domain
    reference corpus — i.e. nowhere in the ground truth (the fabricated-citation smell). Skips
    `(inferred)`/`(ambiguous)` lines (declared synthesis). [] when the domain has no corpus to
    verify against (notes-first) — grounding is then the human's job, not a false accusation."""
    corpus = domain_corpus_tokens(fm.get("domain"))
    if not corpus:
        return []
    return [t for t in extract_distinctive(_strip_fm_body(text)) if t.lower() not in corpus]


_ANSWER_CITE_RE = re.compile(r"\[cite[:\s]\s*([A-Za-z0-9._/-]+)\]", re.IGNORECASE)
_BASIS_TOKEN_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9_]*\b")


def validate_answer_grounding(answer, candidates, query=""):
    """The SINGLE answer-time citation/identifier validator (WI-6).

    Parse the answer's ``[cite: id]`` tokens, intersect them with the offered candidate ids, then
    ground distinctive identifiers against the UNION of those cited notes' FULL bodies plus the
    query. Full bodies are deliberate: the old context-based check could flag an identifier the
    model legitimately read in a cited note merely because it fell beyond ``CTX_CHARS`` in the
    assembled prompt window. An uncited candidate contributes nothing to the basis.

    Membership is case-insensitive exact token equality, not substring containment. Identifier
    extraction and its inferred/cipher/CLI exclusions remain centralized in ``extract_distinctive``
    and are therefore identical to the page-level citation-grounding scanner. Returns a
    machine-readable result used directly by ``graph.nodes.synthesize_node``."""
    offered = {cid: body or "" for cid, body in (candidates or [])}
    parsed = list(dict.fromkeys(_ANSWER_CITE_RE.findall(answer or "")))
    cited_ids = [cid for cid in parsed if cid in offered]
    basis_text = "\n".join([query or ""] + [offered[cid] for cid in cited_ids])
    basis_tokens = {m.group(0).lower() for m in _BASIS_TOKEN_RE.finditer(basis_text)}
    ungrounded = [t for t in extract_distinctive(answer or "") if t.lower() not in basis_tokens]
    return {
        "cited_ids": cited_ids,
        "basis": "cited-full-bodies+query",
        "ungrounded_identifiers": ungrounded,
    }


# ---- Premise extraction + gate (deterministic, no LLM) -----------------------------------------
# The premise-correction-dropout fix (2026-07-12 manual session #4, "RID Block Size"): a user
# question ASSERTED two false facts, the synthesis model's own reasoning found the correction, and
# the served answer dropped it — even endorsed the premise. The counter is structural, not
# instructional (small local models follow STRUCTURE, not nuance): extract the user's checkable
# assertions here (pure regex), inject them as a pre-built Premise-check table the model FILLS
# (graph/nodes.py), then gate on the filled table (premise_gate). Design invariant — SAFE
# DEGRADATION: a missed premise reproduces today's behavior (no row, no gate); a spuriously
# extracted "premise" becomes an injected row the model marks NOT-IN-CORPUS. Neither path can
# false-fire the gate against a correct answer.

# numbers with enough shape to be a checkable claim: power forms (2^31, 2**31), N-bit widths,
# comma-grouped or 2+digit integers, decimals w/ magnitude words, percentages, digit+unit
# durations. Bare single digits are excluded (list ordinals / "step 3" — noise, not claims).
_PREMISE_NUM_RE = re.compile(
    r"(?:\b\d+\s*(?:\^|\*\*)\s*\d+"                       # 2^31, 2**31
    r"|\b\d+-bit\b"                                        # 31-bit
    r"|~?\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b"                 # 50,000 / 1,073,741,823
    r"|~?\b\d+\.\d+(?:\s*(?:billion|million|thousand))?\b" # 2.1 billion
    r"|\b\d+\s*%"                                          # 90%
    r"|\b\d+\s*(?:days?|hours?|minutes?|seconds?)\b"       # 90 days
    r"|\b\d{2,}\b)"                                        # any 2+ digit integer
)
# assertion-verb spans: the user states something as known fact. Extensible list, per-domain later.
# span atom: any char except clause enders — but a comma BETWEEN digits stays (50,000), and a
# period between digits stays (26.4); a plain "." / "," / "?" / "!" still ends the claim span.
_SPAN = r"(?:[^,.?!]|,(?=\d)|\.(?=\d))"
_PREMISE_CLAIM_RES = [
    re.compile(r"\bI know(?: that)?\s+(%s+)" % _SPAN, re.I),
    re.compile(r"\bgiven that\s+(%s+)" % _SPAN, re.I),
    re.compile(r"\bsince\s+(%s*?\bis\b%s+)" % (_SPAN, _SPAN), re.I),
    re.compile(r"\bI(?:'ve| have)? set\s+(%s*?\bto\b%s+)" % (_SPAN, _SPAN), re.I),
    re.compile(r"((?:[A-Za-z][\w() ]{0,50}?)\s*(?:=|is capped at|is limited to|defaults? to)\s*%s+)" % _SPAN, re.I),
]
# identifier shapes a question can assert about, beyond the fabrication gate's ENV/CONST + flags:
# cmdlets (Get-ADUser) and registry-style Title Case value names ("RID Block Size").
_PREMISE_IDENT_RES = [
    re.compile(r"\b[A-Z][a-z]+-[A-Z][A-Za-z]+\b"),
    re.compile(r"\b(?:[A-Z][a-zA-Z]+ ){1,3}(?:Size|Limit|Value|Policy|Quota|Lifetime|Threshold)\b"),
]


def extract_premises(question):
    """The user's checkable assertions from a question text, deterministically (no LLM).
    Returns [{'premise_text', 'tokens', 'kind'}], kind ∈ claimed|number|identifier. `tokens` are
    the matchable atoms the premise gate later uses to bind a Premise-check row to this premise.
    A CLAIMED span subsumes the numbers/identifiers inside it (the span is the richer premise);
    a claim with no checkable atom at all is dropped (nothing to verify deterministically)."""
    q = question or ""
    premises, covered = [], ""
    spans = []
    for cre in _PREMISE_CLAIM_RES:
        for m in cre.finditer(q):
            span = m.group(1).strip().rstrip(")")
            if not span:
                continue
            # containment dedup, longer span wins (it is the richer premise)
            contained = [s for s in spans if span.lower() in s.lower()]
            if contained:
                continue
            spans = [s for s in spans if s.lower() not in span.lower()]
            spans.append(span)
    for span in spans:
        toks = [t for t in _PREMISE_NUM_RE.findall(span)]
        toks += _DISTINCTIVE_RE.findall(span) + _FLAG_RE.findall(span)
        for ire in _PREMISE_IDENT_RES:
            toks += ire.findall(span)
        if toks:
            premises.append({"premise_text": span, "tokens": list(dict.fromkeys(toks)),
                             "kind": "claimed"})
            covered += " " + span.lower()
    for m in _PREMISE_NUM_RE.finditer(q):
        tok = m.group(0)
        if tok.lower() in covered:
            continue
        ctxt = q[max(0, m.start() - 60):m.end() + 60].strip()
        premises.append({"premise_text": ctxt, "tokens": [tok], "kind": "number"})
        covered += " " + ctxt.lower()
    for ire in _PREMISE_IDENT_RES:
        for m in ire.finditer(q):
            tok = m.group(0)
            if tok.lower() in covered:
                continue
            premises.append({"premise_text": tok, "tokens": [tok], "kind": "identifier"})
            covered += " " + tok.lower()
    return premises


PREMISE_VERDICTS = ("CONFIRMED", "CORRECTED", "NOT-IN-CORPUS")
_PREMISE_ROW_RE = re.compile(r"^\s*\|(?!\s*(?:-|#\s|\s*User))(.+)\|\s*$", re.M)


def premise_gate(answer, premises, candidates, query=""):
    """Deterministic post-synthesis enforcement — the dropout catcher. For each extracted premise:
    the answer's Premise-check table must contain a row sharing a token with the premise
    (case-insensitive substring) → else `premise_unaddressed`; the row must carry exactly one
    closed-vocabulary verdict → else `premise_verdict_invalid`; and a CORRECTED row's corpus cell
    must ground: identifiers via extract_distinctive (WI-6 extraction) and numbers via
    boundary-aware digit match, both against the union of ALL retrieved candidate bodies + query —
    deliberately wider than WI-6's cited-only basis, because table cells carry no [cite:] tokens
    and a cited-only basis would false-fire on every correct correction (safe-degradation rule).
    Returns a list of flag dicts; [] = clean. premises=[] short-circuits to [] (today's behavior)."""
    flags = []
    if not premises:
        return flags
    rows = []
    for rm in _PREMISE_ROW_RE.finditer(answer or ""):
        cells = [c.strip() for c in rm.group(1).split("|")]
        if len(cells) >= 3 and not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
    all_bodies = "\n".join((b or "") for _c, b in (candidates or [])) + "\n" + (query or "")
    bodies_tokens = {m.group(0).lower() for m in _BASIS_TOKEN_RE.finditer(all_bodies)}
    for p in premises:
        row = next((r for r in rows
                    if any(t.lower() in " ".join(r).lower() for t in p["tokens"])), None)
        if row is None:
            flags.append({"flag": "premise_unaddressed", "premise": p["premise_text"]})
            continue
        rowtext = " ".join(row).upper()
        hit = [v for v in PREMISE_VERDICTS if v in rowtext]
        # NOT-IN-CORPUS contains no other verdict as substring; CONFIRMED+CORRECTED both present
        # means the model waffled — treat as invalid.
        if len(hit) != 1:
            flags.append({"flag": "premise_verdict_invalid", "premise": p["premise_text"]})
            continue
        if hit[0] == "CORRECTED":
            corpus_cell = " ".join(row[1:-1]) if len(row) >= 3 else " ".join(row)
            ungrounded = [t for t in extract_distinctive(corpus_cell)
                          if t.lower() not in bodies_tokens]
            nobody = all_bodies.replace(",", "")
            for num in _PREMISE_NUM_RE.findall(corpus_cell):
                bare = re.escape(num.replace(",", "").replace(" ", ""))
                if not re.search(r"(?<!\d)" + bare + r"(?!\d)", nobody):
                    ungrounded.append(num)
            if ungrounded:
                flags.append({"flag": "premise_correction_ungrounded",
                              "premise": p["premise_text"],
                              "tokens": list(dict.fromkeys(ungrounded))})
    return flags


# ---- H1 out-of-coverage banner check (filed questions) ----------------------------------------
# A filed `type: question` page can DECLARE its tier (`question_tier:`), but the Confidence gate
# (CLAUDE.md, Operation: QUERY) is a reader-facing contract — the banner text itself, not just the
# frontmatter tag, must reach whoever reads the page body without re-deriving the gate. This checks
# the OUTPUT, not just the input: a `question_tier` outside the domain's `tiers-covered:` must be
# accompanied by an H1 banner line in the body. Lenient on markdown decoration (blockquote `> ⚠️` or
# heading `# ⚠️` are both used in the wiki today) — strict on content (must mention "coverage").
_BANNER_LINE_RE = re.compile(r"^[#>\s]*⚠️")


def has_out_of_coverage_banner(text):
    for line in _strip_fm_body(text).splitlines():
        if _BANNER_LINE_RE.match(line) and "coverage" in line.lower():
            return True
    return False


# ---- F6: near-duplicate question detection (WARNING only) -------------------------------------
# Independent sessions mint near-duplicate question pages under different slugs/phrasing (the
# CLAUDE.md "kc-sh vs kcsh" example, step 5 of Operation: QUERY). Two soft signals, either fires:
# (a) normalized-slug collision — strip all non-alphanumerics, catches hyphenation variants like
# `kc-sh` vs `kcsh`; (b) high title/summary token-set overlap (Jaccard on lowercased word sets,
# threshold 0.6 — checking title as well as summary catches pairs phrased differently in the
# summary but near-identically in the title, e.g. dc-locator-how-windows-clients-find-dc vs
# windows-dc-locator). Pairwise within the same `domain:` only — cross-domain overlap is expected.
_WORD_RE = re.compile(r"[a-z0-9]+")


def _normalized_slug(slug):
    return re.sub(r"[^a-z0-9]", "", (slug or "").lower())


def _word_jaccard(a, b):
    ta, tb = set(_WORD_RE.findall((a or "").lower())), set(_WORD_RE.findall((b or "").lower()))
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def duplicate_question_pairs(pages, threshold=0.6):
    """Pairwise near-duplicate scan over `type: question` pages, grouped by `domain:`.
    ponytail: O(n^2) within a domain — fine at ~100 pages/domain; revisit (MinHash/LSH) only if a
    domain's question count grows into the thousands."""
    by_domain = {}
    for slug, (_d, _p, _t, fm) in pages.items():
        if fm and fm.get("type") == "question":
            by_domain.setdefault(fm.get("domain"), []).append((slug, fm))
    out = []
    for dom, items in by_domain.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                s1, f1 = items[i]
                s2, f2 = items[j]
                reasons = []
                if _normalized_slug(s1) == _normalized_slug(s2):
                    reasons.append("normalized slug collision")
                title_j = _word_jaccard(unquote(f1.get("title", "")), unquote(f2.get("title", "")))
                summary_j = _word_jaccard(unquote(f1.get("summary", "")), unquote(f2.get("summary", "")))
                if title_j >= threshold or summary_j >= threshold:
                    reasons.append(f"title/summary similarity (title={title_j:.2f}, summary={summary_j:.2f})")
                if reasons:
                    out.append(f"[[{s1}]] / [[{s2}]] (domain {dom}): {'; '.join(reasons)}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--stale-days", type=int, default=365)
    ap.add_argument("--ctx-window", type=int, default=32768,
                    help="local model context window; a per-domain index over ~25%% of it is flagged")
    args = ap.parse_args()

    # shared taxonomy (from tags.py / _meta/taxonomy.md); empty if unavailable
    sys.dont_write_bytecode = True
    try:
        from wikikb.build import tags as tagmod
        vocab, synonyms = tagmod.load_taxonomy()
        declared_domains = tagmod.load_domains()
    except Exception:  # noqa: BLE001
        tagmod, vocab, synonyms = None, set(), {}
        declared_domains = set()

    # tiers-covered per domain (taxonomy.md), for the H1 filed-question banner check below
    try:
        from wikikb.quality import coverage as covmod
        tiers_covered = covmod.load_tiers_covered()
    except Exception:  # noqa: BLE001
        tiers_covered = {}

    pages = {}
    for d, slug, path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        pages[slug] = (d, path, text, parse_frontmatter(text))

    slugs = set(pages)
    # reference-tier notes (wiki/reference/<domain>/) are valid [[link]] targets but
    # are NOT synthesized pages — collect their slugs so links to them aren't "wanted"
    ref_slugs = set()
    ref_root = os.path.join(WIKI, "reference")
    if os.path.isdir(ref_root):
        for dom in os.listdir(ref_root):
            dd = os.path.join(ref_root, dom)
            if os.path.isdir(dd):
                for fn in os.listdir(dd):
                    if fn.endswith(".md"):
                        ref_slugs.add(fn[:-3])

    # in-index detection spans the global index.md AND every generated index.<domain>.md
    index_sources = set()
    index_files = ["index.md"] + sorted(
        f for f in os.listdir(WIKI) if re.match(r"^index\.[a-z0-9-]+\.md$", f))

    referenced = {}     # slug -> set of pages (or index files) that link to it
    for slug, (_d, _p, text, _fm) in pages.items():
        # Excise crosslink's GENERATED `## Sources` block first — the same thing expand.py and
        # tkg/model.py already do. Its `[[note|Title]]` entries are provenance edges to the
        # reference tier, not hand-authored page links; counting them would make every cited
        # reference note look like a link hub. (Before the shared pipe-tolerant grammar, the
        # `(no pipe)` rule excluded them by accident — this makes the exclusion deliberate.)
        for target in LINK_RE.findall(crosslink_section_re().sub("", text)):
            referenced.setdefault(target, set()).add(slug)
    for fn in index_files:
        p = os.path.join(WIKI, fn)
        if not os.path.exists(p):
            continue
        index_sources.add(fn)
        with open(p, encoding="utf-8") as fh:
            for target in LINK_RE.findall(fh.read()):
                referenced.setdefault(target, set()).add(fn)

    errors, warnings, notes, seeded, hubs = [], [], [], [], []

    wanted = sorted(t for t in referenced if t not in slugs and t not in ref_slugs)
    for t in wanted:
        src = ", ".join(sorted(referenced[t]))
        notes.append(f"wanted page [[{t}]]  (referenced by: {src})")

    today = datetime.date.today()
    for slug, (_d, path, text, fm) in pages.items():
        rel = os.path.relpath(path, WIKI)
        if fm is None:
            errors.append(f"{rel}: missing frontmatter block")
            continue
        if not fm.get("_has_sources"):
            errors.append(f"{rel}: no `sources:` provenance")

        # domain facet (required; validated against taxonomy ## Domains)
        dom = fm.get("domain")
        if not dom:
            warnings.append(f"{rel}: no `domain:` (required — run backfill.py)")
        elif declared_domains and dom not in declared_domains:
            warnings.append(f"{rel}: domain `{dom}` not declared in taxonomy.md ## Domains")

        # summary checks
        summary = fm.get("summary", "")
        if not summary:
            warnings.append(f"{rel}: no `summary:` (tiered query relies on it)")
        else:
            bd = bold_definition(text)
            if bd and unquote(summary).strip().rstrip(".") == bd:
                seeded.append(f"{rel}: summary auto-seeded from bold definition — wants a human summary")

        # PROVENANCE GATE — page-level arm of the Confidence gate (CLAUDE.md, Operation:
        # QUERY). Reads the native FLAT keys (provenance_extracted/inferred/ambiguous),
        # nested form for back-compat. HARD FAILS via page_gate_verdict(): H2 extracted==0
        # (ungrounded) and H3 reviewed AND inferred>=extracted (incoherent self-review).
        # `status` is ADDITIVE-ONLY — `reviewed` can NEVER suppress H2. The gate only
        # FLAGS; fixing a flagged page is a separate content pass, never an auto-edit.
        # NOTE: prov is None (no provenance keys at all) is NOT a reason to skip the gate —
        # page_gate_verdict() itself treats that as extracted==0 (H2 fires); the "missing
        # provenance" warning below is a SEPARATE, softer signal and fires alongside it.
        prov = provenance_of(fm)
        reviewed = fm.get("status") == "reviewed"
        if prov is None:
            warnings.append(f"{rel}: no provenance (provenance_extracted/inferred/ambiguous)")
        for reason in page_gate_verdict(fm):
            errors.append(f"{rel}: provenance gate — {reason}")
        # soft drift (NOT a gate fail): grounded but synthesis-leaning, not reviewed
        if isinstance(prov, dict):
            ext, inf = prov.get("extracted", 0), prov.get("inferred", 0)
            if not reviewed and ext > 0 and inf >= ext:
                warnings.append(f"{rel}: provenance drifts inferred>=extracted ({inf}>={ext}) — verify vs raw layer")
        elif isinstance(prov, str) and prov in ("needs-review", "unknown") and not reviewed:
            warnings.append(f"{rel}: provenance: {prov} (assign real per-claim provenance)")

        # CITATION-GROUNDING gate — distinctive claims absent from every cited source. A `reviewed`
        # page asserting an ungrounded env var / CLI flag is a fabricated/misattributed citation: a
        # hard ERROR (the SSO_HTTPS_CIPHER_SUITES class). Draft pages get a WARNING to verify.
        if fm.get("type") in ("topic", "entity", "question", "output"):
            ungrounded = ungrounded_citations(text, fm)
            if ungrounded:
                shown = ", ".join(ungrounded[:6]) + ("…" if len(ungrounded) > 6 else "")
                msg = (f"{rel}: citation grounding — {len(ungrounded)} distinctive token(s) in no cited "
                       f"source ({shown}) — possible fabricated/misattributed citation")
                if reviewed:
                    errors.append(msg)
                else:
                    warnings.append(msg + "; verify or tag (inferred)")

        # H1 OUT-OF-COVERAGE BANNER — a filed question (CLAUDE.md, Operation: LINT). A
        # `question_tier` outside the routed domain's `tiers-covered:` means the answer rests on
        # synthesis over an un-ingested tier (H1) — the reader-facing banner is mandatory, not
        # optional, regardless of `status`.
        if fm.get("type") == "question":
            qtier = unquote(fm.get("question_tier", ""))
            if qtier in ("support-kb", "scenarios"):
                covered = tiers_covered.get(dom) or []
                if qtier not in covered and not has_out_of_coverage_banner(text):
                    errors.append(f"{rel}: question_tier '{qtier}' not in domain `{dom}`'s "
                                  f"tiers-covered {covered} — missing H1 out-of-coverage banner")

        # tag checks (Pass 2 — validated against _meta/taxonomy.md)
        if tagmod is not None:
            page_tags = tagmod.parse_tags(fm.get("_block", ""))
            if page_tags is None:
                notes.append(f"{rel}: no `tags:` (run tags.py backfill)")
            else:
                for t in page_tags:
                    if vocab and t not in vocab:
                        hint = f" (synonym of `{synonyms[t]}` — run tags.py normalize)" if t in synonyms else ""
                        warnings.append(f"{rel}: tag `{t}` not in taxonomy{hint}")

        if fm.get("status") == "stub":
            warnings.append(f"{rel}: still status: stub")

        # stale: updated older than threshold
        upd = fm.get("updated", "")
        try:
            d = datetime.date.fromisoformat(upd)
            if (today - d).days > args.stale_days:
                notes.append(f"{rel}: stale (updated {upd}, >{args.stale_days}d)")
        except ValueError:
            pass

        # orphan check (spans index.md + every index.<domain>.md)
        in_index = slug in referenced and bool(referenced[slug] & index_sources)
        linked = slug in referenced and any(s not in index_sources for s in referenced[slug])
        if not in_index and not linked and fm.get("type") not in ("question", "output"):
            warnings.append(f"{rel}: orphan (no inbound [[links]] and not in any index)")

    # RETRACTION CASCADE (Operation: RETRACT) — withdrawing a page is only half the job; the pages
    # that cite it keep serving its claim. `status: retracted` fires the gate's H4 on the page
    # itself (gate_banner, every serve/mcp/ask surface); this arm surfaces the DEPENDENTS, which
    # nothing else can see. Superseded-version churn (26.0 -> 26.6) is the live case.
    for slug, (_d, _p, _t, fm) in pages.items():
        if not fm or fm.get("status") != "retracted":
            continue
        for src in sorted(referenced.get(slug, set()) - index_sources):
            warnings.append(f"{src}: links [[{slug}]], which is status: retracted — re-source or drop the claim")

    # F6 — near-duplicate question pages (soft warning; see duplicate_question_pairs docstring)
    for dup in duplicate_question_pairs(pages):
        warnings.append(f"possible duplicate question: {dup}")

    # hubs: most-linked pages (inbound from other pages, not index files)
    inbound = {s: len([x for x in srcs if x not in index_sources]) for s, srcs in referenced.items() if s in slugs}
    for slug, n in sorted(inbound.items(), key=lambda kv: -kv[1])[:8]:
        if n:
            hubs.append(f"[[{slug}]] — {n} inbound links")

    # cross-domain links: page in one domain linking to a page in another (soft —
    # intentional bridges are fine, but they're the SRE correlation surface, so surface them)
    page_dom = {s: (fm.get("domain") if fm else None) for s, (_d, _p, _t, fm) in pages.items()}
    xdomain = []
    for tgt, srcs in referenced.items():
        if tgt not in pages:
            continue
        for src in sorted(srcs):
            if (src in pages and page_dom.get(src) and page_dom.get(tgt)
                    and page_dom[src] != page_dom[tgt]):
                xdomain.append(f"[[{src}]] ({page_dom[src]}) → [[{tgt}]] ({page_dom[tgt]})")

    # generated-index health: staleness + context-budget (stdlib heuristic, no tokenizer)
    try:
        from wikikb.build import index as indexmod
        for d in indexmod.stale_indexes():
            warnings.append(f"index.{d}.md is stale — run `python3 -m wikikb index`")
    except Exception as e:  # noqa: BLE001
        notes.append(f"index staleness check unavailable: {e}")
    budget = int(args.ctx_window * 0.25)
    for fn in index_files:
        if fn == "index.md":
            continue
        p = os.path.join(WIKI, fn)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as fh:
            est_tokens = len(fh.read()) // 4  # ~4 chars/token heuristic (air-gap-safe, no tiktoken)
        if est_tokens > budget:
            warnings.append(f"{fn}: ~{est_tokens} tokens (> 25% of --ctx-window {args.ctx_window}) "
                            "— split the domain or trim summaries to protect the routing context")

    # reference-tier validation (the folded-in corpus). Light checks (warnings, not errors):
    # these are raw imported notes, not synthesized pages, but a malformed one silently
    # breaks retrieval (e.g. an empty gated index drops every gated pointer).
    ref_root = os.path.join(WIKI, "reference")
    if os.path.isdir(ref_root):
        for dom in sorted(os.listdir(ref_root)):
            dd = os.path.join(ref_root, dom)
            if not os.path.isdir(dd):
                continue
            bodies = 0
            for fn in sorted(os.listdir(dd)):
                if not fn.endswith(".md") or fn.startswith("_"):
                    continue
                bodies += 1
                with open(os.path.join(dd, fn), encoding="utf-8") as fh:
                    rfm = parse_frontmatter(fh.read())
                rrel = f"reference/{dom}/{fn}"
                if rfm is None:
                    warnings.append(f"{rrel}: reference note missing frontmatter")
                elif not rfm.get("source"):
                    warnings.append(f"{rrel}: reference note has no `source:`")
            gated = os.path.join(dd, "_gated-kb-index.md")
            if os.path.exists(gated):
                gtext = open(gated, encoding="utf-8").read()
                if gtext.count("\n## ") == 0:
                    warnings.append(f"reference/{dom}/_gated-kb-index.md: present but no pointers parsed (malformed?)")
            if bodies == 0:
                notes.append(f"reference/{dom}/: no body notes (corpus not folded in?)")

    def section(label, items):
        if items:
            print(f"\n{label} ({len(items)})")
            for i in items:
                print(f"  - {i}")

    print(f"Wiki lint — {len(pages)} pages across {', '.join(PAGE_DIRS)}")
    section("ERRORS", errors)
    section("WARNINGS", warnings)
    section("AUTO-SEEDED SUMMARIES (soft — replace with a real summary)", seeded)
    section("CROSS-DOMAIN LINKS (soft — intentional bridges; the SRE correlation surface)", xdomain)
    section("HUBS (most-linked pages)", hubs)
    section("WANTED PAGES (TODO markers, not errors)", notes)
    if not (errors or warnings or notes or seeded):
        print("\nClean. No issues.")

    if args.status:
        print("\n=== STATUS / delta-manifest audit ===")
        sys.dont_write_bytecode = True  # keep _meta/wikikb/ free of __pycache__
        try:
            from wikikb.build import manifest
            for ln in manifest.status_lines():
                print("  " + ln)
        except Exception as e:  # noqa: BLE001
            print(f"  (manifest audit unavailable: {e})")

        # Optional LLM spend table from the regenerable ledger (BF-11). Read the JSON DIRECTLY —
        # NO module-scope `import cost`/`llm` anywhere in lint.py — so LINT/STATUS stays stdlib-only
        # and green when the optional online tier was never installed. Missing ledger -> a notice.
        print("\n  --- LLM spend (from _meta/eval/cost_report.json; optional online tier) ---")
        report = str(paths.COST_REPORT)   # paths.*, NOT WIKI/_meta (diverges under WIKIKB_VAULT_ROOT)
        if os.path.isfile(report):
            try:
                import json
                with open(report, encoding="utf-8") as fh:
                    rep = json.load(fh)
                print("  calls=%s prompt_tok=%s completion_tok=%s usd=%s cache_hits=%s"
                      % (rep.get("calls"), rep.get("prompt_tokens"), rep.get("completion_tokens"),
                         rep.get("usd"), rep.get("cache_hits")))
                by_dom = rep.get("by_domain") or {}
                for dom in sorted(by_dom):
                    d = by_dom[dom]
                    print("    %-18s calls=%s prompt_tok=%s usd=%s"
                          % (dom, d.get("calls"), d.get("prompt_tokens"), d.get("usd")))
                if not by_dom:
                    print("    (no per-domain generation calls recorded — run `eval.py --measure-llm` with a local model)")
            except Exception as e:  # noqa: BLE001
                print(f"  (spend table unavailable: {e})")
        else:
            print("  (spend table unavailable — run `eval.py --measure-llm`; the ledger is gitignored/regenerable)")

    if args.strict and errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
