---
title: "Disabling BGP routing"
type: reference
domain: openshift
slug: networking-4-22-disabling-bgp-routing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/disabling-bgp-routing
version: 4.22
family: networking
documentKind: "Documentation"
---

# Disabling BGP routing

[id="disabling-bgp-routing"]
= Disabling BGP routing

[role="_abstract"]
To stop external route advertisement and restore standard cluster networking behavior, disable OVN-Kubernetes Border Gateway Protocol (BGP) routing.

As a cluster administrator, you can disable OVN-Kubernetes BGP routing support for your cluster.

// Module included in the following assemblies:
//
// * networking/bgp_routing/disabling-bgp-routing.adoc

[id="nw-bgp-routing-config_{context}"]
= Disabling Border Gateway Protocol (BGP) routing

[role="_abstract"]
Disable Border Gateway Protocol (BGP) routing for your cluster by removing additional routing capabilities from the network configuration.

As a cluster administrator, you can disable BGP routing support for your cluster on bare-metal infrastructure.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in to the cluster as a user with the `cluster-admin` role.
* The cluster is installed on compatible infrastructure.

.Procedure

* To disable dynamic routing, enter the following command:
+
[source,terminal]
----
$ oc patch Network.operator.openshift.io/cluster --type=merge -p '{
  "spec": { "additionalRoutingCapabilities": null }
}'
----
