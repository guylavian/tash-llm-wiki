---
title: "Configuring the {oadp-first} with more than one Backup Storage Location"
type: reference
domain: openshift
slug: backup-and-restore-4-22-configuring-oadp-multiple-bsl
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/configuring-oadp-multiple-bsl
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Configuring the {oadp-first} with more than one Backup Storage Location

[id="configuring-oadp-multiple-bsl"]
= Configuring the {oadp-first} with more than one Backup Storage Location

[role="_abstract"]
Configure multiple backup storage locations (BSLs) in the Data Protection Application (DPA) to store backups across different regions or storage providers. This provides flexibility and redundancy for your backup strategy.

{oadp-short} supports multiple credentials for configuring more than one BSL, so that you can specify the credentials to use with any BSL.

// module for configuring the DPA with multiple BSLs.
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/configuring-oadp-multiple-bsl.adoc

[id="oadp-configuring-dpa-multiple-bsl_{context}"]
= Configuring the DPA with more than one BSL

[role="_abstract"]
Configure the `DataProtectionApplication` (DPA) custom resource (CR) with multiple `BackupStorageLocation` (BSL) resources to store backups across different locations using provider-specific credentials. This provides backup distribution and location-specific restore capabilities.

For example, you have configured the following two BSLs:

* Configured one BSL in the DPA and set it as the default BSL.
* Created another BSL independently by using the `BackupStorageLocation` CR.

As you have already set the BSL created through the DPA as the default, you cannot set the independently created BSL again as the default. This means, at any given time, you can set only one BSL as the default BSL.

.Prerequisites

* You must install the {oadp-short} Operator.
* You must create the secrets by using the credentials provided by the cloud provider.

.Procedure

. Configure the `DataProtectionApplication` CR with more than one `BackupStorageLocation` CR. See the following example:
+
.Example DPA
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
#...
backupLocations:
  - name: aws
    velero:
      provider: aws
      default: true
      objectStorage:
        bucket: <bucket_name>
        prefix: <prefix>
      config:
        region: <region_name>
        profile: "default"
      credential:
        key: cloud
        name: cloud-credentials
  - name: odf
    velero:
      provider: aws
      default: false
      objectStorage:
        bucket: <bucket_name>
        prefix: <prefix>
      config:
        profile: "default"
        region: <region_name>
        s3Url: <url>
        insecureSkipTLSVerify: "true"
        s3ForcePathStyle: "true"
      credential:
        key: cloud
        name: <custom_secret_name_odf>
#...
----
+
where:
+
`name: aws`:: Specifies a name for the first BSL.
`default: true`:: Indicates that this BSL is the default BSL. If a BSL is not set in the `Backup CR`, the default BSL is used. You can set only one BSL as the default.
`<bucket_name>`:: Specifies the bucket name.
`<prefix>`:: Specifies a prefix for Velero backups. For example, `velero`.
`<region_name>`:: Specifies the AWS region for the bucket.
`cloud-credentials`:: Specifies the name of the default `Secret` object that you created.
`name: odf`:: Specifies a name for the second BSL.
`<url>`:: Specifies the URL of the S3 endpoint.
`<custom_secret_name_odf>`:: Specifies the correct name for the `Secret`. For example, `custom_secret_name_odf`. If you do not specify a `Secret` name, the default name is used.

. Specify the BSL to be used in the backup CR. See the following example.
+
.Example backup CR
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
# ...
spec:
  includedNamespaces:
  - <namespace>
  storageLocation: <backup_storage_location>
  defaultVolumesToFsBackup: true
----
+
where:
+
`<namespace>`:: Specifies the namespace to back up.
`<backup_storage_location>`:: Specifies the storage location.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/configuring-oadp-multiple-bsl.adoc

[id="oadp-changing-default-bsl_{context}"]
= Changing the default backup storage location in a DPA

[role="_abstract"]
Understand why the `default` field of the `backupLocations` object in a `DataProtectionApplication` (DPA) does not change the default `BackupStorageLocation` (BSL) when you configure multiple backup locations. This helps you to identify the root cause and apply the correct workaround.

When a DPA includes multiple backup locations, updating the `default` field to change the default BSL does not take effect. After you set `default: true` on a different BSL and set `default: false` on the previously default BSL, the `oc get bsl` command shows that the original BSL remains the default.

Root cause::
The {oadp-short} Operator sets the `default` field on a BSL resource only during initial creation of the DPA. On subsequent reconciliations, the Operator preserves the default BSL.
+
This behavior is intentional. Velero independently manages the `default` field on BSL resources. If the {oadp-short} Operator overwrites this field on every reconciliation, it conflicts with Velero, causing a race condition where both controllers compete over the value.
+
To prevent this conflict, the Operator checks whether the BSL already exists. If it exists, the Operator preserves the current `default` value instead of applying the value from the DPA specification.

Workaround::
To change the default BSL, delete and re-create the DPA. Deleting and re-creating the DPA ensures that the BSL resources are created from scratch. The new `default` setting is applied during initial creation and re-deployment of the DPA.

.Procedure

