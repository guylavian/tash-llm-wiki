---
title: "Improving cluster stability in high latency environments using worker latency profiles"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-scaling-worker-latency-profiles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/scaling-worker-latency-profiles
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Improving cluster stability in high latency environments using worker latency profiles

[id="scaling-worker-latency-profiles"]
= Improving cluster stability in high latency environments using worker latency profiles

[role="_abstract"]
To improve cluster stability in high latency environments, apply worker latency profiles.

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
// * scalability_and_performance/scaling-worker-latency-profiles.adoc

[id="nodes-cluster-worker-latency-profiles-using-at-creation_{context}"]
= Implementing worker latency profiles at cluster creation

[role="_abstract"]
During cluster creation, you can implement worker latency profiles so that you can control the reaction of the cluster to latency issues without relying on manual methods to determine the best values.

[IMPORTANT]
====
To edit the configuration of the installation program, first use the command `openshift-install create manifests` to create the default node manifest and other manifest YAML files. This file structure must exist before you can add `workerLatencyProfile`. The platform on which you are installing might have varying requirements. Refer to the Installing section of the documentation for your specific platform.
====

.Procedure

. Create the manifest that is needed to build the cluster by using a folder name appropriate for your installation.

. Create a YAML file to define `config.node`. The file must be in the `manifests` directory.

. When defining `workerLatencyProfile` in the manifest for the first time, specify any of the profiles at cluster creation time: `Default`, `MediumUpdateAverageReaction` or `LowUpdateSlowReaction`.

.Verification

* View the manifest file by running the following command. The output of the command should show the creation of the `spec.workerLatencyProfile` `Default` value in the manifest file.
+
[source,terminal]
----
$ openshift-install create manifests --dir=<cluster_install_dir>
----
* `<cluster_install_dir>`: Specifies the directory where you installed your cluster.

* Edit the manifest and add the value by entering the following command. The following example command uses the `vi` editor to show an example manifest file with the "Default" `workerLatencyProfile` value added.
+
[source,terminal]
----
$ vi <cluster_install_dir>/manifests/config-node-default-profile.yaml
----
* `<cluster_install_dir>`: Specifies the directory where you installed your cluster.
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Node
metadata:
name: cluster
spec:
workerLatencyProfile: "Default"
# ...
----

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

// Module included in the following assemblies:
//
// scalability_and_performance/scaling-worker-latency-profiles.adoc

[id="nodes-cluster-worker-latency-profiles-examining_{context}"]
= Displaying resulting values of worker latency profile

[role="_abstract"]
You can run specific commands to display the values for the worker latency profile. You can then check the displayed values for information accuracy.

.Procedure

. Check the `default-not-ready-toleration-seconds` and `default-unreachable-toleration-seconds` fields output by the Kube API Server:
+
[source,terminal]
----
$ oc get KubeAPIServer -o yaml | grep -A 1 default-
----
+
.Example output
[source,terminal]
----
default-not-ready-toleration-seconds:
- "300"
default-unreachable-toleration-seconds:
- "300"
----

. Check the values of the `node-monitor-grace-period` field from the Kube Controller Manager:
+
[source,terminal]
----
$ oc get KubeControllerManager -o yaml | grep -A 1 node-monitor
----
+
.Example output
[source,terminal]
----
node-monitor-grace-period:
- 40s
----

. Check the `nodeStatusUpdateFrequency` value from the Kubelet by entering the following command. Set the directory `/host` as the root directory within the debug shell. By changing the root directory to `/host`, you can run binaries contained in the executable paths of the host.
+
[source,terminal]
----
$ oc debug node/<compute_node_name>
----
+
[source,terminal]
----
$ chroot /host
----
+
[source,terminal]
----
# cat /etc/kubernetes/kubelet.conf|grep nodeStatusUpdateFrequency
----
+
.Example output
[source,terminal]
----
“nodeStatusUpdateFrequency”: “10s”
----
+
These outputs validate the set of timing variables for the Worker Latency Profile.
