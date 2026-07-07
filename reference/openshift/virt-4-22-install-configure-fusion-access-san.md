---
title: "Using {VirtProductName} with {IBMFusionFirst}"
type: reference
domain: openshift
slug: virt-4-22-install-configure-fusion-access-san
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/install-configure-fusion-access-san
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using {VirtProductName} with {IBMFusionFirst}

[id="install-configure-fusion-access-san"]
= Using {VirtProductName} with {IBMFusionFirst}

[role="_abstract"]
You configure SAN-based storage for virtual machines by using {IBMFusionFirst} with {VirtProductName}. You must install the {FusionSAN} Operator (Fusion Access for SAN) and set up the storage cluster and file systems.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="about-fusion-access-san_{context}"]
= About {IBMFusionFirst}

[role="_abstract"]
{IBMFusionFirst} provides a scalable clustered file system for enterprise storage, primarily designed to offer access to consolidated, block-level data storage. It presents storage devices, such as disk arrays, to the operating system as if they were direct-attached storage.

{IBMFusionFirst} uses existing Storage Area Network (SAN) infrastructure to provide enterprise storage for {VirtProductName}. A SAN is a dedicated network of storage devices that is typically not accessible through the local area network (LAN).

To use {VirtProductName} with {IBMFusionFirst}, you must first install the {FusionSAN} Operator.

Then you must create a Kubernetes pull secret and create the `FusionAccess` custom resource (CR).

Finally, follow the OpenShift Container Platform web console wizard to configure the storage cluster, local disk, and file systems.

[id="why-use-fusion-san_{context}"]
== Why use {FusionSAN}

Easy user experience:: {FusionSAN} features a wizard-driven user interface (UI) for installing and configuring storage clusters, file systems, and storage classes, to simplify the setup process.

Use existing infrastructure:: Organizations can use their existing SAN investments, including Fibre Channel (FC) and iSCSI technologies, as they migrate to or expand with {VirtProductName}.

Scalability:: The storage cluster is designed to scale with OpenShift Container Platform clusters and virtual machine (VM) workloads. It can support up to approximately 3000 VMs on 6 bare-metal hosts, with possibilities for further scaling by adding more file systems or using specific storage class parameters.

Consolidated and shared storage:: SANs enable multiple servers to access a large, shared data storage capacity. This architecture facilitates automatic data backup and continuous monitoring of the storage and backup processes.

High-speed data transfer:: By using a dedicated high-speed network for storage, {FusionSAN} overcomes the data transfer bottlenecks that can occur over a traditional LAN, especially for large volumes of data.

File-level access:: Although a SAN primarily operates at the block level, file systems built on top of SAN storage can provide file-level access through shared-disk file systems.

Centralized management:: The underlying SAN software manages servers, storage devices, and the network to ensure that data moves directly between storage devices with minimal server intervention. It also supports centralized management and configuration of SAN components such as Logical Unit Numbers (LUNs).

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="fusion-access-san-prereqs_{context}"]
= Prerequisites and Limitations for {FusionSAN}

[role="_abstract"]
Prerequisites and limitations are provided for installing and configuring {FusionSAN}.

== Prerequisites

Installing and configuring {FusionSAN} require the following prerequisites:

* Bare-metal worker nodes with attached SAN storage.
* A working container registry enabled.
* All worker nodes must connect to the same LUNs.
+
A shared LUN is a shared disk that is accessed by all worker nodes simultaneously.
* A Kubernetes pull secret.

== Limitations

* Limitations for {FusionSAN} rely on the IBM Storage Scale container native limitations and can be found in the documentation for https://www.ibm.com/docs/en/scalecontainernative/5.2.3?topic=overview-limitations[IBM Storage Scale container native].
* Hosted control planes (HCP) clusters are not supported.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="installing-fusion-access-operator_{context}"]
= Installing the {FusionSAN} Operator

[role="_abstract"]
You can install the {FusionSAN} Operator from the software catalog in the OpenShift Container Platform web console.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a working container registry enabled.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.

. In the *Filter by keyword* field, type `Fusion Access for SAN`.

. Select the *{FusionSAN}* tile and click *Install*.

. On the *Install Operator* page, keep the default selections for *Update Channel*, *Version*, and *Installation mode*.

. Verify that *Operator recommended Namespace* is selected for *Installed Namespace*.
+
This installs the Operator in the `ibm-fusion-access` namespace. If this namespace does not yet exist, it is automatically created.
+
[WARNING]
====
You must install the {FusionSAN} Operator in the `ibm-fusion-access` namespace. Installation in any other namespace is not supported.
====

. Verify that the *Automatic* default is selected for *Update Approval*.
+
This enables automatic updates when a new z-stream release is available.

