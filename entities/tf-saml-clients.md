---
title: SAML clients (Terraform)
type: entity
domain: keycloak
slug: tf-saml-clients
summary: "The `keycloak/keycloak` Terraform resources that declaratively manage SAML-protocol clients, their client scopes, and the default-scope attachments in a Keycloak/RHBK realm"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_client.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_client_default_scopes.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/saml_client_scope.md (fetched 2026-06-16)
provenance_extracted: 12
provenance_inferred: 1
provenance_ambiguous: 0
tags: [clients, iac]
status: draft
updated: 2026-07-02
---

# SAML clients (Terraform)

**The `keycloak/keycloak` Terraform resources that declaratively manage SAML-protocol clients, their client scopes, and the default-scope attachments in a Keycloak/RHBK realm.** This page is **upstream/community (web-sourced)** reference from the provider's own docs — *not* Red Hat ground-truth. Only the arguments actually present in the fetched docs are listed; confirm against the provider release you pin.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_saml_client` | A Keycloak client using the **SAML protocol** for authentication/SSO. | `realm_id`, `client_id` | Many signing/encryption knobs: `sign_assertions`, `sign_documents` (default `true`), `include_authn_statement`, `encrypt_assertions`, `client_signature_required` (default `true`), `force_post_binding` (default `true`), `valid_redirect_uris`, `signing_certificate`/`signing_private_key`, `encryption_certificate`, `master_saml_processing_url`, `extra_config`. Import: `{{realm_id}}/{{client_keycloak_id}}` (the Keycloak-assigned GUID). |
| `keycloak_saml_client_default_scopes` | A SAML client's **default client scopes** (protocol mappers auto-applied to build claims). | `realm_id`, `client_id`, `default_scopes` | **Authoritative**: removes manually-attached scopes and re-adds manually-detached ones. Keycloak auto-assigns `role_list` to new clients — omit it and every `plan` shows drift. **No import support** — create as new. |
| `keycloak_saml_client_scope` | A reusable **SAML client scope** (shared protocol/role mappings across clients in a realm). | `realm_id`, `name` | Optional `description`, `consent_screen_text`, `gui_order` (integer), `extra_config`. Import: `{{realm_id}}/{{client_scope_id}}` (GUID from the GUI editing URI). |

## Notable resources

### `keycloak_saml_client`
The core resource: it creates a SAML-protocol client. Only `realm_id` and `client_id` are required; everything else is optional with sensible defaults. The bulk of the surface area is SAML signing/encryption: `sign_documents` (default `true`), `sign_assertions` (default `false`), `client_signature_required` (default `true`), `encrypt_assertions` (default `false`) with `encryption_algorithm`/`encryption_key_algorithm` (default `RSA-OAEP-11`), plus the cert/key material (`signing_certificate`, `signing_private_key`, `encryption_certificate`). Binding behaviour is controlled by `force_post_binding` (default `true`), `valid_redirect_uris`, and `master_saml_processing_url`. `extra_config` is an escape hatch map for attributes the provider doesn't model directly.

```hcl
resource "keycloak_saml_client" "saml_client" {
  realm_id  = keycloak_realm.realm.id
  client_id = "saml-client"
  name      = "saml-client"

  sign_documents          = false
  sign_assertions         = true
  include_authn_statement = true

  signing_certificate = file("saml-cert.pem")
  signing_private_key = file("saml-key.pem")
}
```

### `keycloak_saml_client_scope` + `keycloak_saml_client_default_scopes`
These two work as a pair. `keycloak_saml_client_scope` defines a *reusable* scope (its protocol/role mappings live on the scope, not the client), and `keycloak_saml_client_default_scopes` *attaches* a list of scope names to a given client as its defaults so those mappers build claims automatically. The attachment resource is **authoritative** — Terraform owns the full default-scope list, so it will strip any scope someone attaches by hand and re-add any it removes. The gotcha: Keycloak gives every new SAML client the `role_list` default scope, so if you manage `default_scopes` you must include `role_list` (or accept perpetual drift on `terraform plan`). Unlike the scope and client resources, the default-scopes resource has **no import** — recreate it instead.

```hcl
resource "keycloak_saml_client_scope" "saml_client_scope" {
  realm_id    = keycloak_realm.realm.id
  name        = "groups"
  description = "When requested, this scope will map a user's group memberships to a claim"
  gui_order   = 1
}

resource "keycloak_saml_client_default_scopes" "client_default_scopes" {
  realm_id  = keycloak_realm.realm.id
  client_id = keycloak_saml_client.saml_client.id

  default_scopes = [
    "role_list",
    keycloak_saml_client_scope.saml_client_scope.name,
  ]
}
```

## RHBK / migration / air-gap notes
- **Upstream caveat (read first):** these resources track upstream OSS Keycloak. The provider's support statement is community, not a Red Hat one; the *server behaviour* they drive is what the RHBK corpus covers ([[saml-clients-and-migration]]).
- **`mrparkers` → `keycloak/keycloak` source change:** configs still pointing `required_providers` at `mrparkers/keycloak` fail provider resolution. Switch the source to the official `keycloak/keycloak` and re-init. See [[terraform-keycloak-iac]].
- **`base_path = /auth` (RH-SSO vs RHBK):** the resources themselves don't change between RH-SSO and RHBK, but the **provider** block does — legacy **RH-SSO 7.x (Wildfly)** needs `base_path = "/auth"`, while **RHBK (Quarkus)** must omit it. A wrong `base_path` makes every SAML-client `apply` fail to reach the Admin API (inferred).
- **Air-gapped network:** `terraform init` can't reach the registry, so the `keycloak/keycloak` provider must come from a **local filesystem/network mirror** (`terraform providers mirror`, then a `filesystem_mirror` install block). Mirror the runner's platform explicitly and verify the `*_SHA256SUMS`.
- **Version sensitivity:** specific SAML arguments (e.g. encryption algorithm options) and resource availability depend on the provider release — pin a version and confirm an argument exists before relying on it rather than assuming parity with the latest RHBK feature set.

## See also
- [[terraform-keycloak-iac]]
- [[saml-clients-and-migration]]
- [[mod-auth-mellon]]
