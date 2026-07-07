---
title: "Using taints and tolerations to control logging pod placement"
type: reference
domain: openshift
slug: observability-4-22-logging-taints-tolerations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-taints-tolerations
version: 4.22
family: observability
documentKind: "Documentation"
---

# Using taints and tolerations to control logging pod placement

[id="logging-taints-tolerations"]
= Using taints and tolerations to control logging pod placement

Taints and tolerations allow the node to control which pods should (or should not) be scheduled on them.

// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-taints-tolerations.adoc
// * post_installation_configuration/node-tasks.adoc
// * observability/logging/scheduling_resources/logging-taints-tolerations.adoc

[id="nodes-scheduler-taints-tolerations-about_{context}"]
= Understanding taints and tolerations

[role="_abstract"]
You can use a _taint_ on a node to allow that node to refuse a pod to be scheduled unless that pod has a matching _toleration_.

You apply taints to a node through the `Node` specification (`NodeSpec`) and apply tolerations to a pod through the `Pod` specification (`PodSpec`). When you apply a taint to a node, the scheduler cannot place a pod on that node unless the pod can tolerate the taint.

.Example taint in a node specification
[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  name: my-node
#...
spec:
  taints:
  - effect: NoExecute
    key: key1
    value: value1
#...
----

.Example toleration in a `Pod` spec
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
----

Taints and tolerations consist of a key, value, and effect.

[id="taint-components-table_{context}"]
.Taint and toleration components
[cols="3a,8a",options="header"]
|===

|Parameter |Description

|`key`
|The `key` is any string, up to 253 characters. The key must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.

|`value`
| The `value` is any string, up to 63 characters. The value must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.

|`effect`

|The effect is one of the following:
[frame=none]
[cols="2a,3a"]
!====
!`NoSchedule` ^[1]^
!* New pods that do not match the taint are not scheduled onto that node.
* Existing pods on the node remain.
!`PreferNoSchedule`
!* New pods that do not match the taint might be scheduled onto that node, but the scheduler tries not to.
* Existing pods on the node remain.
!`NoExecute`
!* New pods that do not match the taint cannot be scheduled onto that node.
* Existing pods on the node that do not have a matching toleration  are removed.
!====

|`operator`
|[frame=none]
[cols="2,3"]
!====
!`Equal`
!The `key`/`value`/`effect` parameters must match. This is the default.
!`Exists`
!The `key`/`effect` parameters must match. You must leave a blank `value` parameter, which matches any.
!====

|===
[.small]
--
1. If you add a `NoSchedule` taint to a control plane node, the node must have the `node-role.kubernetes.io/master=:NoSchedule` taint, which is added by default.
+
For example:
+
[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  annotations:
    machine.openshift.io/machine: openshift-machine-api/ci-ln-62s7gtb-f76d1-v8jxv-master-0
    machineconfiguration.openshift.io/currentConfig: rendered-master-cdc1ab7da414629332cc4c3926e6e59c
  name: my-node
#...
spec:
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
#...
----
--

A toleration matches a taint:

* If the `operator` parameter is set to `Equal`:
** the `key` parameters are the same;
** the `value` parameters are the same;
** the `effect` parameters are the same.

* If the `operator` parameter is set to `Exists`:
** the `key` parameters are the same;
** the `effect` parameters are the same.

The following taints are built into OpenShift Container Platform:

* `node.kubernetes.io/not-ready`: The node is not ready. This corresponds to the node condition `Ready=False`.
* `node.kubernetes.io/unreachable`: The node is unreachable from the node controller. This corresponds to the node condition `Ready=Unknown`.
* `node.kubernetes.io/memory-pressure`: The node has memory pressure issues. This corresponds to the node condition `MemoryPressure=True`.
* `node.kubernetes.io/disk-pressure`: The node has disk pressure issues. This corresponds to the node condition `DiskPressure=True`.
* `node.kubernetes.io/network-unavailable`: The node network is unavailable.
* `node.kubernetes.io/unschedulable`: The node is unschedulable.
* `node.cloudprovider.kubernetes.io/uninitialized`: When the node controller is started with an external cloud provider, this taint is set on a node to mark it as unusable. After a controller from the cloud-controller-manager initializes this node, the kubelet removes this taint.
* `node.kubernetes.io/pid-pressure`: The node has pid pressure. This corresponds to the node condition `PIDPressure=True`.
+
[IMPORTANT]
====
OpenShift Container Platform does not set a default pid.available `evictionHard`.
====

[id="nodes-scheduler-taints-tolerations-about-seconds_{context}"]
== Understanding how to use toleration seconds to delay pod evictions

You can specify how long a pod can remain bound to a node before being evicted by specifying the `tolerationSeconds` parameter in the `Pod` specification or `MachineSet` object. If a taint with the `NoExecute` effect is added to a node, a pod that does tolerate the taint, which has the `tolerationSeconds` parameter, the pod is not evicted until that time period expires.

.Example output
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
----

Here, if this pod is running but does not have a matching toleration, the pod stays bound to the node for 3,600 seconds and then be evicted. If the taint is removed before that time, the pod is not evicted.

[id="nodes-scheduler-taints-tolerations-about-multiple_{context}"]
== Understanding how to use multiple taints

You can put multiple taints on the same node and multiple tolerations on the same pod. OpenShift Container Platform processes multiple taints and tolerations as follows:

. Process the taints for which the pod has a matching toleration.
. The remaining unmatched taints have the indicated effects on the pod:
+
* If there is at least one unmatched taint with effect `NoSchedule`, OpenShift Container Platform cannot schedule a pod onto that node.
* If there is no unmatched taint with effect `NoSchedule` but there is at least one unmatched taint with effect `PreferNoSchedule`, OpenShift Container Platform tries to not schedule the pod onto the node.
* If there is at least one unmatched taint with effect `NoExecute`, OpenShift Container Platform evicts the pod from the node if it is already running on the node, or the pod is not scheduled onto the node if it is not yet running on the node.
+
** Pods that do not tolerate the taint are evicted immediately.
+
** Pods that tolerate the taint without specifying `tolerationSeconds` in their `Pod` specification remain bound forever.
+
** Pods that tolerate the taint with a specified `tolerationSeconds` remain bound for the specified amount of time.

For example:

* Add the following taints to the node:
+
[source,terminal]
----
$ oc adm taint nodes node1 key1=value1:NoSchedule
----
+
[source,terminal]
----
$ oc adm taint nodes node1 key1=value1:NoExecute
----
+
[source,terminal]
----
$ oc adm taint nodes node1 key2=value2:NoSchedule
----

* The pod has the following tolerations:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoSchedule"
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
#...
----

In this case, the pod cannot be scheduled onto the node, because there is no toleration matching the third taint. The pod continues running if it is already running on the node when the taint is added, because the third taint is the only
one of the three that is not tolerated by the pod.

[id="nodes-scheduler-taints-tolerations-about-taintNodesByCondition_{context}"]
== Understanding pod scheduling and node conditions (taint node by condition)

The Taint Nodes By Condition feature, which is enabled by default, automatically taints nodes that report conditions such as memory pressure and disk pressure. If a node reports a condition, a taint is added until the condition clears. The taints have the `NoSchedule` effect, which means no pod can be scheduled on the node unless the pod has a matching toleration.

The scheduler checks for these taints on nodes before scheduling pods. If the taint is present, the pod is scheduled on a different node. Because the scheduler checks for taints and not the actual node conditions, you configure the scheduler to ignore some of these node conditions by adding appropriate pod tolerations.

To ensure backward compatibility, the daemon set controller automatically adds the following tolerations to all daemons:

* node.kubernetes.io/memory-pressure
* node.kubernetes.io/disk-pressure
* node.kubernetes.io/unschedulable (1.10 or later)
* node.kubernetes.io/network-unavailable (host network only)

You can also add arbitrary tolerations to daemon sets.

[NOTE]
====
The control plane also adds the `node.kubernetes.io/memory-pressure` toleration on pods that have a QoS class. This is because Kubernetes manages pods in the `Guaranteed` or `Burstable` QoS classes. The new `BestEffort` pods do not get scheduled onto the affected node.
====

[id="nodes-scheduler-taints-tolerations-about-taintBasedEvictions_{context}"]
== Understanding evicting pods by condition (taint-based evictions)

The Taint-Based Evictions feature, which is enabled by default, evicts pods from a node that experiences specific conditions, such as `not-ready` and `unreachable`.
When a node experiences one of these conditions, OpenShift Container Platform automatically adds taints to the node, and starts evicting and rescheduling the pods on different nodes.

Taint Based Evictions have a `NoExecute` effect, where any pod that does not tolerate the taint is evicted immediately and any pod that does tolerate the taint will never be evicted, unless the pod uses the `tolerationSeconds` parameter.

The `tolerationSeconds` parameter allows you to specify how long a pod stays bound to a node that has a node condition. If the condition still exists after the `tolerationSeconds` period, the taint remains on the node and the pods with a matching toleration are evicted. If the condition clears before the `tolerationSeconds` period, pods with matching tolerations are not removed.

If you use the `tolerationSeconds` parameter with no value, pods are never evicted because of the not ready and unreachable node conditions.

[NOTE]
====
OpenShift Container Platform evicts pods in a rate-limited way to prevent massive pod evictions in scenarios such as the master becoming partitioned from the nodes.

By default, if more than 55% of nodes in a given zone are unhealthy, the node lifecycle controller changes that zone's state to `PartialDisruption` and the rate of pod evictions is reduced. For small clusters (by default, 50 nodes or less) in this state, nodes in this zone are not tainted and evictions are stopped.

For more information, see "Rate limits on eviction" in the Kubernetes documentation.
====

OpenShift Container Platform automatically adds a toleration for `node.kubernetes.io/not-ready` and `node.kubernetes.io/unreachable` with `tolerationSeconds=300`, unless the `Pod` configuration specifies either toleration.

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: node.kubernetes.io/not-ready
    operator: Exists
    effect: NoExecute
    tolerationSeconds: 300
  - key: node.kubernetes.io/unreachable
    operator: Exists
    effect: NoExecute
    tolerationSeconds: 300
#...
----

These tolerations ensure that the default pod behavior is to remain bound for five minutes after one of these node conditions problems is detected.

You can configure these tolerations as needed. For example, if you have an application with a lot of local state, you might want to keep the pods bound to node for a longer time in the event of network partition, allowing for the partition to recover and avoiding pod eviction.

Pods spawned by a daemon set are created with `NoExecute` tolerations for the following taints with no `tolerationSeconds`:

* `node.kubernetes.io/unreachable`
* `node.kubernetes.io/not-ready`

As a result, daemon set pods are never evicted because of these node conditions.

[id="nodes-scheduler-taints-tolerations-all_{context}"]
== Tolerating all taints

You can configure a pod to tolerate all taints by adding an `operator: "Exists"` toleration with no `key` and `values` parameters.
Pods with this toleration are not removed from a node that has taints.

.`Pod` spec for tolerating all taints
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - operator: "Exists"
#...
----

// Module included in the following assemblies:
//
// * observability/logging/log_storage/cluster-logging-loki.adoc

[id="logging-loki-pod-placement_{context}"]
= Loki pod placement
You can control which nodes the Loki pods run on, and prevent other workloads from using those nodes, by using tolerations or node selectors on the pods.

You can apply tolerations to the log store pods with the LokiStack custom resource (CR) and apply taints to a node with the node specification. A taint on a node is a `key:value` pair that instructs the node to repel all pods that do not allow the taint. Using a specific `key:value` pair that is not on other pods ensures that only the log store pods can run on that node.

.Example LokiStack with node selectors
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
# ...
  template:
    compactor: # <1>
      nodeSelector:
        node-role.kubernetes.io/infra: "" # <2>
    distributor:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    gateway:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    indexGateway:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    ingester:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    querier:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    queryFrontend:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    ruler:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
# ...
----

<1> Specifies the component pod type that applies to the node selector.
<2> Specifies the pods that are moved to nodes containing the defined label.

In the previous example configuration, all Loki pods are moved to nodes containing the `node-role.kubernetes.io/infra: ""` label.

.Example LokiStack CR with node selectors and tolerations
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
# ...
  template:
    compactor:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    distributor:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    indexGateway:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    ingester:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    querier:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    queryFrontend:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    ruler:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
    gateway:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
        value: reserved
      - effect: NoExecute
        key: node-role.kubernetes.io/infra
        value: reserved
# ...
----

To configure the `nodeSelector` and `tolerations` fields of the LokiStack (CR), you can use the [command]`oc explain` command to view the description and fields for a particular resource:

[source,terminal]
----
$ oc explain lokistack.spec.template
----

.Example output
[source,text]
----
KIND:     LokiStack
VERSION:  loki.grafana.com/v1

RESOURCE: template <Object>

DESCRIPTION:
     Template defines the resource/limits/tolerations/nodeselectors per
     component

FIELDS:
   compactor	<Object>
     Compactor defines the compaction component spec.

   distributor	<Object>
     Distributor defines the distributor component spec.
...
----

For more detailed information, you can add a specific field:

[source,terminal]
----
$ oc explain lokistack.spec.template.compactor
----

.Example output
[source,text]
----
KIND:     LokiStack
VERSION:  loki.grafana.com/v1

RESOURCE: compactor <Object>

DESCRIPTION:
     Compactor defines the compaction component spec.

FIELDS:
   nodeSelector	<map[string]string>
     NodeSelector defines the labels required by a node to schedule the
     component onto it.
...
----

// Module included in the following assemblies:
//
// * observability/logging/scheduling_resources/logging-taints-tolerations.adoc

[id="cluster-logging-collector-tolerations_{context}"]
= Using tolerations to control log collector pod placement

By default, log collector pods have the following `tolerations` configuration:

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: collector-example
  namespace: openshift-logging
spec:
# ...
  collection:
    type: vector
    tolerations:
    - effect: NoSchedule
      key: node-role.kubernetes.io/master
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/disk-pressure
      operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/memory-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/pid-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/unschedulable
      operator: Exists
# ...
----

.Prerequisites

* You have installed the {clo} and {oc-first}.

.Procedure

. Add a taint to a node where you want logging collector pods to schedule logging collector pods by running the following command:
+
[source,terminal]
----
$ oc adm taint nodes <node_name> <key>=<value>:<effect>
----
+
.Example command
[source,terminal]
----
$ oc adm taint nodes node1 collector=node:NoExecute
----
+
This example places a taint on `node1` that has key `collector`, value `node`, and taint effect `NoExecute`. You must use the `NoExecute` taint effect. `NoExecute` schedules only pods that match the taint and removes existing pods that do not match.

. Edit the `collection` stanza of the `ClusterLogging` custom resource (CR) to configure a toleration for the logging collector pods:
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
# ...
spec:
# ...
  collection:
    type: vector
    tolerations:
    - key: collector <1>
      operator: Exists <2>
      effect: NoExecute <3>
      tolerationSeconds: 6000 <4>
    resources:
      limits:
        memory: 2Gi
      requests:
        cpu: 100m
        memory: 1Gi
# ...
----
<1> Specify the key that you added to the node.
<2> Specify the `Exists` operator to require the `key`/`value`/`effect` parameters to match.
<3> Specify the `NoExecute` effect.
<4> Optionally, specify the `tolerationSeconds` parameter to set how long a pod can remain bound to a node before being evicted.

This toleration matches the taint created by the `oc adm taint` command. A pod with this toleration can be scheduled onto `node1`.

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/log-forwarding.adoc

[id="log-collector-resources-scheduling_{context}"]
= Configuring resources and scheduling for logging collectors

Administrators can modify the resources or scheduling of the collector by creating a `ClusterLogging` custom resource (CR) that is in the same namespace and has the same name as the `ClusterLogForwarder` CR that it supports.

The applicable stanzas for the `ClusterLogging` CR when using multiple log forwarders in a deployment are `managementState` and `collection`. All other stanzas are ignored.

.Prerequisites

* You have administrator permissions.
* You have installed the {clo} version 5.8 or newer.
* You have created a `ClusterLogForwarder` CR.

.Procedure

. Create a `ClusterLogging` CR that supports your existing `ClusterLogForwarder` CR:
+
.Example `ClusterLogging` CR YAML
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name:  <name> # <1>
  namespace: <namespace> # <2>
spec:
  managementState: "Managed"
  collection:
    type: "vector"
    tolerations:
    - key: "logging"
      operator: "Exists"
      effect: "NoExecute"
      tolerationSeconds: 6000
    resources:
      limits:
        memory: 1Gi
      requests:
        cpu: 100m
        memory: 1Gi
    nodeSelector:
      collector: needed
# ...
----
<1> The name must be the same name as the `ClusterLogForwarder` CR.
<2> The namespace must be the same namespace as the `ClusterLogForwarder` CR.

. Apply the `ClusterLogging` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-collector.adoc

[id="cluster-logging-collector-pod-location_{context}"]
= Viewing logging collector pods

You can view the logging collector pods and the corresponding nodes that they are running on.

.Procedure

* Run the following command in a project to view the logging collector pods and their details:
+
[source,terminal]
----
$ oc get pods --selector component=collector -o wide -n <project_name>
----
+
.Example output
[source,terminal]
----
NAME           READY  STATUS    RESTARTS   AGE     IP            NODE                  NOMINATED NODE   READINESS GATES
collector-8d69v  1/1    Running   0          134m    10.130.2.30   master1.example.com   <none>           <none>
collector-bd225  1/1    Running   0          134m    10.131.1.11   master2.example.com   <none>           <none>
collector-cvrzs  1/1    Running   0          134m    10.130.0.21   master3.example.com   <none>           <none>
collector-gpqg2  1/1    Running   0          134m    10.128.2.27   worker1.example.com   <none>           <none>
collector-l9j7j  1/1    Running   0          134m    10.129.2.31   worker2.example.com   <none>           <none>
----

[role="_additional-resources"]
[id="additional-resources_cluster-logging-tolerations"]
== Additional resources
* Controlling pod placement using node taints
