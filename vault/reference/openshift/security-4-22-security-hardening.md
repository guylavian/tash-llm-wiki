---
title: "Hardening {op-system}"
type: reference
domain: openshift
slug: security-4-22-security-hardening
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/security-hardening
version: 4.22
family: security
documentKind: "Documentation"
---

# Hardening {op-system}

[id="security-hardening"]
= Hardening {op-system}

{op-system} was created and tuned to be deployed in OpenShift Container Platform with
few if any changes needed to {op-system} nodes.
Every organization adopting OpenShift Container Platform has its own requirements for
system hardening. As a {op-system-base} system with OpenShift-specific modifications and
features added (such as Ignition, ostree, and a read-only `/usr` to provide
limited immutability),
{op-system} can be hardened just as you would any {op-system-base} system.
Differences lie in the ways you manage the hardening.

A key feature of OpenShift Container Platform and its Kubernetes engine is to be able
to quickly scale applications and infrastructure up and down as needed.
Unless it is unavoidable, you do not want to make direct changes to {op-system} by
logging into a host and adding software or changing settings. You want
to have the OpenShift Container Platform installer and control plane manage changes
to {op-system} so new nodes can be spun up without manual intervention.

So, if you are setting out to harden {op-system} nodes in OpenShift Container Platform to meet
your security needs, you should consider both what to harden
and how to go about doing that hardening.

// Choosing what to harden in {op-system}
// Module included in the following assemblies:
//
// * security/container_security/security-hardening.adoc

[id="security-hardening-what_{context}"]
= Choosing what to harden in {op-system}

For information on how to approach security for any {op-system-base} system, see the Security category in the Red{nbsp}Hat Enterprise Linux 9 documentation.

Use these documents to learn about managing security updates, security hardening, securing networks, and other security measures.
For information on how to approach security for any {op-system-base} system, see the {op-system-base} 9 Security Hardening guide.

Use this guide to learn how to approach cryptography, evaluate vulnerabilities, and assess threats to various services.
Likewise, you can learn how to scan for compliance standards, check file integrity, perform auditing, and encrypt storage devices.

With the knowledge of what features you want to harden, you can then decide how to harden them in {op-system}.

// Choosing how to harden {op-system}
// Module included in the following assemblies:
//
// * security/container_security/security-hardening.adoc

[id="security-hardening-how_{context}"]
= Choosing how to harden {op-system}

Direct modification of {op-system} systems in OpenShift Container Platform is discouraged. Instead, you should think of modifying systems in pools of nodes, such as worker nodes and control plane nodes. When a new node is needed, in non-bare metal installs, you can request a new node of the type you want and it will be created from an {op-system} image plus the modifications you created earlier.

There are opportunities for modifying {op-system} before installation, during installation, and after the cluster is up and running.

[id="security-harden-before-installation_{context}"]
== Hardening before installation

For bare metal installations, you can add hardening features to {op-system} before beginning the OpenShift Container Platform installation. For example, you can add kernel options when you boot the {op-system} installer to turn security features on or off, such as various SELinux booleans or low-level settings, such as symmetric multithreading.

[WARNING]
====
Disabling SELinux on {op-system} nodes is not supported.
====

Although bare metal {op-system} installations are more difficult, they offer the opportunity of getting operating system changes in place before starting the OpenShift Container Platform installation. This can be important when you need to ensure that certain features, such as disk encryption or special networking settings, be set up at the earliest possible moment.

[id="security-harden-during-installation_{context}"]
== Hardening during installation

You can interrupt the OpenShift Container Platform installation process and change Ignition configs. Through Ignition configs, you can add your own files and systemd services to the {op-system} nodes. You can also make some basic security-related changes to the `install-config.yaml` file used for installation. Contents added in this way are available at each node's first boot.

[id="security-harden-after-installation_{context}"]
== Hardening after the cluster is running
After the OpenShift Container Platform cluster is up and running, there are several ways to apply hardening features to {op-system}:

* Daemon set: If you need a service to run on every node, you can add
that service with a Kubernetes `DaemonSet` object.

* Machine config: `MachineConfig` objects contain a subset of Ignition configs in the same format. By applying machine configs to all worker or control plane nodes, you can ensure that the next node of the same type that is added to the cluster has the same changes applied.

All of the features noted here are described in the OpenShift Container Platform product documentation.

[role="_additional-resources"]
.Additional resources
* OpenShift Security Guide
* Choosing how to configure {op-system}
* Modifying Nodes
* Manually creating the installation configuration file
* Creating the Kubernetes manifest and Ignition config files
* Installing {op-system} by using an ISO image
* Customizing nodes
* Adding kernel arguments to nodes
* Optional configuration parameters
* Support for FIPS cryptography
* {op-system-base} core crypto components
