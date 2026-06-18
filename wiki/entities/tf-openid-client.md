---
title: OpenID Connect clients (core) (Terraform)
type: entity
domain: keycloak
slug: tf-openid-client
summary: "The core `keycloak/keycloak` Terraform resources for declaring OIDC clients, their client scopes (default/optional), scope-based permissions, and service-account role assignments"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_scope.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_default_scopes.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_optional_scopes.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_permissions.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_service_account_role.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_service_account_realm_role.md (fetched 2026-06-16)
provenance: needs-review
tags: [clients, iac]
status: draft
updated: 2026-06-16
---

# OpenID Connect clients (core) (Terraform)

**The core `keycloak/keycloak` Terraform resources for declaring OIDC clients, their client scopes (default/optional), scope-based permissions, and service-account role assignments.** This page is **upstream/community (web-sourced)** reference distilled from the provider's own docs on GitHub — *not* Red Hat ground-truth. Only arguments actually seen in the fetched docs are documented; confirm against the pinned provider version before relying on any of them. It extends [[terraform-keycloak-iac]].

## Resources

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_openid_client` | An OIDC client in a realm (app that authenticates via Keycloak SSO) | `realm_id`, `client_id`, `access_type` | `access_type` is `CONFIDENTIAL`/`PUBLIC`/`BEARER-ONLY`. Optional: `client_secret` (auto-gen if omitted), write-only `client_secret_wo`/`client_secret_wo_version`, `standard_flow_enabled`, `valid_redirect_uris`, `service_accounts_enabled`, `extra_config`. Import: `{{realm_id}}/{{client_keycloak_id}}` (the client GUID). |
| `keycloak_openid_client_scope` | A reusable client scope (shared protocol + role mappings, conditional claims) | `realm_id`, `name` | Optional: `description`, `consent_screen_text`, `include_in_token_scope` (default `true`), `gui_order`, `extra_config`. Import: `{{realm_id}}/{{client_scope_id}}`. |
| `keycloak_openid_client_default_scopes` | A client's **default** client scopes (authoritative) | `realm_id`, `client_id`, `default_scopes` | Authoritative: removes manually-added scopes, re-adds manually-detached ones. Keycloak auto-assigns `profile`, `email`, `roles`, `web-origins` — exclude them and `plan` shows drift. Import not supported. |
| `keycloak_openid_client_optional_scopes` | A client's **optional** client scopes (authoritative) | `realm_id`, `client_id`, `optional_scopes` | Authoritative, same drift semantics. Keycloak auto-assigns `address`, `phone`, `offline_access`, `microprofile-jwt` as optional — omit them and they surface as drift on first apply. Import not supported. |
| `keycloak_openid_client_permissions` | Scope-based (fine-grained) permissions for an OIDC client | `realm_id`, `client_id` | Optional permission-scope blocks: `view_scope`, `manage_scope`, `configure_scope`, `map_roles_scope`, `map_roles_client_scope_scope`, `map_roles_composite_scope`, `token_exchange_scope` — each takes `policies`, `description`, `decision_strategy` (`UNANIMOUS`/`AFFIRMATIVE`/`CONSENSUS`). Requires the authorization (preview) feature; may need `depends_on`. |
| `keycloak_openid_client_service_account_role` | Assigns a **client** role to a client's service account | `realm_id`, `service_account_user_id`, `client_id`, `role` | Target client needs `service_accounts_enabled = true`. For realm roles use the realm-role resource. Import: `{{realmId}}/{{serviceAccountUserId}}/{{clientId}}/{{roleId}}`. |
| `keycloak_openid_client_service_account_realm_role` | Assigns a **realm** role to a client's service account | `realm_id`, `service_account_user_id`, `role` | Target client needs `service_accounts_enabled = true`. For client roles use the client-role resource above. Import: `{{realmId}}/{{serviceAccountUserId}}/{{roleId}}`. |

## Notable resources

**`keycloak_openid_client`** is the anchor. It declares an application as an OIDC client. The three required arguments are `realm_id`, `client_id`, and `access_type`. `access_type` selects the client confidentiality model — `CONFIDENTIAL` (server-side, has a secret), `PUBLIC` (browser-only, no secret), or `BEARER-ONLY` (services that only validate tokens). Flow toggles like `standard_flow_enabled` (Authorization Code grant) and `service_accounts_enabled` (Client Credentials grant) gate which [[oidc-grant-types]] the client can use; `valid_redirect_uris` constrains post-login/logout redirects. Secrets can be auto-generated, or supplied via the write-only `client_secret_wo`/`client_secret_wo_version` pair to keep them out of state and plan files.

```hcl
resource "keycloak_openid_client" "example" {
  realm_id    = "my-realm"
  client_id   = "test-client"
  access_type = "CONFIDENTIAL"
}
```

**`keycloak_openid_client_scope`** defines a reusable scope so multiple clients in a realm share the same protocol/role mappings and request claims conditionally on the OAuth scope parameter. It is then bound to clients via the two authoritative attachment resources.

**`keycloak_openid_client_default_scopes` / `keycloak_openid_client_optional_scopes`** are *authoritative* — they own the full set of default (resp. optional) scopes on a client and will reconcile away anything added out-of-band. The gotcha both share: Keycloak seeds new clients with built-in scopes (`profile`, `email`, `roles`, `web-origins` as default; `address`, `phone`, `offline_access`, `microprofile-jwt` as optional). If your config omits the built-ins, the very first `terraform plan` reports them as drift. Neither resource supports `import` — declare them as if the server is empty.

**`keycloak_openid_client_service_account_role` / `_service_account_realm_role`** wire a confidential client's service account into RBAC. Both require the target client to have `service_accounts_enabled = true`; the client-role variant additionally needs `client_id` (the role-providing client), while the realm-role variant takes only the role `role` name. This is the building block for the machine-to-machine pattern in [[client-authentication-methods]].

## RHBK / migration / air-gap notes

- **Upstream, not Red Hat ground-truth.** These docs come from the community `keycloak/terraform-provider-keycloak` repo. Resource availability and arguments track upstream OSS Keycloak and may lead an RHBK release by versions — a brand-new RHBK server feature can lag in the provider, and vice-versa. Confirm the resource exists at your pinned provider/server version before relying on it.
- **`mrparkers` → `keycloak/keycloak` source change.** The provider moved from `mrparkers/keycloak` to the official `keycloak/keycloak`. Configs still pointing at the old `source` hit provider-resolution errors on `init`; update `required_providers` and re-init. See [[terraform-keycloak-iac]].
- **`base_path = "/auth"` — RH-SSO vs RHBK.** Legacy **RH-SSO 7.x (Wildfly)** serves the Admin API under `/auth`, so set `base_path = "/auth"` (or `KEYCLOAK_BASE_PATH=/auth`) on the provider. **RHBK (Quarkus)** drops that context path — leave `base_path` empty. This is a provider-level setting; the client resources above are unaffected, but the whole config fails to reach the server if `base_path` is wrong.
- **Service accounts need write roles.** Driving these resources requires the provider's service-account client to hold `realm-management` write roles (e.g. `manage-clients`), not just the read-only `view-*` roles an audit account uses.
- **Air-gapped network.** With no internet, `terraform init` cannot reach the registry — the `keycloak/keycloak` provider must come from a **local filesystem/network mirror** (`terraform providers mirror`, then a `provider_installation { filesystem_mirror }` block), with the runner platform mirrored explicitly and integrity verified against `*_SHA256SUMS`. State holds client secrets — encrypt it.

## Contradictions / caveats

- Authoritative scope resources vs. the Keycloak-seeded built-in scopes is the most common source of phantom drift; include the built-ins in your config on first apply.
- `keycloak_openid_client_permissions` depends on the realm's authorization/preview feature being enabled and may require `depends_on` if realm-management authorization isn't on — this is upstream behavior, verify against your RHBK version.

## See also
- [[terraform-keycloak-iac]]
- [[oidc-grant-types]]
- [[client-authentication-methods]]
- [[oidc-client-best-practices]]
