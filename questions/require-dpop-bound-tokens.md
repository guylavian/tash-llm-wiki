---
title: How to require DPoP-bound tokens for a client in RHBK
type: question
question_tier: conceptual
domain: keycloak
slug: require-dpop-bound-tokens
summary: "Enable the 'Require DPoP bound tokens' switch under Capability config in the Admin Console, or use the dpop-bind-enforcer client policy executor for bulk/advanced enforcement; DPoP is supported (not preview) as of RHBK 26.4+."
sources:
  - kb:dpop-
  - guide:securing_applications_and_services_guide
  - ref:rhbk-26-4-assembly-managing-clients-server-administration-guide.md
  - ref:rhbk-26-2-assembly-managing-clients-server-administration-guide.md
  - ref:rhbk-26-0-assembly-managing-clients-server-administration-guide.md
  - ref:rhbk-26-4-features.md
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 1
tags: [clients, dpop, tokens, security]
status: reviewed
updated: 2026-06-28
---

# How to require DPoP-bound tokens for a client in RHBK

**Toggle the "Require DPoP bound tokens" switch under the client's Capability config in the Admin Console. When ON, the client must send a valid DPoP proof JWT on every token request; requests without one are rejected. When OFF (default), DPoP is optional — the client may send a proof but is not forced to.**

## Per-client: Admin Console

1. In the Admin Console, navigate to **Clients** → your client → **Settings** tab.
2. Scroll to the **Capability config** section.
3. Locate the **Require DPoP bound tokens** switch and toggle it **ON**.
4. Save the changes.

The mapping between the Admin Console toggle and the underlying metadata:

| Admin Console | DPoP RFC / spec |
|---|---|
| "Require DPoP bound tokens" ON | `dpop_bound_access_tokens` client registration metadata = `true` — client MUST send a DPoP proof on every request |
| "Require DPoP bound tokens" OFF | `dpop_bound_access_tokens` = `false` — DPoP is optional; Bearer tokens are accepted |

### What happens when ON
- Every token request (authorization code flow, hybrid flow, refresh, etc.) requires a valid DPoP proof JWT in the `DPoP` HTTP header.
- RHBK validates the proof: verifies the signature, checks `htm`/`htu` match the actual request, confirms the public key JWK thumbprint is embedded in the issued token as `cnf.jkt`.
- If the DPoP proof is missing or invalid, RHBK rejects the request.
- **Public clients**: Both access tokens and refresh tokens are DPoP-bound. The client must use the same private key for refresh requests.
- **Confidential clients**: Only the access token is DPoP-bound; the refresh token relies on client credentials (client ID + secret / signed JWT) for security.
- RHBK also enforces DPoP on the **UserInfo endpoint**, **logout endpoint** (for public clients using refresh tokens), and **Admin/Account REST APIs** when a DPoP-bound token is presented.

### What happens when OFF
- The client *may* send a DPoP proof. If it does, RHBK verifies it and binds the token.
- If no proof is sent, RHBK issues a standard Bearer token.
- This is the best choice for gradual adoption or when not all resource servers support DPoP.

> ⚠️ RHBK client adapters do **not** support DPoP holder-of-key verification. Legacy adapters treat access and refresh tokens as Bearer tokens regardless of DPoP binding.

## Bulk / advanced: Client Policies (`dpop-bind-enforcer`)

For controlling DPoP enforcement across many clients at once, use the **`dpop-bind-enforcer`** executor inside a Client Policy. Three modes:

1. **Auto-Configuration** — automatically sets "Require DPoP bound tokens" ON for every newly registered or updated OIDC client.
2. **Refresh Token Only** — enforces DPoP binding for the **refresh token** only, leaving the access token as a standard Bearer. This is useful for public clients where legacy resource servers cannot handle DPoP-bound access tokens (introduced in RHBK 26.4).
3. **Strict OIDC Enforcement** — requires clients to send the `dpop_jkt` parameter during the initial Authorization Code flow, binding the entire authentication flow to the DPoP key.

## Version support — DPoP evolution across RHBK

| RHBK version | DPoP status | Feature flag |
|---|---|---|
| **26.0** | Technology Preview, disabled by default | `--features=dpop` or `--features=preview` |
| **26.2** | Technology Preview, disabled by default | `--features=dpop` or `--features=preview` |
| **26.4** | **Supported**, enabled by default | `dpop:v1` (no feature flag needed) |
| **26.6** | Supported, enabled by default; dedicated guide chapter | None |

In RHBK 26.0 the Admin Console switch was labelled **"OAuth 2.0 DPoP Bound Access Tokens Enabled"**. From 26.4 onward it is labelled **"Require DPoP bound tokens"**.

## Limitations

- **Token Exchange**: DPoP-bound tokens cannot be used as the `subject_token` in Standard Token Exchange (RFC 7800). Only Bearer tokens can be exchanged. However, you *can* obtain DPoP-bound tokens as *output* of token exchange by including a valid DPoP proof in the request.
- **mTLS bound tokens** (RFC 8705) are an alternative to DPoP that works with confidential clients using client certificates. DPoP is the recommended mechanism for public clients.

## See also
- [[dpop]] — RHBK entity page for DPoP
- [[dpop]] — RFC 9449 deep dive with validation rules and anti-patterns
- [[fapi-oauth21-profiles]] — FAPI / OAuth 2.1 client profiles that recommend DPoP
- [[client-authentication-methods]] — other ways clients authenticate to RHBK
- [[tokens-and-sessions]] — token lifespans, sessions, token lifecycle

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- **`kb:dpop-`** → `rhbk-26-6-dpop.md` — Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP), RHBK 26.6 Securing Applications and Services Guide
- **`ref:rhbk-26-4-assembly-managing-clients-server-administration-guide.md`** — Section 13.1.5 "DPoP", RHBK 26.4 Server Administration Guide (the "Require DPoP bound tokens" switch under Capability config)
- **`ref:rhbk-26-2-assembly-managing-clients-server-administration-guide.md`** — RHBK 26.2 Server Administration Guide (DPoP as Technology Preview: "Require Demonstrating Proof of Possession (DPoP) header in token requests")
- **`ref:rhbk-26-0-assembly-managing-clients-server-administration-guide.md`** — RHBK 26.0 Server Administration Guide (DPoP as Technology Preview: "OAuth 2.0 DPoP Bound Access Tokens Enabled")
- **`ref:rhbk-26-4-features.md`** — RHBK 26.4 Features table: `dpop:v1` listed under Supported features (enabled by default)
- **`ref:rhbk-26-6-newfeatures.md`** — RHBK 26.6 Release Notes: "New instructions for Demonstrating Proof-of-Possession"

### Wiki pages
- [[dpop]] — RHBK entity page on DPoP
- [[dpop]] — RFC 9449 sender-constraining entity page
  - `web:https://www.rfc-editor.org/rfc/rfc9449` — RFC 9449 OAuth 2.0 Demonstrating Proof-of-Possession
  - `web:https://www.rfc-editor.org/rfc/rfc9700` — RFC 9700 OAuth 2.0 Security Best Current Practice

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-dpop|Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP)]]
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
<!-- crosslink:end -->
