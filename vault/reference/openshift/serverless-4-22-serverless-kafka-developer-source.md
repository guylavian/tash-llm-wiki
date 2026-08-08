---
title: "Source for Apache Kafka"
type: reference
domain: openshift
slug: serverless-4-22-serverless-kafka-developer-source
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-kafka-developer-source
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Source for Apache Kafka

[id="serverless-kafka-developer-source"]
= Source for Apache Kafka

You can create an Apache Kafka source that reads events from an Apache Kafka cluster and passes these events to a sink. You can create a Kafka source by using the OpenShift Container Platform web console, the Knative (`kn`) CLI, or by creating a `KafkaSource` object directly as a YAML file and using the OpenShift CLI (`oc`) to apply it.

[NOTE]
====
See the documentation for Installing Knative broker for Apache Kafka.
====

// dev console
// Module included in the following assemblies:
//
// * serverless/develop/serverless-kafka-developer.adoc

[id="serverless-kafka-source-odc_{context}"]
= Creating an Apache Kafka event source by using the web console

After the Knative broker implementation for Apache Kafka is installed on your cluster, you can create an Apache Kafka source by using the web console. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a Kafka source.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your cluster.
* You have logged in to the web console.
* You have access to a Red Hat AMQ Streams (Kafka) cluster that produces the Kafka messages you want to import.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. In the *Developer* perspective, navigate to the *+Add* page and select *Event Source*.
. In the *Event Sources* page, select *Kafka Source* in the *Type* section.
. Configure the *Kafka Source* settings:
.. Add a comma-separated list of *Bootstrap Servers*.
.. Add a comma-separated list of *Topics*.
.. Add a *Consumer Group*.
.. Select the *Service Account Name* for the service account that you created.
.. Select the *Sink* for the event source. A *Sink* can be either a *Resource*, such as a channel, broker, or service, or a *URI*.
.. Enter a *Name* for the Kafka event source.
. Click *Create*.

.Verification

You can verify that the Kafka event source was created and is connected to the sink by viewing the *Topology* page.

. In the *Developer* perspective, navigate to *Topology*.
. View the Kafka event source and sink.
+
image::verify-kafka-ODC.png[View the Kafka source and service in the Topology view]
// kn commands
// Module included in the following assemblies:
//
// * serverless/develop/serverless-kafka-developer.adoc
// * serverless/reference/kn-eventing-ref.adoc

[id="serverless-kafka-source-kn_{context}"]
= Creating an Apache Kafka event source by using the Knative CLI

You can use the `kn source kafka create` command to create a Kafka source by using the Knative (`kn`) CLI. Using the Knative CLI to create event sources provides a more streamlined and intuitive user interface than modifying YAML files directly.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, Knative Serving, and the `KnativeKafka` custom resource (CR) are installed on your cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have access to a Red Hat AMQ Streams (Kafka) cluster that produces the Kafka messages you want to import.
* You have installed the Knative (`kn`) CLI.
* Optional: You have installed the OpenShift CLI (`oc`) if you want to use the verification steps in this procedure.

.Procedure

. To verify that the Kafka event source is working, create a Knative service that dumps incoming events into the service logs:
+
[source,terminal]
----
$ kn service create event-display \
    --image quay.io/openshift-knative/knative-eventing-sources-event-display
----

. Create a `KafkaSource` CR:
+
[source,terminal]
----
$ kn source kafka create <kafka_source_name> \
    --servers <cluster_kafka_bootstrap>.kafka.svc:9092 \
    --topics <topic_name> --consumergroup my-consumer-group \
    --sink event-display
----
+
[NOTE]
====
Replace the placeholder values in this command with values for your source name, bootstrap servers, and topics.
====
+
The `--servers`, `--topics`, and `--consumergroup` options specify the connection parameters to the Kafka cluster. The `--consumergroup` option is optional.

. Optional: View details about the `KafkaSource` CR you created:
+
[source,terminal]
----
$ kn source kafka describe <kafka_source_name>
----
+
.Example output
[source,terminal]
----
Name:              example-kafka-source
Namespace:         kafka
Age:               1h
BootstrapServers:  example-cluster-kafka-bootstrap.kafka.svc:9092
Topics:            example-topic
ConsumerGroup:     example-consumer-group

Sink:
  Name:       event-display
  Namespace:  default
  Resource:   Service (serving.knative.dev/v1)

Conditions:
  OK TYPE            AGE REASON
  ++ Ready            1h
  ++ Deployed         1h
  ++ SinkProvided     1h
----

.Verification steps

. Trigger the Kafka instance to send a message to the topic:
+
[source,terminal]
----
$ oc -n kafka run kafka-producer \
    -ti --image=quay.io/strimzi/kafka:latest-kafka-2.7.0 --rm=true \
    --restart=Never -- bin/kafka-console-producer.sh \
    --broker-list <cluster_kafka_bootstrap>:9092 --topic my-topic
----
+
Enter the message in the prompt. This command assumes that:
+
* The Kafka cluster is installed in the `kafka` namespace.
* The `KafkaSource` object has been configured to use the `my-topic` topic.

