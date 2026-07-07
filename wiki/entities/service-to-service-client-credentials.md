---
title: Service-to-Service Client Credentials
type: entity
domain: keycloak
slug: service-to-service-client-credentials
summary: "The OAuth 2.0 Client Credentials grant (grant_type=client_credentials) is the correct mechanism for machine-to-machine authentication where no resource-owner is present; the client authenticates as itself using strong credentials and receives a short-lived access token with no refresh token."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc6749 (RFC 6749 OAuth 2.0 core + RFC 6750 Bearer usage, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
  - web:https://www.keycloak.org/docs/latest/securing_apps/index.html (Keycloak securing-apps upstream OSS, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [clients, tokens, security, profile]
symptoms:
  - "invalid_client"
status: reviewed
updated: 2026-07-02
---

# Service-to-Service Client Credentials

**The `client_credentials` grant issues an access token to a confidential client acting on its own behalf, with no user context, no refresh token, and mandatory client authentication at the token endpoint.**

## Rule

**Grant scope.** Use `grant_type=client_credentials` when a service needs access to resources under its own control and no resource-owner interaction is possible (RFC 6749 §1.3.4, §4.4; OAuth 2.1 §1.3.3, §4.2). This grant has no public-client variant — the client must be confidential.

**Client authentication is mandatory.** The client MUST authenticate at the token endpoint on every request (RFC 6749 §3.2.1, §4.4.2; OAuth 2.1 §3.2.1). Accepted methods:
- `client_secret_basic` — HTTP Basic with `client_id:secret` in the `Authorization` header. Servers MUST support this; prefer it over body-based secret. Sending the secret in the request body (`client_secret_post`) SHOULD be limited to clients that cannot use Basic (RFC 6749 §2.3.1).
- `private_key_jwt` — client signs a JWT assertion with its private key (RFC 7523); register the public key via a JWKS URL so keys rotate without reconfiguration (inferred from keycloak-securing-apps + RFC 7523).
- mTLS (RFC 8705) — mutual TLS; server requires explicit truststore configuration.

RFC 9700 §2.5 and OAuth 2.1 §7.3 recommend asymmetric methods (`private_key_jwt`, mTLS) over shared secrets to contain fleet-wide compromise from a single leak.

**Token response shape.** Success returns `access_token`, `token_type`, `expires_in` (optional), and `scope` (optional) (RFC 6749 §5.1). No `id_token`, no `refresh_token` — the authorization server MUST NOT issue a refresh token for this grant (RFC 6749 §4.4.3; OAuth 2.1 §4.2).

**Token lifetime and scope.** Issue short-lived access tokens (RFC 6750 §5.3 guidance of ≤1 h). Scope the token to the minimum required for the target resource server; audience-restrict with `aud` per RFC 9700 §2.3 and audience-and-scope-checks. (inferred: combining lifetime + scope minimisation best practices across RFC 6750, RFC 9700, and OAuth 2.1.)

**TLS required everywhere.** The token endpoint MUST enforce TLS; the client MUST validate the cert chain (RFC 6749 §2.3.1, §3.2; OAuth 2.1 §1.5). Bearer tokens sent to resource servers also require TLS end-to-end (RFC 6750 §5.2).

**Token delivery.** Send the access token in the `Authorization: Bearer <token>` header (RFC 6750 §2.1; OAuth 2.1 §5.1.1). Do not embed it in a URI query string (RFC 6750 §2.3 / RFC 9700 §4.3.2).

**Re-request, don't refresh.** When the access token expires, the client re-authenticates and requests a fresh token using its own credentials — exactly as it did the first time (inferred from RFC 6749 §4.4.3 "no refresh token" rule).

**Sender-constraining (SHOULD).** RFC 9700 §2.2.1 and OAuth 2.1 §1.4.3 recommend binding access tokens to the client's key material via DPoP (RFC 9449) or mTLS (RFC 8705) so a stolen bearer token cannot be replayed from another host. See [[dpop]] and [[mtls-bound-tokens]].

**Keycloak-specific.** Enable via `Client authentication = On` + `Service accounts roles` on the client configuration. Apply the `oauth-2-1-for-confidential-client` global client profile via Client Policies to enforce the full OAuth 2.1 confidential-client posture.

## Anti-pattern

1. **Public or user-flow credentials for machine-to-machine.** Using ROPC ("service user" with a password), a shared interactive user account, or a public client to authenticate a backend service. ROPC is removed in OAuth 2.1 and blocked by RFC 9700 §2.4.
2. **Weak or static shared secret.** A `client_secret` committed to VCS, shared across multiple services, or never rotated. If one service's environment is compromised the entire fleet is exposed.
3. **Expecting a refresh token.** Client code that stores or tries to use a `refresh_token` from a `client_credentials` response — one will not be issued.
4. **No `aud` / no scope minimization.** A broad-scoped token accepted by every resource server, amplifying the blast radius of a single token leak. (inferred from RFC 9700 §2.3 scope/audience guidance applied to the machine-client context.)
5. **Synchronous per-request introspection at scale.** Calling the introspection endpoint on every inbound request without caching creates a bottleneck on the authorization server; prefer local JWT validation with cached JWKS lookup by `kid`.

## Symptom

| Wrong implementation | Observable fault |
|---|---|
| No client secret / unauthenticated call to token endpoint | `invalid_client` (HTTP 401) — "client authentication failed" |
| Expecting a refresh token | `refresh_token` absent in response → NullPointerException / failed refresh loop |
| Leaked shared secret used by attacker | Attacker mints valid tokens indistinguishable from legitimate service calls; full service impersonation |
| Token sent over HTTP or TLS cert not validated | Token captured on the wire; MITM / DNS-hijack replay |
| Token in URI query string | Token visible in server access logs, browser history, `Referer` header — "token stolen from logs" incident |
| No `aud` validation on resource server | Bearer token issued for Service-A replayed against Service-B and accepted (confused-deputy / privilege crossing) |
| Over-broad scope on service token | A single leaked token grants access to all resource servers; scope-creep audit finding |
| Static JWKS cert never rotated | "Unable to verify signature" / unknown `kid` error after key rotation |
| mTLS not configured server-side | SSL handshake failure; cert presented but untrusted → 401 |

## Surface (client vs backend)

**This concept applies to the backend (service) side only.** There is no browser/SPA surface — `client_credentials` is a confidential-client-only flow with no user interaction.

The **calling service (confidential client)** must:
- Authenticate to the token endpoint on every token acquisition (no caching a refresh token).
- Use `client_secret_basic`, `private_key_jwt`, or mTLS — never expose the secret in source control or logs.
- Cache the access token and re-request on expiry; monitor `expires_in`.
- Send the token as `Authorization: Bearer <token>` over TLS to the resource server.
- Include a DPoP proof on every request if the token is DPoP-bound.

The **resource server (backend receiving the call)** must:
- Validate the access token: issuer, expiry, signature — via local JWT + cached JWKS, or introspection (confidential clients only).
- Enforce `aud`: reject tokens not explicitly addressed to this resource server.
- Enforce `scope`/`authorization_details`: return `insufficient_scope` (403) for missing scope, not a bare 403.
- Return `WWW-Authenticate: Bearer` with `error`, `error_description` on failure, and map errors correctly: `invalid_token` → 401; `insufficient_scope` → 403.

See [[access-token-validation-resource-server]], [[audience-and-scope-checks]], [[token-introspection]].

## See also

- [[client-authentication-methods]]
- [[oidc-grant-types]]
- [[tokens-and-sessions]]
- [[audience-and-scope-checks]]
- [[access-token-validation-resource-server]]
- [[token-introspection]]
- [[token-revocation]]
- [[dpop]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[bearer-token-usage]]
- [[jwt-validation-pitfalls]]
- [[token-exchange]]
- [[fapi2-security-profile]]
- [[fapi-oauth21-profiles]]
- [[oidc-token-validation]]
- [[securing-apps-oidc-saml]]
- [[sso-implementation-review]]
