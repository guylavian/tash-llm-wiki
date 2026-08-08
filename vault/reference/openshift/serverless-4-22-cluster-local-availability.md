---
title: "Cluster local availability"
type: reference
domain: openshift
slug: serverless-4-22-cluster-local-availability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/cluster-local-availability
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Cluster local availability

[id="cluster-local-availability"]
= Cluster local availability

By default, Knative services are published to a public IP address.
Being published to a public IP address means that Knative services are public applications, and have a publicly accessible URL.

Publicly accessible URLs are accessible from outside of the cluster.
However, developers may need to build back-end services that are only be accessible from inside the cluster, known as _private services_.
// Cluster administrators can configure private services for the cluster so that all services are private by default.
// Need to add additional details about editing the configmap for admins
Developers can label individual services in the cluster with the `networking.knative.dev/visibility=cluster-local` label to make them private.

[IMPORTANT]
====
For {ServerlessProductName} 1.15.0 and newer versions, the `serving.knative.dev/visibility` label is no longer available. You must update existing services to use the `networking.knative.dev/visibility` label instead.
====

// Module included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/routing-overview.adoc

[id="knative-service-cluster-local_{context}"]
= Setting cluster availability to cluster local

// remove note for 4.10, OSD

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have created a Knative service.

.Procedure

* Set the visibility for your service by adding the `networking.knative.dev/visibility=cluster-local` label:
+
[source,terminal]
----
$ oc label ksvc <service_name> networking.knative.dev/visibility=cluster-local
----

.Verification

* Check that the URL for your service is now in the format `\http://<service_name>.<namespace>.svc.cluster.local`, by entering the following command and reviewing the output:
+
[source,termina]
----
$ oc get ksvc
----
+
.Example output
[source,terminal]
----
NAME            URL                                                                         LATESTCREATED     LATESTREADY       READY   REASON
hello           http://hello.default.svc.cluster.local                                      hello-tx2g7       hello-tx2g7       True
----

// Module included in the following assemblies:
//
// * /serverless/security/serverless-config-tls.adoc

[id="serverless-enabling-tls-local-services_{context}"]
= Enabling TLS authentication for cluster local services

For cluster local services, the Kourier local gateway `kourier-internal` is used. If you want to use TLS traffic against the Kourier local gateway, you must configure your own server certificates in the local gateway.

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Serving.
* You have administrator permissions.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Deploy server certificates in the `knative-serving-ingress` namespace:
+
[source,terminal]
----
$ export san="knative"
----
+
[NOTE]
====
Subject Alternative Name (SAN) validation is required so that these certificates can serve the request to `<app_name>.<namespace>.svc.cluster.local`.
====

. Generate a root key and certificate:
+
[source,terminal]
----
$ openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 \
    -subj '/O=Example/CN=Example' \
    -keyout ca.key \
    -out ca.crt
----

. Generate a server key that uses SAN validation:
+
[source,terminal]
----
$ openssl req -out tls.csr -newkey rsa:2048 -nodes -keyout tls.key \
  -subj "/CN=Example/O=Example" \
  -addext "subjectAltName = DNS:$san"
----

. Create server certificates:
+
[source,terminal]
----
$ openssl x509 -req -extfile <(printf "subjectAltName=DNS:$san") \
  -days 365 -in tls.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial -out tls.crt
----

. Configure a secret for the Kourier local gateway:
.. Deploy a secret in `knative-serving-ingress` namespace from the certificates created by the previous steps:
+
[source,terminal]
----
$ oc create -n knative-serving-ingress secret tls server-certs \
    --key=tls.key \
    --cert=tls.crt --dry-run=client -o yaml | oc apply -f -
----

.. Update the `KnativeServing` custom resource (CR) spec to use the secret that was created by the Kourier gateway:
+
.Example KnativeServing CR
[source,yaml]
----
...
spec:
  config:
    kourier:
      cluster-cert-secret: server-certs
...
----

The Kourier controller sets the certificate without restarting the service, so that you do not need to restart the pod.

You can access the Kourier internal service with TLS through port `443` by mounting and using the `ca.crt` from the client.
