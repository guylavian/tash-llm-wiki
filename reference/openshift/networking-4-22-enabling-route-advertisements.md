---
title: "Enabling route advertisements"
type: reference
domain: openshift
slug: networking-4-22-enabling-route-advertisements
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/enabling-route-advertisements
version: 4.22
family: networking
documentKind: "Documentation"
---

# Enabling route advertisements

[id="enabling-route-advertisements"]
= Enabling route advertisements

[role="_abstract"]
To improve network reachability and failover visibility for your cluster, you can enable route advertisements for pod and egress IP addresses. This configuration requires the OVN-Kubernetes network plugin and allows your cluster to share routes with an external provider network.

As a cluster administrator, you can configure additional route advertisements for your cluster. You must use the OVN-Kubernetes network plugin.

// Module included in the following assemblies:
//
// * networking/route_advertisements/enabling-route-advertisements.adoc

[id="nw-route-advertisements-enable_{context}"]
= Enabling route advertisements

[role="_abstract"]
To improve network reachability and failover visibility, you can enable additional routing support for your cluster. You can enable route advertisements to manage network traffic within your environment.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in to the cluster as a user with the `cluster-admin` role.
* The cluster is installed on compatible infrastructure.

.Procedure

* To enable a routing provider and additional route advertisements, enter the following command:
+
[source,terminal]
----
$ oc patch Network.operator.openshift.io cluster --type=merge \
  -p='{
    "spec": {
      "additionalRoutingCapabilities": {
        "providers": ["FRR"]
        },
        "defaultNetwork": {
          "ovnKubernetesConfig": {
            "routeAdvertisements": "Enabled"
    }}}}'
----
