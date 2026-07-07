---
title: "Working with volume snapshots"
type: reference
domain: openshift
slug: microshift-storage-4-22-volume-snapshots-microshift
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_storage/volume-snapshots-microshift
version: 4.22
family: microshift_storage
documentKind: "Documentation"
---

# Working with volume snapshots

[id="working-with-volume-snapshots-microshift"]
= Working with volume snapshots

[role="_abstract"]
{microshift-short} administrators can use volume snapshots to help protect against data loss by using the supported {microshift-short} logical volume manager storage (LVMS) Container Storage Interface (CSI) provider. Familiarity with persistent volumes is required.

A snapshot represents the state of the storage volume in a node at a particular point in time. Volume snapshots can also be used to provision new volumes. Snapshots are created as read-only logical volumes (LVs) located on the same device as the original data.

A {microshift-short} administrator can complete the following tasks using CSI volume snapshots:

* Create a snapshot of an existing persistent volume claim (PVC).
* Back up a volume snapshot to a secure location.
* Restore a volume snapshot as a different PVC.
* Delete an existing volume snapshot.

[IMPORTANT]
====
Only the logical volume manager storage (LVMS) plugin CSI driver is supported by {microshift-short}.
====

[role="_additional-resources"]
.Additional resources

* Using persistent volumes

* Managing LVM volume groups

* CSI snapshots: `VolumeSnapshot` APIs

* VolumeSnapshot API specification

// Module included in the following assemblies:
//
// * microshift_storage/volume-snapshots-microshift.adoc

[id="microshift-lvm-thin-volumes_{context}"]
= About LVM thin volumes

[role="_abstract"]
To enable advanced storage capabilities, such as volume snapshots and volume cloning, complete specific configuration steps. Preparing your environment ensures that the necessary components are active and ready to support these features for your workloads.

The following list describes the configuration steps:

* Configure both the logical volume manager storage (LVMS) provider and the node.
* Provision a logical volume manager (LVM) thin-pool on the {op-system-ostree} host.
* Attach LVM thin-pools to a volume group.

[IMPORTANT]
====
To create Container Storage Interface (CSI) snapshots, you must configure thin volumes on the {op-system-ostree} host. The CSI does not support volume shrinking.
====

[IMPORTANT]
====
When using thin provisioning, you must monitor the storage pool and add more capacity as the available physical space runs out. You can configure the storage pool to auto expand when there is available space within the volume group (VG). See "Creating a thin logical volume".
====

For LVMS to manage thin logical volumes (LVs), a thin-pool `device-class` array must be specified in the `etc/lvmd.yaml` configuration file. Multiple thin-pool device classes are permitted.

If additional storage pools are configured with device classes, then additional storage classes must also exist to expose the storage pools to users and workloads. To enable dynamic provisioning on a thin-pool, a `StorageClass` resource must be present on the node. The `StorageClass` resource specifies the source `device-class` array in the `topolvm.io/device-class` parameter.

.Example `lvmd.yaml` file that specifies a single device class for a thin-pool
[source, yaml]
----
socket-name:
device-classes:
  - name: thin
    default: true
    spare-gb: 0
    thin-pool:
      name: thin
      overprovision-ratio: 1
    type: thin
    volume-group: ssd
----

where:

`socket-name`:: Specifies the UNIX domain socket endpoint of gRPC. Defaults to `/run/lvmd/lvmd.socket`. Takes a string value.

`device-classes`:: Specifies a list of maps for the settings for each `device-class`.

`device-classes.name`:: Specifies the unique name of the `device-class`. Takes a string value.

`device-classes.spare-gb`:: Specifies storage capacity in GB to be left unallocated in the volume group. Defaults to `0`. Takes an unsigned 64-bit integer.

`thin-pool.overprovision-ratio`:: Specifies a float factor by which you can provision additional storage based on the available storage in the thin pool. For example, if this field is set to `10`, you can provision up to 10 times the amount of available storage in the thin pool. To disable over-provisioning, set this field to `1`.

