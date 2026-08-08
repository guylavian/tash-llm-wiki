---
title: "Enabling BGP routing"
type: reference
domain: openshift
slug: networking-4-22-enabling-bgp-routing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/enabling-bgp-routing
version: 4.22
family: networking
documentKind: "Documentation"
---

# Enabling BGP routing

[id="enabling-bgp-routing"]
= Enabling BGP routing

[role="_abstract"]
To support dynamic route advertisement and integration with external network infrastructure, you can enable Border Gateway Protocol (BGP) routing for your cluster as a cluster administrator.

As a cluster administrator, you can enable OVN-Kubernetes BGP routing support for your cluster.

// Module included in the following assemblies:
//
// * networking/bgp_routing/enabling-bgp-routing.adoc

[id="nw-bgp-routing-config_{context}"]
= Enabling Border Gateway Protocol (BGP) routing

[role="_abstract"]
To allow external network integration and route advertisement on supported infrastructure, you can enable Border Gateway Protocol (BGP) routing for your cluster by configuring the cluster network to use an FRR-based dynamic routing provider.

As a cluster administrator, you can enable BGP routing support for your cluster on bare-metal infrastructure.

If you are using BGP routing in conjunction with the MetalLB Operator, the necessary BGP routing support is enabled automatically. You do not need to manually enable BGP routing support.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in to the cluster as a user with the `cluster-admin` role.
* The cluster is installed on compatible infrastructure.

.Procedure

* To enable a dynamic routing provider, enter the following command:
+
[source,terminal]
----
$ oc patch Network.operator.openshift.io/cluster --type=merge -p '{
  "spec": {
    "additionalRoutingCapabilities": {
      "providers": ["FRR"]
    }
  }
}'
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Improve east-west performance by routing pods on the underlay with BGP
