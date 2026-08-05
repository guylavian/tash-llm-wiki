---
title: "Configuring TLS authentication"
type: reference
domain: openshift
slug: serverless-4-22-serverless-config-tls
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-config-tls
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Configuring TLS authentication

[id="serverless-config-tls"]
= Configuring TLS authentication

You can use _Transport Layer Security_ (TLS) to encrypt Knative traffic and for authentication.

TLS is the only supported method of traffic encryption for Knative Kafka. Red Hat recommends using both SASL and TLS together for Knative broker for Apache Kafka resources.

[NOTE]
====
If you want to enable internal TLS with a {SMProductName} integration, you must enable {SMProductShortName} with mTLS instead of the internal encryption explained in the following procedure.
{nbsp}See the documentation for Enabling Knative Serving metrics when using Service Mesh with mTLS.
====

// Module included in the following assemblies:
//
// * /serverless/security/serverless-config-tls.adoc

[id="serverless-enabling-tls-internal-traffic_{context}"]
= Enabling TLS authentication for internal traffic

{ServerlessProductName} supports TLS edge termination by default, so that HTTPS traffic from end users is encrypted. However, internal traffic behind the OpenShift route is forwarded to applications by using plain data. By enabling TLS for internal traffic, the traffic sent between components is encrypted, which makes this traffic more secure.

[NOTE]
====
If you want to enable internal TLS with a {SMProductName} integration, you must enable {SMProductShortName} with mTLS instead of the internal encryption explained in the following procedure.
====

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Serving.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Create a Knative service that includes the `internal-encryption: "true"` field in the spec:
+
[source,yaml]
----
...
spec:
  config:
    network:
      internal-encryption: "true"
...
----

. Restart the activator pods in the `knative-serving` namespace to load the certificates:
+
[source,terminal]
----
$ oc delete pod -n knative-serving --selector app=activator
----

[role="_additional-resources"]
.Additional resources
* Configuring TLS authentication for the Knative broker for Apache Kafka
* Configuring TLS authentication for channels for Apache Kafka
* Enabling Knative Serving metrics when using Service Mesh with mTLS
