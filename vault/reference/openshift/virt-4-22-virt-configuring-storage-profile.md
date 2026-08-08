---
title: "Configuring storage profiles"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-storage-profile
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-storage-profile
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring storage profiles

[id="virt-configuring-storage-profile"]
= Configuring storage profiles

[role="_abstract"]
A storage profile provides recommended storage settings based on the associated storage class and is allocated for each storage class.

The Containerized Data Importer (CDI) recognizes a storage provider if it has been configured to identify and interact with the storage provider's capabilities.

For recognized storage types, the CDI provides values that optimize the creation of PVCs. You can also configure automatic settings for the storage class by customizing the storage profile. If the CDI does not recognize your storage provider, you must configure storage profiles.

[IMPORTANT]
====
When using {VirtProductName} with {rh-storage-first}, specify RBD block mode persistent volume claims (PVCs) when creating virtual machine disks. RBD block mode volumes are more efficient and provide better performance than Ceph FS or RBD filesystem-mode PVCs.

To specify RBD block mode PVCs, use the 'ocs-storagecluster-ceph-rbd' storage class and `VolumeMode: Block`.
====

// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-storage-profile.adoc

[id="virt-customizing-storage-profile_{context}"]
= Customizing the storage profile

[role="_abstract"]
You can specify default parameters by editing the `StorageProfile` object for the storage class of the provisioner. These default parameters only apply to the persistent volume claim (PVC) if they are not configured in the `DataVolume` object.

You cannot modify storage class parameters. To make changes, delete and re-create the storage class. You must then reapply any customizations that were previously made to the storage profile.

An empty `status` section in a storage profile indicates that a storage provisioner is not recognized by the Containerized Data Importer (CDI). Customizing a storage profile is necessary if you have a storage provisioner that is not recognized by CDI. In this case, the administrator sets appropriate values in the storage profile to ensure successful allocations.

If you are creating a snapshot of a VM, a warning is displayed if the storage class of the disk has more than one `VolumeSnapshotClass` associated with it. In this case, you must specify one volume snapshot class. Otherwise, any disk that has more than one volume snapshot class is excluded from the snapshots list.

[WARNING]
====
If you create a data volume and omit YAML attributes and these attributes are not defined in the storage profile, then the requested storage will not be allocated and the underlying persistent volume claim (PVC) will not be created.
====

.Prerequisites

* You have installed the {oc-first}.
* Ensure that your planned configuration is supported by the storage class and its provider. Specifying an incompatible configuration in a storage profile causes volume provisioning to fail.

.Procedure

. Edit the storage profile. In this example, the provisioner is not recognized by CDI.
+
[source,terminal,subs="attributes+"]
----
$ oc edit storageprofile <storage_class>
----
+
. Specify the `accessModes` and `volumeMode` values you want to configure for the storage profile. For example:
+
.Example storage profile
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: StorageProfile
metadata:
  name: <unknown_provisioner_class>
# ...
spec:
  claimPropertySets:
  - accessModes:
    - ReadWriteOnce
    volumeMode: Filesystem
status:
  provisioner: <unknown_provisioner>
  storageClass: <unknown_provisioner_class>
----
+
* `spec.claimPropertySets.accessModes` defines how the volume can be mounted. For example, `ReadWriteOnce`
* `spec.claimPropertySets.accessModes.volumeMode` defines whether the volume uses a file system or raw block storage. For example, `volumeMode`.
// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-storage-profile.adoc

[id="virt-customizing-storage-profile-snapshot-class_web_{context}"]
= Specifying a volume snapshot class by using the web console

[role="_abstract"]
If you are creating a snapshot of a VM, a warning is displayed if the storage class of the disk has more than one volume snapshot class associated with it. In this case, you must specify one volume snapshot class. Otherwise, any disk that has more than one volume snapshot class is excluded from the snapshots list.

You can specify the default volume snapshot class in the OpenShift Container Platform web console.

.Procedure

. From the *Virtualization* focused view, select *Storage*.
. Click *VolumeSnapshotClasses*.
. Select a volume snapshot class from the list.
. Click the *Annotations* pencil icon.
. Enter the following *Key*: `snapshot.storage.kubernetes.io/is-default-class`.
. Enter the following *Value*: `true`.
. Click *Save*.
// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-storage-profile.adoc

[id="virt-customizing-storage-profile-snapshot-class-cli_{context}"]
= Specifying a volume snapshot class by using the CLI

[role="_abstract"]
If you are creating a snapshot of a VM, a warning is displayed if the storage class of the disk has more than one volume snapshot class associated with it. In this case, you must specify one volume snapshot class; otherwise, any disk that has more than one volume snapshot class is excluded from the snapshots list.

You can select which volume snapshot class to use by either:

* Setting the `spec.snapshotClass` for the storage profile.
* Setting a default volume snapshot class.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Set the `VolumeSnapshotClass` you want to use. For example:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: StorageProfile
metadata:
  name: ocs-storagecluster-ceph-rbd-virtualization
