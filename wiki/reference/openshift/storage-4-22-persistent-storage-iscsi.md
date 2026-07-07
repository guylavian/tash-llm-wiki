---
title: "Persistent storage using iSCSI"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-iscsi
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-iscsi
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using iSCSI

[id="persistent-storage-using-iscsi"]
= Persistent storage using iSCSI

You can provision your OpenShift Container Platform cluster with
persistent storage using
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/managing_storage_devices/index#getting-started-with-iscsi_managing-storage-devices[iSCSI].
Some familiarity with Kubernetes and iSCSI is assumed.

The Kubernetes persistent volume framework allows administrators to
provision a cluster with persistent storage and gives users a way to
request those resources without having any knowledge of the
underlying infrastructure.

[IMPORTANT]
====
High-availability of storage in the infrastructure is left to the underlying
storage provider.
====

[IMPORTANT]
====
When you use iSCSI on Amazon Web Services, you must update the default
security policy to include TCP traffic between nodes on the iSCSI ports.
By default, they are ports `860` and `3260`.
====

[IMPORTANT]
====
Users must ensure that the iSCSI initiator is already configured on all
OpenShift Container Platform nodes by installing the `iscsi-initiator-utils`
package and configuring their initiator name in `/etc/iscsi/initiatorname.iscsi`.
The `iscsi-initiator-utils` package is already installed on deployments
that use {op-system-first}.

For more information, see https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/managing_storage_devices/index#configuring-an-iscsi-initiator_managing-storage-devices[Managing Storage Devices].
====

// Module included in the following assemblies
//
// * storage/persistent_storage-iscsi.adoc

[id="persistent-storage-iscsi-provisioning_{context}"]
= Provisioning

You can verify that the storage exists in the underlying infrastructure before mounting it as a volume in OpenShift Container Platform. All that is required for the iSCSI is the iSCSI target portal, a valid iSCSI Qualified Name (IQN), a valid LUN number, the filesystem type, and the `PersistentVolume` API.

.Procedure

* Verify that the storage exists in the underlying infrastructure before mounting it as a volume in OpenShift Container Platform by creating the following .`PersistentVolume` object definition:

.`PersistentVolume` object definition
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: iscsi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  iscsi:
     targetPortal: 10.16.154.81:3260
     iqn: iqn.2014-12.example.server:storage.target00
     lun: 0
     fsType: 'ext4'
----

// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="enforcing-disk-quotas-iscsi_{context}"]
= Enforce disk quotas

Use LUN partitions to enforce disk quotas and size constraints. Each LUN is one persistent volume. Kubernetes enforces unique names for persistent
volumes.

Enforcing quotas in this way allows the user to request persistent storage by a specific amount (for example, `10Gi`) and be matched with a
corresponding volume of equal or greater capacity.

// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="volume-security-iscsi_{context}"]
= iSCSI volume security

Users request storage with a `PersistentVolumeClaim` object. This claim only
lives in the user's namespace and can only be referenced by a pod within
that same namespace. Any attempt to access a persistent volume claim across a
namespace causes the pod to fail.

Each iSCSI LUN must be accessible by all nodes in the cluster.

== Challenge Handshake Authentication Protocol (CHAP) configuration

Optionally, OpenShift Container Platform can use CHAP to authenticate itself to iSCSI targets:

[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: iscsi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  iscsi:
    targetPortal: 10.0.0.1:3260
    iqn: iqn.2016-04.test.com:storage.target00
    lun: 0
    fsType: ext4
    chapAuthDiscovery: true <1>
    chapAuthSession: true <2>
    secretRef:
      name: chap-secret <3>
----
<1> Enable CHAP authentication of iSCSI discovery.
<2> Enable CHAP authentication of iSCSI session.
<3> Specify name of Secrets object with user name + password. This `Secret`
object must be available in all namespaces that can use the referenced volume.

// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="iscsi-multipath_{context}"]
= iSCSI multipathing

For iSCSI-based storage, you can configure multiple paths by using the same IQN for more than one target portal IP address. Multipathing ensures
access to the persistent volume when one or more of the components in a path fail.

.Procedure

* To specify multi-paths in the pod specification, specify a value in the `portals` field of the `PersistentVolume` definition object.

.Example PersistentVolume object with a value specified in the portals field.
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: iscsi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  iscsi:
    targetPortal: 10.0.0.1:3260
    portals: ['10.0.2.16:3260', '10.0.2.17:3260', '10.0.2.18:3260'] <1>
    iqn: iqn.2016-04.test.com:storage.target00
    lun: 0
    fsType: ext4
    readOnly: false
----
<1> Add additional target portals using the `portals` field.

// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="iscsi-custom-iqn_{context}"]
= iSCSI custom initiator IQN

Configure the custom initiator iSCSI Qualified Name (IQN) if the iSCSI targets are restricted to certain IQNs, but the nodes that the iSCSI PVs
are attached to are not guaranteed to have these IQNs.

.Procedure

* To specify a custom initiator IQN, update the `initiatorName` field in the `PersistentVolume` definition object .

.Example PersistentVolume object with a value specified in the initiatorName field.
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: iscsi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  iscsi:
    targetPortal: 10.0.0.1:3260
    portals: ['10.0.2.16:3260', '10.0.2.17:3260', '10.0.2.18:3260']
    iqn: iqn.2016-04.test.com:storage.target00
    lun: 0
    initiatorName: iqn.2016-04.test.com:custom.iqn <1>
    fsType: ext4
    readOnly: false
----
<1> Specify the name of the initiator.
