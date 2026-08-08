---
title: "OADP Data protection test"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-data-protection-test
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-data-protection-test
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# OADP Data protection test

[id="oadp-data-protection-test"]
= OADP Data protection test

[role="_abstract"]
Validate your {oadp-short} configuration by using the `DataProtectionTest` (DPT) custom resource (CR). This helps you ensure your data protection environment is properly configured and performing according to your requirements before performing backups.

The DPT checks the upload performance of backups to object storage, CSI snapshot readiness for persistent volume claims, and storage bucket configuration such as encryption and versioning.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="oadp-dpt-spec_{context}"]
= OADP DataProtectionTest CR specification fields

[role="_abstract"]
Review the specification fields available in the `DataProtectionTest` (DPT) custom resource (CR) to configure backup location, upload speed tests, CSI volume snapshot tests, and other options. This helps you customize the DPT CR to validate your specific {oadp-short} configuration requirements.

.DPT CR spec fields
|===
|Field |Type |Description

| `backupLocationName` | string | Name of the `BackupStorageLocation` CR configured in the `DataProtectionApplication` (DPA) CR.
| `backupLocationSpec` | object | Inline specification of the `BackupStorageLocation` CR.
| `uploadSpeedTestConfig` | object | Configuration to run an upload speed test to the object storage.
| `csiVolumeSnapshotTestConfigs` | list | List of persistent volume claims to take a snapshot of and to verify the snapshot readiness.
| `forceRun` | boolean | Re-run the DPT CR even if status is `Complete` or `Failed`.
| `skipTLSVerify` | boolean | Bypasses the TLS certificate validation if set to `true`.

|===

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="oadp-dpt-status_{context}"]
= OADP DataProtectionTest CR status fields

[role="_abstract"]
Review the status fields in the `DataProtectionTest` (DPT) custom resource (CR) to monitor test progress, upload speed results, bucket metadata, and snapshot test outcomes. This helps you interpret the DPT CR results and identify any issues with your {oadp-short} configuration.

.DPT CR status fields
|===
|Field |Type |Description

| `phase` | string | Current phase of the DPT CR. Values are `InProgress`, `Complete`, or `Failed`.
| `lastTested` | timestamp | The timestamp when the DPT CR was last run.
| `uploadTest` | object | Results of the upload speed test.
| `bucketMetadata` | object | Information about the storage bucket encryption and versioning.
| `snapshotTests` | list | Snapshot test results for each persistent volume claim.
| `snapshotSummary` | string | Aggregated pass/fail summary for snapshots. For example, `2/2 passed`.
| `s3Vendor` | string | {aws-short} S3-compatible storage bucket vendors. For example, {aws-short}, MinIO, Ceph.
| `errorMessage` | string | Error message if the DPT CR fails.

|===

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="using-data-protection-test_{context}"]
= Using the DataProtectionTest custom resource

[role="_abstract"]
Configure and run the `DataProtectionTest` (DPT) custom resource (CR) to verify Container Storage Interface (CSI) snapshot readiness and data upload performance to your storage bucket. This helps you validate your {oadp-short} environment before performing backup and restore operations.

.Prerequisites

* You have logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have installed the {oadp-short} Operator.
* You have created the `DataProtectionApplication` (DPA) CR.
* You have configured a backup storage location (BSL) to store the backups.
* You have an application with persistent volume claims (PVCs) running in a separate namespace.

.Procedure

.  Create a manifest file for the DPT CR as shown in the example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationName: <bsl_name>
  csiVolumeSnapshotTestConfigs:
  - snapshotClassName: csi-gce-pd-vsc
    timeout: 90s
    volumeSnapshotSource:
      persistentVolumeClaimName: <pvc1_name>
      persistentVolumeClaimNamespace: <pvc_namespace>
  - snapshotClassName: csi-gce-pd-vsc
    timeout: 120s
    volumeSnapshotSource:
      persistentVolumeClaimName: <pvc2_name>
      persistentVolumeClaimNamespace: <pvc_namespace>
  forceRun: false
  uploadSpeedTestConfig:
    fileSize: 200MB
    timeout: 120s
----
+
where:
+
`<bsl_name>`:: Specifies the name of the BSL.
`csiVolumeSnapshotTestConfigs`:: Specifies a list for `csiVolumeSnapshotTestConfigs`. In this example, two PVCs are being tested.
`<pvc1_name>`:: Specifies the name of the first PVC.
`<pvc_namespace>`:: Specifies the namespace of the PVC.
`<pvc2_name>`:: Specifies the name of the second PVC.
`forceRun`:: Set to `false` if you want to make the {oadp-short} controller skip re-running tests.
`uploadSpeedTestConfig`:: Configures the upload speed test by setting the `fileSize` and `timeout` fields.

