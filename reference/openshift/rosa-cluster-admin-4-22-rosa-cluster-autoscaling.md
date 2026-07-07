---
title: "Cluster autoscaling"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-cluster-autoscaling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-cluster-autoscaling
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Cluster autoscaling

[id="rosa-cluster-autoscaling"]
= Cluster autoscaling

[role="_abstract"]
Applying autoscaling to OpenShift Container Platform clusters involves configuring a cluster autoscaler and then configuring a machine autoscaler for at least one machine pool in your cluster.

Applying autoscaling to OpenShift Container Platform clusters involves configuring one or more machine pools with autoscaling. You can use the Cluster Autoscaler to further configure cluster-wide autoscaling that is applicable to all of the machine pools that are autoscaling.

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

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-cli-interactive_{context}"]
= Enable autoscaling during cluster creation by using the interactive mode with the ROSA CLI

You can use the {rosa-cli-first} in interactive mode of your terminal, if available, to set cluster-wide autoscaling behavior during cluster creation.

Interactive mode provides more information about available configurable parameters. Interactive mode also does basic checks and preflight validations, meaning that if a provided value is invalid, the terminal outputs a prompt for a valid input.

.Procedure

- During cluster creation, use the `--enable-autoscaling` and `--interactive` parameters to enable cluster autoscaling:
+
.Example
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> --enable-autoscaling --interactive
----

When the following prompt appears, enter *y* to go through all available autoscaling options.

.Example interactive prompt
[source,terminal]
----
? Configure cluster-autoscaler (optional): [? for help] (y/N) y <enter>
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-cli-interactive_after_{context}"]
= Enable autoscaling after cluster creation by using the interactive mode with the ROSA CLI

You can use the interactive mode of your terminal, if available, to set cluster-wide autoscaling behavior after cluster creation.

.Procedure

- After you have created a cluster, type the following command:
+
.Example
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster> --interactive
----
+
You can then set all available autoscaling parameters.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-cli-during_{context}"]
= Enable autoscaling during cluster creation with the ROSA CLI

You can use the {rosa-cli-first} to set cluster-wide autoscaling behavior during cluster creation. You can enable the autoscaler on the entire machine or just a cluster.

.Procedure

- During cluster creation, type `--enable autoscaling` after the cluster name to enable machine autoscaling:

.Example
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> --enable-autoscaling
----

Set at least one parameter to enable cluster autoscaling by running the following command:

.Example
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> --enable-autoscaling <parameter>
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-cluster-cli-autoscale-parameters_{context}"]
= Cluster autoscaling parameters using the ROSA CLI

You can add the following parameters to the cluster creation command to configure autoscaler parameters when using the ROSA CLI (`rosa`).

.Configurable autoscaler parameters available with the ROSA CLI (`rosa`)

