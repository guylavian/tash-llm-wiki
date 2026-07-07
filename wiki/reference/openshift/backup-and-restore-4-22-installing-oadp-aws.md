---
title: "Configuring the OpenShift API for Data Protection with AWS S3 compatible storage"
type: reference
domain: openshift
slug: backup-and-restore-4-22-installing-oadp-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/installing-oadp-aws
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Configuring the OpenShift API for Data Protection with AWS S3 compatible storage

[id="installing-oadp-aws"]
= Configuring the OpenShift API for Data Protection with AWS S3 compatible storage

[role="_abstract"]
Install the {oadp-first} with Amazon Web Services (AWS) S3 compatible storage by installing the {oadp-short} Operator. The Operator installs Velero {velero-version}.

You configure AWS for Velero, create a default `Secret`, and then install the Data Protection Application. For more details, see _Installing the OADP Operator_.

To install the OADP Operator in a restricted network environment, you must first disable the default software catalog sources and mirror the Operator catalog. See _Using Operator Lifecycle Manager in disconnected environments_ for details.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-s3-and-gov-cloud_{context}"]
= About Amazon Simple Storage Service, Identity and Access Management, and GovCloud

[role="_abstract"]
Review Amazon Simple Storage Service (S3), Identity and Access Management (IAM), and AWS GovCloud requirements to configure backup storage with appropriate security controls. This helps you meet federal data security requirements and use correct endpoints.

{aws-short} S3 is a storage solution of Amazon for the internet. As an authorized user, you can use this service to store and retrieve any amount of data whenever you want, from anywhere on the web.

You securely control access to Amazon S3 and other Amazon services by using the AWS Identity and Access Management (IAM) web service.

You can use IAM to manage permissions that control which AWS resources users can access. You use IAM to both authenticate, or verify that a user is who they claim to be, and to authorize, or grant permissions to use resources.

AWS GovCloud (US) is an Amazon storage solution developed to meet the stringent and specific data security requirements of the United States Federal Government. AWS GovCloud (US) works the same as Amazon S3 except for the following:

* You cannot copy the contents of an Amazon S3 bucket in the AWS GovCloud (US) regions directly to or from another AWS region.
* If you use Amazon S3 policies, use the AWS GovCloud (US) Amazon Resource Name (ARN) identifier to unambiguously specify a resource  across all of AWS, such as in IAM policies, Amazon S3 bucket names, and API calls.

** In AWS GovCloud (US) regions, ARNs have an identifier that is different from the one in other standard AWS regions, `arn:aws-us-gov`. If you need to specify the US-West or US-East region, use one the following ARNs:

*** For US-West, use `us-gov-west-1`.
*** For US-East, use `us-gov-east-1`.

** For all other standard regions, ARNs begin with: `arn:aws`.

* In AWS GovCloud (US) regions, use the endpoints listed in the *AWS GovCloud (US-East)* and *AWS GovCloud (US-West)* rows of the "Amazon S3 endpoints" table. If you are processing export-controlled data, use one of the SSL/TLS endpoints. If you have FIPS requirements, use a FIPS 140-2 endpoint such as `\https://s3-fips.us-gov-west-1.amazonaws.com` or `\https://s3-fips.us-gov-east-1.amazonaws.com`.
* To find other AWS-imposed restrictions, see the AWS documentation.

[role="_additional-resources"]
== Additional resources

* Amazon Simple Storage Service endpoints and quotas ({aws-short} documentation)
* How Amazon Simple Storage Service Differs for AWS GovCloud (US) ({aws-short} documentation)

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="migration-configuring-aws-s3_{context}"]
= Configuring Amazon Web Services

[role="_abstract"]
Configure Amazon Web Services (AWS) S3 storage and Identity and Access Management (IAM) credentials for backup storage with {oadp-short}. This provides the necessary permissions and storage infrastructure for data protection operations.

.Prerequisites

* You must have the AWS CLI installed.

.Procedure

. Set the `BUCKET` variable:
+
[source,terminal]
----
$ BUCKET=<your_bucket>
----

. Set the `REGION` variable:
+
[source,terminal]
----
$ REGION=<your_region>
----

. Create an AWS S3 bucket:
+
[source,terminal]
----
$ aws s3api create-bucket \
    --bucket $BUCKET \
    --region $REGION \
    --create-bucket-configuration LocationConstraint=$REGION
