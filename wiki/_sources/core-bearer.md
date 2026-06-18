---
source: RFC 6749 (OAuth 2.0 core) + RFC 6750 (Bearer usage)
url: https://www.rfc-editor.org/rfc/rfc6749
fetched: 2026-06-17
status: RFC 6749 + RFC 6750
feeds: [bearer-token-usage, service-to-service-client-credentials, access-token-validation-resource-server]
---

# RFC 6749 (OAuth 2.0 core) + RFC 6750 (Bearer usage) — load-bearing rules

Tightly paraphrased normative requirements (MUST / SHOULD / MUST NOT). Each bullet: RULE (+ section) / ANTI-PATTERN / SYMPTOM.

## bearer-token-usage

- **Prefer Authorization header `Bearer` scheme** (RFC 6750 §2.1). RULE: clients SHOULD send the token as `Authorization: Bearer <token>`; resource servers MUST support this method. ANTI-PATTERN: sending the token a different way by default. SYMPTOM: 401 if server only honors the header method.

- **Never put the token in the URI query string** (RFC 6750 §2.3, §5.3). RULE: query-param method SHOULD NOT be used; only as a last resort, and then send `Cache-Control: no-store` (req) / `private` (2xx resp). Tokens MUST NOT be passed in page URLs. ANTI-PATTERN: `?access_token=...` for convenience / browser GET. SYMPTOM: token leaks into access logs, browser history, proxy logs, and the `Referer` header — replay / "token stolen from logs" incident.

- **Form-encoded body param is tightly conditioned** (RFC 6750 §2.2). RULE: clients MUST NOT use the body param unless `Content-Type: application/x-www-form-urlencoded`, single-part ASCII body, and an HTTP method with body semantics (not GET). ANTI-PATTERN: stuffing `access_token=` into a GET or a JSON/multipart body. SYMPTOM: token ignored / 401, intermittent across methods.

- **TLS is mandatory when transmitting tokens** (RFC 6750 §5.2). RULE: clients MUST use https and MUST validate the cert chain; servers MUST implement TLS. ANTI-PATTERN: plaintext HTTP to a resource server or disabled cert validation. SYMPTOM: token captured on the wire / MITM, DNS-hijack token theft.

- **Bearer = possession is authorization** (RFC 6750 §1, §5.2). RULE: any party holding the token can use it; protect confidentiality end-to-end, do not store in cleartext cookies, use audience + short scope. ANTI-PATTERN: treating the bearer token as a low-sensitivity string; logging it. SYMPTOM: replay from a leaked token, no way to distinguish legit holder.

- **Short token lifetime to limit leak blast radius** (RFC 6750 §5.3). RULE: issue short-lived access tokens (guidance ~<=1h), especially for browser clients. ANTI-PATTERN: long-lived/never-expiring access tokens. SYMPTOM: a single leaked token grants long-term access; revocation lag.

## service-to-service-client-credentials

- **Client Credentials grant is for the client's own resources** (RFC 6749 §1.3.4, §4.4). RULE: use `grant_type=client_credentials` for machine-to-machine where access is scoped to resources under the client's control (no resource-owner present). ANTI-PATTERN: using a user-flow (password/auth-code) or a shared "service user" for app-to-app calls. SYMPTOM: phantom interactive sessions, no user context, brittle service auth.

- **Client MUST authenticate at the token endpoint** (RFC 6749 §3.2.1, §4.4.2). RULE: confidential clients (and any client issued credentials) MUST authenticate when requesting a token. ANTI-PATTERN: calling the token endpoint with only `client_id`, no secret/credential. SYMPTOM: `invalid_client` (HTTP 401) / "client authentication failed".

- **Prefer HTTP Basic for client auth; body params are NOT RECOMMENDED** (RFC 6749 §2.3.1). RULE: server MUST support `client_secret_basic` (id:secret in Basic header); `client_secret_post` (id+secret in body) SHOULD be limited to clients that cannot use Basic. ANTI-PATTERN: defaulting to secret-in-body. SYMPTOM: secret more likely to appear in logs; some servers reject body-auth → `invalid_client`.

- **No refresh token in client-credentials** (RFC 6749 §4.4.3). RULE: the authorization server MUST NOT issue a refresh token for this grant. ANTI-PATTERN: client code expecting/storing a refresh_token from a client-credentials response. SYMPTOM: `refresh_token` is null/absent → NPE / failed refresh; just re-request a new token instead.

- **TLS required at the token endpoint** (RFC 6749 §2.3.1, §3.2). RULE: the authorization server MUST require TLS when credentials are sent (token endpoint). ANTI-PATTERN: plaintext token endpoint or skipping TLS verification. SYMPTOM: client secret captured on the wire; client impersonation (§10.1).

- **Token response shape** (RFC 6749 §5.1). RULE: success returns `access_token`, `token_type`, optional `expires_in`, optional `scope`. ANTI-PATTERN: assuming an `id_token` or refresh_token comes back. SYMPTOM: missing-field errors in the client.

## access-token-validation-resource-server

- **Challenge with `WWW-Authenticate: Bearer` on auth failure** (RFC 6750 §3). RULE: on missing/invalid token the resource server MUST return a `WWW-Authenticate` header with auth-scheme `Bearer`; may carry `realm`, `scope`, `error`, `error_description`, `error_uri` (each at most once). ANTI-PATTERN: returning a bare 401/403 with no challenge. SYMPTOM: clients can't discover why/what scope is needed; opaque failures.

- **Correct error code → HTTP status mapping** (RFC 6750 §3.1). RULE: `invalid_request` → 400; `invalid_token` (expired/revoked/malformed) → 401 (client MAY retry with a fresh token); `insufficient_scope` → 403 (MAY include required `scope`). If the request carried no auth at all, omit the error code. ANTI-PATTERN: returning 500, or 401 for a scope problem, or 403 for an expired token. SYMPTOM: clients fail to auto-refresh on expiry (wrong status), or loop retrying a scope they'll never get.

- **Validate scope before granting access** (RFC 6749 §3.3; RFC 6750 §3, §3.1). RULE: scope is space-delimited, case-sensitive strings; resource server enforces required scope and returns `insufficient_scope` (403) if the token lacks it. ANTI-PATTERN: ignoring scope / authorizing on mere token validity. SYMPTOM: over-privileged access, or 403 surprises when scope names mismatch (case/typo).

- **Validate audience — reject tokens meant for another RS** (RFC 6750 §3, §5.2). RULE: token SHOULD carry intended recipient(s) (audience); resource server should reject tokens not addressed to it (token-redirect threat). ANTI-PATTERN: accepting any signature-valid token regardless of `aud`. SYMPTOM: a token issued for RS-A is replayed against RS-B and accepted (privilege crossing).

- **Enforce token integrity / signature & expiry** (RFC 6750 §5.2, §5.3; RFC 6749 §1.4). RULE: protect tokens against modification (signature/MAC) and check expiry/revocation; access token may be opaque (look up) or self-contained (verify). ANTI-PATTERN: trusting an unverified self-contained token, skipping `exp`. SYMPTOM: forged/expired token accepted → bypass.

- **Resource server MUST support the header method** (RFC 6750 §2.1). RULE: accept `Authorization: Bearer`; body/query methods are optional (MAY). ANTI-PATTERN: only parsing a query param. SYMPTOM: well-behaved header-using clients get 401.
