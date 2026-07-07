# RHBK 26.6 — Authorization Services (Fine-Grained Authorization)

Internal runbook for Red Hat build of Keycloak (RHBK) 26.6 fine-grained authorization. Content is shared with upstream Keycloak 26 except where noted as RHBK-specific. Grounded in the RHBK 26.6 Authorization Services Guide.

> Air-gap note: All authorization flows are server-internal — no outbound network. External touchpoints are limited to: pushed claims sourced from external IdP/LDAP tokens, and JS policy providers deployed as JAR artifacts (stage in your internal Maven/registry, e.g. `registry.example.internal`). Treat client secrets / PATs as `***`.

## 1. Concepts & architecture

RHBK combines ABAC, RBAC, UBAC, CBAC, rule-based (JavaScript), time-based, and custom ACMs (via SPI).

| Pattern | Role |
|---|---|
| PAP (Policy Administration Point) | Admin Console UIs + Protection API to manage resource servers, resources, scopes, permissions, policies |
| PDP (Policy Decision Point) | Receives authorization requests; evaluates policies → permissions |
| PEP (Policy Enforcement Point) | Enforces decisions at the resource server (built-in policy enforcers) |
| PIP (Policy Information Point) | Obtains attributes from identities and runtime during policy evaluation |

Three processes: **Resource Management** (define what is protected), **Permission & Policy Management** (define security requirements), **Policy Enforcement** (enforce decisions via a PEP).

Terminology:
- **Resource server** — any confidential client acting as host of protected resources.
- **Resource** — object being protected; unique id; may represent one or a set (e.g. typed "Bank Account").
- **Scope** — bounded extent of access (verb) on a resource, e.g. `view`, `edit`, `delete`; can also represent resource attributes.
- **Permission** — couples protected object (resource/scope) with policies. Model: `X CAN DO Y ON RESOURCE Z`.
- **Policy** — conditions to grant access; decoupled from the object; reusable; can be aggregated.
- **Policy provider** — implementation of a policy type; pluggable via SPI.
- **Permission ticket** — opaque UMA token representing requested resources/scopes + context; issued by the Protection API; exchanged by the client for an RPT.
- **RPT (Requesting Party Token)** — access token holding granted permissions.

## 2. Enabling authorization services on a client (resource server)

1. Create/select a confidential OIDC client (e.g. `my-resource-server`, Root URL `http://${host}:${port}/my-resource-server`).
2. Client settings → **Capability Config** → toggle **Authorization Enabled** = On → Save.
3. New **Authorization** tab appears with sub-tabs: **Settings**, **Resource**, **Authorization Scopes**, **Policies**, **Permissions**, **Evaluate**, **Export**.

### Resource Server Settings

| Setting | Values / behavior |
|---|---|
| **Policy Enforcement Mode** | `Enforcing` (default) — deny by default even with no policy on a resource; `Permissive` — allow when no policy is associated; `Disabled` — disable all policy evaluation, allow all |
| **Decision Strategy** | `Affirmative` — at least one permission positive grants access (on conflict, grants); `Unanimous` — all permissions must be positive (a single deny denies) |
| **Remote Resource Management** | If `false`, resources managed only from the Admin Console. Enabled by default |

### Export / import configuration

Export tab → JSON (resources+scopes, policies, permissions) shown in a text area; **Download** to save. Import via **Resource Server Settings → Import**, choose a config file. Useful to seed/update a resource server config offline.

## 3. Managing resources & scopes

Manage via **Resource** and **Authorization Scopes** tabs. Resource list shows Type, Owner, URIs, associated scopes, associated permissions; you can **Create Permission** directly from a resource.

Resource fields (Create resource):

| Field | Meaning |
|---|---|
| **Name** | Human-readable, unique |
| **Type** | String grouping a set of resource instances (typed resources) |
| **URIS** | Locations/addresses (relative paths for HTTP resources) |
| **Scopes** | One or more scopes to associate |

- **Attributes** — key/value pairs (value = one or many strings, comma-separated); available to policies during evaluation.
- **Typed resources** — `type` groups resources protected by a common permission set.
- **Owner** — default owner is the resource server; can be a specific user → enables owner-based permissions and (with `ownerManagedAccess`) Account Console management.
- **Remote management** — via the Protection API (set user identifier to assign ownership).

## 4. Managing policies

Policies tab → **Create policy** → select type. Common fields on all types: **Name** (unique), **Description**, **Logic**.

