# Keycloak Admin REST API — Offline Reference

_Distilled from the Keycloak Admin REST API reference (v26, keycloak.org/docs-api). Base path: `/admin/realms`._

## Authentication

Obtain a bearer token (built-in `admin-cli` client), then send `Authorization: Bearer <token>`.

```bash
# Token via password grant (master realm admin)
TOKEN=$(curl -s -X POST "$KC/realms/master/protocol/openid-connect/token" \
  -d grant_type=password -d client_id=admin-cli \
  -d username=admin -d password='***' | jq -r .access_token)

# ...or via a service-account client (preferred for automation)
TOKEN=$(curl -s -X POST "$KC/realms/master/protocol/openid-connect/token" \
  -d grant_type=client_credentials -d client_id=automation \
  -d client_secret='***' | jq -r .access_token)

curl -s -H "Authorization: Bearer $TOKEN" "$KC/admin/realms"
```

> **Path gotcha:** client/group/user paths use the **UUID** (`id`), *not* `clientId`/name. Look it up first, e.g. `GET /clients?clientId=web-portal` → `.[0].id`.

## Realms
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms` | List / create realm |
| GET/PUT/DELETE | `/admin/realms/{realm}` | Get / update / delete realm |

## Clients
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/clients` | List / create client |
| GET/PUT/DELETE | `/admin/realms/{realm}/clients/{uuid}` | Get / update / delete |
| GET/POST | `/admin/realms/{realm}/clients/{uuid}/client-secret` | Get / regenerate secret |
| GET | `/admin/realms/{realm}/clients/{uuid}/service-account-user` | Service-account user |
| GET | `/admin/realms/{realm}/clients/{uuid}/evaluate-scopes/generate-example-access-token` | Preview token |

## Client scopes
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/client-scopes` | List / create |
| GET/PUT/DELETE | `/admin/realms/{realm}/client-scopes/{id}` | Get / update / delete |

## Client initial access & registration
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/clients-initial-access` | List / create registration token |
| DELETE | `/admin/realms/{realm}/clients-initial-access/{id}` | Revoke |
| GET | `/admin/realms/{realm}/client-registration-policy/providers` | Registration policies |

## Users
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/users` | List / create |
| GET/PUT/DELETE | `/admin/realms/{realm}/users/{id}` | Get / update / delete |
| PUT | `/admin/realms/{realm}/users/{id}/reset-password` | Set password |
| GET/DELETE | `/admin/realms/{realm}/users/{id}/credentials[/{cid}]` | List / delete credential |
| GET | `/admin/realms/{realm}/users/{id}/sessions` | Active sessions |
| POST | `/admin/realms/{realm}/users/{id}/logout-sessions` | Log the user out |
| GET | `/admin/realms/{realm}/users/count` | User count |

## Components (user federation, key providers)
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/components` | List / create (LDAP, mappers, key providers) |
| GET/PUT/DELETE | `/admin/realms/{realm}/components/{id}` | Get / update / delete |

## Realm roles & client roles
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/roles` | List / create realm role |
| GET/PUT/DELETE | `/admin/realms/{realm}/roles/{name}` | Get / update / delete by name |
| GET/PUT/DELETE | `/admin/realms/{realm}/roles-by-id/{id}` | By id |
| GET/POST | `/admin/realms/{realm}/clients/{uuid}/roles` | List / create client role |

## Role mappings (users & groups)
| Method | Path | Purpose |
|---|---|---|
| GET | `/admin/realms/{realm}/users/{id}/role-mappings` | All effective mappings |
| GET/POST/DELETE | `/admin/realms/{realm}/users/{id}/role-mappings/realm` | Realm-role mapping |
| GET/POST/DELETE | `/admin/realms/{realm}/users/{id}/role-mappings/clients/{uuid}` | Client-role mapping |
| GET/POST/DELETE | `/admin/realms/{realm}/groups/{id}/role-mappings/realm` | Group realm-role mapping |
| GET/POST/DELETE | `/admin/realms/{realm}/groups/{id}/role-mappings/clients/{uuid}` | Group client-role mapping |

## Groups
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/groups` | List / create (use `?search=`/`?q=`) |
| GET/PUT/DELETE | `/admin/realms/{realm}/groups/{id}` | Get / update / delete |
| GET | `/admin/realms/{realm}/groups/{id}/members` | Members |
| PUT/DELETE | `/admin/realms/{realm}/users/{uid}/groups/{gid}` | Add / remove user |

