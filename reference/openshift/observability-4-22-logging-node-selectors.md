---
title: "Using node selectors to move logging resources"
type: reference
domain: openshift
slug: observability-4-22-logging-node-selectors
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-node-selectors
version: 4.22
family: observability
documentKind: "Documentation"
---

# Using node selectors to move logging resources

[id="logging-node-selectors"]
= Using node selectors to move logging resources

// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-selector.adoc
// * observability/logging/scheduling_resources/logging-node-selectors.adoc

[id="nodes-scheduler-node-selectors-about_{context}"]
= About node selectors

[role="_abstract"]
You can use node selectors on pods and labels on nodes to control where the pod is scheduled. With node selectors, OpenShift Container Platform schedules the pods on nodes that contain matching labels.

You can use a node selector to place specific pods on specific nodes, cluster-wide node selectors to place new pods on specific nodes anywhere in the cluster, and project node selectors to place new pods in a project on specific nodes.

For example, as a cluster administrator, you can create an infrastructure where application developers can deploy pods only onto the nodes closest to their geographical location by including a node selector in every pod they create. In this example, the cluster consists of five data centers spread across two regions. In the U.S., label the nodes as `us-east`, `us-central`, or `us-west`. In the Asia-Pacific region (APAC), label the nodes as `apac-east` or `apac-west`. The developers can add a node selector to the pods they create to ensure the pods get scheduled on those nodes.

A pod is not scheduled if the `Pod` object contains a node selector, but no node has a matching label.

[IMPORTANT]
====
If you are using node selectors and node affinity in the same pod configuration, the following rules control pod placement onto nodes:

* If you configure both `nodeSelector` and `nodeAffinity`, both conditions must be satisfied for the pod to be scheduled onto a candidate node.

* If you specify multiple `nodeSelectorTerms` associated with `nodeAffinity` types, then the pod can be scheduled onto a node if one of the `nodeSelectorTerms` is satisfied.

* If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.
====

Node selectors on specific pods and nodes::
+
You can control which node a specific pod is scheduled on by using node selectors and labels.
+
To use node selectors and labels, first label the node to avoid pods being descheduled, then add the node selector to the pod.
+
[NOTE]
====
You cannot add a node selector directly to an existing scheduled pod. You must label the object that controls the pod, such as deployment config.
====
+
For example, the following `Node` object has the `region: east` label:
+
.Sample `Node` object with a label
[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: ip-10-0-131-14.ec2.internal
  selfLink: /api/v1/nodes/ip-10-0-131-14.ec2.internal
  uid: 7bc2580a-8b8e-11e9-8e01-021ab4174c74
  resourceVersion: '478704'
  creationTimestamp: '2019-06-10T14:46:08Z'
  labels:
    kubernetes.io/os: linux
    topology.kubernetes.io/zone: us-east-1a
    node.openshift.io/os_version: '4.5'
    node-role.kubernetes.io/worker: ''
    topology.kubernetes.io/region: us-east-1
    node.openshift.io/os_id: rhcos
    node.kubernetes.io/instance-type: m4.large
    kubernetes.io/hostname: ip-10-0-131-14
    kubernetes.io/arch: amd64
    region: east
    type: user-node
#...
----
+
In this example, the `region: east` and `type: user-node` labels must match the pod node selector.
.Sample `Node` object with a label
[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: s1
  selfLink: /api/v1/nodes/ip-10-0-131-14.ec2.internal
  uid: 7bc2580a-8b8e-11e9-8e01-021ab4174c74
  resourceVersion: '478704'
  creationTimestamp: '2019-06-10T14:46:08Z'
  labels:
    kubernetes.io/os: linux
    topology.kubernetes.io/zone: us-east-1a
    node.openshift.io/os_version: '4.5'
    node-role.kubernetes.io/worker: ''
    topology.kubernetes.io/region: us-east-1
    node.openshift.io/os_id: fedora
    node.kubernetes.io/instance-type: m4.large
    kubernetes.io/hostname: ip-10-0-131-14
    kubernetes.io/arch: amd64
    region: east
    type: user-node
#...
----
+
In this example, the `region: east` and `type: user-node` labels must match the pod node selector.
+
A pod has the `type: user-node,region: east` node selector:
+
.Sample `Pod` object with node selectors
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: s1
#...
spec:
  nodeSelector:
    region: east
    type: user-node
#...
----
where:
+
--
`spec.nodeSelector`:: Specifies the node selectors to match the node label. The node must have a label for each node selector.
--
+
When you create the pod using the example pod spec, it can be scheduled on the example node.

Default cluster-wide node selectors::
+
With default cluster-wide node selectors, when you create a pod in that cluster, OpenShift Container Platform adds the default node selectors to the pod and schedules
the pod on nodes with matching labels.
+
For example, the following `Scheduler` object has the default cluster-wide `region=east` and `type=user-node` node selectors:
+
.Example Scheduler Operator Custom Resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
#...
spec:
  defaultNodeSelector: type=user-node,region=east
#...
----
+
A node in that cluster has the `type=user-node,region=east` labels:
+
.Example `Node` object
[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  name: ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4
#...
  labels:
    region: east
    type: user-node
#...
----
+
.Example `Pod` object with a node selector
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: s1
#...
spec:
  nodeSelector:
    region: east
#...
----
+
When you create the pod using the example pod spec in the example cluster, the pod is created with the cluster-wide node selector and is scheduled on the labeled node:
+
[source,terminal]
.Example pod list with the pod on the labeled node
----
NAME     READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
pod-s1   1/1     Running   0          20s   10.131.2.6   ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4   <none>           <none>
----
+
[NOTE]
====
If the project where you create the pod has a project node selector, that selector takes preference over a cluster-wide node selector. Your pod is not created or scheduled if the pod does not have the project node selector.
====

[id="project-node-selectors_{context}"]
Project node selectors::
+
With project node selectors, when you create a pod in this project, OpenShift Container Platform adds the node selectors to the pod and schedules the pods on a node with matching labels. If there is a cluster-wide default node selector, a project node selector takes preference.
+
For example, the following project has the `region=east` node selector:
+
.Example `Namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: east-region
  annotations:
    openshift.io/node-selector: "region=east"
#...
----
+
The following node has the `type=user-node,region=east` labels:
+
.Example `Node` object
[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  name: ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4
#...
  labels:
    region: east
    type: user-node
#...
----
+
When you create the pod using the example pod spec in this example project, the pod is created with the project node selectors and is scheduled on the labeled node:
+
.Example `Pod` object
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  namespace: east-region
#...
spec:
  nodeSelector:
    region: east
    type: user-node
#...
----
+
[source,terminal]
.Example pod list with the pod on the labeled node
----
NAME     READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
pod-s1   1/1     Running   0          20s   10.131.2.6   ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4   <none>           <none>
----
+
A pod in the project is not created or scheduled if the pod contains different node selectors. For example, if you deploy the following pod into the example project, it is not created:
+
.Example `Pod` object with an invalid node selector
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: west-region
#...
spec:
  nodeSelector:
    region: west
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
[id="additional-resources_logging-node-selection"]
== Additional resources
* Placing pods on specific nodes using node selectors
