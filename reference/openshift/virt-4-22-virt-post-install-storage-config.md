---
title: "Postinstallation storage configuration"
type: reference
domain: openshift
slug: virt-4-22-virt-post-install-storage-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-post-install-storage-config
version: 4.22
family: virt
documentKind: "Documentation"
---

# Postinstallation storage configuration

[id="virt-post-install-storage-config"]
= Postinstallation storage configuration

[role="_abstract"]
After you install {VirtProductName}, you must configure a default storage class. If your storage provider is not recognized by the Containerized Data Importer (CDI), you must also configure storage profiles.
Configuring a storage class allows your cluster to receive automated boot source updates. Storage profiles provide recommended storage settings based on the associated storage class.
If your storage provider is not recognized by the Containerized Data Importer (CDI), you must configure storage profiles after you install {VirtProductName}. Storage profiles provide recommended storage settings based on the associated storage class.

Optional: You can configure local storage by using the hostpath provisioner (HPP).

See the "Storage configuration overview" documentation for more options, including configuring the CDI, data volumes, and automatic boot source updates.

[id="configuring-local-storage-hpp"]
== Configuring local storage by using the HPP

When you install the {VirtProductName} Operator, the Hostpath Provisioner (HPP) Operator is automatically installed. The HPP Operator creates the HPP provisioner.

The HPP is a local storage provisioner designed for {VirtProductName}. To use the HPP, you must create an HPP custom resource (CR).

[IMPORTANT]
====
HPP storage pools must not be in the same partition as the operating system. Otherwise, the storage pools might fill the operating system partition. If the operating system partition is full, this might negatively impact performance, or the node can become unstable or unusable.
====

// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-local-storage-with-hpp.adoc
// * virt/post_installation_configuration/virt-post-install-storage-config.adoc

[id="virt-creating-storage-class-csi-driver_{context}"]
= Creating a storage class for the CSI driver with the storagePools stanza

[role="_abstract"]
To use the hostpath provisioner (HPP) you must create an associated storage class for the Container Storage Interface (CSI) driver.

When you create a storage class, you set parameters that affect the dynamic provisioning of persistent volumes (PVs) that belong to that storage class. You cannot update a `StorageClass` object's parameters after you create it.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a `storageclass_csi.yaml` file to define the storage class:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: hostpath-csi
provisioner: kubevirt.io.hostpath-provisioner
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
parameters:
  storagePool: my-storage-pool
----
+
* `reclaimPolicy` defines whether the underlying storage is deleted or retained when a user deletes a PVC. The two possible `reclaimPolicy` values are `Delete` and `Retain`. If you do not specify a value, the default value is `Delete`.
* `volumeBindingMode` defines the timing of PV creation. In this example, the `WaitForFirstConsumer` configuration delays PV creation until the scheduler assigns a pod to a specific node.
+
[NOTE]
====
Virtual machines use data volumes based on local PVs, which reside on specific nodes. When the system prepares a disk image for the virtual machine, the scheduler might not place the virtual machine on the node where it pinned the local storage PV.
+
To solve this problem, use the Kubernetes pod scheduler to bind the persistent volume claim (PVC) to a PV on the correct node. Setting the `volumeBindingMode` parameter of the `StorageClass` to `WaitForFirstConsumer` delays PV binding and provisioning until you create a pod that uses the PVC.
====
+
* `parameters.storagePool` defines the name of the storage pool defined in the HPP custom resource (CR).

. Save the file and exit.

. Create the `StorageClass` object by running the following command:
+
[source,terminal]
----
$ oc create -f storageclass_csi.yaml
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Defining a storage class
* Configuring storage profiles
* Storage configuration overview
