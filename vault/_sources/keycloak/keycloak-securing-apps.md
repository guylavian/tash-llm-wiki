---
source: Keycloak securing-apps (upstream OSS) — generic view only
url: https://www.keycloak.org/docs/latest/securing_apps/index.html
fetched: 2026-06-18
status: upstream Keycloak docs (OSS)
feeds: [bff-token-handler, service-to-service-client-credentials]
---

<!-- canonical index 404s; harvested from current per-page docs at the new path structure:
     /securing-apps/overview, /securing-apps/oidc-layers, /securing-apps/token-exchange,
     /securing-apps/dpop. Section anchors cite source page unless noted. -->

## bff-token-handler

- RULE: Browser/SPA front end must be a **public client**; client secrets cannot be stored safely client-side (overview → "Basic steps", client types). ANTI-PATTERN: shipping a confidential client secret in a JS/SPA bundle, or marking the SPA confidential. SYMPTOM: secret visible in network tab / source maps; secret leaks force rotation; "invalid_client" once leaked secret is revoked.

- RULE: Use **Authorization Code flow + PKCE (S256)** for browser and native apps (oidc-layers → Authorization Code, FAPI client profiles → pkce-enforcer). ANTI-PATTERN: Implicit flow for SPAs; omitting PKCE on a public client; using `plain` challenge method instead of S256. SYMPTOM: access token appears in URL fragment, leaks to browser history and web-server logs; "PKCE code verifier invalid" / "Missing parameter: code_challenge" when realm enforces PKCE but app omits it.

- RULE: Put a **confidential client behind the BFF backend** — the server-side handler holds the confidential client, brokers the code exchange, and stores tokens; the browser holds only a session cookie (oidc-layers → public vs confidential clients). ANTI-PATTERN: doing the token exchange in the browser and storing tokens in JS-accessible storage. SYMPTOM: tokens reachable via XSS; no server-side verification of client identity.

- RULE: **Do not store access/refresh tokens in JS-accessible storage** (localStorage, sessionStorage); keep them server-side or in HTTP-only cookies (oidc-layers → Implicit/token-leakage mitigations). ANTI-PATTERN: persisting tokens in browser storage. SYMPTOM: token theft via XSS; long-lived tokens visible in dev tools; replay after page close.

- RULE: **Redirect URIs must be as specific as possible**; production web applications must use HTTPS-only redirect URIs; native apps should prefer `127.0.0.1` over `localhost` (oidc-layers → Redirect URIs). ANTI-PATTERN: wildcard redirect URIs; HTTP callbacks in production. SYMPTOM: open-redirect / phishing vectors; "Invalid parameter: redirect_uri" when actual callback not whitelisted.

- RULE: **All interactions must use TLS/HTTPS** (oidc-layers → TLS Considerations). ANTI-PATTERN: HTTP token or callback endpoints. SYMPTOM: code/token interception, MITM; Keycloak rejects with "HTTPS required".

- RULE: To force browser-app hardening, apply the **oauth-2-1-for-public-client** global client profile via Client Policies (oidc-layers → OAuth 2.1 compliance). ANTI-PATTERN: assuming defaults already enforce OAuth 2.1 posture. SYMPTOM: Implicit/ROPC flows silently remain usable; audit flags non-compliant public client.

- RULE: **Prefer ecosystem / standards-compliant libraries** over custom Keycloak adapters to stay spec-compliant and avoid vendor lock-in (overview → "Basic steps"). ANTI-PATTERN: hand-rolling OIDC or hard-coupling to a Keycloak adapter. SYMPTOM: incomplete protocol handling; painful migration off Keycloak.

- RULE (DPoP / token binding): When the BFF issues tokens bound to its backend key, do not treat DPoP-bound tokens as standard Bearer tokens — each request requires a new DPoP proof signed by the private key, including `typ: "dpop+jwt"` header, asymmetric algorithm, embedded public key JWK, HTTP method (`htm`), and target URI (`htu`) bindings (dpop → DPoP Proof Header, DPoP Proof Body). ANTI-PATTERN: reusing a single DPoP proof across multiple requests; omitting `htm`/`htu` binding. SYMPTOM: resource server rejects replayed proof; "invalid_dpop_proof" error.

- RULE (DPoP nonce): When a resource server returns a `DPoP-Nonce` header, the client must regenerate a new proof including that nonce; nonces are single-use or short-lived (dpop → Nonce Mechanism). ANTI-PATTERN: caching and reusing DPoP proofs after receiving a nonce. SYMPTOM: "use_dpop_nonce" error; old captured proofs succeed on replay despite nonce rotation.

- RULE (Token exchange in BFF downscoping): When the BFF calls downstream services it should downscope the token using the `audience` parameter in a token exchange request to restrict permissions to only what the downstream resource requires (token-exchange → Standard Token Exchange Scope). ANTI-PATTERN: forwarding the original broad-scoped token to all downstream services. SYMPTOM: downstream service receives token with excessive permissions; principle of least privilege violated.

- RULE (Token exchange — no upscoping without policy): By default, token exchange can request extra scopes not in the subject token; apply the `downscope-assertion-grant-enforcer` client policy executor to prevent scope escalation (token-exchange → Standard Token Exchange Scope). ANTI-PATTERN: allowing a backend to silently obtain elevated scopes without explicit policy. SYMPTOM: backend acquires permissions not granted to the original user session.

