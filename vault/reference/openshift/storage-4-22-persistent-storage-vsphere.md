---
title: "Persistent storage using VMware vSphere volumes"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-vsphere
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using VMware vSphere volumes

[id="persistent-storage-using-vsphere"]
= Persistent storage using VMware vSphere volumes

OpenShift Container Platform allows use of VMware vSphere's Virtual Machine Disk (VMDK) volumes. You can provision your OpenShift Container Platform cluster with persistent storage using VMware vSphere. Some familiarity with Kubernetes and VMware vSphere is assumed.

VMware vSphere volumes can be provisioned dynamically. OpenShift Container Platform creates the disk in vSphere and attaches this disk to the correct image.

[NOTE]
====
OpenShift Container Platform provisions new volumes as independent persistent disks that can freely attach and detach the volume on any node in the cluster. Consequently, you cannot back up volumes that use snapshots, or restore volumes from snapshots. See Snapshot Limitations for more information.
====

The Kubernetes persistent volume framework allows administrators to provision a
cluster with persistent storage and gives users a way to request those
resources without having any knowledge of the underlying infrastructure.

Persistent volumes are not bound to a single project or namespace; they can be
shared across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace and can be
requested by users.

[IMPORTANT]
====
For new installations, OpenShift Container Platform 4.13 and later provides automatic migration for the vSphere in-tree volume plugin to its equivalent CSI driver. Updating to OpenShift Container Platform 4.15 and later also provides automatic migration. For more information about updating and migration, see CSI automatic migration.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes.
====

[role="_additional-resources"]
.Additional resources

* VMware vSphere

== Dynamically provisioning VMware vSphere volumes

Dynamically provisioning VMware vSphere volumes is the recommended method.

== Prerequisites
* An OpenShift Container Platform cluster installed on a VMware vSphere version that meets the requirements for the components that you use. See Installing a cluster on vSphere for information about vSphere version support.

You can use either of the following procedures to dynamically provision these volumes using the default storage class.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc

[id="vsphere-dynamic-provisioning_{context}"]
= Dynamically provisioning VMware vSphere volumes using the UI

OpenShift Container Platform installs a default storage class, named `thin`, that uses the `thin` disk format for provisioning volumes.

.Prerequisites

* Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

.Procedure

. In the OpenShift Container Platform console, click *Storage* → *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume Claim*.

. Define the required options on the resulting page.

.. Select the `thin` storage class.

.. Enter a unique name for the storage claim.

.. Select the access mode to determine the read and write access for the created storage claim.

.. Define the size of the storage claim.

. Click *Create* to create the persistent volume claim and generate a persistent volume.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc

[id="vsphere-dynamic-provisioning-cli_{context}"]
= Dynamically provisioning VMware vSphere volumes using the CLI

OpenShift Container Platform installs a default StorageClass, named `thin`, that uses the `thin` disk format for provisioning volumes.

.Prerequisites

* Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

.Procedure (CLI)

. You can define a VMware vSphere PersistentVolumeClaim by creating a file, `pvc.yaml`, with the following contents:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvc <1>
spec:
  accessModes:
  - ReadWriteOnce <2>
  resources:
    requests:
      storage: 1Gi <3>
----
<1> A unique name that represents the persistent volume claim.
<2> The access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.
<3> The size of the persistent volume claim.

. Enter the following command to create the `PersistentVolumeClaim` object from the file:
+
[source,terminal]
----
$ oc create -f pvc.yaml
----

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc

[id="vsphere-static-provisioning_{context}"]
= Statically provisioning VMware vSphere volumes

To statically provision VMware vSphere volumes you must create the virtual machine disks for reference by the persistent volume framework.

.Prerequisites

* Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

.Procedure

. Create the virtual machine disks. Virtual machine disks (VMDKs) must be created manually before statically provisioning VMware vSphere volumes. Use either of the following methods:

  * Create using `vmkfstools`. Access ESX through Secure Shell (SSH) and then use following command to create a VMDK volume:
+
[source,terminal]
----
$ vmkfstools -c <size> /vmfs/volumes/<datastore-name>/volumes/<disk-name>.vmdk
----

  * Create using `vmware-diskmanager`:
+
[source,terminal]
----
$ shell vmware-vdiskmanager -c -t 0 -s <size> -a lsilogic <disk-name>.vmdk
----

. Create a persistent volume that references the VMDKs. Create a file, `pv1.yaml`, with the `PersistentVolume` object definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv1 <1>
spec:
  capacity:
    storage: 1Gi <2>
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  vsphereVolume: <3>
    volumePath: "[datastore1] volumes/myDisk"  <4>
    fsType: ext4  <5>
----
<1> The name of the volume. This name is how it is identified by persistent volume claims or pods.
<2> The amount of storage allocated to this volume.
<3> The volume type used, with `vsphereVolume` for vSphere volumes. The label is used to mount a vSphere VMDK volume into pods. The contents of a volume are preserved when it is unmounted. The volume type supports VMFS and VSAN datastore.
<4> The existing VMDK volume to use. If you used `vmkfstools`, you must enclose the datastore name in square brackets, `[]`, in the volume definition, as shown previously.
<5> The file system type to mount. For example, ext4, xfs, or other file systems.
+
[IMPORTANT]
====
Changing the value of the fsType parameter after the volume is formatted and provisioned can result in data loss and pod failure.
====

. Create the `PersistentVolume` object from the file:
+
[source,terminal]
----
$ oc create -f pv1.yaml
----

. Create a persistent volume claim that maps to the persistent volume you created in the previous step.  Create a file, `pvc1.yaml`, with the `PersistentVolumeClaim` object definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc1 <1>
spec:
  accessModes:
    - ReadWriteOnce <2>
  resources:
   requests:
     storage: "1Gi" <3>
  volumeName: pv1 <4>
----
<1> A unique name that represents the persistent volume claim.
<2> The access mode of the persistent volume claim. With ReadWriteOnce, the volume can be mounted with read and write permissions by a single node.
<3> The size of the persistent volume claim.
<4> The name of the existing persistent volume.

. Create the `PersistentVolumeClaim` object from the file:
+
[source,terminal]
----
$ oc create -f pvc1.yaml
----

// Module included in the following assemblies
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc

[id="vsphere-formatting-volumes_{context}"]
= Formatting VMware vSphere volumes

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks that the volume contains a file system that is specified by the `fsType` parameter value in the `PersistentVolume` (PV) definition. If the device is not formatted with the file system, all data from the device is erased, and the device is automatically formatted with the specified file system.

Because OpenShift Container Platform formats them before the first use, you can use unformatted vSphere volumes as PVs.
