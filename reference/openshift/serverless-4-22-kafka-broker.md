---
title: "Knative broker implementation for Apache Kafka"
type: reference
domain: openshift
slug: serverless-4-22-kafka-broker
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kafka-broker
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Knative broker implementation for Apache Kafka

[id="kafka-broker"]
= Knative broker implementation for Apache Kafka

[id="creating-kafka-broker"]
== Creating an Apache Kafka broker when it is not configured as the default broker type

If your {ServerlessProductName} deployment is not configured to use Kafka broker as the default broker type, you can use one of the following procedures to create a Kafka-based broker.

// Module included in the following assemblies:
//
// * serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-kafka-broker_{context}"]
= Creating an Apache Kafka broker by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe applications declaratively and in a reproducible manner. To create a Kafka broker by using YAML, you must create a YAML file that defines a `Broker` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your OpenShift Container Platform cluster.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a Kafka-based broker as a YAML file:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  annotations:
    eventing.knative.dev/broker.class: Kafka <1>
  name: example-kafka-broker
spec:
  config:
    apiVersion: v1
    kind: ConfigMap
    name: kafka-broker-config <2>
    namespace: knative-eventing
----
<1> The broker class. If not specified, brokers use the default class as configured by cluster administrators. To use the Kafka broker, this value must be `Kafka`.
<2> The default config map for Knative brokers for Apache Kafka. This config map is created when the Kafka broker functionality is enabled on the cluster by a cluster administrator.

. Apply the Kafka-based broker YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
// Module included in the following assemblies:
//
// * serverless/eventing/brokers/serverless-using-brokers.adoc

[id="serverless-kafka-broker-with-kafka-topic_{context}"]
= Creating an Apache Kafka broker that uses an externally managed Kafka topic

If you want to use a Kafka broker without allowing it to create its own internal topic, you can use an externally managed Kafka topic instead. To do this, you must create a Kafka `Broker` object that uses the `kafka.eventing.knative.dev/external.topic` annotation.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your OpenShift Container Platform cluster.

* You have access to a Kafka instance such as Red Hat AMQ Streams, and have created a Kafka topic.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a Kafka-based broker as a YAML file:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  annotations:
    eventing.knative.dev/broker.class: Kafka <1>
    kafka.eventing.knative.dev/external.topic: <topic_name> <2>
...
----
<1> The broker class. If not specified, brokers use the default class as configured by cluster administrators. To use the Kafka broker, this value must be `Kafka`.
<2> The name of the Kafka topic that you want to use.

. Apply the Kafka-based broker YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
// Module included in the following assemblies:
//
// * serverless/eventing/brokers/kafka-broker.adoc

[id="serverless-kafka-broker-with-isolated-dataplane_{context}"]
= Knative Broker implementation for Apache Kafka with isolated data plane

The Knative Broker implementation for Apache Kafka has 2 planes:

Control plane:: Consists of controllers that talk to the Kubernetes API, watch for custom objects, and manage the data plane.

Data plane:: The collection of components that listen for incoming events, talk to Apache Kafka, and send events to the event sinks. The Knative Broker implementation for Apache Kafka data plane is where events flow. The implementation consists of `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments.

When you configure a Broker class of `Kafka`, the Knative Broker implementation for Apache Kafka uses a shared data plane. This means that the `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments in the `knative-eventing` namespace are used for all Apache Kafka Brokers in the cluster.

