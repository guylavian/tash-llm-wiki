---
title: "Preparing your cluster for {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-preparing-cluster-for-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/preparing-cluster-for-virt
version: 4.22
family: virt
documentKind: "Documentation"
---

# Preparing your cluster for {VirtProductName}

[id="preparing-cluster-for-virt"]
= Preparing your cluster for {VirtProductName}

[role="_abstract"]
Review platform compatibility information before you install {VirtProductName}. For detailed system requirements, see "Hardware, software, and operational requirements" in the Additional resources section.

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

[id="compatible-platforms_{context}"]
= Compatible platforms

[role="_abstract"]
{VirtProductName} supports bare-metal servers, ARM64-based systems, and {ibm-z-name} or {ibm-linuxone-name} systems in logical partitions.

Compatible platforms::

* On-premise bare-metal servers. For more information, see "Planning a bare-metal cluster for {VirtProductName}" in the Additional resources section.

* Bare-metal clusters installed on ARM64-based (`arm64`, also known as `aarch64`) systems.

* {ibm-z-name} or {ibm-linuxone-name} (s390x architecture) systems where an OpenShift Container Platform cluster is installed in logical partitions (LPARs). For more information, see "Preparing to install on {ibm-z-title} and {ibm-linuxone-title}" in the Additional resources section.

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

[id="virt-cloud-platforms_{context}"]
= Cloud platforms

[role="_abstract"]
{VirtProductName} is compatible with various public cloud platforms. Each platform has specific storage options available.

[cols="1,1,2a,2a", options="header"]
|===
| Vendor
| Status
| Storage
| Resources

| {aws-first}
| GA
| * Elastic Block Store (EBS)
* {odf-first}
* Portworx
* FSx (NetApp)
| * See "Installing a cluster on {aws-short} with customizations" in the Additional resources section.

| {product-rosa} (ROSA)
| GA
| * EBS
* Portworx
* FSx (Q3)
* {odf-short}
| * {VirtProductName} in the {product-rosa} documentation
* What is {product-rosa}? in the {aws-short} documentation

| {oci-first-no-rt}
| GA
| * {oci} native storage
| * {VirtProductName} and {oci-first-no-rt} known issues and limitations in the Red{nbsp}Hat Knowledgebase
* Installing {VirtProductName} on {oci} in the `oracle-quickstart/oci-openshift` GitHub repository

| Azure Red{nbsp}Hat OpenShift (ARO)
| GA
| * {odf-short}
| * {VirtProductName} for Azure Red Hat OpenShift (preview) in the Microsoft documentation

| {gcp-first}
| GA, as of {VirtProductName} 4.21.1
| * {gcp-short} native storage
* {gcp-short} NetApp Volumes (GCNV); requires {VirtProductName} 4.21.2 or later
| * Storage configuration for {VirtProductName} .x on {gcp-full} in the Red{nbsp}Hat Knowledgebase
* {VirtProductName} on {gcp-full}: Known issues and limitations in the Red{nbsp}Hat Knowledgebase
* Storage configuration for {VirtProductName} with GCNV in the Red{nbsp}Hat Knowledgebase
* {VirtProductName} with GCNV: Known errors and limitations in the Red{nbsp}Hat Knowledgebase

|===

Bare-metal instances or servers offered by other cloud providers are not supported.

[TIP]
====
For platform-specific networking information, see "Networking overview" in the Additional resources section.
====

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc
[id="virt-aws-bm_{context}"]
= {VirtProductName} on AWS bare metal

[role="_abstract"]
You can run {VirtProductName} on an {aws-first} bare metal OpenShift Container Platform cluster.

[NOTE]
====
{VirtProductName} is also supported on {product-rosa} (ROSA) Classic clusters, which have the same configuration requirements as {aws-short} bare-metal clusters.
====

[id="virt-aws-bm_{context}"]
= {VirtProductName} on OpenShift Container Platform
[role="_abstract"]
You can run {VirtProductName} on
a
an
 OpenShift Container Platform cluster.

Installing::

*  You can install the cluster by using installer-provisioned infrastructure, ensuring that you specify bare-metal instance types for the worker nodes.
For example, you can use the
`c5n.metal`
`c3-standard-192-metal`
type value for a machine based on x86_64 architecture.
[NOTE]
====
{VirtProductName} on {gcp-short} requires OpenShift Container Platform 4.21.5 and {VirtProductName} Operator 4.21.1 or later.
====
You specify bare-metal instance types by editing the `install-config.yaml` file.

For more information, see the OpenShift Container Platform documentation about installing on {aws-short}.

Accessing virtual machines (VMs)::

