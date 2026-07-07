---
title: "Storage overview"
type: reference
domain: openshift
slug: microshift-storage-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_storage/index
version: 4.22
family: microshift_storage
documentKind: "Documentation"
---

# Storage overview

[id="storage-overview-microshift"]
= Storage overview

[role="_abstract"]
{microshift-short} supports dynamic, ephemeral, and persistent storage, both for on-premise and cloud providers. You can manage container storage for persistent and non-persistent data in a {microshift-short} node.

//microshift dynamic storage with the LVMS plugin
// Module included in the following assemblies:
//
// * microshift-storage/index.adoc

[id="microshift-dynamic-storage-LVMS-plugin_{context}"]
= Dynamic storage with the LVMS plugin

[role="_abstract"]
Using dynamic provisioning allows you to create storage volumes on-demand, eliminating the need for pre-provisioned storage. {microshift-short} enables dynamic storage provisioning that is ready for immediate use with the logical volume manager storage (LVMS) Container Storage Interface (CSI) provider.

//microshift ephemeral storage
// Module included in the following assemblies:
//
// * microshift-storage/index.adoc

[id="microshift-ephemeral-storage_{context}"]
= Ephemeral storage

[role="_abstract"]
Pods and containers are ephemeral or transient in nature and designed for stateless applications. Ephemeral storage allows administrators and developers to better manage the local storage for some of their operations.

//microshift persistent storage
// Module included in the following assemblies:
//
// * microshift-storage/index.adoc

[id="microshift-persistent-storage_{context}"]
= Persistent storage

[role="_abstract"]
Persistent storage in {microshift-short} enables stateful applications to retain data beyond the lifecycle of individual pods. You can use persistent volumes (PVs) to provision storage and persistent volume claims (PVCs) to request storage for your applications.

//microshift dynamic provisioning overview
// Module included in the following assemblies:
//
// * microshift-storage/index.adoc

[id="microshift-dynamic-provisioning-overview_{context}"]
= Dynamic storage provisioning

[role="_abstract"]
Using dynamic provisioning allows you to create storage volumes on-demand, eliminating the need for pre-provisioned storage.
