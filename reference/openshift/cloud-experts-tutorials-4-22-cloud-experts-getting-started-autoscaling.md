---
title: "Tutorial: Autoscaling"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-autoscaling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-autoscaling
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Autoscaling

[id="cloud-experts-getting-started-autoscaling"]
= Tutorial: Autoscaling

[role="_abstract"]
The cluster autoscaler adds or removes worker nodes from a cluster based on pod resources.

The cluster autoscaler increases the size of the cluster when:

* Pods fail to schedule on the current nodes due to insufficient resources.
* Another node is necessary to meet deployment needs.

The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

The cluster autoscaler decreases the size of the cluster when:

* Some nodes are consistently not needed for a significant period. For example, when a node has low resource use and all of its important pods can fit on other nodes.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-autoscaling.adoc

[id="cloud-experts-getting-started-autoscaling-cli_{context}"]
= Enabling autoscaling for an existing machine pool using the CLI

[role="_abstract"]
You can enable autoscaling on your machine pools by using the {rosa-cli-first}.

[NOTE]
====
Cluster autoscaling can be enabled at cluster creation and when creating a new machine pool by using the `--enable-autoscaling` option.
====

.Procedure
. Autoscaling is set based on machine pool availability. To find out which machine pools are available for autoscaling, run the following command:
+
[source,terminal]
----
$ rosa list machinepools -c <cluster-name>
----
+
**Example output**
+
[source,terminal]
----
ID         AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS     TAINTS    AVAILABILITY ZONES
Default    No           2         m5.xlarge                           us-east-1a
----

. Run the following command to add autoscaling to an available machine pool:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster-name> --enable-autoscaling <machinepool-name> --min-replicas=<num> --max-replicas=<num>
----
+
**Example input**
+
[source,terminal]
----
$ rosa edit machinepool -c my-rosa-cluster --enable-autoscaling Default --min-replicas=2 --max-replicas=4
----
+
The above command creates an autoscaler for the worker nodes that scales between 2 and 4 nodes depending on the resources.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-autoscaling.adoc

[id="cloud-experts-getting-started-autoscaling-ui_{context}"]
= Enabling autoscaling for an existing machine pool using the UI

[role="_abstract"]
You can enable autoscaling on your machine pools in {cluster-manager}.

[NOTE]
====
Cluster autoscaling can be enabled at cluster creation by checking the *Enable autoscaling* checkbox when creating machine pools.
====

.Procedure
. Go to the *Machine pools* tab and click the three dots in the right..
. Click *Scale*, then *Enable autoscaling*.
. Run the following command to confirm that autoscaling was added:
+
[source,terminal]
----
$ rosa list machinepools -c <cluster-name>
----
+
**Example output**
+
[source,terminal]
----
ID         AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS     TAINTS    AVAILABILITY ZONES
Default    Yes          2-4       m5.xlarge                           us-east-1a
----
