---
title: "OpenShift: CrashLoopBackOff from runAsNonRoot + Route 503 despite Ready 1/1"
type: question
question_tier: support-kb
domain: openshift
slug: ocp-scc-root-crashloopbackoff-route-503
summary: "Why a UID-0 image works on vanilla K8s but fails on OpenShift with `container has runAsNonRoot and image will run as root`, how to fix it (three ways ranked by security), and how to debug a 503 from a Route against a pod that shows Ready 1/1."
sources:
  - note:_sources/openshift/openshift-platform.md
  - note:_sources/openshift/kubernetes-networking.md
  - note:_sources/openshift/kubernetes-workloads.md
  - kb:managing-security-context-constraints
  - kb:create-images
  - kb:nw-configuring-routes
  - kb:ingress-operator
  - kb:service
  - kb:pod-v1
  - kb:network-policies
  - web:https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/managing-security-context-constraints (OCP 4.22 — Managing SCCs, fetched 2026-06-28)
  - web:https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-and-managing-pod-security-admission (OCP 4.22 — Understanding and managing PSA, fetched 2026-06-28)
  - web:https://kubernetes.io/docs/concepts/security/pod-security-admission/ (K8s PSA, fetched 2026-06-28)
provenance_extracted: 16
provenance_inferred: 6
provenance_ambiguous: 0
status: draft
updated: 2026-06-28
graph_community: "OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)"
---

# CrashLoopBackOff (runAsNonRoot) + Route 503 on OpenShift — Root Causes and Fixes

> ⚠️ Out of corpus coverage — `openshift` holds `conceptual` only; this is a `support-kb` question and that tier is not ingested; verify against the primary source.

## Part 1 — Why the image fails on OpenShift but runs on vanilla K8s

### The mechanism: Security Context Constraints (SCC)

OpenShift enforces pod security through **Security Context Constraints (SCCs)** — an admission mechanism that mutates a pod's `securityContext` at creation time and validates the result against the cluster policy. There is **no equivalent on vanilla Kubernetes** (the nearest upstream analogue is Pod Security Admission, which is *validating-only* and namespace-scoped).

On OCP 4.x, the **default SCC** granted to all authenticated users' ServiceAccounts is **`restricted-v2`** (see [[security-context-constraints]]). At admission, `restricted-v2` applies:

- **`RunAsUser` strategy: `MustRunAsRange`** — the SCC assigns a **random high UID** from the namespace's `openshift.io/sa.scc.uid-range` annotation (e.g. `1000840000/10000`). Every namespace gets a different block; the pod's containers get the *first* value of that block as `runAsUser`.
- **`runAsNonRoot: true`** is set on the pod's `securityContext` by the SCC admission mutation (inferred: the SCC controller sets this as part of the `restricted-v2` mutation to enforce the non-root contract at the kubelet level).
- All Linux capabilities are dropped (except `NET_BIND_SERVICE` if explicitly requested).
- `allowPrivilegeEscalation` is forced to `false`.
- `seccompProfile` is defaulted to `runtime/default`.

When the pod reaches the kubelet on the node, the kubelet inspects the container image's runtime configuration. If the image has **no `USER` directive** (or `USER 0`), the process would start as UID 0. The kubelet detects the conflict between `runAsNonRoot: true` and the image's UID 0 and refuses to start the container, producing:

```
Error: container has runAsNonRoot and image will run as root (UID 0)
```

### Why vanilla K8s doesn't block this

Vanilla Kubernetes does **not** enable SCC admission. The default `PodSecurity` admission on upstream K8s 1.25+ is **warning-only** unless the namespace is explicitly labeled with an `enforce` mode. Even in `restricted` profile, the upstream PSA only *validates* — it does **not mutate** the pod. A Deployment with `runAsUser: 0` and no explicit `runAsNonRoot` will start (and run as root) unless the operator explicitly labels the namespace `pod-security.kubernetes.io/enforce: restricted`, which would then reject it at admission. The team's "works at home" cluster likely has either:
- No Pod Security Admission configured at all (the pre-1.25 default).
- The namespace in `privileged` or `baseline` mode, which allows root containers.

### How this differs from "the thing that replaced it"

In upstream Kubernetes, **PodSecurityPolicy (PSP)** was the original admission-time pod security mechanism. PSP was **deprecated in K8s 1.25 and removed in 1.25+** (actually shipped the K8s 1.25 release removed PSP). It was replaced by **Pod Security Admission (PSA)**, a simpler three-profile system (privileged / baseline / restricted) controlled via namespace labels.

The key differences between SCC and PSA:

| Dimension | SCC (OpenShift) | PSA (upstream K8s) |
|---|---|---|
| **Scope** | Cluster-wide RBAC-based policy | Per-namespace label on `Namespace` object |
| **Mutation** | **Mutates** the pod (assigns UID, sets `runAsNonRoot`, drops caps) | **Validating only** — rejects non-compliant pods but does not change them |
| **Granularity** | Fine-grained: per-pod, per-ServiceAccount via RBAC, with ~15 control knobs | Three coarse profiles only (`privileged` / `baseline` / `restricted`) |
| **UID strategy** | `MustRunAsRange`, `MustRunAsNonRoot`, `RunAsAny`, or specific numeric ranges | Only `restricted` profile enforces `runAsNonRoot: true` |
| **SELinux** | Full SELinux context control (`MustRunAs`, `RunAsAny`) | Not covered |
| **FSGroup/Groups** | Controls FSGroup strategy and supplemental groups | Only covered in `restricted` profile (sets `fsGroup` to `MustRunAs`) |
| **Lifecycle on OCP** | Still primary; PSA runs **alongside** SCC on OCP 4.11+; a synchronisation controller maps SCC permissions to PSA namespace labels | The standard (PSA) on all K8s 1.25+ |

On OpenShift 4.11+, **PSA runs alongside SCC** — it did not replace it (see: `post-installation-configuration-4-22-security-basics.md`). The SCC admission runs first and mutates the pod; then PSA validates the result against the namespace label. A synchronization controller (`security.openshift.io/scc.podSecurityLabelSync`) translates SCC permissions into PSA labels so the two don't conflict (inferred). OpenShift continues to evolve SCC itself: OCP 4.11 introduced `restricted-v2` (drops ALL caps, forces `runtime/default` seccomp, locks `allowPrivilegeEscalation`), and `restricted-v3` adds `RequirePodLevel` user namespace isolation.

---

## Part 2 — Three ways to solve the UID problem, ranked by security

### Method 1 (worst — "easy fix"): Bind the pod's ServiceAccount to the `anyuid` SCC

```bash
oc adm policy add-scc-to-user anyuid -z default -n payments-prod
```

This assigns the `anyuid` SCC to the `default` ServiceAccount (or whatever SA the Deployment uses). The `anyuid` SCC sets `RunAsUser: RunAsAny`, meaning the pod keeps the image's own USER (UID 0). The pod starts — and runs as root.

**Why this is the worst in prod (three reasons):**

1. **Global security regression.** The `anyuid` SCC allows running with **any UID** including 0 — it removes the entire non-root guarantee. A single vulnerability (RCE) in the container has full root privileges inside the container and may escape via kernel CVEs.
2. **Sets a dangerous precedent.** Other teams see "just add `anyuid`" as the fix and it becomes the org-wide default, bypassing the entire SCC security model.
3. **Audit / compliance failure.** PCI-DSS, SOC2, and most compliance frameworks require containers to run non-root. `anyuid` makes that certification impossible to prove.

### Method 2 (better): Grant the `nonroot` SCC

```bash
oc adm policy add-scc-to-user nonroot -z default -n payments-prod
```

The `nonroot` SCC uses `MustRunAsNonRoot` strategy — it sets `runAsNonRoot: true` but allows any **non-root** UID. Unlike `restricted-v2`, it does **not** force a random UID from the namespace range; instead, the image's own `USER` directive is honored as long as that user is non-root.

**Best for:** Teams that can fix the image's USER directive but don't want to deal with the random-UID portability problems (file permissions, umask, etc.).

**Downside:** Still requires the image to declare a non-root user (`USER 1001`). If the image's entrypoint writes to UID-owned paths, those paths must be group-writable. Less restrictive than `restricted-v2` on other dimensions too (SELinux is `MustRunAs` but not as constrained on capabilities).

### Method 3 (best — OpenShift best practice): Make the image UID-agnostic

This is the **recommended approach** by Red Hat (see `openshift-images-4-22-create-images.md`). The image stays under the default `restricted-v2` SCC, which assigns a random high UID — and the image must work regardless of which UID it gets.

**What to change in the Dockerfile:**

```dockerfile
# 1. Declare a non-root numeric user (named users may not resolve under random UID)
RUN useradd -u 1001 -r -g 0 -d /opt/app -s /sbin/nologin default
USER 1001

# 2. Make all writable directories group-writable by root group (GID 0)
RUN chgrp -R 0 /opt/app && chmod -R g=u /opt/app

# 3. Don't bind privileged ports (< 1024); use a port >= 1024
EXPOSE 8080
```

