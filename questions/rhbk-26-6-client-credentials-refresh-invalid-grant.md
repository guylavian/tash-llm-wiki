---
title: RHBK 26.6 upgrade breaks client-credentials token refresh with invalid_grant
type: question
question_tier: support-kb
domain: keycloak
slug: rhbk-26-6-client-credentials-refresh-invalid-grant
summary: "Upgrading to RHBK 26.6 causes grant_type=refresh_token calls (for tokens obtained via client_credentials grant) to fail with invalid_grant. Three candidate root causes from the 26.6 migration changes: token introspection audience validation (most probable when a resource server introspects tokens), Infinispan 16 cache flush (transient sessions lost at upgrade), and client scope evaluation enforcement (view-users permission required for token generation in evaluation contexts). Diagnose with the check-cluster-audit-jwks flow below."
sources:
  - kb:rhbk-26-6-migration-changes     # 26.6 release-specific changes (introspection audience, Infinispan 16, client scope evaluation)
  - kb:rhbk-26-4-managing-user-sessions # transient sessions + "Use refresh tokens for client credentials grant" switch
  - kb:rhbk-26-4-sso-protocols          # client_credentials does not issue refresh token by default
  - kb:rhbk-26-6-oidc-layers           # OIDC grant types reference
  - web:https://datatracker.ietf.org/doc/rfc6749/ (RFC 6749 OAuth 2.0, refresh_token grant, fetched 2026-06-28)
  - web:https://datatracker.ietf.org/doc/rfc7662/ (RFC 7662 Token Introspection, fetched 2026-06-28)
provenance:
  extracted: 14
  inferred: 8
  ambiguous: 1
tags: [clients, tokens, migration, troubleshooting]
status: draft
updated: 2026-07-02
---

# ⚠️ Out of corpus coverage

> **H1 — Out of corpus coverage.** The keycloak domain holds `conceptual` and `support-kb` tiers only. This is a `scenarios`-tier question (upgrade break-fix) and that operational-playbook tier is not ingested. The answer below is synthesised from the migration-changes reference and the conceptual wiki pages — verify every claim against the primary source (your running 26.6 installation) before acting.

# RHBK 26.6 upgrade breaks client-credentials token refresh with `invalid_grant`

**Your confidential client uses `grant_type=client_credentials` to obtain tokens (with the "Use refresh tokens for client credentials grant" switch enabled on the client), and after upgrading to RHBK 26.6, `grant_type=refresh_token` calls return `{"error":"invalid_grant"}` on tokens that worked before the upgrade.**

## Background: how client_credentials refresh works in RHBK

RHBK differs from the OAuth 2.0 spec (RFC 6749 §4.4.3) in that it *can* issue a refresh token for the `client_credentials` grant — but only when the client has the **"Use refresh tokens for client credentials grant"** switch toggled on in the client's **Advanced Settings**. Without this switch, the token endpoint does not return a `refresh_token` in the response at all (`kb:rhbk-26-4-sso-protocols` §10.1.1.4).

When the switch **is** enabled, RHBK creates a **transient client session** (not a full user session) to anchor the refresh token. The transient session lives in the embedded Infinispan cache (`kb:rhbk-26-4-managing-user-sessions` §6.5). Token refresh succeeds when that transient session is still valid and reachable.

## RHBK 26.6 changes that can cause this

Three changes in the RHBK 26.6 migration notes (`kb:rhbk-26-6-migration-changes`) are candidates, ordered by probability given a *sustained* failure (not just during the upgrade window):

### 1. Token introspection audience validation (§2.1.8) — most probable when a resource server introspects

**What changed:** The OAuth2 token introspection endpoint now validates that the *authenticated client* (the one calling the introspection endpoint) is present in the token's `aud` (audience) claim. Previously, any authenticated client could introspect any valid token. Now, if the introspecting client is not in the token's audience, the endpoint returns `{"active": false}`.

