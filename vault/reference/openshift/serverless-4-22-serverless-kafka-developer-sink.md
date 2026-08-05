---
title: "Sink for Apache Kafka"
type: reference
domain: openshift
slug: serverless-4-22-serverless-kafka-developer-sink
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-kafka-developer-sink
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Sink for Apache Kafka

[id="serverless-kafka-developer-sink"]
= Sink for Apache Kafka

Apache Kafka sinks are a type of event sink that are available if a cluster administrator has enabled Apache Kafka on your cluster. You can send events directly from an event source to a Kafka topic by using a Kafka sink.

// Kafka sink via YAML
// Module included in the following assemblies:
//
// * serverless/develop/serverless-kafka-developer.adoc

[id="serverless-kafka-sink_{context}"]
= Creating an Apache Kafka sink by using YAML

You can create a Kafka sink that sends events to a Kafka topic. By default, a Kafka sink uses the binary content mode, which is more efficient than the structured mode. To create a Kafka sink by using YAML, you must create a YAML file that defines a `KafkaSink` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource (CR) are installed on your cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have access to a Red Hat AMQ Streams (Kafka) cluster that produces the Kafka messages you want to import.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a `KafkaSink` object definition as a YAML file:
+
.Kafka sink YAML
[source,yaml]
----
apiVersion: eventing.knative.dev/v1alpha1
kind: KafkaSink
metadata:
  name: <sink-name>
  namespace: <namespace>
spec:
  topic: <topic-name>
  bootstrapServers:
   - <bootstrap-server>
----

. To create the Kafka sink, apply the `KafkaSink` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

. Configure an event source so that the sink is specified in its spec:
+
.Example of a Kafka sink connected to an API server source
[source,yaml]
----
apiVersion: sources.knative.dev/v1alpha2
kind: ApiServerSource
metadata:
  name: <source-name> <1>
  namespace: <namespace> <2>
spec:
  serviceAccountName: <service-account-name> <3>
  mode: Resource
  resources:
  - apiVersion: v1
    kind: Event
  sink:
    ref:
      apiVersion: eventing.knative.dev/v1alpha1
      kind: KafkaSink
      name: <sink-name> <4>
----
<1> The name of the event source.
<2> The namespace of the event source.
<3> The service account for the event source.
<4> The Kafka sink name.

// Creating a Kafka sink via ODC
// Module included in the following assemblies:
//
// * serverless/eventing/event-sinks/serverless-kafka-developer-sink.adoc

[id="serverless-creating-a-kafka-event-sink_{context}"]
= Creating an event sink for Apache Kafka by using the OpenShift Container Platform web console

You can create a Kafka sink that sends events to a Kafka topic by using the *Developer* perspective in the OpenShift Container Platform web console. By default, a Kafka sink uses the binary content mode, which is more efficient than the structured mode.

As a developer, you can create an event sink to receive events from a particular source and send them to a Kafka topic.

.Prerequisites

* You have installed the {ServerlessOperatorName}, with Knative Serving, Knative Eventing, and Knative broker for Apache Kafka APIs, from the software catalog.
* You have created a Kafka topic in your Kafka environment.

.Procedure

. In the *Developer* perspective, navigate to the *+Add* view.
. Click *Event Sink* in the *Eventing catalog*.
. Search for `KafkaSink` in the catalog items and click it.
. Click *Create Event Sink*.
. In the form view, type the URL of the bootstrap server, which is a combination of host name and port.
+
image::create-event-sink.png[]

. Type the name of the topic to send event data.
. Type the name of the event sink.
. Click *Create*.

.Verification

. In the *Developer* perspective, navigate to the *Topology* view.
. Click the created event sink to view its details in the right panel.

// kafka sink security config
// Module is included in the following assemblies:
//
// * serverless/admin_guide/serverless-kafka-admin.adoc

[id="serverless-kafka-sink-security-config_{context}"]
= Configuring security for Apache Kafka sinks

_Transport Layer Security_ (TLS) is used by Apache Kafka clients and servers to encrypt traffic between Knative and Kafka, as well as for authentication. TLS is the only supported method of traffic encryption for the Knative broker implementation for Apache Kafka.

_Simple Authentication and Security Layer_ (SASL) is used by Apache Kafka for authentication. If you use SASL authentication on your cluster, users must provide credentials to Knative for communicating with the Kafka cluster; otherwise events cannot be produced or consumed.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resources (CRs) are installed on your OpenShift Container Platform cluster.
* Kafka sink is enabled in the `KnativeKafka` CR.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have a Kafka cluster CA certificate stored as a `.pem` file.
* You have a Kafka cluster client certificate and a key stored as `.pem` files.
* You have installed the OpenShift (`oc`) CLI.
* You have chosen the SASL mechanism to use, for example, `PLAIN`, `SCRAM-SHA-256`, or `SCRAM-SHA-512`.

.Procedure

. Create the certificate files as a secret in the same namespace as your `KafkaSink` object:
+
[IMPORTANT]
====
Certificates and keys must be in PEM format.
====

** For authentication using SASL without encryption:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <secret_name> \
  --from-literal=protocol=SASL_PLAINTEXT \
  --from-literal=sasl.mechanism=<sasl_mechanism> \
  --from-literal=user=<username> \
  --from-literal=password=<password>
----

** For authentication using SASL and encryption using TLS:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <secret_name> \
  --from-literal=protocol=SASL_SSL \
  --from-literal=sasl.mechanism=<sasl_mechanism> \
  --from-file=ca.crt=<my_caroot.pem_file_path> \ <1>
  --from-literal=user=<username> \
  --from-literal=password=<password>
----
<1> The `ca.crt` can be omitted to use the system's root CA set if you are using a public cloud managed Kafka service.

** For authentication and encryption using TLS:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <secret_name> \
  --from-literal=protocol=SSL \
  --from-file=ca.crt=<my_caroot.pem_file_path> \ <1>
  --from-file=user.crt=<my_cert.pem_file_path> \
  --from-file=user.key=<my_key.pem_file_path>
----
<1> The `ca.crt` can be omitted to use the system's root CA set if you are using a public cloud managed Kafka service.

. Create or modify a `KafkaSink` object and add a reference to your secret in the `auth` spec:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1alpha1
kind: KafkaSink
metadata:
   name: <sink_name>
   namespace: <namespace>
spec:
...
   auth:
     secret:
       ref:
         name: <secret_name>
...
----

. Apply the `KafkaSink` object:
+
[source,terminal]
----
$ oc apply -f <filename>
----