CRI-O supports **`/etc/passwd` injection** — it inserts the assigned random UID into `/etc/passwd` so `id` and `whoami` work. This means the image **must not have a static `/etc/passwd`** that lists the old numeric UID, or the injection fails (an error that silently breaks UID resolution). (inferred from `openshift-images-4-22-create-images.md`)

**Why this is the best:**
- No SCC change needed → the default `restricted-v2` applies → maximum security
- The same image runs identically across OpenShift, vanilla K8s with PSA `restricted`, and any cluster that enforces non-root
- Passes compliance audits (containers run non-root, DAC is minimized)
- Survives cluster upgrades (SCC names change, but the image behavior doesn't)

### Security ranking summary

| Method | Security posture | Prod suitability | Effort |
|---|---|---|---|
| 1 — `anyuid` SCC | ❌ Critical regression — runs as root | **Do not use** | Very low (1 `oc` command) |
| 2 — `nonroot` SCC | ⚠️ Non-root but relaxed vs default | Acceptable with constraints | Low (1 `oc` command + image USER fix) |
| 3 — UID-agnostic image | ✅ Follows PoLP (Principle of Least Privilege) | **Recommended for all production** | Moderate (Dockerfile changes + testing) |

---

## Part 3 — Route 503 despite pod Ready 1/1: causes and debug flow

The OpenShift HAProxy router returns **HTTP 503** when it cannot forward traffic to any healthy backend endpoint. A pod showing `Ready 1/1` passes its readiness probe — but that does not guarantee the application is accepting traffic on the Route's target port. Here are the three most common root causes and how to differentiate them:

### Cause A — Service has no endpoints (selector mismatch)

**Most common.** The Route targets a Service whose `selector` labels don't match the pod's labels. The Service has an empty endpoint set. The pod is healthy and ready — but invisible to the router.

**Diagnose:**
```bash
oc get endpoints -n payments-prod
# Shows: NAME          ENDPOINTS        AGE
#        my-svc        <none>           5m
#           ^^^^^^^^ — empty = selector mismatch or no ready pods

oc describe svc my-svc -n payments-prod
# Check the Selector: field; compare with:
oc get pod <pod-name> -n payments-prod --show-labels
# Do the key:value pairs match?
```

### Cause B — App listening on wrong interface or port

The process inside the container is listening on `127.0.0.1:8080` (loopback only) or on a port different from what the Service's `targetPort` specifies. The readiness probe might check a management endpoint (e.g. `/health` on a distinct port) that responds, while the main application port is dead, wrong, or bound to localhost.

**Diagnose:**
```bash
# 1. Check what the Service targets:
oc get svc my-svc -n payments-prod -o jsonpath='{.spec.ports}'
# Then check the Route's targetPort:
oc get route my-route -n payments-prod -o jsonpath='{.spec.to.name} {.spec.port.targetPort}'

# 2. Shell into the pod and test locally:
oc exec <pod> -n payments-prod -- curl -v http://localhost:<port>/
#    If this fails but the app is running, check the listening interface:
oc exec <pod> -n payments-prod -- netstat -tlnp
#    Look for 0.0.0.0:<port> vs 127.0.0.1:<port>

# 3. Check if the readiness probe actually tests the app port:
oc get pod <pod> -n payments-prod -o yaml | grep -A20 readinessProbe
```

A common pattern: the app binary starts, the readiness probe (e.g. `exec ls /tmp/healthy`) passes because the process is running, but the HTTP listener hasn't bound yet or bound only to localhost.

### Cause C — NetworkPolicy blocks ingress from the router

If a NetworkPolicy in the `payments-prod` namespace selects the pod's label but does **not** allow ingress from the `openshift-ingress` namespace (where the HAProxy router pods run), traffic reaches the node but is dropped by OVN-Kubernetes before it reaches the pod. The router sees the connection hang or fail and returns 503.

**Diagnose:**
```bash
# Check if any NetworkPolicy exists in the namespace:
oc get networkpolicy -n payments-prod

# If a NetworkPolicy selects the pod, verify it allows ingress from the router:
oc describe networkpolicy <name> -n payments-prod
# Look for:
#   Ingress:
#     From:
#       NamespaceSelector:
#         ...

# The router runs in openshift-ingress; you need either:
# - A rule allowing that namespace, or
# - No NetworkPolicy selecting the pod (because OCP's default is allow-all
#   until a policy selects a pod)

# To confirm this is the blocker: temporarily label the pod with a label that
# no NetworkPolicy selects, or add the openshift-ingress namespace to the
# policy's ingress rule.
```

> **Note:** A fourth variant: the Route's TLS mode mismatches the app (e.g. `edge` termination but the app also terminates TLS, causing double-encryption). Check with `oc describe route` — if the app expects TLS and the Route is `edge`, the router's HTTP-only request to the pod will be rejected. Use `passthrough` or `re-encrypt` instead. (inferred from [[openshift-route]])

### Debug flow — step by step

```
1. Route exists and DNS resolves?
   → curl -v https://app-payments-prod.apps.cluster.example.com
   → 503 ⇒ proceed

2. Service has endpoints?
   → oc get endpoints -n payments-prod
   → If empty: selector mismatch (Cause A)
   → If populated: proceed

3. Can the router reach the pod?
   → oc exec -n openshift-ingress <router-pod> -- curl -v http://<pod-ip>:<port>
   → If fails (timeout/refused): check NetworkPolicy (Cause C)
   → If succeeds: proceed

4. Does the app listen on the right interface?
   → oc exec <pod> -n payments-prod -- netstat -tlnp
   → If 127.0.0.1:<targetPort⟩: wrong interface (Cause B)
   → If 0.0.0.0:<targetPort⟩: check readiness probe depth

5. Does the readiness probe check the actual service port?
   → oc get pod <pod> -n payments-prod -o yaml | grep -A10 readinessProbe
   → If the probe is a shallow exec (e.g., `ls /tmp/ready`) or hits a
     different port, it may pass while the app port is dead.
```

## See also
- [[security-context-constraints]] — SCC model, default SCCs, how a pod gets an SCC
- [[openshift-route]] — Route TLS modes, how HAProxy selects backends
- [[kubernetes-service]] — endpoints, selector model, readiness gating
- [[kubernetes-pod]] — probes, OOM, CrashLoopBackOff mechanics
- [[openshift-implementation-review]] — symptom → cause reverse index

## References

### RH ground-truth (kb: / guide: / ref:)
- `kb:managing-security-context-constraints` — "Managing security context constraints" (OCP 4.22): default SCCs, restricted-v2, MustRunAsRange strategy, SA-to-SCC binding
- `kb:create-images` — "Creating images" (OCP 4.22): UID-agnostic pattern, group-writable dirs, /etc/passwd injection
- `kb:nw-configuring-routes` — "Configuring routes" (OCP 4.22): Route spec, target port, TLS termination modes
- `kb:ingress-operator` — "Ingress Operator" (OCP 4.22): custom 503 error pages, router pod details
- `kb:service` — "Service" (K8s): endpoint set, selector matching, readiness gating
- `kb:pod-v1` — "Pod v1" (K8s API): runAsNonRoot validation logic, securityContext
- `kb:network-policies` — "Network Policies" (K8s): default-deny model, ingress/egress rules
- `ref:post-installation-configuration-4-22-security-basics.md` — SCC vs PSA history: OpenShift added SCC when K8s had none; PSA added in OCP 4.11 alongside SCC
- `ref:post-installation-configuration-4-22-security-sec-context-constraints.md` — restricted-v2 SCC details, MustRunAsRange, capability drop
- `ref:authentication-4-22-understanding-and-managing-pod-security-admission.md` — PSA modes (enforce/audit/warn), profiles (privileged/baseline/restricted)
- `ref:concepts-pod-security-standards.md` — K8s Pod Security Standards definition

### Wiki / upstream (web:)
- [[security-context-constraints]] — SCC entity page with default SCC table and gotchas
- [[openshift-route]] — Route TLS modes, the Service endpoint dependency
- [[kubernetes-service]] — selector → endpoints model, readiness gating → 503
- [[kubernetes-pod]] — probe types, runAsNonRoot validation on the kubelet
- [[openshift-implementation-review]] — symptom → cause table (CrashLoopBackOff on OCP = SCC, 503 from router = no ready endpoints)
- `web:` OCP 4.22 Managing SCCs — `https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/managing-security-context-constraints`
- `web:` OCP 4.22 Understanding and managing PSA — `https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-and-managing-pod-security-admission`
- `web:` K8s Pod Security Admission — `https://kubernetes.io/docs/concepts/security/pod-security-admission/`

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[authentication-4-22-managing-security-context-constraints|Managing security context constraints]]
- [[openshift-images-4-22-create-images|Creating images]]
- [[networking-4-22-nw-configuring-routes|Configuring routes]]
- [[networking-4-22-ingress-operator|Ingress Operator in {product-title}]]
- [[concepts-service|Service]]
- [[microshift-rest-api-4-22-pod-v1|Pod v1]]
- [[concepts-network-policies|Network Policies]]
<!-- crosslink:end -->
