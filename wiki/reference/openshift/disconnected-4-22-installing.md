---
title: "Installing a cluster in a disconnected environment"
type: reference
domain: openshift
slug: disconnected-4-22-installing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected/installing
version: 4.22
family: disconnected
documentKind: "Documentation"
---

# Installing a cluster in a disconnected environment

[id="installing-disconnected-environments"]
= Installing a cluster in a disconnected environment

You can install an OpenShift Container Platform cluster in a disconnected environment, choosing the installation method and infrastructure that best suits your requirements.
This includes installing OpenShift Container Platform on either on-premise hardware or on a cloud hosting service such as Amazon Web Services (AWS).

The following sections outline all of the supported methods for installing a cluster in a disconnected environment.

[NOTE]
====
In order to learn about other requirements for installing a cluster using a particular method, be sure to review other content in the procedure's respective section of the documentation.

For example, if you plan to install a cluster on {aws-short} with installer-provisioned infrastructure, see Configuring an AWS account and Preparing to install a cluster on {aws-short}
====
// Not sure if the sentence above should be a note or just plain text.

[id="installing-agent_{context}"]
== Installing a cluster with the Agent-based Installer

To learn more about installing a cluster in a disconnected environment with the Agent-based installer, see the following pages:

* Understanding disconnected installation mirroring

* Installing an OpenShift Container Platform cluster with the Agent-based Installer

[id="installing-aws_{context}"]
== Installing a cluster on {aws-full}

To learn more about installing a cluster on {aws-first} in a disconnected environment, see the following procedures:

* Installer-provisioned infrastructure: Installing a cluster on {aws-short} in a restricted network

* User-provisioned infrastructure: Installing a cluster on {aws-short} in a restricted network with user-provisioned infrastructure

[id="installing-azure_{context}"]
== Installing a cluster on {azure-full}

To learn more about installing a cluster on {azure-first} in a disconnected environment, see the following procedures:

* Installer-provisioned infrastructure: Installing a cluster on {azure-short} in a restricted network

* User-provisioned infrastructure: Installing a cluster on {azure-short} in a restricted network with user-provisioned infrastructure

[id="installing-gcp_{context}"]
== Installing a cluster on {gcp-full}

To learn more about installing a cluster on {gcp-first} in a disconnected environment, see the following procedures:

* Installer-provisioned infrastructure: Installing a cluster on {gcp-short} in a restricted network

* User-provisioned infrastructure: Installing a cluster on {gcp-short} in a restricted network with user-provisioned infrastructure

[id="installing-ibm-cloud_{context}"]
== Installing a cluster on {ibm-cloud-title}

To learn more about installing a cluster on {ibm-cloud-name} in a disconnected environment, see the following procedure:

* Installing a cluster on {ibm-cloud-title} in a restricted network

[id="installing-nutanix_{context}"]
== Installing a cluster on Nutanix

To learn more about installing a cluster on Nutanix in a disconnected environment, see the following procedure:

* Installing a cluster on Nutanix in a restricted network

[id="installing-baremetal_{context}"]
== Installing a bare-metal cluster

To learn more about installing a bare-metal cluster in a disconnected environment, see the following procedure:

* Installing a user-provisioned bare metal cluster on a restricted network

[id="installing-ibm-z_{context}"]
== Installing a cluster on {ibm-z-name} or {ibm-linuxone-name}

To learn more about installing a cluster on {ibm-z-name} or {ibm-linuxone-name} in a disconnected environment, see the following procedures:

* Installing a cluster with z/VM on {ibm-z-title} and {ibm-linuxone-title} in a restricted network

* Installing a cluster with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title} in a restricted network

* Installing a cluster in an LPAR on {ibm-z-title} and {ibm-linuxone-title} in a restricted network

[id="installing-ibm-power_{context}"]
== Installing a cluster on {ibm-power-title}

To learn more about installing a cluster on {ibm-power-title} in a disconnected environment, see the following procedure:

* Installing a cluster on {ibm-power-title} in a restricted network

[id="installing-ibm-openstack_{context}"]
== Installing a cluster on OpenStack

To learn more about installing a cluster on {rh-openstack-first} in a disconnected environment, see the following procedure:

* Installing a cluster on OpenStack in a restricted network

[id="installing-vsphere_{context}"]
== Installing a cluster on {vmw-short}

To learn more about installing a cluster on {vmw-first} in a disconnected environment, see the following procedures:

* Installer-provisioned infrastructure: Installing a cluster on {vmw-short} in a restricted network

* User-provisioned infrastructure: Installing a cluster on {vmw-short} in a restricted network with user-provisioned infrastructure
