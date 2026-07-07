---
title: "Enabling parallel backup processing"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-enabling-parallel-backup-processing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-enabling-parallel-backup-processing
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Enabling parallel backup processing

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/backing_up_and_restoring/backing-up-applications.adoc

[id="oadp-enabling-parallel-backup-processing_{context}"]
= Enabling parallel backup processing

[role="_abstract"]
By default, {oadp-full} processes only one backup in the `InProgress` phase at a time. Configure the `DataProtectionApplication` (DPA) custom resource (CR) to run several backups simultaneously to prevent smaller backups from being queued behind larger operations.

.Prerequisites
* You must be logged in as a user with `cluster-admin` privileges.
* You must have a DPA CR configured and deployed in your cluster.

.Procedure

. Edit your DPA CR:
+
[source,terminal,subs="+quotes"]
----
$ oc edit dpa <dpa_name> -n openshift-adp
----

. Add the `concurrentBackups` field in the `spec.configuration.velero` section of your DPA CR:
+
[source,yaml]
----
  configuration:
    velero:
      concurrentBackups: <integer_limit>
      defaultPlugins:
        - openshift
        - aws
        - csi
----
+
Replace `<integer_limit>` with the maximum number of backups you want {oadp-short} to process simultaneously. The default value is `1`. Backups that target overlapping namespaces are automatically serialized.

.Verification

* Verify that all backups are in the `InProgress` phase simultaneously:
+
[source,terminal]
----
$ oc get backups.velero.io -n openshift-adp
----
+
.Example output
[source,terminal]
----
NAME                STATUS       CREATED                        EXPIRES
backup-namespace1   InProgress   2026-04-28 10:00:00 +0000 UTC  29d
backup-namespace2   InProgress   2026-04-28 10:00:05 +0000 UTC  29d
----
