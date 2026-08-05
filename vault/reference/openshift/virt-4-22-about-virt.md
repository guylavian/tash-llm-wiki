---
title: "About {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-about-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/about-virt
version: 4.22
family: virt
documentKind: "Documentation"
---

# About {VirtProductName}

[id="about-virt"]
= About {VirtProductName}

[role="_abstract"]
{VirtProductName} provides a comprehensive virtualization solution that allows you to run and manage virtual machine workloads alongside container workloads in your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * virt/about_virt/about-virt.adoc

[id="virt-what-you-can-do-with-virt_{context}"]
= What you can do with {VirtProductName}

[role="_abstract"]
{VirtProductName} provides the scalable, enterprise-grade virtualization functionality in Red{nbsp}Hat OpenShift.
[role="_abstract"]
{VirtProductName} provides the scalable, enterprise-grade virtualization functionality in OpenShift Container Platform.
You can use it to manage virtual machines (VMs) exclusively or alongside container workloads.

[NOTE]
====
If you have a {ove-first} subscription, you can run unlimited VMs on subscribed hosts, but you cannot run application instances in containers. For more information, see the subscription guide section about "{ove-first} and related products".
====

{VirtProductName} adds new objects into your OpenShift Container Platform cluster by using Kubernetes custom resources to enable virtualization tasks. These tasks include:

* Creating and managing Linux and Windows VMs
* Running pod and VM workloads alongside each other in a cluster
* Connecting to VMs through a variety of consoles and CLI tools
* Importing and cloning existing VMs
* Managing network interface controllers and storage disks attached to VMs
* Live migrating VMs between nodes

{VirtProductName} on OpenShift Container Platform includes guest subscriptions for {op-system-base-full} based on the number of vCPUs on the host:

* Hosts with 96 or more vCPUs: Unlimited {op-system-base} guest subscriptions are included.
* Hosts with fewer than 96 vCPUs: You can run {op-system-base} guests with a guest vCPU to host vCPU ratio of up to 8:1.
+
For example, a host with 64 vCPUs can run up to 512 {op-system-base} guest vCPUs (64 host vCPUs x 8 = 512 guest vCPUs).

OVN-Kubernetes is the default network provider for {VirtProductName} on OpenShift Container Platform. For more information, see "OVN-Kubernetes" in the _Additional resources_.

You can manage your cluster and virtualization resources by using the *Virtualization* perspective of the OpenShift Container Platform web console, and by using the {oc-first}.

[IMPORTANT]
====
For supported and unsupported OVN-Kubernetes network plug-in use cases, see "OVN-Kubernetes purpose".
====

{VirtProductName} is designed and tested to work well with {rh-storage-first} features.

[IMPORTANT]
====
When you deploy {VirtProductName} with {rh-storage}, you must create a dedicated storage class for Windows virtual machine disks. See "Optimizing ODF PersistentVolumes for Windows VMs" for details.
====

You can use {VirtProductName} with OVN-Kubernetes or one of the other certified network plug-ins listed in "Certified OpenShift CNI Plug-ins".

// Hiding links in ROSA/OSD until PR 62384 merges
You can check your {VirtProductName} cluster for compliance issues by installing the Compliance Operator and running a scan with the `ocp4-moderate` and `ocp4-moderate-node` profiles. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies.

You can check your {VirtProductName} cluster for compliance issues by installing the Compliance Operator and running a scan with the `ocp4-moderate` and `ocp4-moderate-node` profiles. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies.

For information about partnering with Independent Software Vendors (ISVs) and Services partners for specialized storage, networking, backup, and additional functionality, see the Red Hat Ecosystem Catalog.

// Module included in the following assemblies:
//
// * virt/about_virt/about-virt.adoc

[id="virt-vmware-comparison_{context}"]
= Comparing {VirtProductName} to {vmw-full}

[role="_abstract"]
If you are familiar with {vmw-first}, the following table lists {VirtProductName} components that you can use to accomplish similar tasks.

However, because {VirtProductName} is conceptually different from {vmw-short}, and much of its functionality comes from the underlying OpenShift Container Platform, {VirtProductName} does not have direct alternatives for all {vmw-short} concepts or components.

.Mapping of {vmw-short} concepts to their closest {VirtProductName} counterparts
[options="header"]
[cols="2,2,3"]
|===
|{vmw-short} concept |{VirtProductName} |Explanation

|Datastore
a|Persistent volume (PV)

Persistent volume claim (PVC)

|Stores VM disks. A PV represents existing storage and is attached to a VM through a PVC. When configured for shared access, PVCs can be mounted by multiple VMs simultaneously.
|Stores VM disks. A PV represents existing storage and is attached to a VM through a PVC. When created with the `ReadWriteMany` (RWX) access mode, PVCs can be mounted by multiple VMs simultaneously.

|Dynamic Resource Scheduling (DRS)
a|Pod eviction policy

Descheduler

|Provides active resource balancing. A combination of pod eviction policies and a descheduler allows VMs to be live migrated to more appropriate nodes to keep node resource utilization manageable.

|NSX

a|
Multus
OVN-Kubernetes

