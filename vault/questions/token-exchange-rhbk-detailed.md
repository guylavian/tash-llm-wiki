---
title: Token Exchange V2 in RHBK — impersonation vs delegation, audience/scope semantics, DPoP/revocation pitfalls, and V1 legacy
type: question
question_tier: conceptual
domain: keycloak
slug: token-exchange-rhbk-detailed
summary: "Deep dive into RHBK 26.2+ Standard Token Exchange V2: why it implements impersonation (not delegation), how audience and scope combine from the requester-client's perspective (the #1 trap), four operational pitfalls (DPoP-bound subject_token, revocation chain, multi-site token lifespan, public client ban), and which use cases still require legacy V1 + FGAP:v1."
sources:
  - ref:wiki/reference/keycloak/rhbk-26-2-token-exchange.md
  - ref:wiki/reference/keycloak/rhbk-26-6-token-exchange.md
  - ref:wiki/reference/keycloak/rhbk-26-6-dpop.md
  - ref:wiki/reference/keycloak/rhbk-26-0-token-exchange.md
  - ref:wiki/reference/keycloak/rhbk-26-2-migration-changes.md
  - ref:wiki/reference/keycloak/rhbk-26-4-token-exchange.md
  - ref:wiki/reference/keycloak/rhbk-26-4-features.md
  - ref:wiki/reference/keycloak/rhbk-26-6-deprecated.md
  - ref:references/securing-apps-oidc-saml.md
  - web:https://www.rfc-editor.org/rfc/rfc8693 (RFC 8693 — OAuth 2.0 Token Exchange, fetched 2026-06-18)
  - web:https://www.rfc-editor.org/rfc/rfc9449 (RFC 9449 — OAuth 2.0 DPoP, fetched 2026-06-18)
  - web:https://www.rfc-editor.org/rfc/rfc7009 (RFC 7009 — OAuth 2.0 Token Revocation, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 5
provenance_ambiguous: 0
tags: [tokens]
status: reviewed
updated: 2026-06-18
graph_community: "Tokens & Sessions"
---

# Token Exchange V2 in RHBK — impersonation vs delegation, audience/scope semantics, DPoP/revocation pitfalls, and V1 legacy

**Scenario:** A SPA (public client, PKCE) authenticates and receives an access token with `azp=spa` and an audience that includes `gateway`. The API gateway (confidential client) needs to call `orders-api` in the user's identity and uses Standard Token Exchange V2 to exchange the incoming token for a narrowed token.

---

## 1. Impersonation vs delegation — which does V2 implement, and what does `sub`/`azp`/`act` look like?

### RHBK V2 implements impersonation only — not delegation

RFC 8693 defines two distinct semantic models:

| Model | Semantics | Required claims | The downstream knows… |
|-------|-----------|-----------------|----------------------|
| **Impersonation** | The exchanged token represents the end user alone; the intermediate (gateway) is invisible in the identity | `sub` = end user, `azp` = requester-client, **no `act` claim** | That the token was issued FOR the user to the current client (`azp`). Does NOT know a multi-step chain occurred. |
| **Delegation** | The exchanged token preserves the chain of custody; the resource server can see who the original party was AND who is acting | `sub` = end user, `azp` = requester-client, **`act` = original party** | The complete delegation path — `act` reveals the original caller. |

The RHBK 26.2 token exchange documentation states this explicitly: *"The token exchange specification mentions the concepts of impersonation and delegation. Red Hat build of Keycloak has support for the impersonation use case, but not yet for the delegation use case."* (extracted: rhbk-26-2-token-exchange.md, line 279)

The 26.6 documentation repeats the same statement verbatim. (extracted: rhbk-26-6-token-exchange.md, same section)

### What the exchanged token actually looks like

Given the scenario:

```
Original SPA token:
  sub: alice@example.com
  azp: spa
  aud: ["gateway", "spa"]
  scope: "openid profile orders:read payments:write"

Token exchange request (Gateway → Keycloak):
  grant_type: urn:ietf:params:oauth:grant-type:token-exchange
  subject_token: <SPA token>
  subject_token_type: urn:ietf:params:oauth:token-type:access_token
  audience: orders-api
  scope: orders:read

Exchanged token (returned to Gateway):
  sub: alice@example.com          ← same user, impersonation model
  azp: gateway                    ← the requester-client (the gateway)
  aud: ["orders-api"]             ← filtered by audience parameter
  scope: "orders:read"            ← determined by gateway's client scopes + scope param
  # NO act claim — delegation not supported
```

**Can `orders-api` tell, from the token alone, that the gateway (and not the SPA directly) performed the call?**

**Partially.** The `azp` claim reveals that the token was issued **to the gateway** (the `azp` value is `gateway`, not `spa`). So `orders-api` knows that the token was minted for the gateway client, not for the SPA. The `sub` claim alone does not expose the chain.

However, because V2 uses the **impersonation** model, the token does **not** carry an `act` claim that would record the fact that the gateway invoked token exchange with the SPA's token as input. The `orders-api` can deduce that the gateway is the authorized party (`azp`), but it **cannot reconstruct the full delegation chain** (SPA → Gateway via token exchange) from the token alone. (inferred: RFC 8693 §4.1 and §4.2 define `act` for delegation; its absence versus a delegation-chain-oblivious resource server is an intended consequence of the impersonation model.)

In practice: if the SPA had called `orders-api` directly with its own token, `azp` would be `spa`. The fact that `azp` is `gateway` tells `orders-api` the call came through the gateway, but not whether the gateway obtained the token via token exchange, client credentials, or some other grant — the delegation path is opaque.

---

## 2. What determines audience and scope of the exchanged token?

This is the **single most common trap** in RHBK token exchange — the interplay between the `scope` parameter, the `audience` parameter, and the requester-client's client scopes has subtle semantics that differ from legacy V1.

### The big rule (from the RHBK 26.2 migration notes)

*"The applied client scopes are based on the client triggering the token exchange request rather than the 'target' client specified by the audience parameter."* (extracted: rhbk-26-2-migration-changes.md, lines 75–77)

### How `scope` works

The `scope` parameter in a V2 token exchange request has **the same meaning as in other grants** — it adds **optional client scopes of the requester-client** (the gateway). When `scope` is omitted, only the **default client scopes** of the requester-client are used. (extracted: rhbk-26-2-token-exchange.md, lines 151–155)

This means: the `scope` parameter controls **up-scoping** — it can add optional scopes that the gateway has configured. It does **NOT** restrict the token to a subset of the subject token's scopes. The scope semantics are:
- **`scope` parameter omitted** → only the gateway's **default** client scopes are applied
- **`scope=orders:read`** → the gateway's **default + optional** client scopes that match `orders:read` are applied

### How `audience` works

The `audience` parameter is exclusively a **filtering/down-scoping** tool: *"The audience parameter can be used for filtering of audiences, so that the `aud` claim will contain only the audiences specified by the audience parameter."* And critically: *"This parameter will not add more audiences."* (extracted: rhbk-26-2-token-exchange.md, lines 157–168)

The audience parameter also filters client roles and, via the client scope filtering rule, may remove entire client scopes from the token (if a client scope contains client roles of a client not in the requested audience).

### Putting it together for the scenario

Assume the realm has:
- `gateway` client with default scope `default-scope-gw` and optional scope `orders:read`
- `orders-api` client (the target)
- The original SPA token carried `scope: "openid profile orders:read payments:write"`

**Token exchange request:**
```
POST /realms/demo/protocol/openid-connect/token
Authorization: Basic <gateway:secret>
grant_type=urn:ietf:params:oauth:grant-type:token-exchange
subject_token=<SPA token>
subject_token_type=urn:ietf:params:oauth:token-type:access_token
audience=orders-api
scope=orders:read
```

