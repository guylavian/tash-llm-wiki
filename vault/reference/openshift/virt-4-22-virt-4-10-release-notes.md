---
title: "{VirtProductName} release notes"
type: reference
domain: openshift
slug: virt-4-22-virt-4-10-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-4-10-release-notes
version: 4.22
family: virt
documentKind: "Documentation"
---

# {VirtProductName} release notes

[id="virt-4-10-release-notes"]
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
//CNV-13807 Supported guest operating systems
To view the supported guest operating systems for {VirtProductName}, refer to Certified Guest Operating Systems in Red Hat OpenStack Platform, Red Hat Virtualization and OpenShift Virtualization.

[id="virt-4-10-new"]
== New and changed features

//CNV-13851 SVVP for 4.10: Ensure platform passes Windows Server Virtualization Validation Program - with RHCOS workers
* OpenShift Virtualization is certified in Microsoft’s Windows Server Virtualization Validation Program (SVVP) to run Windows Server workloads.
+
The SVVP Certification applies to:
+
** Red Hat Enterprise Linux CoreOS workers. In the Microsoft SVVP Catalog, they are named __Red Hat OpenShift Container Platform 4 on RHEL CoreOS__.
** Intel and AMD CPUs.

//CNV-14881 Service Mesh for VMs on the primary network with IPv4 (Done in CNV-8577 for 4.9 then reverted in CNV-14481)
* {VirtProductName} is now integrated with OpenShift Service Mesh. You can connect virtual machines to a service mesh to monitor, visualize, and control traffic between pods that run virtual machine workloads on the default pod network with IPv4.

[id="virt-4-10-quick-starts"]
=== Quick starts

* Quick start tours are available for several {VirtProductName} features. To view the tours, click the *Help* icon *?* in the menu bar on the header of the {VirtProductName} console and then select *Quick Starts*. You can filter the available tours by entering the `virtualization` keyword in the *Filter* field.

[id="virt-4-10-installation-new"]
=== Installation

//CNV-14192 Update launchers using live-migration - default/opt out
* {VirtProductName} workloads, such as `virt-launcher` pods, now automatically update if they support live migration. You can configure workload update strategies or opt out of future automatic updates by editing the `HyperConverged` custom resource.

//CNV-16637 SNO availability
* You can now use {VirtProductName} with single node clusters, also known as Single Node OpenShift (SNO).
+
[NOTE]
====
Single node clusters are not configured for high-availability operation, which results in significant changes to {VirtProductName} behavior.
====

//CNV-14910 HyperConverged Operator technical debt

//CNV-16636 Resource requests and priority classes
* Resource requests and priority classes are now defined for all {VirtProductName} control plane components.

[id="virt-4-10-networking-new"]
=== Networking

//CNV-11201 Rollout of NodeNetworkConfigurationPolicy
* You can now configure multiple nmstate-enabled nodes concurrently by using a single `NodeNetworkConfigurationPolicy` manifest.

//CNV-13679 SR-IOV live-migration without privilege escalation
* Live migration is now supported by default for virtual machines that are attached to an SR-IOV network interface.

[id="virt-4-10-storage-new"]
=== Storage

//CNV-16641 Snapshot improvements
* Online snapshots are supported for virtual machines that have hot-plugged virtual disks. However, hot-plugged disks that are not in the virtual machine specification are not included in the snapshot.

//CNV-16673 New CSI driver for HPP
* You can use the Kubernetes Container Storage Interface (CSI) driver with the hostpath provisioner (HPP)  to configure local storage for your virtual machines. Using the CSI driver minimizes disruption to your existing OpenShift Container Platform nodes and clusters when configuring local storage.

[id="virt-4-10-web-new"]
=== Web console

// NOTE: Comment out deprecated and removed features (and their IDs) if not used in a release
[id="virt-4-10-deprecated-removed"]
== Deprecated and removed features

[id="virt-4-10-deprecated"]
=== Deprecated features

Deprecated features are included in the current release and supported. However, they will be removed in a future release and are not recommended for new deployments.

* In a future release, support for the legacy HPP custom resource, and the associated storage class, will be deprecated. Beginning in {VirtProductName} {VirtVersion}, the HPP Operator uses the Kubernetes Container Storage Interface (CSI) driver to configure local storage. The Operator continues to support the existing (legacy) format of the HPP custom resource and the associated storage class. If you use the HPP Operator, plan to create a storage class for the CSI driver as part of your migration strategy.
// NOTE: when uncommenting deprecated features list, change the header level below to ===

[id="virt-4-10-removed"]
=== Removed features

Removed features are not supported in the current release.

* The VM Import Operator has been removed from {VirtProductName} with this release. It is replaced by the Migration Toolkit for Virtualization.

// NOTE: no notable technical changes in 4.9, commenting out to retain
//[id="virt-4-10-changes"]
//== Notable technical changes

