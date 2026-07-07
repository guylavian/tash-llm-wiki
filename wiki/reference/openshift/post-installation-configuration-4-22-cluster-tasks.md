---
title: "Postinstallation cluster tasks"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-cluster-tasks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/cluster-tasks
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Postinstallation cluster tasks

[id="post-install-cluster-tasks"]
= Postinstallation cluster tasks

After installing OpenShift Container Platform, you can further expand and customize your cluster to your requirements.

[id="available_cluster_customizations"]
== Available cluster customizations

You complete most of the cluster configuration and customization after you deploy your OpenShift Container Platform cluster. A number of _configuration resources_ are available.

[NOTE]
====
If you install your cluster on {ibm-z-name}, not all features and functions are available.
====

You modify the configuration resources to configure the major features of the cluster, such as the image registry, networking configuration, image build behavior, and the identity provider.

For current documentation of the settings that you control by using these resources, use the `oc explain` command, for example `oc explain builds --api-version=config.openshift.io/v1`

[id="configuration-resources_{context}"]
=== Cluster configuration resources

All cluster configuration resources are globally scoped (not namespaced) and named `cluster`.
Config changes should not require coordinated changes between config resources, if you find
yourself struggling to update these docs to explain coordinated changes, please reach out
to @api-approvers (github) or #forum-api-review (slack).

[cols="2a,8a",options="header"]
|===
|Resource name
|Description

|`apiserver.config.openshift.io`
|Provides API server configuration such as certificates and certificate authorities.

|`authentication.config.openshift.io`
|Controls the identity provider and authentication configuration for the cluster.

|`build.config.openshift.io`
|Controls default and enforced configuration for all builds on the cluster.

|`console.config.openshift.io`
|Configures the behavior of the web console interface, including the logout behavior.

|`featuregate.config.openshift.io`
|Enables FeatureGates
so that you can use Tech Preview features.

|`image.config.openshift.io`
|Configures how specific image registries should be treated (allowed, disallowed, insecure, CA details).

|`ingress.config.openshift.io`
|Configuration details related to routing such as the default domain for routes.

|`oauth.config.openshift.io`
|Configures identity providers and other behavior related to internal OAuth server flows.

|`project.config.openshift.io`
|Configures how projects are created including the project template.

|`proxy.config.openshift.io`
|Defines proxies to be used by components needing external network access.  Note: not all components currently consume this value.

|`scheduler.config.openshift.io`
|Configures scheduler behavior such as profiles and default node selectors.

|===

[id="operator-configuration-resources_{context}"]
=== Operator configuration resources

These configuration resources are cluster-scoped instances, named `cluster`, which control the behavior of a specific component as
owned by a particular Operator.

[cols="2a,8a",options="header"]
|===
|Resource name
|Description

|`consoles.operator.openshift.io`
|Controls console appearance such as branding customizations

|`config.imageregistry.operator.openshift.io`
|Configures {product-registry} settings such as public routing, log levels, proxy settings, resource constraints, replica counts, and storage type.

|`config.samples.operator.openshift.io`
|Configures the
Samples Operator
to control which example image streams and templates are installed on the cluster.

|===

[id="additional-configuration-resources_{context}"]
=== Additional configuration resources

These configuration resources represent a single instance of a particular component. In some cases, you can request multiple
instances by creating multiple instances of the resource. In other cases, the Operator can use only a specific
resource instance name in a specific namespace. Reference the component-specific
documentation for details on how and when you can create additional resource instances.

[cols="2a,2a,2a,8a",options="header"]
|===
|Resource name
|Instance name
|Namespace
|Description

|`alertmanager.monitoring.coreos.com`
|`main`
|`openshift-monitoring`
|Controls the Alertmanager deployment parameters.

|`ingresscontroller.operator.openshift.io`
|`default`
|`openshift-ingress-operator`
|Configures Ingress Operator behavior such as domain, number of replicas, certificates, and controller placement.

|===

[id="informational-resources_{context}"]
=== Informational Resources

You use these resources to retrieve information about the cluster. Some configurations might require you to edit these resources directly.

[cols="2a,2a,8a",options="header"]
|===
|Resource name|Instance name|Description

|`clusterversion.config.openshift.io`
|`version`
|In OpenShift Container Platform , you must not customize the `ClusterVersion`
resource for production clusters. Instead, follow the process to
update a cluster.

|`dns.config.openshift.io`
|`cluster`
|You cannot modify the DNS settings for your cluster. You can
check the DNS Operator status.

|`infrastructure.config.openshift.io`
|`cluster`
|Configuration details allowing the cluster to interact with its cloud provider.

|`network.config.openshift.io`
|`cluster`
|You cannot modify your cluster networking after installation. To customize your network, follow the process to
customize networking during installation.

|===

[id="adding-worker-nodes_{context}"]
== Adding worker nodes

After you deploy your OpenShift Container Platform cluster, you can add worker nodes to scale cluster resources. There are different ways you can add worker nodes depending on the installation method and the environment of your cluster.

[id="adding-nodes-iso_{context}"]
=== Adding worker nodes to an on-premise cluster

For on-premise clusters, you can add worker nodes by using the OpenShift Container Platform CLI (`oc`) to generate an ISO image, which can then be used to boot one or more nodes in your target cluster.
This process can be used regardless of how you installed your cluster.

You can add one or more nodes at a time while customizing each node with more complex configurations, such as static network configuration, or you can specify only the MAC address of each node.
Any configurations that are not specified during ISO generation are retrieved from the target cluster and applied to the new nodes.

Preflight validation checks are also performed when booting the ISO image to inform you of failure-causing issues before you attempt to boot each node.

Adding worker nodes to an on-premise cluster

=== Adding worker nodes to installer-provisioned infrastructure clusters

For installer-provisioned infrastructure clusters, you can manually or automatically scale the `MachineSet` object to match the number of available bare-metal hosts.

To add a bare-metal host, you must configure all network prerequisites, configure an associated `baremetalhost` object, then provision the worker node to the cluster. You can add a bare-metal host manually or by using the web console.

* Adding worker nodes using the web console

* Adding worker nodes using YAML in the web console

* Manually adding a worker node to an installer-provisioned infrastructure cluster

=== Adding worker nodes to user-provisioned infrastructure clusters

For user-provisioned infrastructure clusters, you can add worker nodes by using a {op-system-base} or {op-system} ISO image and connecting it to your cluster using cluster Ignition config files. For RHEL worker nodes, the following example uses Ansible playbooks to add worker nodes to the cluster. For RHCOS worker nodes, the following example uses an ISO image and network booting to add worker nodes to the cluster.

* Adding RHCOS worker nodes to a user-provisioned infrastructure cluster

=== Adding worker nodes to clusters managed by the Assisted Installer

For clusters managed by the Assisted Installer, you can add worker nodes by using the {cluster-manager-first} console, the Assisted Installer REST API or you can manually add worker nodes using an ISO image and cluster Ignition config files.

* Adding worker nodes using the OpenShift Cluster Manager

* Adding worker nodes using the Assisted Installer REST API

* Manually adding worker nodes to a SNO cluster

=== Adding worker nodes to clusters managed by the multicluster engine for Kubernetes

For clusters managed by the multicluster engine for Kubernetes, you can add worker nodes by using the dedicated multicluster engine console.

* Creating your cluster with the console

[id="post-install-adjust-worker-nodes"]
== Adjust worker nodes
If you incorrectly sized the worker nodes during deployment, adjust them by creating one or more new compute machine sets, scale them up, then scale the original compute machine set down before removing them.

// Module included in the following assemblies:
//
// * post_installation_configuration/node-tasks.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="differences-between-machinesets-and-machineconfigpool_{context}"]
= Understanding the difference between compute machine sets and the machine config pool

`MachineSet` objects describe OpenShift Container Platform nodes with respect to the cloud or machine provider.

The `MachineConfigPool` object allows `MachineConfigController` components to define and provide the status of machines in the context of upgrades.

The `MachineConfigPool` object allows users to configure how upgrades are rolled out to the OpenShift Container Platform nodes in the machine config pool.

The `NodeSelector` object can be replaced with a reference to the `MachineSet` object.

// Module included in the following assemblies:
//
// * machine_management/manually-scaling-machineset.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * windows_containers/scheduling-windows-workloads.adoc

[id="machineset-manually-scaling_{context}"]
= Scaling a compute machine set manually

[role="_abstract"]
To add or remove an instance of a machine in a compute machine set, you can manually scale the compute machine set.

This guidance is relevant to fully automated, installer-provisioned infrastructure installations. Customized, user-provisioned infrastructure installations do not have compute machine sets.

.Prerequisites

* Install an OpenShift Container Platform cluster and the `oc` command line.
* Log in to  `oc` as a user with `cluster-admin` permission.

.Procedure

. View the compute machine sets that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
The compute machine sets are listed in the form of `<clusterid>-worker-<aws-region-az>`.

. View the compute machines that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api
----

. Set the annotation on the compute machine that you want to delete by running the following command:
+
[source,terminal]
----
$ oc annotate machines.machine.openshift.io/<machine_name> -n openshift-machine-api machine.openshift.io/delete-machine="true"
----

. Scale the compute machine set by running one of the following commands:
+
[source,terminal]
----
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
Or:
+
[source,terminal]
----
$ oc edit machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
[TIP]
====
You can alternatively apply the following YAML to scale the compute machine set:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 2
----
====
+
You can scale the compute machine set up or down. It takes several minutes for the new machines to be available.
+
[IMPORTANT]
====
By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.
====

.Verification

* Verify the deletion of the intended machine by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io
----

// Module included in the following assemblies:
//
// * machine_management/manually-scaling-machineset.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="machineset-delete-policy_{context}"]
= The compute machine set deletion policy

[role="_abstract"]
Compute machine sets can be configured to use the `Random`, `Newest`, and `Oldest` deletion options. The default is `Random`, meaning that random machines are chosen and deleted when scaling compute machine sets down.

The deletion policy can be set according to the use case by modifying the particular compute machine set as in the following example:

[source,yaml]
----
spec:
  deletePolicy: <delete_policy>
  replicas: <desired_replica_count>
----

Specific machines can also be prioritized for deletion by adding the annotation `machine.openshift.io/delete-machine=true` to the machine of interest, regardless of the deletion policy.

[IMPORTANT]
====
By default, the OpenShift Container Platform router pods are deployed on workers. Because the router is required to access some cluster resources, including the web console, do not scale the worker compute machine set to `0` unless you first relocate the router pods.
====

[NOTE]
====
Custom compute machine sets can be used for use cases requiring that services run on specific nodes and that those services are ignored by the controller when the worker compute machine sets are scaling down. This prevents service disruption.
====

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-selector.adoc

[id="nodes-scheduler-node-selectors-cluster_{context}"]
= Creating default cluster-wide node selectors

[role="_abstract"]
You can use default cluster-wide node selectors on pods together with labels on nodes to constrain all pods created in a cluster to specific nodes.

With cluster-wide node selectors, when you create a pod in that cluster, OpenShift Container Platform adds the default node selectors to the pod and schedules
the pod on nodes with matching labels.