----
+
where:
+
`LocationConstraint`:: Specifies the bucket configuration location constraint. `us-east-1` does not support `LocationConstraint`. If your region is `us-east-1`, omit `--create-bucket-configuration LocationConstraint=$REGION`.

. Create an IAM user:
+
[source,terminal]
----
$ aws iam create-user --user-name velero
----
+
where:
+
`velero`:: Specifies the user name. If you want to use Velero to back up multiple clusters with multiple S3 buckets, create a unique user name for each cluster.

. Create a `velero-policy.json` file:
+
[source,terminal]
----
$ cat > velero-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVolumes",
                "ec2:DescribeSnapshots",
                "ec2:CreateTags",
                "ec2:CreateVolume",
                "ec2:CreateSnapshot",
                "ec2:DeleteSnapshot"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::${BUCKET}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::${BUCKET}"
            ]
        }
    ]
}
EOF
----

. Attach the policies to give the `velero` user the minimum necessary permissions:
+
[source,terminal]
----
$ aws iam put-user-policy \
  --user-name velero \
  --policy-name velero \
  --policy-document file://velero-policy.json
----

. Create an access key for the `velero` user:
+
[source,terminal]
----
$ aws iam create-access-key --user-name velero
----
+
[source,terminal]
----
{
  "AccessKey": {
        "UserName": "velero",
        "Status": "Active",
        "CreateDate": "2017-07-31T22:24:41.576Z",
        "SecretAccessKey": <AWS_SECRET_ACCESS_KEY>,
        "AccessKeyId": <AWS_ACCESS_KEY_ID>
  }
}
----
. Create a `credentials-velero` file:
+
[source,terminal,subs="attributes+"]
----
$ cat << EOF > ./credentials-velero
[default]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
EOF
----
+
You use the `credentials-velero` file to create a `Secret` object for AWS before you install the Data Protection Application.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-about-backup-snapshot-locations_{context}"]
= About backup and snapshot locations and their secrets

[role="_abstract"]
Review backup location, snapshot location, and secret configuration requirements for the `DataProtectionApplication` custom resource (CR). This helps you understand storage options and credential management for data protection operations.

[id="backup-locations_{context}"]
== Backup locations

You can specify one of the following AWS S3-compatible object storage solutions as a backup location:

* Multicloud Object Gateway (MCG)
* Red{nbsp}Hat Container Storage
* Ceph RADOS Gateway; also known as Ceph Object Gateway
* {odf-full}
* MinIO

Velero backs up OpenShift Container Platform resources, Kubernetes objects, and internal images as an archive file on object storage.

[id="snapshot-locations_{context}"]
== Snapshot locations

If you use your cloud provider's native snapshot API to back up persistent volumes, you must specify the cloud provider as the snapshot location.

If you use Container Storage Interface (CSI) snapshots, you do not need to specify a snapshot location because you will create a `VolumeSnapshotClass` CR to register the CSI driver.

If you use File System Backup (FSB), you do not need to specify a snapshot location because FSB backs up the file system on object storage.

[id="secrets_{context}"]
== Secrets

If the backup and snapshot locations use the same credentials or if you do not require a snapshot location, you create a default `Secret`.

If the backup and snapshot locations use different credentials, you create two secret objects:

* Custom `Secret` for the backup location, which you specify in the `DataProtectionApplication` CR.
* Default `Secret` for the snapshot location, which is not referenced in the `DataProtectionApplication` CR.

[IMPORTANT]
====
The Data Protection Application requires a default `Secret`. Otherwise, the installation will fail.

If you do not want to specify backup or snapshot locations during the installation, you can create a default `Secret` with an empty `credentials-velero` file.
====

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-aws-secrets-for-different-credentials_{context}"]
= Creating profiles for different credentials

[role="_abstract"]
If your backup and snapshot locations use different credentials, you create separate profiles in the `credentials-velero` file.

Then, you create a `Secret` object and specify the profiles in the `DataProtectionApplication` custom resource (CR).

.Procedure

. Create a `credentials-velero` file with separate profiles for the backup and snapshot locations, as in the following example:
+
[source,terminal]
----
[backupStorage]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>

[volumeSnapshot]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
----

