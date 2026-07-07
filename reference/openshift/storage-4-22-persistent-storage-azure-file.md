---
title: "Persistent storage using Azure File"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-azure-file
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-azure-file
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using Azure File

[id="persistent-storage-using-azure-file"]
= Persistent storage using Azure File

OpenShift Container Platform supports Microsoft Azure File volumes. You can
provision your OpenShift Container Platform cluster with persistent storage using Azure.
Some familiarity with Kubernetes and Azure is assumed.

The Kubernetes persistent volume framework allows administrators to provision a cluster with persistent storage and gives users a way to request those resources without having any knowledge of the underlying infrastructure.
You can provision Azure File volumes dynamically.

Persistent volumes are not bound to a single project or namespace, and you can share them across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace, and can be requested by users for use in applications.

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying
storage provider.
====

[IMPORTANT]
====
Azure File volumes use Server Message Block.
====

[IMPORTANT]
====
OpenShift Container Platform 4.13 and later provides automatic migration for the Azure File in-tree volume plugin to its equivalent CSI driver.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see CSI automatic migration.
====

.Additional resources

* Azure Files

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-azure-file.adoc

[id="create-azure-file-secret_{context}"]
= Create the Azure File share persistent volume claim

To create the persistent volume claim, you must first define a `Secret` object that contains the Azure account and key. This secret is used in the `PersistentVolume` definition, and will be referenced by the persistent volume claim for use in applications.

.Prerequisites

* An Azure File share exists.
* The credentials to access this share, specifically the storage account and
key, are available.

.Procedure

. Create a `Secret` object that contains the Azure File credentials:
+
[source,terminal]
----
$ oc create secret generic <secret-name> --from-literal=azurestorageaccountname=<storage-account> \ <1>
  --from-literal=azurestorageaccountkey=<storage-account-key> <2>
----
<1> The Azure File storage account name.
<2> The Azure File storage account key.

. Create a `PersistentVolume` object that references the `Secret` object you created:
+
[source,yaml]
----
apiVersion: "v1"
kind: "PersistentVolume"
metadata:
  name: "pv0001" <1>
spec:
  capacity:
    storage: "5Gi" <2>
  accessModes:
    - "ReadWriteOnce"
  storageClassName: azure-file-sc
  azureFile:
    secretName: <secret-name> <3>
    shareName: share-1 <4>
    readOnly: false
----
<1> The name of the persistent volume.
<2> The size of this persistent volume.
<3> The name of the secret that contains the Azure File share credentials.
<4> The name of the Azure File share.

. Create a `PersistentVolumeClaim` object that maps to the persistent volume you created:
+
[source,yaml]
----
apiVersion: "v1"
kind: "PersistentVolumeClaim"
metadata:
  name: "claim1" <1>
spec:
  accessModes:
    - "ReadWriteOnce"
  resources:
    requests:
      storage: "5Gi" <2>
  storageClassName: azure-file-sc <3>
  volumeName: "pv0001" <4>
----
<1> The name of the persistent volume claim.
<2> The size of this persistent volume claim.
<3> The name of the storage class that is used to provision the persistent volume.
Specify the storage class used in the `PersistentVolume` definition.
<4> The name of the existing `PersistentVolume` object that references the
Azure File share.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-azure-file.adoc

[id="create-azure-file-pod_{context}"]
= Mount the Azure File share in a pod

After the persistent volume claim has been created, it can be used inside by an application. The following example demonstrates mounting this share inside of a pod.

.Prerequisites

* A persistent volume claim exists that is mapped to the underlying Azure File share.

.Procedure

* Create a pod that mounts the existing persistent volume claim:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-name <1>
spec:
  containers:
    ...
    volumeMounts:
    - mountPath: "/data" <2>
      name: azure-file-share
  volumes:
    - name: azure-file-share
      persistentVolumeClaim:
        claimName: claim1 <3>
----
<1> The name of the pod.
<2> The path to mount the Azure File share inside the pod. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. It is safe to mount the host by using `/host`.
<3> The name of the `PersistentVolumeClaim` object that has been previously created.
