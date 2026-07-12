---
origin: eval-cohort
title: How does RHBK's fine-grained authorization service work?
type: question
domain: keycloak
slug: how-fine-grained-authorization-works
summary: "RHBK Authorization Services implement a XACML-style PAP/PDP/PEP/PIP architecture layered on OAuth2 and UMA 2.0: you enable a confidential client as a resource server, register [[authorization-resources-scopes|resources and scopes]] (what to protect), write reusable [[authorization-policy-types|policies]] (the conditions), bind them via [[authorization-permissions|permissions]] (who can do what), and enforce with a [[policy-enforcer]] (PEP) that requests an [[requesting-party-token|RPT]] carrying the granted permissions."
question_tier: conceptual
sources:
  - guide:authorization_services_guide
  - kb:authorization_services_guide/overview
  - kb:authorization_services_guide/service_overview
  - kb:authorization_services_guide/resource_server_overview
  - kb:authorization_services_guide/resource_overview
  - kb:authorization_services_guide/policy_overview
  - kb:authorization_services_guide/permission_overview
  - kb:authorization_services_guide/enforcer_overview
  - kb:authorization_services_guide/policy_evaluation_overview
provenance:
  extracted: 15
  inferred: 3
  ambiguous: 0
status: draft
updated: 2026-07-12
---

# How does RHBK's fine-grained authorization service work?

**RHBK Authorization Services implement a XACML-style PAP/PDP/PEP/PIP architecture layered on OAuth2 and UMA 2.0: you enable a confidential client as a resource server, register resources and scopes (what to protect), write reusable policies (the conditions), bind them via permissions (who can do what on what), and enforce with a Policy Enforcement Point that requests an RPT carrying the granted permissions** (`topics/fine-grained-authorization.md:26-40`).

## The four architectural points

RHBK's authorization architecture maps to the XACML reference model (`topics/fine-grained-authorization.md:31-35`):

