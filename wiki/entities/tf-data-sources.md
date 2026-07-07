---
title: Data sources (read existing Keycloak objects) (Terraform)
type: entity
domain: keycloak
slug: tf-data-sources
summary: "Terraform `data` blocks in the `keycloak/keycloak` provider that *read* existing Keycloak/RHBK objects (realms, clients, roles, users, groups, scopes, auth flows, keys) so you can reference their IDs and attributes without managing their lifecycle."
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/authentication_execution.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/authentication_flow.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/authentication_subflow.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/client_description_converter.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/generic_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/group.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/openid_client.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/openid_client_authorization_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/openid_client_scope.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/openid_client_service_account_user.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/organization.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/realm.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/realm_keys.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/role.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/saml_client.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/saml_client_installation_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/saml_client_scope.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/user.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/user_realm_roles.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/data-sources/workflow.md (fetched 2026-06-16)
provenance_extracted: 19
provenance_inferred: 4
provenance_ambiguous: 0
tags: [iac]
status: draft
updated: 2026-07-02
---

# Data sources (read existing Keycloak objects) (Terraform)

**Terraform `data` blocks in the `keycloak/keycloak` provider that *read* existing Keycloak/RHBK objects (realms, clients, roles, users, groups, scopes, auth flows, keys) so you can reference their IDs and attributes without managing their lifecycle.**

> **Upstream / OSS — web-sourced.** Everything below comes from the community `keycloak/terraform-provider-keycloak` docs on GitHub (`main` branch, fetched 2026-06-16), **not** Red Hat ground-truth. RHBK is downstream of OSS Keycloak, so a brand-new data source or attribute may lag the RHBK release you run — confirm against the provider version you have pinned. Only the arguments actually seen in the fetched docs are documented here.

Data sources are read-only: they look up an object that already exists (perhaps created outside Terraform, or auto-created by Keycloak) and expose its `id`/attributes for use by `resource` blocks. They are also the backbone of **drift detection** workflows where you read live state and compare. All of the below are invoked as `data "keycloak_<name>" "..." { ... }`.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages (reads) | Key required args | Notes |
|---|---|---|---|
| `keycloak_authentication_execution` | An authentication execution within a flow | `realm_id`, `parent_flow_alias`, `provider_id` | Exports `id`, `priority`. `provider_id` is the (former "authenticator") provider name; discoverable via browser dev tools. |
| `keycloak_authentication_flow` | An authentication flow | `realm_id`, `alias` | Exports `id` for use by other resources. |
| `keycloak_authentication_subflow` | A nested subflow inside a parent flow | `realm_id`, `parent_flow_alias` | Specify exactly one of `id` or `alias` (mutually exclusive). Exports `id`, `alias`, `provider_id`, `description`, `requirement`, `priority` (priority is Keycloak 25+). |
| `keycloak_client_description_converter` | Converts a client description (e.g. SAML metadata) into client config via the ClientDescriptionConverter API | `realm_id`, `body` | Exports a union of `keycloak_openid_client` + `keycloak_saml_client` attributes (ClientRepresentation). Example converts a SAML EntityDescriptor XML. |
| `keycloak_generic_protocol_mapper` | A protocol mapper on a client or client scope (for adopting auto-created mappers) | `realm_id`, `name`, and one of `client_id` / `client_scope_id` | `client_id` and `client_scope_id` conflict; exactly one required. Exports `id`, `protocol`, `protocol_mapper`, `config`. |
| `keycloak_group` | A group | `realm_id`, `name` | Returns first match if name is non-unique. Optional `organization_id` (requires Keycloak 26.6.0+). Exports `id`. Pairs with `keycloak_group_roles`. |
| `keycloak_openid_client` | An OpenID Connect client | `realm_id`, `client_id` | `client_id` is the human client id, not the internal UUID. See the resource docs for full exported attributes (`id`, etc.). |
| `keycloak_openid_client_authorization_policy` | A policy/permission on an authorization-enabled OIDC client | `realm_id`, `name`, `resource_server_id` | Exports `decision_strategy`, `owner`, `logic`, `policies`, `resources`, `scopes`, `type`. Used to adopt the default permission created when authz is enabled. |
| `keycloak_openid_client_scope` | An OpenID client scope | `realm_id`, `name` | Exports attributes per the resource docs (notably `id`). Example fetches `offline_access`. |
| `keycloak_openid_client_service_account_user` | The service-account user auto-created for a service-accounts-enabled OIDC client | `realm_id`, `client_id` | Exports `username`, `email`, `first_name`, `last_name`, `enabled`, `attributes`; `federated_identity` is always null. Used to assign roles via `keycloak_user_roles`. |
| `keycloak_organization` | An organization | `realm`, `name` | Note the arg is `realm` (name), not `realm_id`. Exports attributes per the resource docs (e.g. `id`). |
| `keycloak_realm` | A realm | `realm` | Arg is `realm` (the realm name). Exports realm attributes (e.g. `id`) per the resource docs. |
| `keycloak_realm_keys` | The realm's cryptographic keys, with optional filtering | `realm_id` | Optional filters `algorithms`, `status` (`ACTIVE`/`DISABLED`/`PASSIVE`); keys must match all filters. Exports `keys[]` with `algorithm`, `certificate`, `provider_id`, `provider_priority`, `kid`, `public_key`, `status`, `type`. Errors if no match. |
| `keycloak_role` | A realm role or client role | `realm_id`, `name` | Optional `client_id` makes it a client role. Exports `id`, `description`. Example fetches built-in `offline_access`. |
| `keycloak_saml_client` | A SAML client | `realm_id`, `client_id` | `client_id` is the human id, not the UUID. Exported attributes per the resource docs. |
| `keycloak_saml_client_installation_provider` | The installation/descriptor document for a SAML client | `realm_id`, `client_id`, `provider_id` | `provider_id` e.g. `saml-idp-descriptor`, `keycloak-saml`, `saml-sp-descriptor`. Exports `id` (hash) and `value` (the document). Used to feed metadata to cloud IdPs (e.g. AWS IAM). |
| `keycloak_saml_client_scope` | A SAML client scope | `realm_id`, `name` | Exports same attributes as the resource. Example feeds it to `keycloak_saml_client_default_scopes`. |
| `keycloak_user` | A user | `realm_id`, `username` | Exports `id`, `enabled`, `email`, `email_verified`, `first_name`, `last_name`, `attributes`, `federated_identity` (with `identity_provider`, `user_id`, `user_name`). |
| `keycloak_user_realm_roles` | The realm roles assigned to a user | `realm_id`, `user_id` | Exports `role_names` (computed list). |
| `keycloak_workflow` | A workflow | `realm`, `name` | Arg is `realm` (name). Exports attributes per the resource docs. Example fetches `onboarding-new-users`. |

