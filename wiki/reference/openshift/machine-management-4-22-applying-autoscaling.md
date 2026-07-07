---
title: "Applying autoscaling to an {product-title} cluster"
type: reference
domain: openshift
slug: machine-management-4-22-applying-autoscaling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/applying-autoscaling
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Applying autoscaling to an {product-title} cluster

[id="applying-autoscaling"]
= Applying autoscaling to an OpenShift Container Platform cluster

[role="_abstract"]
Apply autoscaling to an OpenShift Container Platform cluster to automatically adjust the size of the cluster to meet deployment needs. You can deploy a cluster autoscaler and then deploy machine autoscalers for each machine type in your cluster. After you configure the cluster autoscaler, you must configure at least one machine autoscaler.

[IMPORTANT]
====
You can configure the cluster autoscaler only in clusters where the Machine API Operator is operational.
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

//Cluster autoscaler resource definition
// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="cluster-autoscaler-cr_{context}"]
= Cluster autoscaler resource definition

[role="_abstract"]
This `ClusterAutoscaler` resource definition shows the parameters and sample values for the cluster autoscaler.

[NOTE]
====
When you change the configuration of an existing cluster autoscaler, it restarts.
====

[source,yaml]
----
apiVersion: "autoscaling.openshift.io/v1"
kind: "ClusterAutoscaler"
metadata:
  name: "default"
spec:
  podPriorityThreshold: -10
  resourceLimits:
    maxNodesTotal: 24
    cores:
      min: 8
      max: 128
    memory:
      min: 4
      max: 256
    gpus:
    - type: <gpu_type>
      min: 0
      max: 16
  logVerbosity: 4
  scaleDown:
    cordonNodeBeforeTerminating: Enabled
    enabled: true
    delayAfterAdd: 10m
    delayAfterDelete: 5m
    delayAfterFailure: 30s
    unneededTime: 5m
    utilizationThreshold: "0.4"
  scaleUp:
    newPodScaleUpDelay: "10s"
  expanders: ["Random"]
----

.Cluster autoscaler parameters
[cols="1,3",options="header"]
|===
|Parameter |Description

|`podPriorityThreshold`
|Specify the priority that a pod must exceed to cause the cluster autoscaler to deploy additional nodes. Enter a 32-bit integer value. The `podPriorityThreshold` value is compared to the value of the `PriorityClass` that you assign to each pod.

|`maxNodesTotal`
|Specify the maximum number of nodes to deploy. This value is the total number of machines that are deployed in your cluster, not just the ones that the autoscaler controls. Ensure that this value is large enough to account for all of your control plane and compute machines and the total number of replicas that you specify in your `MachineAutoscaler` resources.

|`cores.min`
|Specify the minimum number of cores to deploy in the cluster.

|`cores.max`
|Specify the maximum number of cores to deploy in the cluster.

|`memory.min`
|Specify the minimum amount of memory, in GiB, in the cluster.

|`memory.max`
|Specify the maximum amount of memory, in GiB, in the cluster.