. Create the DPT CR by running the following command:
+
[source,terminal]
----
$ oc create -f <dpt_file_name>
----
+
Replace `<dpt_file_name>` with the file name of the DPT manifest.

.Verification

. Verify that the phase of the DPT CR is `Complete` by running the following command:
+
[source,terminal]
----
$ oc get dpt dpt-sample
----
+
The example output is as following:
+
[source,terminal]
----
NAME         PHASE      LASTTESTED   UPLOADSPEED(MBPS)   ENCRYPTION   VERSIONING   SNAPSHOTS    AGE
dpt-sample   Complete   17m          546                 AES256       Enabled      2/2 passed   17m
----

. Verify that the CSI snapshots are ready and the data upload tests are successful by running the following command:
+
[source,terminal]
----
$ oc get dpt dpt-sample -o yaml
----
+
The example output is as following:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
....
status:
  bucketMetadata:
    encryptionAlgorithm: AES256
    versioningStatus: Enabled
  lastTested: "202...:47:51Z"
  phase: Complete
  s3Vendor: AWS
  snapshotSummary: 2/2 passed
  snapshotTests:
  - persistentVolumeClaimName: mysql-data
    persistentVolumeClaimNamespace: ocp-mysql
    readyDuration: 24s
    status: Ready
  - persistentVolumeClaimName: mysql-data1
    persistentVolumeClaimNamespace: ocp-mysql
    readyDuration: 40s
    status: Ready
  uploadTest:
    duration: 3.071s
    speedMbps: 546
    success: true
----
+
where:
+
`bucketMetadata`:: Specifies the bucket metadata information.
`s3Vendor`:: Specifies the S3 bucket vendor.
`snapshotSummary`:: Specifies the summary of the CSI snapshot tests.
`uploadTest`:: Specifies the upload test details.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="oadp-dpt-use-case-bsl-spec_{context}"]
= Running a data protection test by configuring a backup storage location specification

[role="_abstract"]
Configure and run the `DataProtectionTest` (DPT) custom resource (CR) by specifying an inline backup storage location (BSL) specification instead of referencing an existing BSL name. This helps you test data upload performance and CSI snapshot readiness without creating a separate BSL resource.

.Prerequisites

* You have logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have installed the {oadp-short} Operator.
* You have created the `DataProtectionApplication` (DPA) CR.
* You have configured a bucket to store the backups.
* You have created the `Secret` object to access the bucket storage.
* You have an application with persistent volume claims (PVCs) running in a separate namespace.

.Procedure

.  Create a manifest file for the DPT CR as shown in the example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationSpec:
    provider: aws
    default: true
    objectStorage:
      bucket: sample-bucket
      prefix: velero
    config:
      region: us-east-1
      profile: "default"
      insecureSkipTLSVerify: "true"
      s3Url: "https://s3.amazonaws.com/sample-bucket"
    credential:
      name: cloud-credentials
      key: cloud
  uploadSpeedTestConfig:
    fileSize: 50MB
    timeout: 120s
  csiVolumeSnapshotTestConfigs:
    - volumeSnapshotSource:
        persistentVolumeClaimName: mongo
        persistentVolumeClaimNamespace: mongo-persistent
      snapshotClassName: csi-snapclass
      timeout: 2m
  forceRun: true
  skipTLSVerify: true
----
+
where:
+
`backupLocationSpec`:: Configures the BSL spec by specifying details such as the cloud provider.
`sample-bucket`:: Specifies the bucket name. In this example, the bucket name is `sample-bucket`.
`us-east-1`:: Specifies the cloud provider region.
`credential`:: Specifies the cloud credentials for the storage bucket.
`uploadSpeedTestConfig`:: (Optional) Configures the upload speed test by setting the `fileSize` and `timeout` fields.
`csiVolumeSnapshotTestConfigs`:: Configures the CSI volume snapshot test.
`skipTLSVerify`:: Set to `true` to skip the TLS certificate validation during the DPT CR run.

. Create the DPT CR by running the following command:
+
[source,terminal]
----
$ oc create -f <dpt_file_name>
----
+
Replace `<dpt_file_name>` with the file name of the DPT manifest.

.Verification

. Verify that the phase of the DPT CR is `Complete` by running the following command:
+
[source,terminal]
----
$ oc get dpt dpt-sample
----
+
The example output is as following:
+
[source,terminal]
----
NAME         PHASE      LASTTESTED   UPLOADSPEED(MBPS)   ENCRYPTION   VERSIONING   SNAPSHOTS    AGE
dpt-sample   Complete   17m          546                 AES256       Enabled      2/2 passed   17m
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="oadp-dpt-use-case-azure_{context}"]
= Running a data protection test on an Azure object storage

