---
title: "Persistent storage using Cinder"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-cinder
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-cinder
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using Cinder

[id="persistent-storage-cinder"]
= Persistent storage using Cinder

OpenShift Container Platform supports OpenStack Cinder.  Some familiarity with Kubernetes and OpenStack is assumed.

Cinder volumes can be provisioned dynamically.
Persistent volumes are not bound to a single project or namespace; they can be
shared across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace and can be
requested by users.

[IMPORTANT]
====
OpenShift Container Platform 4.11 and later provides automatic migration for the Cinder in-tree volume plugin to its equivalent CSI driver.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see CSI automatic migration.
====

[role="_additional-resources"]
.Additional resources
* For more information about how OpenStack Block Storage provides persistent block storage management for virtual hard drives, see OpenStack Cinder.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage-cinder.adoc

[id="persistent-storage-cinder-provisioning_{context}"]
= Manual provisioning with Cinder

Storage must exist in the underlying infrastructure before it can be mounted as a volume in OpenShift Container Platform.

.Prerequisites

* OpenShift Container Platform configured for {rh-openstack-first}
* Cinder volume ID

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage-cinder.adoc

[id="persistent-storage-cinder-creating-pv_{context}"]
= Creating the persistent volume

You must define your persistent volume (PV) in an object definition before creating
it in OpenShift Container Platform:

.Procedure

. Save your object definition to a file.
+
.cinder-persistentvolume.yaml
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
  cinder: <3>
    fsType: "ext3" <4>
    volumeID: "f37a03aa-6212-4c62-a805-9ce139fab180" <5>
----
<1> The name of the volume that is used by persistent volume claims or pods.
<2> The amount of storage allocated to this volume.
<3> Indicates `cinder` for {rh-openstack-first} Cinder volumes.
<4> The file system that is created when the volume is mounted for the first time.
<5> The Cinder volume to use.
+
[IMPORTANT]
====
Do not change the `fstype` parameter value after the volume is formatted and
provisioned. Changing this value can result in data loss and pod failure.
====

. Create the object definition file you saved in the previous step.
+
[source,terminal]
----
$ oc create -f cinder-persistentvolume.yaml
----

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage-cinder.adoc

[id="persistent-storage-cinder-pv-format_{context}"]
= Persistent volume formatting

You can use unformatted Cinder volumes as PVs because
OpenShift Container Platform formats them before the first use.

Before OpenShift Container Platform mounts the volume and passes it to a container, the system checks that it contains a file system as specified by the `fsType` parameter in the
PV definition. If the device is not formatted with the file system, all data from the device is erased and the device is automatically formatted with the given file system.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage-cinder.adoc

[id="persistent-storage-cinder-volume-security_{context}"]
= Cinder volume security

If you use Cinder PVs in your application, configure security for their
deployment configurations.

.Prerequisites
- An SCC must be created that uses the appropriate `fsGroup` strategy.

.Procedure

. Create a service account and add it to the SCC:
+
[source,terminal]
----
$ oc create serviceaccount <service_account>
----
+
[source,terminal]
----
$ oc adm policy add-scc-to-user <new_scc> -z <service_account> -n <project>
----

. In your application's deployment configuration, provide the service account
name and `securityContext`:
+
[source,yaml]
----
apiVersion: v1
kind: ReplicationController
metadata:
  name: frontend-1
spec:
  replicas: 1  <1>
  selector:    <2>
    name: frontend
  template:    <3>
    metadata:
      labels:  <4>
        name: frontend <5>
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
      serviceAccountName: <service_account> <6>
      securityContext:
        fsGroup: 7777 <7>
----
<1> The number of copies of the pod to run.
<2> The label selector of the pod to run.
<3> A template for the pod that the controller creates.
<4> The labels on the pod. They must include labels from the label selector.
<5> The maximum name length after expanding any parameters is 63 characters.
<6> Specifies the service account you created.
<7> Specifies an `fsGroup` for the pods.
