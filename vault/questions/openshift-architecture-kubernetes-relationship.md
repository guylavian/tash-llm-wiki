---
title: OpenShift Container Platform 4 Architecture and Relationship to Kubernetes
type: question
question_tier: conceptual
domain: openshift
slug: openshift-architecture-kubernetes-relationship
summary: OCP 4 is an operator-driven Kubernetes distribution — upstream Kubernetes core plus a Red Hat platform layer that itself runs on operators — adding Routes, in-cluster builds, OLM, SCCs, and an integrated OAuth server.
sources:
  - note:_sources/openshift/openshift-platform.md
  - note:_sources/openshift/kubernetes-workloads.md
  - note:_sources/openshift/kubernetes-networking.md
  - note:_sources/openshift/kubernetes-storage.md
  - web:https://kubernetes.io/docs/home/ (Kubernetes Documentation, fetched 2026-06-25)
  - web:https://docs.redhat.com/en/documentation/openshift_container_platform/4.22 (OpenShift Container Platform 4.22 docs, fetched 2026-06-25)
provenance:
  extracted: 8
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-07
graph_community: "OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)"
---

# OpenShift Container Platform 4 Architecture and Relationship to Kubernetes

**OpenShift Container Platform (OCP) 4 is a Kubernetes distribution: it ships an upstream-conformant Kubernetes core wrapped in an operator-driven Red Hat platform layer.**

## The Two-Layer Architecture

### Layer 1 — Kubernetes Core (identical to upstream)

Every standard Kubernetes object works unchanged:

- **Workloads** — [[kubernetes-pod]] is the unit; [[kubernetes-deployment]] for stateless apps, [[kubernetes-statefulset]] for stateful, [[kubernetes-daemonset]] for per-node agents, Job/CronJob for batch. Health via probes; placement via resource requests/limits. [[openshift-implementation-review]] catalogs the failure modes.
- **Networking** — a [[kubernetes-service]] is a stable virtual endpoint (ClusterIP + DNS) over churning pod IPs; [[network-policy]] is the allow-list firewall (default: all-pods-reachable until a policy selects a pod).
- **Storage** — [[persistent-volume-claim]] requests storage bound to a [[PersistentVolume]]; [[storage-class]] triggers dynamic provisioning via a [[csi-driver]].

### Layer 2 — OpenShift Platform Layer (operator-driven, over Kubernetes)

- **Operator-driven control plane** — the [[cluster-operators|Cluster Version Operator (CVO)]] manages every built-in component as a ClusterOperator, applying release manifests in ordered runlevels during install/upgrade. The [[machine-config|Machine Config Operator (MCO)]] manages RHCOS node-level OS/config state via MachineConfig objects, detecting drift. Application operators install through [[operator-lifecycle-manager|OLM]] via Subscription/InstallPlan/CSV CRDs — three distinct operator control loops under one "the operator is broken" report.
- **[[openshift-route]]** — native external HTTP(S) exposure through the HAProxy router, with edge/passthrough/re-encrypt TLS termination. A [[kubernetes-ingress]] on OCP auto-generates a managed Route.
- **[[buildconfig-s2i|BuildConfig + Source-to-Image (S2I)]]** — images built in-cluster from source code without a Dockerfile; [[image-streams]] trigger redeploys on new tags.
- **[[security-context-constraints]] (SCC)** — the default `restricted-v2` runs containers as a random non-root UID. This is the #1 reason a community image that works on plain Kubernetes fails on OCP.
- **[[openshift-oauth]]** — built-in OAuth server delegates authentication to configured identity providers (LDAP, GitHub, OIDC, htpasswd, etc.) and mints API access tokens. Vanilla Kubernetes delegates auth to external webhook/OIDC/cert plugins instead.
- **[[kubernetes-rbac]]** — standard Kubernetes RBAC with an OpenShift two-level hierarchy (cluster-wide vs project-scoped) and default reconciled cluster roles (`cluster-admin`, `admin`, `edit`, `view`, …).
- **[[pod-security-admission]]** — runs alongside SCCs, with OpenShift auto-syncing per-namespace PSA labels from the SCCs available to the namespace's ServiceAccounts.

### How the Layers Relate

| Domain | Upstream Kubernetes | OpenShift-Only |
|---|---|---|
| External HTTP(S) | Ingress (frozen API) | Route (native, HAProxy, 3 TLS modes) |
| CNI/overlay | Any CNI plugin (pluggable) | [[ovn-kubernetes]] (OVN-over-OVS, default) |
| Node config | Manual or third-party | [[machine-config]] / MCO (OS-level, drift detection) |
| Auth (human) | Webhook/OIDC/cert plugins | [[openshift-oauth]] + identity providers |
| Auth (workload) | ServiceAccount | Same, plus bound-tokens (≥ 4.16) |
| Pod security | [[pod-security-admission]] (upstream) | [[security-context-constraints]] (stricter, OCP-only) |
| Built-in builds | None | BuildConfig/S2I/ImageStreams |
| Platform lifecycle | Manual | CVO + ClusterOperators + runlevels |

### Versioning

OCP 4.x tracks upstream Kubernetes minors. OCP 4.22 maps to Kubernetes ~1.31. Upgrades are operator-driven over channels (`stable-4.x`, EUS). The wiki's openshift brain covers **OCP 4.8 → 4.22** conceptual docs; the corpus-backed reference tier holds 3,813 doc bodies (1,602 Kubernetes + 2,211 OCP 4.22 assemblies).

## See also
- [[openshift-overview]] — the spine page for this topic
- [[openshift-auth-and-rbac]] — auth/RBAC/SCC/PSA in detail
- [[openshift-networking]] — Services → Routes → OVN-Kubernetes → DNS → NetworkPolicy
- [[openshift-workloads]] — controllers, rollout strategies, probes, scheduling
- [[openshift-storage]] — PVC/PV/StorageClass/CSI chain
- [[openshift-builds-and-images]] — S2I, BuildConfig, ImageStreams
- [[openshift-operators-and-olm]] — CVO, OLM, MCO — three operator control loops
- [[openshift-implementation-review]] — symptom→cause MOC

## References

### RH ground-truth (kb: / ref:)
- [[authentication-4-22-managing-security-context-constraints|Managing security context constraints]]
- [[concepts-service|Service]]
- [[concepts-persistent-volumes|Persistent Volumes]]
- [[concepts-network-policies|Network Policies]]
- [[tasks-configure-liveness-readiness-startup-probes|Configure Liveness, Readiness and Startup Probes]]
- [[cicd-4-22-build-strategies|Using build strategies]]
- [[machine-configuration-4-22-machine-configs-configure|Using machine config objects to configure nodes]]
- [[updating-4-22-how-updates-work|How cluster updates work]]
- [[operators-4-22-olm-understanding-olm|Operator Lifecycle Manager concepts and resources]]

### Wiki ([[slug]])
- [[openshift-overview]] · [[cluster-operators]] · [[openshift-auth-and-rbac]] · [[openshift-networking]] · [[openshift-storage]] · [[openshift-workloads]] · [[openshift-builds-and-images]] · [[openshift-operators-and-olm]]
- [[security-context-constraints]] · [[openshift-route]] · [[ovn-kubernetes]] · [[machine-config]] · [[operator-lifecycle-manager]] · [[buildconfig-s2i]] · [[image-streams]] · [[pod-security-admission]] · [[kubernetes-rbac]] · [[openshift-oauth]]
