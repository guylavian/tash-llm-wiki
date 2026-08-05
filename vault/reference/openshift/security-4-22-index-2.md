---
title: "{external-secrets-operator} overview"
type: reference
domain: openshift
slug: security-4-22-index-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/index
version: 4.22
family: security
documentKind: "Documentation"
---

# {external-secrets-operator} overview

[id="cert-manager-operator-about"]
= {cert-manager-operator} overview

[role="_abstract"]
The {cert-manager-operator} is a cluster-wide service that provides application certificate lifecycle management. The {cert-manager-operator} allows you to integrate with external certificate authorities and provides certificate provisioning, renewal, and retirement.

// About the {cert-manager-operator}
// Module included in the following assemblies:
//
// * security/cert_manager_operator/index.adoc

[id="cert-manager-about_{context}"]
= About the {cert-manager-operator}

[role="_abstract"]
The cert-manager project introduces certificate authorities and certificates as resource types in the Kubernetes API, which makes it possible to provide certificates on-demand to developers working within your cluster. The {cert-manager-operator} provides a supported way to integrate cert-manager into your OpenShift Container Platform cluster.

The {cert-manager-operator} provides the following features:

* Support for integrating with external certificate authorities
* Tools to manage certificates
* Ability for developers to self-serve certificates
* Automatic certificate renewal

[IMPORTANT]
====
Do not attempt to use both {cert-manager-operator} for OpenShift Container Platform and the community cert-manager Operator at the same time in your cluster.

Also, you should not install {cert-manager-operator} for OpenShift Container Platform in multiple namespaces within a single OpenShift cluster.
====

// Supported issuer types
// Module included in the following assemblies:
//
// * security/cert_manager_operator/index.adoc

[id="cert-manager-issuer-types_{context}"]
= {cert-manager-operator} issuer providers

[role="_abstract"]
To configure certificate authorities for your cluster, review the issuer providers offered with the {cert-manager-operator}. You can use the following issuer types to automate certificate validation and issuance:

* Automated Certificate Management Environment (ACME)
* Certificate Authority (CA)
* Self-signed
* Vault
* Venafi
* Nokia NetGuard Certificate Manager (NCM)
* Google cloud Certificate Authority Service (Google CAS)

[NOTE]
====
OpenShift Container Platform does not test all factors associated with third-party {cert-manager-operator} provider functionality. For more information about third-party support, see the OpenShift Container Platform third-party support policy.
====

// Certificate request methods
// Module included in the following assemblies:
//
// * security/cert_manager_operator/index.adoc

[id="cert-manager-request-methods_{context}"]
= Certificate request methods

[role="_abstract"]
To obtain certificates for your workloads, choose a request method supported by the {cert-manager-operator}. You can select the approach that fits your operational requirements and automation workflow.

There are two ways to request a certificate using the {cert-manager-operator}:

Using the `cert-manager.io/CertificateRequest` object:: With this method a service developer creates a `CertificateRequest` object with a valid `issuerRef` pointing to a configured issuer (configured by a service infrastructure administrator). A service infrastructure administrator then accepts or denies the certificate request. Only accepted certificate requests create a corresponding certificate.

Using the `cert-manager.io/Certificate` object:: With this method, a service developer creates a `Certificate` object with a valid `issuerRef` and obtains a certificate from a secret that they pointed to the `Certificate` object.

//Supported versions
// Module included in the following assemblies:
//
// * security/cert_manager_operator/index.adoc

[id="cert-manager-operator-supported-versions_{context}"]
= Supported {cert-manager-operator} versions

[role="_abstract"]
To maintain a supported configuration, review the compatibility of the {cert-manager-operator} with different OpenShift Container Platform releases. To find the list of supported versions of the {cert-manager-operator} across different OpenShift Container Platform releases, see the "Platform Agnostic Operators" section in "OpenShift Container Platform update and support policy".

//FIPS compliant support
// Module included in the following assemblies:
//
// * security/cert_manager_operator/index.adoc

[id="cert-manager-fips-support_{context}"]
= About FIPS compliance for {cert-manager-operator}

[role="_abstract"]
Starting with version 1.14.0, {cert-manager-operator} is designed for FIPS compliance. When running on OpenShift Container Platform in FIPS mode, it uses the RHEL cryptographic libraries submitted to NIST for FIPS validation on the x86_64, ppc64le, and s390X architectures. For more information about the NIST validation program, see "Cryptographic module validation program". For the latest NIST status for the individual versions of the RHEL cryptographic libraries submitted for validation, see "Compliance activities and government standards".

To enable FIPS mode, you must install {cert-manager-operator} on an OpenShift Container Platform cluster configured to operate in FIPS mode. For more information, see "Do you need extra security for your cluster?"

[role="_additional-resources"]
[id="cert-manager-operator-about_additional-resources"]
== Additional resources

* Cryptographic module validation program
* cert-manager project documentation
* OpenShift Container Platform update and support policy
* Understanding compliance
* Installing a cluster in FIPS mode
* Do you need extra security for your cluster?
