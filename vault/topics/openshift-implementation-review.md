---
title: OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: openshift
slug: openshift-implementation-review
summary: "The evaluation lens and Map of Content for the openshift brain — a rule → anti-pattern → symptom checklist across workloads, networking, storage, cluster-auth, and operators-olm, plus a symptom → likely-cause reverse index that turns a kubectl/oc symptom (CrashLoopBackOff, Pending, 503, Forbidden, Degraded) into a cause page."
sources:
  - note:_sources/openshift/kubernetes-workloads.md
  - note:_sources/openshift/kubernetes-networking.md
  - note:_sources/openshift/kubernetes-storage.md
  - note:_sources/openshift/openshift-platform.md
  - kb:managing-security-context-constraints
  - kb:network-policies
  - kb:persistent-volumes
  - kb:pod-v1
  - kb:horizontal-pod-autoscale
  - kb:manage-resources-containers
  - kb:assign-memory-resource
  - kb:statefulset
  - kb:service
  - kb:understanding-persistent-storage
  - kb:troubleshooting-operator-issues
  - kb:authentication-4-22-using-rbac
  - kb:concepts-service-accounts
  - kb:authentication-4-22-configuring-internal-oauth
  - kb:authentication-4-22-understanding-and-managing-pod-security-admission
  - kb:operators-4-22-olm-understanding-olm
  - kb:updating-4-22-how-updates-work
  - kb:machine-configuration-4-22-index
provenance_extracted: 13
provenance_inferred: 21
provenance_ambiguous: 0
symptoms:
  - "CrashLoopBackOff"
  - "ImagePullBackOff"
  - "Pending"
  - "ContainerCreating"
  - "503.*router"
  - "OOMKilled"
  - "Forbidden.*cannot"
  - "violates PodSecurity"
  - "NodeDegraded"
  - "InstallPlanFailed|ResolutionFailed|CatalogSourcesUnhealthy"
tags: [troubleshooting, concept]
status: draft
updated: 2026-07-02
graph_community: "OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)"
---

# OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `openshift` domain.** It indexes the workload / networking / storage / platform pages into a forward checklist (rule → anti-pattern → symptom) and a reverse index (symptom → likely cause) so a `kubectl`/`oc` symptom can be turned into a cause page. The OpenShift analogue of [[sso-implementation-review]], [[active-directory-implementation-review]], and [[cisco-ios-xe-implementation-review]]; grow it as pages land via INGEST.

---

## Health checklist

### Workloads

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Set resource **requests** so the scheduler can place the pod | No requests, or requests larger than any node | Pod stuck **Pending** (`FailedScheduling: Insufficient cpu/memory`) | [[kubernetes-pod]] |
| Set a realistic **memory limit**; size the app to it | Limit far below real usage | Container **OOMKilled** → restarts → CrashLoopBackOff | [[kubernetes-pod]] |
| Make the app **UID-agnostic** for OpenShift's random non-root UID | Image hardcodes root / writes to a UID-owned path | CrashLoopBackOff on OCP, runs fine on plain k8s | [[security-context-constraints]] |
| Use **readiness** to gate traffic, **liveness** to restart, distinctly | Liveness pointed at a slow/deep dependency | Healthy pod killed in a restart loop under load | [[kubernetes-pod]] |
| Use a **StatefulSet** when identity/storage must be stable | Stateful app on a Deployment | Data loss / split identity on rescheduling | [[kubernetes-statefulset]] |

### Networking

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Match the Service **selector** to the pods' labels | Typo'd selector / wrong label | Service has **no endpoints**; clients/Route get connection refused or 503 | [[kubernetes-service]] |
| Remember NetworkPolicy is **default-deny once a pod is selected** | Add an ingress policy, forget egress/DNS | App can't reach DNS/other services after the first policy lands | [[network-policy]] |
| Pick the right Route **TLS mode** for the app | `edge` in front of an app that also terminates TLS | TLS handshake errors / double-encryption | [[openshift-route]] |
| Expose via **Route/Ingress**, not NodePort, for HTTP | NodePort/hostPort hacks on OCP | Fragile external access; SCC rejects hostPort | [[openshift-route]] |

### Storage

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Ensure a **default StorageClass** (or set `storageClassName`) | PVC with no class and no default | PVC stuck **Pending**; pod stuck ContainerCreating | [[persistent-volume-claim]] |
| Use an **RWX**-capable backend when many pods share a volume | RWO volume mounted by a multi-replica Deployment | Second+ pod stuck ContainerCreating (`Multi-Attach`) | [[persistent-volume-claim]] |
| Choose `reclaimPolicy: Retain` for data you can't lose | `Delete` (dynamic default) on critical data | Volume deleted when the PVC is removed | [[persistent-volume-claim]] |

