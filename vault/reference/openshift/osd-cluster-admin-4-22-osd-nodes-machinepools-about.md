---
title: "About machine pools"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-osd-nodes-machinepools-about
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/osd-nodes-machinepools-about
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# About machine pools

[id="osd-machinepools-about"]
= About machine pools

[role="_abstract"]
OpenShift Container Platform uses machine pools as an elastic, dynamic provisioning method on top of your cloud infrastructure. The primary resources are machines, machine sets, and machine pools.

A machine is a fundamental unit that describes the host for a worker node. `MachineSet` resources are groups of compute machines. If you need more machines or must scale them down, change the number of replicas in the machine pool to which the compute machine sets belong.

Machine pools are a higher level construct to compute machine sets. A machine pool creates compute machine sets that are all clones of the same configuration across availability zones. Machine pools perform all of the host node provisioning management actions on a worker node. If you need more machines or must scale them down, change the number of replicas in the machine pool to meet your compute needs. You can manually configure scaling or set autoscaling.

By default, a cluster is created with one machine pool. You can add additional machine pools to an existing cluster, modify the default machine pool, and delete machine pools. Multiple machine pools can exist on a single cluster, and they can each have different types or different size nodes.

By default, when you create a machine pool in a multiple availability zone (Multi-AZ) cluster, that one machine pool has 3 zones. The machine pool, in turn, creates a total of 3 compute machine sets - one for each zone in the cluster. Each of those compute machine sets manages one or more machines in its respective availability zone.

If you create a new Multi-AZ cluster, the machine pools are replicated to those zones automatically. If you add a machine pool to an existing Multi-AZ, the new pool is automatically created in those zones. Similarly, deleting a machine pool will delete it from all zones. Due to this multiplicative effect, using machine pools in Multi-AZ cluster can consume more of your project's quota for a specific region when creating machine pools.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_nodes/osd-nodes-machinepools-about.adoc

[id="osd-deploying-machinepool-single-az-gcp_{context}"]
= Deploy a machine pool in a single availability zone within a Multi-AZ cluster

[role="_abstract"]
Deploy a single machine pool to a specific availability zone that is part of a Multi-AZ cluster. This option is useful when a required instance type is not available in all availability zones of a region or when your cluster does not need multiple instances of the required instance type.

.Prerequisites

* The {cluster-manager} API command-line interface (`ocm`) is installed.
+
[IMPORTANT]
====
[subs="attributes+"]
{cluster-manager} API command-line interface (`ocm`) is a Developer Preview feature only.
For more information about the support scope of Red Hat Developer Preview features, see Developer Preview Support Scope.
====

.Procedure

* Deploy a machine pool to a specific availability zone by running the following command:
+
[source,bash]
----
ocm create machine-pool \
  --cluster <cluster_name> \
  --instance-type <instance_type> \
  --replicas <number_of_replicas> \
  --availability-zone <availability_zone> \
  [<flags>] \
  <machine_pool_id>
----
+
Where:
+
** `<cluster_name>`: Replace with the name or ID of the cluster that you want to add the machine pool to.
** `<instance_type>`: Replace with the instance type you want to deploy to the single availability zone.
** `<number_of_replicas>`: Replace with the number of replicas of the selected instance type you want to include in the machine pool.
** `<availability_zone>`: Replace with the availability zone you want to add the machine pool to.
** `<flags>`: Optional. Replace with any additional flags available for machine pool creation.
** `<machine_pool_id>`: Replace with an ID for your machine pool.
+
[NOTE]
====
To view the additional flags available for machine pool creation, run the `ocm create machine-pool --help` command.
====

[role="_additional-resources"]
== Additional resources

* Managing compute nodes
* Managing cluster autoscaling
* Overview of machine management
* {gcp-full} instance types
* {gcp-full} regions and availability zones
