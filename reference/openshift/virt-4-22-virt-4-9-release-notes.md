---
title: "{VirtProductName} release notes"
type: reference
domain: openshift
slug: virt-4-22-virt-4-9-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-4-9-release-notes
version: 4.22
family: virt
documentKind: "Documentation"
---

# {VirtProductName} release notes

[id="virt-4-9-release-notes"]
= {VirtProductName} release notes

== About Red Hat {VirtProductName}

Red Hat {VirtProductName} enables you to bring traditional virtual machines (VMs) into OpenShift Container Platform where they run alongside containers, and are managed as native Kubernetes objects.

{VirtProductName} is represented by the image:Operator_Icon-OpenShift_Virtualization-5.png[{VirtProductName},40,40] logo.

You can use {VirtProductName} with either the OVN-Kubernetes or the OpenShiftSDN default Container Network Interface (CNI) network provider.

Learn more about what you can do with {VirtProductName}.

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

[id="virt-guest-os"]
=== Supported guest operating systems
{VirtProductName} guests can use the following operating systems:

* Red Hat Enterprise Linux 6, 7, and 8.
* Red Hat Enterprise Linux 9 Alpha (Technology Preview).
* Microsoft Windows Server 2012 R2, 2016, and 2019.
* Microsoft Windows 10.

Other operating system templates shipped with {VirtProductName} are not supported.

//CNV-8167  Supported guest operating systems
//CNV-13793 Supported guest OS

[id="virt-4-9-new"]
== New and changed features
//CNV-8875 OLM and stable channels

//CNV-8577 OpenShift Service Mesh: Commenting out the RN because the feature will now be available in 4.10
* {VirtProductName} is now integrated with OpenShift Service Mesh. You can connect virtual machines to a service mesh to monitor, visualize, and control traffic between pods that run virtual machine workloads on the default pod network with IPv4.

//CNV-12858
* {VirtProductName} is certified in Microsoft’s Windows Server Virtualization Validation Program (SVVP) to run Windows Server workloads.
+
The SVVP Certification applies to:
+
** Red Hat Enterprise Linux CoreOS workers. In the Microsoft SVVP Catalog, they are named __Red Hat OpenShift Container Platform 4 on RHEL CoreOS__.
** Intel and AMD CPUs.

//CNV-9540 High performance windows
* High-performance virtual machine templates are now available for supported Windows operating systems.

//CNV-8875
* If your {VirtProductName} Operator subscription used any update channel other than *stable*, it is now automatically subscribed to the *stable* channel. This single update channel delivers z-stream and minor version updates and ensures that your {VirtProductName} and OpenShift Container Platform versions are compatible.

//CNV-14246
* You can now use the `virtctl guestfs` command to maintain, repair, and debug virtual machine disks.

//CNV-14262
* You can now boot virtual machines with EFI mode without mandatory Secure Boot.

[id="virt-4-9-quick-starts"]
=== Quick starts

* Quick start tours are available for several {VirtProductName} features. To view the tours, click the *Help* icon *?* in the menu bar on the header of the {VirtProductName} console and then select *Quick Starts*. You can filter the available tours by entering the `virtualization` keyword in the *Filter* field.

[id="virt-4-9-installation-new"]
=== Installation

//CNV-14191 FIPS on CNV
* You can now deploy {VirtProductName} on FIPS-enabled clusters.

* You can now download the `virtctl` client even if the cluster is offline by using the `ConsoleCLIDownload` custom resource (CR).

[id="virt-4-9-networking-new"]
=== Networking
//CNV-11197 MAC spoof filtering
* You can now enable or disable MAC spoof filtering on secondary networks by configuring a Linux bridge network attachment definition in the CLI.

[id="virt-4-9-storage-new"]
=== Storage

//CNV-14247 CSI Clones
* You can use storage profiles to set a default cloning method for a storage class, creating a cloning strategy. Setting cloning strategies can be helpful, for example, if your storage vendor only supports certain cloning methods. It also allows you to select a method that limits resource usage or maximizes performance. In addition to previously available cloning methods such as snapshots and host-assisted cloning, you can now specify `csi-clone` as the default cloning behavior, which uses the CSI clone API to efficiently clone an existing volume without using an interim volume snapshot.

//CNV-14245 Online VM snapshots
* You can now take a snapshot of an online virtual machine. If the QEMU guest agent is installed, the file system is quiesced when taking the snapshot, maximizing data integrity.
[id="virt-4-9-web-new"]

=== Web console

//BZ-1931579 Virt machine template descriptions
//CNV-14219 Sysprep UI
* You can now automate your Windows virtual machine setup by uploading answer files in XML format in the *Advanced* -> *SysPrep* section of the *Create virtual machine from template* wizard.

//CNV-11664 Rhel 9 OCP Virt

//CNV-14193 Virt dashboard
* You can use the {VirtProductName} dashboard in the web console to get data on resource consumption for virtual machines and associated pods. The dashboard provides visual representations of cluster metrics so you can quickly understand the state of your cluster.

