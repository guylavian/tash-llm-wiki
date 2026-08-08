---
title: "Backing up applications on AWS STS using OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-aws-sts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-aws-sts
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up applications on AWS STS using OADP

[id="oadp-aws-sts"]
= Backing up applications on AWS STS using OADP

[role="_abstract"]
Install the {oadp-first} with {aws-first} by installing the OADP Operator. The Operator installs {velero-link}.

You configure {aws-short} for Velero, create a default `Secret`, and then install the Data Protection Application. For more details, see _Installing the OADP Operator_.

To install the OADP Operator in a restricted network environment, you must first disable the default software catalog sources and mirror the Operator catalog. See _Using Operator Lifecycle Manager in disconnected environments_.

You can install {oadp-short} on an AWS {sts-first} (AWS STS) cluster manually. Amazon {aws-short} provides {aws-short} STS as a web service that enables you to request temporary, limited-privilege credentials for users. You use STS to provide trusted users with temporary access to resources via API calls, your {aws-short} console, or the {aws-short} command-line interface (CLI).

Before installing {oadp-first}, you must set up role and policy credentials for {oadp-short} so that it can use the {aws-full} API.

This process is performed in the following two stages:

. Prepare {aws-short} credentials.
. Install the OADP Operator and give it an IAM role.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-aws-sts/oadp-aws-sts.adoc

[id="preparing-aws-sts-credentials-for-oadp_{context}"]
= Preparing AWS STS credentials for OADP

[role="_abstract"]
Configure an {aws-full} account to install the {oadp-first}. Prepare the {aws-short} credentials by using the following procedure.

.Procedure

. Define the `cluster_name` environment variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_NAME= <AWS_cluster_name>
----
+
Replace `<AWS_cluster_name>` with the name of the cluster.

. Retrieve all of the details of the `cluster` such as the `AWS_ACCOUNT_ID, OIDC_ENDPOINT` by running the following command:
+
[source,terminal]
----
$ export CLUSTER_VERSION=$(oc get clusterversion version -o jsonpath='{.status.desired.version}{"\n"}')
----
+
[source,terminal]
----
$ export AWS_CLUSTER_ID=$(oc get clusterversion version -o jsonpath='{.spec.clusterID}{"\n"}')
----
+
[source,terminal]
----
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o jsonpath='{.spec.serviceAccountIssuer}' | sed 's|^https://||')
----
+
[source,terminal]
----
$ export REGION=$(oc get infrastructures cluster -o jsonpath='{.status.platformStatus.aws.region}' --allow-missing-template-keys=false || echo us-east-2)
----
+
[source,terminal]
----
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
----
+
[source,terminal]
----
$ export ROLE_NAME="${CLUSTER_NAME}-openshift-oadp-aws-cloud-credentials"
----

. Create a temporary directory to store all of the files by running the following command:
+
[source,terminal]
----
$ export SCRATCH="/tmp/${CLUSTER_NAME}/oadp"
mkdir -p ${SCRATCH}
----

. Display all of the gathered details by running the following command:
+
[source,terminal]
----
$ echo "Cluster ID: ${AWS_CLUSTER_ID}, Region: ${REGION}, OIDC Endpoint:
${OIDC_ENDPOINT}, AWS Account ID: ${AWS_ACCOUNT_ID}"
----

