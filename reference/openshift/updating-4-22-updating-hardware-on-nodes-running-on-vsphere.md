---
title: "Updating hardware on nodes running on vSphere"
type: reference
domain: openshift
slug: updating-4-22-updating-hardware-on-nodes-running-on-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/updating/updating-hardware-on-nodes-running-on-vsphere
version: 4.22
family: updating
documentKind: "Documentation"
---

# Updating hardware on nodes running on vSphere

[id="updating-hardware-on-nodes-running-on-vsphere"]
= Updating hardware on nodes running on vSphere

WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.

[role="_abstract"]
You must ensure that your nodes running in vSphere are running on the hardware version supported by OpenShift Container Platform. Currently, hardware version 15 or later is supported for vSphere virtual machines in a cluster. You can update your virtual hardware immediately or schedule an update in vCenter.

[IMPORTANT]
====
* Version  of OpenShift Container Platform requires VMware virtual hardware version 15 or later.

* Before upgrading OpenShift 4.12 to OpenShift 4.13, you must update vSphere to *v8.0 Update 1 or later*; otherwise, the OpenShift 4.12 cluster is marked *un-upgradeable*.
====

[WARNING]
====
Updating custom API certificates triggers the Machine Config Operator (MCO) to initiate a rolling reboot of the control plane nodes. These nodes must be updated serially. Ensure each node returns to a `Ready` state and the `etcd` static pods are healthy before the next node in the sequence begins its update. Failure to do so might result in a loss of etcd quorum and cluster-wide downtime.
====

// Updating the virtual hardware for control plane nodes on vSphere
// Module included in the following assemblies:
//
// updating/updating_a_cluster/updating-hardware-on-nodes-running-in-vsphere.adoc

[id="update-vsphere-virtual-hardware-on-control-plane-nodes_{context}"]
= Updating the virtual hardware for control plane nodes on vSphere

[role="_abstract"]
You can update the virtual hardware for control plane nodes on vSphere.

To reduce the risk of downtime, it is recommended that control plane nodes be updated serially. This ensures that the Kubernetes API remains available and etcd retains quorum.

.Prerequisites

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

.Procedure

. List the control plane nodes in your cluster by running the following command:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/master
----
+
.Example output
[source,terminal]
----
NAME                    STATUS   ROLES    AGE   VERSION
control-plane-node-0    Ready    master   75m   v1.35.4
control-plane-node-1    Ready    master   75m   v1.35.4
control-plane-node-2    Ready    master   75m   v1.35.4
----
+
Note the names of your control plane nodes.

. Mark the control plane node as unschedulable by running the following command:
+
[source,terminal]
----
$ oc adm cordon <control_plane_node>
----

. Shut down the virtual machine (VM) associated with the control plane node. Do this in the vSphere client by right-clicking the VM and selecting *Power* -> *Shut Down Guest OS*. Do not shut down the VM using *Power Off* because it might not shut down safely.

. Update the VM in the vSphere client. Follow Upgrade the Compatibility of a Virtual Machine Manually (VMware vSphere documentation).

. Power on the VM associated with the control plane node. Do this in the vSphere client by right-clicking the VM and selecting *Power On*.

. Run the following command and wait for the node to report as `Ready`:
+
[source,terminal]
----
$ oc wait --for=condition=Ready node/<control_plane_node>
----

. Mark the control plane node as schedulable again by running the following command:
+
[source,terminal]
----
$ oc adm uncordon <control_plane_node>
----

. Repeat this procedure for each control plane node in your cluster.

// Updating the virtual hardware for compute nodes on vSphere
// Module included in the following assemblies:
//
// updating/updating_a_cluster/updating-hardware-on-nodes-running-in-vsphere.adoc

[id="update-vsphere-virtual-hardware-on-compute-nodes_{context}"]
= Updating the virtual hardware for compute nodes on vSphere

[role="_abstract"]
You can update the virtual hardware for compute nodes on vSphere.

To reduce the risk of downtime, it is recommended that compute nodes be updated serially.