. Create a `Secret` object with the `credentials-velero` file:
+
[source,terminal,subs="attributes+"]
----
$ oc create secret generic {credentials} -n openshift-adp --from-file cloud=credentials-velero <1>
----

. Add the profiles to the `DataProtectionApplication` CR, as in the following example:
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
    - name: default
      velero:
        provider: {provider}
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
        config:
          region: us-east-1
          profile: "backupStorage"
        credential:
          key: cloud
          name: {credentials}
  snapshotLocations:
    - velero:
        provider: {provider}
        config:
          region: us-west-2
          profile: "volumeSnapshot"
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-ssec-encrypted-backups_{context}"]
= Creating an OADP SSE-C encryption key for additional data security

[role="_abstract"]
Configure server-side encryption with customer-provided keys (SSE-C) to add an additional layer of encryption for backup data stored in {aws-first} S3. This protects backup data if AWS credentials become exposed.

{aws-first} S3 applies server-side encryption with {aws-short} S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3.

{oadp-first} encrypts data by using SSL/TLS, HTTPS, and the `velero-repo-credentials` secret when transferring the data from a cluster to storage. To protect backup data in case of lost or stolen AWS credentials, apply an additional layer of encryption.

The velero-plugin-for-aws plugin provides several additional encryption methods. You should review its configuration options and consider implementing additional encryption.

You can store your own encryption keys by using server-side encryption with customer-provided keys (SSE-C). This feature provides additional security if your AWS credentials become exposed.

[WARNING]
====
Be sure to store cryptographic keys in a secure and safe manner. Encrypted data and backups cannot be recovered if you do not have the encryption key.
====

.Prerequisites

* To make {oadp-short} mount a secret that contains your SSE-C key to the Velero pod at `/credentials`, use the following default secret name for AWS: `cloud-credentials`, and leave at least one of the following labels empty:

** `dpa.spec.backupLocations[].velero.credential`
** `dpa.spec.snapshotLocations[].velero.credential`
+
This is a workaround for a known issue: https://issues.redhat.com/browse/OADP-3971.

[NOTE]
====
The following procedure contains an example of a `spec:backupLocations` block that does not specify credentials. This example would trigger an OADP secret mounting.
====

* If you need the backup location to have credentials with a different name than `cloud-credentials`, you must add a snapshot location, such as the one in the following example, that does not contain a credential name. Because the following example does not contain a credential name, the snapshot location will use `cloud-credentials` as its secret for taking snapshots.
+
[source,yaml]
----
 snapshotLocations:
  - velero:
      config:
        profile: default
        region: <region>
      provider: aws
# ...
----

.Procedure
. Create an SSE-C encryption key:

.. Generate a random number and save it as a file named `sse.key` by running the following command:
+
[source,terminal]
----
$ dd if=/dev/urandom bs=1 count=32 > sse.key
----

. Create an OpenShift Container Platform secret:
** If you are initially installing and configuring {oadp-short}, create the AWS credential and encryption key secret at the same time by running the following command:
+
[source,terminal]
----
$ oc create secret generic cloud-credentials --namespace openshift-adp --from-file cloud=<path>/openshift_aws_credentials,customer-key=<path>/sse.key
----
** If you are updating an existing installation, edit the values of the `cloud-credential` `secret` block of the `DataProtectionApplication` CR manifest, as in the following example:
+
[source,yaml]
----
apiVersion: v1
data:
  cloud: W2Rfa2V5X2lkPSJBS0lBVkJRWUIyRkQ0TlFHRFFPQiIKYXdzX3NlY3JldF9hY2Nlc3Nfa2V5P<snip>rUE1mNWVSbTN5K2FpeWhUTUQyQk1WZHBOIgo=
  customer-key: v+<snip>TFIiq6aaXPbj8dhos=
kind: Secret
# ...
----
. Edit the value of the `customerKeyEncryptionFile` attribute in the `backupLocations` block of the `DataProtectionApplication` CR manifest, as in the following example:
+
[source,yaml]
----
spec:
  backupLocations:
    - velero:
        config:
          customerKeyEncryptionFile: /credentials/customer-key
          profile: default
# ...
----
+
[WARNING]
====
You must restart the Velero pod to remount the secret credentials properly on an existing installation.
====
+
The installation is complete, and you can back up and restore OpenShift Container Platform resources. The data saved in AWS S3 storage is encrypted with the new key, and you cannot download it from the AWS S3 console or API without the additional encryption key.

