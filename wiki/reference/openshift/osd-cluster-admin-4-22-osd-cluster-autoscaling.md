---
title: "Cluster autoscaling for {product-title}"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-osd-cluster-autoscaling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/osd-cluster-autoscaling
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# Cluster autoscaling for {product-title}

[id="osd-cluster-autoscaling_{context}"]
= Cluster autoscaling for OpenShift Container Platform

[role="_abstract"]
Apply autoscaling to OpenShift Container Platform clusters to automatically adjust the number of worker nodes based on workload demands. This optimizes resource utilization and reduces costs by scaling up when demand increases and scaling down when resources are underutilized.

[IMPORTANT]
====
You can configure the cluster autoscaler only in clusters where the machine API is operational.

Only one cluster autoscaler can be created per cluster.
====

// Module included in the following assemblies:
//
// * nodes/nodes-about-autoscaling-nodes.adoc
// * machine_management/applying-autoscaling.adoc
// * osd_cluster_admin/osd_nodes/osd-nodes-about-autoscaling-nodes.adoc
// * osd_cluster_admin/osd-cluster-autoscaling.adoc
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc
// * rosa_cluster_admin/rosa-cluster-autoscaling-hcp.adoc (temporary)

[id="cluster-autoscaler-about_{context}"]
= The cluster autoscaler

[role="_abstract"]
The cluster autoscaler adjusts the size of an OpenShift Container Platform cluster to meet its current deployment needs. It uses declarative, Kubernetes-style arguments to provide infrastructure management that does not rely on objects of a specific cloud provider.
In OpenShift Container Platform, the Cluster Autoscaler is fully managed, which means it is hosted along with the control plane.

The cluster autoscaler increases the size of the cluster when there are pods that fail to schedule on any of the current worker nodes due to insufficient resources or when another node is necessary to meet deployment needs. The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

The cluster autoscaler computes the total memory, CPU, and GPU only on the nodes that belong to autoscaling machine pools. All of the machine pool nodes that are not autoscaling are excluded from this aggregation. For example, if you set the `maxNodesTotal` to `50` on a OpenShift Container Platform cluster with three machine pools in which a single machine pool is not autoscaling, the cluster autoscaler restricts the total nodes to `50` in only those two machine pools that are autoscaling. The single manually scaling machine pool can have additional nodes, making the overall cluster nodes total more than `50`.

The cluster autoscaler computes the total
memory, CPU, and GPU
memory and CPU
on all nodes the cluster, even though it does not manage the control plane nodes. These values are not single-machine oriented. They are an aggregation of all the resources in the entire cluster. For example, if you set the maximum memory resource limit, the cluster autoscaler includes all the nodes in the cluster when calculating the current memory usage. That calculation is then used to determine if the cluster autoscaler has the capacity to add more worker resources.

[IMPORTANT]
====
Ensure that the `maxNodesTotal` value in the `ClusterAutoscaler` custom resource (CR) that you create is large enough to account for the total possible number of machines in your cluster. This value must encompass the number of control plane machines and the possible number of compute machines that you might scale to.
====

[id="cluster-autoscaler-scale-down_{context}"]
== Automatic node removal

Every 10 seconds, the cluster autoscaler checks which nodes are unnecessary in the cluster and removes them. The cluster autoscaler considers a node for removal if the following conditions apply:

* The node utilization is less than the _node utilization level_ threshold for the cluster. The node utilization level is the sum of the requested resources divided by the allocated resources for the node. If you do not specify a value in the `ClusterAutoscaler` custom resource, the cluster autoscaler uses a default value of `0.5`, which corresponds to 50% utilization.
* The cluster autoscaler can move all pods running on the node to the other nodes. The Kubernetes scheduler is responsible for scheduling pods on the nodes.
* The cluster autoscaler does not have scale down disabled annotation.

If the following types of pods are present on a node, the cluster autoscaler will not remove the node:

* Pods with restrictive pod disruption budgets (PDBs).
* Kube-system pods that do not run on the node by default.
* Kube-system pods that do not have a PDB or have a PDB that is too restrictive.
* Pods that are not backed by a controller object such as a deployment, replica set, or stateful set.
* Pods with local storage.
* Pods that cannot be moved elsewhere because of a lack of resources, incompatible node selectors or affinity, matching anti-affinity, and so on.
* Unless they also have a `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` annotation, pods that have a `"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"` annotation.

