---
title: "Backup and restore by using VM snapshots"
type: reference
domain: openshift
slug: virt-4-22-virt-backup-restore-snapshots
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-backup-restore-snapshots
version: 4.22
family: virt
documentKind: "Documentation"
---

# Backup and restore by using VM snapshots

[id="virt-backup-restore-snapshots"]
= Backup and restore by using VM snapshots

[role="_abstract"]
You can back up and restore virtual machines (VMs) by using snapshots. Snapshots are supported by the following storage providers:

// Hiding in ROSA/OSD as not supported
* {rh-storage-first}
* Any other cloud storage provider with the Container Storage Interface (CSI) driver that supports the Kubernetes Volume Snapshot API
* Any cloud storage provider with the Container Storage Interface (CSI) driver that supports the Kubernetes Volume Snapshot API

To create snapshots of a VM in the `Running` state with the highest integrity, install the QEMU guest agent if it is not included with your operating system. The QEMU guest agent is included with the default Red{nbsp}Hat templates.

[IMPORTANT]
====
Online snapshots are supported for virtual machines that have hot plugged virtual disks. However, hot plugged disks that are not in the virtual machine specification are not included in the snapshot.

Ensure that the QEMU guest agent is installed and running on the virtual machine before you take an online snapshot.

The QEMU guest agent stops responding to file system operations to ensure that the snapshot captures a consistent state.
====

The QEMU guest agent takes a consistent snapshot by attempting to quiesce the VM file system. This ensures that in-flight I/O is written to the disk before the snapshot is taken. If the guest agent is not present, quiescing is not possible and a best-effort snapshot is taken.

The conditions under which a snapshot is taken are reflected in the snapshot indications that are displayed in the web console or CLI. If these conditions do not meet your requirements, try creating the snapshot again or use an offline snapshot

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-about-vm-snapshots_{context}"]
= About snapshots

[role="_abstract"]
A _snapshot_ represents the state and data of a virtual machine (VM) at a specific point in time. You can use a snapshot to restore an existing VM to a previous state (represented by
the snapshot) for backup and disaster recovery or to rapidly roll back to a previous development version.

A VM snapshot is created from a VM that is powered off (Stopped state) or powered on (Running state).

When taking a snapshot of a running VM, the controller checks that the QEMU guest agent is installed and running. If so, it freezes the VM file system before taking the snapshot, and thaws the file system after the snapshot is taken.

The snapshot stores a copy of each Container Storage Interface (CSI) volume attached to the VM and a copy of the VM specification and metadata. Snapshots cannot be changed after creation.

You can perform the following snapshot actions:

* Create a new snapshot
* Create a clone of a virtual machine from a snapshot
+
[IMPORTANT]
====
Cloning a VM with a vTPM device attached to it or creating a new VM from its snapshot is not supported.
====

* List all snapshots attached to a specific VM
* Restore a VM from a snapshot
* Delete an existing VM snapshot

== VM snapshot controller and custom resources

The VM snapshot feature introduces three new API objects defined as custom resource definitions (CRDs) for managing snapshots:

* `VirtualMachineSnapshot`: Represents a user request to create a snapshot. It contains information about the current state of the VM.
* `VirtualMachineSnapshotContent`: Represents a provisioned resource on the cluster (a snapshot). It is created by the VM snapshot controller and contains references to all resources required to restore the VM.
* `VirtualMachineRestore`: Represents a user request to restore a VM from a snapshot.

The VM snapshot controller binds a `VirtualMachineSnapshotContent` object with the `VirtualMachineSnapshot` object for which it was created, with a one-to-one mapping.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-backup-restore-snapshots.adoc

[id="virt-about-application-consistent-backups_{context}"]
= About application-consistent snapshots and backups

[role="_abstract"]
You can configure application-consistent snapshots and backups for Linux or Windows virtual machines (VMs) through a cycle of freezing and thawing. For any application, you can configure a script on a Linux VM or register on a Windows VM to be notified when a snapshot or backup is due to begin.

