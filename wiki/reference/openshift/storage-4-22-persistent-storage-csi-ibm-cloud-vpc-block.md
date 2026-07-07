---
title: "{ibm-cloud-title} VPC Block CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-ibm-cloud-vpc-block
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-ibm-cloud-vpc-block
version: 4.22
family: storage
documentKind: "Documentation"
---

# {ibm-cloud-title} VPC Block CSI Driver Operator

[id="persistent-storage-csi-ibm-cloud-vpc-block"]
= {ibm-cloud-title} VPC Block CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for {ibm-name} Virtual Private Cloud (VPC) Block Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to {ibm-cloud-name} VPC Block storage assets, OpenShift Container Platform installs the {ibm-cloud-name} VPC Block CSI Driver Operator and the {ibm-cloud-name} VPC Block CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _{ibm-cloud-name} VPC Block CSI Driver Operator_ provides three storage classes named `ibmc-vpc-block-10iops-tier` (default), `ibmc-vpc-block-5iops-tier`, and `ibmc-vpc-block-custom` for different tiers that you can use to create persistent volume claims (PVCs). The {ibm-cloud-name} VPC Block CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see Managing the default storage class).

* The _{ibm-cloud-name} VPC Block CSI driver_ enables you to create and mount {ibm-cloud-name} VPC Block PVs.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

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

For information about installing with user-managed encryption for {ibm-cloud-title}, see User-managed encryption for {ibm-cloud-title} and Preparing to install on {ibm-cloud-title}.

[role="_additional-resources"]
.Additional resources
* Configuring CSI volumes
