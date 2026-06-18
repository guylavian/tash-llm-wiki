---
title: Issuer Identification and Mix-Up Attack Defense
type: entity
domain: keycloak
slug: issuer-identification-mixup
summary: "When a client talks to more than one authorization server, it must verify that the authorization response came from the AS it actually sent the request to — failing this check exposes the flow to the OAuth 2.0 mix-up attack, where a code issued by an honest AS is redeemed at an attacker-controlled AS."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9207 (RFC 9207 AS Issuer Identification, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
provenance:
  extracted: 14
  inferred: 3
  ambiguous: 0
tags: [clients, security, failure-mode]
status: reviewed
updated: 2026-06-17
---

# Issuer Identification and Mix-Up Attack Defense

**The OAuth 2.0 mix-up attack exploits a multi-AS client that cannot tell which authorization server produced a given authorization response; the `iss` response parameter (RFC 9207) and per-issuer redirect URIs are the two recognized defenses.**

## Rule

RFC 9700 §2.1 requires a mix-up defense whenever a client communicates with more than one AS. The preferred mechanism is the `iss` parameter defined in RFC 9207.

**AS obligations (RFC 9207 §2, §2.2, §2.3):**

- The AS MUST append `iss` to every authorization response — both success and error — carrying its issuer identifier (an `https` URL, no query string, no fragment).
- The `iss` value MUST be byte-identical to the `issuer` value published in the AS discovery metadata (`/.well-known/openid-configuration` or `/.well-known/oauth-authorization-server`).
- The AS MUST advertise `authorization_response_iss_parameter_supported: true` in its metadata.

**Client obligations (RFC 9207 §2.4, RFC 9700 §2.1/§4.4.2.1):**

- On every authorization response (success or error), the client MUST extract `iss`, URL-decode it, and compare it to the issuer of the AS the request was sent to using exact string comparison (RFC 3986 §6.2.1).
- Mismatch → the client MUST reject the response and MUST NOT proceed to the token endpoint code exchange.
- If the client's config marks the AS as supporting `iss` (via the metadata flag), a response that arrives without `iss` MUST be rejected — this closes the stripping bypass.
- Each configured AS MUST have a unique issuer identifier; no two ASes may share the same `iss` value (inferred: enforcing uniqueness is a client-side configuration discipline, not something the AS can guarantee across deployments).

**Fallback (RFC 9700 §4.4.2.2):**

When RFC 9207 is not available, clients MUST use a distinct redirect URI per issuer. This approach is less flexible and should be used only when `iss` support cannot be confirmed (inferred).

**Signed equivalents (RFC 9207 §4):**

A JARM JWT response or an `id_token` in a hybrid response carries a signed `iss` claim and is an acceptable alternative. When both a bare `iss` parameter and an ID Token `iss` claim are present, they MUST be identical — a mismatch must cause rejection.

## Anti-pattern

- Multi-IdP client with no issuer check at all (RFC 9700 §2.1).
- Normalizing the `iss` URL before comparison (lowercasing, stripping trailing slashes) — the spec requires exact string comparison; normalization can defeat the check.
- Validating `iss` on success responses but trusting unauthenticated error responses without checking `iss` — an attacker can inject a fake error to redirect or confuse the flow (RFC 9207 §2.4).
- Matching `iss` against the full set of configured ASes rather than the specific AS the request was directed to — this only proves some honest AS answered, not the intended one.
- Two ASes sharing the same issuer identifier due to copy-paste template misconfiguration (RFC 9207 §4).
- Assuming `iss` is an integrity guarantee against response injection — it is unsigned; it defends only against mix-up routing, not against a tampering attacker (RFC 9207 §4).
- Single-AS clients skipping `iss` handling entirely on the assumption they'll never add a second IdP (inferred: this is a latent gap that surfaces at onboarding time).

## Symptom

- **Mix-up succeeds:** the authorization code issued by the honest AS is exchanged at the attacker's token endpoint; the attacker obtains tokens for the victim's account. No error is visible to the user.
- **`iss` stripping bypass:** an attacker removes the `iss` parameter in transit; a client that only rejects a *wrong* `iss` but not a *missing* one silently proceeds.
- **Issuer mismatch error on legitimate response:** the AS emits an `iss` URL that differs in format from its metadata `issuer` (trailing slash, `http` vs `https`, embedded query string) — spec-compliant clients reject valid responses with "issuer mismatch."
- **Fake error injection:** attacker sends an unauthenticated error response without `iss`; a client that trusts error content blindly retries or redirects on attacker-supplied data.
- **Latent exposure:** a production system running fine with one IdP adds a social-login or enterprise IdP without revisiting the authorization response handler — mix-up risk opens silently.

## Surface (client vs backend)

**Client (browser SPA / native app / confidential client front-channel):** The entire `iss` validation obligation sits here. The client must store which AS a request was sent to (keyed by state or PKCE verifier), then on callback extract and compare `iss` before calling the token endpoint. Libraries that implement RFC 9207 do this automatically; hand-rolled callback handlers must implement it explicitly.

**Backend (confidential client / BFF handling the code exchange):** If the BFF owns the authorization flow it inherits all client-side `iss` duties. A resource server validating access tokens has a separate but related obligation: validate the `iss` claim inside the JWT against the expected issuer (see [[access-token-validation-resource-server]] and [[jwt-validation-pitfalls]]). The mix-up attack specifically targets the front-channel; backend token validation is a distinct control.

## See also

- [[authorization-server-metadata-discovery]] — how the client learns the issuer identifier and the `authorization_response_iss_parameter_supported` flag
- [[state-and-nonce]] — `state` binds the session; `iss` binds the AS; both checks are needed
- [[pkce]] — PKCE provides CSRF protection but does not substitute for `iss` validation
- [[redirect-uri-validation]] — per-issuer redirect URI is the RFC 9207 fallback when `iss` is unavailable
- [[jwt-validation-pitfalls]] — `iss` validation inside JWTs at the resource server
- [[access-token-validation-resource-server]] — RS-side issuer validation
- [[oidc-token-validation]] — RHBK token validation overview
- [[oidc-client-best-practices]] — RHBK client security recommendations
- [[fapi2-security-profile]] — FAPI 2.0 mandates signed responses (JARM), an alternative to bare `iss`
- [[dpop-sender-constraining]] — complements issuer binding with token sender-constraining
- [[sso-implementation-review]] — MOC: SSO implementation review checklist
