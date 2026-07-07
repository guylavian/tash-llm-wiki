---
title: "Installation methods"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-ibm-cloud
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-ibm-cloud
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installation methods

[id="preparing-to-install-on-ibm-cloud"]
= Installation methods

You can install OpenShift Container Platform on {ibm-cloud-name} using installer-provisioned infrastructure. This process involves using an installation program to provision the underlying infrastructure for your cluster. Installing OpenShift Container Platform on {ibm-cloud-name} using user-provisioned infrastructure is not supported at this time.

See Installation process for more information about installer-provisioned installation processes.

[id="choosing-an-method-to-install-ocp-on-ibm-cloud-installer-provisioned"]
== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on {ibm-cloud-name} infrastructure that is provisioned by the OpenShift Container Platform installation program by using one of the following methods:

* **Installing a customized cluster on {ibm-cloud-name}**: You can install a customized cluster on {ibm-cloud-name} infrastructure that the installation program provisions. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available post-installation.

* **Installing a cluster on {ibm-cloud-name} with network customizations**: You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements.

* **Installing a cluster on {ibm-cloud-name} into an existing VPC**: You can install OpenShift Container Platform on an existing {ibm-cloud-name}. You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

* **Installing a private cluster on an existing VPC**: You can install a private cluster on an existing Virtual Private Cloud (VPC). You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

* **Installing a cluster on {ibm-cloud-title} in a restricted network**: You can install OpenShift Container Platform on {ibm-cloud-title} on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

[id="next-steps_preparing-to-install-on-ibm-cloud"]
== Next steps
* Configuring an {ibm-cloud-name} account
