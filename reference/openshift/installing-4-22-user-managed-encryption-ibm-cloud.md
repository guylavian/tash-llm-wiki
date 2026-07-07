---
title: "User-managed encryption for {ibm-cloud-title}"
type: reference
domain: openshift
slug: installing-4-22-user-managed-encryption-ibm-cloud
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/user-managed-encryption-ibm-cloud
version: 4.22
family: installing
documentKind: "Documentation"
---

# User-managed encryption for {ibm-cloud-title}

[id="user-managed-encryption-ibm-cloud"]
= User-managed encryption for {ibm-cloud-title}

By default, provider-managed encryption is used to secure the following when you deploy an OpenShift Container Platform cluster:

* The root (boot) volume of control plane and compute machines
* Persistent volumes (data volumes) that are provisioned after the cluster is deployed

You can override the default behavior by specifying an {ibm-name} Key Protect for {ibm-cloud-name} (Key Protect) root key as part of the installation process.

When you bring our own root key, you modify the installation configuration file (`install-config.yaml`) to specify the Cloud Resource Name (CRN) of the root key by using the `encryptionKey` parameter.

You can specify that:

* The same root key be used be used for all cluster machines. You do so by specifying the key as part of the cluster's default machine configuration.
+
When specified as part of the default machine configuration, all managed storage classes are updated with this key. As such, data volumes that are provisioned after the installation are also encrypted using this key.

* Separate root keys be used for the control plane and compute machine pools.

For more information about the `encryptionKey` parameter, see Additional {ibm-cloud-title} configuration parameters.

[NOTE]
====
Make sure you have integrated Key Protect with your {ibm-cloud-title} Block Storage service. For more information, see the Key Protect documentation.
====

[id="user-managed-encryption-ibm-cloud-next-steps"]
== Next steps

Install an OpenShift Container Platform cluster:

* Installing a cluster on {ibm-cloud-title} with customizations
* Installing a cluster on {ibm-cloud-title} with network customizations
* Installing a cluster on {ibm-cloud-title} into an existing VPC
* Installing a private cluster on {ibm-cloud-title}
