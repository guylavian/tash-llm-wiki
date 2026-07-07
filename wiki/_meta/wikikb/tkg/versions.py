#!/usr/bin/env python3
"""versions.py — the curated registry of REAL product version release dates. stdlib only.

This is the ONLY place a `valid_from` can originate (rule R1). It is a hand-curated map of
`family -> version -> {date, precision, source, note}`, gathered by reading public Red Hat sources
(see each `source`). The contract is **OMIT, NEVER FABRICATE**, with the precision of every date made
explicit — exactly like the wiki's own extracted/inferred/ambiguous provenance discipline:

  precision tiers
  ---------------
  * `verified`         — an explicit GA announcement states the date (e.g. a Red Hat blog/announcement).
  * `errata-confirmed` — no public GA date exists (Red Hat's exact GA dates and the product life-cycle page
                         are subscriber-paywalled), but a real, public, dated RHSA/RHEA *errata* proves the
                         version was available by that date. Used as a CONSERVATIVE LOWER BOUND on validity:
                         the docs were authoritative *by* this date (actual GA is earlier but not publicly
                         attributable). A temporal `as-of` query therefore *under*-includes near a release
                         boundary (a false negative) rather than over-claiming early validity — the honest
                         direction.
  * `approximate`      — only a month/quarter could be bounded, with no confirming errata for that exact
                         version; the day is a guess. RECORDED for a future human to confirm, but EXCLUDED
                         from `valid_from` (see USABLE_PRECISION) so a guessed day never becomes a temporal
                         claim.

`release_date()` returns a date ONLY for precision in USABLE_PRECISION ({verified, errata-confirmed}); for
anything else (approximate, unknown, or absent) it returns None and the CITES edge stays STRUCTURAL. The
temporal layer thus degrades gracefully (like embed.py's lexical fallback): a thinner registry simply yields
fewer version-temporal edges, never a fabricated date.

`updated:` (a synthesis page's edit metadata) is *structurally absent* from this file — there is no code path
from page frontmatter into the registry (rule R2). Release dates come from product life-cycle facts only.
"""
from __future__ import annotations

import re
from typing import Optional

USABLE_PRECISION = ("verified", "errata-confirmed")  # precisions allowed to populate a valid_from

# family -> version -> {date, precision, source, note}.  Sources read 2026-06-24.
RELEASES = {
    "rhbk": {
        # The corpus's cited Documentation notes are 26.2 / 26.4 / 26.6 — these errata dates are what
        # actually drive the temporal layer. Exact GA dates are paywalled; these are the earliest public
        # errata proving availability (conservative lower bounds).
        "26.6": {"date": "2026-06-03", "precision": "errata-confirmed",
                 "source": "https://access.redhat.com/errata/RHEA-2026:22857",
                 "note": "RHEA-2026:22857/22858 (26.6.2) issued 2026-06-03 — earliest public errata; upstream "
                         "Keycloak 26.6.0 was 2026-04-08, so RHBK 26.6 GA was Apr–Jun 2026 (exact GA paywalled)."},
        "26.4": {"date": "2025-11-13", "precision": "errata-confirmed",
                 "source": "https://access.redhat.com/errata/RHSA-2025:21370",
                 "note": "RHSA-2025:21370/21371 (26.4.4) issued 2025-11-13 — earliest public errata; upstream "
                         "Keycloak 26.4.0 was 2025-09-30 (exact RHBK GA paywalled)."},
        "26.2": {"date": "2025-06-09", "precision": "errata-confirmed",
                 "source": "https://access.redhat.com/errata/RHSA-2025:8690",
                 "note": "RHSA-2025:8690 (26.2.5) issued 2025-06-09 — earliest public errata; upstream "
                         "Keycloak 26.2.0 was 2025-04-11 (exact RHBK GA paywalled)."},
        "26.0": {"date": "2024-11-21", "precision": "errata-confirmed",
                 "source": "https://access.redhat.com/errata/RHSA-2024:10177",
                 "note": "RHSA-2024:10177 (26.0.6) issued 2024-11-21 — earliest confirmed public errata; "
                         "upstream Keycloak 26.0.5 was 2024-11-01; likely GA 2024-11."},
        "24.0": {"date": "2024-06-18", "precision": "approximate",
                 "source": "https://access.redhat.com/announcements/7075128",
                 "note": "Announcement title says 24.0 GA on 2024-06-18 but the page 404'd (subscriber-only); "
                         "could not confirm the body. Excluded from valid_from until confirmed."},
        "22.0": {"date": "2023-11-15", "precision": "verified",
                 "source": "https://access.redhat.com/articles/7044244",
                 "note": "Article states verbatim: 'On November 15th 2023, Red Hat announced the General "
                         "Availability of Red Hat build of Keycloak.' The first RHBK release."},
    },
    "rhsso": {
        # Legacy. No RH-SSO Source nodes exist in the current corpus, so these affect no edges today;
        # recorded for completeness/future. Only 7.1 has an explicit GA announcement.
        "7.6": {"date": "2022-10-01", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2022:7417",
                "note": "approximate (NOT errata-confirmed): the cited errata is for a later PATCH whose GA "
                        "predates it by an unknown interval, so the GA day can't be confirmed — do not upgrade."},
        "7.5": {"date": "2021-11-01", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2021:5218",
                "note": "approximate (NOT errata-confirmed): 7.5.0 existed before RHSA-2021:5218 (2021-12-20) "
                        "but the exact GA day is not public — bounded-above, not confirmed. Do not upgrade."},
        "7.4": {"date": "2020-06-15", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2020:2813",
                "note": "7.4.0 bounded May 12–Jul 2 2020 by errata; exact GA day not public."},
        "7.3": {"date": "2019-03-01", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2019:1140",
                "note": "7.3.0 bounded Feb–Apr 2019 by errata; exact GA day not public."},
        "7.2": {"date": "2018-02-01", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2018:0501",
                "note": "7.2.0 existed before RHSA-2018:0501 (2018-03-13); exact GA day not public."},
        "7.1": {"date": "2017-04-05", "precision": "verified",
                "source": "https://www.redhat.com/en/blog/announcing-red-hat-single-sign-71-ga-available",
                "note": "Red Hat blog post (2017-04-05) announces RH-SSO 7.1 GA; RHSA-2017:0872 the day prior."},
        "7.0": {"date": "2016-09-30", "precision": "approximate",
                "source": "https://access.redhat.com/errata/RHSA-2017:0872",
                "note": "First RH-SSO (Keycloak-based) release, ~Q3/Q4 2016; exact GA day not publicly confirmed."},
    },
}