`type`:: Specifies thin provisioning is required to create volume snapshots.

`volume-group`:: Specifies the group where the `device-class` creates the logical volumes. Takes a string value.

[IMPORTANT]
====
When multiple PVCs are created simultaneously, a race condition prevents LVMS from accurately tracking the allocated space and preserving the storage capacity for a device class. Use separate volume groups and device classes to protect the storage of highly dynamic workloads from each other.
====

[role="_additional-resources"]
.Additional resources

* Creating a thin logical volume

* Configuring and managing thin provisioned volumes

* Storage classes

* Storage device classes

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="microshift-storage-classes_{context}"]
= Storage classes

[role="_abstract"]
To configure the workload layer interface for device class selection, review the supported storage class parameters in {microshift-short}. By understanding these parameters, you can define how storage is provisioned and managed for your specific workload requirements.

The following storage class parameters are supported in {microshift-short}:

* The `csi.storage.k8s.io/fstype` parameter selects the file system types. Both `xfs` and `ext4` file system types are supported.
* The `topolvm.io/device-class` parameter is the name of the device class. If a device class is not provided, the default device class is assumed.

Multiple storage classes can refer to the same device class. You can provide varying sets of parameters for the same backing device class, such as `xfs` and `ext4` variants.

.Example {microshift-short} default storage class resource
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  name: topolvm-provisioner
parameters:
  "csi.storage.k8s.io/fstype": "xfs"
provisioner: topolvm.io
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion:
# ...
----

where:

`storageclass.kubernetes.io/is-default-class`:: Specifies an example of the default storage class. If a PVC does not specify a storage class, this class is assumed. There can only be one default storage class in a {microshift-short} node. Having no value assigned to this annotation is also supported.

`csi.storage.k8s.io/fstype`:: Specifies what file system to provision on the volume. Options are "xfs" and "ext4".

`provisioner`:: Specifies what provisioner should manage this class.

`volumeBindingMode`:: Specifies whether to provision the volume before a client pod is present or immediately. Options are `WaitForFirstConsumer` and `Immediate`. `WaitForFirstConsumer` is recommended to ensure that storage is only provisioned for pods that can be scheduled.

`allowVolumeExpansion`:: Specifies if PVCs provisioned from the `StorageClass` permit expansion. The {microshift-short} LVMS CSI plugin does support volume expansion, but if this value is set to `false`, expansion is blocked.

[role="_additional-resources"]
.Additional resources

* Defining storage classes

* Storage device classes

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="microshift-volume-snapshot-class_{context}"]
= Volume snapshot classes

[role="_abstract"]
To enable dynamic snapshotting in LVMS, ensure that at least one `VolumeSnapshotClass` configuration file is present on the node. This resource defines the Container Storage Interface (CSI) parameters required to create and manage volume snapshots.

[IMPORTANT]
====
You must enable thin logical volumes to take logical volume snapshots.
====

.Example `VolumeSnapshotClass` configuration file
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: topolvm-snapclass
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: "true"
driver: topolvm.io
deletionPolicy: Delete
----

where:

`snapshot.storage.kubernetes.io/is-default-class`:: Specifies the `VolumeSnapshotClass` configuration file to use when none is specified by `VolumeSnapshot`. Where `VolumeSnapshot` is a request for snapshot of a volume by a user.

`driver`:: Identifies the snapshot provisioner that manages the requests for snapshots of a volume by a user for this class.

`deletionPolicy`:: Specifies the `VolumeSnapshotContent` objects and the backing snapshots that are kept or deleted when a bound `VolumeSnapshot` is deleted. Valid values are `Retain` or `Delete`.

[role="_additional-resources"]
.Additional resources

* OpenShift CSI volume snapshots

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="about-volume-snapshots_{context}"]
= About volume snapshots

[role="_abstract"]
You can use volume snapshots with logical volume manager (LVM) thin volumes to help protect against data loss from applications running in a {microshift-short} node. {microshift-short} only supports the logical volume manager storage (LVMS) Container Storage Interface (CSI) provider.