| Policy type | Key configuration |
|---|---|
| **User** | `Users` — which users get access |
| **Role** | `Realm Roles`, `Client Roles` (requires a Client), `Fetch Roles`. Any listed role grants unless marked **Required** (then all required roles must be held). Combine realm+client roles |
| **Client** | `Clients` — which clients get access |
| **Group** | `Groups Claim` (claim holding group names/paths; defaults to realm config if undefined), `Groups` with per-group **Extend to Children** |
| **Client Scope** | `Client Scopes` — any listed grants unless marked **Required** |
| **Time** | `Start time` / `Expire time`; optional **Repeat**: `Day of Month`, `Month`, `Year`, `Hour`, `Minute` (each accepts a range). All conditions ANDed |
| **Aggregated** | `Apply Policy` (set of policies), `Decision Strategy`. No circular references allowed |
| **Regex** | `Target Claim` (dot notation + `[index]`, e.g. `contact.address[0].country`), `Regex Pattern`; resolves attributes from the current identity |
| **JavaScript** | Rule-based; uses the Evaluation API. JS upload is disabled by default — deploy JS providers as a JAR (see JavaScript Providers) and select the deployed script |

**Fetch Roles**: by default only roles in the request token are checked; enabling makes the policy ignore token roles and check roles associated with the user.

**Logic** (Positive/Negative): `Negative` negates the policy result (e.g. grant only to users *without* a role). `Positive` is the default.

**Decision strategy for aggregated policies**: `Unanimous` (default), `Affirmative`, `Consensus` (positive must outnumber negative; tie = negative).

### JavaScript policy examples (RHBK Evaluation API)

```javascript
// ABAC: context attribute (client IP)
const context = $evaluation.getContext();
if (context.getAttributes().containsValue('kc.client.network.ip_address', '127.0.0.1')) {
    $evaluation.grant();
}
```

```javascript
// ABAC: identity attribute (email domain)
const identity = $evaluation.getContext().getIdentity();
const email = identity.getAttributes().getValue('email').asString(0);
if (email.endsWith('@keycloak.org')) { $evaluation.grant(); }
```

```javascript
// RBAC + group / user checks
const identity = $evaluation.getContext().getIdentity();
if (identity.hasRealmRole('keycloak_user')) { $evaluation.grant(); }
if (identity.hasClientRole('my-client', 'my-client-role')) { $evaluation.grant(); }

const realm = $evaluation.getRealm();
if (realm.isUserInRealmRole('marta', 'role-a')) { $evaluation.grant(); }
if (realm.isUserInClientRole('marta', 'my-client', 'some-client-role')) { $evaluation.grant(); }
if (realm.isGroupInRole('/Group A/Group D', 'role-a')) { $evaluation.grant(); }
if (realm.isUserInGroup('marta', '/Group A/Group B')) { $evaluation.grant(); }
```

```javascript
// Push arbitrary claims to the resource server
const permission = $evaluation.getPermission();
if (granted) {
    permission.addClaim('claim-a', 'claim-a');
    permission.addClaim('claim-a', 'claim-a1');
    permission.addClaim('claim-b', 'claim-b');
}
```

> ABAC caveat: ensure protected attributes are read-only and not user-editable (Threat model mitigation).

### Evaluation API

Main interface `org.keycloak.authorization.policy.evaluation.Evaluation`: `getPermission()`, `getContext()`, `getRealm()`, `grant()`, `deny()`. Default state is **denied** — policies must call `grant()` explicitly. `EvaluationContext` exposes `getIdentity()` (built from the OAuth2 access token, incl. custom protocol-mapper claims) and `getAttributes()`.

Built-in context attributes:

| Name | Description | Type |
|---|---|---|
| `kc.time.date_time` | Current date and time | String |
| `kc.client.network.ip_address` | Client IP (null if not provided) | String |
| `kc.client.network.host` | Client host name (IP or proxy header) | String |
| `kc.client.id` | The client id | String |
| `kc.client.user_agent` | `User-Agent` HTTP header | String[] |
| `kc.realm.name` | Realm name | String |

## 5. Managing permissions

Permissions tab → choose **resource-based** or **scope-based**.

**Resource-based** fields: Name, Description, **Apply To Resource Type** / **Resource Type** (apply to all resources of a type), **Resources**, **Policy**, **Decision Strategy**. Typed permissions apply common policies to all resources of a type (e.g. all bank accounts).

