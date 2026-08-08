---
title: Keycloak as IaC — the Terraform Provider (keycloak/keycloak)
type: topic
domain: keycloak
slug: terraform-keycloak-iac
summary: "Managing Keycloak/RHBK realms, clients, roles, IdPs and federation declaratively with the Terraform provider — and what that means for RH-SSO→RHBK migration and an air-gapped network"
sources:
  - ref:rhbk-platform-support.md
  - web:https://registry.terraform.io/providers/keycloak/keycloak/latest/docs (fetched 2026-06-16)
  - web:https://github.com/keycloak/terraform-provider-keycloak (fetched 2026-06-16)
  - web:https://www.terraform.io/docs/cli/commands/providers/mirror.html (fetched 2026-06-16)
  - web:https://oneuptime.com/blog/post/2026-02-23-how-to-handle-terraform-in-air-gapped-environments/view (fetched 2026-06-16)
provenance_extracted: 15
provenance_inferred: 3
provenance_ambiguous: 0
tags: [iac, concept]
status: draft
updated: 2026-07-02
graph_community: "Keycloak as IaC — the Terraform Provider (keycloak/keycloak)"
---

# Keycloak as IaC — the Terraform Provider (keycloak/keycloak)

**Managing Keycloak/RHBK realms, clients, roles, IdPs and federation declaratively
with the Terraform provider — and what that means for RH-SSO→RHBK migration and an
air-gapped network.** This page is **upstream/community (web-sourced)**, not Red
Hat ground-truth; pin and verify against the provider's own docs.

## Source & version — first migration flag
- The provider **moved from `mrparkers/keycloak` to the official
  `keycloak/keycloak`** (now maintained by the Keycloak org, **`>= 5.8.0`**). Old
  configs still pointing at `mrparkers/keycloak` hit provider-resolution errors.
  🔴 **If your `.tf` still references `mrparkers/keycloak`, that's the #1 fix** —
  switch the `required_providers` source and re-init.
- Tooling: recent provider needs **Terraform ≥ 1.14** (Go 1.25 to build).

## RHBK vs RH-SSO — the one provider change that matters
The provider talks to the **Admin REST API**, so it's largely server-version
agnostic. The **only** significant RH-SSO→RHBK change is the **context path**:
- **RH-SSO 7.x (Wildfly)** → set `base_path = "/auth"` (or `KEYCLOAK_BASE_PATH=/auth`).
- **RHBK (Quarkus)** → **do NOT set `/auth`** (leave `base_path` empty).
🟢 So migrating your IaC to RHBK is mostly: switch provider source, drop the
`/auth` base_path, re-point `url` to the RHBK host. See [[rhsso-to-rhbk-migration]]
and [[quarkus-config-migration]].

## Authentication — matches the audit service account
- Use the **client_credentials** grant (machine-to-machine) over password grant.
- A **dedicated service account** client in the `master` realm with
  `realm-management` roles — **not** the admin user. This is the *same* pattern as
  the read-only audit account ([[air-gapped-client-integration]]); for Terraform
  it needs **write** management roles, for audit only `view-*` (inferred — the
  comparison to the audit-account pattern is this wiki's own cross-page
  synthesis).

```hcl
terraform {
  required_providers {
    keycloak = { source = "keycloak/keycloak", version = ">= 5.8.0" }
  }
}
provider "keycloak" {
  client_id     = "terraform"          # service account, master realm
  client_secret = var.kc_client_secret # from a secret store, never in VCS
  url           = "https://rhbk.internal.example:8443"
  # base_path   = "/auth"              # ONLY for legacy RH-SSO; omit for RHBK
}
```

## Air-gapped operation (critical here)
The network has no internet, so `terraform init` cannot reach the registry. Use a
**filesystem/network provider mirror**:
- `terraform providers mirror ./mirror` on a connected box, then move it in;
  configure a `provider_installation { filesystem_mirror }` block so init **skips
  the upstream registry**.
- **Specify the runner platform explicitly**: `-platform=linux_amd64` if you mirror
  from this Mac but apply on Linux runners (default mirrors only the host platform).
- **Verify integrity** with the release `*_SHA256SUMS` file after manual transfer.
- **State backend offline**: no public S3 — use an **internal S3-compatible store
  (e.g. MinIO)** for remote state + locking + versioning, or a local backend.
  Encrypt state (it contains client secrets). See [[air-gapped-client-integration]].
- Host modules internally; **pin every version**.

## Code-quality best practices (for the IaC review)
(inferred — general Terraform/IaC hygiene, not specific claims from the cited
provider docs.)
- **Modules** per concern (realms / clients / groups); **variables** for env
  differences; **outputs** for IDs other modules need.
- **Never commit secrets** — client secrets via a secret store / TF vars, and keep
  them out of state-in-VCS (remote encrypted backend).
- **Staging realm first** — validate `plan` against a non-prod realm before prod.
- Everything in **version control** for rollback/audit.

## Use in the live audit — drift detection
With the IaC, the audit gains a dimension the REST API alone can't give:
**declared desired-state vs live**. Run `terraform plan` (read-only, no apply) and
treat a non-empty plan as **configuration drift** — someone changed the server
outside Terraform. Cross-check drift findings against the live-audit findings.
(inferred — this application of `terraform plan` to a live audit is this page's
own synthesis, not a claim from any cited Terraform doc.)

## Contradictions / caveats
- Provider resources/attributes track upstream Keycloak; a brand-new RHBK feature
  may lag in the provider. Confirm a resource exists before relying on it.
- This page is web-sourced (provider docs/community), **not** `kb:`/`guide:`
  ground-truth — the RHBK support statement for *the provider itself* is community,
  while the server behavior it drives is covered by the corpus pages linked above.

## Full provider reference (per-group)
The complete `keycloak/keycloak` resource/data-source reference, split by concern.
Each page is upstream/community (provider-docs-sourced), not Red Hat ground-truth.
- [[tf-realm-resources]] — the realm and its realm-scoped resources (events, localization, user profile, default/optional client scopes, client-policy profiles, keystores).
- [[tf-openid-client]] — core OIDC clients, their client scopes, scope permissions, and service-account role bindings.
- [[tf-client-authorization]] — Authorization Services: protected resources, scopes, the built-in policy types, and resource/scope permissions.
- [[tf-protocol-mappers]] — OIDC & SAML protocol mappers that shape claims/assertions (audience, group membership, roles, user attributes, hardcoded values).
- [[tf-saml-clients]] — SAML-protocol clients, their client scopes, and default-scope attachments.
- [[tf-identity-providers]] — external OIDC/SAML/social IdPs for brokering plus the IdP mappers that import attributes/roles/groups.
- [[tf-ldap-federation]] — LDAP/AD user federation, custom federation, and the full set of LDAP attribute/group/role mappers.
- [[tf-roles-groups-users]] — realm/client roles, groups, users, their memberships/role assignments, and generic role mappers.
- [[tf-authentication-flows]] — authentication flows, subflows, executions, per-execution config, and the realm flow bindings that activate them.
- [[tf-data-sources]] — read-only data sources for referencing existing Keycloak objects (realm, clients, scopes, roles, groups, flows, service-account users).

## See also
- [[rhsso-to-rhbk-migration]]
- [[quarkus-config-migration]]
- [[air-gapped-client-integration]]
- [[security-hardening-checklist]]
- [[oidc-client-best-practices]]
- [[kcadm-cli]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
<!-- crosslink:end -->
