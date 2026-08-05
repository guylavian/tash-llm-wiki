---
title: "Getting ready to install {microshift-short}"
type: reference
domain: openshift
slug: microshift-install-get-ready-4-22-microshift-install-get-ready
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_get_ready/microshift-install-get-ready
version: 4.22
family: microshift_install_get_ready
documentKind: "Documentation"
---

# Getting ready to install {microshift-short}

[id="microshift-install-get-ready"]
= Getting ready to install {microshift-short}

[role="_abstract"]
To use {op-system-bundle} to compute at the edge, plan your {op-system-base-full} installation type and your {microshift-short} configuration.

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="microshift-install-system-requirements_{context}"]
= System requirements for installing {microshift-short}

[role="_abstract"]
You must add the resource requirements of your specific workloads to the baseline minimums for {microshift-short} and {op-system-base-full}.

For example, if an IoT gateway solution requires 4 GB of RAM, your system needs to have at least 2 GB for {op-system-base} and {microshift-short}, plus 4 GB for the workloads. Thus, this example deployment requires 6 GB of RAM in total.

Allow for extra capacity for future needs if you are deploying physical devices in remote locations. If you are uncertain of the RAM required, use the maximum RAM capacity that the device can support.

The following conditions must be met before installing {microshift-short}:

* A compatible version of {op-system-base}. For more information, see "Version compatibility".

* Hardware or hypervisors that are certified for your {op-system-base} version are strongly recommended. For more information, see the following links:

** Red Hat certified hardware
** Certified hypervisors
** For information about the support policy for non-certified hardware or hypervisors, see the following How does Red Hat support me when I use non-Red Hat components?

* AArch64 or x86_64 system architecture.
* 2 CPU cores.
* 2 GB RAM. Installing from the network (UEFI HTTPs or PXE boot) requires 3 GB RAM for {op-system-base}.
* 10 GB of storage.
* You have an active {microshift-short} subscription on your Red Hat account. If you do not have a subscription, contact your sales representative for more information.
* If your workload requires Persistent Volumes (PVs), you have a Logical Volume Manager (LVM) Volume Group (VG) with enough free capacity for the workloads.
* You configure secure access to the system to be able to manage it. For more information, see the following Using secure communications between two systems with OpenSSH

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-install-rhde-compat-table_{context}"]
= Version compatibility

[role="_abstract"]
You must pair a supported version of {op-system-base-full} with the {microshift-short} version. For more information, see the "{op-system-bundle} release compatibility matrix".

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc
// * microshift_troubleshooting/microshift-troubleshoot-updates.adoc
// * microshift_updating/microshift-update-options.adoc

[id="microshift-rhde-compatibility-table_{context}"]
= {op-system-bundle} release compatibility matrix

[role="_abstract"]
{op-system-base-full} and {microshift-short} work together as a single solution for device-edge computing. You can update each component separately, but the product versions must be compatible.

Supported configurations of {op-system-bundle} use verified releases for each together as listed in the following table:

[NOTE]
====
Be sure to check the support status of a release on the product lifecycle page.
====

[%header,cols="3",cols="1,1,2"]
|===
^|*{op-system-base} Version(s)*
^|*{microshift-short} Version*
^|*Supported {microshift-short} Version{nbsp}&#8594;{nbsp}Version Updates*

^|10.2
^|4.22
^|4.22.0{nbsp}&#8594;{nbsp}4.22.z (Technology Preview)

^|9.8
^|4.22
^|4.22.0{nbsp}&#8594;{nbsp}4.22.z, 4.22 on {op-system-base} 9.8{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.21
^|4.21.0{nbsp}&#8594;{nbsp}4.21.z, 4.21{nbsp}&#8594;{nbsp}4.22, 4.21{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 9.8, 4.21{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.20
^|4.20.0{nbsp}&#8594;{nbsp}4.20.z, 4.20{nbsp}&#8594;{nbsp}4.21, 4.20{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.19
^|4.19.0{nbsp}&#8594;{nbsp}4.19.z, 4.19{nbsp}&#8594;{nbsp}4.20

^|9.4
^|4.18
^|4.18.0{nbsp}&#8594;{nbsp}4.18.z, 4.18{nbsp}&#8594;{nbsp}4.20 on {op-system-base} 9.6

^|9.4
^|4.17
^|4.17.1{nbsp}&#8594;{nbsp}4.17.z, 4.17{nbsp}&#8594;{nbsp}4.18

^|9.4
^|4.16
^|4.16.0{nbsp}&#8594;{nbsp}4.16.z, 4.16{nbsp}&#8594;{nbsp}4.17, 4.16{nbsp}&#8594;{nbsp}4.18
|===

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-install-tools-intro_{context}"]
= {microshift-short} installation tools

[role="_abstract"]
To use {microshift-short}, you must already have or plan to install a {op-system-base-full} type, such as on bare metal, or as a virtual machine (VM) that you provision. Although each use case has different details, each installation of {op-system-bundle} uses {op-system-base} tools and the {oc-first}.

You can use RPMs to install {microshift-short} on an existing {op-system-base} machine. You do not need other tools unless you are also installing an image-based {op-system-base} system or VM at the same time.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-install-rhel-types_{context}"]
= {op-system-base} installation types

[role="_abstract"]
{microshift-short} supports multiple installation methods depending on your target edge environment and workload requirements. You can deploy {microshift-short} by using the standard RPM packages on an existing machine or build an immutable, image-based operating system tailored for disconnected or networked edge deployments.

