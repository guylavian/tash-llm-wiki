---
title: "Security configuration for channels"
type: reference
domain: openshift
slug: serverless-4-22-serverless-kafka-admin-security-channels
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-kafka-admin-security-channels
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Security configuration for channels

[id="serverless-kafka-admin-security-channels"]
= Security configuration for channels

// kafka channel security config
// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-kafka-admin.adoc
// * /serverless/security/serverless-config-tls.adoc

[id="serverless-kafka-tls-channels_{context}"]
= Configuring TLS authentication for Knative channels for Apache Kafka

_Transport Layer Security_ (TLS) is used by Apache Kafka clients and servers to encrypt traffic between Knative and Kafka, as well as for authentication. TLS is the only supported method of traffic encryption for the Knative broker implementation for Apache Kafka.

.Prerequisites

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.
* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` CR are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have a Kafka cluster CA certificate stored as a `.pem` file.
* You have a Kafka cluster client certificate and a key stored as `.pem` files.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create the certificate files as secrets in your chosen namespace:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <kafka_auth_secret> \
  --from-file=ca.crt=caroot.pem \
  --from-file=user.crt=certificate.pem \
  --from-file=user.key=key.pem
----
+
[IMPORTANT]
====
Use the key names `ca.crt`, `user.crt`, and `user.key`. Do not change them.
====

. Start editing the `KnativeKafka` custom resource:
+
[source,terminal]
----
$ oc edit knativekafka
----

. Reference your secret and the namespace of the secret:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  channel:
    authSecretName: <kafka_auth_secret>
    authSecretNamespace: <kafka_auth_secret_namespace>
    bootstrapServers: <bootstrap_servers>
    enabled: true
  source:
    enabled: true
----
+
[NOTE]
====
Make sure to specify the matching port in the bootstrap server.
====
+
For example:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  channel:
    authSecretName: tls-user
    authSecretNamespace: kafka
    bootstrapServers: eventing-kafka-bootstrap.kafka.svc:9094
    enabled: true
  source:
    enabled: true
----
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-kafka-admin.adoc

[id="serverless-kafka-sasl-channels_{context}"]
= Configuring SASL authentication for Knative channels for Apache Kafka

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

. Create the certificate files as secrets in your chosen namespace:
+
[source,terminal]
----
$ oc create secret -n <namespace> generic <kafka_auth_secret> \
  --from-file=ca.crt=caroot.pem \
  --from-literal=password="SecretPassword" \
  --from-literal=saslType="SCRAM-SHA-512" \
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

. Start editing the `KnativeKafka` custom resource:
+
[source,terminal]
----
$ oc edit knativekafka
----

. Reference your secret and the namespace of the secret:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  channel:
    authSecretName: <kafka_auth_secret>
    authSecretNamespace: <kafka_auth_secret_namespace>
    bootstrapServers: <bootstrap_servers>
    enabled: true
  source:
    enabled: true
----
+
[NOTE]
====
Make sure to specify the matching port in the bootstrap server.
====
+
For example:
+
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  namespace: knative-eventing
  name: knative-kafka
spec:
  channel:
    authSecretName: scram-user
    authSecretNamespace: kafka
    bootstrapServers: eventing-kafka-bootstrap.kafka.svc:9093
    enabled: true
  source:
    enabled: true
----
