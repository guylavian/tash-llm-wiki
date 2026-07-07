---
title: "Understanding image mode for RHEL with {microshift-short}"
type: reference
domain: openshift
slug: microshift-install-bootc-4-22-microshift-about-rhel-image-mode
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_bootc/microshift-about-rhel-image-mode
version: 4.22
family: microshift_install_bootc
documentKind: "Documentation"
---

# Understanding image mode for RHEL with {microshift-short}

[id="microshift-about-rhel-image-mode"]
= Understanding image mode for RHEL with {microshift-short}

[role="_abstract"]
You can embed {microshift-short} into an operating system image using image mode for {op-system-base-full}.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-about-rhel-image-mode

[id="microshift-bootc-conc_{context}"]
= About image mode for {op-system-base-full}

[role="_abstract"]
By using image mode for {op-system-base}, you can use the same tools and techniques for the operating system that you use with application containers. Image mode for {op-system-base} is a deployment method that uses a container-native approach to build, deploy, and manage the operating system as a `rhel-bootc` image.

* This container image uses standard OCI or Docker containers as a transport and delivery format for base operating system updates.
* A bootc image includes a Linux kernel that is used to start the operating system.
* By using bootc containers, developers, operations administrators, and solution providers can all use the same container-native tools and techniques.

Image mode for {op-system-base} splits the creation and installation of software changes into two steps: one on a build system and one on a running target system.

* In the build-system step, a Podman build inspects the RPM files available for installation, determines any dependencies, and creates an ordered list of chained steps to complete. Along with any other system configuration steps taking place, the end result is a new operating system available to install.

* In the running-target-system step, a bootc update downloads, unpacks, and prepares the new operating system to be started alongside the currently running system. Local configuration changes are carried forward to the new operating system. These changes take effect only when the system is restarted and the new operating system image replaces the previously running one.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-about-rhel-image-mode

[id="microshift-preparing-for-image-building_{context}"]
= Preparing for bootc image building

[role="_abstract"]
Use the image builder tool to compose customized {microshift-short} bootc images optimized for edge deployments. You can run a {microshift-short} node with your applications on a {op-system-image} virtual machine for development and testing first, then use your whole solution in edge production environments.

Use the following {op-system-base} documentation to understand the full details of using {op-system-image}:

* Follow the instructions at the following Using image mode for RHEL to build, deploy, and manage operating systems

[id="_additional-resources_microshift-install-rhel-image-mode_{context}"]
== Additional resources

* Image mode for Red Hat Enterprise Linux learning exercises
* Using image mode for RHEL to build, deploy, and manage operating systems
