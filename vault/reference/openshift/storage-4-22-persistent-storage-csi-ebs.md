---
title: "AWS Elastic Block Store CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-ebs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-ebs
version: 4.22
family: storage
documentKind: "Documentation"
---

# AWS Elastic Block Store CSI Driver Operator

[id="persistent-storage-csi-ebs"]
= AWS Elastic Block Store CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the AWS EBS CSI driver.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a Container Storage Interface (CSI) Operator and driver.

To create CSI-provisioned PVs that mount to AWS EBS storage assets, OpenShift Container Platform installs the AWS EBS CSI Driver Operator (a Red Hat operator) and the AWS EBS CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _AWS EBS CSI Driver Operator_ provides a StorageClass by default that you can use to create PVCs. You can disable this default storage class if desired (see Managing the default storage class). You also have the option to create the AWS EBS StorageClass as described in Persistent storage using Amazon Elastic Block Store.

* The _AWS EBS CSI driver_ enables you to create and mount AWS EBS PVs.

[NOTE]
====
If you installed the AWS EBS CSI Operator and driver on an OpenShift Container Platform 4.5 cluster, you must uninstall the 4.5 Operator and driver before you update to OpenShift Container Platform .
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
OpenShift Container Platform defaults to using the CSI plugin to provision Amazon Elastic Block Store (Amazon EBS) storage.
====

For information about dynamically provisioning AWS EBS persistent volumes in OpenShift Container Platform, see Persistent storage using Amazon Elastic Block Store.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-azure.adoc
// storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="byok_{context}"]
= User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes. You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

* Amazon Web Services (AWS) Elastic Block storage (EBS)

* Microsoft Azure Disk storage

* Google Cloud Platform (GCP) persistent disk (PD) storage

* IBM Virtual Private Cloud (VPC) Block storage

[NOTE]
====
If there is no encrypted key defined in the storage class, only set `encrypted: "true"` in the storage class. The AWS EBS CSI driver uses the AWS managed alias/aws/ebs, which is created by Amazon EBS automatically in each region by default to encrypt provisioned storage volumes. In addition, the managed storage classes all have the `encrypted: "true"` setting.
====

For information about installing with user-managed encryption for Amazon EBS, see Installation configuration parameters.

== Support for European Sovereign Cloud (EUSC) region
European Sovereign Cloud (EUSC) region acts as a "digital fortress" built within a specific country's borders. Sovereign Clouds are specifically designed to meet strict legal, jurisdictional, and security requirements of a particular nation or entity.

In the context of storage, EUSC ensures that all data, including primary storage, backups, and the resulting metadata, resides physically within the specific nation's borders and remains exclusively under its legal jurisdiction.

For OpenShift Container Platform 4.22, and later, only AWS Elastic Block Storage supports EUSC. AWS Elastic File Storage (EFS) is not supported.

For information about installing an OpenShift Container Platform cluster into the {aws-short} EUSC, see Section _{aws-short} EUSC region_ under _Installing_.

[role="_additional-resources"]
.Additional resources
* Persistent storage using Amazon Elastic Block Store
* Configuring CSI volumes
