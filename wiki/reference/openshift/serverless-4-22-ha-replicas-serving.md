---
title: "High availability for Knative services"
type: reference
domain: openshift
slug: serverless-4-22-ha-replicas-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/ha-replicas-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# High availability for Knative services

[id="ha-replicas-serving"]
= High availability for Knative services

High availability (HA) is available by default for the Knative Serving `activator`, `autoscaler`, `autoscaler-hpa`, `controller`, `webhook`, `kourier-control`, and `kourier-gateway` components, which are configured to have two replicas each by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeServing` custom resource (CR).

// Module included in the following assemblies:
//
// * /serverless/knative-serving/config-ha-services/ha-replicas-serving.adoc
// * /serverless/eventing/tuning/serverless-ha.adoc

[id="serverless-config-replicas-serving_{context}"]
= Configuring high availability replicas for Knative Serving

To specify three minimum replicas for the eligible deployment resources, set the value of the field `spec.high-availability.replicas` in the custom resource to `3`.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, navigate to *OperatorHub* -> *Installed Operators*.

. Select the `knative-serving` namespace.
+
. Click *Knative Serving* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Serving* tab.

. Click *knative-serving*, then go to the *YAML* tab in the *knative-serving* page.
+
image::serving-YAML-HA.png[Knative Serving YAML]

. Modify the number of replicas in the `KnativeServing` CR:
+
.Example YAML
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  high-availability:
    replicas: 3
----
