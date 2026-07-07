---
title: "Troubleshooting data backup and restore"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-troubleshoot-backup-restore
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-troubleshoot-backup-restore
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Troubleshooting data backup and restore

[id="microshift-troubleshoot-backup-restore"]
= Troubleshooting data backup and restore

[role="_abstract"]
To troubleshoot failed data backups and restorations, check the basics first.

For example, verify the following common causes:

* User permissions
* System health and configuration
* Storage capacity

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-backup-restore.adoc

[id="microshift-backup-data-failed_{context}"]
= Data backup failure

[role="_abstract"]
Data backups are automatic on `rpm-ostree` systems. If you are not using an `rpm-ostree` system and attempted to create a manual backup, certain conditions can cause the backup to fail.

{microshift-short} was stopped too soon after the system started::
Wait until the system completes health checks and background processes before stopping {microshift-short}.

{microshift-short} stopped because of an error::
Verify that {microshift-short} is healthy and in a running state before you create a backup.

Insufficient storage space::
Verify that sufficient storage is available for {microshift-short} data before you create a backup.

Insufficient user permissions::
Verify that you have the correct user permissions and configurations required to create a backup.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-backup-restore.adoc

[id="microshift-checking-backup-logs_{context}"]
= Checking backup logs

[role="_abstract"]
Backup logs can help you identify the location and status of manual and automatic backups, and the processes that occurred during each backup.

* Manual backup logs are displayed in the terminal output.
* Automatic backup logs for `rpm-ostree` systems are available in the {microshift-short} journal logs.

.Procedure

* Check the journal logs:
+
[source,terminal]
----
$ sudo journalctl -u microshift
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-backup-restore.adoc

[id="microshift-restore-data-failed_{context}"]
= Data restoration failure

[role="_abstract"]
The restoration of data can fail for many reasons, including storage and permission issues. Mismatched data versions can cause failures when {microshift-short} restarts.

[id="microshift-image-based-systems-data-restore-failed_{context}"]
== Image-based systems data restore failed

Data restorations are automatic on `rpm-ostree` systems, but can fail, for example:

* The only backups that are restored on `rpm-ostree` systems are backups from the current deployment or a rollback deployment. Backups are not taken on an unhealthy system.

** Only the latest backups that have corresponding deployments are retained. Outdated backups that do not have a matching deployment are automatically removed.

** Data is usually not restored from a newer version of {microshift-short}.

** Ensure that the data you are restoring follows same versioning pattern as the update path. For example, if the destination version of {microshift-short} is an older version than the version of the {microshift-short} data you are currently using, the restoration can fail.

[id="microshift-rpm-manual-restore-data-failed_{context}"]
== RPM-based manual data restore failed

If you are using an RPM system that is not `rpm-ostree` and tried to restore a manual backup, the following reasons can cause the restoration to fail:

* If {microshift-short} stopped running because of an error, you cannot restore data.
** Make sure the system is healthy.
** Start it in a healthy state before attempting to restore data.

* If you do not have enough storage space allocated for the incoming data, the restoration fails.
** Make sure that your current system storage is configured to accept the restored data.

* You are attempting to restore data from a newer version of {microshift-short}.
** Ensure that the data you are restoring follows same versioning pattern as the update path. For example, if the destination version of {microshift-short} is an older version than the version of the {microshift-short} data you are attempting to use, the restoration can fail.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-backup-restore.adoc

[id="microshift-storage-migration-failed_{context}"]
= Storage migration failure

[role="_abstract"]
Storage migration failures typically result from incompatible changes to custom resources (CRs) between {microshift-short} versions. If a storage migration fails, the CR versions are likely incompatible and require manual review.