//CNV-16642 - Dashboard feature.
* The {VirtProductName} dashboard provides resource consumption data for virtual machines and associated pods. The visualization metrics displayed in the {VirtProductName} dashboard are based on Prometheus Query Language (PromQL) queries.

[id="virt-4-10-technology-preview"]
== Technology Preview features

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use. Note the following scope of support on the Red Hat Customer Portal for these features:

Technology Preview Features Support Scope

* You can now use the Red Hat Enterprise Linux 9 Alpha template to create virtual machines.

* You can now deploy {VirtProductName} on AWS bare metal nodes.

* {VirtProductName} has critical alerts that inform you when a problem occurs that requires immediate attention. Now, each alert has a corresponding description of the problem, a reason for why the alert is occurring, a troubleshooting process to diagnose the source of the problem, and steps for resolving the alert.

* A cluster administrator can now back up namespaces that contain VMs by using the OpenShift API for Data Protection with the `kubevirt` plug-in.

* Administrators can now declaratively create and expose mediated devices such as virtual graphics processing units (vGPUs) by editing the `HyperConverged` CR. Virtual machine owners can then assign these devices to VMs.

//CNV-13660 Inherit static IP from a NIC attached to the bridge
* You can transfer the static IP configuration of the NIC attached to the bridge by applying a single `NodeNetworkConfigurationPolicy` manifest to the cluster.

//CNV-16639
* You can now install {VirtProductName} on IBM Cloud bare-metal servers. Bare-metal servers offered by other cloud providers are not supported.

[id="virt-4-10-bug-fixes"]
== Bug fixes

[id="virt-4-10-known-issues"]
== Known issues

//Known issues at time of 4.10 release
//BZ-2054650
* The web console does not display virtual machine templates that are deployed to a custom namespace. Only templates deployed to the default namespace will display in the web console. (*BZ#2056623*)
+
** As a workaround, avoid deploying templates to a custom namespace.

//Known issues at time of 4.9 release
//BZ-2007397
* If you hot-plug a virtual disk and then force delete the `virt-launcher` pod, you might lose data. This is due to a race condition that can cause the VM disk's contents to be wiped from the persistent volume. (*BZ#2007397*)

// Review this for permanent doc home in 4.10
* Editing a virtual machine fails if the VM references a deleted template that was provided by {VirtProductName} before version 4.8. In {VirtProductName} 4.8 and later, deleted {VirtProductName}-provided templates are automatically recreated by the {VirtProductName} Operator.

* If a cloning operation is initiated before the source is available to be cloned, the operation stalls indefinitely. This is because the clone authorization expires before the cloning operation starts. (*BZ#1855182*)
+
** As a workaround, delete the `DataVolume` object that is requesting the clone. When the source is available, recreate the `DataVolume` object that you deleted so that the cloning operation can complete successfully.

* If your OpenShift Container Platform cluster uses OVN-Kubernetes as the default Container Network Interface (CNI) provider, you cannot attach a Linux bridge or bonding to the default interface of a host because of a change in the host network topology of OVN-Kubernetes. (*BZ#1885605*)

** As a workaround, you can use a secondary network interface connected to your host, or switch to the OpenShift SDN default CNI provider.

// Review this for permanent doc home in 4.10
* Running virtual machines that cannot be live migrated might block an OpenShift Container Platform cluster upgrade. This includes virtual machines that use hostpath provisioner storage or SR-IOV network interfaces.

** As a workaround, you can reconfigure the virtual machines so that they can be powered off during a cluster upgrade. In the `spec` section of the virtual machine configuration file:
+
. Remove the `evictionStrategy: LiveMigrate` field. See Configuring virtual machine eviction strategy for more information on how to configure eviction strategy.
. Set the `runStrategy` field to `Always`.

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

* If you run {VirtProductName} 2.6.5 with OpenShift Container Platform 4.8 or later, various issues occur. You can avoid these issues by upgrading {VirtProductName} to version 4.8 or later.
+
** In the web console, if you navigate to the *Virtualization* page and select *Create* -> *With YAML* the following error message is displayed:
+
[source,text]
----
The server doesn't have a resource type "kind: VirtualMachine, apiVersion: kubevirt.io/v1"
----
+
*** As a workaround, edit the `VirtualMachine` manifest so the `apiVersion` is `kubevirt.io/v1alpha3`. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1alpha3
kind: VirtualMachine
metadata:
  annotations:
...
----
+
(*BZ#1979114*)
+
** When connecting to the VNC console by using the {VirtProductName} web console, the VNC console always fails to respond.
+
*** As a workaround, create the virtual machine from the CLI or upgrade to {VirtProductName} 4.8.
+
(*BZ#1977037*)

//Known issues discovered after 4.9 release

* If a single node contains more than 50 images, pod scheduling might be imbalanced across nodes. This is because the list of images on a node is shortened to 50 by default.
** As a workaround, you can disable the image limit by editing the `KubeletConfig` object and setting the value of `nodeStatusMaxImages` to `-1`. (*BZ#1984442*)
