---
title: How OpenShift Networking Works — Services, Routes, DNS, and NetworkPolicy
type: question
question_tier: conceptual
domain: openshift
slug: openshift-networking-services-routes-dns-networkpolicy
summary: "OpenShift networking has four interdependent layers: Services provide stable virtual IPs over ephemeral pods; Routes (or Ingress) expose those Services externally through the HAProxy router; CoreDNS (managed by the DNS Operator) resolves internal cluster names; and NetworkPolicy enforces opt-in pod-to-pod micro-segmentation over the OVN-Kubernetes overlay."
sources:
  - note:_sources/openshift/kubernetes-networking.md
  - note:_sources/openshift/openshift-platform.md
  - kb:service
  - kb:service-v1
  - kb:ingress
  - kb:about-ovn-kubernetes
  - kb:dns-operator
  - kb:dns-pod-service
  - kb:network-policies
  - kb:about-network-policy
  - kb:securing-routes
  - kb:creating-basic-routes
  - kb:nw-configuring-routes
  - kb:ingress-operator
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 0
tags: [authz]
status: draft
updated: 2026-07-07
---

# How OpenShift Networking Works — Services, Routes, DNS, and NetworkPolicy

**OpenShift networking is a four-layer stack: [[kubernetes-service]] gives workloads a stable identity, [[openshift-route]] or [[kubernetes-ingress]] opens that Service to external traffic, [[cluster-dns]] (CoreDNS via the DNS Operator) resolves names for pod-to-pod communication, and [[network-policy]] enforces allow-list firewalling — all running on the [[ovn-kubernetes]] overlay network (Geneve-encapsulated OVN over OVS).**

## Layer 1 — Services: stable endpoints over ephemeral pods

Pods come and go; their IPs change on every reschedule. A **Service** gives callers a stable ClusterIP + DNS name (`<service>.<namespace>.svc.cluster.local`) and load-balances only to pods passing readiness probes. Without ready endpoints, anything in front of the Service (including a Route) returns 503. Four types:

- **ClusterIP** (default) — internal virtual IP, reachable only inside the cluster.
- **NodePort** — also reachable on every node's IP at a static port.
- **LoadBalancer** — provisions an external cloud load balancer.
- **ExternalName** — a CNAME alias to an external DNS name (no proxying).

A Route or Ingress **always** targets a Service, never pods directly. See [[kubernetes-service]] for details.

## Layer 2 — Routes and Ingress: external exposure

- **[[openshift-route]]** is OpenShift's native external-HTTP(S) object. Served by the built-in HAProxy Ingress Controller (managed by the Ingress Operator). Supports three [[route-tls-termination]] modes:
  - **edge** — TLS terminates at the router; router→pod runs plaintext inside the cluster.
  - **passthrough** — encrypted bytes go straight to the pod, which terminates TLS itself (required for mTLS or non-HTTP TLS).
  - **re-encrypt** — TLS terminates at the router, which opens a **new** TLS connection to the pod (requires a destination CA cert).
- **[[kubernetes-ingress]]** is the upstream-Kubernetes equivalent. On OCP, creating an Ingress auto-generates a managed Route, so the two objects coexist. The Ingress API is frozen upstream; Route continues to receive new capabilities (inferred, cross-reference from [[openshift-route]]).

