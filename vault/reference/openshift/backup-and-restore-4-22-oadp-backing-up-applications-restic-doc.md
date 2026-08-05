---
title: "Backing up applications with File System Backup: Kopia or Restic"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-backing-up-applications-restic-doc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-backing-up-applications-restic-doc
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up applications with File System Backup: Kopia or Restic

[id="oadp-backing-up-applications-restic-doc"]
= Backing up applications with File System Backup: Kopia or Restic

[role="_abstract"]
Use {oadp-short} File System Backup (FSB) with Kopia or Restic to back up and restore Kubernetes volumes attached to pods when snapshots are not available. This helps you to protect application data on NFS or other non-snapshot storage.

If your cloud provider does not support snapshots or if your applications are on NFS data volumes, you can create backups by using FSB.

FSB integration with OADP provides a solution for backing up and restoring almost any type of Kubernetes volumes. This integration is an additional capability of OADP and is not a replacement for existing functionality.

You back up Kubernetes resources, internal images, and persistent volumes with Kopia or Restic by editing the `Backup` custom resource (CR).

You do not need to specify a snapshot location in the `DataProtectionApplication` CR.

[NOTE]
====
In OADP version 1.3 and later, you can use either Kopia or Restic for backing up applications.

For the Built-in DataMover, you must use Kopia.

In OADP version 1.2 and earlier, you can only use Restic for backing up applications.
====

[IMPORTANT]
====
FSB does not support backing up `hostPath` volumes. For more information, see _FSB limitations_.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/backing_up_and_restoring/oadp-backing-up-applications-restic-doc.adoc

[id="oadp-backingup-file-system-backup_{context}"]
= Backing up applications with File System Backup

[role="_abstract"]
Create a `Backup` custom resource (CR) to back up applications by using File System Backup (FSB) with Kopia as the uploader. This helps you to protect Kubernetes volumes attached to pods when snapshots are not available or when using NFS data volumes.

.Prerequisites

* You must install the OpenShift API for Data Protection (OADP) Operator.
* You must not disable the default `nodeAgent` installation by setting `spec.configuration.nodeAgent.enable` to `false` in the `DataProtectionApplication` CR.
* You must select Kopia or Restic as the uploader by setting `spec.configuration.nodeAgent.uploaderType` to `kopia` or `restic` in the `DataProtectionApplication` CR.
* The `DataProtectionApplication` CR must be in a `Ready` state.

.Procedure

* Create the `Backup` CR, as in the following example:
+
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup>
  labels:
    velero.io/storage-location: default
  namespace: openshift-adp
spec:
  defaultVolumesToFsBackup: true
...
----
+
where:
+
`defaultVolumesToFsBackup: true`:: Specifies the FSB setting within the `spec` block for OADP version 1.2 and later. In OADP version 1.1, add `defaultVolumesToRestic: true` instead.

[role="_additional-resources"]
.Additional resources

* FSB limitations