[NOTE]
====
LVMS only supports the `volumeBindingMode` of the storage class being set to `WaitForFirstConsumer`. This setting means the storage volume is not provisioned until a pod is ready to mount it.
====

.Example workload that deploys a single pod and PVC
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-claim-thin
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: topolvm-provisioner-thin
---
apiVersion: v1
kind: Pod
metadata:
  name: base
spec:
  containers:
  - command:
	    - nginx
	    - -g
	    - 'daemon off;'
    image: registry.redhat.io/rhel8/nginx-122@sha256:908ebb0dec0d669caaf4145a8a21e04fdf9ebffbba5fd4562ce5ab388bf41ab2
    name: test-container
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - mountPath: /vol
      name: test-vol
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  volumes:
  - name: test-vol
    persistentVolumeClaim:
      claimName: test-claim-thin
EOF
----

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="microshift-storage-creating-vol-snapshot_{context}"]
= Creating a volume snapshot

[role="_abstract"]
To preserve the data on a `PersistentVolumeClaim` (PVC) at a specific point in time, create a volume snapshot. By using a volume snapshot, you can restore the volume to its previous state or provision new volumes with the saved data.

To create a snapshot of a {microshift-short} storage volume, you must first configure {op-system-ostree} and the node.

In the following example procedure, the pod that the source volume is mounted to is deleted. Deleting the pod prevents data from being written to it during snapshot creation. Ensuring that no data is being written during a snapshot is crucial to creating a viable snapshot.

.Prerequisites

* User has root access to a {microshift-short} node.
* {microshift-short} is running.
* A device class defines an LVM thin-pool.
* A `volumeSnapshotClass` specifies `driver: topolvm.io`.
* Any workload attached to the source PVC is paused or deleted. This helps avoid data corruption.

[IMPORTANT]
====
All writes to the volume must be halted while you are creating the snapshot. If you do not halt writes, your data might be corrupted.
====

.Procedure

. Prevent data from being written to the volume during snapshotting by using one of the two following steps:
+
.. Delete the pod to ensure that no data is written to the volume during snapshotting by running the following command:
+
[source,terminal]
----
$ oc delete my-pod
----
+
.. Scale the replica count to zero on a pod that is managed with a replication controller. Setting the count to zero prevents the instant creation of a new pod when one is deleted.

. After all writes to the volume are halted, run a command similar to the example that follows. Insert your own configuration details.
+
.Example snapshot configuration
[source,terminal]
----
# oc apply -f <<EOF
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: <snapshot_name>
spec:
  volumeSnapshotClassName: topolvm-snapclass
  source:
    persistentVolumeClaimName: test-claim-thin
EOF
----
+
where:

`kind`:: Specifies the type of `VolumeSnapshot` object to create.

`metadata.name`:: Specifies the name that you specify for the snapshot.

`volumeSnapshotClassName`:: Specifies the desired name of the `VolumeSnapshotClass` object.

`persistentVolumeClaimName`:: Specifies either `persistentVolumeClaimName` or `volumeSnapshotContentName`. In this example, a snapshot is created from a PVC named `test-claim-thin`.

. Wait for the storage driver to finish creating the snapshot by running the following command:
+
[source,terminal]
----
$ oc wait volumesnapshot/<snapshot_name> --for=jsonpath\='{.status.readyToUse}=true'
----

. When the `volumeSnapshot` object is in a `ReadyToUse` state, you can restore the state as a volume for future PVCs. Restart the pod or scale the replica count back up to the desired number.

. After you have created the volume snapshot, you can remount the source PVC to a new pod.
+
[IMPORTANT]
====
Volume snapshots are located on the same devices as the original data. To use the volume snapshots as backups, move the snapshots to a secure location.
====

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="microshift-storage-backup-volume-snapshots_{context}"]
= Backing up a volume snapshot

[role="_abstract"]
Snapshots of data from applications running on a {microshift-short} node are created as read-only logical volumes (LVs) located on the same devices as the original data. You must manually mount local volumes before they can be copied as persistent volumes (PVs) and used as backup copies. To use a snapshot of a {microshift-short} storage volume as a backup, find it on the local host and then move it to a secure location.

