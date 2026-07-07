---
title: "About networking"
type: reference
domain: openshift
slug: networking-4-22-about-managed-networking
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/about-managed-networking
version: 4.22
family: networking
documentKind: "Documentation"
---

# About networking

[id="about-managed-networking"]
= About networking

[role="_abstract"]
To optimize network traffic management and security across hybrid clusters, configure {openshift-networking}.

The {openshift-networking} ecosystem of networking capabilities integrates ingress, egress, load balancing, high-performance throughput, security, and inter- and intra-cluster traffic management. The {openshift-networking} ecosystem also provides role-based observability tooling to reduce its natural complexities.

The following list details some of the most commonly used {openshift-networking} features available on your cluster:

* Cluster Network Operator for network plugin management.

* Primary cluster network provided by OVN-Kubernetes, the default Container Network Interface (CNI) plugin.

* Primary cluster network provided by either of the following Container Network Interface (CNI) plugins:
+
** OVN-Kubernetes network plugin, which is the default CNI plugin.
** {OCP-short} SDN network plugin, which was deprecated in {OCP-short} 4.16 and removed in {OCP-short} 4.17.

[IMPORTANT]
====
Before upgrading OpenShift Container Platform clusters that are configured with the OpenShift SDN network plugin to version 4.17, you must migrate to the OVN-Kubernetes network plugin. For more information, see _Migrating from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin_.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* {OCP-short} SDN CNI removal in OCP 4.17
* Migrating from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin
* Migrating from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin
