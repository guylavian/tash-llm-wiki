---
title: "OpenStack Cinder CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-cinder
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-cinder
version: 4.22
family: storage
documentKind: "Documentation"
---

# OpenStack Cinder CSI Driver Operator

[id="persistent-storage-csi-cinder"]
= OpenStack Cinder CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for OpenStack Cinder.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a Container Storage Interface (CSI) Operator and driver.

To create CSI-provisioned PVs that mount to OpenStack Cinder storage assets, OpenShift Container Platform installs the OpenStack Cinder CSI Driver Operator and the OpenStack Cinder CSI driver in the `openshift-cluster-csi-drivers` namespace.

* The _OpenStack Cinder CSI Driver Operator_ provides a CSI storage class that you can use to create PVCs. You can disable this default storage class if desired (see Managing the default storage class).

* The _OpenStack Cinder CSI driver_ enables you to create and mount OpenStack Cinder PVs.

[NOTE]
====
OpenShift Container Platform provides automatic migration for the Cinder in-tree volume plugin to its equivalent CSI driver. For more information, see CSI automatic migration.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

[IMPORTANT]
====
OpenShift Container Platform defaults to using the CSI plugin to provision Cinder storage.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-cinder.adoc

[id="persistent-storage-csi-cinder_{context}"]
= Making OpenStack Cinder CSI the default storage class

The OpenStack Cinder CSI driver uses the `cinder.csi.openstack.org` parameter key to support dynamic provisioning.

To enable OpenStack Cinder CSI provisioning in OpenShift Container Platform, it is recommended that you overwrite the default in-tree storage class with `standard-csi`. Alternatively, you can create the persistent volume claim (PVC) and specify the storage class as "standard-csi".

In OpenShift Container Platform, the default storage class references the in-tree Cinder driver. However, with CSI automatic migration enabled, volumes created using the default storage class actually use the CSI driver.

.Procedure
Use the following steps to apply the `standard-csi` storage class by overwriting the default in-tree storage class.

. List the storage class:
+
[source,terminal]
--
$ oc get storageclass
--
+
[source,terminal]
.Example output
--
NAME                   PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard(default)      cinder.csi.openstack.org   Delete          WaitForFirstConsumer   true                   46h
standard-csi           kubernetes.io/cinder       Delete          WaitForFirstConsumer   true                   46h
--

. Change the value of the annotation `storageclass.kubernetes.io/is-default-class` to `false` for the default storage class, as shown in the following example:
+
[source,terminal]
--
$ oc patch storageclass standard -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "false"}}}'
--

. Make another storage class the default by adding or modifying the annotation as `storageclass.kubernetes.io/is-default-class=true`.
+
[source,terminal]
--
$ oc patch storageclass standard-csi -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
--

. Verify that the PVC is now referencing the CSI storage class by default:
+
[source,terminal]
--
$ oc get storageclass
--
+
[source,terminal]
.Example output
--
NAME                   PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard               kubernetes.io/cinder       Delete          WaitForFirstConsumer   true                   46h
standard-csi(default)  cinder.csi.openstack.org   Delete          WaitForFirstConsumer   true                   46h
--

. Optional: You can define a new PVC without having to specify the storage class:
+
[source,yaml]
--
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cinder-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
--
+
A PVC that does not specify a specific storage class is automatically provisioned by using the default storage class.
+
. Optional: After the new file has been configured, create it in your cluster:
+
[source,terminal]
--
$ oc create -f cinder-claim.yaml
--

[role="_additional-resources"]
.Additional resources
* Configuring CSI volumes
