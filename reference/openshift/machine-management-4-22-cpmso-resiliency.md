---
title: "Control plane resiliency and recovery"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-resiliency
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-resiliency
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Control plane resiliency and recovery

[id="cpmso-resiliency"]
= Control plane resiliency and recovery

[role="_abstract"]
You can use the control plane machine set to improve the resiliency of the control plane for your OpenShift Container Platform cluster.

[id="cpmso-failure-domains_{context}"]
== High availability and fault tolerance with failure domains

When possible, the control plane machine set spreads the control plane machines across multiple failure domains. This configuration provides high availability and fault tolerance within the control plane. This strategy can help protect the control plane when issues arise within the infrastructure provider.

//Failure domain platform support and configuration
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-resiliency.adoc

// TODO: See if I can find RHOSP docs links for the proposed changes.

[id="cpmso-failure-domains-provider_{context}"]
= Failure domain platform support and configuration

[role="_abstract"]
Review failure domain support for your cloud provider to determine how to configure high availability for your control plane.

.Failure domain support matrix
[cols="<.^,^.^,^.^"]
|====
|Cloud provider |Support for failure domains |Provider nomenclature

|Amazon Web Services (AWS)
|X
|Availability Zone (AZ)

|{gcp-first}
|X
|zone

|Microsoft Azure
|X
|Azure availability zone

|Nutanix
|X
|failure domain

|{rh-openstack-first}
|X
|OpenStack Nova availability zones and OpenStack Cinder availability zones

|VMware vSphere
|X
|failure domain mapped to a vSphere Zone ^[1]^
|====
. For more information, see "Regions and zones for a VMware vCenter".

The failure domain configuration in the control plane machine set custom resource (CR) is platform-specific. For more information about failure domain parameters in the CR, see the sample failure domain configuration for your provider.

[role="_additional-resources"]
.Additional resources

* Sample {aws-full} failure domain configuration

* Sample {gcp-full} failure domain configuration

* Sample {azure-full} failure domain configuration

* Adding failure domains to an existing Nutanix cluster

* Sample {rh-openstack-first} failure domain configuration

* Sample {vmw-full} failure domain configuration

* Regions and zones for a VMware vCenter

//Balancing control plane machines
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-resiliency.adoc

[id="cpmso-failure-domains-balancing_{context}"]
= Balancing control plane machines

[role="_abstract"]
The control plane machine set balances control plane machines across failure domains to ensure fault tolerance and high availability.

//If failure domains must be reused, they are selected alphabetically by name.
When possible, the control plane machine set uses each failure domain equally to ensure appropriate fault tolerance. If there are fewer failure domains than control plane machines, failure domains are selected for reuse alphabetically by name. For clusters with no failure domains specified, all control plane machines are placed within a single failure domain.

Some changes to the failure domain configuration cause the control plane machine set to rebalance the control plane machines. For example, if you add failure domains to a cluster with fewer failure domains than control plane machines, the control plane machine set rebalances the machines across all available failure domains.

//Recovery of the failed control plane machines
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-resiliency.adoc
// * rosa/architecture/control-plane.adoc
// * osd/architecture/control-plane.adoc

[id="cpmso-control-plane-recovery_{context}"]
= Recovery of failed control plane machines

[role="_abstract"]
The Control Plane Machine Set Operator automates the recovery of control plane machines to maintain cluster availability without manual intervention. When a control plane machine is deleted, the Operator creates a replacement with the configuration that is specified in the `ControlPlaneMachineSet` custom resource (CR).

For clusters that use control plane machine sets, you can configure a machine health check. The machine health check deletes unhealthy control plane machines so that they are replaced.

[IMPORTANT]
====
If you configure a `MachineHealthCheck` resource for the control plane, set the value of `maxUnhealthy` to `1`.

This configuration ensures that the machine health check takes no action when multiple control plane machines appear to be unhealthy. Multiple unhealthy control plane machines can indicate that the etcd cluster is degraded or that a scaling operation to replace a failed machine is in progress.

If the etcd cluster is degraded, manual intervention might be required. If a scaling operation is in progress, the machine health check should allow it to finish.
====

[role="_additional-resources"]
.Additional resources
* Deploying machine health checks

//Quorum protection with machine lifecycle hooks
// Module included in the following assemblies:
//
// * machine_management/deleting-machine.adoc
// * machine_management/control_plane_machine_management/cpmso-resiliency.adoc

[id="machine-lifecycle-hook-deletion-etcd_{context}"]
= Quorum protection with machine lifecycle hooks

[role="_abstract"]
To protect etcd quorum on OpenShift Container Platform clusters that use the Machine API Operator, the etcd Operator uses lifecycle hooks for the machine deletion phase to implement a quorum protection mechanism.

By using a `preDrain` lifecycle hook, the etcd Operator can control when the pods on a control plane machine are drained and removed. To protect etcd quorum, the etcd Operator prevents the removal of an etcd member until it migrates that member onto a new node within the cluster.

This mechanism allows the etcd Operator precise control over the members of the etcd quorum and allows the Machine API Operator to safely create and remove control plane machines without specific operational knowledge of the etcd cluster.

[id="machine-lifecycle-hook-deletion-etcd-order_{context}"]
== Control plane deletion with quorum protection processing order

When a control plane machine is replaced on a cluster that uses a control plane machine set, the cluster temporarily has four control plane machines. When the fourth control plane node joins the cluster, the etcd Operator starts a new etcd member on the replacement node. When the etcd Operator observes that the old control plane machine is marked for deletion, it stops the etcd member on the old node and promotes the replacement etcd member to join the quorum of the cluster.

The control plane machine `Deleting` phase proceeds in the following order:

. A control plane machine is slated for deletion.
. The control plane machine enters the `Deleting` phase.
. To satisfy the `preDrain` lifecycle hook, the etcd Operator takes the following actions:
+
--
.. The etcd Operator waits until a fourth control plane machine is added to the cluster as an etcd member. This new etcd member has a state of `Running` but not `ready` until it receives the full database update from the etcd leader.
.. When the new etcd member receives the full database update, the etcd Operator promotes the new etcd member to a voting member and removes the old etcd member from the cluster.
--
After this transition is complete, it is safe for the old etcd pod and its data to be removed, so the `preDrain` lifecycle hook is removed.
. The control plane machine status condition `Drainable` is set to `True`.
. The machine controller attempts to drain the node that is backed by the control plane machine.
** If draining fails, `Drained` is set to `False` and the machine controller attempts to drain the node again.
** If draining succeeds, `Drained` is set to `True`.
. The control plane machine status condition `Drained` is set to `True`.
. If no other Operators have added a `preTerminate` lifecycle hook, the control plane machine status condition `Terminable` is set to `True`.
. The machine controller removes the instance from the infrastructure provider.
. The machine controller deletes the `Node` object.

.YAML snippet demonstrating the etcd quorum protection `preDrain` lifecycle hook
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preDrain:
    - name: EtcdQuorumOperator
      owner: clusteroperator/etcd
  ...
----
where:

`spec.lifecycleHooks.preDrain.name`:: Specifies the name of the `preDrain` lifecycle hook.
`spec.lifecycleHooks.preDrain.owner`:: Specifies the hook-implementing controller that manages the `preDrain` lifecycle hook.

[role="_additional-resources"]
.Additional resources
* Lifecycle hooks for the machine deletion phase