. Click *Install*.
+
This installs the Operator.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.

. Verify that the {FusionSAN} Operator is displayed.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="creating-pull-secret-fusion-san_{context}"]
= Creating a Kubernetes pull secret

[role="_abstract"]
After installing the {FusionSAN} Operator, you must create a Kubernetes secret object to hold the IBM entitlement key for pulling the required container images from the IBM container registry.

.Prerequisites

* You installed the `oc` CLI.
* You have access to the cluster as a user with the `cluster-admin` role.
* You installed the {FusionSAN} Operator and created the `ibm-fusion-access` namespace in the process.

.Procedure

. Log in to the https://myibm.ibm.com/products-services/containerlibrary[*IBM Container software library*] with your {FusionSAN} *IBMid* and *password*.

. In the *IBM Container software library*, get the entitlement key:

.. If you do not have an entitlement key yet, click *Get entitlement key* or *Add new key*, and then click *Copy*.

.. If you already have an entitlement key, click *Copy*.

. Save the entitlement key in a safe place.

. Create the secret object by running the `oc create` command, replacing `<ibm-entitlement-key>` with the entitlement key that you copied in step 2.
+
[source,terminal]
----
$ oc create secret -n ibm-fusion-access generic fusion-pullsecret \
--from-literal=ibm-entitlement-key=<ibm-entitlement-key>
----

.Verification

. In the OpenShift Container Platform web console, navigate to *Workloads* -> *Secrets*.

. Find the `fusion-pullsecret` in the list.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="creating-fusionaccess-cr_{context}"]
= Creating the FusionAccess CR

[role="_abstract"]
After installing the {FusionSAN} Operator and creating a Kubernetes pull secret, you must create the `FusionAccess` custom resource (CR).

Creating the `FusionAccess` CR triggers the installation of the correct version of IBM Storage Scale and detects worker nodes with shared LUNs.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You installed the {FusionSAN} Operator.
* You created a Kubernetes pull secret.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators*.

. Click the {FusionSAN} Operator you installed.

. In the *Fusion Access for SAN* page, select the *Fusion Access* tab.

. Click *Create FusionAccess*.

. On the *Create FusionAccess* page, enter the object *Name*.

. Optional: You can choose to add *Labels* if they are relevant.

. Select the *IBM Storage Scale Version* from the drop-down list.

. Click *Create*.

.Verification

* In the *Fusion Access for SAN* Operator page, in the *Fusion Access* tab, verify that the created `FusionAccess` CR is displayed with the status *Ready*.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="creating-storage-cluster-fusion-access-san_{context}"]
= Creating a storage cluster with {FusionSAN}

[role="_abstract"]
Once you have installed the {FusionSAN} Operator, you can create a storage cluster with shared storage nodes.

The wizard for creating the storage cluster in the OpenShift Container Platform web console provides easy-to-follow steps and lists the relevant worker nodes with shared disks.

.Prerequisites

* You have bare-metal worker nodes with visible and attached shared LUNs.
+
A shared LUN is a shared disk that is accessed by all workers simultaneously.
* You installed the {FusionSAN} Operator.
* You created the `FusionAccess` custom resource (CR) in the `ibm-fusion-access` namespace.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Storage* -> *{FusionSAN}*.

. Click *Create storage cluster*.

. Select the worker nodes that have shared LUNs.
+
[NOTE]
====
You can only select worker nodes with a minimum of 20 GB of RAM from the list.
====

. Click *Create storage cluster*.
+
The page reloads, opening the {FusionSAN} page for the new storage cluster.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="creating-filesystem-fusion-access-san_{context}"]
= Creating a file system with {FusionSAN}

[role="_abstract"]
You need to create a file system to represent your required storage.

The file system is based on the storage available in the worker nodes you selected when creating the storage cluster.

.Prerequisites

* You created a {FusionSAN} storage cluster.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Storage* -> *{FusionSAN}*.

. In the *File systems* tab, click *Create file system*.

. Enter a *Name* for the new file system.

. Select the LUNs that you want to use as the storage volumes for your file system.

. Click *Create file system*.
+
The *{FusionSAN}* page reloads, and the new file system is displayed in the *File systems* tab.

.Next steps

Repeat this procedure for each file system that you want to create.

.Verification

. Watch the *Status* of the file system in the *File systems* tab until it is marked as *Healthy*. This might take several minutes.

. Click the *StorageClass* for the file system.

. In the *YAML* tab, verify the following:
+
.. The value in the `name` field is the name of the file system you created.
.. The value in the `provisioner` field is `spectrumscale.csi.ibm.com`.
.. The value in the `volBackendFs` field matches the name of the file system you created.
+
[source,yaml,subs="attributes+"]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: filesystem1
  uid: eb410309-a043-a89b-9bb05483872a
  resourceVersion: '87746'
  creationTimestamp: '2025-05-14T12:30:08Z'
  managedFields:
provisioner: spectrumscale.csi.ibm.com
parameters:
  volBackendFs: filesystem1
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: Immediate
----

// Module included in the following assemblies:
//
// * virt/storage/install-configure-fusion-access-san.adoc

[id="troubleshoot-fusion-access-san_{context}"]
= Troubleshooting {IBMFusionFirst}

[role="_abstract"]

If you encounter issues with {IBMFusionFirst}, provide the must-gather image to Red{nbsp}Hat support. This image contains critical data about your cluster and project resources, logs, and events from your deployment.

.Procedure

. To obtain the deployed version of {IBMFusionFirst}, run the following command:
+
[source,terminal]
----
$ oc get fusionaccesses.fusion.storage.openshift.io  -n ibm-fusion-access fusionaccess-sample -o jsonpath='{.spec.storageScaleVersion}'
----
+
[NOTE]
====
This command returns the numeric value of the deployed version of {IBMFusionFirst} such as `2.11.0`.
====

. To create the `must-gather` image, run the following command:
+
[source,terminal]
----
$ oc adm must-gather --image=icr.io/cpopen/ibm-spectrum-scale-must-gather:v<software_version>
----
+
* Replace `<software_version>` with the {IBMFusionFirst} version value.

// Module included in the following assemblies:
//
// * virt/fusion_access_SAN/install-configure-fusion-access-san.adoc

[id="virt-fusion-access-san-release-updates_{context}"]
= {IBMFusionFirst} release updates

[role="_abstract"]
Release updates for {IBMFusionFirst}, including new features, bug fixes, and known issues.

[id="virt-fusion-access-san-new-changes_{context}"]
== New and changed features

{IBMFusionFirst} 1.1.0 includes Spectrum Scale 5.2.3.5::

{IBMFusionFirst} 1.1.0 uses Spectrum Scale version 5.2.3.5. When you upgrade to {IBMFusionFirst} 1.1.0, Spectrum Scale is automatically upgraded to version 5.2.3.5.
+
OCPNAS-294
+
OCPNAS-279

Backend redesign for `FileSystemClaim` resources::

{IBMFusionFirst} updates the backend to use `FileSystemClaim` resources for managing filesystem related objects. Previously, filesystem creation could fail if the process was interrupted. With this update, backend handling improves reliability while keeping the user interface flow and appearance unchanged.
+
After you upgrade to {IBMFusionFirst} 1.1.0, resources that were created by using the 1.0 user interface are automatically migrated and associated with a `FileSystemClaim` resource.
+
OCPNAS-241

Automatic creation of `VolumeSnapshotClass` resources for filesystems::

{IBMFusionFirst} now creates a `VolumeSnapshotClass` resource alongside the `StorageClass` resource for each filesystem. This ensures that snapshot support is consistently available for newly created filesystems.
+
After upgrading from {IBMFusionFirst} 1.0 to 1.1.0, a `VolumeSnapshotClass` resource is automatically created for existing filesystems that did not previously have one.
+
OCPNAS-293

Image registry requirements for kernel module management::

{IBMFusionFirst} uses the OpenShift Container Platform image registry to manage the kernel module. Do not configure the registry to use `emptyDir` storage because it provides only temporary storage and is not suitable for production use. Configure {IBMFusionFirst} to use a different image registry by creating a config map and secret after installing the Operator and before creating the `FusionAccess` CR.
+
OCPNAS-213

[id="virt-fusion-access-san-bug-fixes_{context}"]
== Bug fixes

Filesystem creation button stays disabled until daemons are ready::

The {IBMFusionFirst} Operator was updated to check the readiness of filesystem daemons before allowing a filesystem to be created. The **Create file system** button in the web console now stays disabled with a tooltip explaining the condition until the environment is ready. This change prevents filesystems from appearing stuck during creation.
+
OCPNAS-184

Filesystems cannot be deleted from the user interface::

The OpenShift Container Platform web console does not support deleting filesystems. To delete a filesystem, use the {oc-first}.
+
OCPNAS-217

[id="virt-fusion-access-san-known-issues_{context}"]
== Known issues

Filesystem creation might fail during core pod deletion::

Filesystem creation might fail if core pods are deleted at the same time. The filesystem might be partially created on the LUN, which results in the following persistent error:
+
[source,terminal]
----
Disk <ID> may still belong to an active file system
----
+
No workaround is available. Contact IBM Support for assistance.
+
OCPNAS-233

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Creating virtual machines from instance types

* Creating virtual machines from templates
