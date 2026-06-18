---
title: RP-Initiated Logout
type: entity
domain: keycloak
slug: rp-initiated-logout
summary: "RP-Initiated Logout is the OIDC flow where the client redirects the user agent to the OP's end_session_endpoint to terminate the session; several validation rules around id_token_hint, post_logout_redirect_uri, and state make it a common source of open-redirect and DoS vulnerabilities."
sources:
  - web:https://openid.net/specs/openid-connect-rpinitiated-1_0.html (OIDF RP-Initiated Logout 1.0, fetched 2026-06-17)
provenance:
  extracted: 9
  inferred: 3
  ambiguous: 0
tags: [security, endpoint]
status: reviewed
updated: 2026-06-17
---

# RP-Initiated Logout

**The OIDC mechanism by which a Relying Party redirects the user agent to the OP's `end_session_endpoint` to request session termination, with optional hints and a post-logout redirect.**

## Rule

**Discovery (RPIL §2.1).** The OP MUST publish `end_session_endpoint` in its discovery metadata. RPs MUST read that value rather than hardcode a path. See [[authorization-server-metadata-discovery]] for how discovery works.

**`id_token_hint` (RPIL §2, §6).** Including the ID Token as `id_token_hint` is RECOMMENDED. If the hint is absent or belongs to a different OP session, the OP MUST prompt the user to confirm before logging out. This is the primary defence against forced-logout DoS.

**`client_id` cross-check (RPIL §2).** When a RP sends both `client_id` and `id_token_hint`, the OP MUST verify that `client_id` matches the `aud` of the supplied ID Token (inferred: without this check, a different RP could submit a valid token to trigger logout under the wrong client context).

**`post_logout_redirect_uri` (RPIL §2, §3).** The redirect URI MUST have been pre-registered. The OP MUST perform an exact-string match — no prefix, substring, or wildcard matching. On any failed validation the OP MUST abort without redirecting (RPIL §3, §4).

**HTTP method support (RPIL §2).** The `end_session_endpoint` MUST accept both GET (query-string parameters) and POST (form-encoded body).

**`state` round-trip (RPIL §2).** If the RP includes a `state` parameter, the OP MUST echo it back unchanged on the post-logout redirect so the RP can correlate the callback. `ui_locales` is advisory; an unsupported locale SHOULD NOT cause an error.

**Idempotency (RPIL §4).** Requesting logout when the user is already logged out is not an error; the flow MUST succeed silently.

**Front-channel complement (FCL §2, §4.1).** The OP may render the RP's `frontchannel_logout_uri` in an iframe as part of the flow, but iframe-based logout is unreliable when browsers block third-party content. [[back-channel-logout]] is the durable complement for server-side session invalidation (inferred: the two mechanisms should be used together for resilience).

## Anti-pattern

- Hardcoding a guessed logout path instead of reading `end_session_endpoint` from discovery.
- Accepting a logout request without `id_token_hint` and silently terminating the session (skips the required user-confirmation step, enabling forced-logout DoS).
- Accepting `post_logout_redirect_uri` with prefix or wildcard matching rather than exact-string comparison.
- Redirecting to the caller-supplied URI even when validation fails.
- Implementing GET-only logout — POST requests then return 405.
- Returning an error when the user is already logged out (breaks idempotency).
- Trusting `client_id` without checking it against the `aud` of `id_token_hint` (inferred: opens a cross-client logout confusion vector).

## Symptom

| Mis-implementation | Observable fault |
|---|---|
| Hardcoded logout path | 404 on logout; "end session endpoint not found" |
| No `id_token_hint` + no confirmation prompt | Attacker link logs victim out (forced-logout DoS) |
| Wildcard `post_logout_redirect_uri` match | Open redirect after logout; user lands on phishing page |
| Redirect on failed validation | User bounced to attacker URI even though logout "failed" |
| GET-only endpoint | POST logout returns 405; BFF/SPA integration breaks |
| Dropping `state` | RP cannot correlate logout callback; CSRF / return-path confusion |
| Error on already-logged-out | Spurious error on double-click / repeat logout |

## Surface (client vs backend)

**Browser / SPA client.** Initiates logout by redirecting `window.location` to `end_session_endpoint` (GET) or by submitting a form (POST). Must supply `id_token_hint` (the stored ID Token) and, if a post-logout destination is needed, a pre-registered `post_logout_redirect_uri`. Should include a `state` value for CSRF protection on the return leg. See [[token-storage-browser]] for where the ID Token is kept prior to this call.

**Confidential client / BFF / backend.** A backend initiating logout on behalf of the user (BFF pattern) MUST POST to `end_session_endpoint` with form-encoded parameters including the `id_token_hint`. The backend must not skip `id_token_hint` — without it the OP will prompt the user, defeating silent server-side logout. After the OP redirects back, the BFF clears its own session cookie. The BFF should also trigger [[back-channel-logout]] handling if the OP supports it (inferred: RP-initiated and back-channel logout are complementary, not alternatives).

**Resource server.** Not involved in the logout redirect flow itself. However, it must not cache access tokens indefinitely — short-lived tokens and [[token-introspection]] or [[access-token-validation-resource-server]] checks are the only way the RS will honour the logout without being told explicitly.

## See also

- [[oidc-logout]] — Keycloak/RHBK-specific logout configuration and endpoint details
- [[back-channel-logout]] — server-to-server session invalidation that complements this flow
- [[token-storage-browser]] — where the ID Token (needed as `id_token_hint`) is stored
- [[authorization-server-metadata-discovery]] — how to read `end_session_endpoint` from discovery
- [[redirect-uri-validation]] — general exact-match rules that apply to `post_logout_redirect_uri`
- [[state-and-nonce]] — `state` round-trip pattern reused here for logout callback correlation
- [[tokens-and-sessions]] — session model that logout must invalidate
- [[token-revocation]] — parallel channel to invalidate refresh tokens on logout
- [[bff-token-handler]] — BFF pattern that owns the logout initiation on behalf of the SPA
- [[oidc-endpoints]] — full OP endpoint catalogue
- [[securing-apps-oidc-saml]] — RHBK client adapter logout integration
- [[sso-implementation-review]] — MOC: evaluating an SSO implementation end to end
