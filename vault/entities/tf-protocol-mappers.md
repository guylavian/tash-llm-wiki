---
title: Protocol mappers (OIDC & SAML claims) (Terraform)
type: entity
domain: keycloak
slug: tf-protocol-mappers
summary: "The `keycloak/keycloak` Terraform resources that declare *protocol mappers* — the rules that shape what claims/attributes land in OIDC tokens (access / ID / UserInfo / introspection) and SAML assertions — declaratively as code, attached to a client or a shared client scope"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/generic_client_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/generic_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_audience_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_audience_resolve_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_full_name_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_group_membership_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_hardcoded_claim_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_hardcoded_role_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_sub_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_user_attribute_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_user_client_role_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_user_property_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_user_realm_role_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_user_session_note_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_user_attribute_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_user_property_protocol_mapper.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/hardcoded_attribute_mapper.md (fetched 2026-06-16)
provenance_extracted: 20
provenance_inferred: 6
provenance_ambiguous: 0
tags: [clients, iac]
status: draft
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# Protocol mappers (OIDC & SAML claims) (Terraform)

**The `keycloak/keycloak` Terraform resources that declare *protocol mappers* — the
rules that shape what claims/attributes land in OIDC tokens (access / ID / UserInfo /
introspection) and SAML assertions — declaratively as code, attached to a client or a
shared client scope.** This page is **upstream/community (web-sourced)** reference
distilled from the provider's own docs, **not** Red Hat ground-truth: it tells you what
the provider exposes, not a Red Hat support statement. Confirm any resource exists in
your pinned provider/RHBK version before relying on it. See [[terraform-keycloak-iac]].

