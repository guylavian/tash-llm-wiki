---
title: "Persistent storage using hostPath"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-hostpath
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-hostpath
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using hostPath

[id="persistent-storage-using-hostpath"]
= Persistent storage using hostPath

A hostPath volume in an OpenShift Container Platform cluster mounts a file or directory from the host node's filesystem into your pod. Most pods will not need a hostPath volume, but it does offer a quick option for testing should an application require it.

[IMPORTANT]
====
The cluster administrator must configure pods to run as privileged. This grants access to pods in the same node.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-hostpath.adoc

[id="persistent-storage-hostpath-about_{context}"]
= Overview

OpenShift Container Platform supports hostPath mounting for development and testing on a single-node cluster.

In a production cluster, you would not use hostPath. Instead, a cluster administrator would provision a network resource, such as a GCE Persistent Disk volume, an NFS share, or an Amazon EBS volume. Network resources support the use of storage classes to set up dynamic provisioning.

A hostPath volume must be provisioned statically.

[IMPORTANT]
====
Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged. It is safe to mount the host by using `/host`. The following example shows the `/` directory from the host being mounted into the container at `/host`.

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: test-host-mount
spec:
  containers:
  - image: registry.access.redhat.com/ubi9/ubi
    name: test-container
    command: ['sh', '-c', 'sleep 3600']
    volumeMounts:
    - mountPath: /host
      name: host-slash
  volumes:
   - name: host-slash
     hostPath:
       path: /
       type: ''
----
====

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-hostpath.adoc

[id="hostpath-static-provisioning_{context}"]
= Statically provisioning hostPath volumes

A pod that uses a hostPath volume must be referenced by manual (static) provisioning.

.Procedure

. Define the persistent volume (PV) by creating a `pv.yaml` file with the `PersistentVolume` object definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume <1>
  labels:
    type: local
spec:
  storageClassName: manual <2>
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce <3>
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/mnt/data" <4>
----
<1> The name of the volume. This name is how the volume is identified by persistent volume (PV) claims or pods.
<2> Used to bind persistent volume claim (PVC) requests to the PV.
<3> The volume can be mounted as `read-write` by a single node.
<4> The configuration file specifies that the volume is at `/mnt/data` on the cluster's node. To avoid corrupting your host system, do not mount to the container root, `/`, or any path that is the same in the host and the container. You can safely mount the host by using `/host`

. Create the PV from the file:
+
[source,terminal]
----
$ oc create -f pv.yaml
----

. Define the PVC by creating a `pvc.yaml` file with the `PersistentVolumeClaim` object definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pvc-volume
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: manual
----

. Create the PVC from the file:
+
[source,terminal]
----
$ oc create -f pvc.yaml
----

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-hostpath.adoc

[id="persistent-storage-hostpath-pod_{context}"]
= Mounting the hostPath share in a privileged pod

After the persistent volume claim has been created, it can be used inside by an application. The following example demonstrates mounting this share inside of a pod.

.Prerequisites
* A persistent volume claim exists that is mapped to the underlying hostPath share.

.Procedure

* Create a privileged pod that mounts the existing persistent volume claim:
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
    securityContext:
      privileged: true <2>
    volumeMounts:
    - mountPath: /data <3>
      name: hostpath-privileged
  ...
  securityContext: {}
  volumes:
    - name: hostpath-privileged
      persistentVolumeClaim:
        claimName: task-pvc-volume <4>
----
<1> The name of the pod.
<2> The pod must run as privileged to access the node's storage.
<3> The path to mount the host path share inside the privileged pod. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. It is safe to mount the host by using `/host`.
<4> The name of the `PersistentVolumeClaim` object that has been previously created.