Choose the best {op-system-base-full} installation type based on where you want to run your node and what your applications need to do. For the best results, apply the following principles:

* For every installation target, you must configure both the operating system and {microshift-short}.
* Consider your application storage needs, networking for node or application access, and your authentication and security requirements.
* Understand the differences between the {op-system-base} installation types, including the support scope of each, and the tools used.

[id="microshift-get-ready-install-rpm_{context}"]
== Using RPMs, or package-based installation

This simple installation type uses a basic command to install {microshift-short} on an existing {op-system-base} machine. Basic CLI tools are required for this installation type.

[id="microshift-get-ready-install-rhel-image-based_{context}"]
== {op-system-base} image-based installations

Image-based installation types involve creating an `rpm-ostree`-based, immutable version of {op-system-base} that is optimized for edge deployment.

* {op-system-ostree} can be deployed to the edge in production environments. You can use this installation type where network connections are present, restricted, or completely offline, depending on the local environment.

* Image mode for {op-system-base} is based on OCI container images and bootable containers. See the following link for an introduction to bootc technology:

** bootc: Getting started with bootable containers

When choosing an image-based installation, consider whether the installation target is intended to be in an offline or networked state, where you plan to build system images, and how you plan to load your {op-system-bundle}. Use the following scenarios as general guidance:

* If you build either a fully self-contained {op-system-ostree} or an image mode for {op-system-base} ISO outside a disconnected environment, and then install the ISO locally on your edge devices, you likely do not need an RPM repository or a mirror registry.
* If you build an ISO outside a disconnected environment that does not include the container images, but consists of only the RPMs, you need a mirror registry inside your disconnected environment. You use your mirror registry to pull container images.
* If you build images inside a disconnected environment, or use package-based installations, you need both a mirror registry and a local RPM mirror repository. You can use either the {op-system-base} reposync utility or Red{nbsp}Hat Satellite for advanced use cases. See the following links for more information:

** Creating a local mirror of the latest update for {op-system-base} without using Satellite Server
** Red{nbsp}Hat Satellite

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-install-rhel-tools-concepts_{context}"]
= {op-system-base} installation tools and concepts

[role="_abstract"]
To successfully construct and deploy a custom {microshift-short} image, you must understand the core {op-system-base} components involved in the deployment process.

Review the following resources to familiarize yourself with the required image building components:

* A Kickstart file, which contains the configuration and instructions used during the installation of your specific operating system. For more information, see the following Using Kickstart files for installing {microshift-short} in {op-system-base}

* {op-system-base} image builder is a tool for creating deployment-ready customized system images. {op-system-base} image builder uses a blueprint that you create to make the ISO. {op-system-base} image builder is best installed on a {op-system-base} VM and is built with the `composer-cli` tool. To set up these tools and review the workflow, see the following {op-system-base} documentation links:

** Introducing the RHEL image builder command-line interface
** Installing image builder
** Creating a system image with RHEL image builder in the command-line interface

* A blueprint file directs {op-system-base} image builder to the items to include in the ISO. An image blueprint provides a persistent definition of image customizations. You can create multiple builds from a single blueprint. You can also edit an existing blueprint to build a new ISO as requirements change. See the following link for more information:

** Creating a blueprint by using the command-line interface

* An ISO, which is the bootable operating system on which {microshift-short} runs. See the following links for more information:

** Creating a boot ISO installer image using the RHEL image builder CLI
** Installing a bootable ISO to a media and booting it
** Embedding in a {op-system-ostree} image using image builder

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-install-rhde-steps_{context}"]
= {op-system-bundle} installation steps

[role="_abstract"]
Before proceeding with your specific installation method, you must prepare your environment for installation. To ensure a successful deployment, you must follow the general prerequisites such as obtaining your pull secret, planning your storage strategy, and defining your network topology, before you begin.

For most installation types, you must also take the following steps:

* Download the pull secret from the Red{nbsp}Hat Hybrid Cloud Console using the following Pull secret

* Be ready to configure {microshift-short} by adding parameters and values to the {microshift-short} YAML configuration file. For more information, see "Customizing MicroShift by using the configuration file".

* Decide whether you need to configure storage for the application and tasks you are using in your {microshift-short} node, or disable the {microshift-short} storage plugin completely.

* For more information about creating volume groups and persistent volumes on {op-system-base}, see the following Overview of logical volume management

* Configure networking settings according to the access needs you plan for your {microshift-short} node and applications. Consider whether you want to use single or dual-stack networks, configure a firewall, or configure routes.
+
[NOTE]
====
You can use the {op-system-rt-kernel} where predictable latency is critical. Workload partitioning is also required for low-latency applications. For more information about low latency and the {op-system-rtk}, see "Configuring low latency".
====

// Module included in the following assembly:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc

[id="microshift-encrypt-etcd-data_{context}"]
= Encrypt etcd data

[role="_abstract"]
Kubernetes objects are stored in an etcd database and might contain sensitive data. The etcd data is not encrypted by default. You can encrypt the disk that contains the etcd database by using the Linux Unified Key Setup-on-disk-format (LUKS) management tool for block device encryption.

[id="additional-resources_microshift-install-get-ready_{context}"]
[role="_additional-resources"]
== Additional resources

* Customizing MicroShift by using the configuration file
* Configuring low latency
* Getting started with the OpenShift CLI
* Installing from an RPM package
* Understanding networking settings
* LUKS disk encryption
