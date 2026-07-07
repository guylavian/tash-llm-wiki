---
title: "Configuring certificates with an issuer"
type: reference
domain: openshift
slug: security-4-22-cert-manager-creating-certificate
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-creating-certificate
version: 4.22
family: security
documentKind: "Documentation"
---

# Configuring certificates with an issuer

[id="cert-manager-creating-certificate"]
= Configuring certificates with an issuer

[role="_abstract"]
By using the {cert-manager-operator}, you can manage certificates, handling tasks such as renewal and issuance, for workloads within the cluster, as well as components interacting externally to the cluster.

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-creating-certificate.adoc

[id="cert-manager-certificate-mgmt_{context}"]
= Creating certificates for user workloads

[role="_abstract"]
To secure communications for your applications, create and manage TLS certificates for your workloads by using the {cert-manager-operator}

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed the {cert-manager-operator}.

.Procedure

. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section.

. Create a certificate:

.. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object:
+
[source, yaml]
----
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: <issuer_namespace>
spec:
  isCA: false
  commonName: '<common_name>'
  secretName: <secret_name>
  dnsNames:
  - "<domain_name>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
----
+
where:
+
`<tls_cert>`:: Specifies a name for the certificate.
`<issuer_namespace>`:: Specifies the namespace of the issuer.
`<common_name>`:: Specifies the common name (CN).
`<secret_name>`:: Specifies the name of the secret to create that contains the certificate.
`<domain_name>`:: Specifies the domain name.
`<issuer_name>`:: Specifies the name of the issuer.

.. Create the `Certificate` object by running the following command:
+
[source, terminal]
----
$ oc create -f certificate.yaml
----

.Verification

* Verify that the certificate is created and ready to use by running the following command:
+
[source, terminal]
----
$ oc get certificate -w -n <issuer_namespace>
----
+
Once certificate is in `Ready` status, workloads on your cluster can start using the generated certificate secret.

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-creating-certificate.adoc

[id="cert-manager-certificate-api-server_{context}"]
= Creating certificates for the API server

[role="_abstract"]
To secure interactions with the cluster control plane, create TLS certificates for the API server by using the {cert-manager-operator}.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed version 1.13.0 or later of the {cert-manager-operator}.

.Procedure

. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section.

. Create a certificate:

.. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object:
+
[source, yaml]
----
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: openshift-config
spec:
  isCA: false
  commonName: "api.<cluster_base_domain>"
  secretName: <secret_name>
  dnsNames:
  - "api.<cluster_base_domain>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
----
+
where:
+
`<tls_cert>`:: Specifies a name for the certificate.
`<cluster_base_domain>`:: Specifies the common name (CN).
`<secret_name>`:: Specifies the name of the secret to create that contains the certificate.
`<issuer_name>`:: Specifies the name of the issuer.

.. Create the `Certificate` object by running the following command:
+
[source, terminal]
----
$ oc create -f certificate.yaml
----

. Add the API server named certificate. For more information, see "Adding an API server named certificate" section in the "Additional resources" section.
+
[NOTE]
====
To ensure the certificates are updated, run the `oc login` command again after the certificate is created.
====

.Verification

* Verify that the certificate is created and ready to use by running the following command:
+
[source, terminal]
----
$ oc get certificate -w -n openshift-config
----
+
Once certificate is in `Ready` status, API server on your cluster can start using the generated certificate secret.

// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-creating-certificate.adoc

[id="cert-manager-certificate-ingress_{context}"]
= Creating certificates for the Ingress Controller

[role="_abstract"]
You can create a certificate for the Ingress Controller and then replace bootstrapped default self-signed certificates with cert-manager-managed external certificates.

[NOTE]
====
Before using the procedure, ensure you understand the following Ingress Controller behaviors:

* When certificates are renewed or rotated by using the cert-manager Operator, only the contents of the secret, such as the certificate and key, are updated. The secret name remains unchanged. Kubelet automatically propagates these updates to the mounted volume, allowing the router to detect the file changes and hot-reload the new certificate and key. As a result, no rolling update of the router deployment is triggered or required.

* The secret name is referenced in the Ingress Controller configuration. If you want to replace the default ingress certificate or use different secret name in Ingress Controller configuration, you must patch or edit the configuration to apply the change. This operation triggers a rolling update for router pods where new router pods load the new cert/key pair.

For more information, see this Red{nbsp}Hat Knowledgebase Solution.
====

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed version 1.13.0 or later of the {cert-manager-operator}.

.Procedure

. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section.

. Create a certificate:
+
.. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object:
+
.Example `certificate.yaml` file
[source,yaml]
----
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: openshift-ingress
spec:
  isCA: false
  commonName: "apps.<cluster_base_domain>"
  secretName: <secret_name>
  dnsNames:
  - "apps.<cluster_base_domain>"
  - "\*.apps.<cluster_base_domain>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
----
+
where:
+
`<tls_cert>`:: Specifies the name for the certificate.
`<cluster_base_domain>`:: Specifies the common name (CN).
`<secret_name>`:: Specifies the name of the secret to create that contains the certificate.
`<cluster_base_domain>`:: Specifies the DNS name of the ingress.
`<issuer_name>`:: Specifies the name of the issuer.

+
.. Create the `Certificate` object by running the following command:
+
[source,terminal]
----
$ oc create -f certificate.yaml
----

. Replace the default ingress certificate. For more information, see "Replacing the default ingress certificate" section in the "Additional resources" section.

.Verification

. Verify that the certificate is created and ready to use by running the following command:
+
[source,terminal]
----
$ oc get certificate -n openshift-ingress
----

. Verify the definition and content of the secret object by running the following command:
+
[source,terminal]
----
$ oc get secret <secretName> -n openshift-ingress
----

. Verify that the default TLS certificate has the correct configuration details for the Ingress Controller by running the following command:
+
[source,terminal]
----
$ oc get ingresscontroller default -n openshift-ingress-operator -o yaml | grep -A2 defaultCertificate
----
+
After the certificate is in `Ready` status, the Ingress Controller on your cluster can start using the generated certificate secret.

[role="_additional-resources"]
[id="additional-resources_cert-manager-creating-certificate"]
== Additional resources

* Supported issuer types

* Configuring an ACME issuer

* Adding an API server named certificate

* Replacing the default ingress certificate