## Common shape
Almost every mapper here shares: `realm_id` + `name` + exactly one of `client_id`
**or** `client_scope_id` (mutually exclusive — attach to one client, or to a reusable
scope). OIDC mappers add token-placement toggles (`add_to_id_token`,
`add_to_access_token`, `add_to_userinfo`, and on newer ones
`add_to_token_introspection`) that all default to `true`. SAML mappers instead carry
`saml_attribute_name` + `saml_attribute_name_format`. The two LDAP-side mappers
(`keycloak_hardcoded_attribute_mapper`) are different — they bind to an
`ldap_user_federation_id`, not a client/scope.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_generic_client_protocol_mapper` | Generic mapper for OIDC **or** SAML clients (custom/uncovered mappers) | `realm_id`, `client_id`, `name`, `protocol`, `protocol_mapper`, `config` | **Deprecated** — use `keycloak_generic_protocol_mapper`. `protocol` = `openid-connect`/`saml`. |
| `keycloak_generic_protocol_mapper` | Generic mapper, client **or** scope; custom mappers when no typed resource exists | `realm_id`, `name`, `protocol`, `protocol_mapper`, `config`, + one of `client_id`/`client_scope_id` | Escape hatch for any mapper impl via raw `config` map. |
| `keycloak_openid_audience_protocol_mapper` | Adds an audience to the `aud` claim | `realm_id`, `name`, one of `client_id`/`client_scope_id`, one of `included_client_audience`/`included_custom_audience` | `add_to_id_token`, `add_to_access_token` default true. |
| `keycloak_openid_audience_resolve_protocol_mapper` | Auto-resolves audience from the user's client roles | `realm_id`, + one of `client_id`/`client_scope_id` | `name` optional (defaults to "audience resolve"). No manual audience config. |
| `keycloak_openid_full_name_protocol_mapper` | First+last name → `name` claim | `realm_id`, `name`, one of `client_id`/`client_scope_id` | `add_to_id_token`/`add_to_access_token`/`add_to_userinfo` default true. |
| `keycloak_openid_group_membership_protocol_mapper` | User group memberships → a claim | `realm_id`, `name`, `claim_name`, one of `client_id`/`client_scope_id` | `full_path` (default true) includes parent path; token toggles default true. |
| `keycloak_openid_hardcoded_claim_protocol_mapper` | A claim with a fixed/hardcoded value | `realm_id`, `name`, `claim_name`, `claim_value`, one of `client_id`/`client_scope_id` | `claim_value_type` (String/JSON/long/int/boolean, default String); token toggles default true. |
| `keycloak_openid_hardcoded_role_protocol_mapper` | Always maps one role into the access token | `realm_id`, `name`, `role_id`, one of `client_id`/`client_scope_id` | `client_id`/`client_scope_id` conflict. |
| `keycloak_openid_sub_protocol_mapper` | Adds the `sub` (subject / user ID) claim | `realm_id`, `name`, one of `client_id`/`client_scope_id` | `add_to_access_token`, `add_to_token_introspection` default true. |
| `keycloak_openid_user_attribute_protocol_mapper` | Custom user attribute → claim | `realm_id`, `name`, `user_attribute`, `claim_name`, one of `client_id`/`client_scope_id` | `claim_value_type`, `multivalued` (default false), token toggles incl. `add_to_token_introspection` default true. |
| `keycloak_openid_user_client_role_protocol_mapper` | List of the user's **client** roles → claim | `realm_id`, `name`, `claim_name`, one of `client_id`/`client_scope_id` | `client_id_for_role_mappings`, `client_role_prefix`, `multivalued`, `claim_value_type`. |
| `keycloak_openid_user_property_protocol_mapper` | Built-in user property (e.g. `email`) → claim | `realm_id`, `name`, `user_property`, `claim_name`, one of `client_id`/`client_scope_id` | `claim_value_type`; token toggles default true. |
| `keycloak_openid_user_realm_role_protocol_mapper` | List of the user's **realm** roles → claim | `realm_id`, `name`, `claim_name`, one of `client_id`/`client_scope_id` | `realm_role_prefix`, `multivalued`, `claim_value_type`, token toggles incl. `add_to_token_introspection`. |
| `keycloak_openid_user_session_note_protocol_mapper` | Custom user session note → claim | `realm_id`, `name`, `claim_name`, one of `client_id`/`client_scope_id` | `session_note`, `claim_value_type`, token toggles incl. `add_to_token_introspection`. |
| `keycloak_saml_user_attribute_protocol_mapper` | Custom user attribute → SAML assertion attribute | `realm_id`, `name`, `user_attribute`, `saml_attribute_name`, `saml_attribute_name_format`, one of `client_id`/`client_scope_id` | `friendly_name`, `aggregate_attributes` (default false). |
| `keycloak_saml_user_property_protocol_mapper` | User model property → SAML assertion attribute | `realm_id`, `name`, `user_property`, `saml_attribute_name`, `saml_attribute_name_format`, one of `client_id`/`client_scope_id` | `friendly_name`. |
| `keycloak_hardcoded_attribute_mapper` | **LDAP** mapper: assign a static value to a user model attribute | `realm_id`, `ldap_user_federation_id`, `name`, `attribute_name`, `attribute_value` | Not a client mapper — binds to LDAP federation. Import: `{realm_id}/{ldap_user_federation_id}/{mapper_id}`. |

`saml_attribute_name_format` accepts `Unspecified`, `Basic`, or `URI Reference`.
`protocol_mapper`/`config` on the generic resources are the raw Keycloak mapper impl id
and its key/value config map (the escape hatch when no typed resource exists).

## Notable resources

**`keycloak_generic_protocol_mapper`** is the universal escape hatch. When the provider
has no typed resource for a mapper impl (custom SPI mappers, brand-new server mappers),
you declare it raw via `protocol_mapper` (the impl name) + a `config` map. It supersedes
the **deprecated** `keycloak_generic_client_protocol_mapper`, which only attaches to a
client and is slated for removal in the next major version.

```hcl
resource "keycloak_generic_protocol_mapper" "example" {
  realm_id        = "my-realm"
  client_id       = "my-client-id"
  name            = "my-mapper"
  protocol        = "saml"
  protocol_mapper = "saml-hardcode-attribute-mapper"
  config = {
    "attribute.name"  = "email"
    "attribute.value" = "user@example.com"
  }
}
```

**`keycloak_openid_audience_protocol_mapper`** is the one you reach for to satisfy
RFC-style `aud` validation on resource servers: add a client or a custom string to `aud`
(inferred). Pair it with `keycloak_openid_audience_resolve_protocol_mapper` when you'd
rather have Keycloak derive the audience automatically from the user's client roles
instead of hardcoding a value (inferred). See [[oidc-endpoints]].

```hcl
resource "keycloak_openid_audience_protocol_mapper" "example" {
  realm_id                 = "my-realm"
  client_id                = "my-client-id"
  name                     = "audience-mapper"
  included_custom_audience = "my-audience"
}
```

**Role/group claim mappers** — `keycloak_openid_user_realm_role_protocol_mapper`,
`keycloak_openid_user_client_role_protocol_mapper`, and
`keycloak_openid_group_membership_protocol_mapper` — are the workhorses for
authorization data in tokens (inferred). They support `multivalued` (emit an array), an optional
prefix (`realm_role_prefix` / `client_role_prefix`), and for group membership a
`full_path` toggle that controls whether the parent group hierarchy is encoded.

```hcl
resource "keycloak_openid_group_membership_protocol_mapper" "example" {
  realm_id   = "my-realm"
  client_id  = "my-client"
  name       = "groups-mapper"
  claim_name = "groups"
  full_path  = true
}
```

**SAML mappers** (`keycloak_saml_user_attribute_protocol_mapper`,
`keycloak_saml_user_property_protocol_mapper`) are the SAML-assertion analogues of the
OIDC user-attribute/property mappers, replacing the OIDC `claim_name`/token toggles with
`saml_attribute_name` + `saml_attribute_name_format` (+ optional `friendly_name`). See
[[saml-clients-and-migration]].

## RHBK / migration / air-gap notes
- **Source change (`mrparkers` → `keycloak/keycloak`):** these resources live in the
  official `keycloak/keycloak` provider. Configs still pointing at the legacy
  `mrparkers/keycloak` source fail provider resolution — switch `required_providers`
  and re-init. See [[terraform-keycloak-iac]].
- **RH-SSO vs RHBK context path:** the provider drives mappers through the Admin REST
  API, so mapper resources are largely server-version agnostic (inferred). The
  version-sensitive knob is at the **provider** block, not these resources: set
  `base_path = "/auth"` for legacy **RH-SSO 7.x (Wildfly)** and **omit** it for **RHBK
  (Quarkus)** (inferred).
- **Version drift:** newer token-placement attributes (notably
  `add_to_token_introspection`, present on `sub`, `user_attribute`, `user_realm_role`,
  `user_session_note`) and the audience-resolve resource track upstream Keycloak; a
  feature may lag in your pinned RHBK/provider. Pin the provider version and verify the
  attribute exists before using it. RHBK ships 26.0 / 26.2 / 26.4 / 26.6 (inferred —
  general RHBK version knowledge, not from this page's cited sources).
- **Deprecation:** `keycloak_generic_client_protocol_mapper` is deprecated — migrate to
  `keycloak_generic_protocol_mapper` (which also supports `client_scope_id`).
- **Air-gapped:** with no internet, `terraform init` can't reach the registry — the
  provider must come from a **local filesystem/network mirror** (`terraform providers
  mirror`, then a `provider_installation { filesystem_mirror }` block), with
  `*_SHA256SUMS` verified after transfer. See [[terraform-keycloak-iac]].

## Contradictions / caveats
- This is **upstream/community (web-sourced)** reference from the provider's GitHub
  docs, **not** `kb:`/`guide:` Red Hat ground-truth. Only the arguments actually seen in
  the fetched docs are listed here; nothing is invented. The RHBK support statement for
  the Terraform provider itself is community, while the underlying server behavior it
  configures is Red Hat-supported.

## See also
- [[terraform-keycloak-iac]]
- [[oidc-endpoints]]
- [[saml-clients-and-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
<!-- crosslink:end -->