**Scope-based** fields: Name, Description, **Resource** (restricts scope list; none = all scopes), **Scopes**, **Policy**, **Decision Strategy**.

Permission decision strategies: `Unanimous` (default — all policies positive), `Affirmative` (at least one positive), `Consensus` (positive must outnumber negative; tie = negative).

## 6. Evaluating & testing policies

**Evaluate** tab simulates authorization requests: **Identity Information** (the requesting user), **Contextual Information** (extra context attributes), **Permissions** (build the request from resources/scopes; **Add** with none = all protected resources/scopes). Click **Evaluate**.

## 7. Authorization Services endpoints (RHBK extensions to OAuth2/UMA)

Discovery (UMA 2):

```bash
curl -X GET http://${host}:${port}/realms/${realm-name}/.well-known/uma2-configuration
```

```json
{
  "token_endpoint": "http://${host}:${port}/realms/${realm-name}/protocol/openid-connect/token",
  "token_introspection_endpoint": "http://${host}:${port}/realms/${realm-name}/protocol/openid-connect/token/introspect",
  "resource_registration_endpoint": "http://${host}:${port}/realms/${realm-name}/authz/protection/resource_set",
  "permission_endpoint": "http://${host}:${port}/realms/${realm-name}/authz/protection/permission",
  "policy_endpoint": "http://${host}:${port}/realms/${realm-name}/authz/protection/uma-policy"
}
```

`token_endpoint` supports the `urn:ietf:params:oauth:grant-type:uma-ticket` grant.

## 8. Obtaining permissions (RPT)

POST to the token endpoint with `grant_type=urn:ietf:params:oauth:grant-type:uma-ticket`. Parameters:

| Param | Notes |
|---|---|
| `grant_type` | **Required** — `urn:ietf:params:oauth:grant-type:uma-ticket` |
| `ticket` | Optional — most recent permission ticket (UMA flow) |
| `claim_token` | Optional — BASE64 JSON of pushed claims |
| `claim_token_format` | Optional — `urn:ietf:params:oauth:token-type:jwt` (access token) or `https://openid.net/specs/openid-connect-core-1_0.html#IDToken` (ID token) |
| `rpt` | Optional — previously issued RPT for incremental authorization |
| `permission` | Optional — `RESOURCE_ID#SCOPE_ID` (repeatable). Forms: `Resource A#Scope A`, `Resource A#Scope A, Scope B, Scope C`, `Resource A`, `#Scope A` |
| `permission_resource_format` | Optional — `id` (default) or `uri` |
| `permission_resource_matching_uri` | Optional — boolean, path matching for `uri` format; default `false` |
| `audience` | Optional — resource server client id; **mandatory when `permission` is set** |
| `response_include_resource_name` | Optional — boolean; include resource names in RPT permissions |
| `response_permissions_limit` | Optional — integer N; with `rpt`, keep only last N permissions |
| `submit_request` | Optional — boolean; create permission requests (UMA, with `ticket`) |
| `response_mode` | Optional — `decision` (`{ "result": true }`) or `permissions` (`[ { "rsid": ..., "scopes": [...] } ]`); 403 if no permission maps |

Request access to specific resources/scopes:

```bash
curl -X POST \
  http://${host}:${port}/realms/${realm-name}/protocol/openid-connect/token \
  -H "Authorization: Bearer ${access_token}" \
  --data "grant_type=urn:ietf:params:oauth:grant-type:uma-ticket" \
  --data "audience={resource_server_client_id}" \
  --data "permission=Resource A#Scope A" \
  --data "permission=Resource B#Scope B"
```

UMA ticket exchange:

```bash
curl -X POST \
  http://${host}:${port}/realms/${realm-name}/protocol/openid-connect/token \
  -H "Authorization: Bearer ${access_token}" \
  --data "grant_type=urn:ietf:params:oauth:grant-type:uma-ticket" \
  --data "ticket=${permission_ticket}"
```

Success returns `{ "access_token": "${rpt}" }` (HTTP 200). Denial: HTTP 403 `{ "error": "access_denied", "error_description": "request_denied" }`.