## Identity providers
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/identity-provider/instances` | List / create |
| GET/PUT/DELETE | `/admin/realms/{realm}/identity-provider/instances/{alias}` | Get / update / delete |
| GET | `/admin/realms/{realm}/identity-provider/providers` | Available provider types |

## Protocol mappers
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/clients/{uuid}/protocol-mappers/models` | List / create on client |
| GET/PUT/DELETE | `/admin/realms/{realm}/clients/{uuid}/protocol-mappers/models/{id}` | Get / update / delete |
| GET/POST | `/admin/realms/{realm}/client-scopes/{id}/protocol-mappers/models` | On a client scope |

## Authentication management
| Method | Path | Purpose |
|---|---|---|
| GET/POST | `/admin/realms/{realm}/authentication/flows` | List / create flows |
| POST | `/admin/realms/{realm}/authentication/flows/{alias}/copy` | Copy a built-in flow |
| GET/PUT | `/admin/realms/{realm}/authentication/flows/{alias}/executions` | List / reorder executions |
| GET/POST/PUT/DELETE | `/admin/realms/{realm}/authentication/required-actions[/{alias}]` | Required actions |
| GET | `/admin/realms/{realm}/authentication/authenticator-providers` | Available authenticators |

## Sessions, events, keys, brute force
| Method | Path | Purpose |
|---|---|---|
| GET | `/admin/realms/{realm}/clients/{uuid}/user-sessions` | Client sessions |
| GET/DELETE | `/admin/realms/{realm}/events` | Login events / clear |
| GET/PUT | `/admin/realms/{realm}/events/config` | Events config |
| GET/DELETE | `/admin/realms/{realm}/admin-events` | Admin events / clear |
| GET | `/admin/realms/{realm}/keys` | Realm key metadata |
| GET/DELETE | `/admin/realms/{realm}/attack-detection/brute-force/users/{id}` | Lockout status / clear |
| GET/POST | `/admin/realms/{realm}/organizations` | Organizations (see release notes for status) |

## Common query parameters
| Param | Meaning |
|---|---|
| `first` / `max` | Pagination offset / page size (default max 100) |
| `search` | Substring match (users: username/email/first/last) |
| `q` | Attribute query, e.g. `q=org_id:acme` |
| `exact` | Exact-match for name searches |
| `briefRepresentation` | Minimal payload (default `true` on lists) — set `false` for attributes |
| `enabled` | Filter by enabled state |

## Key representation objects (notable fields)

**RealmRepresentation** — `realm`, `enabled`, `displayName`, `sslRequired`, `accessTokenLifespan`, `ssoSessionIdleTimeout`, `ssoSessionMaxLifespan`, `passwordPolicy`, `bruteForceProtected`, `smtpServer`, `eventsEnabled`, `adminEventsEnabled`, `defaultSignatureAlgorithm`.

**ClientRepresentation** — `id` (UUID), `clientId`, `enabled`, `publicClient`, `standardFlowEnabled`, `serviceAccountsEnabled`, `redirectUris`, `webOrigins`, `protocol` (`openid-connect`|`saml`), `authorizationServicesEnabled`, `attributes` (e.g. `pkce.code.challenge.method=S256`), `defaultClientScopes`, `optionalClientScopes`, `protocolMappers`.

**UserRepresentation** — `id`, `username`, `email`, `emailVerified`, `firstName`, `lastName`, `enabled`, `attributes` (`{key:[values]}`), `credentials`, `requiredActions`, `realmRoles`, `clientRoles`, `groups`, `federatedIdentities`.

**RoleRepresentation** — `id`, `name`, `description`, `composite`, `composites{realm[],client{uuid:[]}}`, `clientRole`, `containerId`, `attributes`.

**GroupRepresentation** — `id`, `name`, `path` (`/parent/child`), `parentId`, `attributes`, `realmRoles`, `clientRoles`, `subGroups`.

**ProtocolMapperRepresentation** — `name`, `protocol`, `protocolMapper`, `config{...}`. Common OIDC mapper types:
`oidc-usermodel-attribute-mapper`, `oidc-usermodel-property-mapper`, `oidc-hardcoded-claim-mapper`, `oidc-full-name-mapper`, `oidc-audience-mapper`, `oidc-usermodel-realm-role-mapper`, `oidc-usermodel-client-role-mapper`, `oidc-group-membership-mapper`.

**IdentityProviderRepresentation** — `alias`, `providerId` (`oidc`|`saml`|`google`…), `enabled`, `trustEmail`, `storeToken`, `firstBrokerLoginFlowAlias`, `syncMode` (`IMPORT`|`LEGACY`|`FORCE`), `config{clientId,clientSecret,authorizationUrl,tokenUrl,userInfoUrl}`, `mappers`.

