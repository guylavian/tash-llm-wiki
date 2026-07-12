---
title: Roles, groups, users & role mappers (Terraform)
type: entity
domain: keycloak
slug: tf-roles-groups-users
summary: "The assignment resources are where the \"authoritative vs partial\" model matters."
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/role.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/group.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/group_memberships.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/group_permissions.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/group_roles.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/user.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/user_groups.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/user_roles.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/users_permissions.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/generic_client_role_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/generic_role_mapper.md (fetched 2026-06-16)
provenance_extracted: 18
provenance_inferred: 1
provenance_ambiguous: 0
tags: [iac, users]
status: draft
updated: 2026-07-02
---

# Roles, groups, users & role mappers (Terraform)

**The `keycloak/keycloak` Terraform resources that declaratively manage realm/client
roles, groups and their hierarchy, users, and the role/group/user assignments and
scope mappings that bind them together.** This page is **upstream/community
(web-sourced)** reference distilled from the provider's own `docs/resources/*.md`,
**not** Red Hat ground-truth — only arguments actually seen in those docs are
documented below; confirm against the provider docs for the version you pin.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_role` | Realm or client roles (privileges mapped to users/groups) | `realm_id`, `name` | `client_id` makes it a client role; `composite_roles` for composites; `attributes` (multivalue via `##`); `import = true` adopts an existing role. Import: `my-realm/<role-uuid>`. |
| `keycloak_group` | Groups (logical wrapper for users; shared attrs/roles/claims) | `realm_id`, `name` | `parent_id` for nested hierarchy; `organization_id` (Keycloak 26.6.0+); `attributes` (`##` multivalue); computed `path`. Do **not** manage LDAP/AD-federated groups. Import: `{{realm_id}}/{{group_id}}`. |
| `keycloak_group_memberships` | Membership of a group by **username** (authoritative) | `realm_id`, `group_id`, `members` | Authoritative: removes manually-added members, re-adds removed ones. Incompatible with `keycloak_default_groups` and federated members; paginates 50/refresh. **No import** — create new. Non-exclusive alternative: `keycloak_user_groups`. |
| `keycloak_group_permissions` | Fine-grained scope permissions for one group | `realm_id`, `group_id` | Preview feature (`admin_fine_grained_authz` profile). Scopes: `view_scope`, `manage_scope`, `view_members_scope`, `manage_members_scope`, `manage_membership_scope`, each with `policies`/`description`/`decision_strategy`. Computed `enabled`, `authorization_resource_server_id`. |
| `keycloak_group_roles` | Roles assigned to a group | `realm_id`, `group_id`, `role_ids` | `exhaustive` (default `true`) = authoritative; set false to let multiple resources manage one group. Composite+constituent assignment may show non-empty plan. Import: `realm_id/group_id`. |
| `keycloak_user` | Users within a realm | `realm_id`, `username` | Docs note it exists mainly for acceptance tests — prefer federation. Optional: `enabled` (default true), `email`, `first_name`, `last_name`, `initial_password` (+ temporary flag), `attributes` (`##`), `federated_identity`, `import`. Import: `{{realm_id}}/{{user_id}}`. |
| `keycloak_user_groups` | A user's group memberships (by group ID) | `realm_id`, `user_id`, `group_ids` | `exhaustive` (default `true`) = authoritative; false allows multiple resources per user (partial). **No import** — create new. |
| `keycloak_user_roles` | Roles assigned to a user | `realm_id`, `user_id`, `role_ids` | `exhaustive` (default `true`) = authoritative; false for partial/multi-resource. Composite+constituent may show non-empty plan. Import: `{{realm_id}}/{{user_id}}`. |
| `keycloak_users_permissions` | Realm-wide fine-grained permissions for all users | `realm_id` | Preview (`-Dkeycloak.profile.feature.admin_fine_grained_authz=enabled`). Create **once per realm**. Scopes: `view_scope`, `manage_scope`, `map_roles_scope`, `manage_group_membership_scope`, `impersonate_scope`, `user_impersonated_scope` (each `policies`/`description`/`decision_strategy`). Computed `enabled`, `authorization_resource_server_id`. |
| `keycloak_generic_client_role_mapper` | Client/client-scope scope mapping (a role) | `realm_id`, `role_id`, and either `client_id` **or** `client_scope_id` | **Deprecated** — use `keycloak_generic_role_mapper`. Limits roles in tokens when `full_scope_allowed` is disabled. `client_id`/`client_scope_id` mutually exclusive. |
| `keycloak_generic_role_mapper` | Role mappings for clients or client scopes | `realm_id`, `role_id`, and either `client_id` **or** `client_scope_id` | Controls which roles appear in access tokens / SAML assertions when `full_scope_allowed` is disabled. `client_id`/`client_scope_id` mutually exclusive. Maps realm or client roles onto clients or client scopes. |