* There is no change to how you access VMs by using the `virtctl` CLI tool or the OpenShift Container Platform web console.
* You can expose VMs by using a `NodePort` or `LoadBalancer` service.
+
[NOTE]
====
The load balancer approach is preferable because OpenShift Container Platform automatically creates the load balancer in
{aws-short}
{gcp-short}
and manages its lifecycle. A security group is also created for the load balancer, and you can use annotations to attach existing security groups. When you remove the service, OpenShift Container Platform removes the load balancer and its associated resources.
====

// Hiding the following in ROSA/OSD because SR-IOV is not supported.
Networking::

* You cannot use Single Root I/O Virtualization (SR-IOV) or bridge Container Network Interface (CNI) networks, including virtual LAN (VLAN). If your application requires a flat layer 2 network or control over the IP pool, consider using OVN-Kubernetes secondary overlay networks.

* If your application requires a flat layer 2 network that does not need egress traffic, consider using OVN-Kubernetes secondary overlay networks with a `Layer2` topology.

Storage::
* You can use any storage solution that is certified by the storage vendor to work with the underlying platform.
* In OpenShift Container Platform on {gcp-short}, you must ensure your StorageClass uses the GCP PD CSI driver or {gcp-short} Filestore CSI driver.
* You can use {gcp-short} Hyperdisk storage with {VirtProductName} on OpenShift Container Platform on {gcp-short}. {gcp-short} Hyperdisk storage provides high performance and flexibility for VM workloads. For more information about using Hyperdisk storage, see "Storage configuration for OpenShift Virtualization 4.21.x on Google Cloud" in the _Additional resources_ section.
* You can use {gcp-short} NetApp Volumes (GCNV) with {VirtProductName} on OpenShift Container Platform on {gcp-short}. GCNV provides NFS-based shared storage that supports `ReadWriteMany` access in `Filesystem` mode, which is required for features such as virtual machine live migration.
** Running {VirtProductName} with GCNV storage requires OpenShift Container Platform 4.21 and {VirtProductName} 4.21.2, and Trident 26.02.0 or later versions.
** Only the *Flex File* service level is supported in this release. When creating storage pools, select the *File* storage type. *Flex Unified* is not supported.
** Flex File volumes are NFS-only and support `volumeMode: Filesystem` exclusively. `volumeMode: Block` is not available with Flex File.
** GCNV Flex pools are limited to 50 volumes per pool. To support larger deployments, create multiple storage pools and list them all in the `TridentBackendConfig` file. For more information, see "GCNV storage pool limits" in the _Additional resources_ section.
** Flex File pools can be *Zonal* or *Regional*. Regional pools replicate volumes across zones but only support default performance, not custom. For more information on service levels and performance, see "GCNV service levels" in the _Additional resources_ section.
+
[IMPORTANT]
====
{aws-short} bare metal, {product-rosa}, and {product-rosa} classic architecture clusters might have different supported storage solutions. Ensure that you confirm support with your storage vendor.
====
* Using Amazon Elastic File System (EFS) or Amazon Elastic Block Store (EBS) with {VirtProductName} might cause performance and functionality limitations as shown in the following table:
+
.EFS and EBS performance and functionality limitations
[cols="1,1,1,1,1,1",options="header"]
|===
|Feature
3+^|EBS volume
|EFS volume
|Shared storage solutions

|
^s|gp2
^s|gp3
^s|io2
|
|

|VM live migration
^|Not available
^|Not available
^|Available
|Available
|Available

|Fast VM creation by using cloning
3+^|Available
|Not available
|Available

|VM backup and restore by using snapshots
3+^|Available
|Not available
|Available

|===
+
Consider using CSI storage, which supports ReadWriteMany (RWX), cloning, and snapshots to enable live migration, fast VM creation, and VM snapshots capabilities.

Hosted control planes (HCPs)::
--
* You can run {VirtProductName} on HCP clusters that use {aws-short} bare-metal nodes. However, using {VirtProductName} VMs as HCP nodes is not currently supported on {aws-short}.
--

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

[id="virt-arm-compatibility_{context}"]
= ARM64 compatibility

[role="_abstract"]
{VirtProductName} on ARM64 systems is generally available (GA) with specific limitations for operating systems and live migration.

Before using {VirtProductName} on an ARM64-based system, consider the following limitations:

Operating system::
* Only Linux-based guest operating systems are supported.
* All virtualization limitations for {op-system-base} also apply to {VirtProductName}. For more information, see How virtualization on ARM64 differs from AMD64 and Intel 64 in the {op-system-base} documentation.

Live migration::
* Live migration is *not supported* on ARM64-based OpenShift Container Platform clusters.
* Hotplug is not supported on ARM64-based clusters because it depends on live migration.

VM creation::
* {op-system-base} 10 supports instance types and preferences, but not templates.
* {op-system-base} 9 supports templates, instance types, and preferences.

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

