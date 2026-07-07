---
title: "Autoscaling"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-autoscaling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-autoscaling
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Autoscaling

[id="learning-getting-started-autoscaling"]
= Autoscaling

[role="_abstract"]
Configure cluster autoscaling to improve performance and ensure that your environment dynamically adapts to changing workload demands. The cluster autoscaler adds or removes worker nodes from a cluster based on pod resources.

The cluster autoscaler increases the size of the cluster when:

* Pods fail to schedule on the current nodes due to insufficient resources.
* Another node is necessary to meet deployment needs.

It does not increase the cluster resources beyond the limits that you specify.

The cluster autoscaler decreases the size of the cluster when:

* Some nodes are consistently not needed for a significant period. For example, when a node has low resource use and all of its important pods can fit on other nodes.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-autoscaling-cli_{context}"]
= Enabling autoscaling for an existing machine pool using the CLI

[role="_abstract"]
To ensure your environment dynamically adapts to changing workload demands, you can enable cluster autoscaling at cluster creation or when creating a new machine pool. To do this, use the `--enable-autoscaling` option.

.Procedure
. Autoscaling is set based on machine pool availability. To find out which machine pools are available for autoscaling, run the following command:
+
[source,terminal]
----
$ rosa list machinepools -c <cluster-name>
----
+
*For example*:
+
[source,terminal]
----
ID       AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    DISK SIZE  VERSION  AUTOREPAIR
workers  No           2/2       m5.xlarge                          us-east-1f         subnet-<subnet_id>  300 GiB    4.14.36  Yes
----

. Run the following command to add autoscaling to an available machine pool:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster-name> --enable-autoscaling <machinepool-name> --min-replicas=<num> --max-replicas=<num>
----
+
*For example*:
+
[source,terminal]
----
$ rosa edit machinepool -c my-rosa-cluster --enable-autoscaling workers --min-replicas=2 --max-replicas=4
----
+
The above command creates an autoscaler for the worker nodes that scales between 2 and 4 nodes depending on the resources.
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-autoscaling-web-ui_{context}"]
= Enabling autoscaling for an existing machine pool using the UI

[role="_abstract"]
You can enable cluster autoscaling when creating a cluster to ensure your environment automatically adapts to workload demands. To do this, select the *Enable autoscaling* checkbox when you create machine pools.

.Procedure
. Go to the *Machine pools* tab and click the three dots in the right..
. Click *Edit*, then *Enable autoscaling*.
. Edit the number of minimum and maximum node counts or leave the default numbers.
. Click *Save*.
. Run the following command to confirm that autoscaling was added:
+
[source,terminal]
----
$ rosa list machinepools -c <cluster-name>
----
+
*For example*:
+
[source,terminal]
----
ID       AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    DISK SIZE  VERSION  AUTOREPAIR
workers  Yes          2/2-4     m5.xlarge                          us-east-1f         subnet-<subnet_id>  300 GiB    4.14.36  Yes
----

[role="_additional-resources"]
== Additional resources

* Cluster autoscaler
