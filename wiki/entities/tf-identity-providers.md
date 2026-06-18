---
title: Identity providers & IdP mappers (brokering) (Terraform)
type: entity
domain: keycloak
slug: tf-identity-providers
summary: "The `keycloak/keycloak` Terraform resources for declaring external identity providers (OIDC, social, SAML, Kubernetes, SPIFFE) and the IdP mappers that transform brokered identities into Keycloak users, roles, groups and attributes"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_facebook_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_github_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_google_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_microsoft_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_openshift_v4_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/kubernetes_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/spiffe_identity_provider.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/attribute_importer_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/attribute_to_role_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/custom_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/hardcoded_attribute_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/hardcoded_group_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/hardcoded_role_identity_provider_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/user_template_importer_identity_provider_mapper.md (fetched 2026-06-16)
provenance: needs-review
tags: [brokering, iac]
status: draft
updated: 2026-06-16
---

# Identity providers & IdP mappers (brokering) (Terraform)

**The `keycloak/keycloak` Terraform resources for declaring external identity
providers (OIDC, social, SAML, Kubernetes, SPIFFE) and the IdP mappers that
transform brokered identities into Keycloak users, roles, groups and attributes.**

> **Honesty note:** this page is **upstream/community (web-sourced)** reference,
> taken from the OSS `terraform-provider-keycloak` docs on GitHub — it is **not**
> Red Hat RHBK ground-truth. Only arguments actually present in the fetched docs
> are listed; confirm against your pinned provider version and the RHBK release
> before relying on any resource. See [[terraform-keycloak-iac]] for the provider
> source/version and air-gap setup.

## Resource reference

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_oidc_identity_provider` | Generic OIDC IdP for third-party auth via the OIDC standard | `realm`, `alias`, `authorization_url`, `token_url`, `client_id`, `client_secret` | `client_secret_wo`/`client_secret_wo_version` write-only variant; `jwks_url`, `issuer`, `logout_url`, `default_scopes` (default `openid`), `store_token`, `trust_email`, `extra_config`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_oidc_facebook_identity_provider` | Facebook social login (OIDC) | `realm`, `client_id`, `client_secret` | `fetched_fields`, `trust_email`, `sync_mode`, `link_only`, `hide_on_login_page`, `first_broker_login_flow_alias`, `extra_config`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_oidc_github_identity_provider` | GitHub (github.com or Enterprise) social login | `realm`, `client_id`, `client_secret` | `base_url` (default `https://github.com`), `api_url` (default `https://api.github.com`), `default_scopes` (default `user:email`), `sync_mode`, `trust_email`, `store_token`, `hide_on_login_page`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_oidc_google_identity_provider` | Google social login (OIDC) | `realm`, `client_id`, `client_secret` | `hosted_domain` (restrict to a Google domain; `*` = any), `request_refresh_token`, `trust_email`, `sync_mode`, `alias`, `display_name`, `extra_config`. Computed `internal_id`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_oidc_microsoft_identity_provider` | Microsoft account login (OIDC) | `realm`, `client_id`, `client_secret` | `tenant_id` (single- vs multi-tenant endpoints), `store_token`, `trust_email`, `sync_mode`, `display_name`, `extra_config`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_oidc_openshift_v4_identity_provider` | OpenShift v4 cluster OIDC IdP; derives OAuth endpoints from `base_url` | `realm`, `client_id`, `client_secret`, `base_url` | `alias` (default `openshift-v4`), `default_scopes` (default `user:full`), `store_token`, `trust_email`, `sync_mode`, `extra_config`. `client_secret` supports `$${vault.ID}`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_saml_identity_provider` | SAML IdP for third-party auth via SAML protocol | `realm`, `entity_id`, `single_sign_on_service_url` | `alias`, `validate_signature`, `signing_certificate`, `signature_algorithm`, `force_authn`, `single_logout_service_url`, `post_binding_response`/`post_binding_authn_request`/`post_binding_logout`, `store_token`, `trust_email`, `sync_mode`. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_kubernetes_identity_provider` | Kubernetes IdP — workloads auth with service-account tokens (federated JWT) | `realm`, `alias`, `issuer` | `issuer`'s `<ISSUER>/.well-known/openid-configuration` must be reachable by Keycloak. **Preview feature** — must be enabled. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_spiffe_identity_provider` | SPIFFE IdP — authenticate clients with SPIFFE JWT SVIDs | `realm`, `alias`, `trust_domain`, `bundle_endpoint` | `trust_domain` uses `spiffe://` scheme; `bundle_endpoint` may need HTTPS per realm `ssl_required`. **Preview feature** — must be enabled. Import `{{realm_id}}/{{idp_alias}}`. |
| `keycloak_attribute_importer_identity_provider_mapper` | Import an external claim/attribute into a Keycloak user property | `realm`, `name`, `identity_provider_alias`, `user_attribute` | `claim_name` (OIDC); `attribute_name`/`attribute_friendly_name` (SAML, mutually exclusive); `extra_config` (required in Keycloak 10+). Import `{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}`. |
| `keycloak_attribute_to_role_identity_provider_mapper` | Grant a realm/client role when an external attribute/claim matches | `realm`, `name`, `identity_provider_alias`, `role` | `claim_name`/`claim_value` (OIDC); `attribute_name`/`attribute_friendly_name`/`attribute_value` (SAML); `extra_config` required in Keycloak 10+ (must include `syncMode`). Import `{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}`. |
| `keycloak_custom_identity_provider_mapper` | Define a custom/unsupported mapper type via Terraform | `realm`, `name`, `identity_provider_alias`, `identity_provider_mapper` | `identity_provider_mapper` supports `%s` for provider ID; `extra_config` needed in Keycloak 10+ to set `syncMode`. Import `{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}`. |
| `keycloak_hardcoded_attribute_identity_provider_mapper` | Assign a fixed value to an IdP/user attribute | `realm`, `name`, `identity_provider_alias`, `attribute_name`, `user_session` | `attribute_value` (hardcoded value); `user_session` (bool — attribute relates to a user session); `extra_config`. |
| `keycloak_hardcoded_group_identity_provider_mapper` | Grant a fixed Keycloak group to every brokered user | `realm`, `name`, `identity_provider_alias` | `group` (group to assign); `extra_config`. Doc example shows OIDC IdP + group + syncMode. |
| `keycloak_hardcoded_role_identity_provider_mapper` | Grant a fixed Keycloak role to every brokered user | `realm`, `name`, `identity_provider_alias` | `role` (role to assign); `extra_config`. |
| `keycloak_user_template_importer_identity_provider_mapper` | Build the Keycloak username from a template of external claims/attributes | `realm`, `name`, `identity_provider_alias`, `template` | `template` uses `${}` substitutions, e.g. `"${ALIAS}.${CLAIM.email}"`; `extra_config` required in Keycloak 10+ (syncMode). Import `{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}`. |