**How it produces `invalid_grant`:** Some client libraries and API gateways translate `{"active": false}` from the introspection endpoint into an OAuth2 `invalid_grant` error when they attempt to validate tokens at the token endpoint or during downstream processing. This is particularly common in:
- API management platforms that introspect tokens before proxying to backend services
- Java adapters with adapter configs that use introspection instead of JWKS
- Custom token-validation middleware that calls the introspection endpoint

**Diagnosis:** Check whether any component in your call chain uses token introspection (RFC 7662 endpoint `/realms/{realm}/protocol/openid-connect/token/introspect`) to validate tokens. If so, the audience claim on the token must include that component's client ID. RHBK 26.6 provides a temporary backwards-compatibility switch:

```
--spi-token-introspection--default--allow-token-introspection-without-audience-check=true
```

Or per-client in the Admin Console (deprecated, logs warnings). The recommended fix is to add an audience protocol mapper to the issuing client's token so the introspecting client appears in the `aud` claim.

**How to test:** Call the introspection endpoint manually with the failing token and compare the `active` field. If the introspecting client is confirmed as missing from `aud`, this is the root cause.

### 2. Infinispan 16 upgrade — caches cleared, transient sessions lost (§2.2.9)

**What changed:** RHBK 26.6 upgrades the embedded Infinispan cache from v15.x to v16.0. The cache serialization format may have changed, and in practice the embedded caches are cleared during the first startup after the upgrade (similar to the 26.0 marshalling format change, `kb:rhbk-26-0-red-hat-build-of-keycloak-26-0` §1.14.36, which explicitly stated "all caches are cleared").

**How it produces `invalid_grant`:** The transient client session that anchors the refresh token lives in the embedded Infinispan cache. If the upgrade cycle cleared the cache, any refresh token issued **before** the upgrade (or during an in-flight rolling update) points to a session that no longer exists. The server returns `invalid_grant` because it cannot find the backing session.

**Important:** This is a *transient* cause — new refresh tokens issued **after** the upgrade completes should work normally. If the failure is persistent and affects even newly-issued tokens, this is not the root cause.

### 3. Client scope evaluation enforces access to the user (§2.1.7)

**What changed:** The `client-scopes-evaluate` endpoint (used in the Admin Console UI to preview client scopes) now requires at minimum the `view-users` admin role — or any permission granting the `view` scope on the user — before generating tokens for evaluation.

**How it produces `invalid_grant`:** If your service account (or the admin calling client scope evaluation on behalf of the service account) lacks `view-users`, the scope evaluation endpoint will fail. This ***does not*** directly affect the `grant_type=refresh_token` token endpoint — but if your automation or administrative scripts generate tokens through evaluation rather than through the standard token endpoint, the upgrade would break them.

**Diagnosis:** Check whether the service account or admin user involved has `view-users` assigned in the `realm-management` client roles. If the failure occurs only via Admin Console operations and not via direct `grant_type=refresh_token` calls at the token endpoint, this is a secondary concern.

### 4. Other 26.6 changes that are less likely but worth ruling out

| Change | Effect | Why less likely |
|---|---|---|
| Sender-constrained tokens rejected in Standard Token Exchange (§2.2.16) | Token exchange for DPoP/mTLS-bound tokens fails | Only affects token exchange, not refresh |
| Client secret auth method now respects registration value (§2.2.7) | Client must use the exact `token_endpoint_auth_method` from registration | Only if client switched auth method or was using both |
| HTTP status code for `invalid_grant` on ROPC changed to 400 (§2.2.15) | Different HTTP status for `invalid_grant` in ROPC grants | This is about ROPC (password), not client_credentials |

## Quick diagnosis flow