However, when you configure a Broker class of `KafkaNamespaced`, the Apache Kafka broker controller creates a new data plane for each namespace where a broker exists. This data plane is used by all `KafkaNamespaced` brokers in that namespace. This provides isolation between the data planes, so that the `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments in the user namespace are only used for the broker in that namespace.

[IMPORTANT]
====
As a consequence of having separate data planes, this security feature creates more deployments and uses more resources. Unless you have such isolation requirements, use a *regular* Broker with a class of `Kafka`.
====
// Module included in the following assemblies:
//
// * serverless/eventing/brokers/kafka-broker.adoc

[id="serverless-create-kafka-namespaced-broker_{context}"]
= Creating a Knative broker for Apache Kafka that uses an isolated data plane

To create a `KafkaNamespaced` broker, you must set the `eventing.knative.dev/broker.class` annotation to `KafkaNamespaced`.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your OpenShift Container Platform cluster.

* You have access to an Apache Kafka instance, such as Red Hat AMQ Streams, and have created a Kafka topic.

* You have created a project, or have access to a project, with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create an Apache Kafka-based broker by using a YAML file:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  annotations:
    eventing.knative.dev/broker.class: KafkaNamespaced <1>
  name: default
  namespace: my-namespace <2>
spec:
  config:
    apiVersion: v1
    kind: ConfigMap
    name: my-config <2>
...
----
<1> To use the Apache Kafka broker with isolated data planes, the broker class value must be `KafkaNamespaced`.
<2> The referenced `ConfigMap` object `my-config` must be in the same namespace as the `Broker` object, in this case `my-namespace`.

. Apply the Apache Kafka-based broker YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

[IMPORTANT]
====
The `ConfigMap` object in `spec.config` must be in the same namespace as the `Broker` object:

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
  namespace: my-namespace
data:
  ...
----
====

After the creation of the first `Broker` object with the `KafkaNamespaced` class, the `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments are created in the namespace. Subsequently, all brokers with the `KafkaNamespaced` class in the same namespace will use the same data plane. If no brokers with the `KafkaNamespaced` class exist in the namespace, the data plane in the namespace is deleted.

// kafka broker general configmap
// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/kafka-broker.adoc

[id="serverless-kafka-broker-configmap_{context}"]
= Configuring Apache Kafka broker settings

You can configure the replication factor, bootstrap servers, and the number of topic partitions for a Kafka broker, by creating a config map and referencing this config map in the Kafka `Broker` object.

.Prerequisites

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.
* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource (CR) are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project that has the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Modify the `kafka-broker-config` config map, or create your own config map that contains the following configuration:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: <config_map_name> <1>
  namespace: <namespace> <2>
data:
  default.topic.partitions: <integer> <3>
  default.topic.replication.factor: <integer> <4>
  bootstrap.servers: <list_of_servers> <5>
----
<1> The config map name.
<2> The namespace where the config map exists.
<3> The number of topic partitions for the Kafka broker. This controls how quickly events can be sent to the broker. A higher number of partitions requires greater compute resources.
<4> The replication factor of topic messages. This prevents against data loss. A higher replication factor requires greater compute resources and more storage.
<5> A comma separated list of bootstrap servers. This can be inside or outside of the OpenShift Container Platform cluster, and is a list of Kafka clusters that the broker receives events from and sends events to.
+
[IMPORTANT]
====
The `default.topic.replication.factor` value must be less than or equal to the number of Kafka broker instances in your cluster. For example, if you only have one Kafka broker, the `default.topic.replication.factor` value should not be more than `"1"`.
====
+
.Example Kafka broker config map
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: kafka-broker-config
  namespace: knative-eventing
data:
  default.topic.partitions: "10"
  default.topic.replication.factor: "3"
  bootstrap.servers: "my-cluster-kafka-bootstrap.kafka:9092"
----

. Apply the config map:
+
[source,yaml]
----
$ oc apply -f <config_map_filename>
----

. Specify the config map for the Kafka `Broker` object:
+
.Example Broker object
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  name: <broker_name> <1>
  namespace: <namespace> <2>
  annotations:
    eventing.knative.dev/broker.class: Kafka <3>
spec:
  config:
    apiVersion: v1
    kind: ConfigMap
    name: <config_map_name> <4>
    namespace: <namespace> <5>
...
----
<1> The broker name.
<2> The namespace where the broker exists.
<3> The broker class annotation. In this example, the broker is a Kafka broker that uses the class value `Kafka`.
<4> The config map name.
<5> The namespace where the config map exists.

