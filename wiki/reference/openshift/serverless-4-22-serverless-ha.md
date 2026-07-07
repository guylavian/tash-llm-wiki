---
title: "High availability"
type: reference
domain: openshift
slug: serverless-4-22-serverless-ha
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-ha
version: 4.22
family: serverless
documentKind: "Documentation"
---

# High availability

[id="serverless-ha"]
= High availability

HA in {ServerlessProductName} is available through leader election, which is enabled by default after the Knative Serving or Eventing control plane is installed. When using a leader election HA pattern, instances of controllers are already scheduled and running inside the cluster before they are required.
These controller instances compete to use a shared resource, known as the leader election lock. The instance of the controller that has access to the leader election lock resource at any given time is called the leader.

// Module included in the following assemblies:
//
// * /serverless/eventing/tuning/serverless-ha.adoc

[id="serverless-config-replicas-eventing_{context}"]
= Configuring high availability replicas for Knative Eventing

High availability (HA) is available by default for the Knative Eventing `eventing-controller`, `eventing-webhook`, `imc-controller`, `imc-dispatcher`, and `mt-broker-controller` components, which are configured to have two replicas each by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeEventing` custom resource (CR).

[NOTE]
====
For Knative Eventing, the `mt-broker-filter` and `mt-broker-ingress` deployments are not scaled by HA. If multiple deployments are needed, scale these components manually.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* The {ServerlessOperatorName} and Knative Eventing are installed on your cluster.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, navigate to *OperatorHub* -> *Installed Operators*.

. Select the `knative-eventing` namespace.

. Click *Knative Eventing* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Eventing* tab.

. Click *knative-eventing*, then go to the *YAML* tab in the *knative-eventing* page.
+
image::eventing-YAML-HA.png[Knative Eventing YAML]

. Modify the number of replicas in the `KnativeEventing` CR:
+
.Example YAML
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
  name: knative-eventing
  namespace: knative-eventing
spec:
  high-availability:
    replicas: 3
----
// Module included in the following assemblies:
//
// * /serverless/eventing/tuning/serverless-ha.adoc

[id="serverless-config-replicas-kafka_{context}"]
= Configuring high availability replicas for the Knative broker implementation for Apache Kafka

High availability (HA) is available by default for the Knative broker implementation for Apache Kafka components `kafka-controller` and `kafka-webhook-eventing`, which are configured to have two each replicas by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeKafka` custom resource (CR).

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* The {ServerlessOperatorName} and Knative broker for Apache Kafka are installed on your cluster.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, navigate to *OperatorHub* -> *Installed Operators*.

. Select the `knative-eventing` namespace.

. Click *Knative Kafka* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Kafka* tab.

. Click *knative-kafka*, then go to the *YAML* tab in the *knative-kafka* page.
+
image::kafka-YAML-HA.png[Knative Kafka YAML]

. Modify the number of replicas in the `KnativeKafka` CR:
+
.Example YAML
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  name: knative-kafka
  namespace: knative-eventing
spec:
  high-availability:
    replicas: 3
----
