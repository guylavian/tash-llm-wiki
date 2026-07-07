---
title: "Securing attached storage"
type: reference
domain: openshift
slug: security-4-22-security-storage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/security-storage
version: 4.22
family: security
documentKind: "Documentation"
---

# Securing attached storage

[id="security-storage"]
= Securing attached storage

OpenShift Container Platform supports multiple types of storage, both
for on-premise and cloud providers. In particular,
OpenShift Container Platform can use storage types that support the Container
Storage Interface.

// Persistent volume plugins
// Module included in the following assemblies:
//
// * security/container_security/security-storage.adoc

[id="security-network-storage-persistent_{context}"]
=  Persistent volume plugins

Containers are useful for both stateless and stateful applications.
Protecting attached storage is a key element of securing stateful services.
Using the Container Storage Interface (CSI), OpenShift Container Platform can
incorporate storage from any storage back end that supports the CSI interface.

OpenShift Container Platform provides plugins for multiple types of storage, including:

* {rh-storage-first} *
* AWS Elastic Block Stores (EBS) *
* AWS Elastic File System (EFS) *
* Azure Disk *
* Azure File *
* OpenStack Cinder *
* GCE Persistent Disks *
* VMware vSphere *
* Network File System (NFS)
* FlexVolume
* Fibre Channel
* iSCSI

Plugins for those storage types with dynamic provisioning are marked with
an asterisk (*). Data in transit is encrypted via HTTPS for all
OpenShift Container Platform components communicating with each other.

You can mount a persistent volume (PV) on a host in any way supported by your
storage type. Different types of storage have different capabilities and each
PV's access modes are set to the specific modes supported by that particular
volume.

For example, NFS can support multiple read/write clients, but a specific NFS PV
might be exported on the server as read-only. Each PV has its own set of access
modes describing that specific PV's capabilities, such as `ReadWriteOnce`,
`ReadOnlyMany`, and `ReadWriteMany`.

// Shared storage
// Module included in the following assemblies:
//
// * security/container_security/security-storage.adoc

[id="security-network-storage-shared_{context}"]
= Shared storage

For shared storage providers like NFS, the PV registers its
group ID (GID) as an annotation on the PV resource. Then, when the PV is claimed by the pod, the annotated GID is added to the supplemental groups of the pod, giving that pod access to the contents of the shared storage.

// Block storage
// Module included in the following assemblies:
//
// * security/container_security/security-storage.adoc

[id="security-network-storage-block_{context}"]
= Block storage

For block storage providers like AWS Elastic Block Store (EBS), GCE Persistent Disks, and iSCSI, OpenShift Container Platform uses SELinux capabilities to secure the root of the mounted volume for non-privileged pods, making the mounted volume owned by and only visible to the container with which it is associated.

[role="_additional-resources"]
.Additional resources
* Understanding persistent storage
* Configuring CSI volumes
* Dynamic provisioning
* Persistent storage using NFS
* Persistent storage using AWS Elastic Block Store
* Persistent storage using GCE Persistent Disk
