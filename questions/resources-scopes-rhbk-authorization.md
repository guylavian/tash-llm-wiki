---
origin: eval-cohort
title: What are resources and scopes in RHBK authorization?
type: question
domain: keycloak
slug: resources-scopes-rhbk-authorization
summary: "A resource is the object being protected (web page, REST endpoint, file, EJB, or a typed group of them); a scope is a bounded action or attribute on that resource (view, edit, delete, cost). Together they form the 'what' that permissions protect."
sources:
  - guide:authorization_services_guide
  - kb:authorization_services_guide/resource_overview
  - kb:authorization_services_guide/overview
  - entity:authorization-resources-scopes
provenance:
  extracted: 9
  inferred: 0
  ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# What are resources and scopes in RHBK authorization?

In Red Hat Build of Keycloak (RHBK) Authorization Services, **resources and scopes are the two fundamental building blocks that define what you want to protect.** Permissions then bind policies to these targets (`rhbk-26-6-overview-2.md:28`).

## Resources — the "what"

A **resource** is the object being protected — a web page, a RESTful endpoint, a file, an EJB, or any application asset (`rhbk-26-6-overview-2.md:102`). Every resource has a unique identifier and can represent either:

- **A single concrete asset** — e.g. "Alice's Banking Account" (a specific resource instance owned by one user)
- **A class/type of assets** — e.g. "Banking Account" (a typed resource grouping all accounts under common policies)

(`rhbk-26-6-overview-2.md:61-63`)

Key fields when creating a resource (`rhbk-26-6-resource-overview.md:35-43`):
- **Name** — unique human-readable string
- **Type** — string grouping resource instances for typed permissions (default: `urn:resource-server-name:resources:default`)
- **URIS** — locations/addresses (for HTTP resources, the relative paths served)
- **Scopes** — zero or more scopes to associate
- **Attributes** — key/value pairs surfaced to policies (enables ABAC) (`rhbk-26-6-resource-overview.md:45-46`)
- **Owner** — defaults to the resource server; can be a user ID for owner-based policies (central to UMA sharing) (`rhbk-26-6-resource-overview.md:50-51`)

## Scopes — the "what can be done"

A **scope** is "one of the potentially many verbs that can logically apply to a resource" (`rhbk-26-6-overview-2.md:105`). Typically an action like `view`, `edit`, `delete`, but it can also name a data attribute — e.g. a `cost` scope on a `project` resource to define separate cost-access policies (`rhbk-26-6-overview-2.md:106`). Scopes are managed under the **Authorization Scopes** tab (`rhbk-26-6-resource-overview.md:19`).

## How they fit together

The authorization model is a three-layer stack (`rhbk-26-6-overview-2.md:53-71`):

1. **Resources & Scopes** — define *what* is protected
2. **Permissions** — bind policies to resources/scopes
3. **Policies** — define *under what conditions* access is granted (roles, user attributes, time, JavaScript rules, etc.)

Two kinds of permissions (`rhbk-26-6-permission-overview.md:22-24`):
- **Resource-based** — protects one or more whole resources. A typed variant applies to all resources sharing a `Type` label
- **Scope-based** — protects specific scopes, optionally narrowed to one resource (finer granularity over actions)

## Architecture note

Resources and scopes are managed through the **Policy Administration Point (PAP)** — the Admin Console — or remotely via the **Protection API** (UMA-compliant Resource Registration Endpoint) (`rhbk-26-6-overview-2.md:45`). The Protection API requires a `uma_protection` scope and is only accessible to resource servers (`rhbk-26-6-overview-2.md:84`).

## References

### RH ground-truth
- **`guide:authorization_services_guide`** — Red Hat Authorization Services Guide (RHBK 26.6)
- **`kb:authorization_services_guide/resource_overview`** → `reference/keycloak/rhbk-26-6-resource-overview.md` — Chapter 4: Managing resources and scopes
- **`kb:authorization_services_guide/overview`** → `reference/keycloak/rhbk-26-6-overview-2.md` — Chapter 1: Authorization services overview
- **`kb:authorization_services_guide/permission_overview`** → `reference/keycloak/rhbk-26-6-permission-overview.md` — Chapter 6: Managing permissions

### Wiki
- [[authorization-resources-scopes]] — entity page on resources & scopes
- [[authorization-permissions]] — how permissions bind policies to resources/scopes
- [[fine-grained-authorization]] — topic page on Authorization Services
- [[authorization-policy-types]] — built-in policy types
- [[protection-api]] — remote resource management via UMA Protection API
