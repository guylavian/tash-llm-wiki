---
title: "Removing Windows nodes"
type: reference
domain: openshift
slug: windows-containers-4-22-removing-windows-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/removing-windows-nodes
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Removing Windows nodes

[id="removing-windows-nodes"]
= Removing Windows nodes

[role="_abstract"]
You can remove a Windows node by deleting its host Windows machine.

// Module included in the following assemblies:
//
// * machine_management/deleting-machine.adoc
// * windows_containers/removing-windows-nodes.adoc

[id="machine-delete_{context}"]
= Deleting a specific machine

[role="_abstract"]
To remove a machine from your cluster, or restart a machine that is part of a machine set, you can use the {oc-first} to delete a specific machine.

[IMPORTANT]
====
Do not delete a control plane machine unless your cluster uses a control plane machine set. If the machine that you delete belongs to a machine set, a new machine is immediately created to satisfy the specified number of replicas.
====

.Prerequisites

* Install an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.

.Procedure

. View the machines that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machine -n openshift-machine-api
----
+
The command output contains a list of machines in the `<clusterid>-<role>-<cloud_region>` format.

. Identify the machine that you want to delete.

. Delete the machine by running the following command:
+
[source,terminal]
----
$ oc delete machine <machine> -n openshift-machine-api
----
+
Replace `<machine>` with the name of the machine.
+
[IMPORTANT]
====
By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.
====
