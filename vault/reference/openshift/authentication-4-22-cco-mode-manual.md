---
title: "Manual mode with long-term credentials for components"
type: reference
domain: openshift
slug: authentication-4-22-cco-mode-manual
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/cco-mode-manual
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Manual mode with long-term credentials for components

[id="cco-mode-manual"]
= Manual mode with long-term credentials for components

Manual mode is supported for Amazon Web Services (AWS), global Microsoft Azure, Microsoft Azure Stack Hub, {gcp-first}, {ibm-cloud-name}, and Nutanix.

[id="manual-mode-classic_{context}"]
== User-managed credentials

In manual mode, a user manages cloud credentials instead of the Cloud Credential Operator (CCO). To use this mode, you must examine the `CredentialsRequest` CRs in the release image for the version of OpenShift Container Platform that you are running or installing, create corresponding credentials in the underlying cloud provider, and create Kubernetes Secrets in the correct namespaces to satisfy all `CredentialsRequest` CRs for the cluster's cloud provider. Some platforms use the CCO utility (`ccoctl`) to facilitate this process during installation and updates.

Using manual mode with long-term credentials allows each cluster component to have only the permissions it requires, without storing an administrator-level credential in the cluster. This mode also does not require connectivity to services such as the AWS public IAM endpoint. However, you must manually reconcile permissions with new release images for every upgrade.

For information about configuring your cloud provider to use manual mode, see the manual credentials management options for your cloud provider.

[NOTE]
====
An AWS, global Azure, or {gcp-short} cluster that uses manual mode might be configured to use short-term credentials for different components. For more information, see Manual mode with short-term credentials for components.
====

[role="_additional-resources"]
[id="additional-resources_cco-mode-manual"]
== Additional resources

* Manually creating long-term credentials for AWS
* Manually creating long-term credentials for Azure
* Manually creating long-term credentials for {gcp-short}
* Configuring IAM for {ibm-cloud-name}
* Configuring IAM for Nutanix
* Manual mode with short-term credentials for components
* Preparing to update a cluster with manually maintained credentials
