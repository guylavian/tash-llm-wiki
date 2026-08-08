# `_sources/cisco-ios-xe/` — raw notes (the immutable ground truth)

Cisco IOS XE is a **notes-first** domain: there is no harvested Red Hat-style
corpus. The Markdown notes in this folder **are** the raw tier — the ground truth
the `cisco-ios-xe` synthesis pages are built on. They are distilled, **paraphrased**
facts from the official Cisco IOS XE configuration guides (provenance, not
transcripts — no long verbatim, per copyright + the wiki rule). Treat them like the
immutable `reference/<domain>/` notes for a corpus-backed domain:

- **One file per source guide / topic cluster.** Named for the concept
  (`ospf-routing.md`, `bgp-routing.md`, `lan-switching.md`, `system-management.md`).
- **Cite it from synthesis pages** with `note:_sources/cisco-ios-xe/<file>.md` in the
  page's `sources:` block (path is relative to `wiki/`). Also carry the upstream
  Cisco doc as a `web:` URL on the synthesis page where one applies.
- **Excluded from the content scanners.** `lint.py` / `index.py` / `crosslink.py`
  scan only `topics/ entities/ questions/`; files here are never linted or counted
  as pages.
- **Provenance, not transcripts.** Each note records its source guide (title +
  IOS XE train, e.g. "IP Routing: OSPF Configuration Guide, IOS XE 16") and the
  load-bearing facts in our own words.

Source guides distilled into this tier (IOS XE 16 / 3S configuration guides):
- **IP Routing: OSPF Configuration Guide** (IOS XE 16) → `ospf-routing.md`
- **IP Routing: BGP Configuration Guide** (IOS XE 16) → `bgp-routing.md`
- **IP Routing: Protocol-Independent Configuration Guide** (IOS XE 3S) → `protocol-independent-routing.md`
- **LAN Switching Configuration Guide** (IOS XE) → `lan-switching.md`

> A 5th PDF supplied with these (`config_system_management_chapter…`) turned out to be
> the **Cisco WLC System Management Guide (AireOS 7.4)** — a different product family, NOT
> IOS XE — so it is intentionally excluded from this brain (it belongs in a separate
> `cisco-wlc` domain).

Grow via the wiki **INGEST** op in `../../CLAUDE.md`; the domain was onboarded via
**Operation: ADD DOMAIN** (worked example: `../../_meta/ADD-DOMAIN.md`).