[id="virt-ibm-z-compatibility_{context}"]
= {ibm-z-title} and {ibm-linuxone-title} compatibility

[role="_abstract"]
You can use {VirtProductName} in an OpenShift Container Platform cluster that is installed in logical partitions (LPARs) on an {ibm-z-name} or {ibm-linuxone-name} (`s390x` architecture) system.

Some features are not currently available on `s390x` architecture, while others require workarounds or procedural changes. These lists are subject to change.

Currently unavailable features::
+
The following features are currently not available on `s390x` architecture:
+
* Memory hot plugging and hot unplugging
* Node Health Check Operator
* SR-IOV Operator
* PCI passthrough
* {VirtProductName} cluster checkup framework
* {VirtProductName} on a cluster installed in FIPS mode
* IPv6
* {ibm-name} Storage scale
* {hcp-capital} for {VirtProductName}
* VM pages using HugePages
+
The following features are not applicable on `s390x` architecture:
+
* virtual Trusted Platform Module (vTPM) devices
* UEFI mode for VMs
* USB host passthrough
* Configuring virtual GPUs
* Creating and managing Windows VMs
* Hyper-V

Functionality differences::
+
The following features are available for use on s390x architecture but function differently or require procedural changes:
+
* When deleting a virtual machine by using the web console, the *grace period* option is ignored. For more information, see "Deleting a virtual machine by using the web console" in the Additional resources section.
+
* When configuring the default CPU model, the `spec.defaultCPUModel` value is `"gen15b"` for an {ibm-z-title} cluster. For more information, see "Configuring the default CPU model" in the Additional resources section.
+
* When configuring a downward metrics device, if you use a VM preference, the `spec.preference.name` value must be set to `rhel.9.s390x` or another available preference with the format `*.s390x`. For more information, see "Configuring a downward metrics device" in the Additional resources section.
+
* When creating virtual machines from instance types, you are not allowed to set `spec.domain.memory.maxGuest` because memory hot plugging is not supported on {ibm-z-name}. For more information, see "Creating virtual machines from instance types" in the Additional resources section.
+
* Prometheus queries for VM guests could have inconsistent outcome in comparison to `x86`.

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc

[id="virt-important-considerations_{context}"]
= Important considerations for any platform

[role="_abstract"]
Before installing {VirtProductName}, note key considerations about installation methods, storage, IPv6, and FIPS mode.

Installation method considerations::
You can use any installation method, including user-provisioned, installer-provisioned, or Assisted Installer, to deploy OpenShift Container Platform. However, the installation method and the cluster topology might affect {VirtProductName} functionality, such as snapshots or live migration. For more information about live migration, see "Hardware, software, and operational requirements" in the Additional resources section.

{rh-storage-first}::
If you deploy {VirtProductName} with {rh-storage-first}, you must create a dedicated storage class for Windows virtual machine disks. For more information, see "Optimizing ODF PersistentVolumes for Windows VMs" in the Additional resources section.

IPv6::
{VirtProductName} support for single-stack IPv6 clusters is limited to the OVN-Kubernetes localnet and Linux bridge Container Network Interface (CNI) plugins.
+

FIPS mode::
If you install your cluster in FIPS mode, no additional setup is required for {VirtProductName}. For more information, see "Installing a FIPS-compliant cluster" in the Additional resources section.

// Module included in the following assemblies:
//
// * virt/install/preparing-cluster-for-virt.adoc
// * virt/install/virt-requirements.adoc

[id="virt-object-maximums_{context}"]
= Object maximums

[role="_abstract"]
Consider tested object maximums for both OpenShift Container Platform and {VirtProductName} when planning your cluster.

OpenShift Container Platform:: See "OpenShift Container Platform object maximums" in the Additional resources section.

{VirtProductName}:: See "{VirtProductName} supported limits" in the Additional resources section.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Hardware, software, and operational requirements
* Planning a bare-metal cluster for {VirtProductName}
* Preparing to install on {ibm-z-title} and {ibm-linuxone-title}
* Installing a cluster on {aws-short} with customizations
* OpenShift Container Platform object maximums
* {VirtProductName} supported limits
* Installing a FIPS-compliant cluster
* Configure CPU models
* Deleting a virtual machine by using the web console
* Configuring a downward metrics device
* Creating virtual machines from instance types
* Networking overview
* Connecting a virtual machine to an OVN-Kubernetes secondary network
* Exposing a virtual machine by using a service
* Optimizing ODF PersistentVolumes for Windows VMs
* {gcp-full} NetApp Volumes
* GCNV storage pool limits
* GCNV service levels
* Glossary of common terms for OpenShift Container Platform storage