On a Linux VM, freeze and thaw processes trigger automatically when a snapshot is taken or a backup is started by using, for example, a plugin from Velero or another backup vendor. The freeze process, performed by QEMU Guest Agent (QEMU GA) freeze hooks, ensures that before the snapshot or backup of a VM occurs, all of the VM's filesystems are frozen and each appropriately configured application is informed that a snapshot or backup is about to start. This notification affords each application the opportunity to quiesce its state. Depending on the application, quiescing might involve temporarily refusing new requests, finishing in-progress operations, and flushing data to disk. The operating system is then directed to quiesce the filesystems by flushing outstanding writes to disk and freezing new write activity. All new connection requests are refused. When all applications have become inactive, the QEMU GA freezes the filesystems, and a snapshot is taken or a backup initiated. After the taking of the snapshot or start of the backup, the thawing process begins. Filesystems writing is reactivated and applications receive notification to resume normal operations.

The same cycle of freezing and thawing is available on a Windows VM. Applications register with the Volume Shadow Copy Service (VSS) to receive notifications that they should flush out their data because a backup or snapshot is imminent. Thawing of the applications after the backup or snapshot is complete returns them to an active state. For more details, see the Windows Server documentation about the Volume Shadow Copy Service.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-creating-vm-snapshot-web_{context}"]
= Creating a snapshot by using the web console

[role="_abstract"]
You can create a snapshot of a virtual machine (VM) by using the OpenShift Container Platform web console.

.Prerequisites

* The `snapshot` feature gate is enabled in the YAML configuration of the `kubevirt` CR.

* The VM snapshot includes disks that meet the following requirements:
** The disks are data volumes or persistent volume claims.
** The disks belong to a storage class that supports Container Storage Interface (CSI) volume snapshots.
** The disks are _bound_ to a persistent volume (PV) and _populated_ with a datasource.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. Click the *Snapshots* tab and then click *Take Snapshot*.
+
Alternatively, right-click the VM and select *Create snapshot* from the menu.
. Enter the snapshot name.
. Expand *Disks included in this Snapshot* to see the storage volumes to be included in the snapshot.
. If your VM has disks that cannot be included in the snapshot and you wish to proceed, select *I am aware of this warning and wish to proceed*.
. Click *Save*.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-creating-vm-snapshot-cli_{context}"]
= Creating a snapshot by using the CLI

[role="_abstract"]
You can create a virtual machine (VM) snapshot for an offline or online VM by creating a `VirtualMachineSnapshot` object.

.Prerequisites

* Ensure the `Snapshot` feature gate is enabled for the `kubevirt` CR by using the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get kubevirt kubevirt-hyperconverged -n {CNVNamespace} -o yaml
----
+
Truncated output:
+
[source,yaml]
----
spec:
  developerConfiguration:
    featureGates:
      - Snapshot
----

* Ensure that the VM snapshot includes disks that meet the following requirements:
** The disks are data volumes or persistent volume claims.
** The disks belong to a storage class that supports Container Storage Interface (CSI) volume snapshots.
** The disks are _bound_ to a persistent volume (PV) and _populated_ with a datasource.

* Install the OpenShift CLI (`oc`).
* Optional: Power down the VM for which you want to create a snapshot.

.Procedure

. Create a YAML file to define a `VirtualMachineSnapshot` object that specifies the name of the new `VirtualMachineSnapshot` and the name of the source VM as in the following example:
+
[source,yaml]
----
apiVersion: snapshot.kubevirt.io/v1beta1
kind: VirtualMachineSnapshot
metadata:
  name: <snapshot_name>
spec:
  source:
    apiGroup: kubevirt.io
    kind: VirtualMachine
    name: <vm_name>
----

. Create the `VirtualMachineSnapshot` object:
+
[source,terminal]
----
$ oc create -f <snapshot_name>.yaml
----
+
The snapshot controller creates a `VirtualMachineSnapshotContent` object, binds it to the `VirtualMachineSnapshot`, and updates the `status` and `readyToUse` fields of the `VirtualMachineSnapshot` object.

.Verification

. Optional: During the snapshot creation process, you can use the `wait` command to monitor the status of the snapshot and wait until it is ready for use:
.. Enter the following command:
+
[source,terminal]
----
$ oc wait <vm_name> <snapshot_name> --for condition=Ready
----