. Verify that the message arrived by viewing the logs:
+
[source,terminal]
----
$ oc logs $(oc get pod -o name | grep event-display) -c user-container
----
+
.Example output
[source,terminal]
----
☁️  cloudevents.Event
Validation: valid
Context Attributes,
  specversion: 1.0
  type: dev.knative.kafka.event
  source: /apis/v1/namespaces/default/kafkasources/example-kafka-source#example-topic
  subject: partition:46#0
  id: partition:46/offset:0
  time: 2021-03-10T11:21:49.4Z
Extensions,
  traceparent: 00-161ff3815727d8755848ec01c866d1cd-7ff3916c44334678-00
Data,
  Hello!
----
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-event-sinks.adoc
// * serverless/eventing/event-sources/serverless-apiserversource.adoc
// * serverless/eventing/event-sources/serverless-custom-event-sources.adoc
// * serverless/develop/serverless-kafka-developer.adoc
// * serverless/reference/kn-flags-reference.adoc

[id="specifying-sink-flag-kn_{context}"]
= Knative CLI sink flag

When you create an event source by using the Knative (`kn`) CLI, you can specify a sink where events are sent to from that resource by using the `--sink` flag. The sink can be any addressable or callable resource that can receive incoming events from other resources.

The following example creates a sink binding that uses a service, `\http://event-display.svc.cluster.local`, as the sink:

.Example command using the sink flag
[source,terminal]
----
$ kn source binding create bind-heartbeat \
  --namespace sinkbinding-example \
  --subject "Job:batch/v1:app=heartbeat-cron" \
  --sink http://event-display.svc.cluster.local \ <1>
  --ce-override "sink=bound"
----
<1> `svc` in `\http://event-display.svc.cluster.local` determines that the sink is a Knative service. Other default sink prefixes include `channel`, and `broker`.
// YAML
// Module included in the following assemblies:
//
// * serverless/develop/serverless-kafka-developer.adoc

[id="serverless-kafka-source-yaml_{context}"]
= Creating an Apache Kafka event source by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe applications declaratively and in a reproducible manner. To create a Kafka source by using YAML, you must create a YAML file that defines a `KafkaSource` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have access to a Red Hat AMQ Streams (Kafka) cluster that produces the Kafka messages you want to import.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a `KafkaSource` object as a YAML file:
+
[source,yaml]
----
apiVersion: sources.knative.dev/v1beta1
kind: KafkaSource
metadata:
  name: <source_name>
spec:
  consumerGroup: <group_name> <1>
  bootstrapServers:
  - <list_of_bootstrap_servers>
  topics:
  - <list_of_topics> <2>
  sink:
  - <list_of_sinks> <3>
----
<1> A consumer group is a group of consumers that use the same group ID, and consume data from a topic.
<2> A topic provides a destination for the storage of data. Each topic is split into one or more partitions.
<3> A sink specifies where events are sent to from a source.
+
[IMPORTANT]
====
Only the `v1beta1` version of the API for `KafkaSource` objects on {ServerlessProductName} is supported. Do not use the `v1alpha1` version of this API, as this version is now deprecated.
====
+
.Example `KafkaSource` object
[source,yaml]
----
apiVersion: sources.knative.dev/v1beta1
kind: KafkaSource
metadata:
  name: kafka-source
spec:
  consumerGroup: knative-group
  bootstrapServers:
  - my-cluster-kafka-bootstrap.kafka:9092
  topics:
  - knative-demo-topic
  sink:
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: event-display
----

. Apply the `KafkaSource` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

.Verification

* Verify that the Kafka event source was created by entering the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                    READY     STATUS    RESTARTS   AGE
kafkasource-kafka-source-5ca0248f-...   1/1       Running   0          13m
----

// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-kafka-admin.adoc

[id="serverless-kafka-sasl-source_{context}"]
= Configuring SASL authentication for Apache Kafka sources

_Simple Authentication and Security Layer_ (SASL) is used by Apache Kafka for authentication. If you use SASL authentication on your cluster, users must provide credentials to Knative for communicating with the Kafka cluster; otherwise events cannot be produced or consumed.

.Prerequisites

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.
* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` CR are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have a username and password for a Kafka cluster.
* You have chosen the SASL mechanism to use, for example, `PLAIN`, `SCRAM-SHA-256`, or `SCRAM-SHA-512`.
* If TLS is enabled, you also need the `ca.crt` certificate file for the Kafka cluster.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Create the certificate files as secrets in your chosen namespace:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <kafka_auth_secret> \
  --from-file=ca.crt=caroot.pem \
  --from-literal=password="SecretPassword" \
  --from-literal=saslType="SCRAM-SHA-512" \ <1>
  --from-literal=user="my-sasl-user"
----
<1> The SASL type can be `PLAIN`, `SCRAM-SHA-256`, or `SCRAM-SHA-512`.

. Create or modify your Kafka source so that it contains the following `spec` configuration:
+
[source,yaml]
----
apiVersion: sources.knative.dev/v1beta1
kind: KafkaSource
metadata:
  name: example-source
spec:
...
  net:
    sasl:
      enable: true
      user:
        secretKeyRef:
          name: <kafka_auth_secret>
          key: user
      password:
        secretKeyRef:
          name: <kafka_auth_secret>
          key: <password>
      type:
        secretKeyRef:
          name: <kafka_auth_secret>
          key: saslType
    tls:
      enable: true
      caCert: <1>
        secretKeyRef:
          name: <kafka_auth_secret>
          key: ca.crt
...
----
<1> The `caCert` spec is not required if you are using a public cloud Kafka service.
