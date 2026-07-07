---
title: "OADP installation issues"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-installation-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-installation-issues
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# OADP installation issues

[id="oadp-installation-issues"]
= OADP installation issues

[role="_abstract"]
Resolve common installation issues with the Data Protection Application (DPA), such as invalid backup storage directories and incorrect cloud provider credentials. This helps you successfully install and configure {oadp-short} in your environment.

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/troubleshooting/oadp-installation-issues.adoc
//

[id="resolving-backup-storage-contains-invalid-directories-issue_{context}"]
= Resolving invalid directories in backup storage

[role="_abstract"]
Resolve the `Backup storage contains invalid top-level directories` error that occurs when object storage contains non-Velero directories. This helps you configure the correct bucket prefix for shared object storage.

.Procedure

* If the object storage is not dedicated to Velero, you must specify a prefix for the bucket by setting the `spec.backupLocations.velero.objectStorage.prefix` parameter in the `DataProtectionApplication` manifest.

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/troubleshooting/oadp-installation-issues.adoc
//

[id="resolving-incorrect-aws-credentials-issue_{context}"]
= Resolving incorrect {aws-short} credentials

[role="_abstract"]
Resolve credential errors such as `InvalidAccessKeyId` or `NoCredentialProviders` that occur when the `credentials-velero` file is incorrectly formatted. This helps you configure valid {aws-short} credentials for {oadp-short} backup operations.

If you incorrectly format the `credentials-velero` file used for creating the `Secret` object, multiple errors might occur, including the following examples:

* The `oadp-aws-registry` pod log displays the following error message:
+
[source,text]
----
`InvalidAccessKeyId: The AWS Access Key Id you provided does not exist in our records.`
----

* The `Velero` pod log displays the following error message:
+
[source,text]
----
NoCredentialProviders: no valid providers in chain.
----

.Procedure

* Ensure that the `credentials-velero` file is correctly formatted, as shown in the following example:
+
----
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
----
+
where:
+
`[default]`:: Specifies the {aws-short} default profile.
`aws_access_key_id`:: Do not enclose the values with quotation marks (`"`, `'`).
