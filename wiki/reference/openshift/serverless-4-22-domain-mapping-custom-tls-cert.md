---
title: "Securing a mapped service using a TLS certificate"
type: reference
domain: openshift
slug: serverless-4-22-domain-mapping-custom-tls-cert
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/domain-mapping-custom-tls-cert
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Securing a mapped service using a TLS certificate

[id="domain-mapping-custom-tls-cert"]
= Securing a mapped service using a TLS certificate

// Module included in the following assemblies:
//
// * /serverless/knative-serving/config-custom-domains/domain-mapping-custom-tls-cert.adoc

[id="serverless-domain-mapping-custom-tls-cert_{context}"]
= Securing a service with a custom domain by using a TLS certificate

After you have configured a custom domain for a Knative service, you can use a TLS certificate to secure the mapped service. To do this, you must create a Kubernetes TLS secret, and then update the `DomainMapping` CR to use the TLS secret that you
have created.

[NOTE]
====
If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.

To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.
====

.Prerequisites

* You configured a custom domain for a Knative service and have a working `DomainMapping` CR.

* You have a TLS certificate from your Certificate Authority provider or a self-signed certificate.

* You have obtained the `cert` and `key` files from your Certificate Authority provider, or a self-signed certificate.

* Install the OpenShift CLI (`oc`).

.Procedure

. Create a Kubernetes TLS secret:
+
[source,terminal]
----
$ oc create secret tls <tls_secret_name> --cert=<path_to_certificate_file> --key=<path_to_key_file>
----

. Add the `networking.internal.knative.dev/certificate-uid: <id>` label to the Kubernetes TLS secret:
+
[source,terminal]
----
$ oc label secret <tls_secret_name> networking.internal.knative.dev/certificate-uid="<id>"
----
+
If you are using a third-party secret provider such as cert-manager, you can configure your secret manager to label the Kubernetes TLS secret automatically. Cert-manager users can use the secret template offered to automatically generate secrets with the correct label. In this case, secret filtering is done based on the key only, but this value can carry useful information such as the certificate ID that the secret contains.
+
[NOTE]
====
The {cert-manager-operator} is a Technology Preview feature. For more information, see the *Installing the {cert-manager-operator}* documentation.
====

. Update the `DomainMapping` CR to use the TLS secret that you have created:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1alpha1
kind: DomainMapping
metadata:
  name: <domain_name>
  namespace: <namespace>
spec:
  ref:
    name: <service_name>
    kind: Service
    apiVersion: serving.knative.dev/v1
# TLS block specifies the secret to be used
  tls:
    secretName: <tls_secret_name>
----

.Verification

. Verify that the `DomainMapping` CR status is `True`, and that the `URL` column of the output shows the mapped domain with the scheme `https`:
+
[source,terminal]
----
$ oc get domainmapping <domain_name>
----
+
.Example output
[source,terminal]
----
NAME                      URL                               READY   REASON
example.com               https://example.com               True
----

. Optional: If the service is exposed publicly, verify that it is available by running the following command:
+
[source,terminal]
----
$ curl https://<domain_name>
----
+
If the certificate is self-signed, skip verification by adding the `-k` flag to the `curl` command.
// Module included in the following assemblies:
//
// * /serverless/knative-serving/config-custom-domains/domain-mapping-custom-tls-cert.adoc

[id="serverless-ossm-secret-filtering-net-kourier_{context}"]
= Improving net-kourier memory usage by using secret filtering

By default, the informers implementation for the Kubernetes `client-go` library fetches all resources of a particular type. This can lead to a substantial overhead when many resources are available, which can cause the Knative `net-kourier` ingress controller to fail on large clusters due to memory leaking. However, a filtering mechanism is available for the Knative `net-kourier` ingress controller, which enables the controller to only fetch Knative related secrets. You can enable this mechanism by setting an environment variable to the `KnativeServing` custom resource (CR).

[IMPORTANT]
====
If you enable secret filtering, all of your secrets need to be labeled with  `networking.internal.knative.dev/certificate-uid: "<id>"`. Otherwise, Knative Serving does not detect them, which leads to failures. You must label both new and existing secrets.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* A project that you created or that you have roles and permissions for to create applications and other workloads in OpenShift Container Platform.
* Install the {ServerlessOperatorName} and Knative Serving.
* Install the OpenShift CLI (`oc`).

.Procedure

* Set the `ENABLE_SECRET_INFORMER_FILTERING_BY_CERT_UID` variable to `true` for `net-kourier-controller` in the `KnativeServing` CR:
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
 deployments:
   - env:
     - container: controller
       envVars:
       - name: ENABLE_SECRET_INFORMER_FILTERING_BY_CERT_UID
         value: 'true'
     name: net-kourier-controller
----
