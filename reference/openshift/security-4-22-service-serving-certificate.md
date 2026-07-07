---
title: "Securing service traffic using service serving certificate secrets"
type: reference
domain: openshift
slug: security-4-22-service-serving-certificate
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/service-serving-certificate
version: 4.22
family: security
documentKind: "Documentation"
---

# Securing service traffic using service serving certificate secrets

[id="add-service-serving"]
= Securing service traffic using service serving certificate secrets

[role="_abstract"]
Service serving certificates provide automatic TLS encryption for service-to-service communication. Configure certificates for services, ConfigMaps, APIServices, CRDs, and webhooks to secure internal cluster traffic.

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="understanding-service-serving_{context}"]
= Understanding service serving certificates

Service serving certificates are intended to support complex
middleware applications that require encryption. These certificates are
issued as TLS web server certificates.

The `service-ca` controller uses the `x509.SHA256WithRSA` signature
algorithm to generate service certificates.

The generated certificate and key are in PEM format, stored in `tls.crt`
and `tls.key` respectively, within a created secret. The
certificate and key are automatically replaced when they get close to
expiration.

The service CA certificate, which issues the service certificates, is valid for 26 months and is automatically rotated when there is less than 13 months validity left. After rotation, the previous service CA configuration is still trusted until its expiration. This allows a grace period for all affected services to refresh their key material before the expiration. If you do not upgrade your cluster during this grace period, which restarts services and refreshes their key material, you might need to manually restart services to avoid failures after the previous service CA expires.

[NOTE]
====
You can use the following command to manually restart all pods in the cluster. Be aware that running this command causes a service interruption, because it deletes every running pod in every namespace. These pods will automatically restart after they are deleted.

[source,terminal]
----
$ for I in $(oc get ns -o jsonpath='{range .items[*]} {.metadata.name}{"\n"} {end}'); \
      do oc delete pods --all -n $I; \
      sleep 1; \
      done
----
====

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate_{context}"]
= Add a service certificate

To secure communication to your service, generate a signed serving certificate and key pair into a secret in the same namespace as the service.

The generated certificate is only valid for the internal service DNS name `<service.name>.<service.namespace>.svc`, and is only valid for internal communications. If your service is a headless service (no `clusterIP` value set), the generated certificate also contains a wildcard subject in the format of `*.<service.name>.<service.namespace>.svc`.

[IMPORTANT]
====
Because the generated certificates contain wildcard subjects for headless services, you must not use the service CA if your client must differentiate between individual pods. In this case:

* Generate individual TLS certificates by using a different CA.
* Do not accept the service CA as a trusted CA for connections that are directed to individual pods and must not be impersonated by other pods. These connections must be configured to trust the CA that was used to generate the individual TLS certificates.
====

.Prerequisites

* You must have a service defined.

.Procedure

. Annotate the service with `service.beta.openshift.io/serving-cert-secret-name`:
+
[source,terminal]
----
$ oc annotate service <service_name> \//<1>
     service.beta.openshift.io/serving-cert-secret-name=<secret_name> //<2>
----
+
--
<1> Replace `<service_name>` with the name of the service to secure.
<2> `<secret_name>` will be the name of the generated secret containing the certificate and key pair.
+
[NOTE]
====
For convenience, it is recommended that this value be the same as `<service_name>`.
====
--
+
For example, use the following command to annotate the service `test1`:
+
[source,terminal]
----
$ oc annotate service test1 service.beta.openshift.io/serving-cert-secret-name=test1
----

. Examine the service to confirm that the annotations are present:
+
[source,terminal]
----
$ oc describe service <service_name>
----
+
.Example output
[source,terminal]
----
...
Annotations:              service.beta.openshift.io/serving-cert-secret-name: <service_name>
                          service.beta.openshift.io/serving-cert-signed-by: openshift-service-serving-signer@1556850837
...
----

. After the cluster generates a secret for your service, your `Pod` spec can
mount it, and the pod will run after it becomes available.

[role="_additional-resources"]
.Additional resources
* Creating a re-encrypt route with a custom certificate

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate-configmap_{context}"]
= Add the service CA bundle to a config map

A pod can access the service Certificate Authority (CA) certificate by mounting a `ConfigMap` object that has the `service.beta.openshift.io/inject-cabundle=true` annotation. After annotating the config map, the cluster automatically injects the service CA certificate into the `service-ca.crt` key on the config map. Access to this CA certificate allows TLS clients to verify connections to services by using service serving certificates.

[IMPORTANT]
====
After adding this annotation to a config map, the OpenShift Service CA Operator deletes all the data in the config map. Consider using a separate config map to contain the `service-ca.crt`, instead of using the same config map that stores your pod configuration.
====

.Procedure