## Notable resources

**`keycloak_role`** is the foundation: it defines a realm role (or a client role
when `client_id` is set) and can compose other roles via `composite_roles`.

```hcl
resource "keycloak_role" "example" {
  realm_id    = keycloak_realm.realm.id
  name        = "my-realm-role"
  description = "My Realm Role"
}
```

**`keycloak_group`** wraps users for shared attributes/roles; nest with `parent_id`
and read the computed `path`. Federated (LDAP/AD) groups should be left out of
Terraform management.

```hcl
resource "keycloak_group" "parent_group" {
  realm_id = keycloak_realm.realm.id
  name     = "parent-group"
}
```

**The assignment resources are where the "authoritative vs partial" model matters.**
`keycloak_group_memberships` (by username), `keycloak_user_groups`,
`keycloak_group_roles`, and `keycloak_user_roles` each default to authoritative
behavior — they will undo out-of-band changes on the next apply. For the `*_roles`
and `user_groups` resources, set `exhaustive = false` to let several resources
co-manage the same subject without fighting. `keycloak_group_memberships` and
`keycloak_user_groups` do **not** support import; create them fresh.

```hcl
resource "keycloak_user" "user" {
  realm_id = keycloak_realm.realm.id
  username = "bob"
  enabled  = true
  email    = "bob@domain.com"
}
```

**`keycloak_generic_role_mapper`** is the supported way to control scope mappings
(which roles land in tokens / SAML assertions when `full_scope_allowed` is off).
Its predecessor `keycloak_generic_client_role_mapper` is **deprecated** — migrate to
the generic mapper.

The two `*_permissions` resources (`keycloak_group_permissions`,
`keycloak_users_permissions`) drive **admin fine-grained authorization**, a preview
feature that must be enabled on the server (`admin_fine_grained_authz`). Enabling
them turns on Authorization on the `realm-management` client and auto-creates the
backing resources/scopes; `keycloak_users_permissions` must exist only once per realm.

## RHBK / migration / air-gap notes

- **Upstream, not Red Hat ground-truth.** Everything above is from the community
  `keycloak/keycloak` provider docs. The RHBK *support* statement for the provider
  itself is community; the server behavior it drives is the corpus authority. See
  `ref:rhbk-platform-support.md`.
- **Source change — the #1 migration fix:** the provider moved from
  **`mrparkers/keycloak`** to the official **`keycloak/keycloak`**. Update
  `required_providers` and re-init; old `mrparkers` references fail to resolve.
- **`base_path = "/auth"` — RH-SSO vs RHBK:** legacy RH-SSO 7.x (Wildfly) needs the
  `/auth` context path on the provider; RHBK (Quarkus) does **not** — omit
  `base_path`. This affects how the provider reaches the Admin REST API these
  resources call, not the resource arguments themselves (inferred).
- **Version-sensitive arguments:** `keycloak_group.organization_id` requires
  **Keycloak 26.6.0+**; the `*_permissions` resources require the
  `admin_fine_grained_authz` preview feature enabled on the server;
  `keycloak_generic_client_role_mapper` is deprecated in favor of
  `keycloak_generic_role_mapper`. Confirm a resource/argument exists for the RHBK
  version you target before relying on it.
- **Air-gapped:** with no internet, `terraform init` cannot reach the registry — the
  `keycloak/keycloak` provider must come from a **local filesystem/network mirror**
  (`terraform providers mirror`, then a `provider_installation { filesystem_mirror }`
  block). Pin the version and verify the `*_SHA256SUMS`. See
  [[terraform-keycloak-iac]].

## See also
- [[terraform-keycloak-iac]]
- [[roles-and-groups]]
- [[managing-users-credentials]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
<!-- crosslink:end -->
