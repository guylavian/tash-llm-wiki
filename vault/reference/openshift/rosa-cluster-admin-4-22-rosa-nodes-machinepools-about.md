---
title: "About machine pools"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-nodes-machinepools-about
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-nodes-machinepools-about
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# About machine pools

[id="rosa-nodes-machinepools-about"]
= About machine pools

OpenShift Container Platform uses machine pools as an elastic, dynamic provisioning method on top of your cloud infrastructure.

The primary resources are machines, compute machine sets, and machine pools.

== Machines
A machine is a fundamental unit that describes the host for a worker node.

== Machine sets
`MachineSet` resources are groups of compute machines. If you need more machines or must scale them down, change the number of replicas in the machine pool to which the compute machine sets belong.

Machine sets are not directly modifiable in OpenShift Container Platform.

== Machine pools
Machine pools are a higher level construct to compute machine sets.

A machine pool creates compute machine sets that are all clones of the same configuration across availability zones. Machine pools perform all of the host node provisioning management actions on a worker node. If you need more machines or must scale them down, change the number of replicas in the machine pool to meet your compute needs. You can manually configure scaling or set autoscaling.

In OpenShift Container Platform clusters, the hosted control plane spans multiple availability zones (AZ) in the installed cloud region. Each machine pool in a OpenShift Container Platform cluster deploys in a single subnet within a single AZ.

Multiple machine pools can exist on a single cluster, and each machine pool can contain a unique node type and node size (AWS EC2 instance type and size) configuration.

=== Machine pools during cluster installation

By default, a cluster has one machine pool. During cluster installation, you can define instance type or size and add labels to this machine pool as well as define the size of the root disk.

=== Configuring machine pools after cluster installation

After a cluster's installation:

* You can remove or add labels to any machine pool.
* You can add additional machine pools to an existing cluster.
* You can add taints to any machine pool if there is one machine pool without any taints.
* You can create or delete a machine pool if there is one machine pool without any taints and at least two replicas for a Single-AZ cluster or three replicas for a Multi-AZ cluster.
* You can create or delete a machine pool if there is one machine pool without any taints and at least two replicas.
+
[NOTE]
====
You cannot change the machine pool node type or size. The machine pool node type or size is specified during their creation only. If you need a different node type or size, you must re-create a machine pool and specify the required node type or size values.
====
* You can add a label to each added machine pool.

.Procedure

* *Optional:* Add a label to the default machine pool after configuration by using the default machine pool labels and running the following command:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster_name> <machinepool_name> -i
----
+
.Example input
+
[source,terminal]
----
$ rosa edit machinepool -c mycluster worker -i
? Enable autoscaling: No
? Replicas: 3
? Labels: mylabel=true
I: Updated machine pool 'worker' on cluster 'mycluster'
----

=== Machine pool upgrade requirements

Each machine pool in a OpenShift Container Platform cluster upgrades independently. Because the machine pools upgrade independently, they must remain within 2 minor (Y-stream) versions of the hosted control plane. For example, if your hosted control plane is 4.16.z, your machine pools must be at least 4.14.z.

The following image depicts how machine pools work within OpenShift Container Platform clusters:

image::hcp-rosa-machine-pools.png[Machine pools on ROSA classic and {product-titLe} clusters]

[NOTE]
====
Machine pools in OpenShift Container Platform clusters each upgrade independently and the machine pool versions must remain within two minor (Y-stream) versions of the control plane.
====

== Machine pools in multiple zone clusters
In a cluster created across multiple Availability Zones (AZ), the machine pools can be created across either all of the three AZs or any single AZ of your choice. The machine pool created by default at the time of cluster creation will be created with machines in all three AZs and scale in multiples of three.

If you create a new Multi-AZ cluster, the machine pools are replicated to those zones automatically. By default, if you add a machine pool to an existing Multi-AZ cluster, the new machine pool is automatically created in all of the zones.

[NOTE]
====
You can override this default setting and create a machine pool in a Single-AZ of your choice.
====

Similarly, deleting a machine pool will delete it from all zones.
Due to this multiplicative effect, using machine pools in Multi-AZ cluster can consume more of your project's quota for a specific region when creating machine pools.

== Additional resources
* Managing compute nodes
* About autoscaling
* Configuring PID limits
