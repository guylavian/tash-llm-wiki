---
title: "CSI volume snapshots"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-snapshots
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-snapshots
version: 4.22
family: storage
documentKind: "Documentation"
---

# CSI volume snapshots

[id="persistent-storage-csi-snapshots"]
= CSI volume snapshots

This document describes how to use volume snapshots with supported Container Storage Interface (CSI) drivers to help protect against data loss in OpenShift Container Platform. Familiarity with persistent volumes is suggested.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-overview_{context}"]
= Overview of CSI volume snapshots

A _snapshot_ represents the state of the storage volume in a cluster at a particular point in time. Volume snapshots can be used to provision a new volume.

OpenShift Container Platform supports Container Storage Interface (CSI) volume snapshots by default. However, a specific CSI driver is required.

With CSI volume snapshots, a cluster administrator can:

* Deploy a third-party CSI driver that supports snapshots.
* Create a new persistent volume claim (PVC) from an existing volume snapshot.
* Take a snapshot of an existing PVC.
* Restore a snapshot as a different PVC.
* Delete an existing volume snapshot.

With CSI volume snapshots, an app developer can:

* Use volume snapshots as building blocks for developing application- or cluster-level storage backup solutions.
* Rapidly rollback to a previous development version.
* Use storage more efficiently by not having to make a full copy each time.

Be aware of the following when using volume snapshots:

* Support is only available for CSI drivers. In-tree and FlexVolumes are not supported.
* OpenShift Container Platform only ships with select CSI drivers. For CSI drivers that are not provided by an OpenShift Container Platform Driver Operator, it is recommended to use the CSI drivers provided by
community or storage vendors. Follow the installation instructions furnished by the CSI driver provider.
* CSI drivers may or may not have implemented the volume snapshot functionality. CSI drivers that have provided support for volume snapshots will likely use the `csi-external-snapshotter` sidecar. See documentation provided by the CSI driver for details.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-controller-sidecar_{context}"]
= CSI snapshot controller and sidecar

OpenShift Container Platform provides a snapshot controller that is deployed into the control plane. In addition, your CSI driver vendor provides the CSI snapshot sidecar as a helper container that is installed during the CSI driver installation.

The CSI snapshot controller and sidecar provide volume snapshotting through the OpenShift Container Platform API. These external components run in the cluster.

The external controller is deployed by the CSI Snapshot Controller Operator.

== External controller
The CSI snapshot controller binds `VolumeSnapshot` and `VolumeSnapshotContent` objects. The controller manages dynamic provisioning by creating and deleting `VolumeSnapshotContent` objects.

== External sidecar
Your CSI driver vendor provides the `csi-external-snapshotter` sidecar. This is a separate helper container that is deployed with the CSI driver. The sidecar manages snapshots by triggering `CreateSnapshot` and `DeleteSnapshot` operations. Follow the installation instructions provided by your vendor.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-operator_{context}"]
= About the CSI Snapshot Controller Operator

The Container Storage Interface (CSI) Snapshot Controller Operator runs in the `openshift-cluster-storage-operator` namespace. It is installed by the Cluster Version Operator (CVO) in all clusters by default.

The CSI Snapshot Controller Operator installs the CSI snapshot controller, which runs in the `openshift-cluster-storage-operator` namespace.

== Volume snapshot CRDs

During OpenShift Container Platform installation, the CSI Snapshot Controller Operator creates the following snapshot custom resource definitions (CRDs) in the `snapshot.storage.k8s.io/v1` API group:

`VolumeSnapshotContent`::

A snapshot taken of a volume in the cluster that has been provisioned by a cluster administrator.
+
Similar to the `PersistentVolume` object, the `VolumeSnapshotContent` CRD is a cluster resource that points to a real snapshot in the storage back end.
+
For manually pre-provisioned snapshots, a cluster administrator creates a number of `VolumeSnapshotContent` CRDs. These carry the details of the real volume snapshot in the storage system.
+
The `VolumeSnapshotContent` CRD is not namespaced and is for use by a cluster administrator.

`VolumeSnapshot`::