.. Verify the status of the snapshot:
* `InProgress` - The snapshot operation is still in progress.
* `Succeeded` - The snapshot operation completed successfully.
* `Failed` - The snapshot operaton failed.
+
[NOTE]
====
Online snapshots have a default time deadline of five minutes (`5m`). If the snapshot does not complete successfully in five minutes, the status is set to `failed`. Afterwards, the file system will be thawed and the VM unfrozen but the status remains `failed` until you delete the failed snapshot image.

To change the default time deadline, add the `FailureDeadline` attribute to the VM snapshot spec with the time designated in minutes (`m`) or in seconds (`s`) that you want to specify before the snapshot operation times out.

To set no deadline, you can specify `0`, though this is generally not recommended, as it can result in an unresponsive VM.

If you do not specify a unit of time such as `m` or `s`, the default is seconds (`s`).
====

. Verify that the `VirtualMachineSnapshot` object is created and bound with `VirtualMachineSnapshotContent` and that the `readyToUse` flag is set to `true`:
+
[source,terminal]
----
$ oc describe vmsnapshot <snapshot_name>
----
+
Example output:
+
[source,yaml]
----
apiVersion: snapshot.kubevirt.io/v1beta1
kind: VirtualMachineSnapshot
metadata:
  creationTimestamp: "2020-09-30T14:41:51Z"
  finalizers:
  - snapshot.kubevirt.io/vmsnapshot-protection
  generation: 5
  name: mysnap
  namespace: default
  resourceVersion: "3897"
  selfLink: /apis/snapshot.kubevirt.io/v1beta1/namespaces/default/virtualmachinesnapshots/my-vmsnapshot
  uid: 28eedf08-5d6a-42c1-969c-2eda58e2a78d
spec:
  source:
    apiGroup: kubevirt.io
    kind: VirtualMachine
    name: my-vm
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2020-09-30T14:42:03Z"
    reason: Operation complete
    status: "False"
    type: Progressing
  - lastProbeTime: null
    lastTransitionTime: "2020-09-30T14:42:03Z"
    reason: Operation complete
    status: "True"
    type: Ready
  creationTime: "2020-09-30T14:42:03Z"
  readyToUse: true
  sourceUID: 355897f3-73a0-4ec4-83d3-3c2df9486f4f
  virtualMachineSnapshotContentName: vmsnapshot-content-28eedf08-5d6a-42c1-969c-2eda58e2a78d
  indications:
    - Online
  includedVolumes:
    - name: rootdisk
      kind: PersistentVolumeClaim
      namespace: default
    - name: datadisk1
      kind: DataVolume
      namespace: default
----
+
where:
+
`status`:: The `status` field of the `Progressing` condition specifies if the snapshot is still being created.
+
The `status` field of the `Ready` condition specifies if the snapshot creation process is complete.
`readyToUse`:: Specifies if the snapshot is ready to be used.
`virtualMachineSnapshotContentName`:: Specifies that the snapshot is bound to a `VirtualMachineSnapshotContent` object created by the snapshot controller.
`indications`:: Specifies additional information about the snapshot, such as whether it is an online snapshot, or whether it was created with QEMU guest agent running.
`includedVolumes`:: Lists the storage volumes that are part of the snapshot, as well as their parameters.

. Check the `includedVolumes` section in the snapshot description to verify that the expected PVCs are included in the snapshot.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-verifying-online-snapshot-creation-with-snapshot-indications_{context}"]
= Verifying online snapshots by using snapshot indications

[role="_abstract"]
Snapshot indications are contextual information about online virtual machine (VM) snapshot operations. Indications are not available for offline virtual machine (VM) snapshot operations. Indications are helpful in describing details about the online snapshot creation.

.Prerequisites

* You must have attempted to create an online VM snapshot.

.Procedure

. Display the output from the snapshot indications by performing one of the following actions:
* Use the command line to view indicator output in the `status` stanza of the `VirtualMachineSnapshot` object YAML.
* In the web console, click *VirtualMachineSnapshot* -> *Status* in the *Snapshot details* screen.

