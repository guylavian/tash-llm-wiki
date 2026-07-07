---
title: "Storage configuration overview"
type: reference
domain: openshift
slug: virt-4-22-virt-storage-config-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-storage-config-overview
version: 4.22
family: virt
documentKind: "Documentation"
---

# Storage configuration overview

[id="virt-storage-config-overview"]
= Storage configuration overview

[role="_abstract"]
You can configure a default storage class, storage profiles, Containerized Data Importer (CDI), data volumes (DVs), and automatic boot source updates.

On OpenShift Container Platform, specific configurations for Hyperdisk are required to ensure performance and support features like live migration. For more information, see "Storage configuration for {VirtProductName} 4.21.x on Google Cloud" in the "Additional resources" section.

[id="storage-configuration-tasks"]
== Storage

The following storage configuration tasks are mandatory:

Configure a default storage class::

You must configure a default storage class for the cluster. Otherwise, {VirtProductName} cannot automatically import boot source images. `DataVolume` objects (DVs) and `PersistentVolumeClaim` objects (PVCs) that do not explicitly specify a storage class remain in the `Pending` state until you set a default storage class.

Configure storage profiles::

You must configure storage profiles if your storage provider is not recognized by CDI. A storage profile provides recommended storage settings based on the associated storage class.

The following storage configuration tasks are optional:

Reserve additional PVC space for file system overhead::

By default, 5.5% of a file system PVC is reserved for overhead, reducing the space available for VM disks by that amount. You can configure a different overhead value.

Configure local storage by using the hostpath provisioner::

You can configure local storage for virtual machines by using the hostpath provisioner (HPP). When you install the {VirtProductName} Operator, the HPP Operator is automatically installed.

Configure user permissions to clone data volumes between namespaces::

You can configure RBAC roles to enable users to clone data volumes between namespaces.

[id="cdi-configuration-tasks"]
== Containerized Data Importer

You can perform the following Containerized Data Importer (CDI) configuration tasks:

Override the resource request limits of a namespace::

You can configure CDI to import, upload, and clone VM disks into namespaces that are subject to CPU and memory resource restrictions.

Configure CDI scratch space::

CDI requires scratch space (temporary storage) to complete some operations, such as importing and uploading VM images. During this process, CDI provisions a scratch space PVC equal to the size of the PVC backing the destination data volume (DV).

[id="dv-configuration-tasks"]
== Data volumes

You can perform the following data volume configuration tasks:

Enable preallocation for data volumes::

CDI can preallocate disk space to improve write performance when creating data volumes. You can enable preallocation for specific data volumes.

Manage data volume annotations::

Data volume annotations allow you to manage pod behavior. You can add one or more annotations to a data volume, which then propagates to the created importer pods.

[id="boot-source-configuration"]
== Boot source updates

You can perform the following boot source update configuration task:

Manage automatic boot source updates::

Boot sources can make virtual machine (VM) creation more accessible and efficient for users. If automatic boot source updates are enabled, CDI imports, polls, and updates the images so that they are ready to be cloned for new VMs. By default, CDI automatically updates Red Hat boot sources. You can enable automatic updates for custom boot sources.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Defining a storage class
* Configure storage profiles
* Reserve additional PVC space for file system overhead
* Configure local storage by using the hostpath provisioner
* Configure user permissions to clone data volumes between namespaces
* Override the resource request limits of a namespace
* Configure CDI scratch space
* Enable preallocation for data volumes
* Manage data volume annotations
* Manage automatic boot source updates
* Storage configuration for {VirtProductName} 4.22.x on Google Cloud
