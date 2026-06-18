---
source: OWASP API Security Top 10 (2023) — Broken Auth, BOLA/BFLA
url: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
fetched: 2026-06-18
status: OWASP API Top 10 2023
feeds: [audience-and-scope-checks, access-token-validation-resource-server]
---

# OWASP API Security Top 10 (2023) — load-bearing requirements

Source pages fetched: index (0x11-t10), API1 BOLA (0xa1), API2 Broken Authentication (0xa2),
API3 BOPLA (0xa3), API5 BFLA (0xa5). This is the web:(upstream) tier — OWASP is advisory/
best-practice, not a normative RFC; "RULE" below means OWASP's prescriptive guidance, not a
spec MUST.

## access-token-validation-resource-server

- RULE (API2:2023, "How to prevent"): the resource server must verify token authenticity —
  validate the signature; never accept unsigned / weakly-signed JWTs. Use standard libraries,
  don't roll your own token handling.
  - ANTI-PATTERN: accepting `{"alg":"none"}`, or skipping signature verification ("trust the
    bearer because it decodes").
  - SYMPTOM: forged/tampered JWT with attacker-chosen claims is accepted; auth bypass, "alg:none"
    token grants access; pentest finding "API accepts unsigned token."

- RULE (API2:2023, "When is the API vulnerable" + prevent): validate the JWT expiration (`exp`)
  before honoring the request; reject expired tokens.
  - ANTI-PATTERN: not checking `exp` / treating any decodable token as live.
  - SYMPTOM: long-dead/replayed tokens still work; revoked or logged-out sessions keep access;
    "token never expires" ticket.

- RULE (API2:2023, "How to prevent"): require re-authentication for sensitive operations
  (e.g. changing account-owner email or 2FA phone number) — a valid access token alone is not
  sufficient for high-impact actions.
  - ANTI-PATTERN: letting any still-valid session mutate security-critical settings silently.
  - SYMPTOM: account-takeover via stolen/long-lived token changing recovery email; no step-up
    challenge on sensitive endpoints.

- RULE (API1:2023, BOLA prevent): derive the acting user's identity from the validated token,
  then authorize against it — do NOT trust an ID supplied in the path/query/header/body to
  decide who the caller is.
  - ANTI-PATTERN: using a client-supplied `user_id`/`account_id` param as the identity instead
    of the token subject.
  - SYMPTOM: changing the ID in the request returns another user's data (IDOR); "I see someone
    else's record by editing the URL."

## audience-and-scope-checks

- RULE (API1:2023, BOLA prevent): object-level authorization must run in every function that
  reads/writes a record using a client-supplied ID — check the authenticated subject is
  permitted for *that specific object*, per user policy/hierarchy. Note OWASP's caveat: merely
  comparing token-subject vs param-ID does not cover all BOLA cases (need full policy check).
  - ANTI-PATTERN: enforcing authentication but not per-object authorization; relying on the ID
    being "unguessable" as the only control.
  - SYMPTOM: horizontal privilege escalation — authorized user reaches objects they don't own;
    sequential/enumerable IDs leak records.

- RULE (API1:2023, BOLA prevent): prefer random, unpredictable GUIDs for record IDs (defense in
  depth — does not replace the authorization check); add tests that probe the authorization
  mechanism.
  - ANTI-PATTERN: sequential integer IDs as the sole obstacle to enumeration; no auth tests.
  - SYMPTOM: trivial ID enumeration scrapes the dataset.

- RULE (API5:2023, BFLA prevent): deny by default — every function requires an explicit role/
  group grant. Enforce function/role authorization in a centralized, consistently-invoked module
  (or external gateway), not scattered per-controller. Admin controllers should inherit a base
  that checks role; regular controllers exposing admin actions need explicit checks.
  - ANTI-PATTERN: inferring "admin-only" from the URL path; protecting only the routes you
    remembered; per-endpoint ad-hoc checks.
  - SYMPTOM: regular user calls an admin endpoint successfully; guessed/undocumented admin route
    works; vertical privilege escalation.

- RULE (API5:2023, BFLA prevent): authorize on the action/role/scope, independent of HTTP method
  and URL structure — every privileged operation re-checks the caller's role/scope.
  - ANTI-PATTERN: assuming a method (e.g. only POST is mutating) or path implies the privilege;
    no scope/role check on alternate verbs.
  - SYMPTOM: method swap (GET→PUT/DELETE) performs an unauthorized mutation; "DELETE worked but
    the UI never offered it."

- RULE (API3:2023, BOPLA prevent): authorize at the *property* level too — check the caller is
  allowed to read/write each specific object field; allowlist returned/bindable properties (no
  blanket `to_json()`/auto-bind), validate responses against a schema, expose the minimum.
  - ANTI-PATTERN: generic serialization that leaks every field; mass-assignment binding client
    input straight onto internal properties (e.g. `blocked`, `total_price`, `role`).
  - SYMPTOM: excessive data exposure (sensitive fields appear in responses); privilege/state
    escalation by injecting an internal field the caller shouldn't write.

## Cross-cutting note (audience / scope vs OWASP)

OWASP's 2023 pages name signature/expiry/authenticity and role-based function authorization
explicitly, but do NOT spell out `aud`/`iss` audience-claim verification or OAuth `scope`
matching as named bullets — those are the RFC layer (see _sources/rfc9068.md JWT-AT profile
and rfc9700 BCP). Map OWASP "verify token authenticity + per-function role check" onto the
spec-level audience/scope rules when crosslinking; OWASP supplies the attack/symptom framing
(BOLA/BFLA), the RFCs supply the normative `aud`/`scope` MUSTs.