**Result:**
- `scope` parameter adds the gateway's optional client scope `orders:read`
- `audience=orders-api` filters the `aud` claim to only `["orders-api"]`
- If any default client scopes of the gateway contain audiences/roles for clients other than `orders-api`, they are filtered out

**The trap (♟️):** Many administrators assume the exchanged token's scope is a **subset** of the subject token's scope. It is NOT. The exchanged token's scope is determined by **the requester-client's (gateway's) client scopes**. The subject token's scope influences only **whether the exchange is authorized for audience/consent purposes** — not what scopes appear in the output.

For example:
- If `payments:write` is NOT an optional client scope of the gateway (and the gateway's default scopes don't include it), the exchanged token will NOT contain `payments:write` — even though the original SPA token had it.
- Conversely, if the gateway has an optional scope `admin:all` and the SPA token did NOT have it, the gateway CAN request `scope=admin:all` and receive an exchanged token with that scope (subject to the `subject_token` passing audience verification). (inferred: this is the "up-scoping" behavior described in the scope documentation — the scope parameter adds optional scopes of the requester-client, which may exceed the subject token's scope.)

**Recommended practice:** Always specify both `audience` (to narrow) and `scope` (to request only the needed optional scopes). Use the Client Scopes Evaluate tab to verify the resulting token. (extracted: rhbk-26-2-token-exchange.md, line 250)

---

## 3. Operational pitfalls

### (a) Gateway receives a DPoP-bound token from the SPA and tries to exchange it

**What happens:** The exchange fails with `invalid_request`.

**Why:** *"Standard Token Exchange does not support DPoP-bound tokens (as defined in RFC 7800) as the `subject_token` parameter. Only Bearer access tokens can be exchanged. If you attempt to use a DPoP-bound token as the subject token, the request will be rejected with an `invalid_request` error."* (extracted: rhbk-26-6-dpop.md, lines 147–150)

The reason is architectural: DPoP binds the token to the **original client's key** (the SPA's private key). If the AS allowed the gateway to use a DPoP-bound token as `subject_token`, the gateway would be impersonating the SPA's possession of the private key, defeating sender-constraining.

**How to still get a sender-constrained token downstream:**

*"While DPoP-bound tokens cannot be used as `subject_token` to token exchange, you can obtain DPoP-bound tokens as output."* (extracted: rhbk-26-6-dpop.md, lines 151–153)

The gateway should:
1. Obtain a **Bearer** subject token from the SPA (the SPA sends its access token in some other way, or the exchange is initiated before DPoP binding is applied).
2. Perform the token exchange with the gateway's own credentials + a **DPoP proof** in the exchange request.
3. The exchanged token returned to the gateway will be DPoP-bound to the **gateway's key** (not the SPA's key).
4. The gateway presents this DPoP-bound token (with a fresh DPoP proof) to `orders-api`.

This pattern is explicitly documented as a use case: *"You want to upgrade a Bearer token to a DPoP-bound token for increased security"* and *"You want to down-scope or change audiences while simultaneously adding DPoP binding."* (extracted: rhbk-26-6-dpop.md, lines 155–158)

**Architectural workaround:** Have the SPA NOT use DPoP. Instead, let the gateway apply DPoP downstream. Or have the gateway act as a token handler (BFF pattern) where the SPA never holds tokens directly.

### (b) Revocation chain — access vs refresh, and multi-site implications