|`gpus.type`
|Optional: To configure the cluster autoscaler to deploy GPU-enabled nodes, specify a `type` value.
This value must match the value of the `spec.template.spec.metadata.labels[cluster-api/accelerator]` label in the machine set that manages the GPU-enabled nodes of that type.
For example, this value might be `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.
For more information, see "Labeling GPU machine sets for the cluster autoscaler".

|`gpus.min`
|Specify the minimum number of GPUs of the specified type to deploy in the cluster.

|`gpus.max`
|Specify the maximum number of GPUs of the specified type to deploy in the cluster.

|`logVerbosity`
a|Specify the logging verbosity level between `0` and `10`. The following log level thresholds are provided for guidance:

* `1`: (Default) Basic information about changes.
* `4`: Debug-level verbosity for troubleshooting typical issues.
* `9`: Extensive, protocol-level debugging information.

If you do not specify a value, the default value of `1` is used.

|`scaleDown`
|In this section, you can specify the period to wait for each action by using any valid ParseDuration interval, including `ns`, `us`, `ms`, `s`, `m`, and `h`.

|`scaleDown.cordonNodeBeforeTerminating`
a|Optional: Specify whether the cluster autoscaler should cordon a node before removing that node by using one of the following values:

* `Enabled`: The cluster autoscaler cordons the node before draining any pods and removing that node.
* `Disabled`: The cluster autoscaler does not cordon the node before draining any pods and removing that node. This is the default.

|`scaleDown.enabled`
|Specify whether the cluster autoscaler can remove unnecessary nodes.

|`scaleDown.delayAfterAdd`
|Optional: Specify the period to wait before deleting a node after a node has recently been _added_. If you do not specify a value, the default value of `10m` is used.

|`scaleDown.delayAfterDelete`
|Optional: Specify the period to wait before deleting a node after a node has recently been _deleted_. If you do not specify a value, the default value of `0s` is used.

|`scaleDown.delayAfterFailure`
|Optional: Specify the period to wait before deleting a node after a scale down failure occurred. If you do not specify a value, the default value of `3m` is used.

|`scaleDown.unneededTime`
|Optional: Specify a period of time before an unnecessary node is eligible for deletion. If you do not specify a value, the default value of `10m` is used.

|`scaleDown.utilizationThreshold`
a|Optional:  Specify the _node utilization level_. Nodes below this utilization level are eligible for deletion.

The node utilization level is the sum of the requested resources divided by the allocated resources for the node, and must be a value greater than `"0"` but less than `"1"`. If you do not specify a value, the cluster autoscaler uses a default value of `"0.5"`, which corresponds to 50% utilization. You must express this value as a string.

|`scaleUp`
|In this section, you can specify the period to wait before recognizing newly pending pods by using any valid ParseDuration interval, including `ns`, `us`, `ms`, `s`, `m`, and `h`.

|`scaleUp.newPodScaleUpDelay`
|Optional: Specify the period to ignore a new unschedulable pod before adding a new node. If you do not specify a value, the default value of `0s` is used.

|`expanders`
a|Optional: Specify any expanders that you want the cluster autoscaler to use.
The following values are valid:

* `LeastWaste`: Selects the machine set that minimizes the idle CPU after scaling.
If multiple machine sets would yield the same amount of idle CPU, the selection minimizes unused memory.
* `Priority`: Selects the machine set with the highest user-assigned priority.
To use this expander, you must create a config map that defines the priority of your machine sets.
For more information, see "Configuring a priority expander for the cluster autoscaler."
* `Random`: (Default) Selects the machine set randomly.

If you do not specify a value, the default value of `Random` is used.

You can specify multiple expanders by using the `[LeastWaste, Priority]` format.
The cluster autoscaler applies each expander according to the specified order.

In the `[LeastWaste, Priority]` example, the cluster autoscaler first evaluates according to the `LeastWaste` criteria.
If more than one machine set satisfies the `LeastWaste` criteria equally well, the cluster autoscaler then evaluates according to the `Priority` criteria.
If more than one machine set satisfies all of the specified expanders equally well, the cluster autoscaler selects one to use at random.

|===

[NOTE]
====
When performing a scaling operation, the cluster autoscaler remains within the ranges set in the `ClusterAutoscaler` resource definition, such as the minimum and maximum number of cores to deploy or the amount of memory in the cluster. However, the cluster autoscaler does not correct the current values in your cluster to be within those ranges.

The minimum and maximum CPUs, memory, and GPU values are determined by calculating those resources on all nodes in the cluster, even if the cluster autoscaler does not manage the nodes. For example, the control plane nodes are considered in the total memory in the cluster, even though the cluster autoscaler does not manage the control plane nodes.
====

//Configuring a priority expander for the cluster autoscaler
// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc

[id="cluster-autoscaler-config-priority-expander_{context}"]
= Configuring a priority expander for the cluster autoscaler

[role="_abstract"]
Configure a priority expander to control which machine set expands when the cluster autoscaler increases the size of the cluster.
You can create a priority expander config map by listing priority values and regular expressions that define machine sets.

.Prerequisites

* You have deployed an OpenShift Container Platform cluster that uses the Machine API.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the {oc-first}.

.Procedure

. List the compute machine sets on your cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io
----
+
.Example output
[source,terminal]
----
NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
archive-agl030519-vplxk-worker-us-east-1c   1         1         1       1           25m
fast-01-agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
fast-02-agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
fast-03-agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
fast-04-agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
prod-01-agl030519-vplxk-worker-us-east-1a   1         1         1       1           33m
prod-02-agl030519-vplxk-worker-us-east-1c   1         1         1       1           33m
----

. Using regular expressions, construct one or more patterns that match the name of any compute machine set that you want to set a priority level for.
+
For example, use the regular expression pattern `\*fast*` to match any compute machine set that includes the string `fast` in its name.

. Create a `cluster-autoscaler-priority-expander.yml` YAML file that defines a config map similar to the following:
+
--
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-autoscaler-priority-expander
  namespace: openshift-machine-api
data:
  priorities: |-
    10:
      - .*fast.*
      - .*archive.*
    40:
      - .*prod.*
----
Define the priority of your machine sets.
The `priorities` values must be positive integers.
The cluster autoscaler uses higher-value priorities before lower-value priorities.
For each priority level, specify the regular expressions that correspond to the machine sets you want to use.
--

. Create the config map by running the following command:
+
[source,terminal]
----
$ oc create configmap cluster-autoscaler-priority-expander \
  --from-file=<location_of_config_map_file>/cluster-autoscaler-priority-expander.yml
----

.Verification

* Review the config map by running the following command:
+
[source,terminal]
----
$ oc get configmaps cluster-autoscaler-priority-expander -o yaml
----

.Next steps

* To use the priority expander, ensure that the `ClusterAutoscaler` resource definition is configured to use the `expanders: ["Priority"]` parameter.

//Labeling GPU machine sets for the cluster autoscaler
// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-bare-metal.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-ibm-cloud.adoc
// * machine_management/creating_machinesets/creating-machineset-ibm-power-vs.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc

[id="machineset-label-gpu-autoscaler_{context}"]
= Labeling GPU machine sets for the cluster autoscaler

[role="_abstract"]
Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

.Prerequisites
* Your cluster uses a cluster autoscaler.

.Procedure

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:
+
--
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: machine-set-name
spec:
  template:
    spec:
      metadata:
        labels:
          cluster-api/accelerator: <accelerator_name>
----

where:

`<accelerator_name>`:: Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.
+
[NOTE]
====
You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR.
For more information, see "Cluster autoscaler resource definition".
====
--

// Be sure to set the :FeatureName: and :FeatureResourceName: values in each assembly on the lines before
// the include statement for this module. For example, add the following lines to the assembly:
// :FeatureName: cluster autoscaler
// :FeatureResourceName: ClusterAutoscaler
//
// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="{FeatureResourceName}-deploying_{context}"]
= Deploying a {FeatureName}

[role="_abstract"]
To deploy a {FeatureName}, you create an instance of the `{FeatureResourceName}` resource.

.Procedure

. Create a YAML file for a `{FeatureResourceName}` resource that contains the custom resource definition.

. Create the custom resource in the cluster by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----
where:

<filename>:: Specifies the name of the YAML file you created.

// Undefine attributes, so that any mistakes are easily spotted

// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="machine-autoscaler-about_{context}"]
= About the machine autoscaler

[role="_abstract"]
The machine autoscaler adjusts the number of Machines in the compute machine sets that you deploy in an OpenShift Container Platform cluster. You can scale both the default `worker` compute machine set and any other compute machine sets that you create. The machine autoscaler makes more Machines when the cluster runs out of resources to support more deployments. Any changes to the values in `MachineAutoscaler` resources, such as the minimum or maximum number of instances, are immediately applied to the compute machine set they target.

[IMPORTANT]
====
You must deploy a machine autoscaler for the cluster autoscaler to scale your machines. The cluster autoscaler uses the annotations on compute machine sets that the machine autoscaler sets to determine the resources that it can scale. If you define a cluster autoscaler without also defining machine autoscalers, the cluster autoscaler will never scale your cluster.
====

// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc

[id="configuring-machineautoscaler_{context}"]
= Configuring machine autoscalers

[role="_abstract"]
After you deploy the cluster autoscaler, deploy `MachineAutoscaler` resources that reference the compute machine sets that are used to scale the cluster.

[IMPORTANT]
====
You must deploy at least one `MachineAutoscaler` resource after you deploy the `ClusterAutoscaler` resource.
====

[NOTE]
====
You must configure separate resources for each compute machine set. Remember that compute machine sets are different in each region, so consider whether you want to enable machine scaling in multiple regions. The compute machine set that you scale must have at least one machine in it.
====

// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="machine-autoscaler-cr_{context}"]
= Machine autoscaler resource definition

[role="_abstract"]
This `MachineAutoscaler` resource definition shows the parameters and sample values for the machine autoscaler.

[source,yaml]
----
apiVersion: "autoscaling.openshift.io/v1beta1"
kind: "MachineAutoscaler"
metadata:
  name: "worker-us-east-1a"
  namespace: "openshift-machine-api"
spec:
  minReplicas: 1
  maxReplicas: 12
  scaleTargetRef:
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    name: worker-us-east-1a
----
where:

<name>:: Specify the machine autoscaler name. To make it easier to identify which compute machine set this machine autoscaler scales, specify or include the name of the compute machine set to scale. The compute machine set name takes the following form: `<clusterid>-<machineset>-<region>`.

<minReplicas>:: Specify the minimum number machines of the specified type that must remain in the specified zone after the cluster autoscaler initiates cluster scaling. If running in AWS, {gcp-short}, Azure, {rh-openstack}, or vSphere, this value can be set to `0`. For other providers, do not set this value to `0`.
+
You can save on costs by setting this value to `0` for use cases such as running expensive or limited-usage hardware that is used for specialized workloads, or by scaling a compute machine set with extra large machines. The cluster autoscaler scales the compute machine set down to zero if the machines are not in use.
+
[IMPORTANT]
====
Do not set the `spec.minReplicas` value to `0` for the three compute machine sets that are created during the OpenShift Container Platform installation process for an installer provisioned infrastructure.
====

<maxReplicas>:: Specify the maximum number machines of the specified type that the cluster autoscaler can deploy in the specified zone after it initiates cluster scaling. Ensure that the `maxNodesTotal` value in the `ClusterAutoscaler` resource definition is large enough to allow the machine autoscaler to deploy this number of machines.

<scaleTargetRef>:: In this section, provide values that describe the existing compute machine set to scale.

<kind>:: The `kind` parameter value is always `MachineSet`.

<name>:: The `name` value must match the name of an existing compute machine set, as shown in the `metadata.name` parameter value.

// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc

[id="deleting-machine-autoscaler_{context}"]
= Disabling a machine autoscaler

[role="_abstract"]
To disable a machine autoscaler, you delete the corresponding `MachineAutoscaler` custom resource (CR).

[NOTE]
====
Disabling a machine autoscaler does not disable the cluster autoscaler. To disable the cluster autoscaler, follow the instructions in "Disabling the cluster autoscaler".
====

.Procedure

. List the `MachineAutoscaler` CRs for the cluster by running the following command:
+
[source,terminal]
----
$ oc get MachineAutoscaler -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                 REF KIND     REF NAME             MIN   MAX   AGE
compute-us-east-1a   MachineSet   compute-us-east-1a   1     12    39m
compute-us-west-1a   MachineSet   compute-us-west-1a   2     4     37m
----

. Optional: Create a YAML file backup of the `MachineAutoscaler` CR by running the following command:
+
[source,terminal]
----
$ oc get MachineAutoscaler/<machine_autoscaler_name> \
  -n openshift-machine-api \
  -o yaml> <machine_autoscaler_name_backup>.yaml
----
where:

<machine_autoscaler_name_backup>:: Specifies the file name in which to store the backup.

. Delete the `MachineAutoscaler` CR by running the following command:
+
[source,terminal]
----
$ oc delete MachineAutoscaler/<machine_autoscaler_name> -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
machineautoscaler.autoscaling.openshift.io "compute-us-east-1a" deleted
----

.Verification

* To verify that the machine autoscaler is disabled, run the following command:
+
[source,terminal]
----
$ oc get MachineAutoscaler -n openshift-machine-api
----
+
The disabled machine autoscaler does not appear in the list of machine autoscalers.

.Next steps

* If you need to re-enable the machine autoscaler, use the `<machine_autoscaler_name_backup>.yaml` backup file and follow the instructions in "Deploying a machine autoscaler".

// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc

[id="deleting-cluster-autoscaler_{context}"]
= Disabling the cluster autoscaler

[role="_abstract"]
To disable the cluster autoscaler, you delete the corresponding `ClusterAutoscaler` resource.

[NOTE]
====
Disabling the cluster autoscaler disables autoscaling on the cluster, even if the cluster has existing machine autoscalers.
====

.Procedure

. List the `ClusterAutoscaler` resource for the cluster by running the following command:
+
[source,terminal]
----
$ oc get ClusterAutoscaler
----
+
.Example output
[source,terminal]
----
NAME      AGE
default   42m
----

. Optional: Create a YAML file backup of the `ClusterAutoscaler` CR by running the following command:
+
[source,terminal]
----
$ oc get ClusterAutoscaler/default \
  -o yaml> <cluster_autoscaler_backup_name>.yaml
----
where:

<cluster_autoscaler_backup_name>:: Specifies the file name in which to store the backup.

. Delete the `ClusterAutoscaler` CR by running the following command:
+
[source,terminal]
----
$ oc delete ClusterAutoscaler/default
----
+
.Example output
[source,terminal]
----
clusterautoscaler.autoscaling.openshift.io "default" deleted
----

.Verification

* To verify that the cluster autoscaler is disabled, run the following command:
+
[source,terminal]
----
$ oc get ClusterAutoscaler
----
+
.Expected output
[source,terminal]
----
No resources found
----

.Next steps

* Disabling the cluster autoscaler by deleting the `ClusterAutoscaler` CR prevents the cluster from autoscaling but does not delete any existing machine autoscalers on the cluster. To clean up unneeded machine autoscalers, see "Disabling a machine autoscaler".

* If you need to re-enable the cluster autoscaler, use the `<cluster_autoscaler_name_backup>.yaml` backup file and follow the instructions in "Deploying a cluster autoscaler".

[role="_additional-resources"]
== Additional resources

* Including pod priority in pod scheduling decisions in OpenShift Container Platform