[role="_abstract"]
Run the `DataProtectionTest` (DPT) custom resource (CR) on Azure object storage by configuring the required Azure credentials, including the `STORAGE_ACCOUNT_ID` parameter in the secret object. This helps you validate your {oadp-short} configuration and verify CSI snapshot readiness on Azure clusters.

.Prerequisites

* You have logged in to the Azure cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have installed the {oadp-short} Operator.
* You have configured a bucket to store the backups.
* You have an application with persistent volume claims (PVCs) running in a separate namespace.

.Procedure

. Add the `Storage Blob Data Contributor` role to Azure `storageAccount` object to avoid DPT run failure. Run the following command:
+
[source,terminal]
----
$ az role assignment create \
--assignee "$AZURE_CLIENT_ID" \
--role "Storage Blob Data Contributor" \
--scope "/subscriptions/$AZURE_SUBSCRIPTION_ID/resourceGroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$AZURE_STORAGE_ACCOUNT_ID"
----

. In your terminal, export the Azure parameters and create a secret credentials file with the parameters as shown in the following example.
+
To run the DPT CR on Azure, you need to specify the `STORAGE_ACCOUNT_ID` parameter in the secret credentials file.
+
[source,terminal]
----
AZURE_SUBSCRIPTION_ID=<subscription_id>
AZURE_TENANT_ID=<tenant_id>
AZURE_CLIENT_ID=<client_id>
AZURE_CLIENT_SECRET=<client_secret>
AZURE_RESOURCE_GROUP=<resource_group>
AZURE_STORAGE_ACCOUNT_ID=<storage_account>
----

. Create the `Secret` CR as shown in the following example:
+
[source,terminal]
----
$ oc create secret generic cloud-credentials-azure -n openshift-adp --from-file cloud=<credentials_file_path>
----

. Create the `DataProtectionApplication` (DPA) CR by using the configuration shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - azure
        - openshift
  backupLocations:
    - velero:
        config:
          resourceGroup: oadp-....-b7q4-rg
          storageAccount: oadp...kb7q4
          subscriptionId: 53b8f5...fd54c8a
        credential:
          key: cloud
          name: cloud-credentials-azure
        provider: azure
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: velero
----
+
Replace `name` with the name of the `Secret` object. In this example, the name is `cloud-credentials-azure`.

. Create the DPT CR by specifying the name of backup storage location (BSL), `VolumeSnapshotClass` object, and the persistent volume claim details as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationName: <bsl_name>
  uploadSpeedTestConfig:
    fileSize: 40MB
    timeout: 120s
  csiVolumeSnapshotTestConfigs:
    - snapshotClassName: csi-azuredisk-vsc
      timeout: 90s
      volumeSnapshotSource:
        persistentVolumeClaimName: mysql-data
        persistentVolumeClaimNamespace: ocp-mysql
    - snapshotClassName: csi-azuredisk-vsc
      timeout: 120s
      volumeSnapshotSource:
        persistentVolumeClaimName: mysql-data1
        persistentVolumeClaimNamespace: ocp-mysql
----
+
where:
+
`<bsl_name>`:: Specifies the name of the BSL.
`csi-azuredisk-vsc`:: Specifies the Azure snapshot class name.
`mysql-data`:: Specifies the name of the persistent volume claim.
`ocp-mysql`:: Specifies the name of the persistent volume claim namespace.

. Run the DPT CR to verify the snapshot readiness.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-data-protection-test.adoc

[id="oadp-troubleshooting-dpt_{context}"]
= Troubleshooting the DataProtectionTest custom resource

[role="_abstract"]
Troubleshoot common `DataProtectionTest` (DPT) custom resource (CR) issues, such as stuck progress states, upload test failures, and snapshot test failures. This helps you identify and resolve problems with your DPT configuration.

.DPT CR troubleshooting
|===
|Error |Reason |Solution

| DPT stuck in `InProgress` state | Bucket credentials or bucket access failure | Check `Secret` object, bucket permissions, and logs.
| Upload test failed | Incorrect `Secret` object or S3 endpoint | Check the `BackupStorageLocation` object config and the access keys.
| Snapshot tests fail | Incorrect configuration of CSI snapshot controller | Check the `VolumeSnapshotClass` object availability and the CSI driver logs.
| Bucket encryption or versioning not populated | Cloud provider limitations | Not all object storage providers expose these fields consistently.

|===
