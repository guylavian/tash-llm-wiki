---
title: Audience and Scope Checks
type: entity
domain: keycloak
slug: audience-and-scope-checks
summary: "A resource server must reject any access token whose `aud` claim does not identify that server, and must enforce the scope/role claims before granting access to each operation; skipping either check enables token substitution, confused-deputy, and over-privilege attacks."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth 2.0 Access Tokens, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://owasp.org/API-Security/editions/2023/en/0x11-t10/ (OWASP API Security Top 10 2023, fetched 2026-06-17)
provenance_extracted: 14
provenance_inferred: 4
provenance_ambiguous: 0
tags: [tokens, security, concept]
symptoms:
  - "invalid_token"
status: reviewed
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# Audience and Scope Checks

**A resource server (RS) must verify that every incoming access token was issued for it (`aud`) and that the token's granted privileges (`scope`/roles) are sufficient for the requested operation before processing the call.**

## Rule

**Audience (`aud`) validation — RFC 9068 §4 / RFC 9700 §4.10.2**

The RS must check that the `aud` claim contains a resource indicator that identifies this RS. If `aud` does not include the RS, the token must be rejected regardless of any other valid claims.

The authorization server (AS) sets `aud` from the `resource` parameter (RFC 8707) when present; otherwise it uses a default resource indicator that may be inferred from scope (RFC 9068 §3). The AS must not issue a token whose scope-to-resource mapping is ambiguous — e.g. a single token with many audiences and a flat scope set leaves the RS unable to determine which scopes apply to it (RFC 9068 §3).

**Scope / role enforcement — RFC 9068 §4 / RFC 9700 §2.3**

After validating `aud`, the RS should use the token's `scope`, `roles`, `groups`, or `entitlements` claims together with its own context to allow or deny the call. Possession of a valid, correctly-addressed token alone is not authorization.

Access tokens should follow least-privilege: scopes should be restricted to the minimum needed for the targeted resource. RFC 9700 §2.3 additionally permits `authorization_details` (RFC 9396) to narrow privileges further.

**Audience distinctness — RFC 9068 §5 / RFC 8725 §2.8**

The AS must use a distinct `aud` identifier per resource. Tokens for different APIs from the same issuer must not be interchangeable (inferred from §5 requirement to prevent cross-JWT confusion).

**Per-object and per-function checks — OWASP API1/API5 2023**

Beyond token-level checks, every function that accesses a named record must verify the authenticated subject is permitted for that specific object (BOLA). Every privileged operation must re-check the caller's role or scope regardless of HTTP method or URL structure (BFLA). These checks complement the token-level `aud`/`scope` rules (inferred: OWASP supplies the attack framing; RFC 9068/9700 supply the normative `aud`/`scope` MUSTs).

**Claim naming conventions — RFC 9068 §2.2.3.1**

For non-delegation authorization attributes the AS should use the SCIM claim names: `roles`, `groups`, `entitlements` (RFC 7643 §4.1.2). Inventing ad-hoc claim names per service creates drift between AS and RS.

## Anti-pattern

- **No `aud` check at all.** The RS accepts any token signed by the trusted AS, regardless of which API it was issued for. This is the most common real-world gap (inferred from RFC 9068 §4 and RFC 9700 §4.10.2 both making this a normative requirement).
- **Wildcard or shared audience.** A single generic audience string covers all APIs, so tokens are freely replayable across the entire estate.
- **Authorizing on authentication alone.** A valid, correctly-addressed token grants full access; scope, roles, and entitlements are not checked. Any endpoint is reachable by any valid token.
- **Overly broad scope.** A single token is issued for all resource servers with a flat scope set; the RS accepts it because it sees its own audience, but also honors scopes that should not apply to it.
- **Per-controller ad-hoc checks.** Role/scope enforcement is scattered across endpoints, relying on developers to remember to add it rather than a centralized, consistently-invoked module (OWASP API5 2023).
- **Client-supplied object ID as identity.** The RS trusts a `user_id`/`account_id` in the path or body to decide what to authorize instead of deriving identity from the validated token subject (inferred from OWASP API1 2023 guidance to derive identity from the token).

## Symptom

- A token minted for API-A is sent to API-B and returns `200 OK` — token substitution / confused-deputy. Ideally `401 invalid_token` per RFC 6750 §3.1.
- A pen-test finding: "scope X for service Y authorizes service Z silently" — scope/audience over-broad.
- Any valid token reaches any endpoint regardless of granted scope — missing fine-grained authorization.
- Horizontal privilege escalation: authenticated user A retrieves user B's records by changing an ID in the URL (BOLA).
- Vertical privilege escalation: regular user successfully calls an admin endpoint because the role check was not applied (BFLA).
- Claim-name drift between AS and RS causes authz decisions to silently fall through to a default-allow.
- On a tightened deployment: `WWW-Authenticate: Bearer error="invalid_token"` on all cross-audience replays.

## Surface (client vs backend)

**Backend / resource server — primary responsibility.**

The RS is responsible for all checks described above: `aud` validation, `scope`/role enforcement before each operation, per-object authorization, and per-function role checks. These are server-side validations that cannot be delegated to the client.

**Authorization server.**

The AS must cooperate by issuing tokens with a distinct, specific `aud` per resource, applying least-privilege scope, and not creating ambiguous multi-audience tokens. RFC 8707 `resource` parameter support enables precise audience targeting.

**Client (SPA / native app) — indirect role.**

The client selects which resource and scopes to request. Using RFC 8707 `resource` parameters and narrow scopes at request time reduces the blast radius of a leaked token. The client itself does not perform `aud` enforcement — that is exclusively a backend concern.

## See also

- [[oidc-token-validation]]
- [[access-token-validation-resource-server]]
- [[jwt-validation-pitfalls]]
- [[bearer-token-usage]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[token-introspection]]
- [[token-revocation]]
- [[service-to-service-client-credentials]]
- [[fapi2-security-profile]]
- [[fapi-oauth21-profiles]]
- [[tokens-and-sessions]]
- [[oidc-grant-types]]
- [[sso-implementation-review]]
