---
title: Realm & realm-scoped resources (Terraform)
type: entity
domain: keycloak
slug: tf-realm-resources
summary: "The `keycloak/keycloak` Terraform resources that create a realm and everything configured at the realm level — events, localization, user profile, client-scope defaults, client policies, signing keystores, default groups/roles, required actions, organizations, and workflows"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_events.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_localization.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_user_profile.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_default_client_scopes.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_optional_client_scopes.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_client_policy_profile.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_client_policy_profile_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_aes_generated.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_ecdsa_generated.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_hmac_generated.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_java_keystore.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_rsa.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm_keystore_rsa_generated.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/default_groups.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/default_roles.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/required_action.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/organization.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/workflow.md (fetched 2026-06-16)
provenance_extracted: 24
provenance_inferred: 4
provenance_ambiguous: 0
tags: [iac]
status: draft
updated: 2026-07-02
---

# Realm & realm-scoped resources (Terraform)

**The `keycloak/keycloak` Terraform resources that create a realm and everything
configured at the realm level — events, localization, user profile, client-scope
defaults, client policies, signing keystores, default groups/roles, required
actions, organizations, and workflows.** This page is **upstream/community
(web-sourced)** reference distilled from the provider's own GitHub docs — **not**
Red Hat ground-truth. Only arguments actually present in the fetched docs are
listed; confirm against the provider docs for your pinned version before relying
on any of them. All 19 docs in this group were fetched successfully (none failed).

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_realm` | A realm — the top-level container for users, credentials, roles, groups | `realm` | Huge optional surface: `enabled`, `display_name`, themes, `ssl_required`, `password_policy`, `smtp_server`, `internationalization`, `security_defenses`, `web_authn_policy`, `otp_policy`, token settings. Import: `terraform import ... my-realm`. |
| `keycloak_realm_events` | Realm event logging/storage config (user + admin events) | `realm_id` | Optional: `events_enabled`, `events_expiration`, `admin_events_enabled`, `admin_events_details_enabled`, `enabled_event_types`, `events_listeners`. Setting `events_listeners` removes the default `jboss-logging` listener unless you re-list it. **No import support.** |
| `keycloak_realm_localization` | Locale-specific text/translation overrides | `realm_id`, `locale` | Optional `texts` map (key→localized value). Locale must first be enabled on the realm. Import: `{{realm_id}}/{{locale}}`. |
| `keycloak_realm_user_profile` | User-profile schema: attributes, groups, validators, permissions | `realm_id` | Optional `attribute` (ordered), `group`, `unmanaged_attribute_policy` (`DISABLED`/`ENABLED`/`ADMIN_EDIT`/`ADMIN_VIEW`). Before KC 24 the user-profile feature must be enabled on the realm. **No import support.** |
| `keycloak_realm_default_client_scopes` | Authoritative set of default client scopes for new clients | `realm_id`, `default_scopes` | Authoritative — overwrites manual/factory defaults on apply. Import by realm ID. |
| `keycloak_realm_optional_client_scopes` | Authoritative set of optional client scopes for new clients | `realm_id`, `optional_scopes` | Authoritative — overwrites manual/factory optional scopes. Import by realm ID. |
| `keycloak_realm_client_policy_profile` | A realm client-policy profile (a named set of executors) | `name`, `realm_id` | Optional ordered `executor` blocks (each `name` + optional `configuration` map). **No import support.** |
| `keycloak_realm_client_policy_profile_policy` | A client-policy *policy* that applies profiles when conditions match | `name`, `realm_id`, `profiles` | Optional `description`, ordered `condition` blocks (each `name` + optional `configuration`). **No import support.** |
| `keycloak_realm_keystore_aes_generated` | Realm AES generated keystore (signing/encryption keys) | `name`, `realm_id` | Optional `enabled`, `active`, `priority`, `secret_size` (16/24/32 → AES-128/192/256, default 16). Import: `my-realm/{keystore-id}`. |
| `keycloak_realm_keystore_ecdsa_generated` | Realm ECDSA generated keystore | `name`, `realm_id` | Optional `enabled`, `active`, `priority`, `elliptic_curve_key` (default `P-256`). Import: `realm-name/keystore-id`. |
| `keycloak_realm_keystore_hmac_generated` | Realm HMAC generated keystore | `name`, `realm_id` | Optional `enabled`, `active`, `priority`, `algorithm` (default `HS256`), `secret_size` (default 64). Import: `my-realm/{keystore-id}`. |
| `keycloak_realm_keystore_java_keystore` | Realm keystore loaded from a Java keystore file on the server | `name`, `realm_id`, `keystore`, `keystore_password`, `key_alias`, `key_password` | Optional `enabled`, `active`, `priority`, `algorithm` (default `RS256`). Import: `realm-name/keystore-id`. |
| `keycloak_realm_keystore_rsa` | Realm RSA keystore from a supplied PEM key + cert | `name`, `realm_id`, `private_key`, `certificate` | Optional `enabled`, `active`, `algorithm` (default `RS256`; `RSA-OAEP` for enc), `keystore_size` (default 2048), `provider_id` (`rsa`/`rsa-enc`), `extra_config` (e.g. `kid`). Import: `my-realm/keystore-id`. |
| `keycloak_realm_keystore_rsa_generated` | Realm RSA generated keystore | `name`, `realm_id` | Optional `enabled`, `active`, `priority`, `algorithm` (default `RS256`), `key_size` (default 2048). Import: `my-realm/keystore-id`. |
| `keycloak_default_groups` | Realm default groups that new users auto-join | `realm_id`, `group_ids` | Don't combine with `keycloak_group_memberships` (conflicts). Import: `{{realm_id}}`. |
| `keycloak_default_roles` | Default roles assigned to new users | `realm_id`, `default_roles` | KC v13+. Supports realm + client roles (`account/manage-account` dot notation). Import: `{{realm_id}}/{{default_role_id}}` (composite role ID). |
| `keycloak_required_action` | A required action enforced before/at first login | `realm_id`, `alias` | Optional `enabled` (default false), `default_action` (default false), `name`, `priority`, `config`. Aliases e.g. `UPDATE_PASSWORD`, `VERIFY_EMAIL`, `CONFIGURE_TOTP`. Import: `{{realm}}/{{alias}}`. |
| `keycloak_organization` | A realm organization (settings, domains, attributes) | `realm`, `name` | Optional `alias`, `description`, `redirect_url`, `domain` (`name`+`verified`), `attributes` (`##` multivalue). Import: `{{realm_id}}/{{organization_id}}`. (Organizations are a recent KC feature.) |
| `keycloak_workflow` | Event-driven automated admin tasks in a realm | `realm`, `name`, `on`, `step` | **KC 26.4+, requires `--features=workflows`.** Optional `enabled`, `conditions`, `cancel_in_progress`/`restart_in_progress`. Steps use `uses` (e.g. `notify-user`, `delete-user`), optional `after` (ms delay), `config`. Import: `{{realm}}/{{workflow_id}}`. |

