---
title: "Backing up applications on ROSA clusters using OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-rosa-backing-up-applications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-rosa-backing-up-applications
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up applications on ROSA clusters using OADP

[id="oadp-rosa-backing-up-applications"]

= Backing up applications on ROSA clusters using OADP

= Installing OADP

[role="_abstract"]
Use {oadp-first} with OpenShift Container Platform clusters to back up and restore application data.

Use {oadp-first} with {product-rosa} (ROSA) clusters to back up and restore application data.

ROSA is a fully-managed, turnkey application platform that allows you to deliver value to your customers by building and deploying applications.

ROSA provides seamless integration with a wide range of {aws-first} compute, database, analytics, machine learning, networking, mobile, and other services to speed up the building and delivery of differentiating experiences to your customers.

You can subscribe to the service directly from your {aws-short} account.

After you create your clusters, you can operate your clusters with the OpenShift Container Platform web console or through {cluster-manager-first}. You can also use ROSA with OpenShift APIs and command-line interface (CLI) tools.

For additional information about ROSA installation, see _Installing Red Hat OpenShift Service on AWS (ROSA)_ interactive walk-through.

Before installing {oadp-first}, you must set up role and policy credentials for OADP so that it can use the {aws-full} API.

This process is performed in the following two stages:

. Prepare {aws-short} credentials
. Install the OADP Operator and give it an IAM role

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc
// * backup_and_restore/application_backup_and_restore/installing-oadp-rosa.adoc

[id="preparing-aws-credentials-for-oadp_{context}"]
= Preparing AWS credentials for OADP

[role="_abstract"]
Prepare and configure an {aws-full} account to install {oadp-first}.

.Procedure

. Create the following environment variables by running the following commands:
+
[IMPORTANT]
====
Change the cluster name to match your cluster, and ensure you are logged into the cluster as an administrator. Ensure that all fields are outputted correctly before continuing.
====
+
[source,terminal]
----
$ export CLUSTER_NAME=<my_cluster>
----
+

Replace `<my_cluster>` with your cluster name.

+
[source,terminal]
----
$ export ROSA_CLUSTER_ID=$(rosa describe cluster -c ${CLUSTER_NAME} --output json | jq -r .id)
----
+
[source,terminal]
----
$ export REGION=$(rosa describe cluster -c ${CLUSTER_NAME} --output json | jq -r .region.id)
----
+
[source,terminal]
----
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o jsonpath='{.spec.serviceAccountIssuer}' | sed 's|^https://||')
----
+
[source,terminal]
----
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
----
+
[source,terminal]
----
$ export CLUSTER_VERSION=$(rosa describe cluster -c ${CLUSTER_NAME} -o json | jq -r .version.raw_id | cut -f -2 -d '.')
----
+
[source,terminal]
----
$ export ROLE_NAME="${CLUSTER_NAME}-openshift-oadp-aws-cloud-credentials"
----
+
[source,terminal]
----
$ export SCRATCH="/tmp/${CLUSTER_NAME}/oadp"
----
+
[source,terminal]
----
$ mkdir -p ${SCRATCH}
----
+
[source,terminal]
----
$ echo "Cluster ID: ${ROSA_CLUSTER_ID}, Region: ${REGION}, OIDC Endpoint:
  ${OIDC_ENDPOINT}, AWS Account ID: ${AWS_ACCOUNT_ID}"
----

. On the {aws-short} account, create an IAM policy to allow access to {aws-short} S3:
+
.. Check to see if the policy exists by running the following command:
+
[source,terminal]
----
$ POLICY_ARN=$(aws iam list-policies --query "Policies[?PolicyName=='RosaOadpVer1'].{ARN:Arn}" --output text)
----
+
--
* `RosaOadp`: Replace `RosaOadp` with your policy name.
--
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

  POLICY_ARN=$(aws iam create-policy --policy-name "RosaOadpVer1" \
  --policy-document file:///${SCRATCH}/policy.json --query Policy.Arn \
  --tags Key=rosa_openshift_version,Value=${CLUSTER_VERSION} Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-oadp Key=operator_name,Value=openshift-oadp \
  --output text)
  fi
----
+
--
* `SCRATCH`: `SCRATCH` is a name for a temporary directory created for the environment variables.
--
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
.. Create the role by running the following command:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam create-role --role-name \
  "${ROLE_NAME}" \
  --assume-role-policy-document file://${SCRATCH}/trust-policy.json \
  --tags Key=rosa_cluster_id,Value=${ROSA_CLUSTER_ID} \
         Key=rosa_openshift_version,Value=${CLUSTER_VERSION} \
         Key=rosa_role_prefix,Value=ManagedOpenShift \
         Key=operator_namespace,Value=openshift-adp \
         Key=operator_name,Value=openshift-oadp \
  --query Role.Arn --output text)
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
$ aws iam attach-role-policy --role-name "${ROLE_NAME}" \
  --policy-arn ${POLICY_ARN}
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="installing-oadp-rosa-sts_{context}"]
= Installing the OADP Operator and providing the IAM role

