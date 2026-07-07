---
title: "Scale-to-zero"
type: reference
domain: openshift
slug: serverless-4-22-serverless-autoscaling-scale-to-zero
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-autoscaling-scale-to-zero
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Scale-to-zero

[id="serverless-autoscaling-scale-to-zero"]
= Scale-to-zero

Knative Serving provides automatic scaling, or _autoscaling_, for applications to match incoming demand.

// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-configuration.adoc

[id="serverless-enable-scale-to-zero_{context}"]
= Enabling scale-to-zero

You can use the `enable-scale-to-zero` spec to enable or disable scale-to-zero globally for applications on the cluster.

.Prerequisites

* You have installed {ServerlessOperatorName} and Knative Serving on your cluster.

* You have cluster administrator permissions.

* You have cluster or dedicated administrator permissions.

* You are using the default Knative Pod Autoscaler. The scale to zero feature is not available if you are using the Kubernetes Horizontal Pod Autoscaler.

.Procedure

* Modify the `enable-scale-to-zero` spec in the `KnativeServing` custom resource (CR):
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    autoscaler:
      enable-scale-to-zero: "false" <1>
----
<1> The `enable-scale-to-zero` spec can be either `"true"` or `"false"`. If set to true, scale-to-zero is enabled. If set to false, applications are scaled down to the configured _minimum scale bound_. The default value is `"true"`.

// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-configuration.adoc

[id="serverless-scale-to-zero-grace-period_{context}"]
= Configuring the scale-to-zero grace period

Knative Serving provides automatic scaling down to zero pods for applications. You can use the `scale-to-zero-grace-period` spec to define an upper bound time limit that Knative waits for scale-to-zero machinery to be in place before the last replica of an application is removed.

.Prerequisites

* You have installed {ServerlessOperatorName} and Knative Serving on your cluster.

* You have cluster administrator permissions.

* You have cluster or dedicated administrator permissions.

* You are using the default Knative Pod Autoscaler. The scale-to-zero feature is not available if you are using the Kubernetes Horizontal Pod Autoscaler.

.Procedure

* Modify the `scale-to-zero-grace-period` spec in the `KnativeServing` custom resource (CR):
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    autoscaler:
      scale-to-zero-grace-period: "30s" <1>
----
<1> The grace period time in seconds. The default value is 30 seconds.