.Verification

To verify that you cannot download the encrypted files without the inclusion of an additional key, create a test file, upload it, and then try to download it.

. Create a test file by running the following command:
+
[source,terminal]
----
$ echo "encrypt me please" > test.txt
----
. Upload the test file by running the following command:
+
[source,terminal]
----
$ aws s3api put-object \
  --bucket <bucket> \
  --key test.txt \
  --body test.txt \
  --sse-customer-key fileb://sse.key \
  --sse-customer-algorithm AES256
----
. Try to download the file. In either the Amazon web console or the terminal, run the following command:
+
[source,terminal]
----
$ s3cmd get s3://<bucket>/test.txt test.txt
----
+
The download fails because the file is encrypted with an additional key.

. Download the file with the additional encryption key by running the following command:
+
[source,terminal]
----
$ aws s3api get-object \
    --bucket <bucket> \
    --key test.txt \
    --sse-customer-key fileb://sse.key \
    --sse-customer-algorithm AES256 \
    downloaded.txt
----

. Read the file contents by running the following command:
+
[source,terminal]
----
$ cat downloaded.txt
----
+
[source,terminal]
----
encrypt me please
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-ssec-encrypted-backups-velero_{context}"]
= Downloading a file with an SSE-C encryption key for files backed up by Velero

[role="_abstract"]
When you are verifying an SSE-C encryption key, you can also download the file with the additional encryption key for files that were backed up with Velero.

.Procedure

* Download the file with the additional encryption key for files backed up by Velero by running the following command:
+
[source,terminal]
----
$ aws s3api get-object \
  --bucket <bucket> \
  --key velero/backups/mysql-persistent-customerkeyencryptionfile4/mysql-persistent-customerkeyencryptionfile4.tar.gz \
  --sse-customer-key fileb://sse.key \
  --sse-customer-algorithm AES256 \
  --debug \
  velero_download.tar.gz
----

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/configuring-oadp.adoc

[id="oadp-self-signed-certificate_{context}"]
= Enabling self-signed CA certificates

[role="_abstract"]
You must enable a self-signed CA certificate for object storage by editing the `DataProtectionApplication` custom resource (CR) manifest to prevent a `certificate signed by unknown authority` error.

.Prerequisites

* You must have the OpenShift API for Data Protection (OADP) Operator installed.

.Procedure

* Edit the `spec.backupLocations.velero.objectStorage.caCert` parameter and `spec.backupLocations.velero.config` parameters of the `DataProtectionApplication` CR manifest:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_sample>
spec:
# ...
  backupLocations:
    - name: default
      velero:
        provider: aws
        default: true
        objectStorage:
          bucket: <bucket>
          prefix: <prefix>
          caCert: <base64_encoded_cert_string>
        config:
          insecureSkipTLSVerify: "false"
# ...
----
+
where:
+
`caCert`:: Specifies the Base64-encoded CA certificate string.
`insecureSkipTLSVerify`:: Specifies the `insecureSkipTLSVerify` configuration. The configuration can be set to either `"true"` or `"false"`. If set to `"true"`, SSL/TLS security is disabled. If set to `"false"`, SSL/TLS security is enabled.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-using-ca-certificates-with-velero-command-aliased-for-velero-deployment_{context}"]
= Using CA certificates with the velero command aliased for Velero deployment

[role="_abstract"]
You might want to use the Velero CLI without installing it locally on your system by creating an alias for it.

.Prerequisites

* You must be logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* You must have the OpenShift CLI (`oc`) installed.

.Procedure

. To use an aliased Velero command, run the following command:
+
[source,terminal]
----
$ alias velero='oc -n openshift-adp exec deployment/velero -c velero -it -- ./velero'
----

. Check that the alias is working by running the following command:
+
[source,terminal]
----
$ velero version
----
+
[source,terminal]
----
Client:
	Version: v1.12.1-OADP
	Git commit: -
Server:
	Version: v1.12.1-OADP
----