# M3 (cross-domain temporal) is BLOCKED on harvest-side metadata, so NO inert registry entries are added:
#   * active-directory reference notes carry `family:`/`documentKind:` but NO `version:` (and documentKind is
#     "concept-article", not "Documentation"), so a windows-server family here (WS 2016/2019/2022/2025 GA dates)
#     would promote zero edges — the model's version+Documentation gates can never fire. Omitted until the
#     AD harvest emits a structured `version:`.
#   * cisco-ios-xe notes DO carry all three (e.g. version: ios-xe-16, family: ip-routing-*, documentKind:
#     Documentation), so cisco is NOT metadata-blocked — but it needs a `_FAMILY_ALIASES` mapping + publicly
#     sourced IOS-XE GA dates, neither of which is in scope here. Left for a dedicated cisco temporal pass.

# Reference-note `family:` values and CLI tokens normalize onto the keys above.
_FAMILY_ALIASES = {
    "rhbk": "rhbk", "keycloak": "rhbk", "red hat build of keycloak": "rhbk",
    "rhsso": "rhsso", "rh-sso": "rhsso", "rh_sso": "rhsso", "red hat single sign-on": "rhsso",
}
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_VERSION_RE = re.compile(r"^\d+(?:\.\d+){0,2}$")


def _norm_family(family: Optional[str]) -> Optional[str]:
    return _FAMILY_ALIASES.get((family or "").strip().lower())


def _valid_iso(s: str) -> bool:
    """True iff s is a calendar-plausible ISO date YYYY-MM-DD (month 01–12, day 01–31). Rejects shapes like
    2025-99-99 so a malformed --as-of can't become a bogus cutoff. With plausible dates, lexical string
    order == chronological order, which the `valid_from <= asof` comparison relies on."""
    if not _ISO_DATE_RE.match(s or ""):
        return False
    y, m, d = (int(x) for x in s.split("-"))
    return 1 <= m <= 12 and 1 <= d <= 31


def _record(family: Optional[str], version: Optional[str]) -> Optional[dict]:
    fam = _norm_family(family)
    if not fam:
        return None
    return (RELEASES.get(fam) or {}).get(str(version or "").strip())


def release_info(family: Optional[str], version: Optional[str]):
    """(date, precision) for (family, version) when the date is USABLE, else (None, None). The SINGLE home
    of the eligibility check (USABLE_PRECISION + valid ISO) — release_date()/precision() delegate here so the
    two can't drift, and model.py gets both in one lookup."""
    rec = _record(family, version)
    if rec and rec.get("precision") in USABLE_PRECISION and _valid_iso(str(rec.get("date") or "")):
        return rec["date"], rec["precision"]
    return None, None


def release_date(family: Optional[str], version: Optional[str]) -> Optional[str]:
    """The usable ISO release date for (family, version), or None ⇒ the edge stays STRUCTURAL. Only
    precisions in USABLE_PRECISION qualify; approximate/unknown return None (omit-not-fabricate)."""
    return release_info(family, version)[0]


def precision(family: Optional[str], version: Optional[str]) -> Optional[str]:
    """The precision tier of the usable date for (family, version), or None if not usable."""
    return release_info(family, version)[1]


def resolve_asof(token: Optional[str], family: Optional[str] = None) -> Optional[str]:
    """Map an `--as-of` token to an ISO date for comparison against an edge's valid_from. Accepts a
    calendar-plausible ISO date verbatim, or a version string resolved through the registry (usable
    precisions only). For a bare version with no family hint it searches ALL families and resolves ONLY if
    unambiguous: if two families map the same version string to DIFFERENT dates it returns None (the caller
    reports it) rather than silently picking one. Returns None when it can't honestly resolve a usable date."""
    if not token:
        return None
    token = token.strip()
    if _valid_iso(token):
        return token
    if _VERSION_RE.match(token):
        if family:
            return release_date(family, token)
        dates = {release_date(fam, token) for fam in RELEASES}
        dates.discard(None)
        if len(dates) == 1:          # exactly one distinct usable date across families → unambiguous
            return next(iter(dates))
        # 0 matches, or >1 distinct dates (ambiguous across families) → can't honestly resolve
    return None
