---
title: "Managing the default storage class"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-sc-manage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-sc-manage
version: 4.22
family: storage
documentKind: "Documentation"
---

# Managing the default storage class

[id="persistent-storage-csi-sc-manage"]
= Managing the default storage class

== Overview

Managing the default storage class allows you to accomplish several different objectives:

* Enforcing static provisioning by disabling dynamic provisioning.

* When you have other preferred storage classes, preventing the storage operator from re-creating the initial default storage class.

* Renaming, or otherwise changing, the default storage class

To accomplish these objectives, you change the setting for the `spec.storageClassState` field in the `ClusterCSIDriver` object. The possible settings for this field are:

* *Managed*: (Default) The Container Storage Interface (CSI) operator is actively managing its default storage class, so that most manual changes made by a cluster administrator to the default storage class are removed, and the default storage class is continuously re-created if you attempt to manually delete it.

* *Unmanaged*: You can modify the default storage class. The CSI operator is not actively managing storage classes, so that it is not reconciling the default storage class it creates automatically.

* *Removed*: The CSI operators deletes the default storage class.

Managing the default storage classes is supported by the following Container Storage Interface (CSI) driver operators:

* Amazon Web Services (AWS) Elastic Block Storage (EBS)

* Azure Disk

* Azure File

* Google Cloud Platform (GCP) Persistent Disk (PD)

* {ibm-cloud-name} VPC Block

* OpenStack Cinder

* VMware vSphere

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc
//

[id="persistent-storage-csi-sc-managing_{context}"]
= Managing the default storage class using the web console

.Prerequisites
* Access to the OpenShift Container Platform web console.

* Access to the cluster with cluster-admin privileges.

.Procedure

To manage the default storage class using the web console:

. Log in to the web console.

. Click *Administration* > *CustomResourceDefinitions*.

. On the *CustomResourceDefinitions* page, type `clustercsidriver` to find the `ClusterCSIDriver` object.

. Click *ClusterCSIDriver*, and then click the *Instances* tab.

. Click the name of the desired instance, and then click the *YAML* tab.

. Add the `spec.storageClassState` field with a value of `Managed`, `Unmanaged`, or `Removed`.
+
.Example
[source, yaml]
----
...
spec:
  driverConfig:
    driverType: ''
  logLevel: Normal
  managementState: Managed
  observedConfig: null
  operatorLogLevel: Normal
  storageClassState: Unmanaged <1>
...
----
<1> `spec.storageClassState` field set to "Unmanaged"

. Click *Save*.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc
//

[id="persistent-storage-csi-sc-managing-cli_{context}"]
= Managing the default storage class using the CLI

.Prerequisites
* Access to the cluster with cluster-admin privileges.

.Procedure

To manage the storage class using the CLI, run the following command:

[source,terminal]
----
$ oc patch clustercsidriver $DRIVERNAME --type=merge -p "{\"spec\":{\"storageClassState\":\"${STATE}\"}}" <1>
----
<1> Where `${STATE}` is "Removed" or "Managed" or "Unmanaged".
+
Where `$DRIVERNAME` is the provisioner name. You can find the provisioner name by running the command `oc get sc`.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc
//
[id="persistent-storage-csi-sc-multiple-none_{context}"]
= Absent or multiple default storage classes

== Multiple default storage classes
Multiple default storage classes can occur if you mark a non-default storage class as default and do not unset the existing default storage class, or you create a default storage class when a default storage class is already present. With multiple default storage classes present, any persistent volume claim (PVC) requesting the default storage class (`pvc.spec.storageClassName`=nil) gets the most recently created default storage class, regardless of the default status of that storage class, and the administrator receives an alert in the alerts dashboard that there are multiple default storage classes, `MultipleDefaultStorageClasses`.

== Absent default storage class
There are two possible scenarios where PVCs can attempt to use a non-existent default storage class:

* An administrator removes the default storage class or marks it as non-default, and then a user creates a PVC requesting the default storage class.

* During installation, the installer creates a PVC requesting the default storage class, which has not yet been created.

In the preceding scenarios, PVCs remain in the pending state indefinitely. To resolve this situation, create a default storage class or declare one of the existing storage classes as the default. As soon as the default storage class is created or declared, the PVCs get the new default storage class. If possible, the PVCs eventually bind to statically or dynamically provisioned PVs as usual, and move out of the pending state.

// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc

[id="change-default-storage-class_{context}"]
= Changing the default storage class

[role="_abstract"]
Change the default storage class to ensure new persistent volume claims (PVCs) automatically use your preferred storage backend. This helps you optimize costs, align with infrastructure changes, or ensure consistent storage types across new deployments without requiring users to specify a storage class for each claim.

In this example, you have two defined storage classes, `gp3` and `standard`, and you want to change the default storage class from `gp3` to `standard`.

.Prerequisites

* Access to the cluster with cluster-admin privileges.

.Procedure

. List the storage classes by running the following command:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source,terminal]
----
NAME                 TYPE
gp3 (default)        ebs.csi.aws.com
standard             ebs.csi.aws.com
----
+
The text `(default)` indicates the default storage class. In this example `gp3` is the current default storage class.

. Make the required storage class the default.
+
For the required storage class, set the `storageclass.kubernetes.io/is-default-class` annotation to `true` by running the following command:
+
[source,terminal]
----
$ oc patch storageclass standard -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
----
+
[NOTE]
====
You can have many default storage classes for a short time. However, you must ensure that only one default storage class exists eventually.

With many default storage classes present, any persistent volume claim (PVC) requesting the default storage class (`pvc.spec.storageClassName`=nil) gets the most recently created default storage class, regardless of the default status of that storage class. The administrator receives an alert in the alerts dashboard that there are many default storage classes, `MultipleDefaultStorageClasses`.
====

. Remove the default storage class setting from the old default storage class.
+
For the old default storage class, change the value of the `storageclass.kubernetes.io/is-default-class` annotation to `false` by running the following command:
+
[source,terminal]
----
$ oc patch storageclass gp3 -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "false"}}}'
----

. Verify the changes by running the following command:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source,terminal]
----
NAME                 TYPE
gp3                  ebs.csi.aws.com
standard (default)   ebs.csi.aws.com
----
+
The `standard` storage class is now the default.