- RULE (Token exchange — no new session): Token exchange never creates a new user session; the exchanged token inherits the original session lifetime (token-exchange → Standard Token Exchange Details). ANTI-PATTERN: designing flows that treat the exchanged token as establishing an independent session. SYMPTOM: session timeout tied to original session; unexpected expiry in downstream call chain.

## service-to-service-client-credentials

- RULE: **client_credentials grant = service account on a confidential client**; the client authenticates as itself, not as a user (oidc-layers → Client Credentials). Enable via Client authentication = On + Service accounts roles. ANTI-PATTERN: public client or ROPC/shared-user-credentials for machine-to-machine. SYMPTOM: "unauthorized_client" / "Client not allowed for direct access grants"; no per-service audit trail; user credential exposure.

- RULE: Confidential clients authenticate by **client secret, private_key_jwt (RFC 7523 signed JWT), or client_secret_jwt**, submitted via `client_assertion` (oidc-layers → Client Credentials, client authentication methods). ANTI-PATTERN: committing client_secret to VCS; using weak or static key material. SYMPTOM: secret exposed in repository history; rotation requires downtime; "invalid_client" on mismatch.

- RULE: For signed JWT auth, **register the client's public key via a JWKS URL** so keys rotate without reconfiguration — Keycloak fetches new keys on an unknown `kid`; include X.509 headers if the upstream IdP requires the cert thumbprint (server-admin → client authentication). ANTI-PATTERN: pasting a single static cert that never rotates. SYMPTOM: auth fails after key rotation; "Unable to verify signature" / unknown kid error.

- RULE: **mTLS / X.509 client auth is disabled by default** and requires a server truststore with the client cert chain plus `--https-client-auth=request|required`; when Keycloak acts as an *outbound* client to an mTLS-protected endpoint, configure a separate outgoing HttpClient keystore (server → mutual-tls). ANTI-PATTERN: expecting mTLS to work without explicit server-side configuration; conflating Keycloak-as-server vs Keycloak-as-client cert config. SYMPTOM: "ssl handshake failure"; cert presented but untrusted → 401.

- RULE: **Resource servers must validate bearer tokens** (issuer, expiry, signature) via JWKS/certificate endpoint or the Introspection endpoint before granting access (oidc-layers → Validating Access Tokens, Introspection). ANTI-PATTERN: trusting the Authorization header without signature + iss/exp checks. SYMPTOM: forged or expired tokens accepted; service-account impersonation.

- RULE: **Introspection endpoint is confidential clients only**; avoid synchronous per-request introspection at scale — prefer local JWT validation with cached JWKS public key lookup by `kid` (oidc-layers → Introspection Endpoint). ANTI-PATTERN: public client calling introspection; synchronous introspection on every request without caching. SYMPTOM: public client receives 401/403 from introspection endpoint; Keycloak server bottleneck under high validation load.

- RULE: To enforce machine-client hardening, apply the **oauth-2-1-for-confidential-client** global client profile via Client Policies (oidc-layers → OAuth 2.1 compliance). ANTI-PATTERN: relying on defaults for OAuth 2.1 confidential-client posture. SYMPTOM: disallowed grants silently remain usable; audit flags non-compliant confidential client.

- RULE (Token exchange — confidential client only): Token exchange requests must originate from **confidential clients only**; public clients are explicitly prohibited (token-exchange → Standard Token Exchange Enable). ANTI-PATTERN: attempting token exchange from a public client. SYMPTOM: request rejected; "unauthorized_client" or exchange aborted.

- RULE (Token exchange — audience in subject token): The `subject_token` sent to the token exchange endpoint **must list the requester client in its `aud` claim**, unless the client is exchanging its own token (token-exchange → Standard Token Exchange Details). ANTI-PATTERN: exchanging a token whose `aud` excludes the requesting client. SYMPTOM: token exchange fails with authorization denied / audience mismatch error.

- RULE (Token exchange — bearer tokens only as subject): **Sender-constrained tokens (DPoP-bound, X.509-bound) cannot be used as `subject_token`** in standard token exchange; only Bearer access tokens are accepted (token-exchange → Standard Token Exchange Details). ANTI-PATTERN: passing a DPoP-bound token as the subject of an exchange. SYMPTOM: exchange rejected with `invalid_request` error.

- RULE (DPoP for service-to-service): When DPoP is enabled, every token request and resource access must include a fresh proof; `cnf.jkt` (public key thumbprint) is embedded in the issued token and must match the proof's key; access token hash (`ath`) must be included in the proof body when accessing protected resources (dpop → Key Binding, DPoP Proof Body). ANTI-PATTERN: treating a DPoP-bound access token as reusable Bearer; omitting `ath` in resource requests. SYMPTOM: resource server rejects requests with "invalid_dpop_proof"; middle-tier service cannot chain the same token downstream.

- RULE (DPoP mandatory enforcement): When "Require DPoP bound tokens" is enabled on a client, **all token requests must include a valid DPoP proof**; without it the token endpoint will reject the request (dpop → Configuring Keycloak). ANTI-PATTERN: issuing Bearer tokens to a client configured to require DPoP. SYMPTOM: tokens issued without DPoP binding bypass sender-constraint; security advisory.

- RULE (PAR caveat): If a confidential client uses **client_secret_post** with PAR, rotate client secrets after upgrade to avoid previously-exposed secrets remaining valid (server-admin → PAR security note). ANTI-PATTERN: keeping old secret post-upgrade. SYMPTOM: previously-exposed secret remains valid; security advisory triggered.