. Delete the existing DPA by running the following command:
+
[source,terminal]
----
$ oc delete dpa <dpa_name> -n openshift-adp
----
+
Replace `<dpa_name>` with the name of the DPA custom resource.

. Re-create the DPA with the updated default BSL configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f <updated_dpa_file>
----
+
Replace `<updated_dpa_file>` with the file name of the updated DPA custom resource definition.

// module for multiple BSL use case.
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/configuring-oadp-multiple-bsl.adoc

[id="oadp-multiple-bsl-use-case_{context}"]
= Configuring two backup BSLs with different cloud credentials

[role="_abstract"]
Configure two backup storage locations with different cloud credentials to back up applications to multiple storage targets. With this setup, you can distribute backups across different storage providers for redundancy.

.Prerequisites

* You must install the {oadp-short} Operator.
* You must configure two backup storage locations: AWS S3 and Multicloud Object Gateway (MCG).
* You must have an application with a database deployed on a Red Hat OpenShift cluster.

.Procedure

. Create the first `Secret` for the AWS S3 storage provider with the default name by running the following command:
+
[source,terminal]
----
$ oc create secret generic cloud-credentials -n openshift-adp --from-file cloud=<aws_credentials_file_name>
----
+
where:
+
`<aws_credentials_file_name>`:: Specifies the name of the cloud credentials file for AWS S3.

. Create the second `Secret` for MCG with a custom name by running the following command:
+
[source,terminal]
----
$ oc create secret generic mcg-secret -n openshift-adp --from-file cloud=<MCG_credentials_file_name>
----
+
where:
+
`<MCG_credentials_file_name>`:: Specifies the name of the cloud credentials file for MCG. Note the name of the `mcg-secret` custom secret.

. Configure the DPA with the two BSLs as shown in the following example.
+
.Example DPA
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: two-bsl-dpa
  namespace: openshift-adp
spec:
  backupLocations:
  - name: aws
    velero:
      config:
        profile: default
        region: <region_name>
      credential:
        key: cloud
        name: cloud-credentials
      default: true
      objectStorage:
        bucket: <bucket_name>
        prefix: velero
      provider: aws
  - name: mcg
    velero:
      config:
        insecureSkipTLSVerify: "true"
        profile: noobaa
        region: <region_name>
        s3ForcePathStyle: "true"
        s3Url: <s3_url>
      credential:
        key: cloud
        name: mcg-secret
      objectStorage:
        bucket: <bucket_name_mcg>
        prefix: velero
      provider: aws
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
      - openshift
      - aws
----
+
where:
+
`<region_name>`:: Specifies the AWS region for the bucket.
`<bucket_name>`:: Specifies the AWS S3 bucket name.
`region: <region_name>`:: Specifies the region, following the naming convention of the documentation of MCG.
`<s3_url>`:: Specifies the URL of the S3 endpoint for MCG.
`mcg-secret`:: Specifies the name of the custom secret for MCG storage.
`<bucket_name_mcg>`:: Specifies the MCG bucket name.

. Create the DPA by running the following command:
+
[source,terminal]
----
$ oc create -f <dpa_file_name>
----
+
where:
+
`<dpa_file_name>`:: Specifies the file name of the DPA you configured.

. Verify that the DPA has reconciled by running the following command:
+
[source,terminal]
----
$ oc get dpa -o yaml
----

. Verify that the BSLs are available by running the following command:
+
[source,terminal]
----
$ oc get bsl
----
+
.Example output
[source,terminal]
----
NAME   PHASE       LAST VALIDATED   AGE     DEFAULT
aws    Available   5s               3m28s   true
mcg    Available   5s               3m28s
----

. Create a backup CR with the default BSL.
+
[NOTE]
====
In the following example, the `storageLocation` field is not specified in the backup CR.
====
+
.Example backup CR
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup1
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <mysql_namespace>
  defaultVolumesToFsBackup: true
----
+
where:
+
`<mysql_namespace>`:: Specifies the namespace for the application installed in the cluster.

. Create a backup by running the following command:
+
[source,terminal]
----
$ oc apply -f <backup_file_name>
----
+
where:
+
`<backup_file_name>`:: Specifies the name of the backup CR file.

. Verify that the backup completed with the default BSL by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io <backup_name> -o yaml
----
+
where:
+
`<backup_name>`:: Specifies the name of the backup.

. Create a backup CR by using MCG as the BSL. In the following example, note that the second `storageLocation` value is specified at the time of backup CR creation.
+
.Example backup `CR`
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup1
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <mysql_namespace>
  storageLocation: mcg
  defaultVolumesToFsBackup: true
----
+
where:
+
`<mysql_namespace>`:: Specifies the namespace for the application installed in the cluster.
`mcg`:: Specifies the second storage location.

. Create a second backup by running the following command:
+
[source, terminal]
----
$ oc apply -f <backup_file_name>
----
+
where:
+
`<backup_file_name>`:: Specifies the name of the backup CR file.

. Verify that the backup completed with the storage location as MCG by running the following command:
+
[source, terminal]
----
$ oc get backups.velero.io <backup_name> -o yaml
----
+
where:
+
`<backup_name>`:: Specifies the name of the backup.

[role="_additional-resources"]
.Additional resources

* Creating profiles for different credentials