Similar to the `PersistentVolumeClaim` object, the `VolumeSnapshot` CRD defines a developer request for a snapshot. The CSI Snapshot Controller Operator runs the CSI snapshot controller, which handles the binding of a `VolumeSnapshot` CRD with an appropriate `VolumeSnapshotContent` CRD. The binding is a one-to-one mapping.
+
The `VolumeSnapshot` CRD is namespaced. A developer uses the CRD as a distinct request for a snapshot.

`VolumeSnapshotClass`::

The `VolumeSnapshotClass` CRD allows a cluster administrator to specify different attributes belonging to a `VolumeSnapshot` object. These attributes may differ among snapshots taken of the same volume on the storage system, in which case they would not be expressed by using the same storage class of a persistent volume claim.
+
The `VolumeSnapshotClass` CRD defines the parameters for the `csi-external-snapshotter` sidecar to use when creating a snapshot. This allows the storage back end to know what kind of snapshot to dynamically create if multiple options are supported.
+
Dynamically provisioned snapshots use the `VolumeSnapshotClass` CRD to specify storage-provider-specific parameters to use when creating a snapshot.
+
The `VolumeSnapshotContentClass` CRD is not namespaced and is for use by a cluster administrator to enable global configuration options for their storage back end.
+
For Google Cloud Platform (GCP) persistent disk (PD) storage  CSI, there is a non-default `VolumeSnapshotClass`, named `csi-gce-pd-vsc-images`, that uses the `snapshot-type`: `images` parameter. When using KubeVirt, this allows you to create VMs from "golden images" (templates saved as snapshots).
+
If you want to use the images volume snapshot class for dynamic snapshot provisioning, you can either:

* Make the images volume snapshot class the default by changing the `snapshot.storage.kubernetes.io/is-default-class` annotation to `true`. Also, for the normal default volume snapshot class, `csi-gce-pd-vsc`, be sure to change this parameter to `false`.

* When creating the snapshot object, be sure to set `volumeSnapshotClassName` to `csi-gce-pd-vsc-images`.
+
For information about creating volume snapshots, see Section _Creating a volume snapshot_.
+
.Example images volume snapshot class YAML file
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-gce-pd-vsc-images
driver: pd.csi.storage.gke.io
parameters:
  snapshot-type: images
----
+
* `metadata.name:csi-gce-pd-vsc-images`: Name for the non-default images volume snapshot class.

* `parameters: snapshot-type: images`: Defines the snapshot as a "golden image" or a bootable template, rather than the standard disk backup.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-provision_{context}"]
= Volume snapshot provisioning

There are two ways to provision snapshots: dynamically and manually.

[id="snapshots-dynamic-provisioning_{context}"]
== Dynamic provisioning

Instead of using a preexisting snapshot, you can request that a snapshot be taken dynamically from a persistent volume claim. Parameters are specified using a `VolumeSnapshotClass` CRD.

[id="snapshots-manual-provisioning_{context}"]
== Manual provisioning

As a cluster administrator, you can manually pre-provision a number of `VolumeSnapshotContent` objects. These carry the real volume snapshot details available to cluster users.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-create_{context}"]
= Creating a volume snapshot

When you create a `VolumeSnapshot` object, OpenShift Container Platform creates a volume snapshot.

.Prerequisites
* Logged in to a running OpenShift Container Platform cluster.
* A PVC created using a CSI driver that supports `VolumeSnapshot` objects.
* A storage class to provision the storage back end.
* No pods are using the persistent volume claim (PVC) that you want to take a snapshot of.
+
[WARNING]
====
Creating a volume snapshot of a PVC that is in use by a pod can cause unwritten data and cached data to be excluded from the snapshot. To ensure that all data is written to the disk, delete the pod that is using the PVC before creating the snapshot.
====

.Procedure

To dynamically create a volume snapshot:

. Create a file with the `VolumeSnapshotClass` object described by the following YAML:

+
.volumesnapshotclass.yaml
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snap
driver: hostpath.csi.k8s.io <1>
deletionPolicy: Delete
----
+
<1> The name of the CSI driver that is used to create snapshots of this `VolumeSnapshotClass` object. The name must be the same as the `Provisioner` field of the storage class that is responsible for the PVC that is being snapshotted.
+
[NOTE]
====
Depending on the driver that you used to configure persistent storage, additional parameters might be required. You can also use an existing `VolumeSnapshotClass` object.
====

