---
title: "About autoscaling nodes on a cluster"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-nodes-about-autoscaling-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-nodes-about-autoscaling-nodes
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# About autoscaling nodes on a cluster

[id="rosa-nodes-about-autoscaling-nodes"]
= About autoscaling nodes on a cluster

[IMPORTANT]
====
Autoscaling is available only on clusters that were purchased through the Red{nbsp}Hat Marketplace.
====

The autoscaler option can be configured to automatically scale the number of machines in a machine pool.

The cluster autoscaler increases the size of the machine pool when there are pods that failed to schedule on any of the current nodes due to insufficient resources or when another node is necessary to meet deployment needs. The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

Additionally, the cluster autoscaler decreases the size of the machine pool when some nodes are consistently not needed for a significant period, such as when it has low resource use and all of its important pods can fit on other nodes.

When you enable autoscaling, you must also set a minimum and maximum number of worker nodes.

[NOTE]
====
Only cluster owners and organization admins can scale or delete a cluster.
====

[id="nodes-enabling-autoscaling-nodes"]
== Enabling autoscaling nodes on a cluster

You can enable autoscaling on worker nodes to increase or decrease the number of nodes available by editing the machine pool definition for an existing cluster.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-nodes-about-autoscaling-nodes.adoc
// * nodes/nodes-about-autoscaling-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-nodes-about-autoscaling-nodes.adoc

[id="ocm-enabling-autoscaling_{context}"]
= Enable autoscaling nodes in an existing cluster using {cluster-manager-first}

[role="_abstract"]
Enable autoscaling for worker nodes in the machine pool definition from {cluster-manager} console.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you want to enable autoscaling for.

. On the selected cluster, select the *Machine pools* tab.

. Click the Options menu {kebab} at the end of the machine pool that you want to enable autoscaling for and select *Edit*.

. On the *Edit machine pool* dialog, select the *Enable autoscaling* checkbox.

. Select *Save* to save these changes and enable autoscaling for the machine pool.

[NOTE]
====
Additionally, you can configure autoscaling on the default machine pool when you create the cluster using interactive mode.
====
// This can be included once the ROSA HCP files are added.
// ifdef::openshift-rosa-hcp[]
// [NOTE]
// ====
// Additionally, you can configure autoscaling on the default machine pool when you create the cluster.
// ====
// endif::[]

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-nodes-about-autoscaling-nodes.adoc
// * nodes/nodes-about-autoscaling-nodes.adoc

[id="rosa-enabling-autoscaling-nodes_{context}"]
= Enabling autoscaling nodes in an existing cluster using the ROSA CLI

Configure autoscaling to dynamically scale the number of worker nodes up or down based on load.

Successful autoscaling is dependent on having the correct AWS resource quotas in your AWS account. Verify resource quotas and request quota increases from the AWS console.

.Procedure

. To identify the machine pool IDs in a cluster, enter the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID      AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONES    SUBNETS    SPOT INSTANCES  DISK SIZE  SG IDs
worker  No           2         m7i.xlarge                          us-east-2a                       No              300 GiB
mp1     No           2         m7i.xlarge                          us-east-2a                       No              300 GiB
----
[source,terminal]
----
ID       AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
workers  No           2/2       m7i.xlarge                          us-east-2a         subnet-03c2998b482bf3b20  4.16.6   Yes
mp1      No           2/2       m7i.xlarge                          us-east-2a         subnet-03c2998b482bf3b20  4.16.6   Yes
----

. Get the ID of the machine pools that you want to configure.

. To enable autoscaling on a machine pool, enter the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> <machinepool_ID> --enable-autoscaling --min-replicas=<number> --max-replicas=<number>
----
+
.Example
Enable autoscaling on a machine pool with the ID `mp1` on a cluster named `mycluster`, with the number of replicas set to scale between 2 and 5 worker nodes:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster mp1 --enable-autoscaling --min-replicas=2 --max-replicas=5
----

[id="nodes-disabling-autoscaling-nodes"]
== Disabling autoscaling nodes on a cluster

You can disable autoscaling on worker nodes to increase or decrease the number of nodes available by editing the machine pool definition for an existing cluster.

You can disable autoscaling on a cluster using {cluster-manager-first}.

You can disable autoscaling on a cluster using {cluster-manager-first} or the {rosa-cli-first}.

[NOTE]
====
Additionally, you can configure autoscaling on the default machine pool when you create the cluster using interactive mode.
====
// This can be included once the ROSA HCP files are added.
// ifdef::openshift-rosa-hcp[]
// [NOTE]
// ====
// Additionally, you can configure autoscaling on the default machine pool when you create the cluster.
// ====
// endif::[]

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-nodes-about-autoscaling-nodes.adoc
// * nodes/nodes-about-autoscaling-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-nodes-about-autoscaling-nodes.adoc

[id="ocm-disabling-autoscaling_{context}"]
= Disable autoscaling nodes in an existing cluster using {cluster-manager-first}

[role="_abstract"]
Disable autoscaling for worker nodes in the machine pool definition from {cluster-manager}.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster with autoscaling that must be disabled.

. On the selected cluster, select the *Machine pools* tab.

. Click the Options menu {kebab} at the end of the machine pool with autoscaling and select *Edit*.

. On the *Edit machine pool* dialog, clear the *Enable autoscaling* checkbox.

. Select *Save* to save these changes and disable autoscaling from the machine pool.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-nodes-about-autoscaling-nodes.adoc
// * nodes/nodes-about-autoscaling-nodes.adoc

[id="rosa-disabling-autoscaling_{context}"]
= Disabling autoscaling nodes in an existing cluster using the ROSA CLI

Disable autoscaling for worker nodes in the machine pool definition using the {rosa-cli-first}.

.Procedure

* Enter the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> <machinepool_ID> --enable-autoscaling=false --replicas=<number>
----
+
.Example
Disable autoscaling on the `default` machine pool on a cluster named `mycluster`:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster default --enable-autoscaling=false --replicas=3
----

[role="_additional-resources"]
[id="nodes-about-autoscaling-nodes-additional-resources"]
== Additional resources
* Troubleshooting: Autoscaling is not scaling down nodes
* About machinepools
* Managing compute nodes
* ROSA CLI command reference
