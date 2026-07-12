---
title: Client-credentials burst load — tokens rejected as expired seconds after issuance
type: question
question_tier: conceptual
domain: keycloak
slug: client-credentials-burst-token-expired
summary: "Under burst load (thousands of parallel client_credentials token requests at cache expiry), tokens issued seconds ago are intermittently rejected by the resource server as expired — with clock skew ruled out — the likely root cause is a resource-server JWKS/introspection cache failure exacerbated by key rotation or clock skew at the RS, not a Keycloak issuance defect or a lifespan-too-short problem."
sources:
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth2 Access Tokens, fetched 2026-06-17)
  - kb:rhbk-26-4-migration-changes
  - kb:rhbk-26-4-managing-user-sessions
  - kb:rhbk-26-4-sso-protocols
  - kb:rhbk-26-4-assembly-managing-clients-server-administration-guide
provenance:
  extracted: 12
  inferred: 8
  ambiguous: 0
tags: [clients, tokens, users]
status: draft
updated: 2026-07-09
---

# Client-credentials burst load — tokens rejected as expired seconds after issuance

**You have RHBK 26 with a 5-minute access token lifespan on the client-credentials (service account) grant. When the partner's token cache expires, thousands of parallel token requests hit the token endpoint. Some tokens are rejected by the resource server (RS) as expired despite being seconds old. Clocks are NTP-synced (<1s skew).** (scenario premise)

## Quick diagnosis

