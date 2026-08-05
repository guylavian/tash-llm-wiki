---
title: "Installation methods"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-ibm-z
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-ibm-z
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installation methods

[id="preparing-to-install-on-ibm-z"]
= Installation methods

You can install an OpenShift Container Platform cluster on {ibm-z-name} and {ibm-linuxone-name} using a variety of different installation methods.
Each method has qualities that can make them more suitable for different use cases, such as installing a cluster in a disconnected environment or installing a cluster with minimal configuration and provisioning.

//moved prerequisites to ibm z cluster installation assemblies zvm, lpar, kvm

[NOTE]
====
While this document refers only to {ibm-z-name}, all information in it also applies to {ibm-linuxone-name}.
====

[id="choosing-an-method-to-install-ocp-on-ibm-z"]
== Choosing a method to install OpenShift Container Platform on {ibm-z-title} or {ibm-linuxone-title}

The OpenShift Container Platform installation program offers the following methods for deploying a cluster on {ibm-z-name}:

* *Interactive*: You can deploy a cluster with the web-based {ai-full}. This method requires no setup for the installer, and is ideal for connected environments like {ibm-z-name}.

* *Local Agent-based*: You can deploy a cluster locally with the Agent-based Installer. It provides many of the benefits of the {ai-full}, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface (CLI). This approach is ideal for disconnected networks.

* *Full control*: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments.

.{ibm-z-name} installation options
[cols="4,1,1,1,1",options="header"]
|===
||Assisted Installer |Agent-based Installer |User-provisioned installation |Installer-provisioned installation

|{ibm-z-name} with z/VM
|&#10003;
|&#10003;
|&#10003;
|

|Restricted network {ibm-z-name} with z/VM
|
|&#10003;
|&#10003;
|

|{ibm-z-name} with {op-system-base} KVM
|&#10003;
|&#10003;
|&#10003;
|

|Restricted network {ibm-z-name} with {op-system-base} KVM
|
|&#10003;
|&#10003;
|

|{ibm-z-name} in an LPAR
|&#10003;
|&#10003;
|&#10003;
|

|Restricted network {ibm-z-name} in an LPAR
|
|&#10003;
|&#10003;
|
|===

For more information about the installation process, see the Installation process.

== User-provisioned infrastructure installation of OpenShift Container Platform on {ibm-z-title}

User-provisioned infrastructure requires the user to provision all resources required by OpenShift Container Platform.

[IMPORTANT]
====
The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the {ibm-z-name} platform and the installation process of OpenShift Container Platform. Use the user-provisioned infrastructure installation instructions as a guide; you are free to create the required resources through other methods.
====

* **Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}**: You can install OpenShift Container Platform with z/VM on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision.

* **Installing a cluster with z/VM on {ibm-z-title} and {ibm-linuxone-title} in a disconnected environment**: You can install OpenShift Container Platform with z/VM on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

* **Installing a cluster with RHEL KVM on {ibm-z-name} and {ibm-linuxone-name}**: You can install OpenShift Container Platform with KVM on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision.

* **Installing a cluster with {op-system-base} KVM on {ibm-z-name} and {ibm-linuxone-name} in a disconnected environment**: You can install OpenShift Container Platform with {op-system-base} KVM on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

* **Installing a cluster in an LPAR on {ibm-z-name} and {ibm-linuxone-name}**: You can install OpenShift Container Platform in a logical partition (LPAR) on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision.

* **Installing a cluster in an LPAR on {ibm-z-name} and {ibm-linuxone-name} in a disconnected environment**: You can install OpenShift Container Platform in an LPAR on {ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.
