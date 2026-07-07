---
title: 3scale API Management ↔ Red Hat SSO / RHBK Support Matrix
type: entity
domain: keycloak
slug: 3scale-rhsso-support
summary: "Which identity-provider product/version Red Hat 3scale API Management is tested and supported with for SSO integration"
sources:
  - external:Red Hat 3scale API Management supported-configurations (user-supplied 2026-06-16)
  - ref:rhbk-platform-support.md
provenance_extracted: 2
provenance_inferred: 4
provenance_ambiguous: 0
tags: [migration]
status: draft
updated: 2026-07-02
---

# 3scale API Management ↔ Red Hat SSO / RHBK Support Matrix

**Which identity-provider product/version Red Hat 3scale API Management is tested
and supported with for SSO integration.**

## Fact (3scale 2.14)
3scale API Management **2.14** is tested and supported with:

| Product | Version |
|---|---|
| Red Hat Single Sign-On | **7.6** |

> *Red Hat note:* "Support for 3scale's integration with Red Hat Single Sign-On
> will be replaced with **Red Hat Build of Keycloak** in future releases."

## Interpretation
- For 3scale 2.14, the **only supported** SSO IdP is RH-SSO **7.6** — not RHBK,
  yet. RHBK becomes the supported integration in a *future* 3scale release. (inferred)
- Practically: if you're on 3scale 2.14 and planning the [[rhsso-to-rhbk-migration]],
  do **not** assume the 3scale↔IdP integration is covered by RHBK until the
  3scale release notes for your target version list RHBK explicitly. (inferred)
- 3scale uses RH-SSO/RHBK as an OIDC provider for API authentication (the generic
  OIDC adapter/endpoint behavior — see [[oidc-token-validation]]). (inferred)

## Caveats
- **Not in the bundled corpus.** The offline `kb/` harvest does not contain the
  3scale supported-configurations page; this fact is **user-supplied** and dated.
  Re-verify against the official 3scale "Supported Configurations" page for the
  exact 3scale version before relying on it.
- Version-locked: applies to **3scale 2.14**. A different 3scale version may
  support different (or RHBK) IdP versions. (inferred)

## Contradictions / caveats
- The 3scale-support fact and quote come from a `external:` (user-supplied)
  source, not the bundled corpus, and `ref:rhbk-platform-support.md` does not
  mention 3scale at all — the fact itself is unverified against ground truth
  and should be re-checked against the live 3scale docs.

## See also
- [[rhsso-to-rhbk-migration]]
- [[oidc-token-validation]]