spec:
  snapshotClass: ocs-storagecluster-rbdplugin-snapclass
----

* Alternatively, set the default volume snapshot class by running the following command:
+
[source,terminal]
----
# oc patch VolumeSnapshotClass ocs-storagecluster-cephfsplugin-snapclass --type=merge -p '{"metadata":{"annotations":{"snapshot.storage.kubernetes.io/is-default-class":"true"}}}'
----
// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-storage-profile.adoc

[id="virt-viewing-automatically-created-storage-profiles_{context}"]
= Viewing automatically created storage profiles

[role="_abstract"]
The system creates storage profiles for each storage class automatically. You can view these storage class profiles by using the `oc` command.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. To view the list of storage profiles, run the following command:
+
[source,terminal]
----
$ oc get storageprofile
----

. To fetch the details of a particular storage profile, run the following command:
+
[source,terminal]
----
$ oc describe storageprofile <name>
----
+
Example storage profile details:
+
[source,yaml]
----
Name:         ocs-storagecluster-ceph-rbd-virtualization
Namespace:
Labels:       app=containerized-data-importer
              app.kubernetes.io/component=storage
              app.kubernetes.io/managed-by=cdi-controller
              app.kubernetes.io/part-of=hyperconverged-cluster
              app.kubernetes.io/version=4.17.2
              cdi.kubevirt.io=
Annotations:  <none>
API Version:  cdi.kubevirt.io/v1beta1
Kind:         StorageProfile
Metadata:
  Creation Timestamp:  2023-11-13T07:58:02Z
  Generation:          2
  Owner References:
    API Version:           cdi.kubevirt.io/v1beta1
    Block Owner Deletion:  true
    Controller:            true
    Kind:                  CDI
    Name:                  cdi-kubevirt-hyperconverged
    UID:                   2d6f169a-382c-4caf-b614-a640f2ef8abb
  Resource Version:        4186799537
  UID:                     14aef804-6688-4f2e-986b-0297fd3aaa68
Spec:
Status:
  Claim Property Sets:
    accessModes:
      ReadWriteMany
    volumeMode:  Block
    accessModes:
      ReadWriteOnce
    volumeMode:  Block
    accessModes:
      ReadWriteOnce
    volumeMode:                   Filesystem
  Clone Strategy:                  csi-clone
  Data Import Cron Source Format:  snapshot
  Provisioner:                     openshift-storage.rbd.csi.ceph.com
  Snapshot Class:                  ocs-storagecluster-rbdplugin-snapclass
  Storage Class:                   ocs-storagecluster-ceph-rbd-virtualization
Events:                            <none>
----
+
`status.claimPropertySets`:: `Claim Property Sets` is an ordered list of `AccessMode`/`VolumeMode` pairs, which describe the PVC modes that are used to provision VM disks.
`status.cloneStrategy`:: The `Clone Strategy` line indicates the clone strategy to be used.
`status.dataImportCronSourceFormat`:: `Data Import Cron Source Format` indicates whether golden images on this storage are stored as PVCs or volume snapshots.
// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-storage-profile.adoc

[id="virt-customizing-storage-profile-default-cloning-strategy_{context}"]
= Setting a default cloning strategy by using a storage profile

[role="_abstract"]
You can use storage profiles to set a default cloning method for a storage class by creating a cloning strategy. This can be helpful, for example, if your storage vendor supports only certain cloning methods. It also allows you to select a method that limits resource usage or maximizes performance.

Cloning strategies are specified by setting the `cloneStrategy` attribute in a storage profile to one of the following values:

* `snapshot` is used by default when snapshots are configured. The Containerized Data Importer (CDI) uses the snapshot method if it recognizes the storage provider and the provider supports Container Storage Interface (CSI) snapshots. This cloning strategy uses a temporary volume snapshot to clone the volume.
* `copy` uses a source pod and a target pod to copy data from the source volume to the target volume. Host-assisted cloning is the least efficient method of cloning.
* `csi-clone` uses the CSI clone API to efficiently clone an existing volume without using an interim volume snapshot. Unlike `snapshot` or `copy`, which are used by default if no storage profile is defined, CSI volume cloning is used only when you specify it in the `StorageProfile` object for the storage class of the provisioner.

[NOTE]
====
You can set clone strategies by using the CLI without modifying the default `claimPropertySets` in your YAML `spec` section.
====

.Procedure

. Create or edit a `StorageProfile` object to define the cloning strategy. In the `spec` section, set the `cloneStrategy` field and define the required `claimPropertySets` values, as shown in the following example.
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: StorageProfile
metadata:
  name: <provisioner_class>
# ...
spec:
  claimPropertySets:
  - accessModes:
    - ReadWriteOnce
    volumeMode: Filesystem
  cloneStrategy: csi-clone
status:
  provisioner: <provisioner>
  storageClass: <provisioner_class>
----
+
* `accessModes` and `volumeMode` define the claim properties.
* `cloneStrategy` sets the default cloning method.

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f <storage_profile>.yaml
----