This is **not** a "token-lifespan-too-short" problem (a 5-minute token seconds old cannot naturally expire across NTP-synced clocks), and **not** a Keycloak token-issuance bug (Keycloak's JWT signing is deterministic regardless of load). It is a **resource-server token-cache or validation problem** — almost certainly involving **stale JWKS key caching** combined with a realm signing-key rotation event, **or** an RS-local clock that is actually ahead of the NTP-synced baseline.

## Analysis of the three hypotheses

### 1. Token-lifespan-too-short — ruled out

- With `exp = iat + 300s` and clocks in sync (<1s NTP skew), a token issued "seconds ago" has ~298–299 s of remaining validity.
- A short lifespan does make the cache-expiry burst pattern *more frequent* but cannot cause a *just-issued* token to appear expired at the RS.
- The only way this hypothesis could fit is if the RS clock is >300s ahead of Keycloak's — which the user says they have verified against NTP. If that verification covered the RS host itself, this is definitively ruled out.

### 2. Resource-server token-cache problem — most likely

The RS has two standard validation paths:

**Path A — Local JWT validation via JWKS (offline)**
- The RS fetches the realm's JWKS URI and caches the public keys keyed by `kid`.
- If the realm signing key has been rotated and the RS's JWKS cache still holds the **old** key, tokens signed with the **new** active key have an unknown `kid`. The RS either cannot validate the signature at all, or it re-fetches the JWKS and temporarily fails under the burst.
- *Why it manifests as "expired":* Some RS libraries and API gateways have a single catch-all `invalid_token` error code and map any validation failure — including unknown `kid` — to "token expired" in their operational logs or error messages (RFC 6750 §3.1 error values: both expiry and signature failure produce `invalid_token`; downstream monitoring may label both as "expired").
- *Intermittent nature:* If the RS has multiple nodes and their JWKS caches expire at different times, or if the JWKS re-fetch races against concurrent requests under burst, some requests succeed (cache had the new key) while others fail (cache still old).
- RHBK's key model supports one **active** and several **passive** keys per realm ([[realm-keys-and-rotation]]). The JWKS endpoint publishes all keys, so a correctly functioning RS can always validate. But the RS's *cache* may not hold all keys.

**Path B — Token introspection (online via RFC 7662)**
- The RS sends each token to Keycloak's introspection endpoint and checks `active`.
- Under burst, if the RS caches introspection results with a **fixed TTL** that does not respect the individual token's `exp`, cached stale entries can produce wrong results ([[token-introspection]] anti-pattern #6: "Long-TTL caching ignoring exp").
- More critically: if the RS's introspection client has a **negative cache** (caching failed/error responses) and the introspection endpoint is briefly overloaded during the burst, valid tokens could be cached as "inactive" for the negative-cache TTL.
- The key anti-pattern from [[service-to-service-client-credentials]] applies: *"Synchronous per-request introspection at scale"* without proper caching creates a bottleneck on the authorization server.

**The JWKS stale-cache variant is the most probable root cause** because client-credentials tokens for high-throughput APIs should use local JWT validation ([[oidc-token-validation]] guidance: *"Use JWKS for high-throughput APIs with short token lifespans"*). If the RS uses JWKS validation, the chain is: key rotation → new `kid` → RS cache miss → validation failure → reported as "expired."

### 3. Keycloak token-issuance problem — ruled out (with one caveat)

- Keycloak's token endpoint is stateless for `client_credentials` (no user session created, only a transient session; see [[oidc-grant-types]] and the RHBK SSO Protocols chapter). The `exp` calculation is `System.currentTimeMillis() + (lifespan_seconds * 1000)` — a deterministic local operation with no shared-state race condition.
- Under extreme load, if Keycloak's internal clock has a transient NTP jump (step adjustment forward), a small window of tokens could receive a `exp` based on a clock that jumped forward — but the user says NTP skew is <1s, so this is unlikely.
- RHBK 26.6 also adjusted the *default clock-skew for not-before JWT token checks* from 0 to 10 seconds ([[rhbk-26-6-migration-changes]] §2.2.10). This affects `iat`/`nbf` validation at Keycloak itself (e.g., identity provider assertion validation), not the access token's `exp` claim. If the RS validates `iat` with a 0s skew and the token took >0s to arrive... but the error is "expired", not "iat in the future."

## Most likely root cause chain

```
Realm signing-key rotation (scheduled or manual)
  → New active key with new `kid`
  → RS's JWKS cache still holds only the old key
  → Burst of partner requests arrives with tokens signed by the new key
  → RS sees unknown `kid` → can't validate → reports as "expired" (invalid_token)
  → RS lazily refreshes JWKS, but under burst some requests hit stale cache
  → Intermittent failures until all RS nodes have the fresh JWKS
```

## Actionable debugging steps

1. **Decode the rejected token offline** — use `base64` to decode the JWT payload and read its `exp`, `iat`, and `kid` header. Compare `exp` against the RS's `/usr/bin/date +%s` at the time of failure. If `exp < RS_epoch`, the RS clock **is** ahead despite NTP — measure the RS host, not the Keycloak host.

2. **Check JWKS cache on the RS** — note the `kid` in the rejected token's header. Fetch the RS's current JWKS cache content (e.g., `GET <RS-discovery>/protocol/openid-connect/certs` and compare the key IDs). If the `kid` is absent from the RS's view, JWKS cache staleness is confirmed.

3. **Check realm key rotation events** — run `kcadm.sh get keys -r <REALM>` and inspect the `Active` key's `providerPriority`. If it changed recently (or if `keycloak-keys.log` in RHBK server logs shows "Generated new key pair for realm"), correlate the rotation timestamp with the first "expired token" complaint.

4. **Test the RS introspection path** — if the RS uses introspection, enable RS logging for introspection responses. Look for HTTP 200 with `active: false` responses for tokens you know are valid. This confirms an introspection-cache or clock issue.

5. **Eliminate lightweight access tokens** — verify the partner's client does **not** have the `use-lightweight-access-token` executor applied via client policies. Lightweight access tokens are rejected by the UserInfo endpoint ([[rhbk-26-4-migration-changes]] §2.1.4) and require introspection for full claims — adding a round-trip dependency.

## Recommended mitigations

- **For the RS:** set the JWKS cache refresh interval to be significantly shorter than the realm key rotation interval (or disable caching for high-security deployments). If using introspection, ensure the cache TTL respects each token's `exp` — never use a fixed TTL that exceeds the shortest valid token lifespan.
- **For the Keycloak realm:** avoid unnecessary manual key rotation. If automated key rotation is enabled (default RHBK behavior rotates the realm key periodically), lengthen the rotation interval or align it with a maintenance window.
- **For the partner:** add a safety margin to the token cache TTL (e.g., `expires_in * 0.8`) so re-fetch happens before the token actually expires, reducing the burst-at-expiry pattern. Use an async pre-fetch mechanism (cache-warming) rather than all-instances waiting until TTL=0.
- **Consider sender-constraining** ([[dpop]] / [[mtls-bound-tokens]]) to bind tokens to the partner's client key — this eliminates the "leaked token" attack motivation for very short lifespans, allowing a longer lifespan (e.g., 15 min) that reduces burst frequency ([[service-to-service-client-credentials]] / RFC 9700 §2.2).

## See also

- [[access-token-validation-resource-server]] — what the RS must verify
- [[oidc-token-validation]] — JWKS vs introspection guidance
- [[token-introspection]] — caching anti-patterns
- [[realm-keys-and-rotation]] — key rotation mechanics
- [[service-to-service-client-credentials]] — client_credentials grant best practice
- [[tokens-and-sessions]] — token lifespan configuration
- [[jwt-validation-pitfalls]] — why RS validation failures are hard to diagnose

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

| ID | Title |
|---|---|
| `kb:rhbk-26-4-sso-protocols` | Chapter 10. SSO protocols — RHBK 26.4 Server Administration Guide (client_credentials grant uses transient sessions, no refresh token, no user session created) |
| `kb:rhbk-26-4-assembly-managing-clients-server-administration-guide` | Chapter 13. Managing OIDC and SAML Clients — RHBK 26.4 Server Administration Guide (service account token issuance, `expires_in` response, key rotation mechanics) |
| `kb:rhbk-26-4-managing-user-sessions` | Chapter 6. Managing user sessions — RHBK 26.4 (transient sessions for service accounts, Client Session Max timeout) |
| `kb:rhbk-26-4-migration-changes` | Chapter 2. Migration changes — RHBK 26.4 (lightweight access tokens rejected at UserInfo endpoint) |
| `kb:rhbk-26-6-migration-changes` | Chapter 2. Release-specific changes — RHBK 26.6 Upgrading Guide (§2.2.10 Adjusted default clock-skew for not-before JWT token checks) |
| `kb:rhbk-26-4-configuring-realms` | Chapter 3. Configuring realms — RHBK 26.4 (key rotation, not-before-policy push) |
| `guide:server_administration_guide` | RHBK Server Administration Guide (token lifespan configuration) |
| `guide:securing_applications_and_services_guide` | RHBK Securing Applications and Services Guide (OIDC flow reference) |

### Wiki pages

| Page | Key claim |
|---|---|
| [[access-token-validation-resource-server]] | RS must validate `exp` with minimal clock-skew leeway; symptom: expired token still works if leeway too wide |
| [[token-introspection]] | Anti-pattern #6: long-TTL caching ignoring `exp` — revoked-but-cached access window |
| [[service-to-service-client-credentials]] | Anti-pattern #5: synchronous per-request introspection at scale — prefer local JWT validation with cached JWKS |
| [[oidc-token-validation]] | Use JWKS for high-throughput APIs with short token lifespans |
| [[realm-keys-and-rotation]] | Active vs passive keys; new active key after rotation has a new `kid`; RS must re-fetch JWKS |
| [[tokens-and-sessions]] | Access token lifespan controlled at realm/client level |
| [[jwt-validation-pitfalls]] | Unknown `kid` reported as `invalid_token`; stale JWKS cache causes intermittent failures |
| [[rhbk-26-6-migration-changes]] | RHBK 26.6 §2.2.10: clock-skew for `iat`/`nbf` checks changed from 0 to 10 seconds |

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-server_administration_guide|keycloak reference — server_administration_guide]]
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
- [[rhbk-26-4-migration-changes|Chapter 2. Release-specific changes]]
- [[rhbk-26-4-managing-user-sessions|Chapter 6. Managing user sessions]]
- [[rhbk-26-4-sso-protocols|Chapter 10. SSO protocols]]
- [[rhbk-26-4-assembly-managing-clients-server-administration-guide|Chapter 13. Managing OpenID Connect and SAML Clients]]
<!-- crosslink:end -->