### Platform (OpenShift)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Triage cluster health via **ClusterOperators** first | Debugging an app while a platform operator is Degraded | App-level symptoms with a root cause in `oc get co` | [[cluster-operators]] |
| Grant SCC narrowly to a **ServiceAccount** | Granting `anyuid`/`privileged` cluster-wide to "make it work" | Security regression; the real bug (root image) unfixed | [[security-context-constraints]] |
| Pin image tags / use ImageStreams + pull secrets | `:latest` from an unauthenticated/unreachable registry | **ImagePullBackOff** / non-reproducible deploys | [[kubernetes-pod]] |

### Authentication & RBAC

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Bind `cluster-admin` cluster-wide only via a **ClusterRoleBinding** | Binding `cluster-admin` with a *local* RoleBinding, expecting real cluster-admin | User only has admin-plus-a-few in one project; confusing "why can't I do X cluster-wide" reports | [[kubernetes-rbac]] |
| Grant least privilege; avoid `get pods/exec` / wildcard verbs | Broad verbs on `*` to unblock a user quickly | Over-privileged identity flagged in a security review | [[kubernetes-rbac]] |
| Use **bound/projected ServiceAccount tokens** (short-lived, auto-rotating) | Minting/mounting a legacy long-lived Secret token | Static credential leak risk; token never expires or rotates | [[service-accounts]] |
| Make workloads **UID-agnostic** for the default `restricted-v2` SCC | Image hardcodes root / a fixed UID-owned path | **CrashLoopBackOff** on OpenShift; fine on plain Kubernetes | [[security-context-constraints]] |
| Treat SCC and Pod Security Admission as two independent gates | Assuming a passing SCC also clears PSA (or vice versa) | Pod admitted by SCC but still flagged/rejected by PSA `warn`/`enforce` | [[pod-security-admission]] |
| Check `oc get co` for `authentication`/`oauth-apiserver` before blaming config | Debugging OAuth client config while the platform auth operator is Degraded | Login/token failures cluster-wide, root cause is a Degraded ClusterOperator | [[openshift-oauth]], [[cluster-operators]] |

### Operators & OLM

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Check `oc get co` (CVO) before `oc get subs` (OLM) for "an operator is broken" | Triaging an application Operator's Subscription when the real fault is a platform ClusterOperator | Wrong control loop investigated; wasted triage time | [[cluster-operators]], [[operator-lifecycle-manager]] |
| Match an Operator's install mode to its **OperatorGroup** target namespaces | Installing a `SingleNamespace`-only Operator into a group targeting many namespaces | Operator never reaches `Succeeded`; CSV stuck | [[operator-lifecycle-manager]] |
| Watch Subscription conditions during install/upgrade | Ignoring `CatalogSourcesUnhealthy` / `ResolutionFailed` | Operator install silently stuck, no obvious error in the console | [[operator-lifecycle-manager]] |
| Let node-level MachineConfig rollout finish before declaring the upgrade "done" | Assuming "cluster reports updated" means every node is updated | Nodes still draining/rebooting after the control plane reports success | [[machine-config]], [[cluster-operators]] |
| Fix configuration drift at the source, not by re-editing the node | Hand-editing a file MachineConfig also manages, repeatedly | Node/pool flips **Degraded** (`NodeDegraded`, `content mismatch for file`) again after each reboot | [[machine-config]] |

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| Pod **Pending**, `FailedScheduling: Insufficient cpu/memory` | Requests don't fit any node (or no requests + cluster full) | [[kubernetes-pod]] |
| Pod **Pending/ContainerCreating** on a fresh PVC | No default StorageClass / PVC unsatisfiable | [[persistent-volume-claim]] |
| 2nd replica stuck ContainerCreating (`Multi-Attach error`) | RWO volume on a multi-pod workload; needs RWX | [[persistent-volume-claim]] |
| **CrashLoopBackOff** only on OpenShift, fine on plain k8s | Image assumes root; blocked by `restricted-v2` SCC | [[security-context-constraints]] |
| Container **OOMKilled** then restarts | Memory limit below real usage | [[kubernetes-pod]] |
| **ImagePullBackOff** | Bad tag, missing pull secret, or unreachable registry | [[kubernetes-pod]] |
| Service/Route returns **503** from the router | Service has no ready endpoints (selector typo / failing readiness) | [[kubernetes-service]], [[openshift-route]] |
| App suddenly can't reach DNS/other services | A NetworkPolicy selected the pod → default-deny, egress/DNS not allowed | [[network-policy]] |
| Healthy pod killed in a restart loop under load | Liveness probe too aggressive / pointed at a deep dependency | [[kubernetes-pod]] |
| App-level errors but root cause cluster-wide | A platform **ClusterOperator** is Degraded/Progressing | [[cluster-operators]] |
| **Forbidden**: `cannot get/list/create <resource>` | Missing/mis-scoped RBAC Role or RoleBinding | [[kubernetes-rbac]] |
| `cluster-admin` bound but user still limited to one project | `cluster-admin` granted via a local RoleBinding, not a ClusterRoleBinding | [[kubernetes-rbac]] |
| Pod rejected: `violates PodSecurity "restricted"` | Namespace PSA label stricter than the pod's securityContext | [[pod-security-admission]] |
| Login/token requests failing cluster-wide | `authentication`/`oauth-apiserver` ClusterOperator Degraded, not OAuth client misconfig | [[openshift-oauth]], [[cluster-operators]] |
| Operator stuck installing, `InstallPlanFailed`/`ResolutionFailed`/`CatalogSourcesUnhealthy` | OLM Subscription/CatalogSource/InstallPlan issue | [[operator-lifecycle-manager]] |
| `oc get co` shows a component **Degraded**/stuck `Progressing=True` | CVO runlevel blocked on that ClusterOperator | [[cluster-operators]] |
| Node/pool flips **Degraded**, `NodeDegraded`, `content mismatch for file` | MachineConfig configuration drift | [[machine-config]] |
| **CrashLoopBackOff** right after a probe/liveness change, or after a deploy | Probe misconfig, resource limits, or image/SCC issue — see the workloads area | [[openshift-workloads]] |
| PVC stuck **Pending** | StorageClass / capacity / access-mode mismatch — see the storage area | [[openshift-storage]] |
| Route/Service returns **503** | No ready endpoints, NetworkPolicy, or Route TLS mode mismatch — see the networking area | [[openshift-networking]] |

