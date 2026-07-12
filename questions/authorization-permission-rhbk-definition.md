---
origin: eval-cohort
title: What is an authorization permission in RHBK fine-grained authorization?
type: question
domain: keycloak
slug: authorization-permission-rhbk-definition
summary: "A permission binds a protected resource or scope to the policies that must be evaluated to decide access — the glue layer between 'what' and 'the conditions,' expressed as resource-based or scope-based permissions."
sources:
  - kb:authorization_services_guide/permission_overview
  - guide:authorization_services_guide
  - entity:authorization-permissions
provenance:
  extracted: 6
  inferred: 0
  ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# What is an authorization permission in RHBK fine-grained authorization?

**A permission associates the object being protected (a [[authorization-resources-scopes|resource or scope]]) with the [[authorization-policy-types|policies]] that must be evaluated to determine whether access is granted — the linkage between "what to protect" and "under what conditions."**

Conceptually: `X CAN DO Y ON RESOURCE Z` ([[authorization-permissions]]:22).

In RHBK's fine-grained authorization model (Authorization Services), permissions are the second layer in a three-layer stack:

1. **Resources & Scopes** — define what is protected ([[authorization-resources-scopes]]).
2. **Permissions** — bind policies to those resources/scopes.
3. **Policies** — define the conditions (role, user attribute, time, JavaScript rule, etc.).

## Two kinds

- **Resource-based permission** — protects one or more whole resources with a set of policies. Fields: resources, policies, decision strategy. A typed variant (`Apply To Resource Type`) protects all resources sharing a `Type` label with the same policies (e.g., every "banking-account" resource gets owner-only + region-locked policies) (rhbk-26-6-permission-overview:45-56).
- **Scope-based permission** — protects specific scopes (actions), optionally restricted to one resource. If no resource is selected, all scopes are available (rhbk-26-6-permission-overview:56-71).

## Decision Strategy on a permission

Each permission carries its own **Decision Strategy** — `Unanimous` (default: all policies must grant), `Affirmative` (at least one grants), or `Consensus` (positive > negative decisions) (rhbk-26-6-permission-overview:72-79). This joins a three-level strategy chain: per-policy **Logic** → per-permission **Decision Strategy** → resource-server **Decision Strategy** ([[authorization-permissions]]:38).

## Stable across versions

The resource/policy/permission model is identical across RHBK 26.0–26.6 ([[fine-grained-authorization]]:58).

## References

### RH ground-truth
- **`guide:authorization_services_guide`** — Red Hat Authorization Services Guide (RHBK 26.6)
- **`kb:authorization_services_guide/permission_overview`** → `reference/keycloak/rhbk-26-6-permission-overview.md` — Chapter 6: Managing permissions

### Wiki
- [[authorization-permissions]] — entity page on permissions
- [[fine-grained-authorization]] — topic page on Authorization Services
- [[authorization-resources-scopes]] — resources & scopes
- [[authorization-policy-types]] — policy types
- [[decision-strategies]] — decision strategies
