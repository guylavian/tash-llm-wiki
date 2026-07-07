---
title: "Managing control plane machines with control plane machine sets"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-managing-machines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-managing-machines
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Managing control plane machines with control plane machine sets

[id="cpmso-managing-machines"]
= Managing control plane machines with control plane machine sets

[role="_abstract"]
Control plane machine sets automate several essential aspects of control plane management to reduce operational overhead and ensure consistency.

//Vertical resizing of the control plane
//include::modules/cpmso-feat-vertical-resize.adoc[leveloffset=+1]

//Updating the control plane configuration
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-managing-machines.adoc

[id="cpmso-feat-config-update_{context}"]
= Updating the control plane configuration

[role="_abstract"]
Update the control plane machine set specification to modify control plane machine configuration and trigger automatic or manual replacements.

The Control Plane Machine Set Operator monitors the control plane machines and compares their configuration with the specification in the control plane machine set CR. When there is a discrepancy between the specification in the CR and the configuration of a control plane machine, the Operator marks that control plane machine for replacement.

[NOTE]
====
For more information about the parameters in the CR, see "Control plane machine set configuration".
====

.Prerequisites

* Your cluster has an activated and functioning Control Plane Machine Set Operator.

.Procedure

. Edit your control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

. Change the values of any fields that you want to update in your cluster configuration.

. Save your changes.

.Next steps

* For clusters that use the default `RollingUpdate` update strategy, the control plane machine set propagates changes to your control plane configuration automatically.

* For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

//Automatic updates to the control plane configuration
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-managing-machines.adoc
// * rosa/architecture/control-plane.adoc
// * osd/architecture/control-plane.adoc

[id="cpmso-feat-auto-update_{context}"]
= Automatic updates to the control plane configuration

[role="_abstract"]
The `RollingUpdate` update strategy automatically propagates changes to your control plane configuration to minimize manual intervention.

//Not for ROSA/OSD:
This update strategy is the default configuration for the control plane machine set.

For clusters that use the `RollingUpdate` update strategy, the Operator creates a replacement control plane machine with the configuration that is specified in the CR.
When the replacement control plane machine is ready, the Operator deletes the control plane machine that is marked for replacement.
The replacement machine then joins the control plane.

If multiple control plane machines are marked for replacement, the Operator protects etcd health during replacement by repeating this replacement process one machine at a time until it has replaced each machine.

//For ROSA/OSD:

On OpenShift Container Platform clusters, control plane machine sets automatically propagate changes to your control plane configuration.
When a control plane machine needs to be replaced, the Control Plane Machine Set Operator creates a replacement machine based on the configuration specified by the `ControlPlaneMachineSet` custom resource (CR). When the new control plane machine is ready, the Operator safely drains and terminates the old control plane machine in a way that mitigates any potential negative effects on cluster API or workload availability.

[IMPORTANT]
====
You cannot request that control plane machine replacements happen only during maintenance windows. The Control Plane Machine Set Operator acts to ensure cluster stability. Waiting for a maintenance window could result in cluster stability being compromised.
====

A control plane machine can be marked for replacement at any time, typically because the machine has fallen out of spec or entered an unhealthy state. Such replacements are a normal part of a cluster's lifecycle and not a cause for concern. SRE will be alerted to the issue automatically if any part of a control plane node replacement fails.

[NOTE]
====
Depending on when the OpenShift Container Platform cluster was originally created, the introduction of control plane machine sets might leave one or two control plane nodes with labels or machine names that are inconsistent with the other control plane nodes. For example `clustername-master-0`, `clustername-master-1`,and `clustername-master-2-abcxyz`. Such naming inconsistencies do not affect the workings of the cluster and are not a cause for concern.
====

//Manual updates to the control plane configuration
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-managing-machines.adoc

[id="cpmso-feat-ondelete-update_{context}"]
= Manual updates to the control plane configuration

[role="_abstract"]
Use the `OnDelete` update strategy to test configuration changes on individual control plane machines before applying them cluster-wide. Manually replacing machines allows you to test changes to your configuration on a single machine before applying the changes more broadly.

For clusters that are configured to use the `OnDelete` update strategy, the Operator creates a replacement control plane machine when you delete an existing machine. When the replacement control plane machine is ready, the etcd Operator allows the existing machine to be deleted. The replacement machine then joins the control plane.

If multiple control plane machines are deleted, the Operator creates all of the required replacement machines simultaneously. The Operator maintains etcd health by preventing more than one machine being removed from the control plane at once.

//Replacing a control plane machine
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-managing-machines.adoc

[id="cpmso-feat-replace_{context}"]
= Replacing a control plane machine

[role="_abstract"]
Replace a control plane machine to apply updated configurations or recover from hardware issues while maintaining cluster stability. The control plane machine set replaces the deleted machine with one using the specification in the control plane machine set custom resource (CR).

.Prerequisites

* If your cluster runs on {rh-openstack-first} and you need to evacuate a compute server, such as for an upgrade, you must disable the {rh-openstack} compute node that the machine runs on by running the following command:
+
[source,terminal]
----
$ openstack compute service set <target_node_host_name> nova-compute --disable
----
+
For more information, see Preparing to migrate in the {rh-openstack} documentation.

.Procedure

. List the control plane machines in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machines \
  -l machine.openshift.io/cluster-api-machine-role==master \
  -n openshift-machine-api
----

. Delete a control plane machine by running the following command:
+
[source,terminal]
----
$ oc delete machine \
  -n openshift-machine-api \
  <control_plane_machine_name>
----
+
where `<control_plane_machine_name>` specifies the name of the control plane machine to delete.
+
[NOTE]
====
If you delete multiple control plane machines, the control plane machine set replaces them according to the configured update strategy:

* For clusters that use the default `RollingUpdate` update strategy, the Operator replaces one machine at a time until each machine is replaced.

* For clusters that are configured to use the `OnDelete` update strategy, the Operator creates all of the required replacement machines simultaneously.

Both strategies maintain etcd health during control plane machine replacement.
====

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* Control plane machine set configuration

* Provider-specific configuration options