. Create the object you saved in the previous step by entering the following command:
+
[source,terminal]
----
$ oc create -f volumesnapshotclass.yaml
----

. Create a `VolumeSnapshot` object:

+
.volumesnapshot-dynamic.yaml
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: mysnap
spec:
  volumeSnapshotClassName: csi-hostpath-snap <1>
  source:
    persistentVolumeClaimName: myclaim <2>
----
+
<1> The request for a particular class by the volume snapshot. If the `volumeSnapshotClassName` setting is absent and there is a default volume snapshot class, a snapshot is created with the default volume snapshot class name. But if the field is absent and no default volume snapshot class exists, then no snapshot is created.
+
<2> The name of the `PersistentVolumeClaim` object bound to a persistent volume. This defines what you want to create a snapshot of. Required for dynamically provisioning a snapshot.

. Create the object you saved in the previous step by entering the following command:
+
[source,terminal]
----
$ oc create -f volumesnapshot-dynamic.yaml
----

To manually provision a snapshot:

. Provide a value for the `volumeSnapshotContentName` parameter as the source for the snapshot, in addition to defining volume snapshot class as shown above.
+
.volumesnapshot-manual.yaml
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: snapshot-demo
spec:
  source:
    volumeSnapshotContentName: mycontent <1>
----
<1> The `volumeSnapshotContentName` parameter is required for pre-provisioned snapshots.

. Create the object you saved in the previous step by entering the following command:
+
[source,terminal]
----
$ oc create -f volumesnapshot-manual.yaml
----

.Verification
After the snapshot has been created in the cluster, additional details about the snapshot are available.

. To display details about the volume snapshot that was created, enter the following command:
+
[source,terminal]
----
$ oc describe volumesnapshot mysnap
----
+
The following example displays details about the `mysnap` volume snapshot:
+
.volumesnapshot.yaml
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: mysnap
spec:
  source:
    persistentVolumeClaimName: myclaim
  volumeSnapshotClassName: csi-hostpath-snap
status:
  boundVolumeSnapshotContentName: snapcontent-1af4989e-a365-4286-96f8-d5dcd65d78d6 <1>
  creationTime: "2020-01-29T12:24:30Z" <2>
  readyToUse: true <3>
  restoreSize: 500Mi
----
<1> The pointer to the actual storage content that was created by the controller.
<2> The time when the snapshot was created. The snapshot contains the volume content that was available at this indicated time.
<3> If the value is set to `true`, the snapshot can be used to restore as a new PVC.
  +
If the value is set to `false`, the snapshot was created. However, the storage back end needs to perform additional tasks to make the snapshot usable so that it can be restored as a new volume. For example, Amazon Elastic Block Store data might be moved to a different, less expensive location, which can take several minutes.

. To verify that the volume snapshot was created, enter the following command:
+
[source,terminal]
----
$ oc get volumesnapshotcontent
----
+
The pointer to the actual content is displayed. If the `boundVolumeSnapshotContentName` field is populated, a `VolumeSnapshotContent` object exists and the snapshot was created.

. To verify that the snapshot is ready, confirm that the `VolumeSnapshot` object has `readyToUse: true`.

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
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-restore_{context}"]
= Restoring a volume snapshot

The `VolumeSnapshot` CRD content can be used to restore the existing volume to a previous state.

After your `VolumeSnapshot` CRD is bound and the `readyToUse` value is set to `true`, you can use that resource to provision a new volume that is pre-populated with data from the snapshot.

.Prerequisites
* Logged in to a running OpenShift Container Platform cluster.
* A persistent volume claim (PVC) created using a Container Storage Interface (CSI) driver that supports volume snapshots.
* A storage class to provision the storage back end.
* A volume snapshot has been created and is ready to use.

.Procedure

. Specify a `VolumeSnapshot` data source on a PVC as shown in the following:
+
.pvc-restore.yaml
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim-restore
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: mysnap <1>
    kind: VolumeSnapshot <2>
    apiGroup: snapshot.storage.k8s.io <3>
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
----
<1> Name of the `VolumeSnapshot` object representing the snapshot to use as source.
<2> Must be set to the `VolumeSnapshot` value.
<3> Must be set to the `snapshot.storage.k8s.io` value.

