---
title: "Cluster autoscaling for {product-title}"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-cluster-autoscaling-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-cluster-autoscaling-hcp
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Cluster autoscaling for {product-title}

[id="rosa-cluster-autoscaling-hcp"]
= Cluster autoscaling for OpenShift Container Platform

[role="_abstract"]
Applying autoscaling to OpenShift Container Platform clusters involves configuring one or more machine pools with autoscaling. You can use the Cluster Autoscaler to further configure cluster-wide autoscaling that is applicable to all of the machine pools that are autoscaling.

[id="rosa-cluster-autoscaler-about_{context}"]
= About the cluster autoscaler

[role="_abstract"]
The cluster autoscaler adjusts the size of a OpenShift Container Platform cluster to meet its current deployment needs. It uses declarative, Kubernetes-style arguments to provide infrastructure management that does not rely on objects of a specific cloud provider. The cluster autoscaler has a cluster scope, and is not associated with a particular namespace. In OpenShift Container Platform, the Cluster Autoscaler is fully managed, which means it is hosted along with the control plane.

The cluster autoscaler increases the size of the cluster when there are pods that fail to schedule on any of the current worker nodes due to insufficient resources or when another node is necessary to meet deployment needs. The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

The cluster autoscaler computes the total memory, CPU, and GPU only on the nodes that belong to autoscaling machine pools. All of the machine pool nodes that are not autoscaling are excluded from this aggregation. For example, if you set the `maxNodesTotal` to `50` on a OpenShift Container Platform cluster with three machine pools in which a single machine pool is not autoscaling, the cluster autoscaler restricts the total nodes to `50` in only those two machine pools that are autoscaling. The single manually scaling machine pool can have additional nodes, making the overall cluster nodes total more than `50`.

[id="rosa-cluster-autoscaler-scale-down_{context}"]
= Automatic node removal

[role="_abstract"]
Every 10 seconds, the cluster autoscaler checks which nodes are unnecessary in the cluster and removes them.

The cluster autoscaler considers a node for removal if the following conditions apply:

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

[id="rosa-cluster-autoscaler-limitations_{context}"]
= Limitations

[role="_abstract"]
If you configure the cluster autoscaler, additional usage restrictions apply.

See the following restrictions:

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

[id="rosa-cluster-autoscaler-interaction_{context}"]
= Interaction with other scheduling features

[role="_abstract"]
The horizontal pod autoscaler (HPA) and the cluster autoscaler modify cluster resources in different ways. The HPA changes the deployment's or replica set's number of replicas based on the current CPU load. If the load increases, the HPA creates new replicas, regardless of the amount of resources available to the cluster. If there are not enough resources, the cluster autoscaler adds resources so that the HPA-created pods can run. If the load decreases, the HPA stops some replicas. If this action causes some nodes to be underutilized or completely empty, the cluster autoscaler deletes the unnecessary nodes.

The cluster autoscaler takes pod priorities into account. The Pod Priority and Preemption feature enables scheduling pods based on priorities if the cluster does not have enough resources, but the cluster autoscaler ensures that the cluster has resources to run all pods. To honor the intention of both features, the cluster autoscaler includes a priority cutoff function. You can use this cutoff to schedule "best-effort" pods, which do not cause the cluster autoscaler to increase resources but instead run only when spare resources are available.

Pods with priority lower than the cutoff value do not cause the cluster to scale up or prevent the cluster from scaling down. No new nodes are added to run the pods, and nodes running these pods might be deleted to free resources.

[id="rosa-cluster-cli-autoscale-parameters_{context}"]
= Cluster autoscaling parameters using the ROSA CLI

[role="_abstract"]
You can add the following parameters to the cluster creation command to configure autoscaler parameters when using the {rosa-cli-first}.

.Configurable autoscaler parameters available with the ROSA CLI

[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Example/Instruction

|`--autoscaler-max-pod-grace-period _int_`
|Gives pods graceful termination time before scaling down, measured in seconds. Replace _int_ in the command with the number of seconds you want to use.
|`integer`
|`--autoscaler-max-pod-grace-period 0`

|`--autoscaler-pod-priority-threshold _int_`
|The priority that a pod must exceed to cause the cluster autoscaler to deploy additional nodes. Replace _int_ in the command with the number you want to use, can be negative.
|`integer`
|`--autoscaler-pod-priority-threshold -10`

|`--autoscaler-max-node-provision-time _string_`
|Maximum time that the cluster autoscaler waits for a node to be provisioned. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-max-node-provision-time 35m`

|`--autoscaler-max-nodes-total _int_`
|Maximum amount of nodes in the cluster, including the autoscaled nodes. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-nodes-total 180`

|===

[id="rosa-edit-cluster-autoscale-cli_{context}"]
= Editing autoscaling after cluster creation with the ROSA CLI

[role="_abstract"]
You can edit any specific parameters of the cluster autoscaler after creating the autoscaler when using the {rosa-cli-first}.

.Procedure
* To edit the cluster autoscaler, run the following command:
+
.Example
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster>
----
+
* To edit a specific parameter, run the following command:
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
