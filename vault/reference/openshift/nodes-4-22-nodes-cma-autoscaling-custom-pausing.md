---
title: "Pausing the custom metrics autoscaler for a scaled object"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-pausing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-pausing
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Pausing the custom metrics autoscaler for a scaled object

[id="nodes-cma-autoscaling-custom-pausing"]
= Pausing the custom metrics autoscaler for a scaled object

You can pause and restart the autoscaling of a workload, as needed.

For example, you might want to pause autoscaling before performing cluster maintenance or to avoid resource starvation by removing non-mission-critical workloads.

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-pausing.adoc

[id="nodes-cma-autoscaling-custom-pausing-workload_{context}"]
= Pausing a custom metrics autoscaler

You can pause the autoscaling of a scaled object by adding the `autoscaling.keda.sh/paused-replicas` annotation to the custom metrics autoscaler for that scaled object. The custom metrics autoscaler scales the replicas for that workload to the specified value and pauses autoscaling until the annotation is removed.

[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4"
# ...
----

.Procedure

. Use the following command to edit the `ScaledObject` CR for your workload:
+
[source,terminal]
----
$ oc edit ScaledObject scaledobject
----

. Add the `autoscaling.keda.sh/paused-replicas` annotation with any value:
+
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4" <1>
  creationTimestamp: "2023-02-08T14:41:01Z"
  generation: 1
  name: scaledobject
  namespace: my-project
  resourceVersion: '65729'
  uid: f5aec682-acdf-4232-a783-58b5b82f5dd0
----
<1> Specifies that the Custom Metrics Autoscaler Operator is to scale the replicas to the specified value and stop autoscaling.

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-pausing.adoc

[id="nodes-cma-autoscaling-custom-pausing-restart_{context}"]
= Restarting the custom metrics autoscaler for a scaled object

You can restart a paused custom metrics autoscaler by removing the `autoscaling.keda.sh/paused-replicas` annotation for that `ScaledObject`.

[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4"
# ...
----

.Procedure

. Use the following command to edit the `ScaledObject` CR for your workload:
+
[source,terminal]
----
$ oc edit ScaledObject scaledobject
----

. Remove the `autoscaling.keda.sh/paused-replicas` annotation.
+
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4" <1>
  creationTimestamp: "2023-02-08T14:41:01Z"
  generation: 1
  name: scaledobject
  namespace: my-project
  resourceVersion: '65729'
  uid: f5aec682-acdf-4232-a783-58b5b82f5dd0
----
<1> Remove this annotation to restart a paused custom metrics autoscaler.
