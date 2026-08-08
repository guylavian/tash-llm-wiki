---
title: "Network Observability Operator"
type: reference
domain: openshift
slug: networking-4-22-network-observability-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/network-observability-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Network Observability Operator

[id="network-observability-operator-default"]
= Network Observability Operator

[role="_abstract"]
Network Observability Operator provides network flow monitoring, visualization, and analysis capabilities for OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * networking/network_observability_operator/network-observability-operator.adoc

[id="network-observability-operator-stub_{context}"]
= Network Observability Operator features

[role="_abstract"]
With the Network Observability Operator, you can monitor ingress, egress, and internal network traffic flows between pods, services, and nodes in your cluster.

Use this network flow data to troubleshoot connectivity issues, analyze traffic patterns, detect security threats, and optimize overall network performance.

You can perform the following tasks with this Operator:

* Collect network flow data by using eBPF technology.
* Visualize traffic flows inside the OpenShift Container Platform web console.
* Filter and analyze flows by namespace, pod, service, or port attributes.
* Export flow data to external analysis tools for long-term storage or processing.

[NOTE]
====
For complete documentation about installing, configuring, and using the Network Observability Operator, see Network Observability overview in the Observability section.
====
