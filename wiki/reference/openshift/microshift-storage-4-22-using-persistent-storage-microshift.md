---
title: "Using persistent storage"
type: reference
domain: openshift
slug: microshift-storage-4-22-using-persistent-storage-microshift
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_storage/using-persistent-storage-microshift
version: 4.22
family: microshift_storage
documentKind: "Documentation"
---

# Using persistent storage

[id="using-persistent-storage-microshift"]
= Using persistent storage

Managing storage is a distinct problem from managing compute resources. {microshift-short} uses the Kubernetes persistent volume (PV) framework to allow node administrators to provision persistent storage for a node. Developers can use persistent volume claims (PVCs) to request PV resources without having specific knowledge of the underlying storage infrastructure.

// Module included in the following assemblies:
//
// * microshift_storage/understanding-persistent-storage-microshift.adoc

[id=microshift-control-permissions-security-context-constraints_{context}]
= Control permissions with security context constraints

You can use security context constraints (SCCs) to control permissions for the pods in your node. These permissions determine the actions that a pod can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run with to be accepted into the system.

For more information, see "Managing security context constraints".

[IMPORTANT]
====
Only RWO volume mounts are supported. SCC could be blocked if pods are not operating with the SCC contexts.
====

[id="additional-resources_using-persistent-storage-microshift_{context}"]
[role="_additional-resources"]
== Additional resources

* Managing security context constraints

// Module included in the following assemblies:
//
// storage/understanding-persistent-storage.adoc
// microshift_storage/understanding-persistent-storage-microshift.adoc

[id=persistent-storage-overview_{context}]
= Persistent storage overview

Stateful applications deployed in containers require persistent storage. {microshift-short} uses a pre-provisioned storage framework called persistent volumes (PV) to allow node administrators to provision persistent storage. The data inside these volumes can exist beyond the lifecycle of an individual pod. Developers can use persistent volume claims (PVCs) to request storage requirements.

Managing storage is a distinct problem from managing compute resources. OpenShift Container Platform uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision persistent storage for a cluster. Developers can use persistent volume claims (PVCs) to request PV resources without having specific knowledge of the underlying storage infrastructure.

PVCs are specific to a project, and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single project; they can be shared across the entire OpenShift Container Platform node and claimed from any project. After a PV is bound to a PVC, that PV can not then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace, that of the binding project.

PVCs are specific to a namespace, and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single namespace; they can be shared across the entire OpenShift Container Platform node and claimed from any namespace. After a PV is bound to a PVC, that PV can not then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace.

PVs are defined by a `PersistentVolume` API object, which represents a piece of existing storage in the cluster that was either statically provisioned by the cluster administrator or dynamically provisioned using a `StorageClass` object. It is a resource in the cluster just like a node is a cluster resource.

PVs are volume plugins like `Volumes` but have a lifecycle that is independent of any individual pod that uses the PV. PV objects capture the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

PVs are volume plugins like `Volumes` but have a lifecycle that is independent of any individual pod that uses the PV. PV objects capture the details of the implementation of the storage, be that LVM, the host filesystem such as hostpath, or raw block devices.

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying storage provider.
====

PVCs are defined by a `PersistentVolumeClaim` API object, which represents a request for storage by a developer. It is similar to a pod in that pods consume node resources and PVCs consume PV resources. For example, pods can request specific levels of resources, such as CPU and memory, while PVCs can request specific storage capacity and access modes. For example, they can be mounted once read-write or many times read-only.

Like `PersistentVolumes`, `PersistentVolumeClaims` (PVCs) are API objects, which represents a request for storage by a developer. It is similar to a pod in that pods consume node resources and PVCs consume PV resources. For example, pods can request specific levels of resources, such as CPU and memory, while PVCs can request specific storage capacity and access modes. Access modes supported by {OCP} are also definable in OpenShift Container Platform. However, because OpenShift Container Platform does not support multi-node deployments, only ReadWriteOnce (RWO) is pertinent.

[role="_additional-resources"]
== Additional resources

* Access modes for persistent storage

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id=lifecycle-volume-claim_{context}]
= Lifecycle of a volume and claim

PVs are resources in the cluster. PVCs are requests for those resources
and also act as claim checks to the resource. The interaction between PVs
and PVCs have the following lifecycle.

[id="provisioning_{context}"]
== Provision storage

In response to requests from a developer defined in a PVC, a cluster
administrator configures one or more dynamic provisioners that provision
storage and a matching PV.

Alternatively, a cluster administrator can create a number of PVs in advance
that carry the details of the real storage that is available for use. PVs
exist in the API and are available for use.

[id="binding_{context}"]
== Bind claims

When you create a PVC, you request a specific amount of storage, specify the
required access mode, and create a storage class to describe and classify
the storage. The control loop in the master watches for new PVCs and binds
the new PVC to an appropriate PV. If an appropriate PV does not exist, a
provisioner for the storage class creates one.

The size of all PVs might exceed your PVC size. This is especially true
with manually provisioned PVs. To minimize the excess, OpenShift Container Platform
binds to the smallest PV that matches all other criteria.

Claims remain unbound indefinitely if a matching volume does not exist or
can not be created with any available provisioner servicing a storage
class. Claims are bound as matching volumes become available. For example,
a cluster with many manually provisioned 50Gi volumes would not match a
PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the
cluster.

[id="using-pods_{context}"]
== Use pods and claimed PVs

Pods use claims as volumes. The cluster inspects the claim to find the bound
volume and mounts that volume for a pod. For those volumes that support
multiple access modes, you must specify which mode applies when you use
the claim as a volume in a pod.

Once you have a claim and that claim is bound, the bound PV belongs to you
for as long as you need it. You can schedule pods and access claimed
PVs by including `persistentVolumeClaim` in the pod's volumes block.

[NOTE]
====
If you attach persistent volumes that have high file counts to pods, those pods can fail or can take a long time to start. For
more information, see When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state?.
====

[id="pvcprotection_{context}"]
== Storage Object in Use Protection

The Storage Object in Use Protection feature ensures that PVCs in active use by a pod and PVs that are bound to PVCs are not removed from the system, as this can result in data loss.

Storage Object in Use Protection is enabled by default.

[NOTE]
====
A PVC is in active use by a pod when a `Pod` object exists that uses the PVC.
====

If a user deletes a PVC that is in active use by a pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any pods. Also, if a cluster admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC.

[id="releasing_{context}"]
== Release a persistent volume

When you are finished with a volume, you can delete the PVC object from
the API, which allows reclamation of the resource. The volume is
considered released when the claim is deleted, but it is not yet available
for another claim. The previous claimant's data remains on the volume and
must be handled according to policy.

[id="reclaiming_{context}"]
== Reclaim policy for persistent volumes

The reclaim policy of a persistent volume tells the cluster what to do with the volume after it is released. A volume's reclaim policy can be
`Retain`, `Recycle`, or `Delete`.

* `Retain` reclaim policy allows manual reclamation of the resource for
those volume plugins that support it.

* `Recycle` reclaim policy recycles the volume back into the pool of
unbound persistent volumes once it is released from its claim.

[IMPORTANT]
====
The `Recycle` reclaim policy is deprecated in OpenShift Container Platform 4. Dynamic provisioning is recommended for equivalent and better
functionality.
====

* `Delete` reclaim policy deletes  both the `PersistentVolume` object
from OpenShift Container Platform and the associated storage asset in external
infrastructure, such as Amazon Elastic Block Store (Amazon EBS) or VMware vSphere.

[NOTE]
====
Dynamically provisioned volumes are always deleted.
====

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="reclaim-manual_{context}"]
= Reclaiming a persistent volume manually

When a persistent volume claim (PVC) is deleted, the persistent volume (PV) still exists and is considered "released". However, the PV is not yet available for another claim because the data of the previous claimant remains on the volume.

When a persistent volume claim (PVC) is deleted, the underlying logical volume is handled according to the `reclaimPolicy`.

.Procedure
To manually reclaim the PV as a cluster administrator:

. Delete the PV by running the following command:
+
[source,terminal]
----
$ oc delete pv <pv_name>
----
+
The associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume, still exists after the PV is deleted.
The associated storage asset in the external infrastructure, such as an AWS EBS or GCE PD volume, still exists after the PV is deleted.
The associated storage asset in the external infrastructure, such as an Amazon Elastic Block Store (Amazon EBS) volume, still exists after the PV is deleted.

. Clean up the data on the associated storage asset.

. Delete the associated storage asset. Alternately, to reuse the same storage asset, create a new PV with the storage asset definition.

The reclaimed PV is now available for use by another PVC.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="reclaim-policy_{context}"]
= Changing the reclaim policy of a persistent volume

You can change the reclaim policy of a persistent volume.

.Procedure

. List the persistent volumes in your cluster:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
----

. Choose one of your persistent volumes and change its reclaim policy:
+
[source,terminal]
----
$ oc patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
----

. Verify that your chosen persistent volume has the right policy:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     3s
----
+
In the preceding output, the volume bound to claim `default/claim3` now has a `Retain` reclaim policy. The volume will not be automatically deleted when a user deletes claim `default/claim3`.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="persistent-volumes_{context}"]
= Persistent volumes

Each PV contains a `spec` and `status`, which is the specification and status of the volume, for example:

.`PersistentVolume` object definition example
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001 <1>
spec:
  capacity:
    storage: 5Gi <2>
  accessModes:
    - ReadWriteOnce <3>
  persistentVolumeReclaimPolicy: Retain <4>
  ...
status:
  ...
----
<1> Name of the persistent volume.
<2> The amount of storage available to the volume.
<3> The access mode, defining the read-write and mount permissions.
<4> The reclaim policy, indicating how the resource should be handled once it is released.

You can view the name of a PVC that is bound to a PV by running the following command:

[source,terminal]
----
$ oc get pv <pv_name> -o jsonpath='{.spec.claimRef.name}'
----

[id="types-of-persistent-volumes_{context}"]
== Types of PVs

OpenShift Container Platform supports the following persistent volume plugins:
OpenShift Container Platform supports the following persistent volume storage options:

// - GlusterFS
// - Ceph RBD
// - OpenStack Cinder
- AWS Elastic Block Store (EBS), which is installed by default.
- AWS Elastic File Store (EFS)
- Azure Disk
- Azure File
- Cinder
- Fibre Channel
- GCP Persistent Disk
- GCP Filestore
- {ibm-power-server-title} Block
- {ibm-cloud-name} VPC Block
- HostPath
- iSCSI
- Local volume
- {lvms}
- NFS
- OpenStack Manila
- {rh-storage-first}
- CIFS/SMB
- VMware vSphere
// - Local

OpenShift Container Platform functions with Kubernetes Container Storage Interface (CSI) compatible volume provisioners from other storage vendors. For more information about CSI drivers in OpenShift Container Platform, see _Configuring CSI volumes_ in the _Additional resources_ section.

[id="pv-capacity_{context}"]
== Capacity

Generally, a persistent volume (PV) has a specific storage capacity. This is set by using the `capacity` attribute of the PV.

Currently, storage capacity is the only resource that can be set or requested. Future attributes may include IOPS, throughput, and so on.

[id="pv-access-modes_{context}"]
== Access modes

A persistent volume can be mounted on a host in any way supported by the resource provider. Providers have different capabilities and each PV's access modes are set to the specific modes supported by that particular volume. For example, NFS can support multiple read-write clients, but a specific NFS PV might be exported on the server as read-only. Each PV gets its own set of access modes describing that specific PV's capabilities.

Claims are matched to volumes with similar access modes. The only two matching criteria are access modes and size. A claim's access modes represent a request. Therefore, you might be granted more, but never less. For example, if a claim requests RWO, but the only volume available is an NFS PV (RWO+ROX+RWX), the claim would then match NFS because it supports RWO.

Direct matches are always attempted first. The volume's modes must match or contain more modes than you requested. The size must be greater than or equal to what is expected. If two types of volumes, such as NFS and iSCSI, have the same set of access modes, either of them can match a claim with those modes. There is no ordering between types of volumes and no way to choose one type over another.

All volumes with the same modes are grouped, and then sorted by size, smallest to largest. The binder gets the group with matching modes and iterates over each, in size order, until one size matches.

[IMPORTANT]
====
Volume access modes describe volume capabilities. They are not enforced constraints. The storage provider is responsible for runtime errors resulting from invalid use of the resource. Errors in the provider show up at runtime as mount errors.

For example, NFS offers `ReadWriteOnce` access mode. If you want to use the volume's ROX capability, mark the claims as `ReadOnlyMany`.

iSCSI and Fibre Channel volumes do not currently have any fencing mechanisms. You must ensure the volumes are only used by one node at a time. In certain situations, such as draining a node, the volumes can be used simultaneously by two nodes. Before draining the node, delete the pods that use the volumes.
====

The following table lists the access modes:

.Access modes
[cols="1,1,3",options="header"]
|===
|Access Mode |CLI abbreviation |Description
|ReadWriteOnce
|`RWO`
|The volume can be mounted as read-write by a single node.
|ReadWriteOncePod
|`RWOP`
|The volume can be mounted as read-write by a single pod on a single node.
|ReadOnlyMany
|`ROX`
|The volume can be mounted as read-only by many nodes.
|ReadWriteMany
|`RWX`
|The volume can be mounted as read-write by many nodes.
|===

.Supported access modes for persistent volumes
[cols=",^v,^v,^v,^v", width="100%",options="header"]
|===
|Volume plugin  |ReadWriteOnce ^[1]^ | ReadWriteOncePod |ReadOnlyMany|ReadWriteMany
|AWS EBS ^[2]^ | ✅ | ✅ |  |
|AWS EFS | ✅ | ✅ | ✅ | ✅
|Azure File | ✅ |✅ | ✅ | ✅
|Azure Disk | ✅ | ✅ |   |
//|Ceph RBD  | ✅ | ✅ |✅ |
//|CephFS  | ✅ | ✅ | ✅ |  ✅
|CIFS/SMB | ✅ | ✅ | ✅ | ✅
|Cinder  | ✅ | ✅ | |
|Fibre Channel  | ✅ | ✅ |✅ |  ✅ ^[3]^
|GCP Persistent Disk  | ✅ ^[4]^ |✅ | ✅ | ✅ ^[4]^
|GCP Filestore | ✅ | ✅ |✅ | ✅
//|GlusterFS  | ✅ |✅ | ✅ | ✅
|HostPath  | ✅ |✅ |   |
|{ibm-power-server-title}  Disk | ✅ |✅  | ✅ |  ✅
|{ibm-cloud-name} VPC Disk | ✅ |✅ |  |
|iSCSI  | ✅ | ✅ |✅ |  ✅ ^[3]^
|Local volume | ✅ |✅ |  |
|LVM Storage | ✅ | ✅ |   |
|NFS  | ✅ | ✅ |✅ | ✅
|OpenStack Manila  |  |✅ |  | ✅
|{rh-storage-first}  | ✅ |✅ |  | ✅
|VMware vSphere | ✅ |✅ |  |  ✅ ^[5]^
|===
[.small]
--
1. ReadWriteOnce (RWO) volumes cannot be mounted on multiple nodes. If a node fails, the system does not allow the attached RWO volume to be mounted on a new node because it is already assigned to the failed node. If you encounter a multi-attach error message as a result, force delete the pod on a shutdown or crashed node to avoid data loss in critical workloads, such as when dynamic persistent volumes are attached.

2. Use a recreate deployment strategy for pods that rely on AWS EBS.

3. Only raw block volumes support the `ReadWriteMany` (RWX) access mode for Fibre Channel and iSCSI. For more information, see "Block volume support".

4. For GCP hyperdisk-balanced disks:
+
* The supported access modes are:
** `ReadWriteOnce`
** `ReadWriteMany`

* Cloning and snapshotting is disabled for disks with `ReadWriteMany` access mode enabled.

* You can attach a single hyperdisk-balanced disk volume in `ReadWriteMany` to a maximum of 8 instances.

* You can only resize a disk in `ReadWriteMany` if you detach the disk from all instances.

* https://cloud.google.com/compute/docs/disks/attach-disks[Additional limitations].

5. If the underlying vSphere environment supports the vSAN file service, the vSphere Container Storage Interface (CSI) Driver Operator installed by OpenShift Container Platform supports provisioning of ReadWriteMany (RWX) volumes. If you do not have vSAN file service configured, and you request RWX, the volume fails to get created and an error is logged. For more information, see "Using Container Storage Interface" -> "VMware vSphere CSI Driver Operator".
// GCE Persistent Disks, or Openstack Cinder PVs.
--

[id="supported-access-modes_{context}"]
== Supported access modes
LVMS is the only CSI plugin OpenShift Container Platform supports. The hostPath and LVs built in to {OCP} also support RWO.

[id="pv-restrictions_{context}"]
== Restrictions

The following restrictions apply when using PVs with OpenShift Container Platform:

 * PVs are provisioned with EBS volumes (AWS).
 * Only RWO access mode is applicable, as EBS volumes and GCE Persistent Disks cannot be mounted to multiple nodes.
 * Docker volumes are disabled.
   ** VOLUME directive without a mapped external volume fails to be
instantiated
.
 * *emptyDir* is restricted to 512 Mi per project (group) per node.
   ** A single pod for a project on a particular node can use up to 512 Mi
of *emptyDir* storage.
   ** Multiple pods for a project on a particular node share the 512 Mi of
*emptyDir* storage.
 *  *emptyDir* has the same lifecycle as the pod:
   ** *emptyDir* volumes survive container crashes/restarts.
   ** *emptyDir* volumes are deleted when the pod is deleted.

[id="pv-phase_{context}"]
== Phase

Volumes can be found in one of the following phases:

.Volume phases
[cols="1,2",options="header"]
|===

|Phase
|Description

|Available
|A free resource not yet bound to a claim.

|Bound
|The volume is bound to a claim.

|Released
|The claim was deleted, but the resource is not yet reclaimed by the
cluster.

|Failed
|The volume has failed its automatic reclamation.

|===

=== Last phase transition time
The `LastPhaseTransitionTime` field has a timestamp that updates every time a persistent volume (PV) transitions to a different phase (`pv.Status.Phase`). To find the time of the last phase transition for a PV, run the following command:

[source,terminal]
----
$ oc get pv <pv_name> -o json | jq '.status.lastPhaseTransitionTime' <1>
----
<1> Specify the name of the PV that you want to see the last phase transition.

[id="pv-mount-options_{context}"]
=== Mount options

You can specify mount options while mounting a PV by using the attribute `mountOptions`.

For example:

.Mount options example
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  mountOptions: <1>
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
  persistentVolumeReclaimPolicy: Retain
  claimRef:
    name: claim1
    namespace: default
----
<1> Specified mount options are used while mounting the PV to the disk.

The following PV types support mount options:

// - GlusterFS
// - Ceph RBD
- AWS Elastic Block Store (EBS)
- AWS Elastic File Storage (EFS)
- Azure Disk
- Azure File
- Cinder
- GCE Persistent Disk
- iSCSI
- Local volume
- NFS
- {rh-storage-first} (Ceph RBD only)
- CIFS/SMB
- VMware vSphere

[NOTE]
====
Fibre Channel and HostPath PVs do not support mount options.
====

.Mount options example
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  name: topolvm-provisioner
mountOptions:
  - uid=1500
  - gid=1500
parameters:
  csi.storage.k8s.io/fstype: xfs
provisioner: topolvm.io
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
----

[NOTE]
====
The `mountOptions` parameter values are not validated. Incorrect values cause the mount to fail and an event to be logged to the PVC.
====

// Module included in the following assemblies:
//
// * microshift_storage/understanding-persistent-storage-microshift.adoc

[id=microshift-pv-rwo-access-mode-permission_{context}]
= Persistent volumes with RWO access mode permissions

[role="_abstract"]
To enable concurrent access for pods on a single node, configure the `ReadWriteOnce` (RWO) access mode for your Persistent Volume Claims (PVCs). This setting allows multiple workloads on the same node to read from and write to the same Persistent Volume (PV) simultaneously.

Sometimes pods of the same node are not able to read or write into the same PV. This happens when the pods in the node do not have the same SELinux context.

Persistent volumes can be mounted, while later claimed by PVCs, with the RWO access mode.

// Module included in the following assemblies:
//
// * microshift_storage/understanding-persistent-storage-microshift.adoc

[id="microshift-checking-pods-mismatch_{context}"]
= Checking the pods for mismatch

[role="_abstract"]
To ensure workload consistency, check the pods running on {microshift-short} for mismatches. Identifying these discrepancies helps verify that your running workloads match the expected configuration.

.Procedure

. List the mount point within the first pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc get pods -n _<pod_name_a>_ -ojsonpath='{.spec.containers[*].volumeMounts[*].mountPath}'
----
** Replace `_<pod_name_a>_` with the name of the first pod.
+
.Example output
[source,terminal]
----
/files /var/run/secrets/kubernetes.io/serviceaccount
----

. List the mount point within the second pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc get pods -n _<pod_name_b>_ -ojsonpath='{.spec.containers[*].volumeMounts[*].mountPath}'
----
** Replace `_<pod_name_b>_` with the name of the second pod.
+
.Example output
[source,terminal]
----
/files /var/run/secrets/kubernetes.io/serviceaccount
----

. Check the context and permissions inside the first pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc rsh _<pod_name_a>_ ls -lZah _<pvc_mountpoint>_
----
** Replace `_<pod_name_a>_` with the name of the first pod.
** Replace `_<pvc_mountpoint>_` with the mount point within the first pod.
+
.Example output
[source,terminal]
----
total 12K
dr-xr-xr-x.   1 root root system_u:object_r:container_file_t:s0:c398,c806   40 Feb 17 13:36 .
dr-xr-xr-x.   1 root root system_u:object_r:container_file_t:s0:c398,c806   40 Feb 17 13:36 ..
[...]
----

. Check the context and permissions inside the second pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc rsh _<pod_name_b>_ ls -lZah _<pvc_mountpoint>_
----
** Replace `_<pod_name_b>_` with the name of the second pod.
** Replace `_<pvc_mountpoint>_` with the mount point within the second pod.
+
.Example output
[source,terminal]
----
total 12K
dr-xr-xr-x.   1 root root system_u:object_r:container_file_t:s0:c15,c25   40 Feb 17 13:34 .
dr-xr-xr-x.   1 root root system_u:object_r:container_file_t:s0:c15,c25   40 Feb 17 13:34 ..
[...]
----

. Compare both the outputs to check if there is a mismatch of SELinux context.

// Module included in the following assemblies:
//
// * microshift_storage/understanding-persistent-storage-microshift.adoc

[id="microshift-updating-pods-mismatch_{context}"]
= Updating the pods which have mismatch

[role="_abstract"]
To resolve configuration discrepancies, update the SELinux context of the pods that display a mismatch status. This process ensures that your running workloads align with the expected configuration, maintaining consistency across your cluster.

.Procedure

. When there is a mismatch of the SELinux content, create a new security context constraint (SCC) and assign it to both pods. To create a SCC, see "Creating security context constraints".

. Update the SELinux context as shown in the following example:
+
.Example output
[source,terminal]
----
 [...]
 securityContext:privileged
      seLinuxOptions:MustRunAs
        level: "s0:cXX,cYY"
  [...]
----

[role="_additional-resources"]
.Additional resources

* Creating security context constraints

// Module included in the following assemblies:
//
// * microshift_storage/understanding-persistent-storage-microshift.adoc

[id="microshift-verifying-pods-mismatch_{context}"]
= Verifying pods after resolving a mismatch

[role="_abstract"]
To confirm that the mismatch is resolved, verify the security context constraint (SCC) and the SELinux label of the pods. Checking these settings ensures that your workloads are functioning with the correct security configurations.

.Procedure

. Verify that the same SCC is assigned to the first pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc describe pod _<pod_name_a>_ |grep -i scc
----
** Replace `_<pod_name_a>_` with the name of the first pod.
+
.Example output
[source,terminal]
----
openshift.io/scc: restricted
----

. Verify that the same SCC is assigned to first second pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc describe pod _<pod_name_b>_ |grep -i scc
----
** Replace `_<pod_name_b>_` with the name of the second pod.
+
.Example output
[source,terminal]
----
openshift.io/scc: restricted
----

. Verify that the same SELinux label is applied to first pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc exec _<pod_name_a>_ -- ls -laZ _<pvc_mountpoint>_
----
** Replace `_<pod_name_a>_` with the name of the first pod.
** Replace `_<pvc_mountpoint>_` with the mount point within the first pod.
+
.Example output
[source,terminal]
----
total 4
drwxrwsrwx. 2 root       1000670000 system_u:object_r:container_file_t:s0:c10,c26 19 Aug 29 18:17 .
dr-xr-xr-x. 1 root       root       system_u:object_r:container_file_t:s0:c10,c26 61 Aug 29 18:16 ..
-rw-rw-rw-. 1 1000670000 1000670000 system_u:object_r:container_file_t:s0:c10,c26 29 Aug 29 18:17 test1
[...]
----

. Verify that the same SELinux label is applied to second pod by running the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc exec _<pod_name_b>_ -- ls -laZ _<pvc_mountpoint>_
----
** Replace `_<pod_name_b>_` with the name of the second pod.
** Replace `_<pvc_mountpoint>_` with the mount point within the second pod.
+
.Example output
[source,terminal]
----
total 4
drwxrwsrwx. 2 root       1000670000 system_u:object_r:container_file_t:s0:c10,c26 19 Aug 29 18:17 .
dr-xr-xr-x. 1 root       root       system_u:object_r:container_file_t:s0:c10,c26 61 Aug 29 18:16 ..
-rw-rw-rw-. 1 1000670000 1000670000 system_u:object_r:container_file_t:s0:c10,c26 29 Aug 29 18:17 test1
[...]
----

[role="_additional-resources"]
.Additional resources
* Common mount options

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="storage-persistent-storage-pvc_{context}"]
= Persistent volume claims

[role="_abstract"]
To define storage requirements for your workloads, review the structure of a `PersistentVolumeClaim` (PVC). This object includes a `spec` field to configure the request and a `status` field to monitor the current state of the claim.

.`PersistentVolumeClaim` object definition example
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
  storageClassName: gold
status:
# ...
----

where:

`apiVersion`:: Specifies the name of the PVC.

`spec.accessModes`:: Specifies the access mode, defining the read/write and mount permissions.

`requests.storage`:: Specifies the amount of storage available to the PVC.

`storageClassName`:: Specifies the name of the `StorageClass` required by the claim.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="pvc-storage-class_{context}"]
= Storage classes

[role="_abstract"]
To request specific storage capabilities, define the `StorageClass` name in the `storageClassName` attribute of your `PersistentVolumeClaim` (PVC). This setting ensures the claim binds only to matching `PersistentVolumes` (PVs) or triggers dynamic provisioning if the cluster administrator has configured on-demand creation.

[IMPORTANT]
====
The Cluster Storage Operator might install a default storage class depending on the platform in use. This storage class is owned and controlled by the Operator. The storage class cannot be deleted or modified beyond defining annotations and labels. If different behavior is desired, you must define a custom storage class.
====

[IMPORTANT]
====
The Cluster Storage Operator installs a default storage class. This storage class is owned and controlled by the Operator. The storage class cannot be deleted or modified beyond defining annotations and labels. If different behavior is desired, you must define a custom storage class.
====

The cluster administrator can also set a default storage class for all PVCs. When you configure a default storage class, the PVC must explicitly ask for `StorageClass` or `storageClassName` annotations set to `""` to be bound to a PV without a storage class.

[NOTE]
====
If more than one storage class is marked as default, a PVC can only be created if the `storageClassName` is explicitly specified. Therefore, only set one storage class as the default.
====

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="pvc-claims-as-volumes_{context}"]
= Claims as volumes

[role="_abstract"]
To enable pods to access storage resources, configure Persistent Volume Claims (PVCs) as volumes. By mounting the claim to the host and into the pod, the cluster locates the backing `PersistentVolume` (PV) in the same namespace, ensuring the workload can read and write data effectively.

Claims use the same conventions as volumes when requesting storage with specific access modes.

Claims, such as pods, can request specific quantities of a resource. In this case, the request is for storage. The same resource model applies to volumes and claims.

.Mount volume to the host and into the pod example
[source,yaml]
----
kind: Pod
apiVersion: v1
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: dockerfile/nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
# ...
----

where:

`volumeMounts.mountPath`:: Specifies the path to mount the volume inside the pod.

`volumeMounts.name`:: Specifies the name of the volume to mount. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. Using `/host` is a safe option for mounting the host.

`persistentVolumeClaim.claimName`:: Specifies the name of the PVC, that exists in the same namespace, to use.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="pvc-cli-command-usage_{context}"]
= Setting PVC viewing permissions

[role="_abstract"]
To monitor storage resources, verify that you have the necessary privileges to view Persistent Volume Claim (PVC) usage statistics. Ensuring you have the correct permissions means that you can access usage data and track resource consumption effectively.

To view PVC usage statistics, you must have the necessary privileges.

.Procedure

* If you have admin privileges, log on to {microshift-short} as an `admin`.

* If you do not have admin privileges, complete the following steps:
+
** Create cluster roles for the user by running the following command:
+
[source,terminal]
----
$ oc create clusterrole routes-view --verb=get,list --resource=routes
----
+
** Add the `routes-view` cluster role for the user by running the following command:
+
[source,terminal]
----
$ oc admin policy add-cluster-role-to-user routes-view _<user_name>_
----
** Replace `_<user_name>_` with the user name.
+
** Add the `cluster-monitoring-view` cluster role for the user by running the following command:
+
[source,terminal]
----
$ oc admin policy add-cluster-role-to-user cluster-monitoring-view _<user_name>_
----
** Replace `_<user_name>_` with the user name.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="viewing-pvc-usage-statistics_{context}"]
= Viewing PVC usage statistics

[role="_abstract"]
To monitor storage consumption, view the usage statistics for Persistent Volume Claims (PVCs). By accessing these metrics, you can track resource use and ensure that your workloads have sufficient capacity.

.Procedure

* To view statistics across a cluster, run the following command:
+
[source, terminal]
----
$ oc adm top pvc -A
----
+
.Example command output
[source,terminal]
----
NAMESPACE     NAME         USAGE(%)
namespace-1   data-etcd-1  3.82%
namespace-1   data-etcd-0  3.81%
namespace-1   data-etcd-2  3.81%
namespace-2   mypvc-fs-gp3 0.00%
default       mypvc-fs     98.36%
----

* To view PVC usage statistics for a specified namespace, run the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc adm top pvc -n _<namespace_name>_
----
** Where `_<namespace_name>_` is the name of the specified namespace.
+
.Example command output
[source,terminal]
----
NAMESPACE     NAME        USAGE(%)
namespace-1   data-etcd-2 3.81%
namespace-1   data-etcd-0 3.81%
namespace-1   data-etcd-1 3.82%
----
+
In this example, the specified namespace is `namespace-1`.

* To view usage statistics for a specified PVC and for a specified namespace, run the following command:
+
[source,terminal]
[subs="+quotes"]
----
$ oc adm top pvc _<pvc_name>_ -n _<namespace_name>_
----
** Where `_<pvc_name>_` is the name of specified PVC.
** Where `_<namespace_name>_` is the name of the specified namespace.
+
.Example command output
[source,terminal]
----
NAMESPACE   NAME        USAGE(%)
namespace-1 data-etcd-0 3.81%
----
+
In this example, the specified namespace is `namespace-1` and the specified PVC is `data-etcd-0`.

// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc

[id="storage-persistent-storage-fsGroup_{context}"]
= Reduce pod timeouts by using fsGroup

[role="_abstract"]
To reduce pod timeouts when using a storage volume with many files, configure the `fsGroup` field. By specifying this field, you can manage how file ownership and permissions are applied, preventing delays caused by the default recursive permission changes on large volumes.

This can occur because, by default, OpenShift Container Platform recursively changes ownership and permissions for the contents of each volume to match the `fsGroup` specified in the `securityContext` of the pod when that volume is mounted. For volumes with many files, checking and changing ownership and permissions can be time consuming, slowing pod startup. You can use the `fsGroupChangePolicy` field inside a `securityContext` to control the way that OpenShift Container Platform checks and manages ownership and permissions for a volume.

`fsGroupChangePolicy` defines behavior for changing ownership and permission of the volume before being exposed inside a pod. This field only applies to volume types that support `fsGroup`-controlled ownership and permissions. This field has two possible values:

* `OnRootMismatch`: Only change permissions and ownership if permission and ownership of root directory does not match with expected permissions of the volume. This can help shorten the time it takes to change ownership and permission of a volume to reduce pod timeouts.

* `Always`: (Default) Always change permission and ownership of the volume when a volume is mounted.

[NOTE]
====
The `fsGroupChangePolicy` field has no effect on ephemeral volume types, such as secret, configMap, and emptydir.
====

You can set `fsGroupChangePolicy` at either the namespace or pod level.
