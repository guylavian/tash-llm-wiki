---
title: "Manually scaling a compute machine set"
type: reference
domain: openshift
slug: machine-management-4-22-manually-scaling-machineset
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/manually-scaling-machineset
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Manually scaling a compute machine set

[id="manually-scaling-machineset"]
= Manually scaling a compute machine set

[role="_abstract"]
You can manually add or remove an instance of a machine in a compute machine set. Manually scaling a compute machine set gives you control over the resource utilization of that machine set.

[NOTE]
====
If you need to modify aspects of a compute machine set outside of scaling, see "Modifying a compute machine set".
====

== Prerequisites

* If you enabled the cluster-wide proxy and scale up compute machines not included in `networking.machineNetwork[].cidr` from the installation configuration, you must add the compute machines to the Proxy object's `noProxy` field to prevent connection issues. See "Add the compute machines to the Proxy object's `noProxy` field" for more information.

// Module included in the following assemblies:
//
// * machine_management/manually-scaling-machineset.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * windows_containers/scheduling-windows-workloads.adoc

[id="machineset-manually-scaling_{context}"]
= Scaling a compute machine set manually

[role="_abstract"]
To add or remove an instance of a machine in a compute machine set, you can manually scale the compute machine set.

This guidance is relevant to fully automated, installer-provisioned infrastructure installations. Customized, user-provisioned infrastructure installations do not have compute machine sets.

.Prerequisites

* Install an OpenShift Container Platform cluster and the `oc` command line.
* Log in to  `oc` as a user with `cluster-admin` permission.

.Procedure

. View the compute machine sets that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
The compute machine sets are listed in the form of `<clusterid>-worker-<aws-region-az>`.

. View the compute machines that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api
----

. Set the annotation on the compute machine that you want to delete by running the following command:
+
[source,terminal]
----
$ oc annotate machines.machine.openshift.io/<machine_name> -n openshift-machine-api machine.openshift.io/delete-machine="true"
----

. Scale the compute machine set by running one of the following commands:
+
[source,terminal]
----
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
Or:
+
[source,terminal]
----
$ oc edit machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
[TIP]
====
You can alternatively apply the following YAML to scale the compute machine set:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 2
----
====
+
You can scale the compute machine set up or down. It takes several minutes for the new machines to be available.
+
[IMPORTANT]
====
By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.
====

.Verification

* Verify the deletion of the intended machine by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io
----

// Module included in the following assemblies:
//
// * machine_management/manually-scaling-machineset.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="machineset-delete-policy_{context}"]
= The compute machine set deletion policy

[role="_abstract"]
Compute machine sets can be configured to use the `Random`, `Newest`, and `Oldest` deletion options. The default is `Random`, meaning that random machines are chosen and deleted when scaling compute machine sets down.

The deletion policy can be set according to the use case by modifying the particular compute machine set as in the following example:

[source,yaml]
----
spec:
  deletePolicy: <delete_policy>
  replicas: <desired_replica_count>
----

Specific machines can also be prioritized for deletion by adding the annotation `machine.openshift.io/delete-machine=true` to the machine of interest, regardless of the deletion policy.

[IMPORTANT]
====
By default, the OpenShift Container Platform router pods are deployed on workers. Because the router is required to access some cluster resources, including the web console, do not scale the worker compute machine set to `0` unless you first relocate the router pods.
====

[NOTE]
====
Custom compute machine sets can be used for use cases requiring that services run on specific nodes and that those services are ignored by the controller when the worker compute machine sets are scaling down. This prevents service disruption.
====

[role="_additional-resources"]
[id="additional-resources_manually-scaling-machineset"]
== Additional resources
* Modifying a compute machine set
* Add the compute machines to the Proxy object's `noProxy` field
* Lifecycle hooks for the machine deletion phase
