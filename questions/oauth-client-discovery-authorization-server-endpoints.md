---
title: How do OAuth clients discover an authorization server's endpoints and capabilities?
type: question
question_tier: conceptual
domain: keycloak
slug: oauth-client-discovery-authorization-server-endpoints
summary: "OAuth clients discover an AS's endpoints and capabilities via two standardized well-known URL conventions (OIDC Discovery 1.0 and RFC 8414), with strict issuer validation required."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc8414 (RFC 8414 — OAuth 2.0 AS Metadata, fetched 2026-06-17)
  - web:https://openid.net/specs/openid-connect-discovery-1_0.html (OpenID Connect Discovery 1.0, fetched 2026-06-17)
  - guide:securing_applications_and_services_guide
  - ref:rhbk-26-4-migration-changes.md (RHBK 26.4 migration notes, RFC 8414 support)
  - ref:rhbk-26-4-reverseproxy.md (Reverse proxy path mapping for /.well-known/)
  - ref:rhbk-26-0-hostname.md (Hostname config impact on discovery URLs)
provenance:
  extracted: 8
  inferred: 2
  ambiguous: 0
tags: [authz, clients]
status: draft
updated: 2026-07-07
---

# How do OAuth clients discover an authorization server's endpoints and capabilities?

**Answer: OAuth 2.0 / OIDC clients discover an authorization server's (AS) endpoints — authorization, token, userinfo, JWKS, revocation, introspection, logout — via a standardized metadata document fetched from a well-known HTTPS URL. Two specifications define slightly different URL constructions, and every response must be validated with a byte-for-byte issuer match.**

## Discovery URL conventions

Two standards define how to construct the metadata URL from an issuer identifier:

- **OIDC Discovery 1.0** ($1, OpenID Connect Discovery): append `/.well-known/openid-configuration` to the issuer URL. Example issuer `https://as.example.com/realms/myrealm` → `https://as.example.com/realms/myrealm/.well-known/openid-configuration`. Strip any trailing slash before appending (`oidc-endpoints.md:26`).

- **RFC 8414 (OAuth 2.0 AS Metadata, §3):** insert `/.well-known/oauth-authorization-server` between the host and the issuer's path. Issuer `https://as.example.com` → `https://as.example.com/.well-known/oauth-authorization-server`. Issuer with path `https://as.example.com/issuer1` → `https://as.example.com/.well-known/oauth-authorization-server/issuer1`.

**These are structurally different** (`authorization-server-metadata-discovery.md:35`, inferred). A client that treats them as equivalent will build the wrong URL when the issuer has a path component.

## What the document contains

The JSON document advertises every endpoint and capability the AS supports:

