---
title: "Postinstallation configuration"
type: reference
domain: openshift
slug: virt-4-22-virt-post-install-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-post-install-config
version: 4.22
family: virt
documentKind: "Documentation"
---

# Postinstallation configuration

[id="virt-post-install-config"]
= Postinstallation configuration

[role="_abstract"]
The following procedures are typically performed after you install {VirtProductName}. You can configure the components that are relevant for your environment:

// * Cluster
// Until cluster checkup framework is supported in ROSA/OSD this is just for OCP
* As a cluster administrator, you can run a self validation checkup to verify that the environment is fully functional and self-sustained before you deploy production workloads.

* The hostpath provisioner is a local storage provisioner designed for {VirtProductName}. If you want to configure local storage for virtual machines, you must enable the hostpath provisioner first.

* Node placement rules for {VirtProductName} Operators, workloads, and controllers.

* Network configuration:

** Installing the Kubernetes NMState and SR-IOV Operators
** Configuring a Linux bridge network for external access to virtual machines (VMs)
** Configuring a dedicated secondary network for live migration
** Configuring an SR-IOV network
** Enabling the creation of load balancer services by using the OpenShift Container Platform web console
** Enabling the creation of load balancer services by using the OpenShift Container Platform web console

* Storage configuration:
** Defining a default storage class for the Container Storage Interface (CSI)
** Configuring local storage by using the Hostpath Provisioner (HPP)

// * Users
// * Alerts and notifications

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Specifying nodes for {VirtProductName} components
* Postinstallation network configuration
* Postinstallation storage configuration