- **PAP (Policy Administration Point)** — the Admin Console UIs (a client's Authorization tab) plus the [[protection-api]] REST endpoints, where you manage resource servers, resources, scopes, permissions, and policies (`entities/protection-api.md:26-31`).
- **PDP (Policy Decision Point)** — RHBK itself, at the token endpoint. When a client sends an authorization request (`grant_type=urn:ietf:params:oauth:grant-type:uma-ticket`), all [[authorization-permissions|permissions]] and their [[authorization-policy-types|policies]] for the requested resources/scopes are evaluated, and an [[requesting-party-token|RPT]] is returned with the granted permissions (`entities/requesting-party-token.md:24-35`).
- **PEP (Policy Enforcement Point)** — the [[policy-enforcer]] running at the resource server. It intercepts requests, obtains an RPT by talking to the PDP, and gates access based on the permissions the RPT carries. RHBK ships Java and JavaScript enforcers; you can build your own against the REST API (`entities/policy-enforcer.md:24-30`).
- **PIP (Policy Information Point)** — attributes from the identity (token claims, roles, groups) and from the runtime (claims pushed via `claim_token`, the evaluation context) that policies read during evaluation (`entities/policy-evaluation-tool.md:24-28`).

## The three processes

### 1. Resource management — define what is protected

Enable a **confidential client** as a *resource server* (Authorization tab → toggle ON). Then register:

- **Resources** — the objects to protect: a page, REST endpoint, file, EJB, or group/type of them. Each resource has a Name, Type (grouping string for typed permissions), URIs (relative paths like `/accounts/*`), Scopes, Attributes (key/value for ABAC), and an Owner (`entities/authorization-resources-scopes.md:26-33`).
- **Scopes** — bounded actions on a resource: `view`, `edit`, `delete`, or a data slice like `cost`. Managed under the **Authorization Scopes** tab (`entities/authorization-resources-scopes.md:35-36`).

Resources and scopes can be managed either through the Admin Console or remotely via the [[protection-api]] Resource Registration Endpoint — `POST /realms/{realm}/authz/protection/resource_set` (`entities/protection-api.md:26-28`).

### 2. Permission and policy management — define the conditions

**Policies** are generic, reusable conditions decoupled from what they protect. Nine built-in types (`entities/authorization-policy-types.md:26-35`):

- **User** — grant to named users.
- **Role** — grant if the requester holds listed roles (optionally **Required** = all roles). **Fetch Roles** reads roles server-side instead of from the token.
- **Client** — grant to named clients.
- **Group** — grant to group members. **Extend to Children** includes subgroups.
- **Client scope** — grant if the client holds listed scopes.
- **Regex** — match a resolved attribute against a regex.
- **Time** — grant within a time window, optionally repeating.
- **JavaScript** — arbitrary logic via the `$evaluation` API, supporting ABAC, RBAC checks, and claim pushing. Deployed as a JAR (not uploadable via UI by default).
- **Aggregated** — combine sub-policies with a [[decision-strategies|Decision Strategy]].

Every policy has a **Logic** field (positive/negate) that inverts the outcome after evaluation.

**Permissions** bind policies to resources/scopes (`entities/authorization-permissions.md:24-34`):

- **Resource-based permission** — protects whole resources with a set of policies. Optionally **Apply To Resource Type** to protect all resources of a given type.
- **Scope-based permission** — protects specific scopes, optionally narrowed to one resource.

Each permission carries its own **Decision Strategy** (`Unanimous`/`Affirmative`/`Consensus`), separate from the server-wide strategy.

### 3. Policy enforcement — gate access at the resource server

The [[policy-enforcer]] at the resource server enforces decisions. Two flows (`entities/requesting-party-token.md:24-35`):

**UMA flow:**
1. Client accesses a protected resource without an RPT.
2. Resource server returns `401` with `WWW-Authenticate: UMA realm="...", ticket="..."` (`entities/permission-ticket.md:26-30`).
3. Client POSTs `grant_type=urn:ietf:params:oauth:grant-type:uma-ticket` with the **ticket** to RHBK's token endpoint.
4. RHBK evaluates all policies and returns an RPT (`200`) or `403 request_denied`.

**UMA-less (direct) flow:**
- Client sends `grant_type=uma-ticket` with `permission=RESOURCE_ID#SCOPE_ID` (no ticket needed) and `audience=<resource-server-client-id>`.
- RHBK evaluates policies directly and returns an RPT.

The RPT is a standard OAuth2 access token carrying the granted permissions. It is validated by the resource server (offline via JWKS or online via introspection) just like any access token (`entities/requesting-party-token.md:48-49`).

### ### Decision combination

Decisions cascade through three levels (`entities/decision-strategies.md:28-35`, the three-context framing is `(inferred)` in the source):
1. **Per-policy Logic** — negate a policy's result or leave as-is.
2. **Per-permission Decision Strategy** — combine that permission's policies into a grant/deny (`Unanimous` = all must pass, `Affirmative` = any passes, `Consensus` = majority).
3. **Resource-server-wide Decision Strategy** — resolve conflicts between permissions on the same resource/scope.

The **Policy Enforcement Mode** (`entities/policy-enforcement-mode.md:24-27`) controls what happens when no policy is associated: `Enforcing` (deny by default), `Permissive` (allow), or `Disabled` (skip all evaluation).

### Resource server defaults — watch the trap

Creating a resource server auto-seeds: a **Default Resource** (`Type urn:...:default`, URI `/*`), a **`Default Policy`** (always-grant JavaScript), and a **Default Permission** binding them. The wildcard `/*` matches all paths — remove or narrow it before adding production resources or the always-grant default leaks access (`topics/fine-grained-authorization.md:48-49`).

## Standards basis

Built on OAuth2 and **User-Managed Access (UMA) 2.0** (`topics/fine-grained-authorization.md:55`, the OAuth2/UMA framing is `(inferred)` in the source). The UMA layer adds person-to-person sharing: a resource **owner** (e.g. Alice) can share her resource (e.g. her bank account) with a **requesting party** (Bob) for specific scopes, managed under Account Console → **My Resources**. The `submit_request=true` parameter makes RHBK persist permission requests for the owner to approve asynchronously (`entities/permission-ticket.md:32-36`).

## See also
- [[fine-grained-authorization]]
- [[authorization-resources-scopes]]
- [[authorization-policy-types]]
- [[authorization-permissions]]
- [[decision-strategies]]
- [[policy-enforcer]]
- [[policy-enforcement-mode]]
- [[protection-api]]
- [[requesting-party-token]]
- [[permission-ticket]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-authorization_services_guide|keycloak reference — authorization_services_guide]]
- [[rhbk-26-6-overview-2|Chapter 1. Authorization services overview]]
- [[rhbk-26-6-service-overview|Chapter 8. Authorization services]]
- [[rhbk-26-6-resource-server-overview|Chapter 3. Managing resource servers]]
- [[rhbk-26-6-resource-overview|Chapter 4. Managing resources and scopes]]
- [[rhbk-26-6-policy-overview|Chapter 5. Managing policies]]
- [[rhbk-26-6-permission-overview|Chapter 6. Managing permissions]]
- [[rhbk-26-6-enforcer-overview|Chapter 9. Policy enforcers]]
- [[rhbk-26-6-policy-evaluation-overview|Chapter 7. Evaluating and testing policies]]
<!-- crosslink:end -->