For example, you set the maximum CPU limit to 64 cores and configure the cluster autoscaler to only create machines that have 8 cores each. If your cluster starts with 30 cores, the cluster autoscaler can add up to 4 more nodes with 32 cores, for a total of 62.

[NOTE]
====
By default, when the cluster autoscaler removes a node, it does not cordon the node when draining the pods from the node. You can configure the cluster autoscaler to cordon the node before draining and moving the pods by setting the `spec.scaleDown.cordonNodeBeforeTerminating` parameter to `enabled` in the `ClusterAutoscaler` CR. This parameter is disabled by default. It is recommended to enable this parameter in production clusters because of the risk of data loss, application errors, pods getting stuck in the terminating state, or other issues if the cluster autoscaler removes a node when the parameter is disabled. Leaving this parameter disabled, which can result in faster node removal, might be appropriate in clusters that run only stateless workloads.
====

[id="cluster-autoscaler-limitations_{context}"]
== Limitations

If you configure the cluster autoscaler, additional usage restrictions apply:

* Do not modify the nodes that are in autoscaled node groups directly. All nodes within the same node group have the same capacity and labels and run the same system pods.
* Specify requests for your pods.
* If you have to prevent pods from being deleted too quickly, configure appropriate PDBs.
* Confirm that your cloud provider quota is large enough to support the maximum node pools that you configure.
* Do not run additional node group autoscalers, especially the ones offered by your cloud provider.

[NOTE]
====
The cluster autoscaler only adds nodes in autoscaled node groups if doing so would result in a schedulable pod.
If the available node types cannot meet the requirements for a pod request, or if the node groups that could meet these requirements are at their maximum size, the cluster autoscaler cannot scale up.
====

[id="cluster-autoscaler-interaction_{context}"]
== Interaction with other scheduling features

The horizontal pod autoscaler (HPA) and the cluster autoscaler modify cluster resources in different ways. The HPA changes the deployment's or replica set's number of replicas based on the current CPU load. If the load increases, the HPA creates new replicas, regardless of the amount of resources available to the cluster. If there are not enough resources, the cluster autoscaler adds resources so that the HPA-created pods can run. If the load decreases, the HPA stops some replicas. If this action causes some nodes to be underutilized or completely empty, the cluster autoscaler deletes the unnecessary nodes.

The cluster autoscaler takes pod priorities into account. The Pod Priority and Preemption feature enables scheduling pods based on priorities if the cluster does not have enough resources, but the cluster autoscaler ensures that the cluster has resources to run all pods. To honor the intention of both features, the cluster autoscaler includes a priority cutoff function. You can use this cutoff to schedule "best-effort" pods, which do not cause the cluster autoscaler to increase resources but instead run only when spare resources are available.

Pods with priority lower than the cutoff value do not cause the cluster to scale up or prevent the cluster from scaling down. No new nodes are added to run the pods, and nodes running these pods might be deleted to free resources.

Default priority cutoff is 0. It can be changed using `--expendable-pods-priority-cutoff` flag, but we discourage it. cluster autoscaler also doesn't trigger scale-up if an unschedulable Pod is already waiting for a lower priority Pod preemption.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc
// * osd_cluster_admin/osd-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-ui-during_{context}"]
= Enable autoscaling during cluster creation with {cluster-manager}

[role="_abstract"]
Enable cluster autoscaling during cluster creation by using {cluster-manager} to automatically adjust the number of nodes based on workload demands.

.Procedure

. During cluster creation, check the *Enable autoscaling* box. The *Edit cluster autoscaling settings* button becomes selectable.

.. You can also choose the minimum or maximum amount of nodes to autoscale.

. Click *Edit cluster autoscaling settings*.

. Edit any settings you want and then click *Close*.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc
// * osd_cluster_admin/osd-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-ui-after_{context}"]
= Enable autoscaling after cluster creation with {cluster-manager}

[role="_abstract"]
Enable cluster autoscaling on an existing cluster by using {cluster-manager} to automatically adjust the number of nodes based on workload demands.

.Procedure

. In {cluster-manager}, click the name of the cluster you want to autoscale. The *Overview* page for the cluster has a *Autoscaling* item that indicates if it is enabled or disabled.

. Click the *Machine Pools* tab.