. Apply the broker:
+
[source,yaml]
----
$ oc apply -f <broker_filename>
----

[id="serverless-kafka-admin-security"]
== Security configuration for the Knative broker implementation for Apache Kafka

Kafka clusters are generally secured by using the TLS or SASL authentication methods. You can configure a Kafka broker or channel to work against a protected Red Hat AMQ Streams cluster by using TLS or SASL.

[NOTE]
====
Red Hat recommends that you enable both SASL and TLS together.
====

// kafka broker security config
// Module is included in the following assemblies:
//
// * serverless/admin_guide/serverless-kafka-admin.adoc
// * /serverless/security/serverless-config-tls.adoc

[id="serverless-kafka-broker-tls-default-config_{context}"]
= Configuring TLS authentication for Apache Kafka brokers

_Transport Layer Security_ (TLS) is used by Apache Kafka clients and servers to encrypt traffic between Knative and Kafka, as well as for authentication. TLS is the only supported method of traffic encryption for the Knative broker implementation for Apache Kafka.

.Prerequisites

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.
* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` CR are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have a Kafka cluster CA certificate stored as a `.pem` file.
* You have a Kafka cluster client certificate and a key stored as `.pem` files.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create the certificate files as a secret in the `knative-eventing` namespace:
+
[source,terminal]
----
$ oc create secret -n knative-eventing generic <secret_name> \
  --from-literal=protocol=SSL \
  --from-file=ca.crt=caroot.pem \
  --from-file=user.crt=certificate.pem \
  --from-file=user.key=key.pem
----
+
[IMPORTANT]
====
Use the key names `ca.crt`, `user.crt`, and `user.key`. Do not change them.
====

. Edit the `KnativeKafka` CR and add a reference to your secret in the `broker` spec:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  broker:
    enabled: true
    defaultConfig:
      authSecretName: <secret_name>
...
----
// Module is included in the following assemblies:
//
// * serverless/admin_guide/serverless-kafka-admin.adoc

[id="serverless-kafka-broker-sasl-default-config_{context}"]
= Configuring SASL authentication for Apache Kafka brokers

_Simple Authentication and Security Layer_ (SASL) is used by Apache Kafka for authentication. If you use SASL authentication on your cluster, users must provide credentials to Knative for communicating with the Kafka cluster; otherwise events cannot be produced or consumed.

.Prerequisites

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.
* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` CR are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have a username and password for a Kafka cluster.
* You have chosen the SASL mechanism to use, for example, `PLAIN`, `SCRAM-SHA-256`, or `SCRAM-SHA-512`.
* If TLS is enabled, you also need the `ca.crt` certificate file for the Kafka cluster.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create the certificate files as a secret in the `knative-eventing` namespace:
+
[source,terminal]
----
$ oc create secret -n knative-eventing generic <secret_name> \
  --from-literal=protocol=SASL_SSL \
  --from-literal=sasl.mechanism=<sasl_mechanism> \
  --from-file=ca.crt=caroot.pem \
  --from-literal=password="SecretPassword" \
  --from-literal=user="my-sasl-user"
----
** Use the key names `ca.crt`, `password`, and `sasl.mechanism`. Do not change them.
** If you want to use SASL with public CA certificates, you must use the `tls.enabled=true` flag, rather than the `ca.crt` argument, when creating the secret. For example:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <kafka_auth_secret> \
  --from-literal=tls.enabled=true \
  --from-literal=password="SecretPassword" \
  --from-literal=saslType="SCRAM-SHA-512" \
  --from-literal=user="my-sasl-user"
----

. Edit the `KnativeKafka` CR and add a reference to your secret in the `broker` spec:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  broker:
    enabled: true
    defaultConfig:
      authSecretName: <secret_name>
...
----

[id="additional-resources_serverless-kafka-admin"]
[role="_additional-resources"]
== Additional resources
* Red Hat AMQ Streams documentation
* TLS and SASL on Kafka