.Prerequisites

* You have root access to the host machine.
* You have an existing volume snapshot.

.Procedure

. Get the name of the volume snapshot by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc get volumesnapshot -n _<namespace>_ _<snapshot_name>_ -o 'jsonpath={.status.volumeSnapshotContentName}'
----
** Replace `_<namespace>_` and `_<snapshot_name>_` with the namespace and snapshot name you used.

. Get the unique identity of the volume created on the storage backend by using the following command and inserting the name retrieved in the previous step:
+
[source,terminal]
----
$ oc get volumesnapshotcontent snapcontent-<retrieved_volume_identity> -o 'jsonpath={.status.snapshotHandle}'
----
** Replace `_<retrieved_volume_identity>_` with the volume identity.

. Display the snapshots by using the unique identity of the volume you retrieved in the previous step to determine which one you want to backup by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ sudo lvdisplay _<retrieved_volume_identity>_
----
** Replace `_<retrieved_volume_identity>_` with the volume identity.
+
.Example output
[source,terminal]
----
--- Logical volume ---
LV Path                /dev/rhel/732e45ff-f220-49ce-859e-87ccca26b14c
LV Name                732e45ff-f220-49ce-859e-87ccca26b14c
VG Name                rhel
LV UUID                6Ojwc0-YTfp-nKJ3-F9FO-PvMR-Ic7b-LzNGSx
LV Write Access        read only
LV Creation host, time rhel-92.lab.local, 2023-08-07 14:45:26 -0500
LV Pool name           thinpool
LV Thin origin name    a2d2dcdc-747e-4572-8c83-56cd873d3b07
LV Status              available
# open                 0
LV Size                1.00 GiB
Mapped size            1.04%
Current LE             256
Segments               1
Allocation             inherit
Read ahead sectors     auto
- currently set to     256
Block device           253:11
----

. Create a directory to use for mounting the LV by running the following command:
+
[source,terminal]
----
$ sudo mkdir /mnt/snapshot
----

. Mount the LV using the device name for the retrieved snapshot handle by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ sudo mount /dev/_<retrieved_snapshot_handle>_ /mnt/snapshot
----
** Replace `_<retrieved_snapshot_handle>_` with the device name.

. Copy the files from the mounted location and store them in a secure location by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ sudo cp -r /mnt/snapshot _<destination>_
----
** Replace `_<destination>_` with the path to the secure location.

// Module included in the following assemblies:
//
// microshift/volume-snapshots-microshift.adoc

[id="microshift-storage-vol-snapshot-restore_{context}"]
= Restoring a volume snapshot

[role="_abstract"]
To recover data from a point-in-time copy, restore a volume snapshot to a new `PersistentVolumeClaim` (PVC). This process ensures that data from the source volume is preserved and you can verify the integrity of the restored content on the new claim.

The following workflow demonstrates snapshot restoration. In this example, the verification steps are also given to ensure that data written to a source persistent volume claim (PVC) is preserved and restored on a new PVC.

[IMPORTANT]
====
A snapshot must be restored to a PVC of exactly the same size as the source volume of the snapshot. You can resize the PVC after the snapshot is restored successfully if a larger PVC is needed.
====

.Procedure

* Restore a snapshot by specifying the `VolumeSnapshot` object as the data source in a persistent volume claim by entering the following command:
+
[source,terminal]
----
$ oc apply -f <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: snapshot-restore
spec:
  accessModes:
  - ReadWriteOnce
  dataSource:
    apiGroup: snapshot.storage.k8s.io
    kind: VolumeSnapshot
    name: my-snap
  resources:
    requests:
      storage: 1Gi
  storageClassName: topolvm-provisioner-thin
---
apiVersion: v1
kind: Pod
metadata:
  name: base