## Status codes
`200` ok · `201` created (new resource URL in `Location` header) · `204` no content · `400` bad input · `401/403` auth/permission · `404` not found · `409` conflict (duplicate). Errors: `{"error":"...","error_description":"..."}`.


<!-- ───────── deepened from Keycloak 26.6.3 docs ───────── -->

---

## Organizations

> Requires the Organizations feature to be enabled in the realm. All paths are under `/admin/realms/{realm}/organizations`. Introduced in Keycloak 24; present in 26.6.3.

### Organization collection

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations` | List organizations (paginated); filter via `search`, `exact`, `q`, `first`, `max`, `briefRepresentation` |
| `POST` | `/admin/realms/{realm}/organizations` | Create a new organization (`OrganizationRepresentation` body) |
| `GET` | `/admin/realms/{realm}/organizations/count` | Count organizations; filter via `search`, `exact`, `q` |
| `GET` | `/admin/realms/{realm}/organizations/members/{member-id}/organizations` | List all organizations a given user belongs to |

### Individual organization

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations/{org-id}` | Fetch full organization representation |
| `PUT` | `/admin/realms/{realm}/organizations/{org-id}` | Replace organization (`OrganizationRepresentation` body) |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}` | Delete organization and all managed members |

### Organization members

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/members` | List members; filter via `search`, `exact`, `first`, `max`, `membershipType` |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/members` | Add existing user by UUID (plain string body) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/members/count` | Count members |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/members/invite-existing-user` | Send invitation to an existing user by `id` (form-encoded) |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/members/invite-user` | Send invitation or registration link by `email` (form-encoded; `firstName`/`lastName` optional) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/members/{member-id}` | Fetch one member's representation |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}/members/{member-id}` | Remove member (deletes user if membership is managed) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/members/{member-id}/groups` | List organization groups the member belongs to |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/members/{member-id}/organizations` | List all organizations the member belongs to |

### Organization identity providers

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/identity-providers` | List all IdPs associated with the organization |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/identity-providers` | Associate an existing IdP by id or alias (plain string body) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/identity-providers/{alias}` | Fetch one associated IdP by alias |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}/identity-providers/{alias}` | Disassociate IdP (provider itself is not deleted) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/identity-providers/{alias}/groups` | List organization groups available for IdP mappers |

### Organization invitations

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/invitations` | List pending invitations; filter via `email`, `first`, `max` |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}/invitations/{id}` | Revoke a pending invitation |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/invitations/{id}/resend` | Resend an invitation e-mail |

### Organization groups

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/groups` | List top-level groups (or search); supports `search`, `q`, `exact`, `first`, `max`, `briefRepresentation`, `populateHierarchy`, `subGroupsCount` |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/groups` | Create a top-level group (or move existing group if `id` provided) |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/groups/group-by-path/{path}` | Fetch group by slash-separated path |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}` | Fetch group by id |
| `PUT` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}` | Update group name, description, attributes |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}` | Delete group and all subgroups |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}/children` | List subgroups (paginated) |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}/children` | Create or move subgroup |
| `GET` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}/members` | List members of the group |
| `POST` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}/members/{userId}` | Add member to group (must already be an org member) |
| `DELETE` | `/admin/realms/{realm}/organizations/{org-id}/groups/{group-id}/members/{userId}` | Remove member from group (user stays in org) |

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# List organizations
curl "${auth[@]}" "$KC/admin/realms/$REALM/organizations?first=0&max=20"

# Create organization
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' \
  -d '{"name":"acme","alias":"acme","enabled":true,"domains":[{"name":"acme.example.internal","verified":false}]}' \
  "$KC/admin/realms/$REALM/organizations"

# Add member (user UUID as plain string body)
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' \
  -d '"***user-uuid***"' \
  "$KC/admin/realms/$REALM/organizations/***org-id***/members"

# Associate IdP
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' \
  -d '"saml-idp-alias"' \
  "$KC/admin/realms/$REALM/organizations/***org-id***/identity-providers"
```

---

## Client Policies and Client Profiles

Realm-level policy engine (introduced Keycloak 19+). Policies enforce profile conditions on client operations (registration, update, token request). Both endpoints sit under the `Realms Admin` tag.

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/client-policies/policies` | Fetch `ClientPoliciesRepresentation`; `include-global-policies` (bool query) also returns built-in policies |
| `PUT` | `/admin/realms/{realm}/client-policies/policies` | Replace all realm policies (`ClientPoliciesRepresentation` body); overwrites existing set |
| `GET` | `/admin/realms/{realm}/client-policies/profiles` | Fetch `ClientProfilesRepresentation`; `include-global-profiles` (bool query) also returns built-in profiles |
| `PUT` | `/admin/realms/{realm}/client-policies/profiles` | Replace all realm profiles (`ClientProfilesRepresentation` body) |

