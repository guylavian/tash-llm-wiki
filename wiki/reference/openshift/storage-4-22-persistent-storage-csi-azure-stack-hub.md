---
title: "Azure Stack Hub CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-azure-stack-hub
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-azure-stack-hub
version: 4.22
family: storage
documentKind: "Documentation"
---

# Azure Stack Hub CSI Driver Operator

[id="persistent-storage-csi-azure-stack-hub"]
= Azure Stack Hub CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Azure Stack Hub Storage. Azure Stack Hub, which is part of the Azure Stack portfolio, allows you to run apps in an on-premise environment and deliver Azure services in your datacenter.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to Azure Stack Hub storage assets, OpenShift Container Platform installs the Azure Stack Hub CSI Driver Operator and the Azure Stack Hub CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _Azure Stack Hub CSI Driver Operator_ provides a storage class (`managed-csi`), with "Standard_LRS" as the default storage account type, that you can use to create persistent volume claims (PVCs). The Azure Stack Hub CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage.

* The _Azure Stack Hub CSI driver_ enables you to create and mount Azure Stack Hub PVs.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

[role="_additional-resources"]
== Additional resources
* Configuring CSI volumes