[NOTE]
====
Multiple compute nodes can be updated in parallel given workloads are tolerant of having multiple nodes in a `NotReady` state. It is the responsibility of the administrator to ensure that the required compute nodes are available.
====

.Prerequisites

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

.Procedure

. List the compute nodes in your cluster by running the following command:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/worker
----
+
.Example output
[source,terminal]
----
NAME              STATUS   ROLES    AGE   VERSION
compute-node-0    Ready    worker   30m   v1.35.4
compute-node-1    Ready    worker   30m   v1.35.4
compute-node-2    Ready    worker   30m   v1.35.4
----
+
Note the names of your compute nodes.

. Mark the compute node as unschedulable by running the following command:
+
[source,terminal]
----
$ oc adm cordon <compute_node>
----

. Evacuate the pods from the compute node. There are several ways to do this. For example, you can evacuate all or selected pods on a node by running the following command:
+
[source,terminal]
----
$ oc adm drain <compute_node> [--pod-selector=<pod_selector>]
----
+
See "Evacuating pods on nodes" for other options to evacuate pods from a node.

. Shut down the virtual machine (VM) associated with the compute node. Do this in the vSphere client by right-clicking the VM and selecting *Power* -> *Shut Down Guest OS*. Do not shut down the VM using *Power Off* because it might not shut down safely.

. Update the VM in the vSphere client. Follow Upgrade the Compatibility of a Virtual Machine Manually (VMware vSphere documentation).

. Power on the VM associated with the compute node. Do this in the vSphere client by right-clicking the VM and selecting *Power On*.

. Run the following command and wait for the node to report as `Ready`:
+
[source,terminal]
----
$ oc wait --for=condition=Ready node/<compute_node>
----

. Mark the compute node as schedulable again by running the following command:
+
[source,terminal]
----
$ oc adm uncordon <compute_node>
----

. Repeat this procedure for each compute node in your cluster.

[role="_additional-resources"]
.Additional resources

* Evacuating pods on nodes

// Updating the virtual hardware for template on vSphere
// Module included in the following assemblies:
//
// updating/updating_a_cluster/updating-hardware-on-nodes-running-in-vsphere.adoc

[id="update-vsphere-virtual-hardware-on-template_{context}"]
= Updating the virtual hardware for template on vSphere

[role="_abstract"]
You can update the virtual hardware for templates on vSphere.

.Prerequisites

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

.Procedure

. If the RHCOS template is configured as a vSphere template, follow Convert a Template to a Virtual Machine (VMware vSphere documentation).
+
[NOTE]
====
Once converted from a template, do not power on the virtual machine.
====

. Update the virtual machine (VM) in the {vmw-full} client. Complete the steps outlined in Upgrade the Compatibility of a Virtual Machine Manually ({vmw-full} documentation).
+
[IMPORTANT]
====
If you modified the VM settings, those changes might reset after moving to a newer virtual hardware. Please review that all your configured settings are still in place after your upgrade before proceeding to the next step.
====
. Convert the VM in the {vmw-short} client to a template by right-clicking on the VM and then selecting **Template -> Convert to Template**.
+
[IMPORTANT]
====
The steps for converting a VM to a template might change in future {vmw-short} documentation versions.
====

// Scheduling an update for virtual hardware on vSphere
// Module included in the following assemblies:
//
// updating/updating_a_cluster/updating-hardware-on-nodes-running-in-vsphere.adoc

[id="scheduling-virtual-hardware-update-on-vsphere_{context}"]
= Scheduled updates for virtual hardware on vSphere

[role="_abstract"]
Virtual hardware updates can be scheduled to occur when a virtual machine is powered on or rebooted. You can schedule your virtual hardware updates exclusively in vCenter by following Schedule a Compatibility Upgrade for a Virtual Machine (VMware vSphere documentation).

When scheduling an update prior to performing an update of OpenShift Container Platform, the virtual hardware update occurs when the nodes are rebooted during the course of the OpenShift Container Platform update.
