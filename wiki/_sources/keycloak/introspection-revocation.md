---
source: RFC 7662 (Introspection) + RFC 7009 (Revocation)
url: https://www.rfc-editor.org/rfc/rfc7662
fetched: 2026-06-17
status: RFC 7662 + RFC 7009
feeds: [token-introspection, token-revocation, access-token-validation-resource-server]
---

# Token introspection + revocation — load-bearing rules (paraphrased)

Two specs distilled: RFC 7662 (OAuth 2.0 Token Introspection) and RFC 7009 (OAuth 2.0 Token Revocation). Section numbers cited inline.

## token-introspection

- **RULE (7662 §2.1):** Introspection request is `HTTP POST` with `application/x-www-form-urlencoded` body; `token` REQUIRED, `token_type_hint` OPTIONAL.
  - **ANTI-PATTERN:** Calling introspection over GET / query string, or sending JSON body.
  - **SYMPTOM:** Endpoint returns 400/415 or silently treats no token as present; "invalid request" errors, token never resolved.

- **RULE (7662 §2.1 / §4):** The introspection endpoint MUST require authorization (client auth or its own bearer token); servers SHOULD require the protected resource to be specifically authorized to call it — guards against token-scanning / fishing.
  - **ANTI-PATTERN:** Open/unauthenticated introspection endpoint; any party can submit arbitrary tokens to probe validity.
  - **SYMPTOM:** Token-scanning attack; attacker enumerates token states; audit shows introspection hits with no caller credential.

- **RULE (7662 §2.2):** `active` boolean is the REQUIRED field; `true` means issued by this AS, not revoked, and within its validity window. Inactive => `{"active": false}` and SHOULD NOT leak any other claims.
  - **ANTI-PATTERN:** Resource server trusts other claims (scope/sub/exp) without first checking `active`; or AS returns claims for an inactive token.
  - **SYMPTOM:** Expired/revoked token still accepted because RS read `exp`/`scope` and skipped `active`; info leak on dead tokens.

- **RULE (7662 §2.2):** OPTIONAL claims the response MAY carry: `scope`, `client_id`, `username`, `token_type`, `exp`, `iat`, `nbf`, `sub`, `aud`, `iss`, `jti`.
  - **ANTI-PATTERN:** RS assumes a given optional claim (e.g. `aud` or `scope`) is always present and hard-fails when absent.
  - **SYMPTOM:** NPE / "missing claim" failures against a spec-compliant AS that omits optional fields.

- **RULE (7662 §2.3):** Bad caller credentials => HTTP 401. A well-formed query for an inactive/unknown token is NOT an error — it returns `200` with `active:false`.
  - **ANTI-PATTERN:** Treating "token not found" as a 4xx error path; or treating a 401 (caller auth failure) as "token invalid".
  - **SYMPTOM:** RS rejects valid users when its own introspection credential is wrong (mislabeled as "invalid token"); or crashes parsing a non-JSON 401.

## access-token-validation-resource-server

- **RULE (7662 §4):** AS MUST perform ALL applicable token-state checks: expiry, not-before/valid start, revocation status, signature (if signed), and any RS-specific usage restrictions.
  - **ANTI-PATTERN:** RS skips local checks because "introspection said active"; or AS only checks expiry and ignores revocation.
  - **SYMPTOM:** Revoked-but-unexpired token keeps working; tickets like "logged-out user still has API access."

- **RULE (7662 §4):** AS MUST support TLS 1.2; the calling RS MUST validate the server certificate.
  - **ANTI-PATTERN:** Plaintext / cert-validation-disabled introspection calls.
  - **SYMPTOM:** MITM can forge `active:true` responses; tokens validated against a spoofed endpoint.

- **RULE (7662 §4):** Cached introspection responses MUST NOT outlive the token's `exp`; aggressive caching widens the window where a revoked token still passes.
  - **ANTI-PATTERN:** RS caches `active:true` for a fixed long TTL ignoring `exp`, to cut latency.
  - **SYMPTOM:** Revoked/expired token accepted for the cache window; "revocation doesn't take effect immediately" complaints.

## token-revocation

- **RULE (7009 §2):** Revocation endpoint URLs MUST be HTTPS and the AS MUST use TLS; an HTTP variant MUST NOT be published as the revocation endpoint.
  - **ANTI-PATTERN:** Advertising/using an http:// revocation URL.
  - **SYMPTOM:** Revocation request observable/tamperable on the wire; attacker strips the revocation.

- **RULE (7009 §2.1):** Request is `HTTP POST`; `token` REQUIRED, `token_type_hint` OPTIONAL (`access_token` | `refresh_token`); client includes its auth credentials and AS verifies the token was issued to that client. AS MUST search all token types if the hint misses.
  - **ANTI-PATTERN:** Letting any authenticated client revoke another client's token; or hard-failing when the hint is wrong instead of widening the search.
  - **SYMPTOM:** Cross-client token revocation (DoS); "wrong hint => token not revoked" bug.

- **RULE (7009 §2.1):** Implementations MUST support refresh-token revocation; revoking a refresh token SHOULD also invalidate access tokens from the same grant; revoking an access token MAY also revoke the related refresh token. Invalidation is immediate.
  - **ANTI-PATTERN:** Revoking the refresh token but leaving derived access tokens live.
  - **SYMPTOM:** After logout/revoke, existing access tokens keep working until natural expiry.

- **RULE (7009 §2.2):** Server returns HTTP 200 whether the token was revoked OR was invalid; response body is ignored — clients can't probe token validity. `503` => still exists, retry later.
  - **ANTI-PATTERN:** Returning 404/400 for unknown tokens, or differentiating valid vs invalid in the response.
  - **SYMPTOM:** Token-existence oracle; client logic that branches on revocation status breaks (spec says ignore body).

- **RULE (7009 §2.2.1):** Error `unsupported_token_type` when the AS won't revoke that token type. An unrecognized `token_type_hint` is ignored, not fatal.
  - **ANTI-PATTERN:** Returning a generic 500 for an unsupported type; or rejecting the request on an unknown hint.
  - **SYMPTOM:** Clients can't tell revocation is unsupported (just see opaque error); spurious failures on benign hints.

- **RULE (7009 §5 / §2.3):** Apply DoS countermeasures (rate limiting) to the endpoint; clients MUST authenticate the endpoint (cert validation) and get its location from a trustworthy source. CORS/JSONP MAY be offered but JSONP risks code injection. Note: if AS doesn't support access-token revocation, access tokens are NOT immediately invalidated — account for this in risk analysis.
  - **ANTI-PATTERN:** Unthrottled revocation endpoint; JSONP enabled without weighing injection risk; assuming access tokens die instantly when only refresh-token revocation exists.
  - **SYMPTOM:** Revocation-flood DoS; XSS via JSONP callback; "revoked access token still valid for token lifetime" surprise.
