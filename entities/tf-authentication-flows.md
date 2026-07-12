---
title: Authentication flows, executions & bindings (Terraform)
type: entity
domain: keycloak
slug: tf-authentication-flows
summary: "The `keycloak/keycloak` Terraform resources that declaratively build authentication flows — the flow container, its nested subflows, the individual executions, per-execution config, and the realm bindings that activate a flow"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/authentication_bindings.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/authentication_execution.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/authentication_execution_config.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/authentication_flow.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/authentication_subflow.md (fetched 2026-06-16)
provenance_extracted: 7
provenance_inferred: 3
provenance_ambiguous: 0
tags: [authn, iac]
status: draft
updated: 2026-07-02
---

# Authentication flows, executions & bindings (Terraform)

**The `keycloak/keycloak` Terraform resources that declaratively build authentication flows — the flow container, its nested subflows, the individual executions, per-execution config, and the realm bindings that activate a flow.** This page is **upstream/community (web-sourced)** reference from the provider's own docs, **not** Red Hat ground-truth; only arguments actually seen in the fetched docs are documented below. Confirm each resource against the provider version you pin.

## Resource table

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_authentication_flow` | A top-level authentication flow — the container for a sequence of authentication actions | `realm_id`, `alias` | Optional `description`, `provider_id` (`basic-flow` \| `client-flow`, default `basic-flow`). Import: `{{realmId}}/{{authenticationFlowId}}`; flow ID is auto-generated, retrieve from the `/admin/realms/${realm}/authentication/flows` API. |
| `keycloak_authentication_subflow` | A subflow nested inside a parent flow — a container for executions | `realm_id`, `alias`, `parent_flow_alias` | Optional `provider_id` (`basic-flow` \| `form-flow` \| `client-flow`, default `basic-flow`), `requirement` (`REQUIRED`/`ALTERNATIVE`/`OPTIONAL`/`CONDITIONAL`/`DISABLED`, default `DISABLED`), `priority` (Keycloak >= 25). Import: `{{realmId}}/{{parentFlowAlias}}/{{authenticationSubflowId}}` — ID is the `flowID` field (not `id`). |
| `keycloak_authentication_execution` | A single execution (action) attached to a flow | `realm_id`, `parent_flow_alias`, `authenticator` | Optional `requirement` (same enum, default `DISABLED`), `priority` (lower runs first, Keycloak >= 25). Import: `{{realmId}}/{{parentFlowAlias}}/{{authenticationExecutionId}}`. |
| `keycloak_authentication_execution_config` | Configuration attached to an execution that supports extra customization (e.g. identity-provider-redirector) | `realm_id`, `execution_id`, `alias` | Optional `config` map (key-value pairs specific to the execution type). Import: `realm/executionId/configId`; a wrong `execution_id` still imports, then a later apply replaces it. |
| `keycloak_authentication_bindings` | Realm-level bindings assigning custom flows to the supported realm flow slots | `realm_id` | Optional flow-alias slots: `browser_flow`, `registration_flow`, `direct_grant_flow`, `reset_credentials_flow`, `client_authentication_flow`, `docker_authentication_flow`, `first_broker_login_flow` (Keycloak 24+). |

## Notable resources

### `keycloak_authentication_flow` — the container
The root of any custom flow. You give it a `realm_id` and an `alias`; everything else (subflows, executions) attaches by referencing that `alias`. The flow ID is server-generated and not surfaced in the UI, so import requires pulling it from the Admin REST API.

```hcl
resource "keycloak_authentication_flow" "flow" {
  realm_id = keycloak_realm.realm.id
  alias    = "my-flow-alias"
}
```

### `keycloak_authentication_execution` — the steps
Each execution is one authenticator (e.g. `auth-cookie`) bound to a flow via `parent_flow_alias`. Note the provider default for `requirement` is `DISABLED`, so you almost always set it explicitly. Ordering via `priority` is only honored on Keycloak >= 25; on older servers, ordering follows resource/declaration order. Executions in the same flow commonly create an ordering dependency, so apply order matters.

```hcl
resource "keycloak_authentication_execution" "example" {
  realm_id          = keycloak_realm.realm.id
  parent_flow_alias = keycloak_authentication_flow.flow.alias
  authenticator     = "auth-cookie"
  requirement       = "ALTERNATIVE"
  priority          = 10
}
```

### `keycloak_authentication_bindings` — activation
A custom flow does nothing until a realm binds it. This resource maps flow aliases into the realm's flow slots (browser, registration, direct grant, reset credentials, client auth, docker, and — Keycloak 24+ — first broker login). It carries only `realm_id` as required; every flow slot is optional.

```hcl
resource "keycloak_authentication_bindings" "example" {
  realm_id     = keycloak_realm.realm.id
  browser_flow = keycloak_authentication_flow.flow.alias
}
```

### `keycloak_authentication_execution_config` — per-step settings
For executions that take extra options (the canonical case is `identity-provider-redirector`), this attaches a named `config` map to a specific `execution_id`. Watch the import caveat: a wrong `execution_id` imports successfully, then the next apply replaces the config to fix it.

## RHBK / migration / air-gap notes (inferred — general Terraform/RHBK migration
knowledge; not covered by this page's cited sources, which document provider
resource arguments, not the provider's history or the RH-SSO→RHBK provider
connection settings. Verify against [[terraform-keycloak-iac]] and the provider's
own changelog before relying on these.)
- **Provider source change:** these resources live in the official **`keycloak/keycloak`** provider, which replaced the legacy **`mrparkers/keycloak`**. A config still pointing at `mrparkers/keycloak` fails provider resolution — switch `required_providers` source and re-init. See [[terraform-keycloak-iac]].
- **`base_path = "/auth"` (RH-SSO vs RHBK):** these resources drive the Admin REST API, so flow-building is version-agnostic, but the *provider connection* differs. Legacy **RH-SSO 7.x (Wildfly)** needs `base_path = "/auth"`; **RHBK (Quarkus)** must **omit** it. The API import paths quoted in the upstream docs show `/auth/admin/...`, which reflects that legacy prefix — on RHBK the path is `/admin/...`.
- **Version-sensitive arguments (upstream-stated):** `priority` on executions and subflows is honored only on **Keycloak >= 25**; `first_broker_login_flow` binding requires **Keycloak 24+**. RHBK trails upstream OSS by versions, so verify these against your RHBK release before relying on them — this is community guidance, not an RHBK support statement.
- **Air-gapped:** on a network with no internet, `terraform init` cannot reach the registry; the `keycloak/keycloak` provider must come from a **local filesystem/network mirror** (`terraform providers mirror`), with a `provider_installation { filesystem_mirror }` block and explicit `-platform` if the runner OS differs from the mirroring host. See [[terraform-keycloak-iac]].

## Contradictions / caveats
- All argument lists here come **only** from the fetched upstream markdown docs; no arguments were inferred. Attribute availability tracks upstream Keycloak and may lead the pinned RHBK release.
- The `requirement` default of `DISABLED` on both executions and subflows is easy to miss and is a common source of "flow does nothing" surprises.

## See also
- [[terraform-keycloak-iac]]
- [[authentication-flows]]
- [[step-up-authentication]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
<!-- crosslink:end -->