. On the {aws-short} account, create an IAM policy to allow access to {aws-short} S3:
+
.. Check to see if the policy exists by running the following commands:
+
[source,terminal]
----
$ export POLICY_NAME="OadpVer1"
----
+
--
* `POLICY_NAME`: The variable can be set to any value.
--
+
[source,terminal]
----
$ POLICY_ARN=$(aws iam list-policies --query "Policies[?PolicyName=='$POLICY_NAME'].{ARN:Arn}" --output text)
----
+
..  Enter the following command to create the policy JSON file and then create the policy:
+
[NOTE]
====
If the policy ARN is not found, the command creates the policy. If the policy ARN already exists, the `if` statement intentionally skips the policy creation.
====
+
[source,terminal]
----
$ if [[ -z "${POLICY_ARN}" ]]; then
cat << EOF > ${SCRATCH}/policy.json
{
"Version": "2012-10-17",
"Statement": [
 {
   "Effect": "Allow",
   "Action": [
     "s3:CreateBucket",
     "s3:DeleteBucket",
     "s3:PutBucketTagging",
     "s3:GetBucketTagging",
     "s3:PutEncryptionConfiguration",
     "s3:GetEncryptionConfiguration",
     "s3:PutLifecycleConfiguration",
     "s3:GetLifecycleConfiguration",
     "s3:GetBucketLocation",
     "s3:ListBucket",
     "s3:GetObject",
     "s3:PutObject",
     "s3:DeleteObject",
     "s3:ListBucketMultipartUploads",
     "s3:AbortMultipartUpload",
     "s3:ListMultipartUploadParts",
     "ec2:DescribeSnapshots",
     "ec2:DescribeVolumes",
     "ec2:DescribeVolumeAttribute",
     "ec2:DescribeVolumesModifications",
     "ec2:DescribeVolumeStatus",
     "ec2:CreateTags",
     "ec2:CreateVolume",
     "ec2:CreateSnapshot",
     "ec2:DeleteSnapshot"
   ],
   "Resource": "*"
 }
]}
EOF

POLICY_ARN=$(aws iam create-policy --policy-name $POLICY_NAME \
--policy-document file:///${SCRATCH}/policy.json --query Policy.Arn \
--tags Key=openshift_version,Value=${CLUSTER_VERSION} Key=operator_namespace,Value=openshift-adp Key=operator_name,Value=oadp \
--output text)
fi
----
* `SCRATCH`: The name for a temporary directory created for storing the files.
+
.. View the policy ARN by running the following command:
+
[source,terminal]
----
$ echo ${POLICY_ARN}
----

. Create an IAM role trust policy for the cluster:
+
.. Create the trust policy file by running the following command:
+
[source,terminal]
----
$ cat <<EOF > ${SCRATCH}/trust-policy.json
{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_ENDPOINT}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "${OIDC_ENDPOINT}:sub": [
            "system:serviceaccount:openshift-adp:openshift-adp-controller-manager",
            "system:serviceaccount:openshift-adp:velero"]
        }
      }
    }]
}
EOF
----
+
.. Create an IAM role trust policy for the cluster by running the following command:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam create-role --role-name \
  "${ROLE_NAME}" \
  --assume-role-policy-document file://${SCRATCH}/trust-policy.json \
  --tags Key=cluster_id,Value=${AWS_CLUSTER_ID}  Key=openshift_version,Value=${CLUSTER_VERSION} Key=operator_namespace,Value=openshift-adp Key=operator_name,Value=oadp --query Role.Arn --output text)
----
+
.. View the role ARN by running the following command:
+
[source,terminal]
----
$ echo ${ROLE_ARN}
----

. Attach the IAM policy to the IAM role by running the following command:
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name "${ROLE_NAME}" --policy-arn ${POLICY_ARN}
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-aws-sts/oadp-aws-sts.adoc

[id="installing-oadp-aws-sts_{context}"]
= Installing the OADP Operator and providing the IAM role

[role="_abstract"]
Install {oadp-first} on an {aws-short} {sts-short} cluster. AWS Security Token Service (AWS STS) is a global web service that provides short-term credentials for IAM or federated users.

[IMPORTANT]
====
Restic is unsupported.

Kopia file system backup (FSB) is supported when backing up file systems that do not support Container Storage Interface (CSI) snapshots.

Example file systems include the following:

* Amazon Elastic File System (EFS)
* Network File System (NFS)
* `emptyDir` volumes
* Local volumes

For backing up volumes, OADP on {aws-short} {sts-short} recommends native snapshots and Container Storage Interface (CSI) snapshots. Data Mover backups are supported, but can be slower than native snapshots.