Common gotcha: a Route to a not-ready pod (probes failing, selector typo'd) returns **503** even though the Route and Service exist — because the Service's endpoint set is empty.

## Layer 3 — Cluster DNS: name resolution

The **DNS Operator** (`dns.operator.openshift.io`) deploys CoreDNS as a daemon set, creates a Service in front of it, and configures the kubelet to point every pod's `/etc/resolv.conf` at that Service IP. This enables:

- **Service DNS:** every Service gets `<name>.<namespace>.svc.cluster.local`. Consumers reach it by short name within the same namespace or by FQDN.
- **Pod DNS:** headless Services expose per-pod A/AAAA records (used by StatefulSets).
- **Search domains** and `ndots:5` default: the kubelet injects a search list (namespace, `svc.cluster.local`, cluster domain, node-inherited). A bare short name is tried against each search domain before falling back to absolute resolution — the mechanism behind "works with FQDN, fails with short name" bugs.

Search domains are capped at 32 entries / 2048 total characters; exceeding it truncates the list, which can silently break name resolution. See [[cluster-dns]].

## Layer 4 — NetworkPolicy: the allow-list firewall

**[[network-policy]]** is opt-in micro-segmentation enforced by OVN-Kubernetes at the OVS/OpenFlow level:

- **Default: all pods in a project are reachable from any other pod.** A pod is "non-isolated" until a NetworkPolicy selects it.
- **Once selected**, the pod accepts **only** the connections explicitly allowed by the union of all policies selecting it for that direction (ingress/egress independently). Policies are **additive** — combining two policies on the same pods grants the union of both, not the intersection.
- Traffic to/from the node itself is always allowed regardless of IP-block rules.
- A policy with a selector typo or targeting a non-supporting CNI **silently does nothing** — confirm enforcement by testing, not just `oc get networkpolicy`.

As of OCP 4.22, OpenShift ships default NetworkPolicy objects in some control-plane namespaces — do not modify them. Later releases may cover more namespaces, so an upgrade can introduce implicit deny-by-default in a namespace that previously had none (inferred from OCP 4.22 docs, which explicitly note coverage will grow). See [[network-policy]] and `oc get networkpolicies --all-namespaces`.

## The underlying plumbing: OVN-Kubernetes

[[ovn-kubernetes]] is the default OCP CNI plugin. It builds an overlay network using **OVN (Open Virtual Network)** over **OVS (Open vSwitch)** with **Geneve** encapsulation. It handles:

- Distributed virtual routing and switching for pod-to-pod and pod-to-Service traffic.
- Service virtual-IP implementation (via OVN load-balancer flows, not iptables).
- NetworkPolicy enforcement and audit logging.
- Egress IPs, IPsec, IPv6/dual-stack, multicast, and hardware offloading.

It replaced the older OpenShift SDN plugin as the default network provider.

## Kubernetes-upstream vs OpenShift-specific

| Concept | Upstream Kubernetes | OpenShift |
|---|---|---|
| External HTTP(S) | Ingress (frozen API; requires 3rd-party controller) | Route (native, HAProxy router, 3 TLS modes) |
| Internal exposure | Service (ClusterIP/NodePort/LoadBalancer) | Same — Service is shared |
| CNI/overlay | Pluggable (any CNI) | OVN-Kubernetes (default, managed) |
| DNS | CoreDNS (generic, manually configured) | DNS Operator manages CoreDNS as CR |
| NetworkPolicy | Requires supporting CNI, no defaults | OCP ships default policies in control-plane namespaces (4.22+) |

## See also
- [[openshift-networking]] — the topic spine
- [[openshift-implementation-review]] — symptom → cause MOC
- [[openshift-overview]] — architecture spine

## References

### RH ground-truth (kb: / ref:)
- [[concepts-service|Service]]
- [[concepts-ingress|Ingress]]
- [[networking-4-22-dns-operator|DNS Operator in {product-title}]]
- [[concepts-dns-pod-service|DNS for Services and Pods]]
- [[concepts-network-policies|Network Policies]]
- [[networking-4-22-about-network-policy|Creating a network policy]]
- [[networking-4-22-about-ovn-kubernetes|About the OVN-Kubernetes network plugin]]
- [[networking-4-22-securing-routes|Securing routes]]
- [[networking-4-22-creating-basic-routes|Creating basic routes]]
- [[networking-4-22-ingress-operator|Ingress Operator in {product-title}]]
- [[networking-4-22-nw-configuring-routes|Configuring routes]]

### Wiki ([[slug]])
- [[openshift-networking]] · [[kubernetes-service]] · [[openshift-route]] · [[kubernetes-ingress]] · [[route-tls-termination]] · [[cluster-dns]] · [[network-policy]] · [[ovn-kubernetes]]
- [[openshift-overview]] · [[openshift-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[concepts-service|Service]]
- [[microshift-rest-api-4-22-service-v1|Service v1]]
- [[concepts-ingress|Ingress]]
- [[networking-4-22-about-ovn-kubernetes|About the OVN-Kubernetes network plugin]]
- [[networking-4-22-dns-operator|DNS Operator in {product-title}]]
- [[concepts-dns-pod-service|DNS for Services and Pods]]
- [[concepts-network-policies|Network Policies]]
- [[networking-4-22-about-network-policy|Creating a network policy]]
- [[networking-4-22-securing-routes|Securing routes]]
- [[networking-4-22-creating-basic-routes|Creating basic routes]]
- [[networking-4-22-nw-configuring-routes|Configuring routes]]
- [[networking-4-22-ingress-operator|Ingress Operator in {product-title}]]
<!-- crosslink:end -->
