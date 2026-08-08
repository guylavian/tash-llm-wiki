---
title: Fine-grained authorization (Authorization Services)
type: topic
domain: keycloak
slug: fine-grained-authorization
summary: "RHBK Authorization Services turn a confidential client into a centralized policy decision point: you register protected [[authorization-resources-scopes|resources and scopes]], attach reusable [[authorization-policy-types|policies]] via [[authorization-permissions|permissions]], and enforce decisions with a [[policy-enforcer|Policy Enforcement Point]] — going beyond plain role checks to combine ABAC, RBAC, UBAC, CBAC, and rule-based access control."
sources:
  - guide:authorization_services_guide
  - kb:authorization_services_guide/overview
  - kb:authorization_services_guide/service_overview
  - kb:authorization_services_guide/resource_server_overview
source_notes:
  - "[[rhbk-26-6-overview-2]]"
  - "[[rhbk-26-6-service-overview]]"
  - "[[rhbk-26-6-resource-server-overview]]"
provenance_extracted: 12
provenance_inferred: 1
provenance_ambiguous: 0
tags: [authz, concept]
status: draft
updated: 2026-07-02
graph_community: "Fine-grained authorization (Authorization Services)"
---

# Fine-grained authorization (Authorization Services)

**RHBK Authorization Services turn a confidential client into a centralized policy decision point: you register protected [[authorization-resources-scopes|resources and scopes]], attach reusable [[authorization-policy-types|policies]] via [[authorization-permissions|permissions]], and enforce decisions with a [[policy-enforcer|Policy Enforcement Point]] — going beyond plain role checks to combine ABAC, RBAC, UBAC, CBAC, and rule-based access control.**

## Why beyond roles
Most resource servers authorize purely on RBAC: roles on the user are checked against roles on the resource. The guide notes the limits — resources and roles are tightly coupled, security changes force code changes, role management grows error-prone, and roles carry no contextual information. Authorization Services centralize resource, permission, and policy management so applications only know *what* they protect, not *how*.

## Architecture (the XACML-style points)
- **PAP — Policy Administration Point**: Admin Console UIs + the [[protection-api]] to manage resource servers, resources, scopes, permissions, policies.
- **PDP — Policy Decision Point**: where authorization requests are sent; all policies for the requested resource(s)/scope(s) are evaluated. See [[requesting-party-token]].
- **PEP — Policy Enforcement Point**: enforces decisions at the resource server. See [[policy-enforcer]].
- **PIP — Policy Information Point**: pulls attributes from identities and the runtime during evaluation (claims pushing, [[policy-evaluation-tool|evaluation context]]).

## The three processes
1. **Resource management** — define what is protected. Enable any confidential client as a *resource server*, then register [[authorization-resources-scopes|resources and scopes]] (Console or [[protection-api]]).
2. **Permission & policy management** — define [[authorization-policy-types|policies]] (generic, reusable conditions) and bind them to objects via [[authorization-permissions|permissions]].
3. **Policy enforcement** — a [[policy-enforcer]] asks the server for authorization data and gates access using the returned [[requesting-party-token]].

## Resource server settings
On the Resource Server Settings page (a client's Authorization tab) you configure:
- **Policy Enforcement Mode** — `Enforcing` (default; deny if no policy), `Permissive` (allow if no policy associated), or `Disabled` (evaluation off, all access granted). See [[policy-enforcement-mode]].
- **Decision Strategy** — server-wide `Affirmative`/`Unanimous` conflict resolution. See [[decision-strategies]].
- **Remote Resource Management** — whether the resource server may manage resources via the [[protection-api]] (enabled by default) vs. Console-only.

### Default configuration
Creating a resource server seeds: a **default resource** (`Type urn:my-resource-server:resources:default`, URI `/*`), a **`Default Policy`** ("only from realm", a JavaScript policy calling `$evaluation.grant()` unconditionally), and a **Default Permission** binding them. The wildcard `/*` matches all paths — remove or narrow it before writing your own resources, or the always-grant default will leak access.

### Export / import
A resource server's full config (resources+scopes, policies, permissions) can be exported as JSON from the client **Export** tab and re-imported, useful for seeding or updating environments.

## Standards basis
Built on OAuth2 and **User-Managed Access (UMA) 2.0**. RHBK extends OAuth2 so access tokens (the [[requesting-party-token|RPT]]) are issued after evaluating policies; UMA adds person-to-person/person-to-organization sharing via [[permission-ticket|permission tickets]]. Authorization decisions ride on tokens, so this composes with [[tokens-and-sessions]] and [[oidc-token-validation]] (inferred).

## Contradictions / caveats
- The guide's chapter bodies are essentially stable across RHBK **26.0, 26.2, 26.4, 26.6** (`--primary` resolves to 26.6; bodies shown are identical to 26.0). No behavioral divergence is documented between these minors for the core resource/policy/permission model.
- JavaScript policies are **not uploadable** by default — deploy them as a JAR (JavaScript Providers). Treat ABAC attributes as read-only (Threat model mitigation) so users can't edit attributes their own policies trust.
- Legacy **RH-SSO 7.x** ships the same guide but uses the older WildFly/Java adapter ecosystem; client-adapter packaging differs from RHBK. See [[rhsso-to-rhbk-migration]].

## See also
- [[authorization-resources-scopes]]
- [[authorization-policy-types]]
- [[authorization-permissions]]
- [[decision-strategies]]
- [[protection-api]]
- [[requesting-party-token]]
- [[policy-enforcer]]
- [[tokens-and-sessions]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-authorization_services_guide|keycloak reference — authorization_services_guide]]
- [[rhbk-26-6-overview-2|Chapter 1. Authorization services overview]]
- [[rhbk-26-6-service-overview|Chapter 8. Authorization services]]
- [[rhbk-26-6-resource-server-overview|Chapter 3. Managing resource servers]]
<!-- crosslink:end -->
