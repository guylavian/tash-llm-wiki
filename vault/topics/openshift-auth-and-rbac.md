---
title: OpenShift Authentication, RBAC & Pod Security — Overview
type: topic
domain: openshift
slug: openshift-auth-and-rbac
summary: "The spine page for the cluster-auth area: how OpenShift authenticates a request (internal OAuth + identity providers, or a ServiceAccount JWT), how it authorizes the resulting identity (Kubernetes RBAC), and the two independent pod-admission gates (SCC and Pod Security Admission) that decide what a pod is allowed to actually run as."
sources:
  - kb:authentication-4-22-configuring-internal-oauth
  - kb:authentication-4-22-understanding-identity-provider
  - kb:authentication-4-22-using-rbac
  - kb:concepts-service-accounts
  - kb:authentication-4-22-understanding-and-creating-service-accounts
  - kb:concepts-pod-security-admission
  - kb:authentication-4-22-understanding-and-managing-pod-security-admission
  - kb:managing-security-context-constraints
provenance_extracted: 6
provenance_inferred: 4
provenance_ambiguous: 0
tags: [cluster-auth, security]
status: draft
updated: 2026-07-02
graph_community: "OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)"
---

# OpenShift Authentication, RBAC & Pod Security — Overview

**Three separate questions, three separate control loops: who are you (authentication), what can you do (RBAC authorization), and what may your pod actually run as (SCC + Pod Security Admission).** Conflating them is the single biggest source of "it's a permissions problem" mis-triage in this area.

## 1. Authentication — who is making the request
Two distinct identity paths:
- **Human/external users** authenticate through OpenShift's built-in [[openshift-oauth|internal OAuth server]], which delegates the actual credential check to a configured **identity provider** — htpasswd, LDAP, GitHub, GitLab, Google, Keystone, request-header, basic-auth, or OIDC — and mints a Kubernetes-API access token (24h default lifetime) once the identity provider confirms who the caller is.
- **In-cluster workloads** authenticate as a [[service-accounts|ServiceAccount]] — a namespaced non-human identity with its own bearer JWT, entirely bypassing the OAuth server. Modern (≥1.22 upstream, and OpenShift ≥4.16 for the pull-secret/token generation change) ServiceAccounts get short-lived, auto-rotating **bound tokens** via `TokenRequest`; long-lived static Secret tokens are legacy and no longer auto-created.

Neither path implies authorization — that's a separate step, deliberately.

## 2. Authorization — what the identity may do
[[kubernetes-rbac|RBAC]] evaluates the identity (user/group, or a ServiceAccount's `system:serviceaccount:<project>:<name>` groups) against bound **Roles**/**ClusterRoles**: cluster-wide allow rules first, then project-local allow rules, then deny by default. OpenShift's default cluster roles (`cluster-admin`, `admin`, `edit`, `view`, `basic-user`, `self-provisioner`, …) are reconciled on every upgrade — a customized default role stops being auto-reconciled and needs manual upkeep thereafter (inferred: this is the practical upgrade-hygiene consequence of the reconciliation behavior). A `RoleBinding` referencing a `ClusterRole` scoped to one project is the standard reuse pattern; binding `cluster-admin` via a *local* binding is a well-documented trap (only grants admin-plus-a-few in that one project, not real cluster-admin).

## 3. Pod admission — what the pod may actually request
Two **independent** controllers reconcile in sequence, and both matter:
- **[[security-context-constraints|Security Context Constraints (SCC)]]** — OpenShift-only, granted to a ServiceAccount, decides UID, host namespaces, capabilities, volume types. Default `restricted-v2` runs random non-root UIDs — stricter than upstream Kubernetes defaults, and the top cause of "works on kind, CrashLoopBackOff on OpenShift."
- **[[pod-security-admission|Pod Security Admission (PSA)]]** — upstream Kubernetes, namespace-labeled `enforce`/`audit`/`warn` against the `privileged`/`baseline`/`restricted` Pod Security Standards. OpenShift enforces `privileged` globally and only warns/audits `restricted`, then auto-syncs each namespace's warn/audit labels to track the SCCs its ServiceAccounts can use.

A pod can clear SCC admission and still trip a PSA warning (or vice versa) — they don't merge into one check (inferred: consequence of the two-controller design, not stated as a single sentence in either source).

## Practical triage order
1. `oc get co` first if the symptom looks platform-wide (see [[cluster-operators]]) — an auth-adjacent symptom can be a Degraded `authentication` or `oauth-apiserver` ClusterOperator, not a config mistake.
2. `oc auth can-i` / `oc describe rolebinding` for a Forbidden error — RBAC, not identity.
3. `oc get events` / pod describe for SCC/PSA admission denials — check which SCC the ServiceAccount is actually allowed, not just what's requested.
4. Never widen SCC/RBAC broadly to "make it work" — fix the workload (UID-agnostic image, correct ServiceAccount) instead; see [[security-context-constraints]]'s anti-pattern note.

## See also
- [[kubernetes-rbac]] · [[service-accounts]] · [[openshift-oauth]] · [[pod-security-admission]] · [[security-context-constraints]]
- [[openshift-overview]] · [[openshift-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[authentication-4-22-configuring-internal-oauth|Configuring the internal OAuth server]]
- [[authentication-4-22-understanding-identity-provider|Understanding identity provider configuration]]
- [[authentication-4-22-using-rbac|Using RBAC to define and apply permissions]]
- [[concepts-service-accounts|Service Accounts]]
- [[authentication-4-22-understanding-and-creating-service-accounts|Understanding and creating service accounts]]
- [[concepts-pod-security-admission|Pod Security Admission]]
- [[authentication-4-22-understanding-and-managing-pod-security-admission|Understanding and managing pod security admission]]
- [[authentication-4-22-managing-security-context-constraints|Managing security context constraints]]
<!-- crosslink:end -->
