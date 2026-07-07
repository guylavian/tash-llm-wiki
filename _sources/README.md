# `_sources/` — per-domain raw staging (NOT wiki content)

Raw, pre-synthesis material, **namespaced one folder per domain** to match the
`domain:` partition of the vault. Nothing here is a synthesized page: `lint.py`,
`index.py`, and `crosslink.py` scan only `topics/ entities/ questions/`, so files
under `_sources/` are never linted, linked, or counted — same discipline as `_meta/`.

```
_sources/
├── keycloak/          # upstream web: tier — IETF RFCs, OIDF, OWASP, practitioner docs
│                      #   (corpus-backed domain; RH ground truth lives in reference/keycloak/)
└── active-directory/  # notes-first ground truth + _raw/ harvest drop zone
    └── _raw/          #   bulk docs harvest staging, pre-fold-in (see its README)
```

Two kinds of raw tier land here, depending on the domain's `shape:` (see
`_meta/taxonomy.md`):

- **Corpus-backed domain (keycloak):** the authoritative raw tier is the immutable
  `reference/<domain>/` notes folded in from a harvest. `_sources/<domain>/` then
  holds only the **upstream `web:` tier** — standards/best-practice notes that enrich
  the synthesis but are *not* product support statements. Cited in pages via `web:`.
- **Notes-first domain (active-directory):** there is no harvested corpus, so the
  Markdown you author in `_sources/<domain>/` **is** the immutable ground truth.
  Cited in pages via `note:_sources/<domain>/<file>.md`. A `_raw/` subfolder may hold
  a bulk docs harvest awaiting fold-in (which can promote the domain to
  corpus-backed — see `_meta/ADD-DOMAIN.md`).

In all cases: provenance, not transcripts — record each source's URL + fetch date and
the load-bearing facts (paraphrased, no long verbatim). Grow via the wiki **INGEST**
op in `../CLAUDE.md`; onboard a new domain via **Operation: ADD DOMAIN**.