[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Example/Instruction

//Classic only
|`--autoscaler-balance-similar-node-groups`
|Identify node groups with the same instance type and label set, and try to balance respective sizes of those node groups.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-skip-nodes-with-local-storage`
|If set, the cluster autoscaler does not delete nodes with pods that have local storage, for example, EmptyDir or HostPath.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-log-verbosity _int_`
|Autoscaler log level. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-log-verbosity 4`

//Both Classic and HCP
|`--autoscaler-max-pod-grace-period _int_`
|Gives pods graceful termination time before scaling down, measured in seconds. Replace _int_ in the command with the number of seconds you want to use.
|`integer`
|`--autoscaler-max-pod-grace-period 0`

//Both Classic and HCP
|`--autoscaler-pod-priority-threshold _int_`
|The priority that a pod must exceed to cause the cluster autoscaler to deploy additional nodes. Replace _int_ in the command with the number you want to use, can be negative.
|`integer`
|`--autoscaler-pod-priority-threshold -10`

//Classic only
|`--autoscaler-gpu-limit _stringArray_`
|Minimum and maximum number of different GPUs in cluster. Cluster autoscaler does not scale the cluster less than or greater than these numbers. The format must be a comma-separated list of "<gpu_type>,<min>,<max>".
|`array`
|`--autoscaler-gpu-limit nvidia.com/gpu,0,10  --autoscaler-gpu-limit amd.com/gpu,1,5`

|`--autoscaler-ignore-daemonsets-utilization`
|If set, the cluster-autoscaler ignores daemon set pods when calculating resource utilization for scaling down.
|`boolean`
|Add it to set to true, omit the option to set to false.

//Both Classic and HCP
|`--autoscaler-max-node-provision-time _string_`
|Maximum time that the cluster autoscaler waits for a node to be provisioned. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-max-node-provision-time 35m`

//Classic only
|`--autoscaler-balancing-ignored-labels _strings_`
|A comma-separated list of label keys that the cluster autoscaler should ignore when comparing node groups for similarity. Replace _strings_ in the command with the relevant labels..
|`string`
|`--autoscaler-balancing-ignored-labels topology.ebs.csi.aws.com/zone,alpha.eksctl.io/instance-id`

//Both Classic and HCP
|`--autoscaler-max-nodes-total _int_`
|Maximum amount of nodes in the cluster, including the autoscaled nodes. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-nodes-total 180`

//Classic only
|`--autoscaler-min-cores _int_`
|Minimum number of cores to deploy in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-min-cores 0`

|`--autoscaler-max-cores _int_`
|Maximum number of cores to deploy in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-cores 100`

|`--autoscaler-min-memory _int_`
|Minimum amount of memory, in GiB, in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-min-memory 0`

|`--autoscaler-max-memory _int_`
|Maximum amount of memory, in GiB, in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-memory 4096`

|`--autoscaler-scale-down-enabled`
|If set, the cluster autoscaler should scale down the cluster.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-scale-down-unneeded-time _string_`
|How long a node should be unneeded before it is eligible for scale down. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-unneeded-time 1h`

|`--autoscaler-scale-down-utilization-threshold _float_`
|Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. Value must be between 0 and 1.
|`float`
|`--autoscaler-scale-down-utilization-threshold 0.5`

|`--autoscaler-scale-down-delay-after-add _string_`
|How long after scale up that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-add 1h`

|`--autoscaler-scale-down-delay-after-delete _string_`
|How long after node deletion that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-delete 1h`

|`--autoscaler-scale-down-delay-after-failure _string_`
|How long after scale down failure that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-failure 1h`

|===

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-enable-cluster-autoscale-cli-after_{context}"]
= Enable autoscaling after cluster creation with the {rosa-cli}

[IMPORTANT]
====
The following procedure is only supported for {rosa-classic-short} clusters. To enable autoscaling after cluster creation for OpenShift Container Platform clusters, see Enabling autoscaling nodes on a cluster.
====

[role="_abstract"]
You can use the {rosa-cli} (`rosa`) to set cluster-wide autoscaling after cluster creation.

.Procedure

* After you have created a cluster, create the autoscaler:
+
.Example
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster>
----
+
** You can also create the autoscaler with specific parameters using the following command:
+
.Example
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster> <parameter>
----

.Next steps
* Enabling autoscaling after cluster creation with the {rosa-cli}

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-edit-cluster-autoscale-cli_{context}"]
= Edit autoscaling after cluster creation with the ROSA CLI

You can edit any specific parameters of the cluster autoscaler after creating the autoscaler.

.Procedure

//ROSA HCP procedure
* To edit the cluster autoscaler, run the following command:
+
.Example
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster>
----
+
** To edit a specific parameter, run the following command:
+
.Example
[source,terminal]
----
$ rosa edit autoscaler -h --cluster=<mycluster> <parameter>=<value>
----

//ROSA Classic procedure
* To edit the cluster autoscaler, run the following command:
+
.Example
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster>
----
+
** To edit a specific parameter, run the following command:
+
.Example
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster> <parameter>
----

[id="rosa-cluster-autoscaler-cli-describe_{context}"]
= View autoscaler configurations with the ROSA CLI

[role="_abstract"]
You can view your cluster autoscaler configurations using the `rosa describe autoscaler` command.

.Procedure
* To view cluster autoscaler configurations, run the following command:
+
.Example
[source,terminal]
----
$ rosa describe autoscaler -h --cluster=<mycluster>
----

----
$ rosa describe autoscaler --cluster=<mycluster>
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

[id="rosa-delete-cluster-autoscale-cli_{context}"]
= Delete autoscaling using the ROSA CLI

You can delete the cluster autoscaler if you no longer want to use it.

.Procedure

* To delete the cluster autoscaler, run the following command:
+
.Example
[source,terminal]
----
$ rosa delete autoscaler --cluster=<mycluster>
----
