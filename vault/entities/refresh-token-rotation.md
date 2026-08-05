---
title: Refresh Token Rotation
type: entity
domain: keycloak
slug: refresh-token-rotation
summary: "Refresh token rotation is a one-time-use mechanism that defends public clients against stolen refresh tokens by issuing a new token on every refresh and revoking the entire grant chain when a replayed (already-consumed) token is detected."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 Security BCP, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (Browser-Based Apps BCP draft-26, fetched 2026-06-17)
provenance_extracted: 12
provenance_inferred: 3
provenance_ambiguous: 0
tags: [tokens, security, concept]
symptoms:
  - "invalid_grant"
status: reviewed
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# Refresh Token Rotation

**A per-use refresh token policy that issues a replacement token on every redemption and treats reuse of an already-consumed token as an indicator of theft.**

## Rule

Public clients (SPAs, native apps) MUST either use refresh token rotation or hold sender-constrained (DPoP / mTLS-bound) refresh tokens — plain long-lived static refresh tokens are prohibited (RFC 9700 §2.2.2, §4.14; OAuth 2.1 §4.3; BBA draft-26 §6.3.2.3).

Rotation semantics:

1. **One-time use.** Each refresh token is valid for exactly one exchange; the AS issues a fresh token and invalidates the old one atomically.
2. **Fixed total lifetime.** The replacement token MUST NOT extend its `exp` beyond the original token's expiry (RFC 9700 §4.14.2; BBA §6.3.2.3). An initial 8-hour window, for example, stays fixed regardless of how many rotations occur (inferred from the clock-reset prohibition).
3. **Maximum-lifetime / inactivity cap.** The AS MUST set an absolute maximum lifetime OR expire the token after a defined idle window (BBA §6.3.2.3). A token that is never used MUST NOT live forever.
4. **Replay = compromise signal.** If a rotated (already-consumed) token is replayed, the AS SHOULD revoke the entire grant family (all tokens derived from the same original authorization) (RFC 9700 §4.14.2). The correct observed result is `invalid_grant` on both the attacker's replayed token and the legitimate client's next attempt.
5. **Confidential clients.** Their refresh tokens MUST be bound to the issuing client via client authentication (RFC 9700 §2.2.2); rotation is not mandated but remains a defense-in-depth option (inferred from the BCP's focus on public clients).
6. **Session alignment.** The AS SHOULD tie refresh token lifetime to the user's authenticated session; a browser app's refresh token SHOULD NOT outlive a logout event (BBA §6.3.2.3). See [[oidc-logout]] and [[back-channel-logout]].
7. **No rotation for client credentials.** A refresh token MUST NOT be issued for the client credentials grant at all — the service re-authenticates with its own credentials (OAuth 2.1 §3.2.3 / §4.2).

Rotation is not a substitute for sender-constraining; DPoP or mTLS binding is the stronger mitigation when the client supports it (OAuth 2.1 §1.4.3; RFC 9700 §2.2.1). See [[dpop]] and [[mtls-bound-tokens]].

## Anti-pattern

| Pattern | What goes wrong |
|---|---|
| Long-lived static refresh token for a public client | Stolen token mints access tokens indefinitely; no replay detection |
| Clock reset on every rotation | "Rotating" token that effectively lives forever via continuous refresh |
| Accepting a refresh token without client auth (confidential client) | Cross-client replay; any holder can impersonate the legitimate client |
| No maximum lifetime / inactivity cap | A single theft yields permanent access |
| Ignoring replay of an already-consumed token | Attacker and legitimate client both refresh silently; breach goes undetected |

## Symptom

Concrete signals a wrong implementation produces:

- **`invalid_grant`** — the correct error code on token endpoint when a rotated (consumed) refresh token is replayed. If you see `invalid_grant` only on the *second* use of a token, rotation is working; if the first use also returns `invalid_grant`, the token was already consumed (possibly by an attacker).
- **"Token still valid after logout"** — refresh token outlives the session; user logs out but a captured refresh token keeps producing access tokens. Indicates the AS did not bind refresh-token lifetime to the session.
- **No `invalid_grant` on replay** — a consumed refresh token is accepted for a second exchange. The AS is not enforcing one-time use; incident labeled "refresh token replay."
- **Access tokens issued indefinitely from a single stolen refresh token** — no expiry or rotation enforcement; breach detected only by downstream audit, not by the AS.
- **Whole session suddenly invalidated** — expected and correct when the AS detects a replay and revokes the grant family. Legitimate clients see `invalid_grant` on their next refresh; they must redirect the user to re-authenticate (inferred: this is the correct recovery path).

## Surface (client vs backend)

**Backend / Authorization Server:**

- Enforce one-time use: atomically consume the incoming refresh token and issue a replacement.
- Enforce fixed total lifetime: compute `exp` from the *original* grant's issue time, not the current exchange time.
- Enforce maximum lifetime and / or idle expiry.
- On replay of a consumed token: revoke all tokens in the grant family; return `invalid_grant`.
- For confidential clients: require client authentication before accepting any refresh token; reject unauthenticated requests.
- Bind refresh token lifetime to the user session; expire / revoke when the session ends (see [[tokens-and-sessions]]).

**Client (SPA / browser-based / BFF):**

- Always use the latest issued refresh token; discard the previous one immediately after a successful exchange.
- Handle `invalid_grant` gracefully: treat it as a hard session termination and redirect the user to re-authenticate rather than retrying.
- Do not store refresh tokens in browser-accessible storage (localStorage / sessionStorage) — use HttpOnly cookies (BFF pattern) or in-memory only. See [[token-storage-browser]] and [[bff-token-handler]].
- For SPAs that hold the refresh token client-side, consider DPoP binding as a complement to rotation (see [[dpop]]).
- Confidential clients (BFF): authenticate at every token-endpoint call so the AS can enforce client binding.

**Limitation to be aware of (inferred from BBA §5.1.2.3 / §5.2.2.4):** rotation does not stop a determined attacker who can suppress the legitimate client from using the newest token (network isolation, clearing storage). DPoP similarly cannot protect a freshly minted access token if the attacker can bind it to their own key before the legitimate client does. Rotation raises the cost of token theft but does not eliminate it for browser clients.

## See also
- [[securing-apps-oidc-saml]] — where rotation is configured per client in RHBK

- [[tokens-and-sessions]]
- [[token-storage-browser]]
- [[bff-token-handler]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[dpop]]
- [[oidc-logout]]
- [[back-channel-logout]]
- [[rp-initiated-logout]]
- [[token-revocation]]
- [[token-introspection]]
- [[oidc-token-validation]]
- [[access-token-validation-resource-server]]
- [[pkce]]
- [[service-to-service-client-credentials]]
- [[client-authentication-methods]]
- [[oidc-grant-types]]
- [[bearer-token-usage]]
- [[fapi2-security-profile]]
- [[sso-implementation-review]]
