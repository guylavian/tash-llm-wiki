---
title: How can you manage Keycloak realms declaratively with Terraform?
type: question
question_tier: conceptual
domain: keycloak
slug: terraform-keycloak-realms-declarative
summary: "The `keycloak/keycloak` Terraform provider manages Keycloak/RHBK realms as code — the `keycloak_realm` resource defines the realm, and ~15 realm-scoped resources cover events, user profile, keystores, client policies, default scopes, required actions, organizations, and workflows."
sources:
  - web:https://registry.terraform.io/providers/keycloak/keycloak/latest/docs (fetched 2026-07-07)
  - web:https://github.com/keycloak/terraform-provider-keycloak (fetched 2026-07-07)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/realm.md (fetched 2026-07-07)
provenance:
  extracted: 18
  inferred: 2
  ambiguous: 0
tags: [iac]
status: draft
updated: 2026-07-07
graph_community: "Keycloak as IaC — the Terraform Provider (keycloak/keycloak)"
---

# How can you manage Keycloak realms declaratively with Terraform?

The **`keycloak/keycloak`** Terraform provider (official, community-maintained, **≥ 5.8.0**) manages Keycloak/RHBK realms via the Admin REST API. The config block uses `client_credentials` (service account):

```hcl
terraform {
  required_providers {
    keycloak = { source = "keycloak/keycloak", version = ">= 5.8.0" }
  }
}
provider "keycloak" {
  client_id     = "terraform"
  client_secret = var.kc_client_secret
  url           = "https://rhbk.internal.example:8443"
  # base_path   = "/auth"   # RH-SSO 7.x only; omit for RHBK (Quarkus)
}
```

## Core realm resource

`keycloak_realm` is the root — `realm` (name) is required; it supports themes, `ssl_required`, `password_policy`, `smtp_server`, brute-force `security_defenses`, WebAuthn/OTP policy, token lifespans, and internationalization. Everything else references the realm via `realm_id`.

## Realm-scoped resources

| Resource | What it manages |
|---|---|
| `keycloak_realm_events` | User + admin event logging configuration |
| `keycloak_realm_localization` | Locale-specific text overrides |
| `keycloak_realm_user_profile` | User-profile attribute schema (KC 24+) |
| `keycloak_realm_default_client_scopes` | Authoritative default scopes for new clients |
| `keycloak_realm_optional_client_scopes` | Authoritative optional scopes for new clients |
| `keycloak_realm_client_policy_profile` | Named bundles of policy executors |
| `keycloak_realm_client_policy_profile_policy` | Conditions + profiles for client governance |
| `keycloak_realm_keystore_*` (6 resources) | AES/ECDSA/HMAC/RSA generated + PEM/JKS imported signing keystores |
| `keycloak_default_groups` | Groups auto-assigned to new users |
| `keycloak_default_roles` | Default realm/client roles (KC 13+) |
| `keycloak_required_action` | Actions enforced at login (e.g. `UPDATE_PASSWORD`) |
| `keycloak_organization` | Realm organizations with domains (recent KC feature) |
| `keycloak_workflow` | Event-driven admin workflows (KC 26.4+, `--features=workflows`) |

## Practical concerns

- **Provider move:** `mrparkers/keycloak` → `keycloak/keycloak`. Old source breaks — update `required_providers` and re-init.
- **base_path:** RHBK (Quarkus) omits `/auth`; legacy RH-SSO 7.x (Wildfly) needs it.
- **Air-gapped:** mirror the provider on a connected box (`terraform providers mirror -platform=linux_amd64`), then configure a `filesystem_mirror` block on the sealed network. Use an internal S3-compatible state backend.
- **Drift detection:** `terraform plan` (read-only) against live server reveals configuration drift — changes made outside Terraform.

## References

**Upstream / community:**
- `web:https://registry.terraform.io/providers/keycloak/keycloak/latest/docs` — provider docs
- `web:https://github.com/keycloak/terraform-provider-keycloak` — source + resource-level docs

**Wiki:**
- [[terraform-keycloak-iac]] — full topic: provider setup, auth, air-gap, drift
- [[tf-realm-resources]] — realm resource reference with all arguments
- [[rhsso-to-rhbk-migration]] — RH-SSO 7.x → RHBK migration context
