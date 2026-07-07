---
title: Client authorization services (policies/permissions) (Terraform)
type: entity
domain: keycloak
slug: tf-client-authorization
summary: "resources** + **scopes** (what is protected and which actions), **policies"
sources:
  - ref:rhbk-platform-support.md
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_aggregate_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_authorization_client_scope_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_authorization_permission.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_authorization_resource.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_authorization_scope.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_client_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_group_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_regex_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_role_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_time_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/openid_client_user_policy.md (fetched 2026-06-16)
  - web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/identity_provider_token_exchange_scope_permission.md (fetched 2026-06-16)
provenance_extracted: 12
provenance_inferred: 4
provenance_ambiguous: 0
tags: [authz, clients, iac]
status: draft
updated: 2026-07-02
---

# Client authorization services (policies/permissions) (Terraform)

**The Terraform resources that declaratively manage a Keycloak/RHBK client's
fine-grained authorization services — the resources, scopes, policies, and
permissions of a resource server — plus identity-provider token-exchange
permissions.** This page is **upstream/community (web-sourced)** reference
distilled from the `keycloak/keycloak` provider docs, **not** Red Hat
ground-truth; confirm each resource and argument against the provider docs for
your pinned version before relying on it.

These resources all hang off a client that has Authorization Services enabled
(its `resource_server_id` is that client's ID). The building blocks are:
**resources** + **scopes** (what is protected and which actions), **policies**
(the conditions: who/when/how), and **permissions** (which policies gate which
resources/scopes). See the domain pages [[fine-grained-authorization]],
[[authorization-policy-types]] and [[authorization-permissions]].

## Resource reference

All policy/permission/resource/scope resources below share three required
arguments — `realm_id`, `resource_server_id`, and `name` — and all import as
`{{realmId}}/{{resourceServerId}}/{{policyId}}` (the token-exchange permission
is the exception, noted in its row).

| Terraform resource (`keycloak_<name>`) | Manages | Key required args | Notes |
|---|---|---|---|
| `keycloak_openid_client_aggregate_policy` | Combines multiple policies into one for complex logic | `realm_id`, `resource_server_id`, `name`, `decision_strategy`, `policies` (list of policy IDs) | `decision_strategy` ∈ `UNANIMOUS`/`AFFIRMATIVE`/`CONSENSUS`. Optional `logic` (`POSITIVE`/`NEGATIVE`, default `POSITIVE`), `description`. |
| `keycloak_openid_client_authorization_client_scope_policy` | Client-scope-based policy (matches on client scopes) | `realm_id`, `resource_server_id`, `name`, `scope` (≥1 block) | `scope` block has required `id` and optional `required` (bool, default `false`). Optional `decision_strategy` (default `UNANIMOUS`), `logic`, `description`. |
| `keycloak_openid_client_authorization_permission` | A permission binding policies to resources and/or scopes | `realm_id`, `resource_server_id`, `name` | Optional `policies`, `resources` (conflicts with `resource_type`), `resource_type`, `scopes`, `type` (`resource`/`scope`), `decision_strategy` (default `UNANIMOUS`), `description`. |
| `keycloak_openid_client_authorization_resource` | A protected resource on the resource server | `realm_id`, `resource_server_id`, `name` | Optional `display_name`, `uris` (set), `icon_uri`, `owner_managed_access` (default false), `scopes` (set of scope names), `type`, `attributes` (map). |
| `keycloak_openid_client_authorization_scope` | An authorization scope (an action on a resource) | `realm_id`, `resource_server_id`, `name` | Optional `display_name`, `icon_uri`. Computed `id`. |
| `keycloak_openid_client_client_policy` | Policy matching on which clients access the resource | `realm_id`, `resource_server_id`, `name`, `clients` (list of client IDs) | Optional `decision_strategy`, `logic` (default `POSITIVE`), `description`. |
| `keycloak_openid_client_group_policy` | Policy matching on group membership | `realm_id`, `resource_server_id`, `name`, `decision_strategy`, `groups` (≥1 block: `id`, `path`, `extend_children` bool) | Optional `logic` (default `POSITIVE`), `groups_claim`, `description`. |
| `keycloak_openid_client_regex_policy` | Policy matching a regex against a token claim | `realm_id`, `resource_server_id`, `name`, `decision_strategy`, `target_claim`, `pattern` | Optional `logic` (default `POSITIVE`), `target_context_attributes` (bool), `type` (default `regex`), `description`. |
| `keycloak_openid_client_role_policy` | Policy matching on assigned roles | `realm_id`, `resource_server_id`, `name`, `type` (= `role`), `role` (≥1 block: `id`, `required` bool) | Optional `decision_strategy`, `logic` (default `POSITIVE`), `fetch_roles` (roles from user claims, Keycloak 25+), `description`. |
| `keycloak_openid_client_time_policy` | Time-based access policy | `realm_id`, `resource_server_id`, `name`, `decision_strategy` | Optional `logic`, `not_before`/`not_on_or_after` (`YYYY-MM-DD HH:MM:SS`), `hour`/`hour_end`, `minute`/`minute_end`, `month`/`month_end`, `year`/`year_end`, `day_month`/`day_month_end`, `description`. |
| `keycloak_openid_client_user_policy` | Policy matching on specific users | `realm_id`, `resource_server_id`, `name`, `decision_strategy`, `users` (list of user IDs) | Optional `logic` (default `POSITIVE`), `description`. |
| `keycloak_identity_provider_token_exchange_scope_permission` | IdP token-exchange scope-based permission | `realm_id`, `provider_alias`, `clients` (list of client IDs) | Optional `policy_type` (default `client`, only supported type). **Preview feature** — must be explicitly enabled. Import is `{{realmId}}/{{providerAlias}}` — different from the others. |

## Notable resources

**`keycloak_openid_client_authorization_resource` + `..._scope`** are the
foundation: a resource is the thing being protected (with `uris`, a `type`, and
the `scopes` it supports), and a scope is a named action. Everything else
references their IDs.

```hcl
resource "keycloak_openid_client_authorization_scope" "read" {
  realm_id           = keycloak_realm.realm.id
  resource_server_id = keycloak_openid_client.client.resource_server_id
  name               = "read"
}

resource "keycloak_openid_client_authorization_resource" "doc" {
  realm_id           = keycloak_realm.realm.id
  resource_server_id = keycloak_openid_client.client.resource_server_id
  name               = "document"
  uris               = ["/api/document"]
  scopes             = [keycloak_openid_client_authorization_scope.read.name]
}
```

**`keycloak_openid_client_authorization_permission`** is the glue that ties
policies to what they protect. Note `resources` and `resource_type` are mutually
exclusive, and `type` selects whether the permission is `resource`- or
`scope`-scoped.

```hcl
resource "keycloak_openid_client_authorization_permission" "doc_read" {
  realm_id           = keycloak_realm.realm.id
  resource_server_id = keycloak_openid_client.client.resource_server_id
  name               = "doc-read-permission"
  type               = "scope"
  resources          = [keycloak_openid_client_authorization_resource.doc.id]
  scopes             = [keycloak_openid_client_authorization_scope.read.id]
  policies           = [keycloak_openid_client_role_policy.editors.id]
  decision_strategy  = "AFFIRMATIVE"
}
```

**`keycloak_openid_client_aggregate_policy`** composes several existing policies
under one `decision_strategy`, letting you build complex AND/OR logic without
duplicating conditions; it takes a `policies` list of policy IDs.

**`keycloak_identity_provider_token_exchange_scope_permission`** is the odd one
out — it is not bound to a client resource server but to an identity provider
(`provider_alias`), and it creates client-type policies inside the
`realm-management` client (to avoid circular dependencies). It targets the
**Token Exchange** preview feature and so requires that preview feature be
enabled on the server.

## RHBK / migration / air-gap notes (inferred — general Terraform/RHBK migration
knowledge not covered by this page's cited sources, which document only provider
resource arguments; verify against [[terraform-keycloak-iac]] and the provider
changelog.)