// NOTE: no deprecated features in 4.9; commenting out these sections to retain for future use
//[id="virt-4-9-deprecated-removed"]
//== Deprecated and removed features

//[id="virt-4-9-deprecated"]
//=== Deprecated features

//Deprecated features are included in the current release and supported. However, they will be removed in a future release and are not recommended for new deployments.

// NOTE: when uncommenting deprecated features list, change the header level below to ===
[id="virt-4-9-removed"]
== Removed features

Removed features are not supported in the current release.

* Importing a single virtual machine from Red Hat Virtualization (RHV) or VMware is removed from {VirtProductName} 4.9. This feature is replaced by the Migration Toolkit for Virtualization.

// NOTE: no notable technical changes in 4.9, commenting out to retain
//[id="virt-4-9-changes"]
//== Notable technical changes

[id="virt-4-9-technology-preview"]
== Technology Preview features

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use. Note the following scope of support on the Red Hat Customer Portal for these features:

Technology Preview Features Support Scope

//CNV-14192 virt-launcher now automatically updates - now TP
* You can now enable automatic updates for {VirtProductName} workloads, such as `virt-launcher` pods. Configure workload update strategies by editing the `HyperConverged` custom resource.

* You can now hot-plug and hot-unplug virtual disks when you want to add or remove them from your virtual machine without stopping the virtual machine instance.

* You can now use the Red Hat Enterprise Linux 9 Alpha template to create virtual machines.

[id="virt-4-9-known-issues"]
== Known issues

//New known issues should go below here.

//BZ-1963254 UEFI without Secure Boot

//BZ-2007397
* If you hot-plug a virtual disk and then force delete the `virt-launcher` pod, you might lose data. This is due to a race condition that can cause the VM disk's contents to be wiped from the persistent volume. (*BZ#2007397*)

//New known issues should go above here.

* If a cloning operation is initiated before the source is available to be cloned, the operation stalls indefinitely. This is because the clone authorization expires before the cloning operation starts. (*BZ#1855182*)
+
** As a workaround, delete the `DataVolume` object that is requesting the clone. When the source is available, recreate the `DataVolume` object that you deleted so that the cloning operation can complete successfully.

* If your OpenShift Container Platform cluster uses OVN-Kubernetes as the default Container Network Interface (CNI) provider, you cannot attach a Linux bridge or bonding to the default interface of a host because of a change in the host network topology of OVN-Kubernetes. (*BZ#1885605*)

** As a workaround, you can use a secondary network interface connected to your host, or switch to the OpenShift SDN default CNI provider.

* Running virtual machines that cannot be live migrated might block an OpenShift Container Platform cluster upgrade. This includes virtual machines that use hostpath-provisioner storage or SR-IOV network interfaces. (*BZ#1858777*)

** As a workaround, you can reconfigure the virtual machines so that they can be powered off during a cluster upgrade. In the `spec` section of the virtual machine configuration file:
+
. Remove the `evictionStrategy: LiveMigrate` field. See Configuring virtual machine eviction strategy for more information on how to configure eviction strategy.
. Set the `runStrategy` field to `Always`.

* Live migration fails when nodes have different CPU models. Even in cases where nodes have the same physical CPU model, differences introduced by microcode updates have the same effect. This is because the default settings trigger host CPU passthrough behavior, which is incompatible with live migration. (*BZ#1760028*)

** As a workaround, set the default CPU model by running the following command:
+
[NOTE]
====
You must make this change before starting the virtual machines that support live migration.
====
+
[source,terminal]
----
$ oc annotate --overwrite -n openshift-cnv hyperconverged kubevirt-hyperconverged kubevirt.kubevirt.io/jsonpatch='[
  {
      "op": "add",
      "path": "/spec/configuration/cpuModel",
      "value": "<cpu_model>" <1>
  }
]'
----
<1> Replace `<cpu_model>` with the actual CPU model value. You can determine this value by running `oc describe node <node>` for all nodes and looking at the `cpu-model-<name>` labels. Select the CPU model that is present on all of your nodes.

* If you enter the wrong credentials for the RHV Manager while importing a RHV VM, the Manager might lock the admin user account because the `vm-import-operator` tries repeatedly to connect to the RHV API. (*BZ#1887140*)
+
** To unlock the account, log in to the Manager and enter the following command:
+
[source,terminal]
----
$ ovirt-aaa-jdbc-tool user unlock admin
----

// fix targeted for 4.8.1
* RHV VM import fails if the VM affinity policy is `Migratable` even when live migration is enabled in {VirtProductName}. VM import succeeds if the affinity policy is `Pinned`. (*BZ#1977277*)

// fix targeted for 4.8.1
* Selecting *Create* -> *With Import wizard* on the *Virtualization* page of the {VirtProductName} console displays the following warning message:
+
[source]
----
Could not load VirtualMachines
No model registered for VirtualMachines
----
+
You can ignore this message. It does not affect VM import. (*BZ#1974812*)
