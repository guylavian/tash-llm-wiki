---
title: "Configuring the {oadp-full} with {ibm-cloud-title}"
type: reference
domain: openshift
slug: backup-and-restore-4-22-installing-oadp-ibm-cloud
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/installing-oadp-ibm-cloud
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Configuring the {oadp-full} with {ibm-cloud-title}

[id="installing-oadp-ibm-cloud"]
= Configuring the {oadp-full} with {ibm-cloud-title}

[role="_abstract"]
You install the {oadp-first} Operator on an {ibm-cloud-title} cluster to back up and restore applications on the cluster. You configure {ibm-cloud-object-storage} to store the backups.

// configuring the IBM COS instance
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ibm-cloud.adoc

[id="configuring-ibm-cos_{context}"]
= Configuring the COS instance

[role="_abstract"]
You create an {ibm-cloud-object-storage} instance to store the {oadp-short} backup data. After you create the COS instance, configure the `HMAC` service credentials.

.Prerequisites

* You have an {ibm-cloud-title} Platform account.
* You installed the {ibm-cloud-title} CLI.
* You are logged in to {ibm-cloud-title}.

.Procedure

. Install the {ibm-cloud-object-storage} plugin by running the following command:
+
[source,terminal]
----
$ ibmcloud plugin install cos -f
----

. Set a bucket name by running the following command:
+
[source,terminal]
----
$ BUCKET=<bucket_name>
----

. Set a bucket region by running the following command:
+
[source,terminal]
----
$ REGION=<bucket_region>
----
+
where:
+
`<bucket_region>`:: Specifies the bucket region. For example, `eu-gb`.

. Create a resource group by running the following command:
+
[source,terminal]
----
$ ibmcloud resource group-create <resource_group_name>
----

. Set the target resource group by running the following command:
+
[source,terminal]
----
$ ibmcloud target -g <resource_group_name>
----

. Verify that the target resource group is correctly set by running the following command:
+
[source,terminal]
----
$ ibmcloud target
----
+
.Example output

[source,yaml]
----
API endpoint:     https://cloud.ibm.com
Region:
User:             test-user
Account:          Test Account (fb6......e95) <-> 2...122
Resource group:   Default
----
+
In the example output, the resource group is set to `Default`.

. Set a resource group name by running the following command:
+
[source,terminal]
----
$ RESOURCE_GROUP=<resource_group>
----
+
where:
+
`<resource_group>`:: Specifies the resource group name. For example, `"default"`.

. Create an {ibm-cloud-title} `service-instance` resource  by running the following command:
+
[source,terminal]
----
$ ibmcloud resource service-instance-create \
<service_instance_name> \
<service_name> \
<service_plan> \
<region_name>
----
+
where:
+
`<service_instance_name>`:: Specifies a name for the `service-instance` resource.
`<service_name>`:: Specifies the service name. Alternatively, you can specify a service ID.
`<service_plan>`:: Specifies the service plan for your {ibm-cloud-title} account.
`<region_name>`:: Specifies the region name.

+
--
Refer to the following example command:

[source,terminal]
----
$ ibmcloud resource service-instance-create test-service-instance cloud-object-storage \
standard \
global \
-d premium-global-deployment
----
where:

`cloud-object-storage`:: Specifies the service name.
`-d premium-global-deployment`:: Specifies the deployment name.
--
+

. Extract the service instance ID by running the following command:
+
[source,terminal]
----
$ SERVICE_INSTANCE_ID=$(ibmcloud resource service-instance test-service-instance --output json | jq -r '.[0].id')
----

. Create a COS bucket by running the following command:
+
[source,terminal]
----
$ ibmcloud cos bucket-create \
--bucket $BUCKET \
--ibm-service-instance-id $SERVICE_INSTANCE_ID \
--region $REGION
----
+
Variables such as `$BUCKET`, `$SERVICE_INSTANCE_ID`, and `$REGION` are replaced by the values you set previously.