Third-party container network interface (CNI) plug-ins

|Provides an overlay network configuration. There is no direct equivalent for NSX in {VirtProductName}, but you can use the OVN-Kubernetes network provider
.
or install certified third-party CNI plug-ins.

|Storage Policy Based Management (SPBM)
|Storage class
|Provides policy-based storage selection. Storage classes represent various storage types and describe storage capabilities, such as quality of service, backup policy, reclaim policy, and whether volume expansion is allowed. A PVC can request a specific storage class to satisfy application requirements.

a|vCenter

vRealize Operations

|OpenShift Metrics and Monitoring
|Provides host and VM metrics. You can view metrics and monitor the overall health of the cluster and VMs by using the OpenShift Container Platform web console.

|vMotion
|Live migration
|Moves a running VM to another node without interruption. For live migration to be available, the PVC attached to the VM must use storage that supports live migration.
|Moves a running VM to another node without interruption. For live migration to be available, the PVC attached to the VM must have the `ReadWriteMany` (RWX) access mode.

a|vSwitch

DvSwitch

a|NMState Operator

Multus

|Provides a physical network configuration. You can use the NMState Operator to apply state-driven network configuration and manage various network interface types, including Linux bridges and network bonds. With Multus, you can attach multiple network interfaces and connect VMs to external networks.
|===

// Module included in the following assemblies:
//
// * virt/about_virt/about-virt.adoc
// * virt/virt_release_notes/virt-4-19-release-notes.adoc

[id="virt-supported-cluster-version_{context}"]
= Supported cluster versions for {VirtProductName}

[role="_abstract"]
{VirtProductName} on {gcp-short} is supported on OpenShift Container Platform using either {gcp-short} Hyperdisk or {gcp-short} NetApp Volumes (GCNV) for persistent storage.

Refer to the following table for the minimum version you need to install based on your chosen storage solution.

|===
|Component |Version required with {gcp-short} Hyperdisk |Version required with {gcp-short} NetApp Volumes (GCNV)

|OpenShift Container Platform  |4.21.5 or later |4.21 or later
|{VirtProductName} Operator |4.21.1 or later |4.21.2 or later
|NetApp Trident CSI Operator |N/A |26.02.0 or later
|===
{VirtProductName} {VirtVersion} is supported for use on OpenShift Container Platform  clusters. To use the latest z-stream release of {VirtProductName}, you must first upgrade to the latest version of OpenShift Container Platform.
The latest stable release of {VirtProductName} {VirtVersion} is {HCOVersion}.

[NOTE]
====
{VirtProductName} is currently available on x86-64 CPUs. Arm-based nodes are not yet supported.
====

// Module included in the following assemblies:
//
// * virt/about/about-virt.adoc
// * virt/install/virt-requirements.adoc

[id="virt-about-storage-volumes-for-vm-disks_{context}"]
= About volume and access modes for virtual machine disks

[role="_abstract"]
If you use the storage API with known storage providers, the volume and access modes are selected automatically. However, if you use a storage class that does not have a storage profile, you must configure the volume and access mode.

For a list of known storage providers for {VirtProductName}, see the  Red Hat Ecosystem Catalog.

For best results, use the `ReadWriteMany` (RWX) access mode and the `Block` volume mode. This is important for the following reasons:

* `ReadWriteMany` (RWX) access mode is required for live migration.
* The `Block` volume mode performs significantly better than the `Filesystem` volume mode. This is because the `Filesystem` volume mode uses more storage layers, including a file system layer and a disk image file. These layers are not necessary for VM disk storage.

+
For example, if you use {rh-storage-first}, Ceph RBD volumes are preferable to CephFS volumes.

[IMPORTANT]
====
You cannot live migrate virtual machines with the following configurations:

* Storage volume with `ReadWriteOnce` (RWO) access mode
* Passthrough features such as GPUs

Set the `evictionStrategy` field to `None` for these virtual machines.
The `None` strategy powers down VMs during node reboots.
====

// removing from OSD/ROSA, as SNO is not supported
// Module included in the following assemblies:
//
// * virt/about-virt.adoc

[id="virt-sno-differences_{context}"]
= {sno-caps} differences

[role="_abstract"]
You can install {VirtProductName} on {sno}.

However, you should be aware that {sno-caps} does not support the following features:

* High availability
* Pod disruption
* Live migration
* Virtual machines or templates that have an eviction strategy configured

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* {ove-first} and related products
* OVN-Kubernetes
* Optimizing ODF PersistentVolumes for Windows VMs
* Compliance Operator
* Supported compliance profiles
* {VirtProductName} supported limits
* OVN-Kubernetes purpose
* Glossary of common terms for OpenShift Container Platform storage
* About {sno}
* Using the OpenShift Assisted Installer Service to Deploy an OpenShift Cluster on Bare Metal and vSphere
* Certified OpenShift CNI Plug-ins
* NIST-certified tool
* Red Hat Ecosystem Catalog
* Pod disruption budgets
* About live migration
* Configure eviction and run strategies
* Tuning & Scaling Guide in the Red{nbsp}Hat Knowledgebase