In an {aws-short} cluster that uses STS authentication, restoring backed-up data in a different {aws-short} region is not supported.
====

.Prerequisites

* An OpenShift Container Platform {aws-short} {sts-short} cluster with the required access and tokens. For instructions, see the previous procedure _Preparing AWS credentials for OADP_. If you plan to use two different clusters for backing up and restoring, you must prepare {aws-short} credentials, including `ROLE_ARN`, for each cluster.

.Procedure

. Create an OpenShift Container Platform secret from your {aws-short} token file by entering the following commands:

.. Create the credentials file:
+
[source,terminal]
----
$ cat <<EOF > ${SCRATCH}/credentials
  [default]
  role_arn = ${ROLE_ARN}
  web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
  region = <aws_region>
EOF
----
+
Replace `<aws_region>` with the AWS region to use for the {sts-short} endpoint.

.. Create a namespace for OADP:
+
[source,terminal]
----
$ oc create namespace openshift-adp
----

.. Create the OpenShift Container Platform secret:
+
[source,terminal]
----
$ oc -n openshift-adp create secret generic cloud-credentials \
  --from-file=${SCRATCH}/credentials
----
+
[NOTE]
====
In OpenShift Container Platform versions 4.14 and later, the OADP Operator supports a new standardized {sts-short} workflow through the Operator Lifecycle Manager (OLM) and Cloud Credentials Operator (CCO). In this workflow, you do not need to create the above secret, you only need to supply the role ARN during the installation of OLM-managed operators using the OpenShift Container Platform web console, for more information see _Installing from the software catalog using the web console_.

The preceding secret is created automatically by CCO.
====

. Install the OADP Operator:
.. In the OpenShift Container Platform web console, browse to *Ecosystem* -> *Software Catalog*.
.. Search for the *OADP Operator*.
.. In the *role_ARN* field, paste the role_arn that you created previously and click *Install*.

. Create {aws-short} cloud storage using your {aws-short} credentials by entering the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: CloudStorage
  metadata:
    name: ${CLUSTER_NAME}-oadp
    namespace: openshift-adp
  spec:
    creationSecret:
      key: credentials
      name: cloud-credentials
    enableSharedConfig: true
    name: ${CLUSTER_NAME}-oadp
    provider: aws
    region: $REGION
EOF
----
// bringing over from MOB docs
. Check your application's storage default storage class by entering the following command:
+
[source,terminal]
----
$ oc get pvc -n <namespace>
----
+
[source,terminal]
----
NAME     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
applog   Bound    pvc-351791ae-b6ab-4e8b-88a4-30f73caf5ef8   1Gi        RWO            gp3-csi        4d19h
mysql    Bound    pvc-16b8e009-a20a-4379-accc-bc81fedd0621   1Gi        RWO            gp3-csi        4d19h
----

. Get the storage class by running the following command:
+
[source,terminal]
----
$ oc get storageclass
----
+
[source,terminal]
----
NAME                PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
gp2                 kubernetes.io/aws-ebs   Delete          WaitForFirstConsumer   true                   4d21h
gp2-csi             ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
gp3                 ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
gp3-csi (default)   ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
----
+
[NOTE]
====
The following storage classes will work:

  * gp3-csi
  * gp2-csi
  * gp3
  * gp2
====
+
If the application or applications that are being backed up are all using persistent volumes (PVs) with Container Storage Interface (CSI), it is advisable to include the CSI plugin in the OADP DPA configuration.

. Create the `DataProtectionApplication` resource to configure the connection to the storage where the backups and volume snapshots are stored:

.. If you are using only CSI volumes, deploy a Data Protection Application by entering the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    name: ${CLUSTER_NAME}-dpa
    namespace: openshift-adp
  spec:
    backupImages: true
    features:
      dataMover:
        enable: false
    backupLocations:
    - bucket:
        cloudStorageRef:
          name: ${CLUSTER_NAME}-oadp
        credential:
          key: credentials
          name: cloud-credentials
        prefix: velero
        default: true
        config:
          region: ${REGION}
    configuration:
      velero:
        defaultPlugins:
        - openshift
        - aws
        - csi
      nodeAgent:
        enable: false
        uploaderType: kopia
