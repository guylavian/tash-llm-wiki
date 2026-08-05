---
title: "Persistent storage using GCE Persistent Disk"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-gce
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-gce
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using GCE Persistent Disk

[id="persistent-storage-using-gce"]
= Persistent storage using GCE Persistent Disk

OpenShift Container Platform supports GCE Persistent Disk volumes (gcePD).
You can provision your OpenShift Container Platform cluster with persistent storage
using GCE.
Some familiarity with Kubernetes and GCE is assumed.

The Kubernetes persistent volume framework allows administrators to
provision a cluster with persistent storage and gives users a way to
request those resources without having any knowledge of the underlying
infrastructure.

GCE Persistent Disk volumes can be provisioned dynamically.

Persistent volumes are not bound to a single project or namespace;
they can be shared across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace and can be
requested by users.

[IMPORTANT]
====
OpenShift Container Platform 4.12 and later provides automatic migration for the GCE Persist Disk in-tree volume plugin to its equivalent CSI driver.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes.

For more information about migration, see CSI automatic migration.
====

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying
storage provider.
====

[role="_additional-resources"]
.Additional resources

* GCE Persistent Disk

// Defining attributes required by the next module

// Be sure to set the :StorageClass: and :Provisioner: value in each assembly
// on the line before the include statement for this module. For example, to
// set the StorageClass value to "AWS EBS", add the following line to the
// assembly:
// :StorageClass: AWS EBS
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="storage-create-storage-class_{context}"]
= Creating the {StorageClass} storage class

Storage classes are used to differentiate and delineate storage levels and
usages. By defining a storage class, users can obtain dynamically provisioned
persistent volumes.

The _AWS EFS CSI Driver Operator (a Red Hat operator)_, after being installed, does not create a storage class by default. However, you can manually create the AWS EFS storage class.

// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="creating-volume-claim_{context}"]
= Creating the persistent volume claim

.Prerequisites

Storage must exist in the underlying infrastructure before it can be mounted as
a volume in OpenShift Container Platform.

.Procedure

. In the OpenShift Container Platform web console, click *Storage* -> *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume Claim*.

. Define the desired options on the page that appears.

.. Select the previously-created storage class from the drop-down menu.

.. Enter a unique name for the storage claim.

.. Select the access mode. This selection determines the read and write access for the storage claim.

.. Define the size of the storage claim.

. Click *Create* to create the persistent volume claim and generate a persistent
volume.

// Be sure to set the :provider: value in each assembly
// on the line before the include statement for this module.
// For example:
// :provider: AWS
//
// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc
// * storage/persistent_storage-gce.adoc

[id="volume-format-{provider}_{context}"]
= Volume format

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks that the volume contains a file system as specified by the `fsType` arameter in the persistent volume definition. If the device is not formatted with the file system, all data from the device is erased and the device is automatically formatted with the given file system.

This verification enables you to use unformatted {provider} volumes as persistent volumes, because OpenShift Container Platform formats them before the first use.

// Undefined {provider} attribute, so that any mistakes are easily spotted
