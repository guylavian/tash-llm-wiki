---
title: "About the {oadp-short} Data Mover"
type: reference
domain: openshift
slug: backup-and-restore-4-22-about-oadp-data-mover
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/about-oadp-data-mover
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# About the {oadp-short} Data Mover

[id="about-oadp-data-mover"]
= About the {oadp-short} Data Mover

[role="_abstract"]
Use the {oadp-first} built-in Data Mover to move Container Storage Interface (CSI) volume snapshots to remote object storage and restore stateful applications after cluster failures. This provides disaster recovery capabilities for both containerized and virtual machine workloads.

The Data Mover uses Kopia as the uploader mechanism to read the snapshot data and write to the unified repository.

{oadp-short} supports CSI snapshots on the following:

* {odf-full}
* Any other cloud storage provider with the Container Storage Interface (CSI) driver that supports the Kubernetes Volume Snapshot API

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/installing/about-oadp-data-mover.adoc

[id="oadp-data-mover-support_{context}"]
= Data Mover support

[role="_abstract"]
Review Data Mover support and compatibility across {oadp-short} versions to understand which backups can be restored. This helps you plan version upgrades and backup strategies.

The {oadp-short} built-in Data Mover, which was introduced in {oadp-short} 1.3 as a Technology Preview, is now fully supported for both containerized and virtual machine workloads.

Supported::

The Data Mover backups taken with {oadp-short} 1.3 can be restored using {oadp-short} 1.3 and later.

Not supported::

Backups taken with {oadp-short} 1.1 or {oadp-short} 1.2 using the Data Mover feature cannot be restored using {oadp-short} 1.3 and later.

{oadp-short} 1.1 and {oadp-short} 1.2 are no longer supported. The DataMover feature in {oadp-short} 1.1 or {oadp-short} 1.2 was a Technology Preview and was never supported. DataMover backups taken with {oadp-short} 1.1 or {oadp-short} 1.2 cannot be restored on later versions of {oadp-short}.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/installing/about-oadp-data-mover.adoc

[id="enabling-oadp-data-mover_{context}"]
= Enabling the built-in Data Mover

[role="_abstract"]
Enable the built-in Data Mover by configuring the CSI plugin and node agent in the `DataProtectionApplication` custom resource (CR). This provides volume-level backup and restore operations by using the Kopia uploader.

.Procedure

* Include the CSI plugin and enable the node agent in the `DataProtectionApplication` custom resource (CR) as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-sample
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
      - openshift
      - aws
      - csi
      defaultSnapshotMoveData: true
      defaultVolumesToFSBackup:
      featureFlags:
      - EnableCSI
# ...
----
+
where:

`enable`:: Specifies the flag to enable the node agent.
`uploaderType`:: Specifies the type of uploader. The possible values are `restic` or `kopia`. The built-in Data Mover uses Kopia as the default uploader mechanism regardless of the value of the `uploaderType` field.
`csi`:: Specifies the CSI plugin included in the list of default plugins.
`defaultVolumesToFSBackup`:: Specifies the default behavior for volumes. In {oadp-short} 1.3.1 and later, set to `true` if you use Data Mover only for volumes that opt out of `fs-backup`. Set to `false` if you use Data Mover by default for volumes.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/installing/about-oadp-data-mover.adoc

[id="built-in-data-mover-crds_{context}"]
= Built-in Data Mover controller and custom resource definitions (CRDs)

[role="_abstract"]
Review the custom resource definitions (CRDs) that the built-in Data Mover uses to manage volume snapshot backup and restore operations. This helps you understand how Data Mover handles data upload, download, and repository management.

The built-in Data Mover feature introduces three new API objects defined as CRDs for managing backup and restore:

* `DataDownload`: Represents a data download of a volume snapshot. The CSI plugin creates one `DataDownload` object per volume to be restored. The `DataDownload` CR includes information about the target volume, the specified Data Mover, the progress of the current data download, the specified backup repository, and the result of the current data download after the process is complete.

* `DataUpload`: Represents a data upload of a volume snapshot. The CSI plugin creates one `DataUpload` object per CSI snapshot. The `DataUpload` CR includes information about the specified snapshot, the specified Data Mover, the specified backup repository, the progress of the current data upload, and the result of the current data upload after the process is complete.

* `BackupRepository`: Represents and manages the lifecycle of the backup repositories. {oadp-short} creates a backup repository per namespace when the first CSI snapshot backup or restore for a namespace is requested.

// Module included in the following assemblies:
// backup_and_restore/application_backup_and_restore/installing/about-oadp-1-3-data-mover.adoc
// backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.adoc

[id="oadp-about-incremental-backup-support_{context}"]
= About incremental backup support

[role="_abstract"]
{oadp-short} supports incremental backups of `block` and `Filesystem` persistent volumes for both containerized, and {VirtProductName} workloads. The following table summarizes the support for File System Backup (FSB), Container Storage Interface (CSI), and CSI Data Mover:

[cols="5", options="header"]
.{oadp-short} backup support matrix for containerized workloads
|===
| Volume mode |FSB - Restic  |FSB - Kopia | CSI | CSI Data Mover
| Filesystem | Backup supported, Incremental backup supported | Backup supported, Incremental backup supported | Backup supported | Backup supported, Incremental backup supported
| Block | Not supported | Not supported | Backup supported | Backup supported, Incremental backup supported
|===

[cols="5", options="header"]
.{oadp-short} backup support matrix for {VirtProductName} workloads
|===
| Volume mode |FSB - Restic  |FSB - Kopia | CSI | CSI Data Mover
| Filesystem | Not supported | Not supported | Backup supported | Backup supported, Incremental backup supported
| Block | Not supported | Not supported | Backup supported | Backup supported, Incremental backup supported
|===

[NOTE]
====
The CSI Data Mover backups use Kopia regardless of `uploaderType`.
====

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About Kopia
