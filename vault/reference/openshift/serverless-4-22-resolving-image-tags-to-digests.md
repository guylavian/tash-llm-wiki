---
title: "Resolving image tags to digests"
type: reference
domain: openshift
slug: serverless-4-22-resolving-image-tags-to-digests
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/resolving-image-tags-to-digests
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Resolving image tags to digests

[id="resolving-image-tags-to-digests"]
= Resolving image tags to digests

If the Knative Serving controller has access to the container registry, Knative Serving resolves image tags to a digest when you create a revision of a service. This is known as _tag-to-digest resolution_, and helps to provide consistency for deployments.

// Tag to digest resolution
// Module included in the following assemblies
//
// * serverless/admin_guide/serverless-configuration.adoc

[id="serverless-tag-to-digest-resolution_{context}"]
= Tag-to-digest resolution

To give the controller access to the container registry on OpenShift Container Platform, you must create a secret and then configure controller custom certificates. You can configure controller custom certificates by modifying the `controller-custom-certs` spec in the `KnativeServing` custom resource (CR). The secret must reside in the same namespace as the `KnativeServing` CR.

If a secret is not included in the `KnativeServing` CR, this setting defaults to using public key infrastructure (PKI). When using PKI, the cluster-wide certificates are automatically injected into the Knative Serving controller by using the `config-service-sa` config map. The {ServerlessOperatorName} populates the `config-service-sa` config map with cluster-wide certificates and mounts the config map as a volume to the controller.
// Module included in the following assemblies
//
// * serverless/admin_guide/serverless-configuration.adoc

[id="knative-serving-controller-custom-certs-secrets_{context}"]
= Configuring tag-to-digest resolution by using a secret

If the `controller-custom-certs` spec uses the `Secret` type, the secret is mounted as a secret volume. Knative components consume the secret directly, assuming that the secret has the required certificates.

.Prerequisites

* You have cluster administrator permissions on OpenShift Container Platform.

* You have cluster or dedicated administrator permissions on OpenShift Container Platform.

* You have installed the {ServerlessOperatorName} and Knative Serving on your cluster.

.Procedure

. Create a secret:
+
.Example command
[source,yaml]
----
$ oc -n knative-serving create secret generic custom-secret --from-file=<secret_name>.crt=<path_to_certificate>
----

. Configure the `controller-custom-certs` spec in the `KnativeServing` custom resource (CR) to use the `Secret` type:
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  controller-custom-certs:
    name: custom-secret
    type: Secret
----
