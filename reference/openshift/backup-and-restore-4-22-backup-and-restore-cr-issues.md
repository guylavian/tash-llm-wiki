---
title: "Backup and Restore CR issues"
type: reference
domain: openshift
slug: backup-and-restore-4-22-backup-and-restore-cr-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/backup-and-restore-cr-issues
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backup and Restore CR issues

[id="backup-and-restore-cr-issues"]
= Backup and Restore CR issues

[role="_abstract"]
Resolve common issues with `Backup` and `Restore` custom resources (CRs), such as volume retrieval failures, and backups remaining in progress or partially failed states. This helps you ensure successful backup and restore operations in {oadp-short}.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/backup-and-restore-cr-issues.adoc
//

[id="troubleshooting-backup-cr-cannot-retrieve-volume-issue_{context}"]
= Troubleshooting issue where backup CR cannot retrieve volume

[role="_abstract"]
Resolve the `InvalidVolume.NotFound` error that occurs when the persistent volume (PV) and snapshot locations are in different regions. This helps you ensure the `Backup` CR can successfully retrieve volumes.

If the PV and the snapshot locations are in different regions, the `Backup` custom resource (CR) displays the following error message:

[source,text]
----
InvalidVolume.NotFound: The volume vol-xxxx does not exist.
----

.Procedure

. Edit the value of the `spec.snapshotLocations.velero.config.region` key in the `DataProtectionApplication` manifest so that the snapshot location is in the same region as the PV.

. Create a new `Backup` CR.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/backup-and-restore-cr-issues.adoc
//

[id="troubleshooting-backup-cr-status-remains-in-progress-issue_{context}"]
= Troubleshooting issue where backup CR status remains in progress

[role="_abstract"]
Resolve the issue where an interrupted backup causes the `Backup` CR status to remain in the `InProgress` phase. This helps you clear stalled backups and create new ones to complete your backup operations.

.Procedure

. Retrieve the details of the `Backup` CR by running the following command:
+
[source,terminal]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  backup describe <backup>
----

. Delete the `Backup` CR by running the following command:
+
[source,terminal]
----
$ oc delete backups.velero.io <backup> -n openshift-adp
----
+
You do not need to clean up the backup location because an in progress `Backup` CR has not uploaded files to object storage.

. Create a new `Backup` CR.

. View the Velero backup details by running the following command:
+
[source,terminal, subs="+quotes"]
----
$ velero backup describe <backup_name> --details
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/backup-and-restore-cr-issues.adoc
//

[id="troubleshooting-backup-cr-status-remains-in-partiallyfailed-issue_{context}"]
= Troubleshooting issue where backup CR status remains partially failed

[role="_abstract"]
Resolve the `PartiallyFailed` status that occurs when a `Backup` CR cannot create a CSI snapshot due to a missing label on the `VolumeSnapshotClass`. This helps you ensure successful backups by properly labeling the snapshot class.

If the backup created based on the CSI snapshot class is missing a label, the CSI snapshot plugin fails to create a snapshot. As a result, the `Velero` pod logs an error similar to the following message:

[source,text]
----
time="2023-02-17T16:33:13Z" level=error msg="Error backing up item" backup=openshift-adp/user1-backup-check5 error="error executing custom action (groupResource=persistentvolumeclaims, namespace=busy1, name=pvc1-user1): rpc error: code = Unknown desc = failed to get volumesnapshotclass for storageclass ocs-storagecluster-ceph-rbd: failed to get volumesnapshotclass for provisioner openshift-storage.rbd.csi.ceph.com, ensure that the desired volumesnapshot class has the velero.io/csi-volumesnapshot-class label" logSource="/remote-source/velero/app/pkg/backup/backup.go:417" name=busybox-79799557b5-vprq
----

.Procedure

. Delete the `Backup` CR by running the following command::
+
[source,terminal]
----
$ oc delete backups.velero.io <backup> -n openshift-adp
----

. If required, clean up the stored data on the `BackupStorageLocation` resource  to free up space.

. Apply the `velero.io/csi-volumesnapshot-class=true` label to the `VolumeSnapshotClass` object by running the following command:
+
[source,terminal]
----
$ oc label volumesnapshotclass/<snapclass_name> velero.io/csi-volumesnapshot-class=true
----

. Create a new `Backup` CR.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/backup-and-restore-cr-issues.adoc

[id="oadp-troubleshooting-pvc-binding-delay_{context}"]
= Troubleshooting PVC binding failures with the waitForFirstConsumer storage class

[role="_abstract"]
To ensure that restored persistent volume claims (PVCs) successfully bind to PVs when node affinity is configured, adjust the storage class binding mode settings during restore operations.

PVCs that use a storage class with `bindingMode: WaitForFirstConsumer` might fail to bind to a PV when node affinity is configured. This issue can occur during restore operations, including virtual machine file restore (VMFR) workflows.

.Procedure

* Set the `ignoreDelayBinding` field to `true` in the `restorePVC` section of the `nodeAgent` configuration in the `DataProtectionApplication` CR, as shown in the following example:
+
[source,yaml,subs="+quotes"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-test
  namespace: openshift-adp
spec:
# ...
  configuration:
    nodeAgent:
      enable: true
      restorePVC:
        ignoreDelayBinding: true
      uploaderType: kopia
----