. Annotate the config map with the `service.beta.openshift.io/inject-cabundle=true` annotation by entering the following command:
+
[source,terminal]
----
$ oc annotate configmap <config_map_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<config_map_name>` with the name of the config map to annotate.
+
[NOTE]
====
Explicitly referencing the `service-ca.crt` key in a volume mount prevents a pod from starting until the config map has been injected with the CA bundle. You can override this behavior by setting the `optional` parameter to `true` in the serving certificate configuration of the volume.
====

. View the config map to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get configmap <config_map_name> -o yaml
----
+
The CA bundle is displayed as the value of the `service-ca.crt` key in the YAML output:
+
[source,terminal]
----
apiVersion: v1
data:
  service-ca.crt: |
    -----BEGIN CERTIFICATE-----
...
----

. Mount the config map as a volume to each container that exists in a pod by configuring your `Deployment` object.
+
.Example Deployment object that defines the volume for the mounted config map
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-example-custom-ca-deployment
  namespace: my-example-custom-ca-ns
spec:
  ...
    spec:
      ...
      containers:
        - name: my-container-that-needs-custom-ca
          volumeMounts:
          - name: trusted-ca
            mountPath: /etc/pki/ca-trust/extracted/pem
            readOnly: true
      volumes:
      - name: trusted-ca
        configMap:
          name: <config_map_name> <1>
          items:
            - key: ca-bundle.crt <2>
              path: tls-ca-bundle.pem <3>
# ...
----
<1> Specify the name of the config map that you annotated in an earlier step of the procedure.
<2> `ca-bundle.crt` is required as the ConfigMap key.
<3> `tls-ca-bundle.pem` is required as the ConfigMap path.

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate-apiservice_{context}"]
= Add the service CA bundle to an API service

You can annotate an `APIService` object with `service.beta.openshift.io/inject-cabundle=true` to have its `spec.caBundle` field populated with the service CA bundle. This allows the Kubernetes API server to validate the service CA certificate used to secure the targeted endpoint.

.Procedure

. Annotate the API service with `service.beta.openshift.io/inject-cabundle=true`:
+
[source,terminal]
----
$ oc annotate apiservice <api_service_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<api_service_name>` with the name of the API service to annotate.
+
For example, use the following command to annotate the API service `test1`:
+
[source,terminal]
----
$ oc annotate apiservice test1 service.beta.openshift.io/inject-cabundle=true
----

. View the API service to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get apiservice <api_service_name> -o yaml
----
+
The CA bundle is displayed in the `spec.caBundle` field in the YAML output:
+
[source,terminal]
----
apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
...
spec:
  caBundle: <CA_BUNDLE>
...
----

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate-crd_{context}"]
= Add the service CA bundle to a custom resource definition

You can annotate a `CustomResourceDefinition` (CRD) object with `service.beta.openshift.io/inject-cabundle=true` to have its `spec.conversion.webhook.clientConfig.caBundle` field populated with the service CA bundle. This allows the Kubernetes API server to validate the service CA certificate used to secure the targeted endpoint.

[NOTE]
====
The service CA bundle will only be injected into the CRD if the CRD is configured to use a webhook for conversion. It is only useful to inject the service CA bundle if a CRD's webhook is secured with a service CA certificate.
====

.Procedure

. Annotate the CRD with `service.beta.openshift.io/inject-cabundle=true`:
+
[source,terminal]
----
$ oc annotate crd <crd_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<crd_name>` with the name of the CRD to annotate.
+
For example, use the following command to annotate the CRD `test1`:
+
[source,terminal]
----
$ oc annotate crd test1 service.beta.openshift.io/inject-cabundle=true
----

. View the CRD to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get crd <crd_name> -o yaml
----
+
The CA bundle is displayed in the `spec.conversion.webhook.clientConfig.caBundle` field in the YAML output:
+
[source,terminal]
----
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
...
spec:
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        caBundle: <CA_BUNDLE>
...
----

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate-mutating-webhook_{context}"]
= Add the service CA bundle to a mutating webhook configuration

You can annotate a `MutatingWebhookConfiguration` object with `service.beta.openshift.io/inject-cabundle=true` to have the `clientConfig.caBundle` field of each webhook populated with the service CA bundle. This allows the Kubernetes API server to validate the service CA certificate used to secure the targeted endpoint.

[NOTE]
====
Do not set this annotation for admission webhook configurations that need to specify different CA bundles for different webhooks. If you do, then the service CA bundle will be injected for all webhooks.
====

.Procedure

. Annotate the mutating webhook configuration with `service.beta.openshift.io/inject-cabundle=true`:
+
[source,terminal]
----
$ oc annotate mutatingwebhookconfigurations <mutating_webhook_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<mutating_webhook_name>` with the name of the mutating webhook configuration to annotate.
+
For example, use the following command to annotate the mutating webhook configuration `test1`:
+
[source,terminal]
----
$ oc annotate mutatingwebhookconfigurations test1 service.beta.openshift.io/inject-cabundle=true
----