[role="_abstract"]
Install {oadp-first} on clusters with {aws-short} {sts-short}. AWS Security Token Service (AWS STS) is a global web service that provides short-term credentials for IAM or federated users. OpenShift Container Platform with {sts-short} is the recommended credential mode.

[IMPORTANT]
====
Restic is unsupported.

Kopia file system backup (FSB) is supported when backing up file systems that do not support Container Storage Interface (CSI) snapshots.

Example file systems include the following:

* Amazon Elastic File System (EFS)
* Network File System (NFS)
* `emptyDir` volumes
* Local volumes

For backing up volumes, OADP on ROSA with {aws-short} {sts-short} recommends native snapshots and Container Storage Interface (CSI) snapshots. Data Mover backups are supported, but can be slower than native snapshots.

In an Amazon ROSA cluster that uses STS authentication, restoring backed-up data in a different {aws-short} region is not supported.
====

.Prerequisites

* An OpenShift Container Platform
* A OpenShift Container Platform
cluster with the required access and tokens. For instructions, see the previous procedure _Preparing AWS credentials for OADP_. If you plan to use two different clusters for backing up and restoring, you must prepare {aws-short} credentials, including `ROLE_ARN`, for each cluster.

.Procedure

. Create
an OpenShift Container Platform
a OpenShift Container Platform
secret from your {aws-short} token file by entering the following commands:

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
--
[NOTE]
====
In OpenShift Container Platform versions 4.15 and later, the OADP Operator supports a new standardized {sts-short} workflow through the Operator Lifecycle Manager (OLM) and Cloud Credentials Operator (CCO). In this workflow, you do not need to create the above secret, you only need to supply the role ARN during the installation of OLM-managed operators using the OpenShift Container Platform web console, for more information see _Installing from software catalog using the web console_.

The preceding secret is created automatically by CCO.
====
--

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
`backupImages`:: ROSA supports internal image backup. Set this field to `false` if you do not want to use image backup.
`backupImages`:: OpenShift Container Platform supports internal image backup. Set this field to `false` if you do not want to use image backup.
`nodeAgent`:: See the important note regarding the `nodeAgent` attribute at the end of this procedure.
`uploaderType`:: Specifies the type of uploader. The built-in Data Mover uses Kopia as the default uploader mechanism regardless of the value of the `uploaderType` field.
+
// . Create the `DataProtectionApplication` resource, which is used to configure the connection to the storage where the backups and volume snapshots are stored:

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
`backupImages`:: ROSA supports internal image backup. Set this field to `false` if you do not want to use image backup.
`backupImages`:: OpenShift Container Platform supports internal image backup. Set this field to `false` if you do not want to use image backup.
`nodeAgent`:: See the important note regarding the `nodeAgent` attribute at the end of this procedure.
`credentialsFile`:: Specifies the mounted location of the bucket credential on the pod.
`enableSharedConfig`:: Specifies whether the `snapshotLocations` can share or reuse the credential defined for the bucket.
`profile`:: Specifies the profile name set in the {aws-short} credentials file.
`region`:: Specifies your {aws-short} region. This must be the same as the cluster region.
+
You are now ready to back up and restore OpenShift Container Platform applications, as described in _Backing up applications_.

+

--
[IMPORTANT]
====
The `enable` parameter of `restic` is set to `false` in this configuration, because OADP does not support Restic in
ROSA
OpenShift Container Platform
environments.
====
--

+

If you want to use two different clusters for backing up and restoring, the two clusters must have the same {aws-short} S3 storage names in both the cloud storage CR and the OADP `DataProtectionApplication` configuration.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="updating-role-arn-oadp-rosa-sts_{context}"]
= Updating the IAM role ARN in the {oadp-short} Operator subscription

[role="_abstract"]
Update the {oadp-short} Operator subscription to fix an installation error due to incorrect IAM role Amazon Resource Name (ARN).

While installing the {oadp-short} Operator on a
ROSA Security Token Service (STS)
OpenShift Container Platform
cluster, if you provide an incorrect IAM role Amazon Resource Name (ARN), the `openshift-adp-controller` pod gives an error. The credential requests that are generated contain the wrong IAM role ARN. To update the credential requests object with the correct IAM role ARN, you can edit the {oadp-short} Operator subscription and patch the IAM role ARN with the correct value. By editing the {oadp-short} Operator subscription, you do not have to uninstall and reinstall {oadp-short} to update the IAM role ARN.

.Prerequisites

* You have a {product-rosa} STS cluster with the required access and tokens.
* You have a OpenShift Container Platform cluster with the required access and tokens.
* You have installed {oadp-short} on the ROSA STS cluster.

.Procedure