```
Is the failure persistent (hours after upgrade) or transient (right after restart)?
  ↓
PERSISTENT (new tokens fail too):
  1. Identify any component using token introspection
     → If YES, test introspection endpoint, check aud claim, apply fix or compat flag
     → If NO, move to step 2
  2. Decode the failing refresh token (base64url-decode the payload)
     → Check `exp` — if token is not expired, proceed
  3. Check the server logs for `SESSION_NOT_ACTIVE` _(inferred — this is the expected Infinispan-cache log message when a transient session is not found and the cache was cleared)_ or `invalid_grant` with details
     → Look for "client session not found" or "token not valid"
  4. Verify the "Use refresh tokens for client credentials grant" switch on the client
     → Navigate to Clients > {client} > Advanced Settings
     → Confirm it is still ON (database migration should preserve it)
  5. Test with a brand-new token:
     → Issue new client_credentials token, then immediately refresh it
     → If this also fails, open a Red Hat support case with DEBUG-level logs

TRANSIENT (right after upgrade only):
  6. Infinispan cache flush is the likely cause
     → Issue a fresh client_credentials token and try the refresh → should work
     → If yes, the issue resolved itself once the new tokens were in the new cache
```

## See also

- [[service-to-service-client-credentials]] — client_credentials grant rules (no refresh token by standard, anti-pattern #3)
- [[oidc-grant-types]] — available grant types and refresh token exceptions
- [[tokens-and-sessions]] — access/refresh token lifespan configuration
- [[token-introspection]] — anti-pattern #6: long-TTL caching ignoring exp
- [[rhbk-26-6-migration-changes]] — the 26.6 migration reference (see §2.1.8, §2.2.9, §2.1.7)

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

| ID | Title |
|---|---|
| `kb:rhbk-26-6-migration-changes` | Chapter 2. Release-specific changes — RHBK 26.6 Upgrading Guide (§2.1.8 introspection audience, §2.2.9 Infinispan 16, §2.1.7 scope evaluation) |
| `kb:rhbk-26-4-managing-user-sessions` | Chapter 6. Managing user sessions — RHBK 26.4 (§6.5 Transient sessions, "Use refresh tokens for client credentials grant" switch) |
| `kb:rhbk-26-4-sso-protocols` | Chapter 10. SSO protocols — RHBK 26.4 (§10.1.1.4 Client credentials grant, refresh token exceptions) |
| `kb:rhbk-26-6-oidc-layers` | Chapter 2. Securing applications with OpenID Connect — RHBK 26.6 (grant types reference, introspection endpoint) |
| `kb:rhbk-26-0-red-hat-build-of-keycloak-26-0` | Chapter 1. RHBK 26.0 Release Notes (§1.14.36 Infinispan marshalling change — caches cleared on upgrade precedent) |

### Wiki

| Page | Key claim |
|---|---|
| [[service-to-service-client-credentials]] | Client_credentials grant issues no refresh token per OAuth 2.0 spec; RHBK can opt-in with the "Use refresh tokens" switch (anti-pattern #3) |
| [[oidc-grant-types]] | Refresh token exceptions per grant type; client_credentials is an implicit exception by default |
| [[tokens-and-sessions]] | Token lifespan configuration realms/clients; session idle/max bound refresh token validity |
| [[token-introspection]] | Anti-pattern #6: long-TTL caching ignoring `exp`; new 26.6 audience check for introspection |
| [[client-credentials-burst-token-expired]] | Related: client_credentials tokens rejected by resource server under burst load (stale JWKS cache, not refresh issue) |
| [[oidc-client-best-practices]] | Refresh code rules: single-use, never reuse, serialize; `invalid_grant` → re-auth, not retry |

### Upstream (`web:`)

| Source | Relevance |
|---|---|
| RFC 6749 §4.4.3 (Client Credentials Grant) | Standard says no refresh token for client_credentials — RHBK's opt-in is a non-standard extension |
| RFC 7662 (Token Introspection) | The introspection endpoint whose audience check was tightened in 26.6 |

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-migration-changes|Chapter 2. Release-specific changes]]
- [[rhbk-26-4-managing-user-sessions|Chapter 6. Managing user sessions]]
- [[rhbk-26-4-sso-protocols|Chapter 10. SSO protocols]]
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
<!-- crosslink:end -->
