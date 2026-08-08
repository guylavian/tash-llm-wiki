---
title: "Backing up and restoring {microshift-short} data"
type: reference
domain: openshift
slug: microshift-backup-and-restore-4-22-microshift-backup-and-restore
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_backup_and_restore/microshift-backup-and-restore
version: 4.22
family: microshift_backup_and_restore
documentKind: "Documentation"
---

# Backing up and restoring {microshift-short} data

[id="microshift-backup-and-restore"]
= Backing up and restoring {microshift-short} data

[role="_abstract"]
To back up and restore {microshift-short} data manually, you can use the backup and restore procedures for the database on all supported systems. For application data, you must define your own backup and restore steps.

//Module included in the following assemblies:
//
// * microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-about-data-backups_{context}"]
= About backing up and restoring {microshift-short} data

[role="_abstract"]
Backing up and restoring {microshift-short} data applies to the database only, and not to any application data. Before you can create a manual backup, greenboot health checks must finish running and you must stop the {microshift-short} service.

* On `rpm-ostree` systems, {microshift-short} automatically creates a backup on every start. These automatic backups are deleted and replaced with the latest backup each time the system restarts.
* Data is also automatically restored on an `rpm-ostree` system after a greenboot system rollback. This data restoration ensures that the database matches the software running on the host after the rollback is completed.
* On other system types, you must back up and restore data manually.

Automated backups are in the `/var/lib/microshift-backups` directory by default. You can use this directory for manually backing up and restoring data by specifying it in each command. When you restore a backup, you must use the entire file path.

[NOTE]
====
The following procedures only backup and restore {microshift-short} data. Application data is not included.
====

// Module included in the following assemblies:
//
// * microshift/microshift-install-rpm.adoc
// * microshift/microshift-update-rpms-ostree.adoc
// * microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="stopping-microshift-service_{context}"]
= Stopping the {microshift-short} service

[role="_abstract"]
When you want to stop the {microshift-short} service, you must stop both the service and any deployed workloads.

.Prerequisites

* The {microshift-short} service is running.

.Procedure

. Enter the following command to stop the {microshift-short} service:
+
[source,terminal]
----
$ sudo systemctl stop microshift
----

. Workloads deployed on {microshift-short} might continue running even after the {microshift-short} service has been stopped. Enter the following command to display running workloads:
+
[source,terminal]
----
$ sudo crictl ps -a
----

. Enter the following commands to stop the deployed workloads:
+
[source,terminal]
----
$ sudo systemctl stop kubepods.slice
----

//Module included in the following assemblies:
//
// * microshift_updating/microshift-update-options.adoc
// * microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-backing-up-manually_{context}"]
= Backing up {microshift-short} data manually

[role="_abstract"]
To back up OpenShift Container Platform data manually, you can run `microshift backup` with a full path to the backup location. Stop the service first and use the entire path for the output file or directory.

You can back up {microshift-short} data manually at any time. Back up your data before system updates to preserve it for use if an update fails or for other system trouble. You can use the `/var/lib/microshift-backups` for manually backing up and restoring data by specifying it in each command.

.Prerequisites

* You have root access to the host.
* {microshift-short} is stopped.

.Procedure

. Manually create a backup by using the parent directory and specifying a name, such as `/var/lib/microshift-backups/_<manual_backup>_`, by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift backup /var/lib/microshift-backups/_<manual_backup>_
----
+
** For `_<manual_backup>_`, specify the backup name that you want to use.
+
.Example output
[source,terminal]
----
??? I1017 07:38:16.770506    5900 data_manager.go:92] "Copying data to backup directory" storage="/var/lib/microshift-backups" name="test" data="/var/lib/microshift"
??? I1017 07:38:16.770713    5900 data_manager.go:227] "Starting copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift /var/lib/microshift-backups/test"
??? I1017 07:38:16.776162    5900 data_manager.go:241] "Finished copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift /var/lib/microshift-backups/test"
??? I1017 07:38:16.776256    5900 data_manager.go:125] "Copied data to backup directory" backup="/var/lib/microshift-backups/test" data="/var/lib/microshift"
----

. Optional: Manually create a backup in a specific parent directory with a custom name by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift backup /mnt/_<other_backups_location>_/_<another_manual_backup>_
----
+
** For `_<other_backups_location>_`, specify the directory that you want to use.
** For `_<another_manual_backup>_`, specify the backup name that you want to use.

.Verification

* You can verify that the backup exists by viewing the data in the directory you chose. For example, `/var/lib/microshift-backups/_<manual_backup>_/` or `/mnt/_<other_backups_location>_/_<another_manual_backup>_`.

//Module included in the following assemblies:
//
// * microshift_updating/microshift-update-options.adoc
// * microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-restoring-data-backups-manually_{context}"]
= Restoring {microshift-short} data backups manually

[role="_abstract"]
To restore OpenShift Container Platform data after an update or data loss, you can run `microshift restore` with the full path to the backup. Backups can be restored after updates, or after other system events that remove or damage required data. When you restore a backup, you must use the entire file path.

[NOTE]
====
On an `rpm-ostree` system, {microshift-short} backs up and restores data automatically. Automated backups are in the `/var/lib/microshift-backups` directory by default.
====

.Prerequisites

* Root access to the host.
* You have the full path of the data backup file.
* The {microshift-short} service is stopped.

.Procedure

. Manually restore {microshift-short} data by using the full file path of the backup you want to restore by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift restore /var/lib/microshift-backups/_<manual_backup>_
----
+
** For `_<manual_backup>_`, specify the backup name that you want to use. Optionally, you can also restore automatic `ostree` backups using the full file path.
+
.Example output
[source,terminal]
----
??? I1017 07:39:52.055165    6007 data_manager.go:131] "Copying backup to data directory" storage="/var/lib/microshift-backups" name="test" data="/var/lib/microshift"
??? I1017 07:39:52.055243    6007 data_manager.go:154] "Renaming existing data dir" data="/var/lib/microshift" renamedTo="/var/lib/microshift.saved"
??? I1017 07:39:52.055326    6007 data_manager.go:227] "Starting copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift-backups/test /var/lib/microshift"
??? I1017 07:39:52.061363    6007 data_manager.go:241] "Finished copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift-backups/test /var/lib/microshift"
??? I1017 07:39:52.061404    6007 data_manager.go:175] "Removing temporary data directory" path="/var/lib/microshift.saved"
??? I1017 07:39:52.063745    6007 data_manager.go:180] "Copied backup to data directory" name="test" data="/var/lib/microshift"
----

. Optional. Manually restore data from a customized directory by using the full file path of the backup. Run the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift restore /mnt/_<other_backups_location>_/_<another_manual_backup>_
----
+
** For `_<other_backups_location>_`, specify the directory that you used.
** For `_<another_manual_backup>_`, specify the backup name that you used when creating the backup you are restoring.

. Restart the host. Restarting the host enables all workloads and pods to restart.

.Verification

* Use the `oc get pods -A` command to verify that the node is running, then check the restored data.
+
--
--
