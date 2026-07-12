---
title: LDAP / user federation & LDAP mappers (Terraform)
type: entity
domain: keycloak
slug: tf-ldap-federation
summary: "The `keycloak/keycloak` Terraform resources that declare an LDAP/AD user-federation provider (or a custom User Storage SPI provider) plus the mappers that translate LDAP attributes, groups and roles into the Keycloak user model"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_user_federation.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/custom_user_federation.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_custom_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_full_name_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_group_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_hardcoded_attribute_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_hardcoded_group_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_hardcoded_role_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_msad_lds_user_account_control_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_msad_user_account_control_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_role_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/ldap_user_attribute_mapper.md (fetched 2026-06-16)
provenance_extracted: 13
provenance_inferred: 4
provenance_ambiguous: 0
tags: [federation, iac]
status: draft
updated: 2026-07-02
---

# LDAP / user federation & LDAP mappers (Terraform)

**The `keycloak/keycloak` Terraform resources that declare an LDAP/AD user-federation provider (or a custom User Storage SPI provider) plus the mappers that translate LDAP attributes, groups and roles into the Keycloak user model.** This page is **upstream/community (web-sourced)** reference distilled from the provider's own raw docs — it is **not** Red Hat ground-truth. Only arguments actually seen in the fetched docs are documented; confirm against the provider docs for your pinned version. See [[terraform-keycloak-iac]] for provider setup, auth and air-gap handling.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_ldap_user_federation` | An LDAP/AD user-federation provider on a realm | `realm_id`, `name`, `username_ldap_attribute`, `rdn_ldap_attribute`, `uuid_ldap_attribute`, `user_object_classes`, `connection_url`, `users_dn` | Optional `edit_mode` (`READ_ONLY`/`WRITABLE`/`UNSYNCED`), `import_enabled`, `bind_dn`+`bind_credential`, `connection_timeout`/`read_timeout` (Go durations), `kerberos` block, `cache` block. Import: `{{realm_id}}/{{federation_id}}`. |
| `keycloak_custom_user_federation` | A custom User Storage SPI provider (non-LDAP source) | `realm_id`, `name`, `provider_id` (matches `UserStorageProviderFactory`) | Optional `enabled`, `priority`, `cache_policy`, `full_sync_period`/`changed_sync_period` (seconds), `config` (multivalued uses `##` separator). Import: `{{realm_id}}/{{custom_user_federation_id}}`. |
| `keycloak_ldap_custom_mapper` | A self-implemented (custom) LDAP attribute mapper | `realm_id`, `ldap_user_federation_id`, `name`, `provider_id`, `provider_type` | Optional `config` map. Import: `{{realm_id}}/{{federation_id}}/{{mapper_id}}`. |
| `keycloak_ldap_full_name_mapper` | Maps an LDAP full-name attribute to Keycloak first/last name | `realm_id`, `ldap_user_federation_id`, `name`, `ldap_full_name_attribute` | Optional `read_only`, `write_only` (both default false). |
| `keycloak_ldap_group_mapper` | Maps LDAP groups (from a DN) to Keycloak groups; auto-creates groups | `realm_id`, `ldap_user_federation_id`, `name`, `ldap_groups_dn`, `group_name_ldap_attribute`, `group_object_classes`, `membership_ldap_attribute`, `membership_user_ldap_attribute` | Optional `preserve_group_inheritance`, `mode` (`READ_ONLY`/`LDAP_ONLY`/`IMPORT`, default `READ_ONLY`), `user_roles_retrieve_strategy`, `groups_path`, `drop_non_existing_groups_during_sync`. |
| `keycloak_ldap_hardcoded_attribute_mapper` | Sets a hardcoded value on an LDAP attribute during sync | `realm_id`, `ldap_user_federation_id`, `name`, `attribute_name`, `attribute_value` | Only works when `sync_registrations` is enabled on the federation provider. |
| `keycloak_ldap_hardcoded_group_mapper` | Grants a fixed Keycloak group to every LDAP-linked user | `realm_id`, `ldap_user_federation_id`, `name`, `group` | Import: `{{realm_id}}/{{federation_id}}/{{mapper_id}}`. |
| `keycloak_ldap_hardcoded_role_mapper` | Grants a fixed Keycloak role to every LDAP-linked user | `realm_id`, `ldap_user_federation_id`, `name`, `role` | Client roles use `{{client_id}}.{{client_role_name}}`. No optional args documented. |
| `keycloak_ldap_msad_lds_user_account_control_mapper` | Propagates MS AD LDS account state (expired pw / disabled) to Keycloak | `realm_id`, `ldap_user_federation_id`, `name` | No optional args documented. |
| `keycloak_ldap_msad_user_account_control_mapper` | Propagates Microsoft AD account state (expired pw / disabled) to Keycloak | `realm_id`, `ldap_user_federation_id`, `name` | Optional `ldap_password_policy_hints_enabled` (default false) for advanced AD password policies. |
| `keycloak_ldap_role_mapper` | Maps LDAP user roles (from a DN) to Keycloak roles | `realm_id`, `ldap_user_federation_id`, `name`, `ldap_roles_dn`, `role_name_ldap_attribute`, `role_object_classes`, `membership_ldap_attribute`, `membership_user_ldap_attribute` | Optional `membership_attribute_type` (`DN`/`UID`, default `DN`), `user_roles_retrieve_strategy` (default `LOAD_ROLES_BY_MEMBER_ATTRIBUTE`), `mode` (default `READ_ONLY`), `use_realm_roles_mapping` (default true), `client_id`. |
| `keycloak_ldap_user_attribute_mapper` | Maps one LDAP attribute to one Keycloak user-model attribute | `realm_id`, `ldap_user_federation_id`, `name`, `user_model_attribute`, `ldap_attribute` | Optional `read_only`, `always_read_value_from_ldap`, `is_mandatory_in_ldap`, `attribute_force_default` (default true), `is_binary_attribute`. |