. Create a PVC by entering the following command:

+
[source,terminal]
----
$ oc create -f pvc-restore.yaml
----

. Verify that the restored PVC has been created by entering the following command:

+
[source,terminal]
----
$ oc get pvc
----
+
A new PVC such as `myclaim-restore` is displayed.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc
// * storage/persistent_storage/persistent-storage-csi-snapshots.adoc

[id="vsphere-change-max-snapshot_{context}"]
= Changing the maximum number of snapshots for vSphere

The default maximum number of snapshots per volume in vSphere Container Storage Interface (CSI) is 3. You can change the maximum number up to 32 per volume.

However, be aware that increasing the snapshot maximum involves a performance trade off, so for better performance use only 2 to 3 snapshots per volume.

For more VMware snapshot performance recommendations, see *_Additional resources_*.

.Prerequisites

* Access to the cluster with administrator rights.

.Procedure

. Check the current secret by the running the following command:
+
[source, terminal]
----
$ oc -n openshift-cluster-csi-drivers get secret/vsphere-csi-config-secret -o jsonpath='{.data.cloud\.conf}' | base64 -d
----
+
.Example output
+
[source, terminal]
----
# Labels with topology values are added dynamically via operator
[Global]
cluster-id = vsphere-01-cwv8p

# Populate VCenters (multi) after here
[VirtualCenter "vcenter.openshift.com"]
insecure-flag           = true
datacenters             = DEVQEdatacenter
password                = "xxxxxxxx"
user                    = "xxxxxxxx@devcluster.openshift.com"
migration-datastore-url = ds:///vmfs/volumes/vsan:52c842f232751e0d-3253aadeac21ca82/
----
+
In this example, the global maximum number of snapshots is not configured, so the default value of 3 is applied.

. Change the snapshot limit by running the following command:
+
* Set *global* snapshot limit:
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"globalMaxSnapshotsPerBlockVolume": 10}}}}'

clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the global limit is being changed to 10 (`globalMaxSnapshotsPerBlockVolume` set to 10).

* Set *Virtual Volume* snapshot limit:
+
This parameter sets the limit on the Virtual Volumes datastore only. The Virtual Volume maximum snapshot limit overrides the global constraint if set, but defaults to the global limit if it is not set.
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"granularMaxSnapshotsPerBlockVolumeInVVOL": 5}}}}'
clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the Virtual Volume limit is being changed to 5 (`granularMaxSnapshotsPerBlockVolumeInVVOL` set to 5).

* Set *vSAN* snapshot limit:
+
This parameter sets the limit on the vSAN datastore only. The vSAN maximum snapshot limit overrides the global constraint if set, but defaults to the global limit if it is not set. You can set a maximum value of 32 under vSAN ESA setup.
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"granularMaxSnapshotsPerBlockVolumeInVSAN": 7}}}}'
clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the vSAN limit is being changed to 7 (`granularMaxSnapshotsPerBlockVolumeInVSAN` set to 7).

.Verification

* Verify that any changes you made are reflected in the config map by running the following command:
+
[source, terminal]
----
$ oc -n openshift-cluster-csi-drivers get secret/vsphere-csi-config-secret -o jsonpath='{.data.cloud\.conf}' | base64 -d
----
+
.Example output
+
[source, terminal]
----
# Labels with topology values are added dynamically via operator
[Global]
cluster-id = vsphere-01-cwv8p

# Populate VCenters (multi) after here
[VirtualCenter "vcenter.openshift.com"]
insecure-flag           = true
datacenters             = DEVQEdatacenter
password                = "xxxxxxxx"
user                    = "xxxxxxxx@devcluster.openshift.com"
migration-datastore-url = ds:///vmfs/volumes/vsan:52c842f232751e0d-3253aadeac21ca82/

[Snapshot]
global-max-snapshots-per-block-volume = 10 <1>
----
<1> `global-max-snapshots-per-block-volume` is now set to 10.

== Additional resources
* Best practices for using VMware snapshots in the vSphere environment