**Client authentication to token endpoint**: Bearer Token (acts on behalf of a user — permissions evaluated in that user's context) or Client Credentials (`client_id`/`client_secret` or JWT — any supported method).

**Pushing claims (non-UMA)**: send `claim_token` (BASE64 JSON like `{ "organization": ["acme"] }`, values must be string arrays) + `claim_token_format` + client credentials + `audience`.

## 9. User-Managed Access (UMA 2.0)

RHBK is a UMA 2.0 compliant AS (privacy, party-to-party authorization, resource sharing). Flow: client hits a UMA-protected resource server without an RPT → RS returns `401` with a `WWW-Authenticate: UMA` header carrying `as_uri` and `ticket` → client exchanges the ticket at the token endpoint for an RPT.

```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: UMA realm="${realm-name}",
  as_uri="https://${host}:${port}/realms/${realm-name}",
  ticket="016f84e8-f9b9-11e0-bd6f-0021cc6004de"
```

**Submitting permission requests**: add `submit_request=true` to the ticket exchange → RHBK persists a permission request per denied resource; owners approve/deny in the Account Console.

**Account Console (My Resources)**: enable realm **User-Managed Access** (Realm Settings → toggle On). Owners manage owned resources, resources shared with them, people with access (Revoke / remove Permission), and share by username/email selecting scopes.

## 10. Protection API

UMA-compliant; **only resource servers** may call it; requires a **PAT** (OAuth2 access token with scope `uma_protection`). RHBK auto-creates a `uma_protection` role on the client's service account when a resource server is created.

Obtain a PAT (client_credentials):

```bash
curl -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'grant_type=client_credentials&client_id=${client_id}&client_secret=***' \
  "http://${host}:${port}/realms/${realm-name}/protocol/openid-connect/token"
```

### Resource registration — `/authz/protection/resource_set`

| Operation | Request |
|---|---|
| Create | `POST /resource_set` |
| Read | `GET /resource_set/{_id}` |
| Update | `PUT /resource_set/{_id}` |
| Delete | `DELETE /resource_set/{_id}` |
| List | `GET /resource_set` |

```bash
curl -v -X POST \
  http://${host}:${port}/realms/${realm-name}/authz/protection/resource_set \
  -H 'Authorization: Bearer '$pat -H 'Content-Type: application/json' \
  -d '{
    "name":"Tweedl Social Service",
    "type":"http://www.example.com/rsrcs/socialstream/140-compatible",
    "icon_uri":"http://www.example.com/icons/sharesocial.png",
    "resource_scopes":["read-public","post-updates","read-private","http://www.example.com/scopes/all"]
  }'
```

Set `owner` (username or user id) for a user-owned resource; add `"ownerManagedAccess": true` to allow Account Console management. Update example body uses `_id`, `name`, `resource_scopes`.

Query (GET `/resource_set?...`): `name=` (partial; add `exactName=true` for exact), `uri=`, `owner=`, `type=`, `scope=`. Use `first` / `max` to limit results.

### Permission tickets — `/authz/protection/permission`

```bash
curl -X POST \
  http://${host}:${port}/realms/${realm-name}/authz/protection/permission \
  -H 'Authorization: Bearer '$pat -H 'Content-Type: application/json' \
  -d '[ { "resource_id": "{resource_id}", "resource_scopes": ["view"],
         "claims": { "organization": ["acme"] } } ]'
```

Pushed `claims` become available to policies. Normally handled by the policy enforcer, not directly.

Non-UMA ticket endpoints (`/permission/ticket`, bearer = user access token): grant via `POST` (`resource`, `requester`, `granted`, `scopeName`); list via `GET` (params `scopeId`, `resourceId`, `owner`, `requester`, `granted`, `returnNames`, `first`, `max`); update via `PUT` (`id`, ...); delete via `DELETE /permission/ticket/{ticket_id}`.

### Policy API — `/authz/protection/uma-policy/{resource_id}`

Lets resource servers set permissions on behalf of users. Bearer token must represent user consent — obtained via Resource Owner Password Credentials grant or **Token Exchange** (exchange a public client's access token for one whose audience is the resource server).

```bash
curl -X POST \
  http://localhost:8180/realms/photoz/authz/protection/uma-policy/{resource_id} \
  -H 'Authorization: Bearer '$access_token -H 'Content-Type: application/json' \
  -d '{ "name": "Any people manager", "description": "Allow access to any people manager",
        "scopes": ["read"], "roles": ["people-manager"] }'
```

Access-control variants in the body: `roles`, `groups` (e.g. `["/Managers/People Managers"]`), `clients`, or `condition` (deployed JS, e.g. `my-deployed-script.js`) — combinable. Update (`PUT /uma-policy/{permission_id}`) full representation:

```json
{
  "id": "21eb3fed-02d7-4b5a-9102-29f3f09b6de2",
  "name": "Any people manager",
  "description": "Allow access to any people manager",
  "type": "uma",
  "scopes": ["album:view"],
  "logic": "POSITIVE",
  "decisionStrategy": "UNANIMOUS",
  "owner": "7e22131a-aa57-4f5f-b1db-6e82babcd322",
  "roles": ["user"]
}
```

Delete: `DELETE /uma-policy/{permission_id}`. Query (GET `/uma-policy?...`): `resource=`, `name=`, `scope=`, or none for all; `first` / `max` to limit.

## 11. Requesting Party Token (RPT)

RPT = JWT signed via JWS, built from the OAuth2 access token. Decoded payload:

```json
{
  "authorization": {
    "permissions": [
      { "resource_set_id": "d2fe9843-6462-4bfc-baba-b5787bb6e0e7",
        "resource_set_name": "Hello World Resource" }
    ]
  },
  "jti": "d6109a09-78fd-4998-bf89-95730dfd0892-1464906679405",
  "exp": 1464906971, "nbf": 0, "iat": 1464906671,
  "sub": "f1888f4d-5172-4359-be0c-af338505d86c",
  "typ": "kc_ett", "azp": "hello-world-authz-service"
}
```

### Introspecting an RPT

`POST .../protocol/openid-connect/token/introspect` with `token_type_hint=requesting_party_token` and `token=${RPT}`; authenticate the client (HTTP Basic shown, any supported method works):

```bash
curl -X POST \
  -H "Authorization: Basic ***" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'token_type_hint=requesting_party_token&token=${RPT}' \
  "http://localhost:8080/realms/hello-world-authz/protocol/openid-connect/token/introspect"
```

Active response:

```json
{
  "permissions": [
    { "resource_id": "90ccc6fc-b296-4cd1-881e-089e1ee15957",
      "resource_name": "Hello World Resource" }
  ],
  "exp": 1465314139, "nbf": 0, "iat": 1465313839,
  "aud": "hello-world-authz-service", "active": true
}
```

Inactive: `{ "active": false }`.

**Local validation** (no remote call): RPT is a JWT — validate the signature against the realm public key and check `exp`, `iat`, `aud`. This is what policy enforcers do. Offline note: the realm public key/JWKS must be reachable from the PEP within the air-gapped network.

## 12. Policy enforcers (PEP)

Built-in: **Java** policy enforcer (Java client apps) and **JavaScript** policy enforcer (apps secured by the RHBK JavaScript adapter).

### JavaScript integration

```bash
npm install keycloak-js   # stage on registry.example.internal for air-gapped installs
```

```javascript
import Keycloak from "keycloak-js";
import KeycloakAuthorization from "keycloak-js/authz";
const keycloak = new Keycloak({ url: "http://keycloak-server", realm: "my-realm", clientId: "my-app" });
const authorization = new KeycloakAuthorization(keycloak);
await keycloak.init();
```

Two features: obtain permissions via a permission ticket (UMA), or by sending resources/scopes directly.

**UMA response handling** — RS returns `401` + `WWW-Authenticate: UMA` (`as_uri`, `ticket`). Extract the ticket and:

```javascript
const authorizationRequest = { ticket };
authorization.authorize(authorizationRequest).then(
  (rpt) => { /* onGrant */ },
  () => { /* onDeny */ },
  () => { /* onError */ });
```

Callbacks: `onGrant` (1st arg, receives RPT), `onDeny` (2nd), `onError` (3rd). Retry the original request with the RPT as a bearer token after a 401.

**Entitlements** — obtain an RPT by resource server client_id:

```javascript
authorization.entitlement("my-resource-server-id").then((rpt) => { /* onGrant */ });
authorization.entitlement("my-resource-server", {
  permissions: [ { id: "Some Resource" } ]
}).then((rpt) => { /* onGrant */ });
```

**Authorization request object** (for `authorize` / `entitlement`):

| Property | Meaning |
|---|---|
| `permissions` | Array of `{ id, scopes: [...] }` |
| `metadata.response_include_resource_name` | Boolean; include resource names in RPT permissions |
| `metadata.response_permissions_limit` | Integer N; with `rpt`, keep last N permissions |
| `metadata.submit_request` | Boolean; create permission requests (UMA, with `ticket`) |

Retrieve the last RPT: `const rpt = authorization.rpt;`

_Source: Red Hat build of Keycloak 26.6 Authorization Services Guide (docs.redhat.com), distilled offline._