EOF
----
+
where:
+
`backupImages`:: Specifies whether to use image backup. Set to `false` if you do not want to use image backup.
`nodeAgent`:: Specifies the node agent configuration. See the important note regarding the `nodeAgent` attribute at the end of this procedure.
`uploaderType`:: Specifies the type of uploader. The built-in Data Mover uses Kopia as the default uploader mechanism regardless of the value of the `uploaderType` field.

.. If you are using CSI or non-CSI volumes, deploy a Data Protection Application by entering the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    name: ${CLUSTER_NAME}-dpa
    namespace: openshift-adp
  spec:
    backupImages: true
    features:
      dataMover:
         enable: false
    backupLocations:
    - bucket:
        cloudStorageRef:
          name: ${CLUSTER_NAME}-oadp
        credential:
          key: credentials
          name: cloud-credentials
        prefix: velero
        default: true
        config:
          region: ${REGION}
    configuration:
      velero:
        defaultPlugins:
        - openshift
        - aws
      nodeAgent:
        enable: false
        uploaderType: restic
    snapshotLocations:
      - velero:
          config:
            credentialsFile: /tmp/credentials/openshift-adp/cloud-credentials-credentials
            enableSharedConfig: "true"
            profile: default
            region: ${REGION}
          provider: aws
EOF
----
+
where:
+
`backupImages`:: Specifies whether to use image backup. Set to `false` if you do not want to use image backup.
`nodeAgent`:: Specifies the node agent configuration. See the important note regarding the `nodeAgent` attribute at the end of this procedure.
`credentialsFile`:: Specifies the mounted location of the bucket credential on the pod.
`enableSharedConfig`:: Specifies whether the `snapshotLocations` can share or reuse the credential defined for the bucket.
`profile`:: Specifies the profile name set in the {aws-short} credentials file.
`region`:: Specifies your {aws-short} region. This must be the same as the cluster region.
+
You are now ready to back up and restore OpenShift Container Platform applications, as described in _Backing up applications_.
+

[IMPORTANT]
====
If you use OADP 1.2, replace this configuration:

[source,terminal]
----
nodeAgent:
  enable: false
  uploaderType: restic
----
with the following configuration:

[source,terminal]
----
restic:
  enable: false
----
====

+

If you want to use two different clusters for backing up and restoring, the two clusters must have the same {aws-short} S3 storage names in both the cloud storage CR and the OADP `DataProtectionApplication` configuration.

[role="_additional-resources"]
.Additional resources

* Installing the OADP Operator

* Using Operator Lifecycle Manager in disconnected environments

* Installing from the software catalog using the web console

* Backing up applications

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-aws-sts/oadp-aws-sts.adoc

[id="performing-a-backup-oadp-aws-sts_{context}"]
= Performing a backup with OADP and AWS STS

[role="_abstract"]
Perform a backup by using {oadp-first} with {aws-first} (AWS STS). The following `hello-world` example application has no persistent volumes (PVs) attached.

Either Data Protection Application (DPA) configuration will work.

.Procedure

. Create a workload to back up by running the following commands:
+
[source,terminal]
----
$ oc create namespace hello-world
----
+
[source,terminal]
----
$ oc new-app -n hello-world --image=docker.io/openshift/hello-openshift
----

. Expose the route by running the following command:
+
[source,terminal]
----
$ oc expose service/hello-openshift -n hello-world
----

. Check that the application is working by running the following command:
+
[source,terminal]
----
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
----
+
[source,terminal]
----
Hello OpenShift!
----

. Back up the workload by running the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Backup
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    includedNamespaces:
    - hello-world
    storageLocation: ${CLUSTER_NAME}-dpa-1
    ttl: 720h0m0s
EOF
----