. To use a CA certificate with this command, you can add a certificate to the Velero deployment by running the following commands:
+
[source,terminal]
----
$ CA_CERT=$(oc -n openshift-adp get dataprotectionapplications.oadp.openshift.io <dpa-name> -o jsonpath='{.spec.backupLocations[0].velero.objectStorage.caCert}')
----
+
[source,terminal]
----
$ [[ -n $CA_CERT ]] && echo "$CA_CERT" | base64 -d | oc exec -n openshift-adp -i deploy/velero -c velero -- bash -c "cat > /tmp/your-cacert.txt" || echo "DPA BSL has no caCert"
----
+
[source,terminal]
----
$ velero describe backup <backup_name> --details --cacert /tmp/<your_cacert>.txt
----

. To fetch the backup logs, run the following command:
+
[source,terminal]
----
$ velero backup logs  <backup_name>  --cacert /tmp/<your_cacert.txt>
----
+
You can use these logs to view failures and warnings for the resources that you cannot back up.

. If the Velero pod restarts, the `/tmp/your-cacert.txt` file disappears, and you must re-create the `/tmp/your-cacert.txt` file by re-running the commands from the previous step.

. You can check if the `/tmp/your-cacert.txt` file still exists, in the file location where you stored it, by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-adp -i deploy/velero -c velero -- bash -c "ls /tmp/your-cacert.txt"
/tmp/your-cacert.txt
----
+
In a future release of OpenShift API for Data Protection (OADP), we plan to mount the certificate to the Velero pod so that this step is not required.

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc

[id="oadp-configuring-aws-md5sum_{context}"]
= Configuring the backup storage location with a MD5 checksum algorithm

[role="_abstract"]
You can configure the Backup Storage Location (BSL) in the Data Protection Application (DPA) to use a MD5 checksum algorithm for both Amazon Simple Storage Service (Amazon S3) and S3-compatible storage providers. The checksum algorithm calculates the checksum for uploading and downloading objects to Amazon S3. You can use one of the following options to set the `checksumAlgorithm` field in the `spec.backupLocations.velero.config.checksumAlgorithm` section of the DPA.

* `CRC32`
* `CRC32C`
* `SHA1`
* `SHA256`

You can also set the `checksumAlgorithm` field to an empty value to skip the MD5 checksum check. If you do not set a value for the `checksumAlgorithm` field, then the default value is set to `CRC32`.

.Prerequisites

* You have installed the {oadp-short} Operator.
* You have configured Amazon S3, or S3-compatible object storage as a backup location.

.Procedure

* Configure the BSL in the DPA as shown in the following example:
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
        checksumAlgorithm: ""
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
    velero:
      defaultPlugins:
      - openshift
      - aws
      - csi
----
+
where:
+
`checksumAlgorithm`:: Specifies the `checksumAlgorithm`. In this example, the `checksumAlgorithm` field is set to an empty value. You can select an option from the following list: `CRC32`, `CRC32C`, `SHA1`, `SHA256`.

+
[IMPORTANT]
====
If you are using Noobaa as the object storage provider, and you do not set the `spec.backupLocations.velero.config.checksumAlgorithm` field in the DPA, an empty value of `checksumAlgorithm` is added to the BSL configuration.

The empty value is only added for BSLs that are created using the DPA. This value is not added if you create the BSL by using any other method.
====

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.adoc

[id="oadp-configuring-node-agent-non-root_{context}"]
= Configuring the node agent as a non-root and non-privileged user

[role="_abstract"]
To enhance the node agent security, you can configure the {oadp-short} Operator node agent daemonset to run as a non-root and non-privileged user by using the `spec.configuration.velero.disableFsBackup` setting in the `DataProtectionApplication` (DPA) custom resource (CR).

By setting the `spec.configuration.velero.disableFsBackup` setting to `true`, the node agent security context sets the root file system to read-only and sets the `privileged` flag to `false`.

[NOTE]
====
Setting `spec.configuration.velero.disableFsBackup` to `true` enhances the node agent security by removing the need for privileged containers and enforcing a read-only root file system.

However, it also disables File System Backup (FSB) with Kopia. If your workloads rely on FSB for backing up volumes that do not support native snapshots, then you should evaluate whether the `disableFsBackup` configuration fits your use case.
====

.Prerequisites

* You have installed the {oadp-short} Operator.

.Procedure

* Configure the `disableFsBackup` field in the DPA as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
  namespace: openshift-adp