. View the mutating webhook configuration to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get mutatingwebhookconfigurations <mutating_webhook_name> -o yaml
----
+
The CA bundle is displayed in the `clientConfig.caBundle` field of all webhooks in the YAML output:
+
[source,terminal]
----
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
...
webhooks:
- myWebhook:
  - v1beta1
  clientConfig:
    caBundle: <CA_BUNDLE>
...
----

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="add-service-certificate-validating-webhook_{context}"]
= Add the service CA bundle to a validating webhook configuration

You can annotate a `ValidatingWebhookConfiguration` object with `service.beta.openshift.io/inject-cabundle=true` to have the `clientConfig.caBundle` field of each webhook populated with the service CA bundle. This allows the Kubernetes API server to validate the service CA certificate used to secure the targeted endpoint.

[NOTE]
====
Do not set this annotation for admission webhook configurations that need to specify different CA bundles for different webhooks. If you do, then the service CA bundle will be injected for all webhooks.
====

.Procedure

. Annotate the validating webhook configuration with `service.beta.openshift.io/inject-cabundle=true`:
+
[source,terminal]
----
$ oc annotate validatingwebhookconfigurations <validating_webhook_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<validating_webhook_name>` with the name of the validating webhook configuration to annotate.
+
For example, use the following command to annotate the validating webhook configuration `test1`:
+
[source,terminal]
----
$ oc annotate validatingwebhookconfigurations test1 service.beta.openshift.io/inject-cabundle=true
----

. View the validating webhook configuration to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get validatingwebhookconfigurations <validating_webhook_name> -o yaml
----
+
The CA bundle is displayed in the `clientConfig.caBundle` field of all webhooks in the YAML output:
+
[source,terminal]
----
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
...
webhooks:
- myWebhook:
  - v1beta1
  clientConfig:
    caBundle: <CA_BUNDLE>
...
----

// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

[id="rotate-service-serving_{context}"]
= Manually rotate the generated service certificate

You can rotate the service certificate by deleting the
associated secret. Deleting the secret results in a new one
being automatically created, resulting in a new certificate.

.Prerequisites

* A secret containing the certificate and key pair must
have been generated for the service.

.Procedure

. Examine the service to determine the secret containing the
certificate. This is found in the `serving-cert-secret-name`
annotation, as seen below.
+
[source,terminal]
----
$ oc describe service <service_name>
----
+
.Example output
[source,terminal]
----
...
service.beta.openshift.io/serving-cert-secret-name: <secret>
...
----

. Delete the generated secret for the service. This process
will automatically recreate the secret.
+
[source,terminal]
----
$ oc delete secret <secret> //<1>
----
<1> Replace `<secret>` with the name of the secret from the previous
step.

. Confirm that the certificate has been recreated
by obtaining the new secret and examining the `AGE`.
+
[source,terminal]
----
$ oc get secret <service_name>
----
+
.Example output
[source,terminal]
----
NAME              TYPE                DATA   AGE
<service.name>    kubernetes.io/tls   2      1s
----

// Module included in the following assemblies:
//
// * authentication/certificates/service-signing-certificates.adoc

[id="manually-rotate-service-ca_{context}"]
= Manually rotate the service CA certificate

The service CA is valid for 26 months and is automatically refreshed when there is less than 13 months validity left.

If necessary, you can manually refresh the service CA by using the following procedure.

[WARNING]
====
A manually-rotated service CA does not maintain trust with the previous service CA. You might experience a temporary service disruption until the pods in the cluster are restarted, which ensures that pods are using service serving certificates issued by the new service CA.
====

.Prerequisites

* You must be logged in as a cluster admin.

.Procedure

. View the expiration date of the current service CA certificate by
using the following command.
+
[source,terminal]
----
$ oc get secrets/signing-key -n openshift-service-ca \
     -o template='{{index .data "tls.crt"}}' \
     | base64 --decode \
     | openssl x509 -noout -enddate
----

. Manually rotate the service CA. This process generates a new service CA
which will be used to sign the new service certificates.
+
[source,terminal]
----
$ oc delete secret/signing-key -n openshift-service-ca
----

. To apply the new certificates to all services, restart all the pods
in your cluster. This command ensures that all services use the
updated certificates.
+
[source,terminal]
----
$ for I in $(oc get ns -o jsonpath='{range .items[*]} {.metadata.name}{"\n"} {end}'); \
      do oc delete pods --all -n $I; \
      sleep 1; \
      done
----
+
[WARNING]
====
This command will cause a service interruption, as it goes through and
deletes every running pod in every namespace. These pods will automatically
restart after they are deleted.
====