## Notable resources

### `keycloak_realm` — the root of every config
Almost everything else in this group references it via `realm_id`. Only `realm`
(the internal name/ID) is required; the rest of its large surface — themes,
`ssl_required`, `password_policy`, brute-force `security_defenses`, WebAuthn/OTP
policy, token lifespans — is optional and defaults to Keycloak's built-ins.

```hcl
resource "keycloak_realm" "realm" {
  realm        = "my-realm"
  enabled      = true
  display_name = "My Realm"
  login_theme  = "keycloak"
}
```

### Signing keystores — `keycloak_realm_keystore_*`
Six keystore resources manage the realm's signing/encryption key material. The
`*_generated` variants (aes/ecdsa/hmac/rsa) have Keycloak generate the keys and
share the same control knobs — `enabled`, `active`, `priority` — so `priority`
plus a new `active` key is how you stage a key rotation (inferred). The two non-generated
ones import external material: `keycloak_realm_keystore_rsa` takes a PEM
`private_key` + `certificate`, and `keycloak_realm_keystore_java_keystore` reads
a Java keystore **file already present on the Keycloak server** (`keystore`,
`keystore_password`, `key_alias`, `key_password`). See [[realm-keys-and-rotation]].

### Client policies — `keycloak_realm_client_policy_profile(_policy)`
These two model Keycloak's client-policies feature (FAPI-style governance):
the **profile** is a named bundle of `executor` blocks (what to enforce), and the
**policy** binds one or more `profiles` to a realm subject to ordered `condition`
blocks (when to enforce). Neither supports `terraform import` today, so adopt them
greenfield rather than importing existing server state (inferred).

### `keycloak_default_roles` — version-gated
Requires Keycloak v13+. It manages the realm's composite "default-roles-<realm>"
role and accepts both realm roles and client roles via `client/role` dot notation.
Its import ID is the composite role's GUID, which the docs note you typically have
to dig out of browser dev tools.

## RHBK / migration / air-gap notes
- **Upstream, not Red Hat support.** Everything here is from the community
  `keycloak/keycloak` provider docs. RHBK's *server* behavior these resources drive
  is covered by the corpus, but the provider itself is not a Red Hat support
  statement. Verify support posture against `ref:rhbk-platform-support.md`.
- **`mrparkers/keycloak` → `keycloak/keycloak`.** The provider source moved to the
  official Keycloak org. Configs still pinning `mrparkers/keycloak` fail provider
  resolution — switch `required_providers.source` and re-init. See
  [[terraform-keycloak-iac]].
- **`base_path = "/auth"` is RH-SSO-only.** These resources hit the Admin REST API
  via the provider's `url`/`base_path`. On legacy **RH-SSO 7.x (Wildfly)** the API
  lives under `/auth`; on **RHBK (Quarkus)** drop `/auth` (leave `base_path` empty).
  This is a provider-block setting, not a per-resource one, but it gates whether any
  of these resources can reach the server at all.
- **Version-sensitive resources** — confirm the target RHBK/KC version supports them
  before applying:
  - `keycloak_default_roles` → KC 13+.
  - `keycloak_realm_user_profile` → before KC 24 the user-profile feature must be
    enabled on the realm.
  - `keycloak_organization` → recent KC organizations feature.
  - `keycloak_workflow` → **KC 26.4+ and `--features=workflows`** (so RHBK 26.6 era,
    not earlier RHBK releases (inferred — mapping upstream KC version to RHBK release
    train)). A brand-new feature like this can lag in the provider — confirm the
    resource exists in your pinned provider version.
- **Air-gapped:** with no internet, `terraform init` cannot reach the registry —
  the provider must come from a **local filesystem/network mirror**
  (`terraform providers mirror`, then a `provider_installation { filesystem_mirror }`
  block) and be pinned + checksum-verified. Several keystore resources also reference
  on-server files/secrets (`keycloak_realm_keystore_java_keystore`,
  `keycloak_realm_keystore_rsa`) — keep that key material out of VCS and out of
  unencrypted state (inferred). See [[terraform-keycloak-iac]].

## See also
- [[terraform-keycloak-iac]]
- [[realm-administration]]
- [[realm-keys-and-rotation]]
- [[authentication-flows]]