. Verify the status of your online VM snapshot by viewing the values of the `status.indications` parameter:
* `Online` indicates that the VM was running during online snapshot creation.
* `GuestAgent` indicates that the QEMU guest agent was active and successfully quiesced the guest file system for the online snapshot. This results in an application-consistent snapshot, preserving data integrity as if the applications had been gracefully shut down.
* `NoGuestAgent` indicates that the QEMU guest agent was not installed, or not ready to quiesce the file system during the online snapshot. This results in a crash-consistent snapshot, which captures the VM's state like an abrupt power-off. As a result, application consistency is not guaranteed, which causes a risk of data issues for critical applications. For higher reliability, install and run the guest agent, or retry the snapshot.
* `QuiesceFailed` indicates that an attempt to quiesce the file system failed during the online snapshot process. This means that the snapshot was created, but it is not necessarily application-consistent. To achieve proper consistency, retry the snapshot.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-restoring-vm-from-snapshot-web_{context}"]
= Restoring a VM from a snapshot by using the web console

[role="_abstract"]
You can restore a virtual machine (VM) to a previous configuration represented by a snapshot in the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. If the VM is running, click the Options menu {kebab} and select *Stop* to power it down.
. Click the *Snapshots* tab to view a list of snapshots associated with the VM.
. Select a snapshot to open the *Snapshot Details* screen.
. Click the Options menu {kebab} and select *Restore VirtualMachine from snapshot*.
. Optional: In the *Volume restore policy* section, select how restored persistent volume claims (PVCs) are named:
** *Prefix target name* - The restored PVC names use the target VM name as a prefix. This is the default setting.
** *In place* - The restored PVCs overwrite the original PVCs with the same names.
** *Randomize names* - The restored PVC names are randomly generated.
. Click *Restore*.

. Optional: You can also create a new VM based on the snapshot. To do so:
.. In the Options menu {kebab} of the snapshot, select *Create VirtualMachine from Snapshot*.
.. Provide a name for the new VM.
.. Click *Create*

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-restoring-vm-from-snapshot-cli_{context}"]
= Restoring a VM from a snapshot by using the CLI

[role="_abstract"]
You can restore an existing virtual machine (VM) to a previous configuration by using the command line. You can only restore from an offline VM snapshot.

.Prerequisites

* Install the {oc-first}.

* Power down the VM you want to restore.

* Optional: Adjust what happens if the target VM is not fully stopped (_ready_). To do so, set the `targetReadinessPolicy` parameter in the `vmrestore` YAML configuration to one of the following values:
** `FailImmediate` - The restore process fails immediately if the VM is not ready.
** `StopTarget` - If the VM is not ready, it gets stopped, and the restore process starts.
** `WaitGracePeriod 5` - The restore process waits for a set amount of time, in minutes, for the VM to be ready. This is the default setting, with the default value set to 5 minutes.
** `WaitEventually` - The restore process waits indefinitely for the VM to be ready.

* Optional: To control how restored persistent volume claims (PVCs) are named, you can set the `volumeRestorePolicy` parameter to one of the following values:
** `PrefixTargetName` - The restored PVC names use the target VM name as a prefix: `<vm_name>-<volume_name>`. This is the default setting.
** `RandomizeNames` - The restored PVC names are randomly generated: `restore-<uid>-<volume_name>`.
** `InPlace` - The restored PVCs overwrite the original PVCs. The original PVCs are deleted if they exist, and new PVCs are created with the same names.

.Procedure

. Create a YAML file to define a `VirtualMachineRestore` object that specifies the name of the VM you want to restore and the name of the snapshot to be used as the source as in the following example:
+
[source,yaml]
----
apiVersion: snapshot.kubevirt.io/v1beta1
kind: VirtualMachineRestore
metadata:
  name: <vm_restore>
spec:
  target:
    apiGroup: kubevirt.io
    kind: VirtualMachine
    name: <vm_name>
  virtualMachineSnapshotName: <snapshot_name>
  volumeRestorePolicy: PrefixTargetName
----
+
Where:
+
** `volumeRestorePolicy`: Optional. The volume restore policy determines how restored PVCs are named. Valid values are `PrefixTargetName` (default), `RandomizeNames`, or `InPlace`.

. Optional: To customize the names, labels, and annotations of individual restored persistent volume claims (PVCs), add the `volumeRestoreOverrides` parameter to the YAML file:
+
[source,yaml]
----
apiVersion: snapshot.kubevirt.io/v1beta1
kind: VirtualMachineRestore
metadata:
  name: <vm_restore>
