---
title: "Managing worker nodes"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-managing-worker-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-managing-worker-nodes
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Managing worker nodes

[id="learning-getting-started-managing-worker-nodes"]
= Managing worker nodes

[role="_abstract"]
To manage multiple worker nodes as a single entity, configure machine pools for your OpenShift Container Platform cluster. You can create custom machine pools by using the {rosa-cli-first} or {cluster-manager}.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-cli_{context}"]
= Creating a machine pool with the {rosa-cli}

[role="_abstract"]
You can use the {rosa-cli} to create a machine pool.

.Procedure

. Run the following command:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> --name=<machinepool-name> --replicas=<number-nodes>
----
+
*For example*:
+
[source,terminal]
----
 $ rosa create machinepool --cluster=my-rosa-cluster --name=new-mp
 --replicas=2
----
+
*Example output*:
+
[source,terminal]
----
I: Machine pool 'new-mp' created successfully on cluster 'my-rosa-cluster'
I: To view all machine pools, run 'rosa list machinepools -c my-rosa-cluster'
----

. *Optional:* Add node labels or taints to specific nodes in a new machine pool by running the following command:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> --name=<machinepool-name> --replicas=<number-nodes> --labels=`<key=pair>`
----
+
*For example*:
+
[source,terminal]
----
$ rosa create machinepool --cluster=my-rosa-cluster --name=db-nodes-mp --replicas=2 --labels='app=db','tier=backend'
----
+
*Example output*:
+
[source,terminal]
----
I: Machine pool 'db-nodes-mp' created successfully on cluster 'my-rosa-cluster'
----
+
This creates an additional 2 nodes that can be managed as a unit and also assigns them the labels shown.

. Run the following command to confirm machine pool creation and the assigned labels:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster-name>
----
+
*Example output*:
+
[source,terminal]
----
ID       AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    DISK SIZE  VERSION  AUTOREPAIR
workers  Yes          2/2-4     m5.xlarge                          us-east-1f         subnet-<subnet_id>  300 GiB    4.14.36  Yes
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-ui_{context}"]
= Creating a machine pool with the UI

[role="_abstract"]
You can create your machine pools by using {cluster-manager}.

.Procedure

. Log in to the {cluster-manager-url} and click your cluster.
+
image::cloud-experts-getting-started-managing-ocm-cluster.png[]

. Click the *Machine pools* tab.
+
image:cloud-experts-getting-started-managing-mp-ocm.png[]

. Click *Add machine pool*.

. Enter the desired configuration.
+
[TIP]
====
You can also and expand the *Edit node labels and taints* section to add node labels and taints to the nodes in the machine pool.
====
+
image::cloud-experts-getting-started-managing-mp-nlt.png[]

. Click the *Add machine pool* button to save.
. You will see the new machine pool you created.
+
image::cloud-experts-getting-started-managing-mp-fromui.png[]
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-scaling-cli_{context}"]
= Scaling worker nodes using the CLI

[role="_abstract"]
Edit a machine pool to scale the number of worker nodes in that specific machine pool by using {rosa-cli}.

.Procedure

. Run the following command to see the default machine pool that is created with each cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster-name>
----
+
*Example output*:
+
[source,terminal]
----
ID          AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS            TAINTS    AVAILABILITY ZONES
Default     No           2         m5.xlarge                                  us-east-1a
----

. To scale the default machine pool out to a different number of nodes, run the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster-name> --replicas=<number-nodes> <machinepool-name>
----
+
*For example*:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=my-rosa-cluster --replicas 3 Default
----

. Run the following command to confirm that the machine pool has scaled:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster-name> | grep Compute
----
+
*For example*:
+
[source,terminal]
----
$ rosa describe cluster --cluster=my-rosa-cluster | grep Compute
----
+
*Example output*:
+
[source,terminal]
----
 - Compute (Autoscaled):    2-4
 - Compute (current):       2
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-scaling-ui_{context}"]
= Scaling worker nodes using the UI

[role="_abstract"]
Edit a machine pool to scale the number of worker nodes in that specific machine pool by using {cluster-manager}.

.Procedure

. Click the three dots to the right of the machine pool you want to edit.
. Click *Edit*.
. Enter the desired number of nodes, and click *Save*.
. Confirm that the cluster has scaled by selecting the cluster, clicking the *Overview* tab, and scrolling to *Compute listing*. The compute listing should equal the scaled nodes. For example, 3/3.
+
image::cloud-experts-getting-started-managing-ocm-nodes.png[]
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-node-labels_{context}"]
= Adding node labels

[role="_abstract"]
To provide a description or extra information, you can add node labels to your machine pools by using the {rosa-cli}.

.Procedure
* Use the following command to add node labels:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster-name> --replicas=<number-nodes> --labels='key=value' <machinepool-name>
----
+
*For example*:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=my-rosa-cluster --replicas=2 --labels 'foo=bar','baz=one' new-mp
----
+
This adds 2 labels to the new machine pool.
+
[IMPORTANT]
====
This command replaces all machine pool configurations with the newly defined configuration. If you want to add another label *and* keep the old label, you must state both the new and the preexisting label. Otherwise the command will replace all preexisting labels with the one you wanted to add. Similarly, if you want to delete a label, run the command and state the ones you want, excluding the one you want to delete.
====
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-managing-worker-nodes.adoc
[id="learning-getting-started-learning-machine-pool-mixing-node-types_{context}"]
= Mixing node types

[role="_abstract"]
You can also mix different worker node machine types in the same cluster by using new machine pools. You cannot change the node type of a machine pool once it is created, but you can create a new machine pool with different nodes by adding the `--instance-type` flag.

.Procedure
. For example, to change the database nodes to a different node type, run the following command:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> --name=<mp-name> --replicas=<number-nodes> --labels='<key=pair>' --instance-type=<type>
----
+
*For example*:
+
[source,terminal]
----
$ rosa create machinepool --cluster=my-rosa-cluster --name=db-nodes-large-mp --replicas=2 --labels='app=db','tier=backend' --instance-type=m5.2xlarge
----

. To see all the instance types available, run the following command:
+
[source,terminal]
----
$ rosa list instance-types
----

. To make step-by-step changes, use the `--interactive` flag:
+
[source,terminal]
----
$ rosa create machinepool -c <cluster-name> --interactive
----
+
image::cloud-experts-getting-started-managing-mp-interactive.png[]

. Run the following command to list the machine pools and see the new, larger instance type:
+
[source,terminal]
----
$ rosa list machinepools -c <cluster-name>
----
+
image::cloud-experts-getting-started-managing-large-mp.png[]

[role="_additional-resources"]
[id="additional-resources_managing-work-nodes-tutorial_{context}"]
.Additional resources
* About machine pools