**Subject token (SPA's token) revoked after exchange:**

From the RHBK 26.2 revocation documentation (lines 284–311):

| Exchange type | Revocation chain? | Details |
|--------------|-------------------|---------|
| access-token → **access-token** | **NO** | Revoking the subject token does NOT revoke the exchanged access token. "Supporting of a 'revocation chain' for access tokens would mean quite an overhead." |
| access-token → **refresh-token** | **YES** | Revoking the subject token revokes the exchanged refresh token AND all downstream tokens in the chain. Additionally removes the client session of the requester-client from the user session. |

(extracted: rhbk-26-2-token-exchange.md, lines 285–305)

**Why the difference?** Access tokens are ephemeral and stateless — the AS does not track cross-token relationships for them (the overhead would be prohibitive). Refresh tokens, however, are stateful and tied to the user session, so the chain is naturally maintained through the session's client sub-sessions.

#### Multi-site HA implications

In an **Active-Passive multi-site** deployment with external Infinispan / Data Grid cross-site replication:

- **Exchanged access tokens (no revocation chain):** These are signed JWTs validated offline by `orders-api` via JWKS. There is no session-side state to replicate. If the subject token is revoked at Site A, the exchanged access token (already delivered to the gateway) continues to work at both sites until natural expiry. The site failover does not affect this — the token is valid until its `exp` claim regardless of which site signed it (assuming both sites share the same signing keys or JWKS).
  - **Implication:** The exchanged access token's TTL must be **very short** (minutes, not hours). The documentation explicitly warns: *"the administrator must ensure that access tokens are short-lived and are revoked automatically after some time."* (extracted: rhbk-26-2-token-exchange.md, lines 290–291)

- **Exchanged refresh tokens (revocation chain works):** Revocation of the subject token triggers removal of the requester's client session from the user session. This session state lives in Infinispan and **is** replicated cross-site via Data Grid Cross-DC. Therefore, revocation propagation **does** work across sites for refresh tokens — but only if the Infinispan cross-site replication is healthy. A split-brain or replication delay could create a window where the refresh token is still usable at the passive site.
  - **Implication:** Even for refresh tokens, keep lifetimes bounded by the site-replication RPO. In Active-Passive mode, the failover process (take-offline → clearcache → bring-online) destroys all session state, so any not-yet-revoked refresh tokens are lost anyway. (inferred: cross-site session consistency considerations from the HA architecture.)

**Practical rule for multi-site:** Keep exchanged **access token TTL at ≤ 5 minutes** (the HA guide's typical failover window). For **refresh token exchange**, set `Allow refresh token in Standard Token Exchange` to `Same session` (not broader values), so the refresh token is tied to the user's authenticated session and revoked when the session ends.

---

## Bonus: Why was token exchange preview for years, what made V2 GA in 26.2, and what still needs V1?

### Token exchange's long preview history

In RHBK 26.0 and earlier, token exchange was a single **Preview** feature (`--features=token-exchange` or `--features=preview`), disabled by default. The implementation was described as *"a very loose implementation of the OAuth Token Exchange specification at the IETF. We have extended it a little, ignored some of it, and loosely interpreted other parts of the specification."* (extracted: rhbk-26-0-token-exchange.md, line 30) For non-internal use cases, it additionally required `admin-fine-grained-authz` (also preview).

The feature stayed preview for years because:
1. The implementation was not RFC 8693-compliant (loose interpretation)
2. It depended on FGAP v1 (itself preview) for authorization — coupling two unstable features
3. The scope/audience semantics were confusing (based on target client, not requester)
4. Security review was incomplete (public clients allowed, no clear impersonation/delegation split)

### What made V2 GA in 26.2

The **Standard token exchange V2** (`token-exchange-standard:v2`) became **enabled by default, fully supported** in RHBK 26.2. (extracted: rhbk-26-2-migration-changes.md, lines 58–60)

The one use case that truly drove V2 to GA: **Internal-to-internal token exchange** (RFC 8693) — the ability for a confidential client to exchange an existing RHBK token for a new token targeted at a different client **in the same realm**. This is the critical enabler for API gateway / service-mesh / BFF architectures where:
- A gateway receives a token meant for itself
- The gateway needs to call a downstream service in the user's identity
- The downstream service must not see the gateway's privileged scopes

This use case (internal→internal) is the most common, the most spec-compliant, and the one with the cleanest security boundary (confidential clients only, audience verification, same-realm). It was prioritized for GA.

The 26.2 upgrade guide says: *"If you used the internal-internal token exchange, consider migrating to the new standard token exchange."* (extracted: rhbk-26-2-migration-changes.md, line 60)

### What still needs legacy V1 (+ FGAP:v1) or alternative features

| Use case | V1 required? | Alternative in V2/other |
|----------|-------------|------------------------|
| **Internal→internal (same realm)** | ❌ | V2 — GA, supported, recommended |
| **Internal→external IdP token** (e.g. RHBK → Facebook) | ✅ V1 only | Identity Brokering API V2 (preview), or JWT Authorization Grant |
| **External→internal** (foreign JWT → RHBK token) | ✅ V1 only | JWT Authorization Grant (confidential clients) or OAuth Identity & Authorization Chaining across domains |
| **Impersonation** (`requested_subject`) | ✅ V1 only | V2 explicitly says "not implemented yet" (extracted: rhbk-26-2-token-exchange.md, line 279; rhbk-26-6-token-exchange.md table) |
| **Public client exchanges** | ✅ V1 only (limited) | Use refresh token grant for downscoping (extracted: rhbk-26-2-migration-changes.md, lines 79–81) |
| **SAML2 assertion output** | ✅ V1 only | Not available in V2 — use JWT Authorization Grant or SAML flows |
| **Cross-realm token exchange** | ✅ V1 only | OAuth Identity & Authorization Chaining across domains (rhbk-26-6 supports this) |

**FGAP dependency:** *"If you still need legacy token exchange feature, you also need Fine-grained admin permissions version 1 (FGAP:v1) enabled because version 2 (FGAP:v2) does not have support for token exchange permissions. This is on purpose because token-exchange is conceptually not really an 'admin' permission and hence there is no plan to add token exchange permissions to FGAP:v2."* (extracted: rhbk-26-2-migration-changes.md, lines 68–70)

FGAP:v1 is **deprecated** as of RHBK 26.6: *"Fine-Grained Admin Permissions (FGAP) v1 is deprecated. This version no longer receives enhancements and improvements and will be removed in a future release. To ensure continued support, migrate to FGAP v2."* (extracted: rhbk-26-6-deprecated.md, lines 20–21)

This means the V1+FGAP:v1 combination has a **limited lifespan** — Red Hat recommends migrating away from V1 use cases to the alternatives listed above.

---

## Contradictions / caveats

- The `scope` parameter's ability to **up-scope** beyond the subject token's scope (because it uses the requester-client's optional client scopes) may surprise administrators familiar with V1, where scopes were based on the target client. This is by design in V2 — the subject token's scope only controls **audience verification** (the subject token must list the requester in `aud`) and **consent** checks, not the scope of the output.
- The DPoP restriction (no DPoP-bound `subject_token`) is documented in the DPoP chapter (rhbk-26-6-dpop.md §16.6) but not repeated in the token exchange chapter — an administrator configuring both features might miss the interaction.
- The revocation chain distinction (access→access has no chain, access→refresh does) is asymmetric but documented — the "no chain" for access tokens means the administrator MUST keep access token TTLs short themselves. The referenced guide does not specify a recommended maximum, but the HA architecture's ~5-minute failover window is a reasonable bound for exchanged tokens.
- Legacy V1's deprecation timeline is not specified beyond "will be removed in a future release" — organizations relying on V1-only use cases (particularly impersonation and external exchange) should plan migration now.

## See also
- [[token-exchange]] — V2 vs V1 comparison, key form parameters, limitations
- [[dpop]] — DPoP sender-constraining: key binding, proof JWT, DPoP vs bearer
- [[dpop]] — DPoP mechanics, use cases, refresh token handling
- [[token-revocation]] — RFC 7009 semantics, cascade rules, unsupported token types
- [[refresh-token-rotation]] — one-time-use refresh tokens, replay detection
- [[tokens-and-sessions]] — token lifespans, session types, timeout governance
- [[rhbk-ha-architectures]] — single-cluster vs multi-cluster HA, Infinispan replication
- [[client-authentication-methods]] — confidential client auth for exchange requests
- [[oidc-grant-types]] — the full list of supported grants including token exchange
- [[securing-apps-oidc-saml]] — the Securing Applications guide (the source guide for these reference notes)
- [[sso-implementation-review]] — evaluation lens for SSO integration
- [[bff-token-handler]] — BFF pattern for token management, DPoP, and exchange

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **rhbk-26-2-token-exchange.md** — Chapter 12, RHBK 26.2 Securing Applications and Services Guide. Full documentation of Standard Token Exchange V2: flow, parameters, scope/audience semantics, revocation chain, comparison table with V1. Source: Red Hat RHBK 26.2 documentation.
- **rhbk-26-6-token-exchange.md** — Chapter 13, RHBK 26.6 Securing Applications and Services Guide. Updated version: V1 marked deprecated, impersonation-only confirmed, same scope/audience rules. Source: Red Hat RHBK 26.6 documentation.
- **rhbk-26-6-dpop.md** — Chapter 16, RHBK 26.6 Securing Applications and Services Guide. Section 16.6 explicitly documents the "DPoP with Standard Token Exchange" interaction: DPoP-bound `subject_token` rejected, DPoP output possible. Source: Red Hat RHBK 26.6 documentation.
- **rhbk-26-0-token-exchange.md** — Chapter 12, RHBK 26.0 Securing Applications and Services Guide. Shows the "preview, loosely implemented" baseline before V2. Source: Red Hat RHBK 26.0 documentation.
- **rhbk-26-2-migration-changes.md** — RHBK 26.2 Upgrading Guide. Documents the V2 GA announcement, the scope behavior change (requester-client vs target-client), public client ban, FGAP dependency for V1. Source: Red Hat RHBK 26.2 documentation.
- **rhbk-26-6-deprecated.md** — RHBK 26.6 Release Notes. Documents FGAP:v1 as deprecated. Source: Red Hat RHBK 26.6 documentation.
- **rhbk-26-4-features.md** — RHBK 26.4 Enabling and disabling features. Lists `token-exchange-standard:v2` as enabled-by-default supported, `token-exchange:v1` as disabled-by-default preview. Source: Red Hat RHBK 26.4 documentation.
- **rhbk-26-4-token-exchange.md** — Chapter 12, RHBK 26.4 Securing Applications and Services Guide. V2 and V1 comparison, FGAP:v1 requirement for V1, internal→internal only for V2. Source: Red Hat RHBK 26.4 documentation.
- **securing-apps-oidc-saml.md** (references guide) — Sections 11–13: consolidated V2/V1 comparison, DPoP integration, cross-domain chaining. Source: Red Hat RHBK ref guide.

### Wiki / upstream (`web:`)

- **RFC 8693** — *OAuth 2.0 Token Exchange*. IETF. Defines the `urn:ietf:params:oauth:grant-type:token-exchange` grant type, impersonation vs delegation models, `act` claim semantics, audience/scope parameters.
- **RFC 9449** — *OAuth 2.0 Demonstrating Proof-of-Possession (DPoP)*. IETF. Defines `cnf.jkt` binding, DPoP proof JWT, `dpop_bound_access_tokens` client metadata, interaction with other grant types.
- **RFC 7009** — *OAuth 2.0 Token Revocation*. IETF. Defines the revocation endpoint, cascade requirement (refresh token revocation SHOULD invalidate derived access tokens), token-type hint handling.
- **token-exchange** (wiki entity) — Wiki page comparing V2 vs V1, listing key form parameters and limitations.
- **dpop** (wiki entity) — Wiki page on DPoP sender-constraining mechanics.
- **token-revocation** (wiki entity) — Wiki page on RFC 7009 revocation semantics and cascade rules.
