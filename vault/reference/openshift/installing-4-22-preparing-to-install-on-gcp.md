---
title: "Preparing to install on {gcp-short}"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-gcp
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing to install on {gcp-short}

[id="preparing-to-install-on-gcp"]
= Preparing to install on {gcp-short}

[id="{context}-prerequisites"]
== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.

* You read the documentation on selecting a cluster installation method and preparing it for users.

[id="requirements-for-installing-ocp-on-gcp"]
== Requirements for installing OpenShift Container Platform on {gcp-short}

Before installing OpenShift Container Platform on {gcp-first}, you must create a service account and configure a {gcp-short} project. See Configuring a {gcp-short} project for details about creating a project, enabling API services, configuring DNS, {gcp-short} account limits, and supported {gcp-short} regions.

If the cloud Identity and Access Management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see Configuring a {gcp-short} cluster to use short-term credentials, Manually creating long-term credentials for {gcp-short}, or both for other options.

[id="choosing-an-method-to-install-ocp-on-gcp"]
== Choosing a method to install OpenShift Container Platform on {gcp-short}

You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See Installation process for more information about installer-provisioned and user-provisioned installation processes.

[id="choosing-an-method-to-install-ocp-on-gcp-installer-provisioned"]
=== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on {gcp-short} infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

* **Installing a cluster quickly on {gcp-short}**: You can install OpenShift Container Platform on {gcp-short} infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options.

* **Installing a customized cluster on {gcp-short}**: You can install a customized cluster on {gcp-short} infrastructure that the installation program provisions. You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available post-installation.

* **Installing a cluster on {gcp-short} in a restricted network**: You can install OpenShift Container Platform on {gcp-short} on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the {gcp-short} APIs.

* **Installing a cluster into an existing Virtual Private Cloud**: You can install OpenShift Container Platform on an existing {gcp-short} Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits on creating new accounts or infrastructure.

* **Installing a private cluster on an existing VPC**: You can install a private cluster on an existing {gcp-short} VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

[id="choosing-an-method-to-install-ocp-on-gcp-user-provisioned"]
=== Installing a cluster on user-provisioned infrastructure

You can install a cluster on {gcp-short} infrastructure that you provision, by using one of the following methods:

* **Installing a cluster on {gcp-short} with user-provisioned infrastructure**: You can install OpenShift Container Platform on {gcp-short} infrastructure that you provide. You can use the provided Infrastructure Manager templates to assist with the installation.

* **Installing a cluster with shared VPC on user-provisioned infrastructure in {gcp-short}**: You can use the provided Infrastructure Manager templates to create {gcp-short} resources in a shared VPC infrastructure.

* **Installing a cluster on {gcp-short} in a restricted network with user-provisioned infrastructure**: You can install OpenShift Container Platform on {gcp-short} in a restricted network with user-provisioned infrastructure. By creating an internal mirror of the installation release content, you can install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

[id="preparing-to-install-on-gcp-next-steps"]
== Next steps

* Configuring a {gcp-short} project
