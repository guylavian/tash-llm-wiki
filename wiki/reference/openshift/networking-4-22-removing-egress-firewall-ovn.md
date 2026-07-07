---
title: "Removing an egress firewall from a project"
type: reference
domain: openshift
slug: networking-4-22-removing-egress-firewall-ovn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/removing-egress-firewall-ovn
version: 4.22
family: networking
documentKind: "Documentation"
---

# Removing an egress firewall from a project

[id="removing-egress-firewall-ovn"]
= Removing an egress firewall from a project

[role="_abstract"]
As a cluster administrator, you can remove an egress firewall from a project to remove all restrictions on network traffic from the project that leaves the OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/removing-egress-firewall-ovn.adoc

[id="nw-egress-firewall-delete_{context}"]
= Removing an EgressFirewall CR

[role="_abstract"]
As a cluster administrator, you can remove an egress firewall from a project.

.Prerequisites

* A cluster using the OVN-Kubernetes network plugin.
* Install the OpenShift CLI (`oc`).
* You must log in to the cluster as a cluster administrator.

.Procedure

. Find the name of the `EgressFirewall` CR for the project. Replace `<project>` with the name of the project.
+
[source,terminal,subs="attributes+"]
----
$ oc get egressfirewall -n <project>
----

. Delete the `EgressFirewall` CR by entering the following command. Replace `<project>` with the name of the project and `<name>` with the name of the object.
+
[source,terminal,subs="attributes+"]
----
$ oc delete -n <project> egressfirewall <name>
----