All mapper resources import with the format `{{realm_id}}/{{ldap_user_federation_id}}/{{ldap_mapper_id}}`; the two federation/mapper IDs are GUIDs visible in the Keycloak GUI.

## Notable resources

**`keycloak_ldap_user_federation`** is the anchor: every mapper hangs off its `ldap_user_federation_id`. It declares how Keycloak connects to and reads the directory — the connection URL, the bind credentials, the users subtree DN, the object classes that identify users, and the attributes used as username/RDN/UUID. `edit_mode` controls write-back (`READ_ONLY`, `WRITABLE`, `UNSYNCED`); `import_enabled` controls whether LDAP users are imported into the Keycloak DB. A minimal example from the doc:

```hcl
resource "keycloak_ldap_user_federation" "ldap_user_federation" {
  name     = "openldap"
  realm_id = keycloak_realm.realm.id

  enabled = true

  username_ldap_attribute = "cn"
  rdn_ldap_attribute      = "cn"
  uuid_ldap_attribute     = "entryUUID"
  user_object_classes = [
    "simpleSecurityObject",
    "organizationalRole",
  ]
  connection_url  = "ldap://openldap"
  users_dn        = "dc=example,dc=org"
  bind_dn         = "cn=admin,dc=example,dc=org"
  bind_credential = "admin"
}
```

**`keycloak_ldap_group_mapper`** is the most argument-heavy and most commonly needed mapper: it joins an LDAP group subtree to Keycloak groups and can preserve LDAP group hierarchy (`preserve_group_inheritance`) and prune groups dropped from LDAP (`drop_non_existing_groups_during_sync`). Its `mode` (`READ_ONLY`/`LDAP_ONLY`/`IMPORT`) decides whether group membership lives in LDAP, in Keycloak, or is imported. `keycloak_ldap_role_mapper` is its role-side counterpart and additionally chooses realm vs client roles via `use_realm_roles_mapping`/`client_id`.

**`keycloak_ldap_user_attribute_mapper`** is the everyday single-attribute mapper (e.g. LDAP `mail` → Keycloak `email`); `always_read_value_from_ldap` makes LDAP authoritative on each read, and `is_binary_attribute` handles binary values.

**`keycloak_custom_user_federation`** is the escape hatch for non-LDAP sources: it wires a deployed User Storage SPI implementation (identified by `provider_id` matching the `UserStorageProviderFactory`) into a realm, with caching and full/changed sync periods.

## RHBK / migration / air-gap notes (inferred — general Terraform/RHBK migration
knowledge, not covered by this page's cited sources, which document only LDAP
federation/mapper resource arguments; verify against [[terraform-keycloak-iac]]
and the provider changelog.)

- **Upstream, not Red Hat ground-truth.** These resources track upstream Keycloak. A brand-new RHBK federation/mapper option can lag in the provider; confirm a resource/argument exists for your pinned provider version before relying on it. The server behavior they drive (LDAP federation, mappers) is covered by the Red Hat corpus — see [[ldap-user-federation]] and [[ldap-mappers]].
- **`mrparkers` → `keycloak/keycloak` source change.** Configs still referencing `mrparkers/keycloak` in `required_providers` must switch `source` to `keycloak/keycloak` and re-init. This is the #1 migration fix (see [[terraform-keycloak-iac]]).
- **`base_path = "/auth"` — RH-SSO vs RHBK.** The provider reaches these resources through the Admin REST API, so it is largely server-version agnostic. The one provider-level difference: legacy **RH-SSO 7.x (Wildfly)** needs `base_path = "/auth"`, while **RHBK (Quarkus)** must omit it. This affects the provider block, not the LDAP resource arguments themselves.
- **Version sensitivity in the resources.** `edit_mode`/`mode` enums and defaults (e.g. group/role mappers defaulting to `READ_ONLY`) and the `##` multivalued separator in `keycloak_custom_user_federation.config` are upstream conventions; treat the per-argument defaults above as version-specific and re-verify on upgrade.
- **Air-gapped network.** With no internet, `terraform init` cannot reach the registry — the `keycloak/keycloak` provider must come from a **local filesystem/network mirror** (`terraform providers mirror`, then a `provider_installation { filesystem_mirror }` block), mirrored for the runner platform and integrity-checked against `*_SHA256SUMS`. Bind credentials in `keycloak_ldap_user_federation` land in state, so keep state on an encrypted internal backend. See [[terraform-keycloak-iac]].

## See also
- [[terraform-keycloak-iac]]
- [[ldap-user-federation]]
- [[ldap-mappers]]
- [[ldap-storage-mode]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
<!-- crosslink:end -->