spec:
  backupLocations:
  - velero:
      credential:
        key: cloud
        name: cloud-credentials
      default: true
      objectStorage:
        bucket: <bucket_name>
        prefix: velero
      provider: gcp
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
      - csi
      - gcp
      - openshift
      disableFsBackup: true
----
+
where:
+
`nodeAgent`:: Specifies to enable the node agent in the DPA.
`disableFsBackup`:: Specifies to set the `disableFsBackup` field to `true`.

.Verification

. Verify that the node agent security context is set to run as non-root and the root file system is `readOnly` by running the following command:
+
[source,terminal]
----
$ oc get daemonset node-agent -o yaml
----
+
The example output is as following:
+
[source,yaml]
----
apiVersion: apps/v1
kind: DaemonSet
metadata:
  ...
  name: node-agent
  namespace: openshift-adp
  ...
spec:
  ...
  template:
    metadata:
      ...
    spec:
      containers:
      ...
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          privileged: false
          readOnlyRootFilesystem: true
        ...
      nodeSelector:
        kubernetes.io/os: linux
      os:
        name: linux
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      serviceAccount: velero
      serviceAccountName: velero
      ....
----
+
where:
+
`allowPrivilegeEscalation`:: Specifies that the `allowPrivilegeEscalation` field is false.
`privileged`:: Specifies that the `privileged` field is false.
`readOnlyRootFilesystem`:: Specifies that the root file system is read-only.
`runAsNonRoot`:: Specifies that the node agent is run as a non-root user.

// end of module. Need to add this comment because the level offset attribute does not get unset at the end of this module due to the continuation plus symbol. Causing the level offset from this module to stack on to the next module. This causes build failures or deeply nested modules.

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.adoc

[id="oadp-configuring-priority-class_{context}"]
= Configuring a priority class for node agent and Velero pods

[role="_abstract"]
Configure a `priorityClassName` field for the node agent and Velero pods by editing the `DataProtectionApplication` (DPA) custom resource (CR). This helps you ensure that the Kubernetes scheduler prioritizes {oadp-short} pods during resource contention.

By setting a priority class, you ensure that critical {oadp-short} pods are scheduled first after events such as worker node outages, when user workloads might otherwise consume available resources.

.Prerequisites

* The {oadp-short} Operator is installed.
* A DPA CR is configured.
* A `PriorityClass` object is created in the cluster.

.Procedure

. In your DPA CR, configure the `priorityClassName` field for the node agent, Velero, or both, in the `podConfig` object as shown in the following example:
+
[source,yaml,subs="+quotes"]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: <dpa_name>
  namespace: openshift-adp
spec:
# ...
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        priorityClassName: <priority_class_name>
    velero:
      podConfig:
        priorityClassName: <priority_class_name>
----
+
where:
`<priority_class_name>`:: Specifies the name of an existing `PriorityClass` to apply to the pods managed by this `podConfig` object. For example, `system-cluster-critical`.

. Apply the `DataProtectionApplication` CR by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f <dpa_file_name>
----

.Verification

. Verify that the node agent daemon set pods have the correct priority class by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-adp -l name=node-agent -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.spec.priorityClassName}{"\n"}{end}'
----
+
[source,terminal]
----
node-agent-xxxxx <priority_class_name>
node-agent-yyyyy <priority_class_name>
----

. Verify that the Velero deployment pods have the correct priority class by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-adp -l app.kubernetes.io/name=velero -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.spec.priorityClassName}{"\n"}{end}'
----
+
[source,terminal]
----
velero-xxxxx <priority_class_name>
----

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

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-enabling-csi-dpa_{context}"]
= Enabling CSI in the DataProtectionApplication CR

[role="_abstract"]
You enable the Container Storage Interface (CSI) in the `DataProtectionApplication` custom resource (CR) in order to back up persistent volumes with CSI snapshots.

.Prerequisites

* The cloud provider must support CSI snapshots.

.Procedure

* Edit the `DataProtectionApplication` CR, as in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
spec:
  configuration:
    velero:
      defaultPlugins:
      - openshift
      - csi
----
+
where:
+
`csi`:: Specifies the `csi` default plugin.

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

[role="_additional-resources"]
.Additional resources

* Installing the OADP Operator

* Velero {velero-version}

* Using Operator Lifecycle Manager in disconnected environments

* Installing the Data Protection Application with the `kubevirt` and `openshift` plugins

* Running tasks in pods using jobs