---

## Domain map — pages by area

### Workloads
- [[kubernetes-pod]] — the unit; probes, requests/limits, OOM
- [[kubernetes-statefulset]] — stable identity + per-pod storage

### Networking
- [[kubernetes-service]] — stable endpoint over pod churn; endpoints/readiness
- [[network-policy]] — default-deny allow-list firewall
- [[openshift-route]] — native external HTTP(S) + TLS modes
- [[kubernetes-ingress]] — upstream HTTP routing object

### Storage
- [[persistent-volume-claim]] — PV/PVC, StorageClass, CSI, reclaim policy

### Platform
- [[security-context-constraints]] — the SCC admission model
- [[cluster-operators]] — operator-driven cluster + day-2 triage
- [[pod-security-admission]] — upstream PSA, layered alongside SCC

### Authentication & RBAC
- [[kubernetes-rbac]] — Roles/ClusterRoles/Bindings, cluster vs local
- [[service-accounts]] — non-human identity for Pods
- [[openshift-oauth]] — internal OAuth server + identity providers
- [[openshift-auth-and-rbac]] — spine topic for this area

### Operators & OLM
- [[operator-lifecycle-manager]] — CatalogSource/Subscription/InstallPlan/CSV
- [[cluster-operators]] — CVO-managed platform ClusterOperators
- [[machine-config]] — node-level day-2, MachineConfigPools, drift
- [[openshift-operators-and-olm]] — spine topic for this area

## See also
- [[openshift-overview]] — the brain's spine
- [[sso-implementation-review]] · [[active-directory-implementation-review]] · [[cisco-ios-xe-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[authentication-4-22-managing-security-context-constraints|Managing security context constraints]]
- [[concepts-network-policies|Network Policies]]
- [[concepts-persistent-volumes|Persistent Volumes]]
- [[microshift-rest-api-4-22-pod-v1|Pod v1]]
- [[concepts-horizontal-pod-autoscale|Horizontal Pod Autoscaling]]
- [[concepts-manage-resources-containers|Resource Management for Pods and Containers]]
- [[tasks-assign-memory-resource|Assign Memory Resources to Containers and Pods]]
- [[concepts-statefulset|StatefulSets]]
- [[concepts-service|Service]]
- [[storage-4-22-understanding-persistent-storage|Understanding persistent storage]]
- [[support-4-22-troubleshooting-operator-issues|Troubleshooting Operator issues]]
- [[authentication-4-22-using-rbac|Using RBAC to define and apply permissions]]
- [[concepts-service-accounts|Service Accounts]]
- [[authentication-4-22-configuring-internal-oauth|Configuring the internal OAuth server]]
- [[authentication-4-22-understanding-and-managing-pod-security-admission|Understanding and managing pod security admission]]
- [[operators-4-22-olm-understanding-olm|Operator Lifecycle Manager concepts and resources]]
- [[updating-4-22-how-updates-work|How cluster updates work]]
- [[machine-configuration-4-22-index|Machine configuration overview]]
<!-- crosslink:end -->