. Create `HMAC` credentials by running the following command.
+
[source,terminal]
----
$ ibmcloud resource service-key-create test-key Writer --instance-name test-service-instance --parameters {\"HMAC\":true}
----

. Extract the access key ID and the secret access key from the `HMAC` credentials and save them in the `credentials-velero` file. You can use the `credentials-velero` file to create a `secret` for the backup storage location. Run the following command:
+
[source,terminal]
----
$ cat > credentials-velero << __EOF__
[default]
aws_access_key_id=$(ibmcloud resource service-key test-key -o json  | jq -r '.[0].credentials.cos_hmac_keys.access_key_id')
aws_secret_access_key=$(ibmcloud resource service-key test-key -o json  | jq -r '.[0].credentials.cos_hmac_keys.secret_access_key')
__EOF__
----
// include the module for creating default secret

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-creating-default-secret_{context}"]
= Creating a default Secret

[role="_abstract"]
You create a default `Secret` if your backup and snapshot locations use the same credentials or if you do not require a snapshot location.

The default name of the `Secret` is `{credentials}`.
The default name of the `Secret` is `{credentials}`, unless your backup storage provider has a default plugin, such as `aws`, `azure`, or `gcp`. In that case, the default name is specified in the provider-specific OADP installation procedure.

[NOTE]
====
The `DataProtectionApplication` custom resource (CR) requires a default `Secret`.  Otherwise, the installation will fail. If the name of the backup location `Secret` is not specified, the default name is used.

If you do not want to use the backup location credentials during the installation, you can create a `Secret` with the default name by using an empty `credentials-velero` file.
====

.Prerequisites

* Your object storage and cloud storage, if any, must use the same credentials.
* You must configure object storage for Velero.

.Procedure

. Create a `credentials-velero` file for the backup storage location in the appropriate format for your cloud provider.

+
See the following example:
+
[source,terminal]
----
[default]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
----
+
You can use one of the following two methods to authenticate {oadp-short} with Azure.

* Use the service principal with secret-based authentication. See the following example:
+
[source,terminal]
----
AZURE_SUBSCRIPTION_ID=<azure_subscription_id>
AZURE_TENANT_ID=<azure_tenant_id>
AZURE_CLIENT_ID=<azure_client_id>
AZURE_CLIENT_SECRET=<azure_client_secret>
AZURE_RESOURCE_GROUP=<azure_resource_group>
AZURE_CLOUD_NAME=<azure_cloud_name>
----

* Use a storage account access key. See the following example:
+
[source,terminal]
----
AZURE_STORAGE_ACCOUNT_ACCESS_KEY=<azure_storage_account_access_key>
AZURE_SUBSCRIPTION_ID=<azure_subscription_id>
AZURE_RESOURCE_GROUP=<azure_resource_group>
AZURE_CLOUD_NAME=<azure_cloud_name>
----

. Create a `Secret` custom resource (CR) with the default name:
+
[source,terminal,subs="attributes+"]
----
$ oc create secret generic {credentials} -n openshift-adp --from-file cloud=credentials-velero
----
+
The `Secret` is referenced in the `spec.backupLocations.credential` block of the `DataProtectionApplication` CR when you install the Data Protection Application.
// include the module for creating custom secret

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-secrets-for-different-credentials_{context}"]
= Creating secrets for different credentials

[role="_abstract"]
Create separate `Secret` objects when your backup and snapshot locations require different credentials. This allows you to configure distinct authentication for each storage location while maintaining secure credential management.

.Procedure

. Create a `credentials-velero` file for the snapshot location in the appropriate format for your cloud provider.
. Create a `Secret` for the snapshot location with the default name:
+
[source,terminal,subs="attributes+"]
----
$ oc create secret generic {credentials} -n openshift-adp --from-file cloud=credentials-velero
----

. Create a `credentials-velero` file for the backup location in the appropriate format for your object storage.
. Create a `Secret` for the backup location with a custom name:
+
[source,terminal,subs="attributes+"]
----
$ oc create secret generic <custom_secret> -n openshift-adp --from-file cloud=credentials-velero
----

. Add the `Secret` with the custom name to the `DataProtectionApplication` CR, as in the following example:

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
...
  backupLocations:
    - velero:
        config:
          resourceGroup: <azure_resource_group>
          storageAccount: <azure_storage_account_id>
          subscriptionId: <azure_subscription_id>
          storageAccountKeyEnvVar: AZURE_STORAGE_ACCOUNT_ACCESS_KEY
        credential:
          key: cloud
          name: <custom_secret>
        provider: azure
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
  snapshotLocations:
    - velero:
        config:
          resourceGroup: <azure_resource_group>
          subscriptionId: <azure_subscription_id>
          incremental: "true"
        provider: {provider}
----
+
where:
+
`custom_secret`:: Specifies the backup location `Secret` with custom name.
+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
...
  backupLocations:
    - velero:
        provider: {provider}
        default: true
        credential:
          key: cloud
          name: <custom_secret>
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
  snapshotLocations:
    - velero:
        provider: {provider}
        default: true
        config:
          project: <project>
          snapshotLocation: us-west1
----
+
where:
+
`custom_secret`:: Specifies the backup location `Secret` with custom name.
+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
...
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: <region_name>
          s3Url: <url>
          insecureSkipTLSVerify: "true"
          s3ForcePathStyle: "true"
        provider: {provider}
        default: true
        credential:
          key: cloud
          name:  <custom_secret>
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
----
+
where:
+
`region_name`:: Specifies the region, following the naming convention of the documentation of your object storage server.
`custom_secret`:: Specifies the backup location `Secret` with custom name.
+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
...
  backupLocations:
    - velero:
        provider: <provider>
        default: true
        credential:
          key: cloud
          name: <custom_secret>
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
----
+
where:
+
`custom_secret`:: Specifies the backup location `Secret` with custom name.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include the DPA module

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.adoc
// * virt/backup_restore/virt-backup-restore-overview.adoc

[id="oadp-installing-dpa_{context}"]
= Installing the Data Protection Application

[role="_abstract"]
You install the Data Protection Application (DPA) by creating an instance of the `DataProtectionApplication` API.

.Prerequisites

* You must install the OADP Operator.
* You must configure object storage as a backup location.
* If you use snapshots to back up PVs, your cloud provider must support either a native snapshot API or Container Storage Interface (CSI) snapshots.
* If the backup and snapshot locations use the same credentials, you must create a `Secret` with the default name, `{credentials}`.
* If the backup and snapshot locations use different credentials, you must create two `Secrets`:

** `Secret` with a custom name for the backup location. You add this `Secret` to the `DataProtectionApplication` CR.
** `Secret` with another custom name for the snapshot location. You add this `Secret` to the `DataProtectionApplication` CR.

* If the backup and snapshot locations use different credentials, you must create a `Secret` with the default name, `{credentials}`, which contains separate profiles for the backup and snapshot location credentials.
+
[NOTE]
====
If you do not want to specify backup or snapshot locations during the installation, you can create a default `Secret` with an empty `credentials-velero` file. If there is no default `Secret`, the installation will fail.
====

.Procedure

. Click *Ecosystem* -> *Installed Operators* and select the OADP Operator.
. Under *Provided APIs*, click *Create instance* in the *DataProtectionApplication* box.

. Click *YAML View* and update the parameters of the `DataProtectionApplication` manifest:

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - openshift
        - aws
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - name: default
      velero:
        provider: {provider}
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
        config:
          region: <region>
          profile: "default"
          s3ForcePathStyle: "true"
          s3Url: <s3_url>
        credential:
          key: cloud
          name: {credentials}
  snapshotLocations:
    - name: default
      velero:
        provider: {provider}
        config:
          region: <region>
          profile: "default"
        credential:
          key: cloud
          name: {credentials}
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` or `restic` as your uploader. You cannot change the selection after the installation. For the Built-in DataMover you must use Kopia. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia or Restic are available. By default, Kopia or Restic run on all nodes.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.
`s3ForcePathStyle`:: Specifies whether to force path style URLs for S3 objects (Boolean). Not Required for AWS S3. Required only for S3 compatible storage.
`s3Url`:: Specifies the URL of the object store that you are using to store backups. Not required for AWS S3. Required only for S3 compatible storage.
`name`:: Specifies the name of the `Secret` object that you created. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the backup location.
`snapshotLocations`:: Specifies a snapshot location, unless you use CSI snapshots or a File System Backup (FSB) to back up PVs.
`region`:: Specifies that the snapshot location must be in the same region as the PVs.
`name`:: Specifies the name of the `Secret` object that you created. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the snapshot location. If your backup and snapshot locations use different credentials, create separate profiles in the `credentials-velero` file.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  namespace: openshift-adp
  name: <dpa_name>
spec:
  configuration:
    velero:
      defaultPlugins:
      - openshift
      - aws
      - csi
  backupLocations:
    - velero:
        provider: aws
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: velero
        config:
          insecureSkipTLSVerify: 'true'
          profile: default
          region: <region_name>
          s3ForcePathStyle: 'true'
          s3Url: <s3_url>
        credential:
          key: cloud
          name: cloud-credentials
----
+
where:
+
`provider`:: Specifies that the provider is `aws` when you use {ibm-cloud-title} as a backup storage location.
`bucket`:: Specifies the {ibm-cloud-object-storage} bucket name.
`region`:: Specifies the COS region name, for example, `eu-gb`.
`s3Url`:: Specifies the S3 URL of the COS bucket. For example, `http://s3.eu-gb.cloud-object-storage.appdomain.cloud`. Here, `eu-gb` is the region name. Replace the region name according to your bucket region.
`name`:: Specifies the name of the secret you created by using the access key and the secret access key from the `HMAC` credentials.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - azure
        - openshift
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - velero:
        config:
          resourceGroup: <azure_resource_group>
          storageAccount: <azure_storage_account_id>
          subscriptionId: <azure_subscription_id>
        credential:
          key: cloud
          name: {credentials}
        provider: {provider}
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
  snapshotLocations:
    - velero:
        config:
          resourceGroup: <azure_resource_group>
          subscriptionId: <azure_subscription_id>
          incremental: "true"
        name: default
        provider: {provider}
        credential:
          key: cloud
          name: {credentials}
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` or `restic` as your uploader. You cannot change the selection after the installation. For the Built-in DataMover you must use Kopia. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia or Restic are available. By default, Kopia or Restic run on all nodes.
`resourceGroup`:: Specifies the Azure resource group.
`storageAccount`:: Specifies the Azure storage account ID.
`subscriptionId`:: Specifies the Azure subscription ID.
`name`:: Specifies the name of the `Secret` object. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the backup location.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.
`snapshotLocations`:: Specifies the snapshot location. You do not need to specify a snapshot location if you use CSI snapshots or Restic to back up PVs.
`name`:: Specifies the name of the `Secret` object that you created. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the backup location.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: <OPERATOR_INSTALL_NS>
spec:
  configuration:
    velero:
      defaultPlugins:
        - gcp
        - openshift
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - velero:
        provider: {provider}
        default: true
        credential:
          key: cloud
          name: {credentials}
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
  snapshotLocations:
    - velero:
        provider: {provider}
        default: true
        config:
          project: <project>
          snapshotLocation: us-west1
        credential:
          key: cloud
          name: {credentials}
  backupImages: true
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` or `restic` as your uploader. You cannot change the selection after the installation. For the Built-in DataMover you must use Kopia. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia or Restic are available. By default, Kopia or Restic run on all nodes.
`key`:: Specifies the secret key that contains credentials. For Google workload identity federation cloud authentication use `service_account.json`.
`name`:: Specifies the secret name that contains credentials. If you do not specify this value, the default name, `{credentials}`, is used.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.
`snapshotLocations`:: Specifies a snapshot location, unless you use CSI snapshots or Restic to back up PVs.
`snapshotLocation`:: Specifies that the snapshot location must be in the same region as the PVs.
`name`:: Specifies the name of the `Secret` object that you created. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the backup location.
`backupImages`:: Specifies that Google workload identity federation supports internal image backup. Set this field to `false` if you do not want to use image backup.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - aws
        - openshift
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: <region_name>
          s3Url: <url>
          insecureSkipTLSVerify: "true"
          s3ForcePathStyle: "true"
        provider: {provider}
        default: true
        credential:
          key: cloud
          name: {credentials}
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`aws`:: Specifies that an object store plugin corresponding to your storage locations is required. For all S3 providers, the required plugin is `aws`. For {azure-short} and {gcp-short} object stores, the `azure` or `gcp` plugin is required.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` or `restic` as your uploader. You cannot change the selection after the installation. For the Built-in DataMover you must use Kopia. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia or Restic are available. By default, Kopia or Restic run on all nodes.
`region`:: Specifies the region, following the naming convention of the documentation of your object storage server.
`s3Url`:: Specifies the URL of the S3 endpoint.
`name`:: Specifies the name of the `Secret` object that you created. If you do not specify this value, the default name, `{credentials}`, is used. If you specify a custom name, the custom name is used for the backup location.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - aws
        - kubevirt
        - csi
        - openshift
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - velero:
        provider: {provider}
        default: true
        credential:
          key: cloud
          name: <default_secret>
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`aws`:: Specifies that an object store plugin corresponding to your storage locations is required. For all S3 providers, the required plugin is `aws`. For {azure-short} and {gcp-short} object stores, the `azure` or `gcp` plugin is required.
`kubevirt`:: Optional: The `kubevirt` plugin is used with {VirtProductName}.
`csi`:: Specifies the `csi` default plugin if you use CSI snapshots to back up PVs. The `csi` plugin uses the Velero CSI beta snapshot APIs. You do not need to configure a snapshot location.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` or `restic` as your uploader. You cannot change the selection after the installation. For the Built-in DataMover you must use Kopia. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia or Restic are available. By default, Kopia or Restic run on all nodes.
`provider`:: Specifies the backup provider.
`name`:: Specifies the correct default name for the `Secret`, for example, `cloud-credentials-gcp`, if you use a default plugin for the backup provider. If specifying a custom name, then the custom name is used for the backup location. If you do not specify a `Secret` name, the default name is used.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.

+
[source,yaml,subs="attributes+"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - kubevirt
        - gcp
        - csi
        - openshift
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector: <node_selector>
  backupLocations:
    - velero:
        provider: {provider}
        default: true
        credential:
          key: cloud
          name: <default_secret>
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
----
+
where:
+
`namespace`:: Specifies the default namespace for OADP which is `openshift-adp`. The namespace is a variable and is configurable.
`kubevirt`:: Specifies that the `kubevirt` plugin is mandatory for {VirtProductName}.
`gcp`:: Specifies the plugin for the backup provider, for example, `gcp`, if it exists.
`csi`:: Specifies that the `csi` plugin is mandatory for backing up PVs with CSI snapshots. The `csi` plugin uses the Velero CSI beta snapshot APIs. You do not need to configure a snapshot location.
`openshift`:: Specifies that the `openshift` plugin is mandatory.
`resourceTimeout`:: Specifies how many minutes to wait for several Velero resources such as Velero CRD availability, volumeSnapshot deletion, and backup repository availability, before timeout occurs. The default is 10m.
`nodeAgent`:: Specifies the administrative agent that routes the administrative requests to servers.
`enable`:: Set this value to `true` if you want to enable `nodeAgent` and perform File System Backup.
`uploaderType`:: Specifies the uploader type. Enter `kopia` as your uploader to use the Built-in DataMover. The `nodeAgent` deploys a daemon set, which means that the `nodeAgent` pods run on each working node. You can configure File System Backup by adding `spec.defaultVolumesToFsBackup: true` to the `Backup` CR.
`nodeSelector`:: Specifies the nodes on which Kopia are available. By default, Kopia runs on all nodes.
`provider`:: Specifies the backup provider.
`name`:: Specifies the correct default name for the `Secret`, for example, `cloud-credentials-gcp`, if you use a default plugin for the backup provider. If specifying a custom name, then the custom name is used for the backup location. If you do not specify a `Secret` name, the default name is used.
`bucket`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`prefix`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.

. Click *Create*.

.Verification

. Verify the installation by viewing the {oadp-first} resources by running the following command:
+
[source,terminal]
----
$ oc get all -n openshift-adp
----
+
----
NAME                                                     READY   STATUS    RESTARTS   AGE
pod/oadp-operator-controller-manager-67d9494d47-6l8z8    2/2     Running   0          2m8s
pod/node-agent-9cq4q                                     1/1     Running   0          94s
pod/node-agent-m4lts                                     1/1     Running   0          94s
pod/node-agent-pv4kr                                     1/1     Running   0          95s
pod/velero-588db7f655-n842v                              1/1     Running   0          95s

NAME                                                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/oadp-operator-controller-manager-metrics-service   ClusterIP   172.30.70.140    <none>        8443/TCP   2m8s
service/openshift-adp-velero-metrics-svc                   ClusterIP   172.30.10.0      <none>        8085/TCP   8h

NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/node-agent    3         3         3       3            3           <none>          96s

NAME                                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/oadp-operator-controller-manager    1/1     1            1           2m9s
deployment.apps/velero                              1/1     1            1           96s

NAME                                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/oadp-operator-controller-manager-67d9494d47    1         1         1       2m9s
replicaset.apps/velero-588db7f655                              1         1         1       96s
----

. Verify that the `DataProtectionApplication` (DPA) is reconciled by running the following command:
+
[source,terminal]
----
$ oc get dpa dpa-sample -n openshift-adp -o jsonpath='{.status}'
----
+
[source,yaml]
----
{"conditions":[{"lastTransitionTime":"2023-10-27T01:23:57Z","message":"Reconcile complete","reason":"Complete","status":"True","type":"Reconciled"}]}
----

. Verify the `type` is set to `Reconciled`.

. Verify the backup storage location and confirm that the `PHASE` is `Available` by running the following command:
+
[source,terminal]
----
$ oc get backupstoragelocations.velero.io -n openshift-adp
----
+
[source,yaml]
----
NAME           PHASE       LAST VALIDATED   AGE     DEFAULT
dpa-sample-1   Available   1s               3d16h   true
----
// include the module for setting Velero CPU and memory resource allocations
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/configuring-oadp.adoc
// * backup_and_restore/application_backup_and_restore/oadp-aws-sts/oadp-aws-sts.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-setting-resource-limits-and-requests_{context}"]
= Setting Velero CPU and memory resource allocations

[role="_abstract"]
You set the CPU and memory resource allocations for the `Velero` pod by editing the  `DataProtectionApplication` custom resource (CR) manifest.

.Prerequisites

* You must have the OpenShift API for Data Protection (OADP) Operator installed.

.Procedure

* Edit the values in the `spec.configuration.velero.podConfig.ResourceAllocations` block of the `DataProtectionApplication` CR manifest, as in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
spec:
# ...
  configuration:
    velero:
      podConfig:
        nodeSelector: <node_selector>
        resourceAllocations:
          limits:
            cpu: "1"
            memory: 1024Mi
          requests:
            cpu: 200m
            memory: 256Mi
----
+
where:
+
`nodeSelector`:: Specifies the node selector to be supplied to Velero podSpec.
`resourceAllocations`:: Specifies the resource allocations listed for average usage.
+
[NOTE]
====
Kopia is an option in OADP 1.3 and later releases. You can use Kopia for file system backups, and Kopia is your only option for Data Mover cases with the built-in Data Mover.

Kopia is more resource intensive than Restic, and you might need to adjust the CPU and memory requirements accordingly.
====
// include the node agent config module
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.adoc
// * backup_and_restore/application_backup_and_restore/oadp-api.adoc
// * virt/backup_restore/virt-backup-restore-overview.adoc

[id="oadp-configuring-node-agents_{context}"]
= Configuring node agents and node labels

[role="_abstract"]
The Data Protection Application (DPA) uses the `nodeSelector` field to select which nodes can run the node agent. The `nodeSelector` field is the recommended form of node selection constraint.

.Procedure

. Run the node agent on any node that you choose by adding a custom label:
+
[source,terminal]
----
$ oc label node/<node_name> node-role.kubernetes.io/nodeAgent=""
----
+
[NOTE]
====
Any label specified must match the labels on each node.
====

. Use the same custom label in the `DPA.spec.configuration.nodeAgent.podConfig.nodeSelector` field, which you used for labeling nodes:
+
[source,terminal]
----
configuration:
  nodeAgent:
    enable: true
    podConfig:
      nodeSelector:
        node-role.kubernetes.io/nodeAgent: ""
----
+
The following example is an anti-pattern of `nodeSelector` and does not work unless both labels, `node-role.kubernetes.io/infra: ""` and `node-role.kubernetes.io/worker: ""`, are on the node:
+
[source,terminal]
----
    configuration:
      nodeAgent:
        enable: true
        podConfig:
          nodeSelector:
            node-role.kubernetes.io/infra: ""
            node-role.kubernetes.io/worker: ""
----
// include the module for client burst and qps config

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-client-burst-qps_{context}"]
= Configuring the DPA with client burst and QPS settings

[role="_abstract"]
The burst setting determines how many requests can be sent to the `velero` server before the limit is applied. After the burst limit is reached, the queries per second (QPS) setting determines how many additional requests can be sent per second.

You can set the burst and QPS values of the `velero` server by configuring the Data Protection Application (DPA) with the burst and QPS values. You can use the `dpa.configuration.velero.client-burst` and `dpa.configuration.velero.client-qps` fields of the DPA to set the burst and QPS values.

.Prerequisites

* You have installed the {oadp-short} Operator.

.Procedure

* Configure the `client-burst` and the `client-qps` fields in the DPA as shown in the following example:
+
.Example Data Protection Application
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: test-dpa
  namespace: openshift-adp
spec:
  backupLocations:
    - name: default
      velero:
        config:
          insecureSkipTLSVerify: "true"
          profile: "default"
          region: <bucket_region>
          s3ForcePathStyle: "true"
          s3Url: <bucket_url>
        credential:
          key: cloud
          name: cloud-credentials
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: velero
        provider: aws
  configuration:
    nodeAgent:
      enable: true
      uploaderType: restic
    velero:
      client-burst: 500
      client-qps: 300
      defaultPlugins:
        - openshift
        - aws
        - kubevirt
----
+
where:
+
`client-burst`:: Specifies the `client-burst` value. In this example, the `client-burst` field is set to 500.
`client-qps`:: Specifies the `client-qps` value. In this example, the `client-qps` field is set to 300.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include module for load affinity setting

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-node-agent-load-affinity_{context}"]
= Configuring node agent load affinity

[role="_abstract"]
You can schedule the node agent pods on specific nodes by using the `spec.podConfig.nodeSelector` object of the `DataProtectionApplication` (DPA) custom resource (CR).

See the following example in which you can schedule the node agent pods on nodes with the label `label.io/role: cpu-1` and `other-label.io/other-role: cpu-2`.

[source,yaml]
----
...
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        nodeSelector:
          label.io/role: cpu-1
          other-label.io/other-role: cpu-2
        ...
----

You can add more restrictions on the node agent pods scheduling by using the `nodeagent.loadAffinity` object in the DPA spec.

.Prerequisites

* You must be logged in as a user with `cluster-admin` privileges.
* You have installed the {oadp-short} Operator.
* You have configured the DPA CR.

.Procedure

* Configure the DPA spec `nodegent.loadAffinity` object as shown in the following example.
+
In the example, you ensure that the node agent pods are scheduled only on nodes with the label `label.io/role: cpu-1` and the label `label.io/hostname` matching with either `node1` or `node2`.
+
[source,yaml]
----
...
spec:
  configuration:
    nodeAgent:
      enable: true
      loadAffinity:
        - nodeSelector:
            matchLabels:
              label.io/role: cpu-1
            matchExpressions:
              - key: label.io/hostname
                operator: In
                values:
                  - node1
                  - node2
                  ...
----
+
where:
+
`loadAffinity`:: Specifies the `loadAffinity` object by adding the `matchLabels` and `matchExpressions` objects.
`matchExpressions`:: Specifies the `matchExpressions` object to add restrictions on the node agent pods scheduling.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include module for load affinity guidelines
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-node-agent-load-affinity-guidelines_{context}"]
= Node agent load affinity guidelines

[role="_abstract"]
Use the following guidelines to configure the node agent `loadAffinity` object in the `DataProtectionApplication` (DPA) custom resource (CR).

* Use the `spec.nodeagent.podConfig.nodeSelector` object for simple node matching.
* Use the `loadAffinity.nodeSelector` object without the `podConfig.nodeSelector` object for more complex scenarios.
* You can use both `podConfig.nodeSelector` and `loadAffinity.nodeSelector` objects, but the `loadAffinity` object must be equal or more restrictive as compared to the `podConfig` object. In this scenario, the `podConfig.nodeSelector` labels must be a subset of the labels used in the `loadAffinity.nodeSelector` object.
* You cannot use the `matchExpressions` and `matchLabels` fields if you have configured both `podConfig.nodeSelector` and `loadAffinity.nodeSelector` objects in the DPA.
* See the following example to configure both `podConfig.nodeSelector` and `loadAffinity.nodeSelector` objects in the DPA.
+
[source,yaml]
----
...
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
      loadAffinity:
        - nodeSelector:
            matchLabels:
              label.io/location: 'US'
              label.io/gpu: 'no'
      podConfig:
        nodeSelector:
          label.io/gpu: 'no'
----
// include module for loadConcurrency setting

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-node-agent-load-concurrency_{context}"]
= Configuring node agent load concurrency

[role="_abstract"]
You can control the maximum number of node agent operations that can run simultaneously on each node within your cluster.

You can configure it using one of the following fields of the Data Protection Application (DPA):

* `globalConfig`: Defines a default concurrency limit for the node agent across all nodes.
* `perNodeConfig`: Specifies different concurrency limits for specific nodes based on `nodeSelector` labels. This provides flexibility for environments where certain nodes might have different resource capacities or roles.

.Prerequisites
* You must be logged in as a user with `cluster-admin` privileges.

.Procedure

. If you want to use load concurrency for specific nodes, add labels to those nodes:
+
[source,terminal]
----
$ oc label node/<node_name> label.io/instance-type='large'
----

. Configure the load concurrency fields for your DPA instance:
+
[source,yaml]
----
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
      loadConcurrency:
        globalConfig: 1
        perNodeConfig:
        - nodeSelector:
              matchLabels:
                 label.io/instance-type: large
          number: 3
----
+
where:
+
`globalConfig`:: Specifies the global concurrent number. The default value is 1, which means there is no concurrency and only one load is allowed. The `globalConfig` value does not have a limit.
`label.io/instance-type`:: Specifies the label for per-node concurrency.
`number`:: Specifies the per-node concurrent number. You can specify many per-node concurrent numbers, for example, based on the instance type and size. The range of per-node concurrent number is the same as the global concurrent number. If the configuration file contains a per-node concurrent number and a global concurrent number, the per-node concurrent number takes precedence.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include module for repo maintenance setting

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-repository-maintenance_{context}"]
= Configuring repository maintenance

[role="_abstract"]
{oadp-short} repository maintenance is a background job, you can configure it independently of the node agent pods. This means that you can schedule the repository maintenance pod on a node where the node agent is or is not running.

You can use the repository maintenance job affinity configurations in the `DataProtectionApplication` (DPA) custom resource (CR) only if you use Kopia as the backup repository.

You have the option to configure the load affinity at the global level affecting all repositories. Or you can configure the load affinity for each repository. You can also use a combination of global and per-repository configuration.

.Prerequisites

* You must be logged in as a user with `cluster-admin` privileges.
* You have installed the {oadp-short} Operator.
* You have configured the DPA CR.

.Procedure

* Configure the `loadAffinity` object in the DPA spec by using either one or both of the following methods:
** Global configuration: Configure load affinity for all repositories as shown in the following example:
+
[source,yaml]
----
...
spec:
  configuration:
    repositoryMaintenance:
      global:
        podResources:
          cpuRequest: "100m"
          cpuLimit: "200m"
          memoryRequest: "100Mi"
          memoryLimit: "200Mi"
        loadAffinity:
          - nodeSelector:
              matchLabels:
                label.io/gpu: 'no'
              matchExpressions:
                - key: label.io/location
                  operator: In
                  values:
                    - US
                    - EU
----
+
where:
+
`repositoryMaintenance`:: Specifies the `repositoryMaintenance` object as shown in the example.
`global`:: Specifies the `global` object to configure load affinity for all repositories.

** Per-repository configuration: Configure load affinity per repository as shown in the following example:
+
[source,yaml]
----
...
spec:
  configuration:
    repositoryMaintenance:
      myrepositoryname:
        loadAffinity:
          - nodeSelector:
              matchLabels:
                label.io/cpu: 'yes'
----
+
where:
+
`myrepositoryname`:: Specifies the `repositoryMaintenance` object for each repository.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include module for velero load affinity setting
// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-velero-load-affinity_{context}"]
= Configuring Velero load affinity

[role="_abstract"]
With each {oadp-short} deployment, there is one Velero pod and its main purpose is to schedule Velero workloads. To schedule the Velero pod, you can use the `velero.podConfig.nodeSelector` and the `velero.loadAffinity` objects in the `DataProtectionApplication` (DPA) custom resource (CR) spec.

Use the `podConfig.nodeSelector` object to assign the Velero pod to specific nodes. You can also configure the `velero.loadAffinity` object for pod-level affinity and anti-affinity.

The OpenShift scheduler applies the rules and performs the scheduling of the Velero pod deployment.

.Prerequisites

* You must be logged in as a user with `cluster-admin` privileges.
* You have installed the {oadp-short} Operator.
* You have configured the DPA CR.

.Procedure

* Configure the `velero.podConfig.nodeSelector` and the `velero.loadAffinity` objects in the DPA spec as shown in the following examples:
** `velero.podConfig.nodeSelector` object configuration:
+
[source,yaml]
----
...
spec:
  configuration:
    velero:
      podConfig:
        nodeSelector:
          some-label.io/custom-node-role: backup-core
----

** `velero.loadAffinity` object configuration:
+
[source,yaml]
----
...
spec:
  configuration:
    velero:
      loadAffinity:
        - nodeSelector:
            matchLabels:
              label.io/gpu: 'no'
            matchExpressions:
              - key: label.io/location
                operator: In
                values:
                  - US
                  - EU
----

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include module for image pull policy setting

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-imagepullpolicy_{context}"]
= Overriding the imagePullPolicy setting in the DPA

[role="_abstract"]
In {oadp-short} 1.4.0 or earlier, the Operator sets the `imagePullPolicy` field of the Velero and node agent pods to `Always` for all images.

In {oadp-short} 1.4.1 or later, the Operator first checks if each image has the `sha256` or `sha512` digest and sets the `imagePullPolicy` field accordingly:

* If the image has the digest, the Operator sets `imagePullPolicy` to `IfNotPresent`.
* If the image does not have the digest, the Operator sets `imagePullPolicy` to `Always`.

You can also override the `imagePullPolicy` field by using the `spec.imagePullPolicy` field in the Data Protection Application (DPA).

.Prerequisites

* You have installed the {oadp-short} Operator.

.Procedure

* Configure the `spec.imagePullPolicy` field in the DPA as shown in the following example:
+
.Example Data Protection Application
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: test-dpa
  namespace: openshift-adp
spec:
  backupLocations:
    - name: default
      velero:
        config:
          insecureSkipTLSVerify: "true"
          profile: "default"
          region: <bucket_region>
          s3ForcePathStyle: "true"
          s3Url: <bucket_url>
        credential:
          key: cloud
          name: cloud-credentials
        default: true
        objectStorage:
          bucket: <bucket_name>
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
        - kubevirt
        - csi
  imagePullPolicy: Never
----
+
where:
+
`imagePullPolicy`:: Specifies the value for `imagePullPolicy`. In this example, the `imagePullPolicy` field is set to `Never`.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.
// include the module for configuring multiple BSL
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
// include the module for disabling node agent in the DPA

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-about-disable-node-agent-dpa_{context}"]
= Disabling the node agent in DataProtectionApplication

[role="_abstract"]
If you are not using `Restic`, `Kopia`, or `DataMover` for your backups, you can disable the `nodeAgent` field in the `DataProtectionApplication` custom resource (CR). Before you disable `nodeAgent`, ensure the {oadp-short} Operator is idle and not running any backups.

.Procedure

. To disable the `nodeAgent`, set the `enable` flag to `false`. See the following example:
+
.Example `DataProtectionApplication` CR
[source, yaml]
----
# ...
configuration:
  nodeAgent:
    enable: false
    uploaderType: kopia
# ...
----
+
where:
+
`enable`:: Enables the node agent.

. To enable the `nodeAgent`, set the `enable` flag to `true`. See the following example:
+
.Example `DataProtectionApplication` CR
[source, yaml]
----
# ...
configuration:
  nodeAgent:
    enable: true
    uploaderType: kopia
# ...
----
+
where:
+
`enable`:: Enables the node agent.
+
You can set up a job to enable and disable the `nodeAgent` field in the `DataProtectionApplication` CR. For more information, see "Running tasks in pods using jobs".
