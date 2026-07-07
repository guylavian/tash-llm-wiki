---
title: "Configuring quotas"
type: reference
domain: openshift
slug: ai-workloads-4-22-configuring-quotas
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/configuring-quotas
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Configuring quotas

[id="configuring-quotas"]
= Configuring quotas

As an administrator, you can use {kueue-name} to configure quotas to optimize resource allocation and system throughput for user workloads.
You can configure quotas for compute resources such as CPU, memory, pods, and GPU.

You can configure quotas in {kueue-name} by completing the following steps:

. Configure a cluster queue.
. Configure a resource flavor.
. Configure a local queue.

Users can then submit their workloads to the local queue.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/configuring-quotas.adoc

[id="configuring-clusterqueues_{context}"]
= Configuring a cluster queue

A cluster queue is a cluster-scoped resource, represented by a `ClusterQueue` object, that governs a pool of resources such as CPU, memory, and pods.
Cluster queues can be used to define usage limits, quotas for resource flavors, order of consumption, and fair sharing rules.

[NOTE]
====
The cluster queue is not ready for use until a `ResourceFlavor` object has also been configured.
====

.Prerequisites

.Procedure

. Create a `ClusterQueue` object as a YAML file:
+
.Example of a basic `ClusterQueue` object using a single resource flavor
[source,yaml]
----
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: cluster-queue
spec:
  namespaceSelector: {} # <1>
  resourceGroups:
  - coveredResources: ["cpu", "memory", "pods", "foo.com/gpu"] # <2>
    flavors:
    - name: "default-flavor" # <3>
      resources: # <4>
      - name: "cpu"
        nominalQuota: 9
      - name: "memory"
        nominalQuota: 36Gi
      - name: "pods"
        nominalQuota: 5
      - name: "foo.com/gpu"
        nominalQuota: 100
----
<1> Defines which namespaces can use the resources governed by this cluster queue. An empty `namespaceSelector` as shown in the example means that all namespaces can use these resources.
<2> Defines the resource types governed by the cluster queue. This example `ClusterQueue` object governs CPU, memory, pod, and GPU resources.
<3> Defines the resource flavor that is applied to the resource types listed. In this example, the `default-flavor` resource flavor is applied to CPU, memory, pod, and GPU resources.
<4> Defines the resource requirements for admitting jobs. This example cluster queue only admits jobs if the following conditions are met:
+
* The sum of the CPU requests is less than or equal to 9.
* The sum of the memory requests is less than or equal to 36Gi.
* The total number of pods is less than or equal to 5.
* The sum of the GPU requests is less than or equal to 100.

. Apply the `ClusterQueue` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

[role="_next-steps"]
[id="clusterqueues-next-steps_{context}"]
.Next steps

The cluster queue is not ready for use until a `ResourceFlavor` object has also been configured.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/configuring-quotas.adoc

[id="configuring-resourceflavors_{context}"]
= Configuring a resource flavor

After you have configured a `ClusterQueue` object, you can configure a `ResourceFlavor` object.

Resources in a cluster are typically not homogeneous. If the resources in your cluster are homogeneous, you can use an empty `ResourceFlavor` instead of adding labels to custom resource flavors.

You can use a custom `ResourceFlavor` object to represent different resource variations that are associated with cluster nodes through labels, taints, and tolerations. You can then associate workloads with specific node types to enable fine-grained resource management.

.Prerequisites

.Procedure

. Create a `ResourceFlavor` object as a YAML file:
+
.Example of an empty `ResourceFlavor` object
[source,yaml]
----
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: default-flavor
----
+
.Example of a custom `ResourceFlavor` object
[source,yaml]
----
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: "x86"
spec:
  nodeLabels:
    cpu-arch: x86
----

. Apply the `ResourceFlavor` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * ai_workloads/kueue/configuring-quotas.adoc

[id="configuring-localqueues_{context}"]
= Configuring a local queue

A local queue is a namespaced object, represented by a `LocalQueue` object, that groups closely related workloads that belong to a single namespace.

As an administrator, you can configure a `LocalQueue` object to point to a cluster queue. This allocates resources from the cluster queue to workloads in the namespace specified in the `LocalQueue` object.

.Prerequisites

* You have created a `ClusterQueue` object.

.Procedure

. Create a `LocalQueue` object as a YAML file:
+
.Example of a basic `LocalQueue` object
[source,yaml]
----
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: team-namespace
  name: user-queue
spec:
  clusterQueue: cluster-queue
----

. Apply the `LocalQueue` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * ai_workloads/kueue/configuring-quotas.adoc

[id="configuring-localqueue-defaults_{context}"]
= Configuring a default local queue

As a cluster administrator, you can improve quota enforcement in your cluster by managing all jobs in selected namespaces without needing to explicitly label each job. You can do this by creating a default local queue.

A default local queue serves as the local queue for newly created jobs that do not have the `kueue.x-k8s.io/queue-name` label. After you create a default local queue, any new jobs created in the namespace without a `kueue.x-k8s.io/queue-name` label automatically update to have the `kueue.x-k8s.io/queue-name: default` label.

[IMPORTANT]
====
Preexisting jobs in a namespace are not affected when you create a default local queue. If jobs already exist in the namespace before you create the default local queue, you must label those jobs explicitly to assign them to a queue.
====

.Prerequisites

* You have created a `ClusterQueue` object.

.Procedure

. Create a `LocalQueue` object named `default` as a YAML file:
+
.Example of a default `LocalQueue` object
[source,yaml]
----
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: team-namespace
  name: default
spec:
  clusterQueue: cluster-queue
----

. Apply the `LocalQueue` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

. Create a job in the same namespace as the default local queue.
. Observe that the job updates with the `kueue.x-k8s.io/queue-name: default` label.

[role="_additional-resources"]
[id="clusterqueues-additional-resources_{context}"]
== Additional resources
* RBAC permissions
* Kubernetes documentation about cluster queues
