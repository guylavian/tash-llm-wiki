---
title: How OpenShift authenticates requests and what pod-admission gates control workloads
type: question
domain: openshift
slug: openshift-authentication-pod-admission-gates
summary: "OpenShift authenticates requests via two distinct paths — human users through the internal OAuth server with a configured identity provider, and in-cluster workloads as ServiceAccounts using bound JWTs — then authorizes via Kubernetes RBAC; two independent pod-admission gates (SCC and Pod Security Admission) control what workloads are allowed to run."
sources:
  - kb:authentication-4-22-configuring-internal-oauth
  - kb:authentication-4-22-understanding-identity-provider
  - kb:authentication-4-22-using-rbac
  - kb:concepts-service-accounts
  - kb:concepts-pod-security-admission
  - kb:authentication-4-22-understanding-and-managing-pod-security-admission
  - kb:managing-security-context-constraints
provenance_extracted: 6
provenance_inferred: 2
provenance_ambiguous: 0
status: draft
updated: 2026-07-07
---

# How OpenShift authenticates requests and what pod-admission gates control workloads

## Authentication — two distinct paths

OpenShift separates *who you are* from *what you can do*. Authentication has two completely separate paths:

1. **Human/external users** authenticate through OpenShift's built-in [[openshift-oauth|internal OAuth server]], which delegates the actual credential check to a configured **identity provider** — htpasswd, LDAP, GitHub, GitLab, Google, Keystone, request-header, basic-auth, or OIDC. Once the provider confirms the identity, the server mints a Kubernetes API access token (24‑hour default lifetime). The OAuth server is OpenShift-specific — vanilla Kubernetes has no equivalent, instead relying on external webhook/OIDC/cert authentication plugins.

2. **In-cluster workloads (Pods)** authenticate as a [[service-accounts|ServiceAccount]] — a namespaced, non-human identity with its own bearer JWT. ServiceAccounts bypass the OAuth server entirely. Modern clusters (Kubernetes ≥1.22, OpenShift ≥4.16) use **bound/projected tokens** via `TokenRequest`: short-lived, audience-scoped, auto-rotating, and revoked immediately when the backing object is deleted. Legacy long-lived static Secret tokens are deprecated; OpenShift 4.16+ no longer auto-generates them for new ServiceAccounts. Every namespace gets a `default` ServiceAccount automatically, and a Pod that specifies none gets it assigned. *(inferred: the timeline mapping from the two sources)*

## Authorization — RBAC

Once authenticated, [[kubernetes-rbac|RBAC]] decides what the identity may do. Roles/ClusterRoles define permitted verbs on resources; RoleBindings/ClusterRoleBindings associate identities with roles. OpenShift layers a two-level hierarchy (cluster-wide + project-scoped) and ships default roles: `cluster-admin`, `admin`, `edit`, `view`, `basic-user`, `self-provisioner`, and others. No matching rule ⇒ deny by default.

## Pod-admission gates — two independent controllers

Two separate controllers decide what a pod is actually allowed to *run as*, reconciling in sequence:

1. **[[security-context-constraints|Security Context Constraints (SCC)]]** — OpenShift-only, cluster-level policy. Controls UID, host namespaces, Linux capabilities, volume types. Granted to a ServiceAccount via RBAC. The default `restricted-v2` SCC runs containers as a random non-root UID with most capabilities dropped — stricter than upstream Kubernetes defaults and the #1 cause of "works on kind, CrashLoopBackOff on OpenShift." The fix is to make the image UID-agnostic (group GID 0, group-writable dirs), not to grant `anyuid` broadly.

2. **[[pod-security-admission|Pod Security Admission (PSA)]]** — upstream Kubernetes admission controller, namespace-labeled. Enforces three levels: `privileged`, `baseline`, `restricted` in `enforce`/`audit`/`warn` modes. OpenShift sets `privileged` as the global enforce level, uses `restricted` for warn+audit only, and has a sync controller that auto-sets each namespace's warn/audit labels based on the SCCs its ServiceAccounts can use. System namespaces are permanently pinned to `privileged`.

The SCC controller may mutate the pod first (e.g. defaulting `seccompProfile`), then validates it against the matched SCC; the PSA controller then validates the (possibly mutated) pod against namespace labels. **A pod can pass SCC and still be flagged/rejected by PSA (or vice versa)** — they are independently enforced. *(inferred: two-controller design consequence)*

## Practical triage

| Symptom | First check |
|---|---|
| 401 / login failure | Identity provider config, OAuth server health (`oc get co authentication`) |
| 403 Forbidden | RBAC bindings (`oc auth can-i`, `oc describe rolebinding`) |
| CrashLoopBackOff / admission denied | SCC allowed for the ServiceAccount, PSA namespace labels |

## References

**RH ground-truth (`kb:`):**
- `kb:authentication-4-22-configuring-internal-oauth` — Configuring the internal OAuth server
- `kb:authentication-4-22-understanding-identity-provider` — Understanding identity provider configuration
- `kb:authentication-4-22-using-rbac` — Using RBAC to define and apply permissions
- `kb:concepts-service-accounts` — Service Accounts
- `kb:authentication-4-22-understanding-and-creating-service-accounts` — Understanding and creating service accounts
- `kb:authentication-4-22-understanding-and-managing-pod-security-admission` — Understanding and managing pod security admission
- `kb:concepts-pod-security-admission` — Pod Security Admission
- `kb:managing-security-context-constraints` — Managing security context constraints
- `kb:authentication-4-22-bound-service-account-tokens` — Using bound service account tokens
- `kb:concepts-rbac-good-practices` — RBAC Good Practices

**Wiki pages:**
- [[openshift-auth-and-rbac]] — OpenShift Authentication, RBAC & Pod Security Overview
- [[openshift-oauth]] — OpenShift internal OAuth server
- [[service-accounts]] — ServiceAccounts
- [[kubernetes-rbac]] — Kubernetes RBAC (Roles, Bindings, ClusterRoles)
- [[security-context-constraints]] — Security Context Constraints (SCC)
- [[pod-security-admission]] — Pod Security Admission (PSA)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[authentication-4-22-configuring-internal-oauth|Configuring the internal OAuth server]]
- [[authentication-4-22-understanding-identity-provider|Understanding identity provider configuration]]
- [[authentication-4-22-using-rbac|Using RBAC to define and apply permissions]]
- [[concepts-service-accounts|Service Accounts]]
- [[concepts-pod-security-admission|Pod Security Admission]]
- [[authentication-4-22-understanding-and-managing-pod-security-admission|Understanding and managing pod security admission]]
- [[authentication-4-22-managing-security-context-constraints|Managing security context constraints]]
<!-- crosslink:end -->