. To verify that the {oadp-short} subscription has the wrong IAM role ARN environment variable set, run the following command:
+
[source,terminal]
----
$ oc get sub -o yaml redhat-oadp-operator
----
+
.Example subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  annotations:
  creationTimestamp: "2025-01-15T07:18:31Z"
  generation: 1
  labels:
    operators.coreos.com/redhat-oadp-operator.openshift-adp: ""
  name: redhat-oadp-operator
  namespace: openshift-adp
  resourceVersion: "77363"
  uid: 5ba00906-5ad2-4476-ae7b-ffa90986283d
spec:
  channel: stable-1.4
  config:
    env:
    - name: ROLEARN
      value: arn:aws:iam::11111111:role/wrong-role-arn
  installPlanApproval: Manual
  name: redhat-oadp-operator
  source: prestage-operators
  sourceNamespace: openshift-marketplace
  startingCSV: oadp-operator.v1.4.2
----
+
where:
+
`ROLEARN`:: Verify the value of `ROLEARN` you want to update.

. Update the `ROLEARN` field of the subscription with the correct role ARN by running the following command:
+
[source,terminal]
----
$ oc patch subscription redhat-oadp-operator -p '{"spec": {"config": {"env": [{"name": "ROLEARN", "value": "<role_arn>"}]}}}' --type='merge'
----
+
where:
+
`<role_arn>`:: Specifies the IAM role ARN to be updated. For example, `arn:aws:iam::160.....6956:role/oadprosa.....8wlf`.

. Verify that the `secret` object is updated with correct role ARN value by running the following command:
+
[source,terminal]
----
$ oc get secret cloud-credentials -o jsonpath='{.data.credentials}' | base64 -d
----
+
.Example output
[source,terminal]
----
[default]
sts_regional_endpoints = regional
role_arn = arn:aws:iam::160.....6956:role/oadprosa.....8wlf
web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
----

. Configure the `DataProtectionApplication` custom resource (CR) manifest file as shown in the following example:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: test-rosa-dpa
  namespace: openshift-adp
spec:
  backupLocations:
  - bucket:
      config:
        region: us-east-1
      cloudStorageRef:
        name: <cloud_storage>
      credential:
        name: cloud-credentials
        key: credentials
      prefix: velero
      default: true
  configuration:
    velero:
      defaultPlugins:
      - aws
      - openshift
----
+
where:
+
`<cloud_storage>`:: Specifies the `CloudStorage` CR.

. Create the `DataProtectionApplication` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <dpa_manifest_file>
----

. Verify that the `DataProtectionApplication` CR is reconciled and the `status` is set to `"True"` by running the following command:
+
[source,terminal]
----
$  oc get dpa -n openshift-adp -o yaml
----
+
.Example `DataProtectionApplication`
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
status:
    conditions:
    - lastTransitionTime: "2023-07-31T04:48:12Z"
      message: Reconcile complete
      reason: Complete
      status: "True"
      type: Reconciled
----

. Verify that the `BackupStorageLocation` CR is in an available state by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {oadp-bsl-api} -n openshift-adp
----
+
.Example `BackupStorageLocation`
[source,terminal]
----
NAME       PHASE       LAST VALIDATED   AGE   DEFAULT
ts-dpa-1   Available   3s               6s    true
----

[role="_additional-resources"]
.Additional resources
// This xref points to a topic that is not published in the ROSA docs.

* Installing from the software catalog using the web console

* Backing up applications

* Installing Red Hat OpenShift Service on AWS (ROSA) interactive walkthrough

* {cluster-manager-first}

// For ROSA and ROSA HCP, this section is in oadp-use-cases/oadp-rosa-backup-restore.adoc

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="performing-a-backup-oadp-rosa-sts_{context}"]
= Example: Performing a backup with OADP and OpenShift Container Platform

[role="_abstract"]
Perform a backup by using {oadp-first} with OpenShift Container Platform. The following example `hello-world` application has no persistent volumes (PVs) attached.

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
You should see an output similar to the following example:
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

. Wait until the backup is complete, and then run the following command:
+
[source,terminal]
----
$ watch "oc -n openshift-adp get backup hello-world -o json | jq .status"
----
+
You should see an output similar to the following example:
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
You should see an output similar to the following example:
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
You should see an output similar to the following example:
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
You should see an output similar to the following example:
+
[source,terminal]
----
Hello OpenShift!
----
+
[NOTE]
====
For troubleshooting tips, see the troubleshooting documentation.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="cleanup-a-backup-oadp-rosa-sts_{context}"]
= Cleaning up a cluster after a backup with OADP and ROSA STS

[role="_abstract"]
Uninstall the {oadp-first} Operator together with the backups and the S3 bucket from the hello-world example.

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
[WARNING]
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

. Remove the namespace from the Operator:
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

. To delete backup, restore and remote objects in {aws-short} S3 run the following command:
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