## Notable resources

### `keycloak_oidc_identity_provider` — the generic OIDC broker
The most flexible resource: any standards-compliant OIDC provider that the
purpose-built social resources don't cover. Unlike the social variants it
requires the **endpoints explicitly** (`authorization_url`, `token_url`), since
there is no hardcoded vendor default. Prefer the write-only `client_secret_wo`
(with `client_secret_wo_version`) so the secret never lands in state where the
plain `client_secret` would.

```hcl
resource "keycloak_oidc_identity_provider" "realm_identity_provider" {
  realm             = keycloak_realm.realm.id
  alias             = "my-idp"
  authorization_url = "https://authorizationurl.com"
  client_id         = "clientID"
  client_secret     = "clientSecret"
  token_url         = "https://tokenurl.com"
}
```

### `keycloak_oidc_openshift_v4_identity_provider` — relevant to OpenShift fleets
Purpose-built for brokering against an OpenShift 4 cluster's OAuth server: you
give it `base_url` and it derives the OAuth endpoints, defaulting `alias` to
`openshift-v4` and `default_scopes` to `user:full`. The `client_secret` accepts
the vault interpolation `$${vault.ID}`. Useful when RHBK fronts logins for an
OpenShift platform.

### `keycloak_saml_identity_provider` — enterprise SAML brokering
For brokering to a corporate SAML IdP (ADFS, Shibboleth, etc.). Required
identification is `entity_id` + `single_sign_on_service_url`; the rich optional
surface (`validate_signature`/`signing_certificate`/`signature_algorithm`,
the `post_binding_*` flags, `single_logout_service_url`, `force_authn`) maps
directly onto SAML SP trust configuration.

### The mapper family — turning brokered identity into Keycloak state
All `*_identity_provider_mapper` resources share `realm`, `name`,
`identity_provider_alias` and import as `{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}`
(the mapper ID is a Keycloak-assigned GUID visible in the admin console URL).
Pick by intent: **importer** (claim→user attribute), **attribute_to_role**
(conditional role grant), **hardcoded_role / hardcoded_group / hardcoded_attribute**
(unconditional grants), **user_template_importer** (username synthesis), and
**custom** (escape hatch for unsupported mapper types). Note the recurring
gotcha: on **Keycloak 10+** most of these require `extra_config` to carry a
`syncMode` value or the mapper won't behave.

## RHBK / migration / air-gap notes
- **Upstream, not Red Hat ground-truth.** These resources track OSS Keycloak.
  A brand-new RHBK feature (or a preview such as the **Kubernetes** and
  **SPIFFE** IdPs above) may lag in the provider or be gated behind a preview
  feature flag on the server. Confirm the resource and feature exist on your
  pinned provider + RHBK release before depending on them.
- **`mrparkers/keycloak` → `keycloak/keycloak`.** The provider source moved to
  the official Keycloak org; configs still pointing at `mrparkers/keycloak` fail
  provider resolution. Switch `required_providers.source` and re-init. See
  [[terraform-keycloak-iac]].
- **`base_path = "/auth"` (RH-SSO vs RHBK).** These resources talk to the Admin
  REST API and are server-version agnostic, so the only cross-cutting migration
  knob lives on the **provider block**, not on these resources: legacy RH-SSO 7.x
  (Wildfly) needs `base_path = "/auth"`; RHBK (Quarkus) must **omit** it.
- **`syncMode` / Keycloak 10+.** Several mappers (attribute importer,
  attribute_to_role, custom, user_template_importer) require `extra_config` with
  `syncMode` on Keycloak 10 and later — a version-sensitive footgun when porting
  older configs forward to RHBK 26.x.
- **Air-gapped network.** With no internet, `terraform init` cannot reach the
  registry — the `keycloak/keycloak` provider must come from a **local
  filesystem/network mirror** (`terraform providers mirror`, plus a
  `provider_installation { filesystem_mirror }` block). Mirror the runner
  platform explicitly and verify the release `*_SHA256SUMS`. See
  [[terraform-keycloak-iac]].

## See also
- [[terraform-keycloak-iac]]
- [[identity-brokering]]