spec:
  target:
    apiGroup: kubevirt.io
    kind: VirtualMachine
    name: <vm_name>
  virtualMachineSnapshotName: <snapshot_name>
  volumeRestoreOverrides:
  - volumeName: <volume_name>
    restoreName: <custom_pvc_name>
    labels:
      custom-label: <label_value>
    annotations:
      custom-annotation: <annotation_value>
----
+
Where:
+
** `volumeName`: Required. The name of the volume from the snapshot to customize.
** `restoreName`: Optional. The custom name for the restored PVC. If not specified, the PVC name is determined by the `volumeRestorePolicy` setting.
** `labels`: Optional. Custom labels to add to the restored PVC. These labels are merged with any existing labels from the source PVC.
** `annotations`: Optional. Custom annotations to add to the restored PVC. These annotations are merged with any existing annotations from the source PVC.

. Create the `VirtualMachineRestore` object:
+
[source,terminal]
----
$ oc create -f <vm_restore>.yaml
----
+
The snapshot controller updates the status fields of the `VirtualMachineRestore` object and replaces the existing VM configuration with the snapshot content.

.Verification

* Verify that the VM is restored to the previous state represented by the snapshot and that the `status.complete` flag is set to `true`:
+
[source,terminal]
----
$ oc get vmrestore <vm_restore>
----
+
Example output:
+
[source, yaml]
----
apiVersion: snapshot.kubevirt.io/v1beta1
kind: VirtualMachineRestore
metadata:
  creationTimestamp: "2020-09-30T14:46:27Z"
  generation: 5
  name: my-vmrestore
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: my-vm
    uid: 355897f3-73a0-4ec4-83d3-3c2df9486f4f
  resourceVersion: "5512"
  uid: 71c679a8-136e-46b0-b9b5-f57175a6a041
spec:
  target:
    apiGroup: kubevirt.io
    kind: VirtualMachine
    name: my-vm
  virtualMachineSnapshotName: my-vmsnapshot
status:
  complete: true
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2020-09-30T14:46:28Z"
    reason: Operation complete
    status: "False"
    type: Progressing
  - lastProbeTime: null
    lastTransitionTime: "2020-09-30T14:46:28Z"
    reason: Operation complete
    status: "True"
    type: Ready
  deletedDataVolumes:
  - test-dv1
  restoreTime: "2020-09-30T14:46:28Z"
  restores:
  - dataVolumeName: restore-71c679a8-136e-46b0-b9b5-f57175a6a041-datavolumedisk1
    persistentVolumeClaim: restore-71c679a8-136e-46b0-b9b5-f57175a6a041-datavolumedisk1
    volumeName: datavolumedisk1
    volumeSnapshotName: vmsnapshot-28eedf08-5d6a-42c1-969c-2eda58e2a78d-volume-datavolumedisk1
----
+
[NOTE]
====
If the `Progressing` condition has `status: "True"`, the VM is still being restored.
====

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-deleting-vm-snapshot-web_{context}"]
= Deleting a snapshot by using the web console

[role="_abstract"]
You can delete an existing virtual machine (VM) snapshot by using the web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. Click the *Snapshots* tab to view a list of snapshots associated with the VM.
. Click the Options menu {kebab} beside a snapshot and select *Delete snapshot*.
. Click *Delete*.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

[id="virt-deleting-vm-snapshot-cli_{context}"]
= Deleting a virtual machine snapshot in the CLI

[role="_abstract"]
You can delete an existing virtual machine (VM) snapshot by deleting the appropriate `VirtualMachineSnapshot` object.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

* Delete the `VirtualMachineSnapshot` object:
+
[source,terminal]
----
$ oc delete vmsnapshot <snapshot_name>
----
+
The snapshot controller deletes the `VirtualMachineSnapshot` along with the associated `VirtualMachineSnapshotContent` object.

.Verification

* Verify that the snapshot is deleted and no longer attached to this VM:
+
[source,terminal]
----
$ oc get vmsnapshot
----

// Hiding in ROSA/OSD as not supported
[role="_additional-resources-snapshots"]
== Additional resources

* CSI Volume Snapshots