> Both `PUT` operations perform a full replacement — merge the current GET response with your changes before submitting.

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# Read current policies (including globals)
curl "${auth[@]}" "$KC/admin/realms/$REALM/client-policies/policies?include-global-policies=true"

# Update profiles (read-modify-write pattern)
CURRENT=$(curl -s "${auth[@]}" "$KC/admin/realms/$REALM/client-policies/profiles")
UPDATED=$(echo "$CURRENT" | jq '.profiles += [{"name":"my-profile","description":"","executors":[]}]')
curl "${auth[@]}" -X PUT -H 'Content-Type: application/json' \
  -d "$UPDATED" "$KC/admin/realms/$REALM/client-policies/profiles"
```

---

## Authentication — Required Actions

Required actions are mapped to aliases that match the provider's `providerId`. The `config` sub-resource stores per-action configuration, while `config-description` exposes the schema of configurable properties.

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/authentication/required-actions` | List all registered required-action providers |
| `GET` | `/admin/realms/{realm}/authentication/unregistered-required-actions` | List providers available in classpath but not yet registered |
| `POST` | `/admin/realms/{realm}/authentication/register-required-action` | Register an unregistered action; body is `{"providerId":"<id>","name":"<display name>"}` |
| `GET` | `/admin/realms/{realm}/authentication/required-actions/{alias}` | Fetch `RequiredActionProviderRepresentation` for alias |
| `PUT` | `/admin/realms/{realm}/authentication/required-actions/{alias}` | Update action (enable/disable, set default, change `priority`) |
| `DELETE` | `/admin/realms/{realm}/authentication/required-actions/{alias}` | Unregister action |
| `POST` | `/admin/realms/{realm}/authentication/required-actions/{alias}/raise-priority` | Increment priority by one position |
| `POST` | `/admin/realms/{realm}/authentication/required-actions/{alias}/lower-priority` | Decrement priority by one position |
| `GET` | `/admin/realms/{realm}/authentication/required-actions/{alias}/config-description` | Fetch `RequiredActionConfigInfoRepresentation` (property schema) |
| `GET` | `/admin/realms/{realm}/authentication/required-actions/{alias}/config` | Fetch `RequiredActionConfigRepresentation` (current config values) |
| `PUT` | `/admin/realms/{realm}/authentication/required-actions/{alias}/config` | Set config (`{"config":{"key":"value"}}`) |
| `DELETE` | `/admin/realms/{realm}/authentication/required-actions/{alias}/config` | Clear config back to defaults |

**`RequiredActionProviderRepresentation` fields:** `alias`, `name`, `providerId`, `enabled` (bool), `defaultAction` (bool), `priority` (int), `config` (map).

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# Disable an action
curl "${auth[@]}" -X PUT -H 'Content-Type: application/json' \
  -d '{"alias":"VERIFY_EMAIL","name":"Verify Email","providerId":"VERIFY_EMAIL","enabled":false,"defaultAction":false,"priority":50}' \
  "$KC/admin/realms/$REALM/authentication/required-actions/VERIFY_EMAIL"

# Register a provider from classpath
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' \
  -d '{"providerId":"my-custom-action","name":"My Custom Action"}' \
  "$KC/admin/realms/$REALM/authentication/register-required-action"
```

---

## Partial Export and Partial Import

Both endpoints operate on an existing realm. Export returns a `RealmRepresentation` JSON. Import accepts a JSON file (binary string) and returns a result object. Both require the caller to hold `manage-realm` (or master-realm admin) permissions; `403 Forbidden` otherwise.

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/admin/realms/{realm}/partial-export` | Export realm data; query params control scope (see table below) |
| `POST` | `/admin/realms/{realm}/partialImport` | Import realm data from a JSON file; returns conflict/import summary |

**`partial-export` query parameters:**

| Option | Purpose | Example |
|--------|---------|---------|
| `exportClients` | Include client definitions in the export | `?exportClients=true` |
| `exportGroupsAndRoles` | Include groups and roles | `?exportGroupsAndRoles=true` |

**`partialImport` response codes:** `200 OK` (success), `403 Forbidden`, `409 Conflict` (duplicate resource when policy is `FAIL`).

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# Export realm including clients, groups, roles
curl "${auth[@]}" -X POST \
  "$KC/admin/realms/$REALM/partial-export?exportClients=true&exportGroupsAndRoles=true" \
  -o realm-export.json

