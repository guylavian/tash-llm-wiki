---
title: Kubernetes NetworkPolicy
type: entity
domain: openshift
slug: kubernetes-networkpolicy
summary: "A namespaced object that selects pods and declares allowed ingress/egress connections by pod, namespace, or IP block; policies are additive-only (default allow-all until a policy selects a pod), require a CNI plugin that implements NetworkPolicy, and OpenShift's OVN-Kubernetes plugin adds default deny-all policies plus a router-allow label in some system namespaces."
sources:
  - ref:reference/openshift/concepts-network-policies.md
  - ref:reference/openshift/networking-4-22-about-network-policy.md
  - kb:network-policies
  - kb:about-network-policy
provenance_extracted: 8
provenance_inferred: 1
provenance_ambiguous: 0
tags: [cluster-networking, concept]
status: draft
updated: 2026-07-05
---

# Kubernetes NetworkPolicy

**A NetworkPolicy selects a set of pods (by label) and declares the ingress/egress connections allowed to/from them; without any policy selecting a pod, all traffic to and from it is allowed.**

## The default and how isolation turns on
- By default a pod is **non-isolated** for both ingress and egress — all traffic is allowed. (extracted: concepts-network-policies.md — "By default, if no policies exist in a namespace, then all ingress and egress traffic is allowed to and from pods in that namespace.")
- A pod becomes isolated for a direction (ingress or egress) as soon as **any** NetworkPolicy selects it and lists that direction in `policyTypes`; only the allowed connections listed by such policies are then permitted in that direction. (extracted: concepts-network-policies.md, "The two sorts of pod isolation")
- **Policies are additive, never conflicting** — if multiple policies apply to a pod for a direction, the allowed set is the union of what each policy permits; evaluation order doesn't matter. (extracted: concepts-network-policies.md — "Network policies do not conflict; they are additive.")
- A `NetworkPolicy` object with no controller implementing it **has no effect** — it requires a CNI plugin (OVN-Kubernetes on OpenShift) that supports the resource. (extracted: concepts-network-policies.md, "Prerequisites")

## The three selector kinds
Each `ingress`/`egress` rule's `from`/`to` can match:
- **podSelector** — pods in the same namespace as the policy.
- **namespaceSelector** — all pods in namespaces matching the label selector.
- **ipBlock** — a CIDR range, for cluster-external IPs (pod IPs are ephemeral, so this isn't meant for pod-to-pod).
(extracted: concepts-network-policies.md, "Behavior of `to` and `from` selectors")

Combining `namespaceSelector` **and** `podSelector` in one `from`/`to` entry (single list item) narrows to pods with that label *within* those namespaces; listing them as two separate entries is an OR (either match qualifies) — a common authoring mistake. (extracted: concepts-network-policies.md, YAML example)

## Default-deny and default-allow recipes
- **Default-deny-all-ingress**: a policy with an empty `podSelector: {}` (selects every pod) and `policyTypes: [Ingress]` but no `ingress` rules — every pod in the namespace becomes ingress-isolated with nothing allowed in.
- **Default-deny-all** (both directions): same, with `policyTypes: [Ingress, Egress]` and no rules in either. A default-deny-all-egress policy also blocks DNS — pair it with an explicit egress-to-DNS allow rule.
(extracted: concepts-network-policies.md, "Default policies")

## Port targeting
`endPort` lets a rule target a port range (`port`..`endPort`) instead of a single port — stable since Kubernetes v1.25, and requires CNI plugin support (silently collapses to the single `port` if unsupported). (extracted: concepts-network-policies.md, "Targeting a range of ports")

## OpenShift specifics (OVN-Kubernetes)
- Since OCP 4.22, OpenShift ships default `NetworkPolicy` objects in some of its own namespaces (`openshift-dns`, `openshift-dns-operator`, `openshift-ingress`, `openshift-ingress-operator`) — a deny-all baseline plus targeted allow rules for the traffic those components need (API server, DNS ports, route endpoints, metrics). Do not modify these. (extracted: networking-4-22-about-network-policy.md, "About network policy")
- To allow the OpenShift router (HAProxy, running in `openshift-ingress`) to reach an app pod when a NetworkPolicy already selects it, add an ingress rule matching the `policy-group.network.openshift.io/ingress: ""` namespace label — this is an OVN-Kubernetes-specific convenience label, not a stock Kubernetes selector. (extracted: networking-4-22-about-network-policy.md, "Policy additivity")
- (inferred) This is the mechanism behind the "pod is Ready 1/1 but the Route returns 503" failure mode when a NetworkPolicy exists: if it selects the pod but its `ingress.from` doesn't include the ingress-router namespace, the router's connection is dropped before reaching the pod — see [[ocp-scc-root-crashloopbackoff-route-503]] Cause C.

## Contradictions / caveats
- NetworkPolicy behavior for `hostNetwork` pods is explicitly **undefined** by the upstream spec; most CNI implementations just can't distinguish hostNetwork traffic and treat it like node traffic.
- The upstream doc (`kb:network-policies`) describes the generic Kubernetes API; the OpenShift-specific default-deny namespaces and the `policy-group.network.openshift.io/ingress` label (`kb:about-network-policy`) are OVN-Kubernetes/OpenShift additions, not portable to every CNI plugin.

## See also
- [[kubernetes-service]] — the endpoint set a NetworkPolicy's `podSelector` ultimately gates traffic to
- [[kubernetes-pod]] — the unit NetworkPolicy selects
- [[openshift-route]] — router traffic that a NetworkPolicy can silently block (503)
- [[ocp-scc-root-crashloopbackoff-route-503]] — worked debug flow including the NetworkPolicy 503 cause

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[concepts-network-policies|Network Policies]]
- [[networking-4-22-about-network-policy|Creating a network policy]]
<!-- crosslink:end -->