. Click the *Edit cluster autoscaling* button. The *Edit cluster autoscaling* settings window is shown.

. Click the *Autoscale cluster* toggle at the top of the window. All the settings are now editable.

. Edit any settings you want and then click *Save*.

. Click the *x* at the top right of the screen to close the settings window.
+
To revert all autoscaling settings to the defaults if they have been changed, click the *Revert all to defaults* button.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc
// * osd_cluster_admin/osd-cluster-autoscaling.adoc

[id="rosa-cluster-autoscale-settings_{context}"]
= Cluster autoscaling settings using {cluster-manager}

[role="_abstract"]
The tables explain all the configurable UI settings when using cluster autoscaling with {cluster-manager}.

.Configurable general settings for cluster autoscaling when using {cluster-manager}
[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Default

|`log-verbosity`
|Sets the autoscaler log level. The default value is 1. Level 4 is recommended for debugging. Level 6 enables almost everything.
|`integer`
|1

|`skip-nodes-with-local-storage`
|If `true`, the cluster autoscaler never deletes nodes with pods with local storage, e.g. EmptyDir or HostPath.
|`boolean`
|true

|`max-pod-grace-period`
|Gives pods graceful termination time in seconds before scaling down.
|`integer`
|600

|`max-node-provision-time`
|Maximum time the cluster autoscaler waits for nodes to be provisioned.
|`string`
|15m

|`pod-priority-threshold`
|Allows users to schedule "best-effort" pods, which are not expected to trigger cluster autoscaler actions. These pods only run when spare resources are available.
|`integer`
|-10

|`ignore-daemonsets-utilization`
|Determines whether the cluster autoscaler ignores daemon set pods when calculating resource utilization for scaling down.
|`boolean`
|false

|`balance-similar-node-groups`
|If `true`, this setting automatically identifies node groups with the same instance type and the same set of labels and tries to keep the respective sizes of those node groups balanced.
|`boolean`
|false

|`balancing-ignored-labels`
|This option specifies labels that the cluster autoscaler should ignore when considering node group similarity. This option cannot contain spaces.
|`array (string)`
|Format should be a comma-separated list of labels.
|===

.Configurable resource limit settings for cluster autoscaling when using {cluster-manager}
[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Default

|`cores-total-min`
|Minimum number of cores in cluster. The cluster autoscaler does not scale the cluster less than this number.
|`object`
|0

|`cores-total-max`
|Maximum number of cores in cluster. The cluster autoscaler does not scale the cluster greater than this number.
|`object`
|180 * 64 (11520)

|`memory-total-min`
|Minimum number of gigabytes of memory in cluster. The cluster autoscaler does not scale the cluster less than this number.
|`object`
|0

|`memory-total-max`
|Maximum number of gigabytes of memory in cluster. The cluster autoscaler does not scale the cluster greater than this number.
|`object`
|180 * 64 * 20 (230400)

|`max-nodes-total`
|Maximum number of nodes in all node groups. Includes all nodes, not just automatically scaled nodes. The cluster autoscaler does not grow the cluster greater than this number.
|`integer`
|180

|GPUs
|Minimum and maximum number of different GPUs in cluster. The cluster autoscaler does not scale the cluster less than or greater than these numbers.
|`array`
|Format should be a comma-separated list of "<gpu_type>:<min>:<max>".
|===

.Configurable scale down settings for cluster autoscaling when using {cluster-manager}
[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Default

|`scale-down-enabled`
|Should the cluster autoscaler scale down the cluster.
|`boolean`
|true

|`scale-down-utilization-threshold`
|Node utilization level, defined as the sum of the requested resources divided by capacity, below which a node can be considered for scale down.
|`float`
|0.5

|`scale-down-unneeded-time`
|How long a node should be unneeded before it is eligible for scale down.
|`string`
|10m

|`scale-down-delay-after-add`
|How long after scale up that scale-down evaluation resumes.
|`string`
|10m

|`scale-down-delay-after-delete`
|How long after node deletion that scale-down evaluation resumes.
|`string`
|0s

|`scale-down-delay-after-failure`
|How long after scale down failure that scale-down evaluation resumes.
|`string`
|3m
|===

[role="_additional-resources"]
== Additional resources

* About machine pools
* Managing compute nodes
* Applying autoscaling to a cluster
* Overview of machine management
