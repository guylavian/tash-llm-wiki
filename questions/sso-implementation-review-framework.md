---
origin: eval-cohort
title: What is the SSO Implementation Review Framework?
type: question
domain: keycloak
slug: sso-implementation-review-framework
summary: The SSO Implementation Review Framework is a wiki-hosted evaluation-lens (MOC page `sso-implementation-review`) that maps every OIDC/SSO security concept to a best-practice rule, its anti-pattern, and the observable symptom — providing both proactive checklists (client/SPA + backend) and a symptom-to-cause reverse index for fault diagnosis.
sources:
  - id: sso-implementation-review
    type: wiki
    title: SSO / OIDC Implementation Review — Evaluation-Lens MOC
provenance_extracted: 0
provenance_inferred: 1
provenance_ambiguous: 0
tags: [sso, oidc, review, framework, security]
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# What is the SSO Implementation Review Framework?

⚠️ **Ungrounded provenance — this answer rests on synthesis, not extracted sources; weigh the References.** (The `sso-implementation-review` page was written from inferred upstream standards, not extracted from a single corpus source).

The **SSO Implementation Review Framework** (documented in [[sso-implementation-review]]) is a structured evaluation lens for reviewing whether an SSO/OIDC integration meets current best-practice standards (IETF, OIDF, OWASP). It organizes security concepts into three dimensions:

1. **Client / SPA checklist** — rules for browser-based Relying Parties: PKCE, redirect URI validation, `state`/`nonce`, token storage (BFF pattern), DPoP, back-channel logout, CORS, bearer-token usage, and revocation.

2. **Backend checklist** — rules for resource servers, confidential clients, BFFs, and M2M: JWT validation (sig/exp/iss/aud/typ), algorithm allowlisting, DPoP/mTLS binding, client credentials grant hygiene, refresh token rotation, JWKS caching, metadata discovery, and FAPI 2.0 compliance.

3. **Reverse index** — maps observable faults/tickets (e.g. "tokens readable via XSS", "logged out but token still works", "`alg=none` accepted") to the most likely root-cause concept page, turning production incidents into actionable diagnosis.

Each checklist row is a four-column table: Best-practice rule → Anti-pattern → Symptom (observable fault) → Wiki page link. The framework complements [[oidc-client-best-practices]] (which grounds the same concepts in RHBK/Keycloak specifics).

## References

**RH ground-truth** — none (this is an upstream `web:` tier page synthesized from IETF/OIDF/OWASP standards, not from any Red Hat corpus source).

**Wiki** — [[sso-implementation-review]] · [[pkce]] · [[redirect-uri-validation]] · [[state-and-nonce]] · [[token-storage-browser]] · [[bff-token-handler]] · [[dpop]] · [[mtls-bound-tokens]] · [[access-token-validation-resource-server]] · [[jwt-validation-pitfalls]] · [[refresh-token-rotation]] · [[back-channel-logout]] · [[rp-initiated-logout]] · [[cors-for-spa]] · [[bearer-token-usage]] · [[token-revocation]] · [[token-introspection]] · [[audience-and-scope-checks]] · [[authorization-server-metadata-discovery]] · [[issuer-identification-mixup]] · [[native-app-oauth]] · [[service-to-service-client-credentials]] · [[fapi2-security-profile]] · [[oidc-client-best-practices]]