# Import back
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' \
  -d @realm-export.json \
  "$KC/admin/realms/$REALM/partialImport"
```

---

## User — Configured Storage Credential Types

Returns credential type strings (e.g. `"password"`, `"otp"`) that the backing user-storage provider supports for a specific user. Always returns an empty list for users stored in the local Keycloak database.

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/users/{user-id}/configured-user-storage-credential-types` | List credential types offered by the user's storage provider |

**Response:** `200 OK` — JSON array of strings, e.g. `["password","otp"]`. `403 Forbidden` if insufficient privileges.

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

curl "${auth[@]}" \
  "$KC/admin/realms/$REALM/users/***user-uuid***/configured-user-storage-credential-types"
```

---

## Attack Detection — Clear Brute-Force State

The brute-force detector tracks per-user failure counts and can temporarily lock accounts. The `DELETE` on the collection path clears all users at once; the per-user path targets one account.

| Method | Path | Purpose |
|--------|------|---------|
| `DELETE` | `/admin/realms/{realm}/attack-detection/brute-force/users` | Clear login-failure state for **all** users in the realm (releases all temporarily disabled accounts) |
| `GET` | `/admin/realms/{realm}/attack-detection/brute-force/users/{userId}` | Fetch brute-force status object for a single user |
| `DELETE` | `/admin/realms/{realm}/attack-detection/brute-force/users/{userId}` | Clear login-failure state for a single user |

**Both `DELETE` operations return `204 No Content` on success.**

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# Release all locked accounts
curl "${auth[@]}" -X DELETE \
  "$KC/admin/realms/$REALM/attack-detection/brute-force/users"

# Check one user's brute-force status
curl "${auth[@]}" \
  "$KC/admin/realms/$REALM/attack-detection/brute-force/users/***user-uuid***"

# Clear one user
curl "${auth[@]}" -X DELETE \
  "$KC/admin/realms/$REALM/attack-detection/brute-force/users/***user-uuid***"
```

---

## Realm Key Management via Components

Cryptographic key providers are managed as `Component` resources. The SPI type for key providers is `org.keycloak.keys.KeyProvider` (resolved at runtime as `KeyProvider.class.getName()`). Built-in `providerId` values include `rsa-generated`, `rsa`, `rsa-enc-generated`, `ec-generated`, `hmac-generated`, `aes-generated`, and `java-keystore`.

### Component CRUD

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/admin/realms/{realm}/components` | List components; filter by `name`, `parent`, `providerId`, `type` |
| `POST` | `/admin/realms/{realm}/components` | Create a component (`ComponentRepresentation` body) |
| `GET` | `/admin/realms/{realm}/components/{id}` | Fetch one component |
| `PUT` | `/admin/realms/{realm}/components/{id}` | Replace one component |
| `DELETE` | `/admin/realms/{realm}/components/{id}` | Delete one component |
| `GET` | `/admin/realms/{realm}/components/{id}/sub-component-types` | List sub-component types available for this parent component |

**`ComponentRepresentation` fields:** `id`, `name`, `providerId`, `providerType`, `parentId`, `subType`, `config` (multivalued map).

**Key query parameters for `GET /components`:**

| Option | Purpose | Example |
|--------|---------|---------|
| `type` | Filter by SPI interface; use `org.keycloak.keys.KeyProvider` for key providers | `?type=org.keycloak.keys.KeyProvider` |
| `parent` | Filter to components belonging to a specific parent id (default: realm id) | `?parent=***realm-uuid***` |
| `providerId` | Filter to a specific provider implementation | `?providerId=rsa-generated` |

```bash
KC=https://keycloak.example.internal
REALM=corp
auth=(-H "Authorization: Bearer $TOKEN")

# List all key providers for the realm
curl "${auth[@]}" \
  "$KC/admin/realms/$REALM/components?type=org.keycloak.keys.KeyProvider"

# Add a generated RSA key provider
curl "${auth[@]}" -X POST -H 'Content-Type: application/json' -d '{
  "name": "rsa-2048",
  "providerId": "rsa-generated",
  "providerType": "org.keycloak.keys.KeyProvider",
  "config": {
    "keySize": ["2048"],
    "active": ["true"],
    "enabled": ["true"],
    "priority": ["100"]
  }
}' "$KC/admin/realms/$REALM/components"

# Delete a key provider
curl "${auth[@]}" -X DELETE \
  "$KC/admin/realms/$REALM/components/***component-id***"
```

> **Source:** Keycloak 26.6.3 Admin REST API — https://www.keycloak.org/docs-api/26.6.3/rest-api/
