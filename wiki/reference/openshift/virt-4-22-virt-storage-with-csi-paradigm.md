---
title: "Understanding virtual machine storage with the CSI paradigm"
type: reference
domain: openshift
slug: virt-4-22-virt-storage-with-csi-paradigm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-storage-with-csi-paradigm
version: 4.22
family: virt
documentKind: "Documentation"
---

# Understanding virtual machine storage with the CSI paradigm

[id="virt-storage-with-csi-paradigm"]
= Understanding virtual machine storage with the CSI paradigm

[role="_abstract"]
Virtual machines (VMs) in {VirtProductName} use PersistentVolume (PV) and PersistentVolumeClaim (PVC) paradigms to manage storage. This ensures seamless integration with the Container Storage Interface (CSI).

// Module included in the following assemblies:
//
// * virt/storage/virt-storage-with-csi-paradigm.adoc

[id="virt-storage-vp-csi-overview_{context}"]
= Virtual machine CSI storage overview

[role="_abstract"]
{VirtProductName} integrates with the Container Storage Interface (CSI) to manage virtual machine (VM) storage.

Storage classes define storage capabilities such as performance tiers and types. PersistentVolumeClaims (PVCs) request storage resources, which bind to PersistentVolumes (PVs). CSI drivers connect Kubernetes to vendor storage backends, including iSCSI, NFS, and Fibre Channel.

[IMPORTANT]
====
A VM can start even if its PVC is already mounted by another pod. This behavior follows Kubernetes PVC access semantics and can lead to data corruption if multiple writers access the same volume.
====

image:virt-storage-csi-paradigm.png[title="Virtual machine disks and the CSI paradigm"]
