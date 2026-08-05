---
title: "Preparing for bare-metal cluster installation"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-bare-metal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-bare-metal
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing for bare-metal cluster installation

[id="preparing-to-install-on-bare-metal"]
= Preparing for bare-metal cluster installation

[role="_abstract"]
Review the different methods for installing OpenShift Container Platform on bare metal and prepare your environment for installation.

[id="preparing_preparing-to-install-on-bare-metal"]
== Prerequisites

* You have read details about the OpenShift Container Platform installation and update processes.
* You have read the documentation on selecting a cluster installation method and preparing it for users.
* You have read the documentation for supported and unsupported OVN-Kubernetes network plugin use cases.

[id="choosing-a-method-to-install-ocp-on-bare-metal"]
== Choosing a method to install OpenShift Container Platform on bare metal

The OpenShift Container Platform installation program offers four methods for deploying a cluster:

* *Interactive*: You can deploy a cluster with the web-based {ai-full}. This is the recommended approach for clusters with networks connected to the internet. The {ai-full} is the easiest way to install OpenShift Container Platform, it provides smart defaults, and it performs pre-flight validations before installing the cluster. It also provides a RESTful API for automation and advanced configuration scenarios.

* *Local Agent-based*: You can deploy a cluster locally with the agent-based installer for air-gapped or restricted networks. It provides many of the benefits of the {ai-full}, but you must download and configure the agent-based installer first. Configuration is done with a commandline interface. This approach is ideal for air-gapped or restricted networks.

* *Automated*: You can deploy a cluster on installer-provisioned infrastructure and the cluster it maintains. The installation program uses each cluster host's baseboard management controller (BMC) for provisioning. You can deploy clusters with both connected or air-gapped or restricted networks.

* *Full control*: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters with both connected or air-gapped or restricted networks.

The clusters have the following characteristics:

* Highly available infrastructure with no single points of failure is available by default.
* Administrators maintain control over what updates are applied and when.

[id="choosing-a-method-to-install-ocp-on-bare-metal-installer-provisioned"]
== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on bare-metal infrastructure that is provisioned by the OpenShift Container Platform installation program, by using the following method:

**Installing an installer-provisioned cluster on bare metal**::
You can install OpenShift Container Platform on bare metal by using installer provisioning.

[id="choosing-a-method-to-install-ocp-on-bare-metal-user-provisioned"]
== Installing a cluster on user-provisioned infrastructure

You can install a cluster on bare-metal infrastructure that you provision, by using one of the following methods:

**Installing a user-provisioned cluster on bare metal**::
You can install OpenShift Container Platform on bare-metal infrastructure that you provision. For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

**Installing a user-provisioned bare-metal cluster with network customizations**::
You can install a bare-metal cluster on user-provisioned infrastructure with network-customizations. By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. Most of the network customizations must be applied at the installation stage.

**Installing a user-provisioned bare-metal cluster on a restricted network**::
You can install a user-provisioned bare-metal cluster on a restricted or disconnected network by using a mirror registry. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/preparing-to-install-on-bare-metal.adoc
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="virt-planning-bare-metal-cluster-for-ocp-virt_{context}"]
= Bare-metal cluster installation requirements for {VirtProductName}

[role="_abstract"]
Configure your bare-metal cluster correctly during installation to support {VirtProductName}, as certain required settings cannot be changed after installation.

[id="virt-planning-bare-metal-cluster-for-ocp-virt-HA_{context}"]
== High availability requirements for {VirtProductName}

When discussing high availability (HA) features in the context of {VirtProductName}, this refers only to the replication model of the core cluster components, determined by the `controlPlaneTopology` and `infrastructureTopology` fields in the `Infrastructure` custom resource (CR).
Setting these fields to `HighlyAvailable` offers component redundancy, which is distinct from general cluster-wide application HA. Setting these fields to `SingleReplica` disables component redundancy, and therefore disables {VirtProductName} HA features.

If you plan to use {VirtProductName} HA features, you must have three control plane nodes at the time of cluster installation. The `controlPlaneTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`.

[NOTE]
====
You can install {VirtProductName} on a single-node cluster, but {sno} does not support HA features.
====

[id="virt-planning-bare-metal-cluster-for-ocp-virt-LM_{context}"]
== Live migration requirements for {VirtProductName}

* If you plan to use live migration, you must have multiple worker nodes. The `infrastructureTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`. A minimum of three worker nodes is recommended.
+
[NOTE]
====
You can install {VirtProductName} on a single-node cluster, but {sno} does not support live migration.
====
* Live migration requires shared storage. Storage for {VirtProductName} must support and use the ReadWriteMany (RWX) access mode.

[id="virt-planning-bare-metal-cluster-for-ocp-virt-SR-IOV_{context}"]
== SR-IOV requirements for {VirtProductName}

If you plan to use Single Root I/O Virtualization (SR-IOV), ensure that your network interface controllers (NICs) are supported by OpenShift Container Platform.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-device.adoc

[id="nw-sriov-dual-nic-con_{context}"]
= NIC partitioning for SR-IOV devices

[role="_abstract"]
You can partition a single, high-speed dual port NIC into multiple virtual functions (VFs) and enable SR-IOV to support high availability with Link Aggregation Control Protocol (LACP) bonding.

This feature supports the use of bonds for high availability with the Link Aggregation Control Protocol (LACP).

[NOTE]
====
Only one LACP can be declared by physical NIC.
====

An OpenShift Container Platform cluster can be deployed on a bond interface with 2 VFs on 2 physical functions (PFs) using the following methods:

* Agent-based installer
+
[NOTE]
====
The minimum required version of `nmstate` is:

* `1.4.2-4` for RHEL 8 versions
* `2.2.7` for RHEL 9 versions
====

* Installer-provisioned infrastructure installation
* User-provisioned infrastructure installation

[role="_additional-resources"]
[id="additional-resources_preparing-to-install-on-bare-metal"]
== Additional resources

* OpenShift Container Platform installation and update processes
* Selecting a cluster installation method and preparing it for users
* OVN-Kubernetes purpose
* {ai-full}
* Preparing to install with the Agent-based Installer
* Agent-based installer
* Deploying installer-provisioned clusters on bare metal
* Installing a user-provisioned cluster on bare metal
* Installing a user-provisioned bare-metal cluster with network customizations
* Installing a user-provisioned bare-metal cluster on a restricted network
* Installation process
* Getting started with {VirtProductName}
* Preparing your cluster for {VirtProductName}
* About Single Root I/O Virtualization (SR-IOV) hardware networks
* Connecting a virtual machine to an SR-IOV network
* Example: Bonds and SR-IOV dual-NIC node network configuration
* Optional: Configuring host network interfaces for dual port NIC
* Bonding multiple SR-IOV network interfaces to a dual port NIC interface
