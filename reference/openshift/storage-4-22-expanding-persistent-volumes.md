---
title: "Expanding persistent volumes"
type: reference
domain: openshift
slug: storage-4-22-expanding-persistent-volumes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/expanding-persistent-volumes
version: 4.22
family: storage
documentKind: "Documentation"
---

# Expanding persistent volumes

[id="expanding-persistent-volumes"]
= Expanding persistent volumes

[role="_abstract"]
You can use the Container Storage Interface (CSI) to expand storage volumes after they have already been created.

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="add-volume-expansion_{context}"]
= Enabling volume expansion support

Before you can expand persistent volumes, the `StorageClass` object must
have the `allowVolumeExpansion` field set to `true`.

.Procedure

* Edit the `StorageClass` object and add the `allowVolumeExpansion` attribute by running the following command:
+
[source,terminal]
----
$ oc edit storageclass <storage_class_name> <1>
----
<1> Specifies the name of the storage class.
+
The following example demonstrates adding this line at the bottom
of the storage class configuration.
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
...
parameters:
  type: gp2
reclaimPolicy: Delete
allowVolumeExpansion: true <1>
----
<1> Setting this attribute to `true` allows PVCs to be
expanded after creation.

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-csi-volumes_{context}"]
= Expanding CSI volumes

[role="_abstract"]
You can use the Container Storage Interface (CSI) to expand storage volumes after they have already been created.

[IMPORTANT]
====
Shrinking persistent volumes (PVs) is _not_ supported.
====

.Prerequisites

* The underlying CSI driver supports resize. See "CSI drivers supported by OpenShift Container Platform" in the "Additional resources" section.

* Dynamic provisioning is used.

* The controlling `StorageClass` object has `allowVolumeExpansion` set to `true`. For more information, see "Enabling volume expansion support."

.Procedure

. For the persistent volume claim (PVC), set `.spec.resources.requests.storage` to the desired new size.

. Watch the `status.conditions` field of the PVC to see if the resize has completed. OpenShift Container Platform adds the `Resizing` condition to the PVC during expansion, which is removed after expansion completes.

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-flexvolume_{context}"]
= Expanding FlexVolume with a supported driver

When using FlexVolume to connect to your back-end storage system, you can expand persistent storage volumes after they have already been created. This is done by manually updating the persistent volume claim (PVC) in OpenShift Container Platform.

FlexVolume allows expansion if the driver is set with `RequiresFSResize` to `true`. The FlexVolume can be expanded on pod restart.

Similar to other volume types, FlexVolume volumes can also be expanded when in use by a pod.

.Prerequisites

* The underlying volume driver supports resize.
* The driver is set with the `RequiresFSResize` capability to `true`.
* Dynamic provisioning is used.
* The controlling `StorageClass` object has `allowVolumeExpansion` set to `true`.

.Procedure

* To use resizing in the FlexVolume plugin, you must implement the `ExpandableVolumePlugin` interface using these methods:

`RequiresFSResize`::
If `true`, updates the capacity directly. If `false`, calls the `ExpandFS` method to finish the filesystem resize.

`ExpandFS`::
If `true`, calls `ExpandFS` to resize filesystem after physical volume expansion is done. The volume driver can also perform physical volume resize together with filesystem resize.

[IMPORTANT]
====
Because OpenShift Container Platform does not support installation of FlexVolume plugins on control plane nodes, it does not support control-plane expansion of FlexVolume.
====

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-local-volumes_{context}"]
= Expanding local volumes

[role="_abstract"]
You can manually expand persistent volumes (PVs) and persistent volume claims (PVCs) created by using the local storage operator (LSO).

.Procedure

. Expand the underlying devices. Ensure that appropriate capacity is available on these devices.

. Update the corresponding PV objects to match the new device sizes by editing the `.spec.capacity` field of the PV.

. For the storage class that is used for binding the PVC to PV, set the `allowVolumeExpansion` field to `true`.

. For the PVC, set the `.spec.resources.requests.storage` field to match the new size.
+
Kubelet automatically expands the underlying file system on the volume, if necessary, and updates the status field of the PVC to reflect the new size.

// Module included in the following assemblies:
//
// * storage/expanding-persistent-volume.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-pvc-filesystem_{context}"]
= Expanding persistent volume claims (PVCs) with a file system

[role="_abstract"]
Expanding PVCs based on volume types that need file system resizing, such as GCE, EBS, and Cinder, is a two-step process. First, expand the volume objects in the cloud provider. Second, expand the file system on the node.
Expanding PVCs based on volume types that need file system resizing, such as GCE Persistent Disk volumes (gcePD), AWS Elastic Block Store (EBS), and Cinder, is a two-step process. First, expand the volume objects in the cloud provider. Second, expand the file system on the node.

Expanding PVCs based on volume types that need file system resizing, such as AWS Elastic Block Store (EBS) is a two-step process. First, expand the volume objects in the cloud provider. Second, expand the file system on the node.

Expanding the file system on the node only happens when a new pod is started with the volume.

.Prerequisites

* The controlling `StorageClass` object must have `allowVolumeExpansion` set to `true`.

.Procedure

. Edit the PVC and request a new size by editing `spec.resources.requests`. For example, the following expands the `ebs` PVC to 8 Gi:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: ebs
spec:
  storageClass: "storageClassWithFlagSet"
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
----
** `requests.storage`: Specifies the size for the PVC.

. After the cloud provider object has finished resizing, the PVC is set to `FileSystemResizePending`. Check the condition by entering the following command:
+
[source,terminal]
----
$ oc describe pvc <pvc_name>
----

. When the cloud provider object has finished resizing, the `PersistentVolume` object reflects the newly requested size in `PersistentVolume.Spec.Capacity`. At this point, you can create or re-create a pod from the PVC to finish the file system resizing. Once the pod is running, the newly requested size is available and the `FileSystemResizePending` condition is removed from the PVC.

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-recovering-from-failure_{context}"]
= Recovering from failure when expanding volumes

[role="_abstract"]
To retry a failed or pending resize request, update the `spec.resources.requests.storage` field in the persistent volume claim (PVC). You must specify a value larger than the original volume size to successfully retrigger the operation.

Entering a smaller resize value in the `.spec.resources.requests.storage` field for the existing PVC does not work.

.Procedure

. Mark the persistent volume (PV) that is bound to the PVC with the `Retain` reclaim policy. Change the `persistentVolumeReclaimPolicy` field to `Retain`.

. Delete the PVC.

. Manually edit the PV and delete the `claimRef` entry from the PV specification to ensure that the newly created PVC can bind to the PV marked `Retain`. This marks the PV as `Available`.

. Recreate the PVC in a smaller size, or a size that can be allocated by the underlying storage provider.

. Set the `volumeName` field of the PVC to the name of the PV. This binds the PVC to the provisioned PV only.

. Restore the reclaim policy on the PV.

// Module included in the following assemblies
//
// * storage/expanding-persistent-volumes.adoc
//* microshift_storage/expanding-persistent-volumes-microshift.adoc

[id="expanding-recovering-from-failure-view-status_{context}"]
= Viewing the status of volume resize

[role="_abstract"]
You can view the status of volume resizing with the `pvc.Status.AllocatedResourceStatus` field. If a user changes the size of their PVCs, the `pvc.Status.AllocatedResourceStatus` field allows resource quota to be tracked accurately.

The possible values for `pvc.Status.AllocatedResourceStatus` are:

* `ControllerResizeInProgress`: Controller resize attempt is in progress.

* `ControllerResizeFailed`: Controller resize attempt failed.

* `NodeResizeInProgress`: Node resize attempt is in progress.

* `NodeResizeFailed`: Node resize attempt failed.

For a typical block volume, the field transitions between `ControllerResizeInProgress`, `NodeResizePending`, `NodeResizeInProgress`, and then nil/empty when the volume expansion finishes.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* CSI drivers supported by OpenShift Container Platform
