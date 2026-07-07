---
title: "Disabling route advertisements"
type: reference
domain: openshift
slug: networking-4-22-disabling-route-advertisements
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/disabling-route-advertisements
version: 4.22
family: networking
documentKind: "Documentation"
---

# Disabling route advertisements

[id="disabling-route-advertisements"]
= Disabling route advertisements

[role="_abstract"]
To stop the broadcast of cluster network routes and egress IP addresses to your provider network, you can disable route advertisements. Disabling this feature removes the automatically generated routing configurations while maintaining your existing network infrastructure.

// Module included in the following assemblies:
//
// * networking/route_advertisements/disabling-route-advertisements.adoc

[id="nw-route-advertisements-disable_{context}"]
= Disabling route advertisements

[role="_abstract"]
To prevent your cluster from advertising additional routes to the network, you must disable the route advertisements feature in the network operator configuration. You can disable route advertisements to manage network traffic and maintain security within your environment.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in to the cluster as a user with the `cluster-admin` role.
* The cluster is installed on compatible infrastructure.

.Procedure

* To disable additional routing support, enter the following command:
+
[source,terminal]
----
$ oc patch network.operator cluster -p '{
  "spec": {
    "defaultNetwork": {
      "ovnKubernetesConfig": {
        "routeAdvertisements": "Disabled"
      }
    }
  }
}'
----