| Field | Meaning |
|---|---|
| `issuer` | The AS's issuer identifier (REQUIRED — must byte-match the request URL) |
| `authorization_endpoint` | Browser redirect for user auth (REQUIRED unless grant types don't need it) |
| `token_endpoint` | Token grant/code exchange/refresh (REQUIRED unless implicit-only) |
| `userinfo_endpoint` | Standard claims from ID Token |
| `jwks_uri` | JWK Set URL for offline token validation (REQUIRED per OIDC Discovery §3) |
| `end_session_endpoint` | RP-initiated logout |
| `introspection_endpoint` | Token active-state check (RFC 7662) |
| `revocation_endpoint` | Token revocation (RFC 7009) |
| `device_authorization_endpoint` | Device Authorization Grant (RFC 8628) |
| `response_types_supported` | e.g. `code`, `id_token` (REQUIRED per RFC 8414 §2) |
| `grant_types_supported` | e.g. `authorization_code`, `client_credentials` |
| `id_token_signing_alg_values_supported` | Signing algs for ID Tokens (RS256 REQUIRED per OIDC Discovery §3) |
| `scopes_supported` | Must include `openid` per OIDC Discovery §3 |
| `code_challenge_methods_supported` | PKCE support (`S256`) |
| `subject_types_supported` | e.g. `public`, `pairwise` (REQUIRED per OIDC Discovery §3) |

(OIDC Discovery §3, RFC 8414 §2; `oidc-endpoints.md:25-50`)

## Critical validation: exact-match issuer check

Both RFC 8414 (§3.3, §6.2) and OIDC Discovery (§4.3, §7.2) require the returned `issuer` value to be **byte-for-byte identical** to the issuer URL used in the discovery request. A trailing slash, scheme case difference, or proxy-rewritten hostname means the document MUST be rejected (`authorization-server-metadata-discovery.md:43`).

In OIDC, the ID Token's `iss` claim must also match the issuer from discovery — this is the primary defense against authorization-server mix-up attacks (`authorization-server-metadata-discovery.md:61-63`).

## RHBK-specific details

- **OIDC Discovery URL per realm:** `https://{host}/realms/{realm}/.well-known/openid-configuration` (`oidc-endpoints.md:26`).
- **RFC 8414 URL (RHBK 26.4+):** `https://{host}/.well-known/oauth-authorization-server/realms/{realm}` — RHBK 26.4 added this alternative path for clients that follow the RFC 8414 construction (`rhbk-26-4-migration-changes.md:310-315`).
- **Reverse proxy must expose `/.well-known/`** for RFC 8414 discovery to function. The recommended proxy path mapping is `/.well-known/` → `/.well-known/` (`rhbk-26-4-reverseproxy.md:111`).
- **Hostname configuration controls discovery document URLs:** the `hostname` (frontend), `hostname-backchannel-dynamic`, and `hostname-url` options determine what base URLs appear in the discovery document. The base URL affects how applications discover endpoints from the OIDC Discovery Document (`rhbk-26-0-hostname.md:94`, inferred).
- **`http-relative-path` requires extra reverse proxy mapping:** if configured, map the `/.well-known/` path without the prefix to the path with the prefix on the server (`rhbk-26-4-migration-changes.md:318-320`).
- **UMA 2.0 discovery** is a separate well-known endpoint: `/realms/{realm}/.well-known/uma2-configuration` (`rhbk-26-6-service-overview.md:22-26`).

## JWK Set retrieval

The `jwks_uri` field in the discovery document points to the AS's public key set. Clients must fetch and refresh keys from this URI at runtime (honoring the `kid` header in tokens) rather than caching keys at deploy time. This is the only safe path through AS key rotations (`authorization-server-metadata-discovery.md:47`, inferred).

## Contradictions / caveats

- Upstream OSS Keycloak and RHBK both follow the same well-known conventions, but RHBK 26.4+ adds the RFC 8414 alternative path — which older clients may not use. The OIDC Discovery path (`/.well-known/openid-configuration`) works across all RHBK and RH-SSO versions.

## References

### RH ground-truth
- `kb:oidc-layers-` — OIDC endpoints and discovery (from RH Securing Applications guide)
- `ref:rhbk-26-4-migration-changes.md` — RFC 8414 support added in RHBK 26.4
- `ref:rhbk-26-4-reverseproxy.md` — Reverse proxy path mapping for `/.well-known/`
- `ref:rhbk-26-0-hostname.md` — Hostname config impact on discovery document URLs
- `ref:rhbk-26-6-service-overview.md` — UMA 2.0 discovery endpoint

### Wiki pages
- [[authorization-server-metadata-discovery]] — detailed entity page with rules, anti-patterns, symptoms, and client per-surface guidance
- [[oidc-endpoints]] — the full set of RHBK OIDC endpoints per realm
- [[oidc-client-best-practices]] — how to write client code correctly
- [[issuer-identification-mixup]] — RFC 9207 `iss` response param defense
- [[sso-implementation-review]] — evaluation lens covering client discovery pitfalls

### Web (upstream)
- RFC 8414 (OAuth 2.0 Authorization Server Metadata, fetched 2026-06-17)
- OpenID Connect Discovery 1.0 (fetched 2026-06-17)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
<!-- crosslink:end -->