spec:
  containers:
  - command:
      - nginx
	    - -g
	    - 'daemon off;'
    image: registry.redhat.io/rhel8/nginx-122@sha256:908ebb0dec0d669caaf4145a8a21e04fdf9ebffbba5fd4562ce5ab388bf41ab2
    name: test-container
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - mountPath: /vol
      name: test-vol
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  volumes:
  - name: test-vol
    persistentVolumeClaim:
      claimName: snapshot-restore
EOF
----

.Verification

. Wait for the pod to reach the `Ready` state:
+
[source,terminal]
----
$ oc wait --for=condition=Ready pod/base
----

. When the new pod is ready, verify that the data from your application is correct in the snapshot.

[role="_additional-resources"]
.Additional resources

* Restoring a volume snapshot

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc
// * microshift_storage/volume-snapshots-microshift.adoc

[id="persistent-storage-csi-snapshots-delete_{context}"]
= Deleting a volume snapshot

[role="_abstract"]
You can configure how OpenShift Container Platform deletes volume snapshots.

.Procedure

. Specify the deletion policy that you require in the `VolumeSnapshotClass` object, as shown in the following example:
+
.Example volumesnapshotclass.yaml file
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snap
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
# ...
----
** `deletionPolicy`: When deleting the volume snapshot, if the `Delete` value is set, the underlying snapshot is deleted along with the `VolumeSnapshotContent` object. If the `Retain` value is set, both the underlying snapshot and `VolumeSnapshotContent` object remain.
+
[NOTE]
====
If the `Retain` value is set and the `VolumeSnapshot` object is deleted without deleting the corresponding `VolumeSnapshotContent` object, the content remains. The snapshot itself is also retained in the storage back end.
====

. Delete the volume snapshot by entering the following command:
+
[source,terminal]
----
$ oc delete volumesnapshot _<volumesnapshot_name>_
----
** Replace `_<volumesnapshot_name>_` with the name of the volume snapshot you want to delete.
+
.Example output
[source,terminal]
----
volumesnapshot.snapshot.storage.k8s.io "mysnapshot" deleted
----

. If the deletion policy is set to `Retain`, delete the volume snapshot content by entering the following command:
+
[source,terminal]
----
$ oc delete volumesnapshotcontent _<volumesnapshotcontent_name>_
----
** Replace `_<volumesnapshotcontent_name>_` with the content you want to delete.

. Optional: If the `VolumeSnapshot` object is not successfully deleted, enter the following command to remove any finalizers for the leftover resource so that the delete operation can continue:
+
[IMPORTANT]
====
Only remove the finalizers if you are confident that there are no existing references from either persistent volume claims or volume snapshot contents to the `VolumeSnapshot` object. Even with the `--force` option, the delete operation does not delete snapshot objects until all finalizers are removed.
====
+
[source,terminal]
----
$ oc patch -n $PROJECT volumesnapshot/$NAME --type=merge -p '{"metadata": {"finalizers":null}}'
----
+
.Example output
[source,terminal]
----
volumesnapshotclass.snapshot.storage.k8s.io "csi-ocs-rbd-snapclass" deleted
----
+
The finalizers are removed and the volume snapshot is deleted.

// Module included in the following assemblies:
//
// * microshift_storage/volume-snapshots-microshift.adoc

[id="microshift-storage-volume-cloning_{context}"]
= About LVM volume cloning

[role="_abstract"]
You can use the logical volume manager storage (LVMS) for persistent volume claim (PVC) cloning of the logical volume manager (LVM) thin volumes. A clone is a duplicate of an existing volume that can be used like any other volume.

When you provision the clone, an exact duplicate of the original volume is created if the data source references a source PVC in the same namespace. After a cloned PVC is created, the cloned VPC is considered a new object and completely separate from the source PVC. The clone represents a snapshot of the data from the source at the moment in time.

[NOTE]
====
Cloning is only possible when the source and destination PVCs are in the same namespace. To create PVC clones, you must configure thin volumes on the {op-system-ostree} host.
====

[role="_additional-resources"]
.Additional resources

* CSI volume cloning

* About LVM thin volumes
