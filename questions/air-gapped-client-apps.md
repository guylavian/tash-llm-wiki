---
origin: eval-cohort
title: What changes when client apps operate in air-gapped networks without internet
slug: air-gapped-client-apps
type: question
domain: keycloak
summary: In an air-gapped network, OIDC/SAML client apps must acquire libraries from internal mirrors, validate tokens against internal hostnames (never public issuers), use pre-optimized server images, and handle SAML metadata by manual descriptor exchange rather than URL polling.
sources:
  - entities/air-gapped-client-integration
  - entities/client-libraries-by-stack
  - entities/oidc-token-validation
  - entities/custom-keycloak-image
provenance_extracted: 2
provenance_inferred: 5
provenance_ambiguous: 0
tags: [clients, server-config, migration]
status: draft
question_tier: conceptual
updated: 2026-07-12
graph_community: "Tokens & Sessions"
---

# What changes when client apps operate in air-gapped networks without internet?

## Answer

Every part of the OIDC/SAML client integration path that touches a public URL must be redirected to an internal equivalent. The three areas that change:

### 1. Library acquisition (build-time)
Public package registries are unreachable. Use an **internal mirror** for each language ecosystem:
- **Java/Maven** → internal Nexus/Artifactory proxy for Spring Security, Quarkus OIDC, EAP 8 feature packs *(inferred)*
- **Node/npm** → internal Verdaccio/Artifactory for `openid-client`, `passport-openidconnect`, `oidc-client-ts` *(inferred)*
- **SPA bundles** → vendored into the app image at build time, served from your own host *(inferred)*
- **keycloak-js** → its "load from Keycloak server" pattern is air-gap ideal: the browser fetches the adapter from your *internal* RHBK host, staying version-aligned automatically *(inferred, extracted from air-gapped-client-integration)*

### 2. Runtime — no public calls
- **Token validation:** JWKS ([[oidc-token-validation]]) is fetched from the **internal** realm `jwks_uri` via discovery `.well-known` on your host. The `iss` claim must be the internal hostname ([[hostname-v2]]) — never hardcode or proxy to a public issuer *(inferred)*
- **Discovery:** Point RP libraries at the **internal** `.well-known/openid-configuration` URL *(inferred)*
- **SAML:** Exchange entity-descriptor files manually rather than metadata-URL polling; if metadata-by-URL is required, target the internal host ([[saml-clients-and-migration]]) *(extracted from air-gapped-client-integration)*

### 3. Server / platform migration offline
- **Operator/images** must come from a **disconnected registry mirror**; use a **pre-optimized custom image** ([[custom-keycloak-image]]) so the server never reaches out at start *(extracted from air-gapped-client-integration)*
- **DB migration** is local and automatic ([[database-auto-migration]]) — no external dependency *(inferred)*

### Provenance note
This answer synthesizes from the draft [[air-gapped-client-integration]] page (`extracted: 2, inferred: 6`). The exact mirror tooling (Nexus vs Artifactory vs Verdaccio, `oc-mirror`, ImageContentSourcePolicy) is site-specific operational guidance not present verbatim in the keycloak corpus.

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- **keycloak reference — operator_guide** — via [[air-gapped-client-integration]]
- **keycloak reference — migration_guide** — via [[air-gapped-client-integration]]
- **RHBK Operator on OpenShift — Keycloak CR Reference — RHBK 26.6** (`references/rhbk-operator`)
- **RHBK Platform & Support — Offline Reference** (`references/rhbk-platform-support`)

### Wiki
- [[air-gapped-client-integration]] — entity page on air-gap changes
- [[client-libraries-by-stack]] — per-stack library choices
- [[oidc-token-validation]] — JWKS vs introspection validation
- [[saml-clients-and-migration]] — SAML integration and migration
- [[operator-olm-install]] — Operator installation, including disconnected mirror
- [[custom-keycloak-image]] — pre-optimized custom image for air-gap
- [[hostname-v2]] — hostname configuration for internal issuer
- [[database-auto-migration]] — automatic database migration