- **Upstream, not Red Hat ground-truth.** Everything here is from the
  community/upstream `keycloak/keycloak` provider docs. The RHBK support
  statement for *the provider* is community; the server behavior it drives
  (authorization services) is the Red-Hat-supported part — see
  [[fine-grained-authorization]] and `ref:rhbk-platform-support.md`.
- **Provider source change:** configs still pointing at `mrparkers/keycloak`
  must switch to the official `keycloak/keycloak` source and re-init, or
  provider resolution fails. See [[terraform-keycloak-iac]].
- **`base_path = "/auth"`:** these resources only talk to the Admin REST API, so
  they are server-version agnostic. The one provider-level RH-SSO→RHBK
  difference is the context path — set `base_path = "/auth"` for legacy RH-SSO
  7.x (Wildfly), and omit it for RHBK (Quarkus).
- **Version-sensitive arguments:** `keycloak_openid_client_role_policy`
  `fetch_roles` is documented as Keycloak 25+. The token-exchange permission
  relies on a **preview** feature that must be explicitly enabled — confirm
  RHBK ships and supports it on your version before depending on it. A
  brand-new RHBK authorization capability may lag the provider.
- **Air-gapped:** with no internet, `terraform init` cannot reach the registry —
  the `keycloak/keycloak` provider must come from a **local filesystem/network
  mirror** (`terraform providers mirror`, then a
  `provider_installation { filesystem_mirror }` block), with the runner platform
  specified explicitly. See [[terraform-keycloak-iac]].

## See also
- [[terraform-keycloak-iac]]
- [[fine-grained-authorization]]
- [[authorization-policy-types]]
- [[authorization-permissions]]
