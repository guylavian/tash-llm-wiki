---
title: "Installing a cluster on Alibaba Cloud by using the Assisted Installer"
type: reference
domain: openshift
slug: installing-4-22-installing-alibaba-assisted-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-alibaba-assisted-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on Alibaba Cloud by using the Assisted Installer

[id="installing-alibaba-assisted-installer"]
= Installing a cluster on Alibaba Cloud by using the Assisted Installer

{alibaba} provides a broad range of cloud computing and data storage services to online businesses and global enterprises. You can install an OpenShift Container Platform cluster on {alibaba} using the {ai-full}.

// Module included in the following assemblies:
//
// * installing/installing_alibaba/installing-alibaba-assisted-installer.adoc

[id="alibaba-ai-installing_{context}"]
= Process outline for creating a cluster with the {ai-full}

The main steps of the installation process are as follows:

. Create the cluster with the {ai-full} and download the generated image.

. Convert the image to `QCOW2` format. For more information, see the following section.

. Upload the image to the Object Storage Service bucket in {alibaba}.

. Import the image to the Elastic Compute Service in {alibaba}.

. Provision the {alibaba} resources:

.. In the Virtual Private Cloud (VPC) console, set the networking configurations.

.. In the {alibaba} DNS console, define the Domain Name System.

.. In the Elastic Compute Service (ECS) console, provision the compute instances.

. Complete host discovery in the {ai-full}.

. Complete the network configurations in {alibaba}.

. Complete the cluster configuration and installation in the {ai-full}.

.Additional resources

* Installing OpenShift Container Platform with the {ai-full}

// Module included in the following assemblies:
//
// * installing/installing_alibaba/installing-alibaba-assisted-installer.adoc

[id="alibaba-ai-converting-image-to-qcow2_{context}"]
= Converting the discovery image to QCOW2 format

Convert the generated ISO to `QCOW2` format before importing it into {alibaba}.

.Prerequisites

* You have created a cluster and downloaded the discovery image in the {ai-full}.
* You have access to a Linux machine that is outside the cluster, such as your desktop machine.

.Procedure

. Open the command-line interface on the Linux machine.

. Verify that the system has virtualization flags enabled by running the following command:
+
[source,terminal]
----
$ grep -e lm -e svm -e vmx /proc/cpuinfo
----

. Install the `qemu-img` package on a {op-system-base} or Fedora machine by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y qemu-img
----
+
[NOTE]
====
If your system uses the `APT` package manager, install the package using the name `qemu-utils` instead.
====

. Convert the image to `QCOW2` by running the following command:
+
[source,terminal]
----
$ qemu-img convert -O qcow2 ${CLUSTER_NAME}.iso ${CLUSTER_NAME}.qcow2
----