## Notable resources

**`keycloak_realm`** is the usual root of a data-source graph: nearly every other lookup wants a `realm_id`, and you get it by reading the realm by name first. Note the argument is `realm` (the realm name), and it exports the internal `id` used downstream.

```hcl
data "keycloak_realm" "realm" {
  realm = "my-realm"
}

data "keycloak_role" "offline_access" {
  realm_id = data.keycloak_realm.realm.id
  name     = "offline_access"
}
```

**`keycloak_openid_client`** reads an OIDC client by its human `client_id` (not the internal UUID) and is the standard way to reach a client created elsewhere — e.g. the built-in `realm-management` client — so you can then pull a role out of it:

```hcl
data "keycloak_openid_client" "realm_management" {
  realm_id  = data.keycloak_realm.realm.id
  client_id = "realm-management"
}

data "keycloak_role" "admin" {
  realm_id  = data.keycloak_realm.realm.id
  client_id = data.keycloak_openid_client.realm_management.id
  name      = "realm-admin"
}
```

**`keycloak_openid_client_service_account_user`** is the idiomatic bridge for machine-to-machine setups: when a client has service accounts enabled Keycloak auto-creates a hidden user, and this data source surfaces it so you can grant roles to it via `keycloak_user_roles`. This is directly relevant to the Terraform service-account pattern described on [[terraform-keycloak-iac]].

**`keycloak_realm_keys`** is the one to reach for in audit/drift work — it enumerates a realm's signing/encryption keys with `status` and `algorithms` filters, exposing `kid`, `public_key`, `certificate` and `provider_priority`, which lets IaC assert on the active signing key without hard-coding it.

## RHBK / migration / air-gap notes (inferred — general Terraform/RHBK migration
knowledge, not covered by this page's cited sources, which document only data-source
arguments; verify against [[terraform-keycloak-iac]] and the provider changelog.)

- **`mrparkers` → `keycloak/keycloak` source change.** These data sources only exist under the official `keycloak/keycloak` provider. Configs still pointing `required_providers` at the legacy `mrparkers/keycloak` must be switched and re-`init`ed. See [[terraform-keycloak-iac]].
- **`base_path = "/auth"` (RH-SSO vs RHBK).** Data sources hit the Admin REST API through the provider's configured endpoint, so they inherit the context-path difference: legacy **RH-SSO 7.x (Wildfly)** needs `base_path = "/auth"`; **RHBK (Quarkus)** must leave it empty. A wrong `base_path` makes every data-source lookup 404, not just resources.
- **Version-sensitive lookups.** `keycloak_group`'s `organization_id` argument requires **Keycloak 26.6.0+**; `keycloak_authentication_subflow`'s `priority` export is **Keycloak 25+**. `keycloak_organization` and `keycloak_workflow` read newer Keycloak constructs — confirm the feature exists on your RHBK build before relying on them. Argument *naming* is also inconsistent: `keycloak_realm`, `keycloak_organization`, and `keycloak_workflow` take `realm` (the name), while most others take `realm_id`.
- **Air-gapped network.** Reading data sources still requires the provider plugin, which `terraform init` normally pulls from the registry. On a disconnected net the provider must come from a **local filesystem/network mirror** (`terraform providers mirror`, `provider_installation { filesystem_mirror }`), verified against `*_SHA256SUMS`. Data-source reads themselves only need network reachability to the RHBK Admin API host, not the internet.
- **Drift detection.** Because these blocks read live server state read-only, they are useful for comparing declared desired-state against the running RHBK during an audit — a non-empty `plan` against data-sourced values signals out-of-band change.

## Contradictions / caveats

- This page is **upstream/community (web-sourced)**, not a Red Hat support statement. Several docs ("see the resource docs for exported attributes") do not enumerate every attribute on the data-source page itself; only attributes explicitly listed in the fetched pages are reproduced here, and the rest are deferred to the corresponding resource page rather than invented.
- All fetches succeeded; no resource above is undocumented.

## See also
- [[realm-resource-access]] — realm-management roles these data sources read back
- [[terraform-keycloak-iac]]
