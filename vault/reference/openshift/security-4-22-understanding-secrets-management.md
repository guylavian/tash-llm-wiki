---
title: "Understanding secrets management in {product-title}"
type: reference
domain: openshift
slug: security-4-22-understanding-secrets-management
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/understanding-secrets-management
version: 4.22
family: security
documentKind: "Documentation"
---

# Understanding secrets management in {product-title}

[id="understanding-secrets-management"]
= Understanding secrets management in OpenShift Container Platform

[role="_abstract"]
Secret management tools can be used to automate the lifecycle of sensitive data, such as passwords, private files, and certificates, by providing a centralized system to control and monitor access. This approach enhances security by limiting the uncontrolled spread of secrets and enables automation for the entire secret lifecycle, including updates, expiration, and removal.

OpenShift Container Platform uses a flexible Operator and plugin design to decouple your workloads from external secret managers, ensuring you are not locked into a single vendor. In this model, the Operator acts as an intermediary, while a vendor-specific plugin manages communication between the cluster and the external storage. This allows applications to access secrets without needing to know the details of where or how they are stored.

// Module included in the following assemblies:
//
// * security/understanding-secrets-management.adoc
[id="secrets-management-operators_{context}"]
= Secrets management Operators in OpenShift Container Platform

[role="_abstract"]
OpenShift Container Platform offers a suite of supported Operators designed to secure and automate the management of sensitive data, such as external credentials and digital certificates. Each secrets management Operator provides quick starts and sample YAML manifests to streamline the onboarding process. These tools simplify installation and deployment, and help you build complex custom resources by using pre-defined YAML snippets. The following list details the key Operators available for these tasks:

* *{secrets-store-driver}*: Enables Kubernetes to connect to external systems, and mount credentials from the external system into an application workload.

* *{external-secrets-operator}*: Retrieves credentials stored in external management systems and makes them available within OpenShift Container Platform as standard Kubernetes Secrets.

* *{cert-manager-operator}*: Manages the lifecycle of digital certificates that are used by applications running on OpenShift Container Platform by automating the process of issuance and renewal.

// Module included in the following assemblies:
//
// * security/understanding-secrets-management.adoc
[id="secrets-management-scenarios_{context}"]
= Secrets management use cases

[role="_abstract"]
Using secrets management tools with other Red{nbsp}Hat products can protect sensitive data across your OpenShift Container Platform cluster. You can integrate secrets management Operators with other OpenShift Container Platform components to securely manage, automate, and consume credentials across various infrastructure and application workflows.

[id="secrets-management-scenarios-eso_{context}"]
== {external-secrets-operator} use cases

You can integrate the {external-secrets-operator-short} with other OpenShift Container Platform components to securely manage and inject credentials. Learn how to apply {external-secrets-operator-short} in real-world deployment strategies, by reviewing the following example.

Securing {gitops-title} by using {external-secrets-operator-short} short-lived tokens::

To reduce the security risk of compromised credentials, you can configure the {external-secrets-operator-short} to generate short-lived tokens. {gitops-title} can then use these temporary tokens to securely authenticate when accessing GitHub repositories. You can refer to an example of the integration in the {external-secrets-operator-short} and {gitops-shortname} demonstration.

.Additional resources

* {external-secrets-operator-short} and {gitops-shortname} demonstration
* Zero trust GitOps: Build a secure, secretless GitOps pipeline

[role="_additional-resources"]
.Additional resources

* Secrets Store Container Storage Interface Driver Operator

* {external-secrets-operator}

* {cert-manager-operator}