You configure cluster-wide node selectors by editing the Scheduler Operator custom resource (CR). You add labels to a node, a compute machine set, or a machine config. Adding the label to the compute machine set ensures that if the node or machine goes down, new nodes have the label. Labels added to a node or machine config do not persist if the node or machine goes down.

[NOTE]
====
You can add additional key/value pairs to a pod. But you cannot add a different value for a default key.
====

The following procedure adds a default cluster-wide node selector.

.Procedure

. Edit the Scheduler Operator CR to add the default cluster-wide node selectors:
+
[source,terminal]
----
$ oc edit scheduler cluster
----
+
.Example Scheduler Operator CR with a node selector
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
...
spec:
  defaultNodeSelector: type=user-node,region=east
  mastersSchedulable: false
----
where:
+
--
`spec.defaultNodeSelector`:: Specifies a node selector with the appropriate `<key>:<value>` pairs.
--
+
After making this change, wait for the pods in the `openshift-kube-apiserver` project to redeploy. This can take several minutes. The default cluster-wide node selector does not take effect until the pods redeploy.

. Add labels to a node by using a compute machine set or editing the node directly:

* Use a compute machine set to add labels to nodes managed by the compute machine set when a node is created:

.. Run the following command to add labels to a `MachineSet` object:
+
[source,terminal]
----
$ oc patch MachineSet <name> --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"<key>"="<value>","<key>"="<value>"}}]'  -n openshift-machine-api
----
+
Add a `<key>/<value>` pair for each label.
+
For example:
+
[source,terminal]
----
$ oc patch MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"type":"user-node","region":"east"}}]'  -n openshift-machine-api
----
+
[TIP]
====
You can alternatively apply the following YAML to add labels to a compute machine set:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  template:
    spec:
      metadata:
        labels:
          region: "east"
          type: "user-node"
----
====

.. Verify that the labels are added to the `MachineSet` object by using the `oc edit` command:
+
For example:
+
[source,terminal]
----
$ oc edit MachineSet abc612-msrtw-worker-us-east-1c -n openshift-machine-api
----
+
.Example `MachineSet` object
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
  ...
spec:
  ...
  template:
    metadata:
  ...
    spec:
      metadata:
        labels:
          region: east
          type: user-node
  ...
----

.. Redeploy the nodes associated with that compute machine set by scaling down to `0` and scaling up the nodes:
+
For example:
+
[source,terminal]
----
$ oc scale --replicas=0 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
----
+
[source,terminal]
----
$ oc scale --replicas=1 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
----

.. When the nodes are ready and available, verify that the label is added to the nodes by using the `oc get` command:
+
[source,terminal]
----
$ oc get nodes -l <key>=<value>
----
+
For example:
+
[source,terminal]
----
$ oc get nodes -l type=user-node
----
+
.Example output
[source,terminal]
----
NAME                                       STATUS   ROLES    AGE   VERSION
ci-ln-l8nry52-f76d1-hl7m7-worker-c-vmqzp   Ready    worker   61s   v1.35.4
----

* Add labels directly to a node:

.. Edit the `Node` object for the node:
+
[source,terminal]
----
$ oc label nodes <name> <key>=<value>
----
+
For example, to label a node:
+
[source,terminal]
----
$ oc label nodes ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49 type=user-node region=east
----
+
[TIP]
====
You can alternatively apply the following YAML to add labels to a node:

[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    type: "user-node"
    region: "east"
----
====

.. Verify that the labels are added to the node using the `oc get` command:
+
[source,terminal]
----
$ oc get nodes -l <key>=<value>,<key>=<value>
----
+
For example:
+
[source,terminal]
----
$ oc get nodes -l type=user-node,region=east
----
+
.Example output
[source,terminal]
----
NAME                                       STATUS   ROLES    AGE   VERSION
ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49   Ready    worker   17m   v1.35.4
----

[id="post-worker-latency-profiles"]
== Improving cluster stability in high latency environments using worker latency profiles

// Module included in the following assemblies:
//
// scalability_and_performance/scaling-worker-latency-profiles.adoc

[id="nodes-cluster-worker-latency-profiles-about_{context}"]
= Understanding worker latency profiles

[role="_abstract"]
Review the following information to learn about worker latency profiles, which allow you to control the reaction of the cluster to latency issues without needing to determine the best values by using manual methods.

Worker latency profiles are four different categories of carefully-tuned parameters. The four parameters which implement these values are `node-status-update-frequency`, `node-monitor-grace-period`, `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds`.

[IMPORTANT]
====
Setting these parameters manually is not supported. Incorrect parameter settings adversely affect cluster stability.
====

All worker latency profiles configure the following parameters:

node-status-update-frequency:: Specifies how often the kubelet posts node status to the API server.
node-monitor-grace-period::  Specifies the amount of time in seconds that the Kubernetes Controller Manager waits for an update from a kubelet before marking the node unhealthy and adding the `node.kubernetes.io/not-ready` or `node.kubernetes.io/unreachable` taint to the node.
default-not-ready-toleration-seconds:: Specifies the amount of time in seconds after marking a node unhealthy that the Kube API Server Operator waits before evicting pods from that node.
default-unreachable-toleration-seconds:: Specifies the amount of time in seconds after marking a node unreachable that the Kube API Server Operator waits before evicting pods from that node.

The following Operators monitor the changes to the worker latency profiles and respond accordingly:

* The Machine Config Operator (MCO) updates the `node-status-update-frequency` parameter on the compute nodes.
* The Kubernetes Controller Manager updates the `node-monitor-grace-period` parameter on the control plane nodes.
* The Kubernetes API Server Operator updates the `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` parameters on the control plane nodes.

Although the default configuration works in most cases, OpenShift Container Platform offers two other worker latency profiles for situations where the network is experiencing higher latency than usual. The three worker latency profiles are described in the following sections:
Although the default configuration works in most cases, OpenShift Container Platform offers a second worker latency profile for situations where the network is experiencing higher latency than usual. The two worker latency profiles are described in the following sections:

Default worker latency profile:: With the `Default` profile, each `Kubelet` updates its status every 10 seconds (`node-status-update-frequency`). The `Kube Controller Manager` checks the statuses of `Kubelet` every 5 seconds.
+
The Kubernetes Controller Manager waits 40 seconds (`node-monitor-grace-period`) for a status update from `Kubelet` before considering the `Kubelet` unhealthy. If no status is made available to the Kubernetes Controller Manager, it then marks the node with the `node.kubernetes.io/not-ready` or `node.kubernetes.io/unreachable` taint and evicts the pods on that node.
+
If a pod is on a node that has the `NoExecute` taint, the pod runs according to `tolerationSeconds`. If the node has no taint, it will be evicted in 300 seconds (`default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` settings of the `Kube API Server`).
+
[cols="2,1,2,1"]
|===
| Profile | Component | Parameter | Value

.4+| Default
| kubelet
| `node-status-update-frequency`
| 10s

| Kubelet Controller Manager
| `node-monitor-grace-period`
| 40s

| Kubernetes API Server Operator
| `default-not-ready-toleration-seconds`
| 300s

| Kubernetes API Server Operator
| `default-unreachable-toleration-seconds`
| 300s

|===

Medium worker latency profile:: Use the `MediumUpdateAverageReaction` profile if the network latency is slightly higher than usual.
+
The `MediumUpdateAverageReaction` profile reduces the frequency of kubelet updates to 20 seconds and changes the period that the Kubernetes Controller Manager waits for those updates to 2 minutes. The pod eviction period for a pod on that node is reduced to 60 seconds. If the pod has the `tolerationSeconds` parameter, the eviction waits for the period specified by that parameter.
+
The Kubernetes Controller Manager waits for 2 minutes to consider a node unhealthy. In another minute, the eviction process starts.
+
[cols="2,1,2,1"]
|===
| Profile | Component | Parameter | Value

.4+| MediumUpdateAverageReaction
| kubelet
| `node-status-update-frequency`
| 20s

| Kubelet Controller Manager
| `node-monitor-grace-period`
| 2m

| Kubernetes API Server Operator
| `default-not-ready-toleration-seconds`
| 60s

| Kubernetes API Server Operator
| `default-unreachable-toleration-seconds`
| 60s

|===

Low worker latency profile:: Use the `LowUpdateSlowReaction` profile if the network latency is extremely high.
+
The `LowUpdateSlowReaction` profile reduces the frequency of kubelet updates to 1 minute and changes the period that the Kubernetes Controller Manager waits for those updates to 5 minutes. The pod eviction period for a pod on that node is reduced to 60 seconds. If the pod has the `tolerationSeconds` parameter, the eviction waits for the period specified by that parameter.
+
The Kubernetes Controller Manager waits for 5 minutes to consider a node unhealthy. In another minute, the eviction process starts.
+
[cols="2,1,2,1"]
|===
| Profile | Component | Parameter | Value

.4+| LowUpdateSlowReaction
| kubelet
| `node-status-update-frequency`
| 1m

| Kubelet Controller Manager
| `node-monitor-grace-period`
| 5m

| Kubernetes API Server Operator
| `default-not-ready-toleration-seconds`
| 60s

| Kubernetes API Server Operator
| `default-unreachable-toleration-seconds`
| 60s

|===

[NOTE]
====
The latency profiles do not support custom machine config pools, only the default worker machine config pools.
====

// Module included in the following assemblies:
//
// scalability_and_performance/scaling-worker-latency-profiles.adoc

[id="nodes-cluster-worker-latency-profiles-using_{context}"]
= Using and changing worker latency profiles

[role="_abstract"]
You can change a worker latency profile to deal with network latency at any time by editing the `node.config` object. With this configuration, you can ensure that your cluster runs properly if network latency between the control plane and the compute nodes fluctuates.

You must move one worker latency profile at a time. For example, you cannot move directly from the `Default` profile to the `LowUpdateSlowReaction` worker latency profile. You must move from the `Default` worker latency profile to the `MediumUpdateAverageReaction` profile and then to the `LowUpdateSlowReaction` profile. Similarly, when returning to the `Default` profile, you must move from the low profile to the medium profile first, then to `Default`.

[NOTE]
====
You can also configure worker latency profiles upon installing an OpenShift Container Platform cluster.
====

.Procedure

. Move to the medium worker latency profile:
+
.. Edit the `node.config` object:
+
[source,terminal]
----
$ oc edit nodes.config/cluster
----
+
.. Add `spec.workerLatencyProfile: MediumUpdateAverageReaction`:
+
.Example `node.config` object
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Node
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: "true"
    include.release.openshift.io/self-managed-high-availability: "true"
    include.release.openshift.io/single-node-developer: "true"
    release.openshift.io/create-only: "true"
  creationTimestamp: "2022-07-08T16:02:51Z"
  generation: 1
  name: cluster
  ownerReferences:
  - apiVersion: config.openshift.io/v1
    kind: ClusterVersion
    name: version
    uid: 36282574-bf9f-409e-a6cd-3032939293eb
  resourceVersion: "1865"
  uid: 0c0f7a4c-4307-4187-b591-6155695ac85b
spec:
  workerLatencyProfile: MediumUpdateAverageReaction
# ...
----
where:
+
--
`spec.workerLatencyProfile.MediumUpdateAverageReaction`:: Specifies that the medium worker latency policy should be used.
--
+
Scheduling on each compute node is disabled as the change is being applied.

. Optional: Move to the low worker latency profile:
+
.. Edit the `node.config` object:
+
[source,terminal]
----
$ oc edit nodes.config/cluster
----
+
.. Change the `spec.workerLatencyProfile` value to `LowUpdateSlowReaction`:
+
.Example `node.config` object
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Node
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: "true"
    include.release.openshift.io/self-managed-high-availability: "true"
    include.release.openshift.io/single-node-developer: "true"
    release.openshift.io/create-only: "true"
  creationTimestamp: "2022-07-08T16:02:51Z"
  generation: 1
  name: cluster
  ownerReferences:
  - apiVersion: config.openshift.io/v1
    kind: ClusterVersion
    name: version
    uid: 36282574-bf9f-409e-a6cd-3032939293eb
  resourceVersion: "1865"
  uid: 0c0f7a4c-4307-4187-b591-6155695ac85b
spec:
  workerLatencyProfile: LowUpdateSlowReaction
# ...
----
where:
+
--
`spec.workerLatencyProfile.LowUpdateSlowReaction`:: Specifies that the low worker latency policy should be used.
--
+
Scheduling on each compute node is disabled as the change is being applied.

.Verification

* When all nodes return to the `Ready` condition, you can use the following command to look in the Kubernetes Controller Manager to ensure it was applied:
+
[source,terminal]
----
$ oc get KubeControllerManager -o yaml | grep -i workerlatency -A 5 -B 5
----
+
.Example output
[source,terminal]
----
# ...
    - lastTransitionTime: "2022-07-11T19:47:10Z"
      reason: ProfileUpdated
      status: "False"
      type: WorkerLatencyProfileProgressing
    - lastTransitionTime: "2022-07-11T19:47:10Z"
      message: all static pod revision(s) have updated latency profile
      reason: ProfileUpdated
      status: "True"
      type: WorkerLatencyProfileComplete
    - lastTransitionTime: "2022-07-11T19:20:11Z"
      reason: AsExpected
      status: "False"
      type: WorkerLatencyProfileDegraded
    - lastTransitionTime: "2022-07-11T19:20:36Z"
      status: "False"
# ...
----
where:
+
--
`status.message: all static pod revision(s) have updated latency profile`:: Specifies that the profile is applied and active.
--
+
To change the medium profile to default or change the default to medium, edit the `node.config` object and set the `spec.workerLatencyProfile` parameter to the appropriate value.

[id="post-install-cpms-setup"]
== Managing control plane machines

Control plane machine sets provide management capabilities for control plane machines that are similar to what compute machine sets provide for compute machines. The availability and initial status of control plane machine sets on your cluster depend on your cloud provider and the version of OpenShift Container Platform that you installed. For more information, see Getting started with control plane machine sets.

// Adding a control plane node to your cluster
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-manually-scaling-control-planes.adoc

[id="creating-control-plane-node_{context}"]
= Adding a control plane node to your cluster

[role="_abstract"]
Add a control plane node to recover from a degraded state, perform deep-level debugging, or ensure stability and security of the control plane in complex bare metal scenarios.

.Prerequisites

* You have installed a healthy cluster with at least three control plane nodes.
* You have created a single control plane node that you intend to add to your cluster as a postinstalltion task.

.Procedure

. Retrieve pending Certificate Signing Requests (CSRs) for the new control plane node by entering the following command:
+
[source,terminal]
----
$ oc get csr | grep Pending
----

. Approve all pending CSRs for the control plane node by entering the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
----
+
[IMPORTANT]
====
You must approve the CSRs to complete the installation.
====

. Confirm that the control plane node is in the `Ready` status by entering the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
[NOTE]
====
On installer-provisioned infrastructure, the etcd Operator relies on the Machine API to manage the control plane and ensure etcd quorum. The Machine API then uses `Machine` CRs to represent and manage the underlying control plane nodes.
====

. Create the `BareMetalHost` and `Machine` CRs and link them to the `Node` CR of the control plane node.
+
.. Create the `BareMetalHost` CR with a unique `.metadata.name` value as demonstrated in the following example:
+
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: node-5
  namespace: openshift-machine-api
spec:
  automatedCleaningMode: metadata
  bootMACAddress: 00:00:00:00:00:02
  bootMode: UEFI
  customDeploy:
    method: install_coreos
  externallyProvisioned: true
  online: true
  userData:
    name: master-user-data-managed
    namespace: openshift-machine-api
# ...
----
+
.. Apply the `BareMetalHost` CR by entering the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----
+
where `<filename>` specifies the name of the `BareMetalHost` CR.
+
.. Create the `Machine` CR by using the unique `.metadata.name` value as demonstrated in the following example:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  annotations:
    machine.openshift.io/instance-state: externally provisioned
    metal3.io/BareMetalHost: openshift-machine-api/node-5
  finalizers:
  - machine.machine.openshift.io
  labels:
    machine.openshift.io/cluster-api-cluster: <cluster_name>
    machine.openshift.io/cluster-api-machine-role: master
    machine.openshift.io/cluster-api-machine-type: master
  name: node-5
  namespace: openshift-machine-api
spec:
  metadata: {}
  providerSpec:
    value:
      apiVersion: baremetal.cluster.k8s.io/v1alpha1
      customDeploy:
        method: install_coreos
      hostSelector: {}
      image:
        checksum: ""
        url: ""
      kind: BareMetalMachineProviderSpec
      metadata:
        creationTimestamp: null
      userData:
        name: master-user-data-managed
# ...
----
+
where `<cluster_name>` specifies the name of the specific cluster, for example, `test-day2-1-6qv96`.
+
.. Get the cluster name by running the following command:
+
[source,terminal]
----
$ oc get infrastructure cluster -o=jsonpath='{.status.infrastructureName}{"\n"}'
----
+
.. Apply the `Machine` CR by entering the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----
+
where `<filename>` specifies the name of the `Machine` CR.
+
.. Link `BareMetalHost`, `Machine`, and `Node` objects by running the `link-machine-and-node.sh` script:
+
... Copy the following `link-machine-and-node.sh` script to a local machine:
+
[source,text]
----
#!/bin/bash

# Credit goes to
# https://bugzilla.redhat.com/show_bug.cgi?id=1801238.
# This script will link Machine object
# and Node object. This is needed
# in order to have IP address of
# the Node present in the status of the Machine.

set -e

machine="$1"
node="$2"

if [ -z "$machine" ] || [ -z "$node" ]; then
    echo "Usage: $0 MACHINE NODE"
    exit 1
fi

node_name=$(echo "${node}" | cut -f2 -d':')

oc proxy &
proxy_pid=$!
function kill_proxy {
    kill $proxy_pid
}
trap kill_proxy EXIT SIGINT

HOST_PROXY_API_PATH="http://localhost:8001/apis/metal3.io/v1alpha1/namespaces/openshift-machine-api/baremetalhosts"

function print_nics() {
    local ips
    local eob
    declare -a ips

    readarray -t ips < <(echo "${1}" \
                         | jq '.[] | select(. | .type == "InternalIP") | .address' \
                         | sed 's/"//g')

    eob=','
    for (( i=0; i<${#ips[@]}; i++ )); do
        if [ $((i+1)) -eq ${#ips[@]} ]; then
            eob=""
        fi
        cat <<- EOF
          {
            "ip": "${ips[$i]}",
            "mac": "00:00:00:00:00:00",
            "model": "unknown",
            "speedGbps": 10,
            "vlanId": 0,
            "pxe": true,
            "name": "eth1"
          }${eob}
EOF
    done
}

function wait_for_json() {
    local name
    local url
    local curl_opts
    local timeout

    local start_time
    local curr_time
    local time_diff

    name="$1"
    url="$2"
    timeout="$3"
    shift 3
    curl_opts="$@"
    echo -n "Waiting for $name to respond"
    start_time=$(date +%s)
    until curl -g -X GET "$url" "${curl_opts[@]}" 2> /dev/null | jq '.' 2> /dev/null > /dev/null; do
        echo -n "."
        curr_time=$(date +%s)
        time_diff=$((curr_time - start_time))
        if [[ $time_diff -gt $timeout ]]; then
            printf '\nTimed out waiting for %s' "${name}"
            return 1
        fi
        sleep 5
    done
    echo " Success!"
    return 0
}
wait_for_json oc_proxy "${HOST_PROXY_API_PATH}" 10 -H "Accept: application/json" -H "Content-Type: application/json"

addresses=$(oc get node -n openshift-machine-api "${node_name}" -o json | jq -c '.status.addresses')

machine_data=$(oc get machines.machine.openshift.io -n openshift-machine-api -o json "${machine}")
host=$(echo "$machine_data" | jq '.metadata.annotations["metal3.io/BareMetalHost"]' | cut -f2 -d/ | sed 's/"//g')

if [ -z "$host" ]; then
    echo "Machine $machine is not linked to a host yet." 1>&2
    exit 1
fi

# The address structure on the host doesn't match the node, so extract
# the values we want into separate variables so we can build the patch
# we need.
hostname=$(echo "${addresses}" | jq '.[] | select(. | .type == "Hostname") | .address' | sed 's/"//g')

set +e
read -r -d '' host_patch << EOF
{
  "status": {
    "hardware": {
      "hostname": "${hostname}",
      "nics": [
$(print_nics "${addresses}")
      ],
      "systemVendor": {
        "manufacturer": "Red Hat",
        "productName": "product name",
        "serialNumber": ""
      },
      "firmware": {
        "bios": {
          "date": "04/01/2014",
          "vendor": "SeaBIOS",
          "version": "1.11.0-2.el7"
        }
      },
      "ramMebibytes": 0,
      "storage": [],
      "cpu": {
        "arch": "x86_64",
        "model": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "clockMegahertz": 2199.998,
        "count": 4,
        "flags": []
      }
    }
  }
}
EOF
set -e

echo "PATCHING HOST"
echo "${host_patch}" | jq .

curl -s \
     -X PATCH \
     "${HOST_PROXY_API_PATH}/${host}/status" \
     -H "Content-type: application/merge-patch+json" \
     -d "${host_patch}"

oc get baremetalhost -n openshift-machine-api -o yaml "${host}"
----
+
... Make the script executable by entering the following command:
+
[source,terminal]
----
$ chmod +x link-machine-and-node.sh
----
+
... Run the script by entering the following command:
+
[source,terminal]
----
$ bash link-machine-and-node.sh node-5 node-5
----
+
[NOTE]
====
The first `node-5` instance represents the machine, and the second instance represents the node.
====

.Verification

. Confirm members of etcd by executing into one of the pre-existing control plane nodes:
+
.. Open a remote shell session to the control plane node by entering the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-node-0
----
+
.. List etcd members:
+
[source,terminal]
----
# etcdctl member list -w table
----

. Check the etcd Operator configuration process until completion by entering the following command. Expected output shows `False` under the `PROGRESSING` column.
+
[source,terminal]
----
$ oc get clusteroperator etcd
----

. Confirm etcd health by running the following commands:
+
.. Open a remote shell session to the control plane node:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-node-0
----
+
.. Check endpoint health. Expected output shows `is healthy` for the endpoint.
+
[source,terminal]
----
# etcdctl endpoint health
----

. Verify that all nodes are ready by entering the following command. The expected output shows the `Ready` status beside each node entry.
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the cluster Operators are all available by entering the following command. Expected output lists each Operator and shows the available status as `True` beside each listed Operator.
+
[source,terminal]
----
$ oc get ClusterOperators
----

. Verify that the cluster version is correct by entering the following command:
+
[source,terminal]
----
$ oc get ClusterVersion
----
+
.Example output
[source,terminal,subs="attributes+"]]
----
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   OpenShift Container Platform.5    True        False         5h57m   Cluster version is OpenShift Container Platform.5
----

[id="post-install-creating-infrastructure-machinesets-production"]
== Creating infrastructure machine sets for production environments

You can create a compute machine set to create machines that host only infrastructure components, such as the default router, the integrated container image registry, and components for cluster metrics and monitoring. These infrastructure machines are not counted toward the total number of subscriptions that are required to run the environment.

For information on infrastructure nodes and which components can run on infrastructure nodes, see Creating infrastructure machine sets.

To create an infrastructure node, you can use a machine set, assign a label to the nodes, or use a machine config pool.

For sample machine sets that you can use with these procedures, see Creating machine sets for different clouds.

Applying a specific node selector to all infrastructure components causes OpenShift Container Platform to schedule those workloads on nodes with that label.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-nutanix.adoc

[id="machineset-creating_{context}"]
= Creating a compute machine set

[role="_abstract"]
To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

[NOTE]
====
Clusters that are installed with user-provisioned infrastructure have a different networking stack than clusters with infrastructure that is provisioned by the installation program. As a result of this difference, automatic load balancer management is unsupported on clusters that have user-provisioned infrastructure. For these clusters, a compute machine set can only create `worker` and `infra` type machines.
====

.Prerequisites

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* Have the necessary permissions to deploy VMs in your vCenter instance and have the required access to the datastore specified.
* If your cluster uses user-provisioned infrastructure, you have satisfied the specific Machine API requirements for that configuration.
* Create an availability set in which to deploy Azure Stack Hub compute machines.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the OpenSSH server v0.0.1.0 installed.

.Procedure

. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.
+
Ensure that you set the `<clusterID>` and `<role>` parameter values.
Ensure that you set the `<availabilitySet>`, `<clusterID>`, and `<role>` parameter values.

. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

.. To list the compute machine sets in your cluster, run the following command:
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----

.. To view values of a specific compute machine set custom resource (CR), run the following command:
+
[source,terminal]
----
$ oc get machineset <machineset_name> \
  -n openshift-machine-api -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      providerSpec:
        ...
----
+
where:

`metadata.labels.machine.openshift.io/cluster-api-cluster`:: Specifies the cluster infrastructure ID.
`metadata.labels.name`:: Specifies a default node label.
+
[NOTE]
====
For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.
====
`spec.template.metadata.spec.providerSpec`:: Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
.. If you are creating a compute machine set for a cluster that has user-provisioned infrastructure, note the following important values:
+
.Example vSphere `providerSpec` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
...
template:
  ...
  spec:
    providerSpec:
      value:
        apiVersion: machine.openshift.io/v1beta1
        credentialsSecret:
          name: vsphere-cloud-credentials
        dataDisks:
        - name: <disk_name>
          provisioningMode: <mode>
          sizeGiB: 10
        diskGiB: 120
        kind: VSphereMachineProviderSpec
        memoryMiB: 16384
        network:
          devices:
            - networkName: "<vm_network_name>"
        numCPUs: 4
        numCoresPerSocket: 4
        snapshot: ""
        template: <vm_template_name>
        userDataSecret:
          name: worker-user-data
        workspace:
          datacenter: <vcenter_data_center_name>
          datastore: <vcenter_datastore_name>
          folder: <vcenter_vm_folder_path>
          resourcepool: <vsphere_resource_pool>
          server: <vcenter_server_address>
----
+
where:

`vsphere-cloud-credentials`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required vCenter credentials.
`<disk_name>`:: Specifies the collection of data disk definitions. For more information, see "Configuring data disks by using machine sets".
`<vm_template_name>`:: Specifies the name of the {op-system} VM template for your cluster that was created during installation.
`worker-user-data`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required Ignition configuration credentials.
`<vcenter_server_address>`:: Specifies the IP address or fully qualified domain name (FQDN) of the vCenter server.

. Create a `MachineSet` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. If you need compute machine sets in other availability zones, repeat this process to create more compute machine sets.

.Verification

* View the list of compute machine sets by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
agl030519-vplxk-edge-us-east-1-nyc-1a      1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d          0         0                             55m
agl030519-vplxk-worker-us-east-1e          0         0                             55m
agl030519-vplxk-worker-us-east-1f          0         0                             55m
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----
+
When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

* Optional: To check nodes that were created by the edge machine, run the following command:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/edge
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES         AGE    VERSION
ip-10-0-207-188.ec2.internal   Ready    edge,worker   172m   v1.25.2+d2e245f
----

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * machine_management/creating-infrastructure-machinesets.adoc
// * nodes/nodes/nodes-nodes-creating-infrastructure-nodes.adoc

[id="creating-an-infra-node_{context}"]
= Creating an infrastructure node

[role="_abstract"]
To reduce subscription costs, you can use labels to configure compute nodes as infrastructure nodes, where you can move infrastructure resources.

After you create the infrastructure nodes, you can move appropriate workloads to those nodes by using taints and tolerations.

You can optionally create a default cluster-wide node selector. The default node selector is applied to pods created in all namespaces and creates an intersection with any existing node selectors on a pod, which additionally constrains the pod's selector.

[IMPORTANT]
====
* See "Creating infrastructure machine sets" for installer-provisioned infrastructure environments or for any cluster where the control plane nodes are managed by the Machine API.

* If the default node selector key conflicts with the key of a pod's label, then the default node selector is not applied.
+
However, do not set a default node selector that might cause a pod to become unschedulable. For example, setting the default node selector to a specific node role, such as `node-role.kubernetes.io/infra=""`, when a pod's label is set to a different node role, such as `node-role.kubernetes.io/master=""`, can cause the pod to become unschedulable. For this reason, use caution when setting the default node selector to specific node roles.
+
You can alternatively use a project node selector to avoid cluster-wide node selector key conflicts.
====

.Procedure

. Add a label to the compute nodes that you want to act as infrastructure nodes by running the following command:
+
[source,terminal]
----
$ oc label node <node-name> node-role.kubernetes.io/infra=""
----

. Check to see if applicable nodes now have the `infra` role by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Optional: Create a default cluster-wide node selector.

.. Edit the `Scheduler` object by running the following command:
+
[source,terminal]
----
$ oc edit scheduler cluster
----

.. Add the `defaultNodeSelector` field with the appropriate node selector by running the following command:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
spec:
  defaultNodeSelector: node-role.kubernetes.io/infra=""
# ...
----
+
This example node selector deploys pods on infrastructure nodes by default.

.. Save the file to apply the changes.

+
You can now move infrastructure resources to the new infrastructure nodes and remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components".

[role="_additional-resources"]
.Additional resources

* For information on how to configure project node selectors to avoid cluster-wide node selector key conflicts, see Project node selectors.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="creating-infra-machines_{context}"]
= Creating a machine config pool for infrastructure machines

[role="_abstract"]
You can create a machine configuration pool for infrastructure machines to apply dedicated configuration to infra machines. You might want to apply dedicated configuration to infra machines because they run distinct workloads from other nodes in the cluster.

[IMPORTANT]
====
Creating a custom machine configuration pool overrides default worker pool configurations if they refer to the same file or unit.
====

.Procedure

. Add a label to the node you want to assign as the infra node by running the following command:
+
[source,terminal]
----
$ oc label node <node_name> node-role.kubernetes.io/infra=
----
+
where:
+
`<node_name>`:: Specifies the name of the node you want to assign as an infra node.

. Create a YAML file that defines the machine config pool, as in the following example:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: infra
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/infra: ""
----
+
* Add the worker role and your custom role in the `spec.machineConfigSelector.matchExpressions[]` field.
* Add the label you added to the node in the `spec.nodeSelector.matchLabels` field.
+
[NOTE]
====
Custom machine config pools inherit machine configs from the worker pool. Custom pools use any machine config targeted for the worker pool, but add the ability to also deploy changes that are targeted at only the custom pool. Because a custom pool inherits resources from the worker pool, any change to the worker pool also affects the custom pool.
====

. After you have the YAML file, you can create the machine config pool by specifying the file you created in the following command:
+
[source,terminal]
----
$ oc create -f <filename>
----

. Check the machine configs to ensure that the infrastructure configuration rendered successfully by running the following command:
+
[source,terminal]
----
$ oc get machineconfig
----
+
.Example output
[source,terminal]
----
NAME                                                        GENERATEDBYCONTROLLER                      IGNITIONVERSION   CREATED
00-master                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
00-worker                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
# ...
rendered-infra-4e48906dca84ee702959c71a53ee80e7             365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             23m
----
+
You should see a new machine config, with the `rendered-infra-*` prefix.

. Optional: To deploy changes to a custom pool, create a machine config that uses the custom pool name as the label, such as `infra`. Note that this is not required and only shown for instructional purposes. In this manner, you can apply any custom configurations specific to only your infra nodes.
+
[NOTE]
====
After you create the new machine config pool, the MCO generates a new rendered config for that pool, and associated nodes of that pool reboot to apply the new configuration.
====

.. Create a YAML file that defines the machine config pool, as in the following example:
+
[source,terminal]
----
$ cat infra.mc.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: 51-infra
  labels:
    machineconfiguration.openshift.io/role: <role>
spec:
  config:
    ignition:
      version: 3.5.0
    storage:
      files:
      - path: /etc/infratest
        mode: 0644
        contents:
          source: data:,infra
----
+
where:
+
`role`:: Specifies the label you added to the node as a `nodeSelector`.

..  Apply the machine config to the infra-labeled nodes by running the following command:
+
[source,terminal]
----
$ oc create -f infra.mc.yaml
----

. Confirm that your new machine config pool is available by running the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
infra    rendered-infra-60e35c2e99f42d976e084fa94da4d0fc    True      False      False      1              1                   1                     0                      4m20s
master   rendered-master-9360fdb895d4c131c7c4bebbae099c90   True      False      False      3              3                   3                     0                      91m
worker   rendered-worker-60e35c2e99f42d976e084fa94da4d0fc   True      False      False      2              2                   2                     0                      91m
----
+
In this example, the role of the node was changes from `worker` to `infra`.

[role="_additional-resources"]
.Additional resources

* See Node configuration management with machine config pools for more information on grouping infra machines in a custom pool.

[id="assigning-machine-set-resources-to-infra-nodes"]
== Assigning machine set resources to infrastructure nodes

After creating an infrastructure machine set, the `worker` and `infra` roles are applied to new infra nodes. Nodes with the `infra` role are not counted toward the total number of subscriptions that are required to run the environment, even when the `worker` role is also applied.

However, when an infra node is assigned the worker role, there is a chance that user workloads can get assigned inadvertently to the infra node. To avoid this, you can apply a taint to the infra node and tolerations for the pods that you want to control.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="binding-infra-node-workloads-using-taints-tolerations_{context}"]
= Binding infrastructure node workloads using taints and tolerations

[role="_abstract"]
To avoid user workloads being inadvertently assigned to an infra node, you can apply a taint to the infra node and tolerations for the pods you want to control. After creating an infrastructure machine set, the `worker` and `infra` roles are applied to new infra nodes.

Nodes with the `infra` role applied are not counted toward the total number of subscriptions that are required to run the environment, even when the `worker` role is also applied.
If you have an infrastructure node that has the `infra` and `worker` roles assigned, you must configure the node so that user workloads are not assigned to it.

[IMPORTANT]
====
It is recommended that you preserve the dual `infra,worker` label that is created for infrastructure nodes and use taints and tolerations to manage nodes that user workloads are scheduled on. If you remove the `worker` label from the node, you must create a custom pool to manage it. A node with a label other than `master` or `worker` is not recognized by the MCO without a custom pool. Maintaining the `worker` label allows the node to be managed by the default worker machine config pool, if no custom pools that select the custom label exists. The `infra` label communicates to the cluster that it does not count toward the total number of subscriptions.
====

.Prerequisites

* Configure additional `MachineSet` objects in your OpenShift Container Platform cluster.

.Procedure

. Add a taint to the infrastructure node to prevent scheduling user workloads on it:

.. Determine if the node has the taint by running the following command:
+
[source,terminal]
----
$ oc describe nodes <node_name>
----
+
.Sample output
[source,text]
----
oc describe node ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
Name:               ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
Roles:              worker
 ...
Taints:             node-role.kubernetes.io/infra=reserved:NoSchedule
 ...
----
+
This example shows that the node has a taint. You can proceed with adding a toleration to your pod in the next step.

.. If you have not configured a taint to prevent scheduling user workloads on it, configure a taint by running the following command:
+
[source,terminal]
----
$ oc adm taint nodes <node_name> <key>=<value>:<effect>
----
+
For example:
+
[source,terminal]
----
$ oc adm taint nodes node1 node-role.kubernetes.io/infra=reserved:NoSchedule
----
+
[TIP]
====
You can alternatively edit the pod specification to add the taint:

[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  name: node1
# ...
spec:
  taints:
    - key: node-role.kubernetes.io/infra
      value: reserved
      effect: NoSchedule
# ...
----
====
+
These examples place a taint on `node1` that has the `node-role.kubernetes.io/infra` key and the `NoSchedule` taint effect. Nodes with the `NoSchedule` effect schedule only pods that tolerate the taint, but allow existing pods to remain scheduled on the node.
If you added a `NoSchedule` taint to the infrastructure node, any pods that are controlled by a daemon set on that node are marked as `misscheduled`. You must either delete the pods or add a toleration to the pods as shown in the Red Hat Knowledgebase solution add toleration on `misscheduled` DNS pods. Note that you cannot add a toleration to a daemon set object that is managed by an operator.
+
[NOTE]
====
If a descheduler is used, pods violating node taints could be evicted from the cluster.
====

. Add tolerations to the pods that you want to schedule on the infrastructure node, such as the router, registry, and monitoring workloads. Referencing the previous examples, add the following tolerations to the `Pod` object specification:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:

# ...
spec:
# ...
  tolerations:
    - key: <node_taint_key>
      value: <node_taint_value>
      effect: <taint_effect>
      operator: Equal
----
where:

`<node_taint_key>`:: Specifies the key that you added to the taint on the node.
`<node_taint_value>`:: Specifies the value of the key-value pair taint that you added to the node.
`<taint_effect>`:: Specifies the effect that you added to the node.
`Equal`:: Specifies that a taint with a key matching `<node_taint_key>` is required to be present on the node.
+
This toleration matches the taint created by the `oc adm taint` command. A pod with this toleration can be scheduled onto the infrastructure node.
+
[NOTE]
====
Moving pods for an Operator installed via OLM to an infrastructure node is not always possible. The capability to move Operator pods depends on the configuration of each Operator.
====

. Schedule the pod to the infrastructure node by using a scheduler. See the documentation for "Controlling pod placement using the scheduler" for details.

. Remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components".

[role="_additional-resources"]
.Additional resources

* See Controlling pod placement using the scheduler for general information on scheduling a pod to a node.

[id="moving-resources-to-infrastructure-machinesets"]
== Moving resources to infrastructure machine sets

Some of the infrastructure resources are deployed in your cluster by default. You can move them to the infrastructure machine sets that you created.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc

[id="infrastructure-moving-router_{context}"]
= Moving the router

[role="_abstract"]
Deploying the router pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the router pod by editing the `IngressController` object in the `openshift-ingress-operator` namespace. By default, the pod is deployed to a worker node.

.Prerequisites

* Configure additional compute machine sets in your OpenShift Container Platform cluster.

.Procedure

. View the `IngressController` custom resource for the router Operator by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller default -n openshift-ingress-operator -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: 2019-04-18T12:35:39Z
  finalizers:
  - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
  generation: 1
  name: default
  namespace: openshift-ingress-operator
  resourceVersion: "11341"
  selfLink: /apis/operator.openshift.io/v1/namespaces/openshift-ingress-operator/ingresscontrollers/default
  uid: 79509e05-61d6-11e9-bc55-02ce4781844a
spec: {}
status:
  availableReplicas: 2
  conditions:
  - lastTransitionTime: 2019-04-18T12:36:15Z
    status: "True"
    type: Available
  domain: apps.<cluster>.example.com
  endpointPublishingStrategy:
    type: LoadBalancerService
  selector: ingresscontroller.operator.openshift.io/deployment-ingresscontroller=default
----

. Edit the `ingresscontroller` resource and change the `nodeSelector` to use the `infra` label by running the following command:
+
[source,terminal]
----
$ oc edit ingresscontroller default -n openshift-ingress-operator
----
+
.Example output
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: "2025-03-26T21:15:43Z"
  finalizers:
  - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
  generation: 1
  name: default
# ...
spec:
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/infra: ""
    tolerations:
    - effect: NoSchedule
      key: node-role.kubernetes.io/infra
      value: reserved
# ...
----
+
Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.

.Verification
* Confirm that the router pod is running on the `infra` node.
.. View the list of router pods and note the node name of the running pod by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ingress -o wide
----
+
.Example output
[source,terminal]
----
NAME                              READY     STATUS        RESTARTS   AGE       IP           NODE                           NOMINATED NODE   READINESS GATES
router-default-86798b4b5d-bdlvd   1/1      Running       0          28s       10.130.2.4   ip-10-0-217-226.ec2.internal   <none>           <none>
router-default-955d875f4-255g8    0/1      Terminating   0          19h       10.129.2.4   ip-10-0-148-172.ec2.internal   <none>           <none>
----
+
In this example, the running pod is on the `ip-10-0-217-226.ec2.internal` node.

.. View the node status of the running pod by running the following command:
+
[source,terminal]
----
$ oc get node <node_name>
----
+
Specify the `<node_name>` that you obtained from the pod list.
+
.Example output
[source,terminal]
----
NAME                          STATUS  ROLES         AGE   VERSION
ip-10-0-217-226.ec2.internal  Ready   infra,worker  17h   v1.35.4
----
+
Because the role list includes `infra`, the pod is running on the correct node.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc

[id="infrastructure-moving-registry_{context}"]
= Moving the default registry

[role="_abstract"]
Deploying the registry pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the registry pod by editing the `configs.imageregistry.operator.openshift.io/cluster` config object.

.Prerequisites

* Configure additional compute machine sets in your OpenShift Container Platform cluster.

.Procedure

. Edit the `configs.imageregistry.operator.openshift.io/cluster` object by running the following command:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----

. Add a `nodeSelector` parameter with the appropriate value to the component you want to move, as shown in the following example.
+
[source,yaml]
----
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
# ...
spec:
  logLevel: Normal
  managementState: Managed
  nodeSelector:
    node-role.kubernetes.io/infra: ""
  tolerations:
  - effect: NoSchedule
    key: node-role.kubernetes.io/infra
    value: reserved
----
+
You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.

.Verification

* Verify the registry pod has been moved to the infrastructure node.
+
.. Identify the node where the registry pod is located by running the following command:
+
[source,terminal]
----
$ oc get pods -o wide -n openshift-image-registry
----
+
.. Confirm the node has the label you specified:
+
[source,terminal]
----
$ oc describe node <node_name>
----
+
where:

`<node_name>`:: Specifies the name of the node that you modified. Review the command output and confirm that `node-role.kubernetes.io/infra` is in the `LABELS` list.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc

[id="infrastructure-moving-monitoring_{context}"]
= Moving the monitoring solution

[role="_abstract"]
Redeploy the monitoring stack to infrastructure nodes to reduce your subscription requirements. Create and apply a custom config map to move the monitoring stack to infrastructure nodes. The monitoring stack includes Prometheus, Thanos Querier, and Alertmanager, and is managed by the {cmo-first}.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have installed the {oc-first}.

.Procedure

. Edit the `cluster-monitoring-config` config map and change the `nodeSelector` to use the `infra` label by running the following command:
+
[source,terminal]
----
$ oc edit configmap cluster-monitoring-config -n openshift-monitoring
----
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |+
    alertmanagerMain:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    prometheusK8s:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    prometheusOperator:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    metricsServer:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    kubeStateMetrics:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    telemeterClient:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    openshiftStateMetrics:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    thanosQuerier:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    monitoringPlugin:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
----
+
Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.

. Watch the monitoring pods move to the new machines by running the following command:
+
[source,terminal]
----
$ watch 'oc get pod -n openshift-monitoring -o wide'
----

. If a component has not moved to the `infra` node, delete the pod with this component by running the following command:
+
[source,terminal]
----
$ oc delete pod -n openshift-monitoring <pod>
----
+
The component from the deleted pod is re-created on the `infra` node.

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

[id="custer-tasks-applying-autoscaling"]
== Applying autoscaling to your cluster

Applying autoscaling to an OpenShift Container Platform cluster involves deploying a cluster autoscaler and then deploying machine autoscalers for each machine type in your cluster.

For more information, see Applying autoscaling to an OpenShift Container Platform cluster.

[id="post-install-tp-tasks"]
== Enabling Technology Preview features using FeatureGates

You can turn on a subset of the current Technology Preview features on for all nodes in the cluster by editing the `FeatureGate` custom resource (CR).

// Module included in the following assemblies:
//
// nodes/clusters/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-about_{context}"]
= Understanding feature gates

[role="_abstract"]
You can use the `FeatureGate` custom resource (CR) to enable specific feature sets so that you can use specific non-default features in your cluster.

A feature set is a collection of OpenShift Container Platform features that are not enabled by default.

You can activate the following feature set by using the `FeatureGate` CR:

* `TechPreviewNoUpgrade`. This feature set is a subset of the current Technology Preview features. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them, while leaving the features disabled on production clusters.
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====
+
The following Technology Preview features are enabled by this feature set:
+
--
** `AdditionalStorageConfig`
** `AutomatedEtcdBackup`
** `AWSClusterHostedDNS`
** `AWSClusterHostedDNSInstall`
** `AWSDedicatedHosts`
** `AWSDualStackInstall`
** `AWSEuropeanSovereignCloudInstall`
** `AWSServiceLBNetworkSecurityGroup`
** `AzureClusterHostedDNSInstall`
** `AzureDedicatedHosts`
** `AzureDualStackInstall`
** `AzureMultiDisk`
** `AzureWorkloadIdentity`
** `BootcNodeManagement`
** `BootImageSkewEnforcement`
** `BuildCSIVolumes`
** `CBORServingAndStorage`
** `ClientsPreferCBOR`
** `ClusterAPIInstallIBMCloud`
** `ClusterAPIMachineManagement`
** `ClusterAPIMachineManagementAWS`
** `ClusterAPIMachineManagementAzure`
** `ClusterAPIMachineManagementBareMetal`
** `ClusterAPIMachineManagementGCP`
** `ClusterAPIMachineManagementOpenStack
** `ClusterAPIMachineManagementPowerVS`
** `ClusterAPIMachineManagementVSphere`
** `ClusterMonitoringConfig`
** `ClusterUpdateAcceptRisks`
** `ClusterVersionOperatorConfiguration`
** `ConfigurablePKI`
** `ConsolePluginContentSecurityPolicy`
** `CRDCompatibilityRequirementOperator`
** `CRIOCredentialProviderConfig`
** `DNSNameResolver`
** `DRAPartitionableDevices`
** `DualReplica`
** `DynamicServiceEndpointIBMCloud`
** `EtcdBackendQuota`
** `EventTTL`
//** `EVPN` From Anurag Saxena: EVPN shouldn't be there. It is lifted and to be GA'ed in 4.22.
** `Example`
** `ExternalOIDC`
** `ExternalOIDCWithUIDAndExtraClaimMappings`
** `ExternalOIDCWithUpstreamParity`
** `GatewayAPIWithoutOLM`
** `GCPCustomAPIEndpoints`
** `GCPCustomAPIEndpointsInstall`
** `GCPDualStackInstall`
** `HyperShiftOnlyDynamicResourceAllocation`
** `ImageModeStatusReporting`
** `ImageStreamImportMode`
** `IngressControllerDynamicConfigurationManager`
** `InsightsConfig`
** `InsightsOnDemandDataGather`
** `IrreconcilableMachineConfig`
** `KMSEncryption`
** `KMSv1`
** `MachineAPIMigration`
** `MachineAPIMigrationAWS`
** `MachineAPIMigrationOpenStack`
** `ManagedBootImagesCPMS`
** `MaxUnavailableStatefulSet`
** `MetricsCollectionProfiles`
** `MinimumKubeletVersion`
** `MixedCPUsAllocation`
** `MultiDiskSetup`
** `MutableCSINodeAllocatableCount`
** `MutatingAdmissionPolicy`
** `NewOLM`
** `NewOLMBoxCutterRuntime`
** `NewOLMCatalogdAPIV1Metas`
** `NewOLMConfigAPI`
** `NewOLMOwnSingleNamespace`
** `NewOLMPreflightPermissionChecks`
** `NewOLMWebhookProviderOpenshiftServiceCA`
//From Arti Sood: lgtm for NoOverlayMode
** `NoOverlayMode`
** `NoRegistryClusterInstall`
** `NutanixMultiSubnets`
** `OnPremDNSRecords`
** `OpenShiftPodSecurityAdmission`
** `OSStreams`
** `OVNObservability`
** `RouteExternalCertificate`
** `SELinuxMount`
** `ServiceAccountTokenNodeBinding`
** `SignatureStores`
** `SigstoreImageVerification`
** `SigstoreImageVerificationPKI`
** `StoragePerformantSecurityPolicy`
** `TLSAdherence`
** `UpgradeStatus`
** `UserNamespacesPodSecurityStandards`
** `UserNamespacesSupport`
** `VolumeGroupSnapshot`
** `VSphereConfigurableMaxAllowedBlockVolumesPerNode`
** `VSphereHostVMGroupZonal`
** `VSphereMixedNodeEnv`
** `VSphereMultiDisk`
** `VSphereMultiNetworks`
--

See the _Additional resources_ sections for information on some of these features.

Do not document per Derek Carr: https://github.com/openshift/api/pull/370#issuecomment-510632939
|`CustomNoUpgrade` ^[2]^
|Allows the enabling or disabling of any feature. Turning on this feature set on is not supported, cannot be undone, and prevents upgrades.

[.small]
--
1.
2. If you use the `CustomNoUpgrade` feature set to disable a feature that appears in the web console, you might see that feature, but
no objects are listed. For example, if you disable builds, you can see the *Builds* tab in the web console, but there are no builds present. If you attempt to use commands associated with a disabled feature, such as `oc start-build`, OpenShift Container Platform displays an error.

[NOTE]
====
If you disable a feature that any application in the cluster relies on, the application might not
function properly, depending upon the feature disabled and how the application uses that feature.
====

// Module included in the following assemblies:
//
// * nodes/clusters/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-console_{context}"]
= Enabling feature sets using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

.Procedure

. In the OpenShift Container Platform web console, switch to the *Administration* -> *Custom Resource Definitions* page.

. On the *Custom Resource Definitions* page, click *FeatureGate*.

. On the *Custom Resource Definition Details* page, click the *Instances* tab.

. Click the *cluster* feature gate, then click the *YAML* tab.

. Edit the *cluster* instance to add specific feature sets:
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====

+
.Sample Feature Gate custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster <1>
# ...
spec:
  featureSet: TechPreviewNoUpgrade <2>
----
where:
+
--
`metadata.name`:: Specifies the name of the `FeatureGate` CR. You must specify `cluster` for the name.

`spec.featureSet`:: Specifies the feature set that you want to enable:
* `TechPreviewNoUpgrade` enables specific Technology Preview features.
--
+
After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

.Verification

// Module included in the following assemblies:
//
// * nodes/cluster/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-cli_{context}"]
= Enabling feature sets using the CLI

[role="_abstract"]
You can use the {oc-first} to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Edit the `FeatureGate` CR named `cluster`:
+
[source,terminal]
----
$ oc edit featuregate cluster
----
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====
+
.Sample FeatureGate custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster
# ...
spec:
  featureSet: TechPreviewNoUpgrade
----
where:
+
--
`metadata.name`:: Specifies the name of the `FeatureGate` CR. This must be `cluster`.

`spec.featureSet`:: Specifies the feature set that you want to enable:
* `TechPreviewNoUpgrade` enables specific Technology Preview features.
--
+
After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

.Verification

[id="post-install-etcd-tasks"]
== etcd tasks
Back up etcd, enable or disable etcd encryption, or defragment etcd data.

[NOTE]
====
If you deployed a bare-metal cluster, you can scale the cluster up to 5 nodes as part of your post-installation tasks. For more information, see Node scaling for etcd.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-encrypt.adoc

[id="about-etcd_{context}"]
= About etcd encryption

By default, etcd data is not encrypted in OpenShift Container Platform. You can enable etcd encryption for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties.

When you enable etcd encryption, the following OpenShift API server and Kubernetes API server resources are encrypted:

* Secrets
* Config maps
* Routes
* OAuth access tokens
* OAuth authorize tokens

When you enable etcd encryption, encryption keys are created. You must have these keys to restore from an etcd backup.

[NOTE]
====
Etcd encryption only encrypts values, not keys. Resource types, namespaces, and object names are unencrypted.

If etcd encryption is enabled during a backup, the `__static_kuberesources_<datetimestamp>.tar.gz__` file contains the encryption keys for the etcd snapshot. For security reasons, store this file separately from the etcd snapshot. However, this file is required to restore a previous state of etcd from the respective etcd snapshot.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-encrypt.adoc

[id="etcd-encryption-types_{context}"]
= Supported encryption types

The following encryption types are supported for encrypting etcd data in OpenShift Container Platform:

AES-CBC:: Uses AES-CBC with PKCS#7 padding and a 32 byte key to perform the encryption.

AES-GCM:: Uses AES-GCM with a random nonce and a 32 byte key to perform the encryption.

The etcd encryption keys are rotated every 7 days. Up to 10 historical encryption keys are preserved after rotation to facilitate the decryption of older backups and provide an extra layer of data recovery safety.

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-encrypt.adoc

[id="enabling-etcd-encryption_{context}"]
= Enabling etcd encryption

You can enable etcd encryption to encrypt sensitive resources in your cluster.

[WARNING]
====
Do not back up etcd resources until the initial encryption process is completed. If the encryption process is not completed, the backup might be only partially encrypted.

After you enable etcd encryption, several changes can occur:

* The etcd encryption might affect the memory consumption of a few resources.
* You might notice a transient affect on backup performance because the leader must serve the backup.
* A disk I/O can affect the node that receives the backup state.
====

You can encrypt the etcd database in either AES-GCM or AES-CBC encryption.

[NOTE]
====
To migrate your etcd database from one encryption type to the other, you can modify the API server's `spec.encryption.type` field. Migration of the etcd data to the new encryption type occurs automatically.
====

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Modify the `APIServer` object:
+
[source,terminal]
----
$ oc edit apiserver
----

. Set the `spec.encryption.type` field to `aesgcm` or `aescbc`:
+
[source,yaml]
----
spec:
  encryption:
    type: aesgcm <1>
----
<1> Set to `aesgcm` for AES-GCM encryption or `aescbc` for AES-CBC encryption.

. Save the file to apply the changes.
+
The encryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of the etcd database.

. Verify that etcd encryption was successful.

.. Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully encrypted:
+
[source,terminal]
----
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `EncryptionCompleted` upon successful encryption:
+
[source,terminal]
----
EncryptionCompleted
All resources encrypted: routes.route.openshift.io
----
+
If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

.. Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully encrypted:
+
[source,terminal]
----
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `EncryptionCompleted` upon successful encryption:
+
[source,terminal]
----
EncryptionCompleted
All resources encrypted: secrets, configmaps
----
+
If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

.. Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully encrypted:
+
[source,terminal]
----
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `EncryptionCompleted` upon successful encryption:
+
[source,terminal]
----
EncryptionCompleted
All resources encrypted: oauthaccesstokens.oauth.openshift.io, oauthauthorizetokens.oauth.openshift.io
----
+
If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-encrypt.adoc

[id="disabling-etcd-encryption_{context}"]
= Disabling etcd encryption

You can disable encryption of etcd data in your cluster.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Modify the `APIServer` object:
+
[source,terminal]
----
$ oc edit apiserver
----

. Set the `encryption` field type to `identity`:
+
[source,yaml]
----
spec:
  encryption:
    type: identity <1>
----
<1> The `identity` type is the default value and means that no encryption is performed.

. Save the file to apply the changes.
+
The decryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of your cluster.

. Verify that etcd decryption was successful.

.. Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully decrypted:
+
[source,terminal]
----
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `DecryptionCompleted` upon successful decryption:
+
[source,terminal]
----
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
----
+
If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

.. Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully decrypted:
+
[source,terminal]
----
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `DecryptionCompleted` upon successful decryption:
+
[source,terminal]
----
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
----
+
If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

.. Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully decrypted:
+
[source,terminal]
----
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
The output shows `DecryptionCompleted` upon successful decryption:
+
[source,terminal]
----
DecryptionCompleted
Encryption mode set to identity and everything is decrypted
----
+
If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

// Module included in the following assemblies:
//
// * backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="backing-up-etcd-data_{context}"]
= Backing up etcd data

[role="_abstract"]
Follow these steps to back up etcd data by creating an etcd snapshot and backing up the resources for the static pods. This backup can be saved and used at a later time if you need to restore etcd.

[IMPORTANT]
====
Only save a backup from a single control plane host. Do not take a backup from each control plane host in the cluster.
====

For a Two-Node with Fencing (TNF) setup, follow the steps to back up etcd data on only one node in the cluster. The cluster restore process is driven by data from a single node, so you can perform the etcd backup steps on only one node.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have checked whether the cluster-wide proxy is enabled.
+
[TIP]
====
You can check whether the proxy is enabled by reviewing the output of `oc get proxy cluster -o yaml`. The proxy is enabled if the `httpProxy`, `httpsProxy`, and `noProxy` fields have values set.
====

.Procedure

. Start a debug session as root for a control plane node:
+
[source,terminal]
----
$ oc debug --as-root node/<node_name>
----

. Change your root directory to `/host` in the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. If the cluster-wide proxy is enabled, export the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` environment variables by running the following commands:
+
[source,terminal]
----
$ export HTTP_PROXY=http://<your_proxy.example.com>:8080
----
+
[source,terminal]
----
$ export HTTPS_PROXY=https://<your_proxy.example.com>:8080
----
+
[source,terminal]
----
$ export NO_PROXY=<example.com>
----
+

. Run the `cluster-backup.sh` script in the debug shell and pass in the location to save the backup to.
+
[TIP]
====
The `cluster-backup.sh` script is maintained as a component of the etcd Cluster Operator and is a wrapper around the `etcdctl snapshot save` command.
====
+
[source,terminal]
----
sh-4.4# /usr/local/bin/cluster-backup.sh /home/core/assets/backup
----
+
.Example script output
[source,terminal]
----
found latest kube-apiserver: /etc/kubernetes/static-pod-resources/kube-apiserver-pod-6
found latest kube-controller-manager: /etc/kubernetes/static-pod-resources/kube-controller-manager-pod-7
found latest kube-scheduler: /etc/kubernetes/static-pod-resources/kube-scheduler-pod-6
found latest etcd: /etc/kubernetes/static-pod-resources/etcd-pod-3
ede95fe6b88b87ba86a03c15e669fb4aa5bf0991c180d3c6895ce72eaade54a1
etcdctl version: 3.4.14
API version: 3.4
{"level":"info","ts":1624647639.0188997,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db.part"}
{"level":"info","ts":"2021-06-25T19:00:39.030Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":1624647639.0301006,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"https://10.0.0.5:2379"}
{"level":"info","ts":"2021-06-25T19:00:40.215Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
{"level":"info","ts":1624647640.6032252,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"https://10.0.0.5:2379","size":"114 MB","took":1.584090459}
{"level":"info","ts":1624647640.6047094,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db"}
Snapshot saved at /home/core/assets/backup/snapshot_2021-06-25_190035.db
{"hash":3866667823,"revision":31407,"totalKey":12828,"totalSize":114446336}
snapshot db and kube resources are successfully saved to /home/core/assets/backup
----
+
In this example, two files are created in the `/home/core/assets/backup/` directory on the control plane host:

* `snapshot_<datetimestamp>.db`: This file is the etcd snapshot. The `cluster-backup.sh` script confirms its validity.
* `static_kuberesources_<datetimestamp>.tar.gz`: This file contains the resources for the static pods. If etcd encryption is enabled, it also contains the encryption keys for the etcd snapshot.
+
[NOTE]
====
If etcd encryption is enabled, store this second file separately from the etcd snapshot for security reasons. However, this file is required to restore from the etcd snapshot.

The etcd encryption only encrypts values, not keys. This means that resource types, namespaces, and object names are not encrypted.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-performance.adoc

[id="etcd-defrag_{context}"]
= Defragmenting etcd data

For large and dense clusters, etcd can suffer from poor performance if the keyspace grows too large and exceeds the space quota. Periodically maintain and defragment etcd to free up space in the data store. Monitor Prometheus for etcd metrics and defragment it when required; otherwise, etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode that accepts only key reads and deletes.

Monitor these key metrics:

* `etcd_server_quota_backend_bytes`, which is the current quota limit
* `etcd_mvcc_db_total_size_in_use_in_bytes`, which indicates the actual database usage after a history compaction
* `etcd_mvcc_db_total_size_in_bytes`, which shows the database size, including free space waiting for defragmentation

Defragment etcd data to reclaim disk space after events that cause disk fragmentation, such as etcd history compaction.

History compaction is performed automatically every five minutes and leaves gaps in the back-end database. This fragmented space is available for use by etcd, but is not available to the host file system. You must defragment etcd to make this space available to the host file system.

Defragmentation occurs automatically, but you can also trigger it manually.

[NOTE]
====
Automatic defragmentation is good for most cases, because the etcd operator uses cluster information to determine the most efficient operation for the user.
====

[id="automatic-defrag-etcd-data_{context}"]
== Automatic defragmentation

The etcd Operator automatically defragments disks. No manual intervention is needed.

Verify that the defragmentation process is successful by viewing one of these logs:

* etcd logs
* cluster-etcd-operator pod
* operator status error log

[WARNING]
====
Automatic defragmentation can cause leader election failure in various OpenShift core components, such as the Kubernetes controller manager, which triggers a restart of the failing component. The restart is harmless and either triggers failover to the next running instance or the component resumes work again after the restart.
====

.Example log output for successful defragmentation
[source,terminal]
[subs="+quotes"]
----
etcd member has been defragmented: __<member_name>__, memberID: __<member_id>__
----

.Example log output for unsuccessful defragmentation
[source,terminal]
[subs="+quotes"]
----
failed defrag on member: __<member_name>__, memberID: __<member_id>__: __<error_message>__
----

[id="manual-defrag-etcd-data_{context}"]
== Manual defragmentation

//You can monitor the `etcd_db_total_size_in_bytes` metric to determine whether manual defragmentation is necessary.

A Prometheus alert indicates when you need to use manual defragmentation. The alert is displayed in two cases:

   * When etcd uses more than 50% of its available space for more than 10 minutes
   * When etcd is actively using less than 50% of its total database size for more than 10 minutes

You can also determine whether defragmentation is needed by checking the etcd database size in MB that will be freed by defragmentation with the PromQL expression: `(etcd_mvcc_db_total_size_in_bytes - etcd_mvcc_db_total_size_in_use_in_bytes)/1024/1024`

[WARNING]
====
Defragmenting etcd is a blocking action. The etcd member will not respond until defragmentation is complete. For this reason, wait at least one minute between defragmentation actions on each of the pods to allow the cluster to recover.
====

Follow this procedure to defragment etcd data on each etcd member.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Determine which etcd member is the leader, because the leader should be defragmented last.

.. Get the list of etcd pods:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
----
+
.Example output
[source,terminal]
----
etcd-ip-10-0-159-225.example.redhat.com                3/3     Running     0          175m   10.0.159.225   ip-10-0-159-225.example.redhat.com   <none>           <none>
etcd-ip-10-0-191-37.example.redhat.com                 3/3     Running     0          173m   10.0.191.37    ip-10-0-191-37.example.redhat.com    <none>           <none>
etcd-ip-10-0-199-170.example.redhat.com                3/3     Running     0          176m   10.0.199.170   ip-10-0-199-170.example.redhat.com   <none>           <none>
----

.. Choose a pod and run the following command to determine which etcd member is the leader:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com etcdctl endpoint status --cluster -w table
----
+
.Example output
[source,terminal]
----
Defaulting container name to etcdctl.
Use 'oc describe pod/etcd-ip-10-0-159-225.example.redhat.com -n openshift-etcd' to see all of the containers in this pod.
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
----
+
Based on the `IS LEADER` column of this output, the [x-]`https://10.0.199.170:2379` endpoint is the leader. Matching this endpoint with the output of the previous step, the pod name of the leader is `etcd-ip-10-0-199-170.example.redhat.com`.

. Defragment an etcd member.

.. Connect to the running etcd container, passing in the name of a pod that is _not_ the leader:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com
----

.. Unset the `ETCDCTL_ENDPOINTS` environment variable:
+
[source,terminal]
----
sh-4.4# unset ETCDCTL_ENDPOINTS
----

.. Defragment the etcd member:
+
[source,terminal]
----
sh-4.4# etcdctl --command-timeout=30s --endpoints=https://localhost:2379 defrag
----
+
.Example output
[source,terminal]
----
Finished defragmenting etcd member[https://localhost:2379]
----
+
If a timeout error occurs, increase the value for `--command-timeout` until the command succeeds.

.. Verify that the database size was reduced:
+
[source,terminal]
----
sh-4.4# etcdctl endpoint status -w table --cluster
----
+
.Example output
[source,terminal]
----
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
| https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |   41 MB |     false |      false |         7 |      91624 |              91624 |        | <1>
| https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
+---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
----
This example shows that the database size for this etcd member is now 41 MB as opposed to the starting size of 104 MB.

.. Repeat these steps to connect to each of the other etcd members and defragment them. Always defragment the leader last.
+
Wait at least one minute between defragmentation actions to allow the etcd pod to recover. Until the etcd pod recovers, the etcd member will not respond.

. If any `NOSPACE` alarms were triggered due to the space quota being exceeded, clear them.

.. Check if there are any `NOSPACE` alarms:
+
[source,terminal]
----
sh-4.4# etcdctl alarm list
----
+
.Example output
[source,terminal]
----
memberID:12345678912345678912 alarm:NOSPACE
----

.. Clear the alarms:
+
[source,terminal]
----
sh-4.4# etcdctl alarm disarm
----

// Module included in the following assemblies:
//
// * disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

// Contributors: The documentation for this section changed drastically for 4.18+.

// Contributors: Some changes for the `etcd` restore procedure are only valid for 4.14+.
// In the 4.14+ documentation, OVN-K requires different steps because there is no centralized OVN
// control plane to be converted. For more information, see PR #64939.
// Do not cherry pick from "main" to "enterprise-4.12" or "enterprise-4.13" because the cherry pick
// procedure is different for these versions. Instead, open a separate PR for 4.13 and
// cherry pick to 4.12 or make the updates directly in 4.12.

[id="dr-scenario-2-restoring-cluster-state_{context}"]
= Restoring to an earlier cluster state for more than one node

[role="abstract"]
You can use a saved etcd backup to restore an earlier cluster state or restore a cluster that has lost the majority of control plane hosts.

For a Two-Node with Fencing (TNF) setup, a single surviving node can continue to operate in degraded mode. Use a saved etcd backup to restore an earlier cluster state if only one node is operational, or when both nodes have failed and you need to restart the cluster from a known safe state. In both cases, perform the restore procedure on a single node. The peer node automatically synchronizes its data with the restored node when it rejoins the cluster.

For a 3-node HA cluster, shut down etcd on the following number of hosts:

- For 3-node clusters: Shut down etcd on 2 hosts.
- For 4-node and 5-node clusters: Shut down etcd on 3 hosts.

Quorum requires a simple majority of nodes. The minimum number of nodes required for a quorum is as follows:

- For 3-node HA cluster: 2.
- For 4-node and 5-node HA clusters: 3.

If you start a new cluster from backup on your recovery host, the other etcd members might still form a quorum and continue service.

[NOTE]
====
If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in "Troubleshooting the control plane machine set" for an etcd recovery procedure. For OpenShift Container Platform on a single node, see "Restoring to an earlier cluster state for a single node".
====

[IMPORTANT]
====
When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform .2 cluster must use an etcd backup that was taken from .2.
====

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation.
* A healthy control plane host to use as the recovery host.
* You have SSH access to control plane hosts.
* A backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.
* Nodes must be accessible or bootable.

[IMPORTANT]
====
For non-recovery control plane nodes, it is not required to establish SSH connectivity or to stop the static pods. You can delete and re-create other non-recovery, control plane machines, one by one.
====

.Procedure

. Select a control plane host to use as the recovery host. This is the host that you run the restore operation on.

. Establish SSH connectivity to each of the control plane nodes, including the recovery host.
+
`kube-apiserver` becomes inaccessible after the restore process starts, so you cannot access the control plane nodes. For this reason, it is recommended to establish SSH connectivity to each control plane host in a separate terminal.
+
[IMPORTANT]
====
If you do not complete this step, you cannot access the control plane hosts to complete the restore procedure, and you cannot recover your cluster from this state.
====

. Using SSH, connect to each control plane node and run the following command to disable etcd:
+
[source,terminal]
----
$ sudo -E /usr/local/bin/disable-etcd.sh
----

. Copy the etcd backup directory to the recovery control plane host.
+
This procedure assumes that you copied the `backup` directory containing the etcd snapshot and the resources for the static pods to the `/home/core/` directory of your recovery control plane host.

. Use SSH to connect to the recovery host. To restore the cluster from an earlier backup, run the following command:
+
[source,terminal]
----
$ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd-backup-directory>
----

. Exit the SSH session.

. When the API responds, to turn off the etcd Operator quorum guard, run the following command:

[IMPORTANT]
====
For a TNF setup, do not:

  * Change the etcd Operator quorum setting.

  * Turn the etcd Operator quorum off.

  * Turn the etcd Operator quorum on back.
====
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----

. Monitor the recovery progress of the control plane by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
[NOTE]
====
It can take up to 15 minutes for the control plane to recover. Wait for the control plane to recover before using the next step.
====

. Enable the quorum guard by running the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

.Troubleshooting

If the etcd static pods do not roll out, you can manually force an etcd redeployment from the `cluster-etcd-operator` by running the following command:

[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
----

[role="_additional-resources"]
.Additional resources
* Recommended etcd practices
* Installing a user-provisioned cluster on bare metal
* Replacing a bare-metal control plane node

// Module included in the following assemblies:
//
// * disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

[id="dr-scenario-cluster-state-issues_{context}"]
= Issues and workarounds for restoring a persistent storage state

If your OpenShift Container Platform cluster uses persistent storage of any form, a state of the cluster is typically stored outside etcd. When you restore from an etcd backup, the status of the workloads in OpenShift Container Platform is also restored. However, if the etcd snapshot is old, the status might be invalid or outdated.

[IMPORTANT]
====
The contents of persistent volumes (PVs) are never part of the etcd snapshot. When you restore an OpenShift Container Platform cluster from an etcd snapshot, non-critical workloads might gain access to critical data, or vice-versa.
====

The following are some example scenarios that produce an out-of-date status:

* MySQL database is running in a pod backed up by a PV object. Restoring OpenShift Container Platform from an etcd snapshot does not bring back the volume on the storage provider, and does not produce a running MySQL pod, despite the pod repeatedly attempting to start. You must manually restore this pod by restoring the volume on the storage provider, and then editing the PV to point to the new volume.

* Pod P1 is using volume A, which is attached to node X. If the etcd snapshot is taken while another pod uses the same volume on node Y, then when the etcd restore is performed, pod P1 might not be able to start correctly due to the volume still being attached to node Y. OpenShift Container Platform is not aware of the attachment, and does not automatically detach it. When this occurs, the volume must be manually detached from node Y so that the volume can attach on node X, and then pod P1 can start.

* Cloud provider or storage provider credentials were updated after the etcd snapshot was taken. This causes any CSI drivers or Operators that depend on the those credentials to not work. You might have to manually update the credentials required by those drivers or Operators.

* A device is removed or renamed from OpenShift Container Platform nodes after the etcd snapshot is taken. The Local Storage Operator creates symlinks for each PV that it manages from `/dev/disk/by-id` or `/dev` directories. This situation might cause the local PVs to refer to devices that no longer exist.
+
To fix this problem, an administrator must:

. Manually remove the PVs with invalid devices.
. Remove symlinks from respective nodes.
. Delete `LocalVolume` or `LocalVolumeSet` objects (see _Storage_ -> _Configuring persistent storage_ -> _Persistent storage using local volumes_ -> _Deleting the Local Storage Operator Resources_).

[id="post-install-pod-disruption-budgets"]
== Pod disruption budgets

Understand and configure pod disruption budgets.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring
// * post_installation_configuration/cluster-tasks.adoc

[id="nodes-pods-pod-distruption-about_{context}"]
= Understanding how to use pod disruption budgets to specify the number of pods that must be up

[role="_abstract"]
To ensure pod availability during voluntary disruptions such as node maintenance or cluster updates, you can use pod disruption budgets to define safety constraints for your applications.

A `PodDisruptionBudget` is an API object that specifies the minimum number or
percentage of replicas that must be up at a time. Setting these in projects can
be helpful during node maintenance (such as scaling a cluster down or a cluster
upgrade) and is only honored on voluntary evictions (not on node failures).

A `PodDisruptionBudget` object's configuration consists of the following key
parts:

* A label selector, which is a label query over a set of pods.
* An availability level, which specifies the minimum number of pods that must be
 available simultaneously, either:
** `minAvailable` is the number of pods must always be available, even during a disruption.
** `maxUnavailable` is the number of pods can be unavailable during a disruption.

[NOTE]
====
`Available` refers to the number of pods that has condition `Ready=True`.
`Ready=True` refers to the pod that is able to serve requests and should be added to the load balancing pools of all matching services.

A `maxUnavailable` of `0%` or `0` or a `minAvailable` of `100%` or equal to the number of replicas
is permitted but can block nodes from being drained.
====

[WARNING]
====
The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.
====

You can check for pod disruption budgets across all projects with the following:

[source,terminal]
----
$ oc get poddisruptionbudget --all-namespaces
----

.Example output
[source,terminal]
----
NAMESPACE                              NAME                                    MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
openshift-apiserver                    openshift-apiserver-pdb                 N/A             1                 1                     121m
openshift-cloud-controller-manager     aws-cloud-controller-manager            1               N/A               1                     125m
openshift-cloud-credential-operator    pod-identity-webhook                    1               N/A               1                     117m
openshift-cluster-csi-drivers          aws-ebs-csi-driver-controller-pdb       N/A             1                 1                     121m
openshift-cluster-storage-operator     csi-snapshot-controller-pdb             N/A             1                 1                     122m
openshift-cluster-storage-operator     csi-snapshot-webhook-pdb                N/A             1                 1                     122m
openshift-console                      console                                 N/A             1                 1                     116m
#...
----

The `PodDisruptionBudget` is considered healthy when there are at least
`minAvailable` pods running in the system. Every pod above that limit can be evicted.

[NOTE]
====
Depending on your pod priority and preemption settings,
lower-priority pods might be removed despite their pod disruption budget requirements.
====

// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring
// * post_installation_configuration/cluster-tasks.adoc

[id="nodes-pods-pod-disruption-configuring_{context}"]
= Specifying the number of pods that must be up with pod disruption budgets

[role="_abstract"]
You can use a `PodDisruptionBudget` object to specify the minimum number or percentage of replicas that must be up at a time. This ensures pod availability during voluntary disruptions such as node maintenance or cluster updates.

The following procedure shows how to configure a pod disruption budget.

.Procedure

. Create a YAML file with the an object definition similar to the following:
+
[source,yaml]
----
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      name: my-pod
----
where:
+
--
`apiVersion`:: Specifies the `policy/v1` API group.
`spec.minAvailable`:: Specifies the minimum number of pods that must be available simultaneously. This can
be either an integer or a string specifying a percentage, for example, `20%`.
`spec.selector`:: Specifies a label query over a set of resources. The result of `matchLabels` and
 `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project.
--
+
Or:
+
[source,yaml]
----
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  maxUnavailable: 25%
  selector:
    matchLabels:
      name: my-pod
----
where:
+
--
`apiVersion`:: Specifies the `policy/v1` API group.
`spec.maxUnavailable`:: Specifies the maximum number of pods that can be unavailable simultaneously. This can
be either an integer or a string specifying a percentage, for example, `20%`.
`spec.selector`:: Specifies a label query over a set of resources. The result of `matchLabels` and
 `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project.
--

. Run the following command to add the object to project:
+
[source,terminal]
----
$ oc create -f </path/to/file> -n <project_name>
----

// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring
// * post_installation_configuration/cluster-tasks.adoc

[id="pod-disruption-eviction-policy_{context}"]
= Specifying the eviction policy for unhealthy pods

[role="_abstract"]
When you use pod disruption budgets (PDBs) to specify how many pods must be available simultaneously, you can also define the criteria for how unhealthy pods are considered for eviction. The eviction policy determines which pods the cluster can evict.

You can choose one of the following policies:

IfHealthyBudget:: Running pods that are not yet healthy can be evicted only if the guarded application is not disrupted.

AlwaysAllow:: Running pods that are not yet healthy can be evicted regardless of whether the criteria in the pod disruption budget is met. This policy can help evict malfunctioning applications, such as ones with pods stuck in the `CrashLoopBackOff` state or failing to report the `Ready` status.
+
[NOTE]
====
It is recommended to set the `unhealthyPodEvictionPolicy` field to `AlwaysAllow` in the `PodDisruptionBudget` object to support the eviction of misbehaving applications during a node drain. The default behavior is to wait for the application pods to become healthy before the drain can proceed.
====

.Procedure

. Create a YAML file that defines a `PodDisruptionBudget` object and specify the unhealthy pod eviction policy:
+
.Example `pod-disruption-budget.yaml` file
[source,yaml]
----
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      name: my-pod
  unhealthyPodEvictionPolicy: AlwaysAllow
----
where:

`spec.unhealthyPodEvictionPolicy`:: Specifies the unhealthy pod eviction policy, either `IfHealthyBudget` or `AlwaysAllow`. The default is `IfHealthyBudget` when the `unhealthyPodEvictionPolicy` field is empty.

. Create the `PodDisruptionBudget` object by running the following command:
+
[source,terminal]
----
$ oc create -f pod-disruption-budget.yaml
----
+
With a PDB that has the `AlwaysAllow` unhealthy pod eviction policy set, you can now drain nodes and evict the pods for a malfunctioning application guarded by this PDB.

[role="_additional-resources"]
.Additional resources
* Enabling features using feature gates
* Unhealthy Pod Eviction Policy in the Kubernetes documentation