. Wait until the backup has completed and then run the following command:
+
[source,terminal]
----
$ watch "oc -n openshift-adp get backup hello-world -o json | jq .status"
----
+
[source,json]
----
{
  "completionTimestamp": "2022-09-07T22:20:44Z",
  "expiration": "2022-10-07T22:20:22Z",
  "formatVersion": "1.1.0",
  "phase": "Completed",
  "progress": {
    "itemsBackedUp": 58,
    "totalItems": 58
  },
  "startTimestamp": "2022-09-07T22:20:22Z",
  "version": 1
}
----

. Delete the demo workload by running the following command:
+
[source,terminal]
----
$ oc delete ns hello-world
----

. Restore the workload from the backup by running the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Restore
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    backupName: hello-world
EOF
----

. Wait for the Restore to finish by running the following command:
+
[source,terminal]
----
$ watch "oc -n openshift-adp get restore hello-world -o json | jq .status"
----
+
[source,json]
----
{
  "completionTimestamp": "2022-09-07T22:25:47Z",
  "phase": "Completed",
  "progress": {
    "itemsRestored": 38,
    "totalItems": 38
  },
  "startTimestamp": "2022-09-07T22:25:28Z",
  "warnings": 9
}
----

. Check that the workload is restored by running the following command:
+
[source,terminal]
----
$ oc -n hello-world get pods
----
+
[source,terminal]
----
NAME                              READY   STATUS    RESTARTS   AGE
hello-openshift-9f885f7c6-kdjpj   1/1     Running   0          90s
----
. Check the JSONPath by running the following command:
+
[source,terminal]
----
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
----
+
[source,terminal]
----
Hello OpenShift!
----

+

[NOTE]
====
For troubleshooting tips, see troubleshooting documentation.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-aws-sts/oadp-aws-sts.adoc

[id="cleanup-a-backup-oadp-aws-sts_{context}"]
= Cleaning up a cluster after a backup with OADP and AWS STS

[role="_abstract"]
Uninstall the {oadp-first} Operator together with the backups and the S3 bucket from the `hello-world` example.

.Procedure

. Delete the workload by running the following command:
+
[source,terminal]
----
$ oc delete ns hello-world
----

. Delete the Data Protection Application (DPA) by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete dpa ${CLUSTER_NAME}-dpa
----

. Delete the cloud storage by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete cloudstorage ${CLUSTER_NAME}-oadp
----

+
[IMPORTANT]
====
If this command hangs, you might need to delete the finalizer by running the following command:

[source,terminal]
----
$ oc -n openshift-adp patch cloudstorage ${CLUSTER_NAME}-oadp -p '{"metadata":{"finalizers":null}}' --type=merge
----
====

. If the Operator is no longer required, remove it by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete subscription oadp-operator
----

. Remove the namespace from the Operator by running the following command:
+
[source,terminal]
----
$ oc delete ns openshift-adp
----

. If the backup and restore resources are no longer required, remove them from the cluster by running the following command:
+
[source,terminal]
----
$ oc delete backups.velero.io hello-world
----

. To delete backup, restore and remote objects in {aws-short} S3, run the following command:
+
[source,terminal]
----
$ velero backup delete hello-world
----

. If you no longer need the Custom Resource Definitions (CRD), remove them from the cluster by running the following command:
+
[source,terminal]
----
$ for CRD in `oc get crds | grep velero | awk '{print $1}'`; do oc delete crd $CRD; done
----

. Delete the {aws-short} S3 bucket by running the following commands:
+
[source,terminal]
----
$ aws s3 rm s3://${CLUSTER_NAME}-oadp --recursive
----
+
[source,terminal]
----
$ aws s3api delete-bucket --bucket ${CLUSTER_NAME}-oadp
----

. Detach the policy from the role by running the following command:
+
[source,terminal]
----
$ aws iam detach-role-policy --role-name "${ROLE_NAME}"  --policy-arn "${POLICY_ARN}"
----

. Delete the role by running the following command:
+
[source,terminal]
----
$ aws iam delete-role --role-name "${ROLE_NAME}"
----
