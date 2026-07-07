---
title: Air-Gapped Client Integration & Migration
type: entity
domain: keycloak
slug: air-gapped-client-integration
summary: "What changes when the network has no internet: how client apps get their OIDC/ SAML libraries, validate tokens, and migrate RH-SSO→RHBK without reaching public endpoints"
sources:
  - guide:operator_guide
  - guide:migration_guide
  - ref:rhbk-operator.md
  - ref:rhbk-platform-support.md
provenance_extracted: 2
provenance_inferred: 6
provenance_ambiguous: 0
tags: [clients]
status: draft
updated: 2026-07-02
---

# Air-Gapped Client Integration & Migration

**What changes when the network has no internet: how client apps get their OIDC/
SAML libraries, validate tokens, and migrate RH-SSO→RHBK without reaching public
endpoints.** Important for this environment — the team's network is disconnected.

## The core constraint
Nothing in the auth path may depend on a public URL at runtime or build time.
Everything must resolve to an **internal mirror/host** or a **local file**.
(inferred — a synthesis framing, not a single-source statement.)

## Library acquisition (build-time)
The per-stack libraries in [[client-libraries-by-stack]] still apply — but you
**cannot pull them from public registries**. Use internal mirrors:
- **Java/Maven** → internal **Nexus/Artifactory** proxy (Spring Security, Quarkus
  OIDC, the EAP 8 SAML/OIDC feature packs). (inferred — mirror-tooling names are
  not in this page's cited sources; see Contradictions below.)
- **Node/npm** → internal **Verdaccio/Artifactory** registry (`openid-client`,
  `passport-openidconnect`, `oidc-client-ts`). (inferred, same caveat.)
- **SPA bundles** → vendored into the app image at build, served from your host.
- **keycloak-js** → its "load from the Keycloak server" pattern is **air-gap
  ideal**: the browser fetches the adapter from your *internal* RHBK host, and it
  stays version-aligned with the server automatically. (inferred)

## Runtime — no public calls
- **Token validation:** JWKS ([[oidc-token-validation]]) is fetched from the
  **internal** realm `jwks_uri` (discovery `.well-known` on your host) — fine
  offline. Just don't hardcode or proxy to a public issuer; the `iss` must be the
  internal hostname ([[hostname-v2]]). (inferred — synthesized from linked
  entity pages, not a single cited source here.)
- **Discovery:** point RP libraries at the **internal** `.well-known/openid-
  configuration`.
- **SAML:** exchange **entity-descriptor files** manually rather than metadata-URL
  polling; if using metadata-by-URL, target the internal host. See
  [[saml-clients-and-migration]].

## Server / platform migration offline
- **Operator/images** from a **disconnected registry mirror**; manual OLM
  upgrade approval — grounded in `ref:rhbk-operator.md`'s air-gap notes. The
  specific tools named (`oc-mirror`, ImageContentSourcePolicy/IDMS) do not
  appear verbatim anywhere in this domain's corpus — general OpenShift
  knowledge, not corpus-verified (inferred). See [[operator-olm-install]] and
  [[custom-keycloak-image]] — use a **pre-optimized custom image** so the
  server never tries to reach out at start.
- **DB migration** is local (auto-migrate on first start) — no external dependency.
  See [[database-auto-migration]]. (inferred — the cited source only states DB
  migration is one-way, not the auto-on-first-start mechanics asserted here.)

## Note on this wiki's web-sourced material
Upstream/best-practice facts (RFC 9700, library status) were fetched **once** and
**embedded** into the wiki pages, so the *knowledge* is available offline even
though your network can't reach those URLs. The `web:` citations are provenance
labels, **not** a runtime dependency — treat them as "where this came from", and
re-verify only when you next have a connected machine. (inferred — meta-commentary
about this wiki's own methodology, not sourced from the raw layer.)

## Contradictions / caveats
- Exact mirror tooling (Nexus vs Artifactory vs Verdaccio) is site-specific; the
  corpus documents the **image/operator** disconnected flow, not language package
  mirrors (that part is operational guidance, not Red Hat ground-truth).
- `oc-mirror` / ImageContentSourcePolicy / ImageDigestMirrorSet are real
  OpenShift disconnected-install mechanisms but are **not present anywhere** in
  the `reference/keycloak/` or `../references/` corpus searched for this pass —
  treat as general platform knowledge, not a Red Hat RHBK-specific citation.
- Confirm disconnected-install specifics for your RHBK version in
  `ref:rhbk-operator.md` / `ref:rhbk-platform-support.md`.

## See also
- [[client-libraries-by-stack]]
- [[saml-clients-and-migration]]
- [[operator-olm-install]]
- [[custom-keycloak-image]]
- [[oidc-token-validation]]
- [[rhsso-to-rhbk-migration]]
