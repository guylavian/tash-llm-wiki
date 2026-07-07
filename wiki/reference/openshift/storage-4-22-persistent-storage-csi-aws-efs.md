---
title: "AWS Elastic File Service CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-aws-efs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-aws-efs
version: 4.22
family: storage
documentKind: "Documentation"
---

# AWS Elastic File Service CSI Driver Operator

[id="persistent-storage-csi-aws-efs"]
= AWS Elastic File Service CSI Driver Operator

[IMPORTANT]
====
This procedure is specific to the AWS EFS CSI Driver Operator (a Red Hat Operator), which is only applicable for OpenShift Container Platform 4.10 and later versions.
====

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for AWS Elastic File Service (EFS).

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

After installing the AWS EFS CSI Driver Operator, OpenShift Container Platform installs the AWS EFS CSI Operator and the AWS EFS CSI driver by default in the `openshift-cluster-csi-drivers` namespace. This allows the AWS EFS CSI Driver Operator to create CSI-provisioned PVs that mount to AWS EFS assets.

* The _AWS EFS CSI Driver Operator_, after being installed, does not create a storage class by default to use to create persistent volume claims (PVCs). However, you can manually create the AWS EFS `StorageClass`.
The AWS EFS CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand.
This eliminates the need for cluster administrators to pre-provision storage.

* The _AWS EFS CSI driver_ enables you to create and mount AWS EFS PVs.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="persistent-storage-efs-csi-driver-operator-setup_{context}"]
= Setting up the {FeatureName} CSI Driver Operator

. If you are using {FeatureName} with AWS Secure Token Service (STS), obtain a role Amazon Resource Name (ARN) for STS. This is required for installing the {FeatureName} CSI Driver Operator.

. Install the {FeatureName} CSI Driver Operator.

. Install the {FeatureName} CSI Driver.

// Obtaining a role ARN (OCP)
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="efs-sts_{context}"]
= Obtaining a role Amazon Resource Name for Security Token Service

This procedure explains how to obtain a role Amazon Resource Name (ARN) to configure the AWS EFS CSI Driver Operator with OpenShift Container Platform on AWS Security Token Service (STS).

[IMPORTANT]
====
Perform this procedure before you install the AWS EFS CSI Driver Operator (see _Installing the AWS EFS CSI Driver Operator_ procedure).
====

.Prerequisites

* Access to the cluster as a user with the cluster-admin role.
* AWS account credentials

.Procedure

You can obtain the ARN role in multiple ways. The following procedure shows one method that uses the same concept and CCO utility (`ccoctl`) binary tool as cluster installation.

[NOTE]
====
If you are using One Zone file system, you need to create two `CredentialRequests`, one for the controller and one for the driver node. For more information, see Section _Setting up One Zone file systems with STS_.
====

To obtain a role ARN for configuring AWS EFS CSI Driver Operator using STS:

. Extract the `ccoctl` from the OpenShift Container Platform release image, which you used to install the cluster with STS. For more information, see "Configuring the Cloud Credential Operator utility".

. Create and save an EFS `CredentialsRequest` YAML file, such as shown in the following example, and then place it in the `credrequests` directory:
+
.Example
[source, yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: openshift-aws-efs-csi-driver
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - action:
      - elasticfilesystem:*
      effect: Allow
      resource: '*'
  secretRef:
    name: aws-efs-cloud-credentials
    namespace: openshift-cluster-csi-drivers
  serviceAccountNames:
  - aws-efs-csi-driver-operator
  - aws-efs-csi-driver-controller-sa
----

. Run the `ccoctl` tool to generate a new IAM role in AWS, and create a YAML file for it in the local file system (`<path_to_ccoctl_output_dir>/manifests/openshift-cluster-csi-drivers-aws-efs-cloud-credentials-credentials.yaml`).
+
[source,terminal]
----
$ ccoctl aws create-iam-roles --name=<name> --region=<aws_region> --credentials-requests-dir=<path_to_directory_with_list_of_credentials_requests>/credrequests --identity-provider-arn=arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com
----
+
* `name=<name>` is the name used to tag any cloud resources that are created for tracking.

* `region=<aws_region>` is the AWS region where cloud resources are created.

* `dir=<path_to_directory_with_list_of_credentials_requests>/credrequests` is the directory containing the EFS CredentialsRequest file in previous step.

* `<aws_account_id>` is the AWS account ID.
+
.Example
+
[source,terminal]
----
$ ccoctl aws create-iam-roles --name my-aws-efs --credentials-requests-dir credrequests --identity-provider-arn arn:aws:iam::123456789012:oidc-provider/my-aws-efs-oidc.s3.us-east-2.amazonaws.com
----
+
.Example output
+
[source,terminal]
----
2022/03/21 06:24:44 Role arn:aws:iam::123456789012:role/my-aws-efs -openshift-cluster-csi-drivers-aws-efs-cloud- created
2022/03/21 06:24:44 Saved credentials configuration to: /manifests/openshift-cluster-csi-drivers-aws-efs-cloud-credentials-credentials.yaml
2022/03/21 06:24:45 Updated Role policy for Role my-aws-efs-openshift-cluster-csi-drivers-aws-efs-cloud-
----

. Copy the role ARN from the first line of the _Example output_ in the preceding step. The role ARN is between "Role" and "created". In this example, the role ARN is "arn:aws:iam::123456789012:role/my-aws-efs -openshift-cluster-csi-drivers-aws-efs-cloud".
+
You will need the role ARN when you install the AWS EFS CSI Driver Operator.

.Next steps

//??the below step not needed for 4.14? ???
//. Create the AWS EFS cloud credentials and secret:
//+
//[source, terminal]
//----
//$ oc create -f <path_to_ccoctl_output_dir>/manifests/openshift-cluster-csi-drivers-aws-efs-cloud-credentials-credentials.yaml
//----
//+
//.Example
//+
//[source, terminal]
//----
//$ oc create -f /manifests/openshift-cluster-csi-drivers-aws-efs-cloud-credentials-credentials.yaml
//----
//+
//.Example output
//+
//[source, terminal]
//----
//secret/aws-efs-cloud-credentials created
//----

// Obtaining a role ARN (OSD and ROSA)
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="efs-sts_{context}"]
= Obtaining a role Amazon Resource Name for Security Token Service

[role="_abstract"]
This procedure explains how to obtain a role Amazon Resource Name (ARN) to configure the AWS EFS CSI Driver Operator with OpenShift Container Platform on AWS Security Token Service (STS).

[IMPORTANT]
====
Perform this procedure before you install the AWS EFS CSI Driver Operator (see _Installing the AWS EFS CSI Driver Operator_ procedure).
====

.Prerequisites

* Access to the cluster as a user with the cluster-admin role.
* AWS account credentials

.Procedure

. Create an IAM policy JSON file with the following content:
+
[source,json]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticfilesystem:DescribeAccessPoints",
        "elasticfilesystem:DescribeFileSystems",
        "elasticfilesystem:DescribeMountTargets",
        "ec2:DescribeAvailabilityZones",
        "elasticfilesystem:TagResource"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "elasticfilesystem:CreateAccessPoint"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:RequestTag/efs.csi.aws.com/cluster": "true"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "elasticfilesystem:DeleteAccessPoint",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/efs.csi.aws.com/cluster": "true"
        }
      }
    }
  ]
}
----

. Create an IAM trust JSON file with the following content:
+
[source,json]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::<your_aws_account_ID>:oidc-provider/<openshift_oidc_provider>"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "<openshift_oidc_provider>:sub": [
            "system:serviceaccount:openshift-cluster-csi-drivers:aws-efs-csi-driver-operator",
            "system:serviceaccount:openshift-cluster-csi-drivers:aws-efs-csi-driver-controller-sa"
          ]
        }
      }
    }
  ]
}
----
+
--
where:

`Statement.Principal.Federated`:: Specifies your AWS account ID and the OpenShift OIDC provider endpoint.
+
Obtain your AWS account ID by running the following command:
+
[source,terminal]
----
$ aws sts get-caller-identity --query Account --output text
----
+
Obtain the OpenShift OIDC endpoint by running the following command:
+
[source,terminal]
----
$ rosa describe cluster \
  -c $(oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}') \
  -o yaml | awk '/oidc_endpoint_url/ {print $2}' | cut -d '/' -f 3,4
----
+
Obtain the OpenShift OIDC endpoint by running the following command:
+
[source,terminal]
----
$ openshift_oidc_provider=`oc get authentication.config.openshift.io cluster \
  -o json | jq -r .spec.serviceAccountIssuer | sed -e "s/^https:\/\///"`; \
  echo $openshift_oidc_provider
----

`Statement.Condition.StringEquals[0]`:: Specify the OpenShift OIDC endpoint again.
--

. Create the IAM role:
+
[source,terminal]
----
ROLE_ARN=$(aws iam create-role \
  --role-name "<your_cluster_name>-aws-efs-csi-operator" \
  --assume-role-policy-document file://<your_trust_file_name>.json \
  --query "Role.Arn" --output text); echo $ROLE_ARN
----
+
Copy the role ARN. You will need it when you install the AWS EFS CSI Driver Operator.

. Create the IAM policy:
+
[source,terminal]
----
POLICY_ARN=$(aws iam create-policy \
  --policy-name "<your_cluster_name>-aws-efs-csi" \
  --policy-document file://<your_policy_file_name>.json \
  --query 'Policy.Arn' --output text); echo $POLICY_ARN
----

. Attach the IAM policy to the IAM role:
+
[source,terminal]
----
$ aws iam attach-role-policy \
  --role-name "<your_cluster_name>-aws-efs-csi-operator" \
  --policy-arn $POLICY_ARN
----

. Create a `Secret` YAML file for the driver operator:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
 name: aws-efs-cloud-credentials
 namespace: openshift-cluster-csi-drivers
stringData:
  credentials: |-
    [default]
    sts_regional_endpoints = regional
    role_arn = <role_ARN>
    web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
----

. Create the secret:
+
[source,terminal]
----
$ oc apply -f aws-efs-cloud-credentials.yaml
----
+
You are now ready to install the AWS EFS CSI driver.

.Next steps
Install the AWS EFS CSI Driver Operator.

[role="_additional-resources"]
.Additional resources
* Installing the AWS EFS CSI Driver Operator
* Configuring the Cloud Credential Operator utility
* Installing the {FeatureName} CSI Driver

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-olm-operator-install_{context}"]
= Installing the {FeatureName} CSI Driver Operator

The {FeatureName} CSI Driver Operator (a Red{nbsp}Hat Operator) is not installed in OpenShift Container Platform by default. Use the following procedure to install and configure the {FeatureName} CSI Driver Operator in your cluster.

// The following ifeval and restricted ifdef statements exclude STS and a note about avoiding
// installing community operator content for CSI drivers other than EWS

.Prerequisites
* Access to the OpenShift Container Platform web console.

.Procedure
To install the {FeatureName} CSI Driver Operator from the web console:

. Log in to the web console.

. Install the {FeatureName} CSI Operator:

.. Click *Ecosystem* -> *Software Catalog*.

.. Locate the {FeatureName} CSI Operator by typing *{FeatureName} CSI* in the filter box.

.. Click the *{FeatureName} CSI Driver Operator* button.

+
[IMPORTANT]
====
Be sure to select the *{FeatureName} CSI Driver Operator* and not the *{FeatureName} Operator*. The *{FeatureName} Operator* is a community Operator and is not supported by Red Hat.
====

.. On the *{FeatureName} CSI Driver Operator* page, click *Install*.

.. On the *Install Operator* page, ensure that:
+
* If you are using {FeatureName} with AWS Secure Token Service (STS), in the *role ARN* field, enter the ARN role copied from the last step of the _Obtaining a role Amazon Resource Name for Security Token Service_ procedure.
* *All namespaces on the cluster (default)* is selected.
* *Installed Namespace* is set to *openshift-cluster-csi-drivers*.

.. Click *Install*.
+
After the installation finishes, the {FeatureName} CSI Operator is listed in the *Installed Operators* section of the web console.

// The following ifeval statements exclude STS and a note about avoiding
// installing community operator content for CSI drivers other than EWS

.Next steps
Install the AWS EFS CSI Driver.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="persistent-storage-csi-efs-driver-install_{context}"]
= Installing the {FeatureName} CSI Driver

After installing the {FeatureName} CSI Driver Operator (a Red Hat operator), you install the {FeatureName} CSI driver.

.Prerequisites
* Access to the OpenShift Container Platform web console.

.Procedure

. Click *Administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.

. On the *Instances* tab, click *Create ClusterCSIDriver*.

. Use the following YAML file:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
    name: efs.csi.aws.com
spec:
  managementState: Managed
----

. Click *Create*.

. Wait for the following Conditions to change to a "True" status:
+

* AWSEFSDriverNodeServiceControllerAvailable

* AWSEFSDriverControllerServiceControllerAvailable

// Be sure to set the :StorageClass: and :Provisioner: value in each assembly
// on the line before the include statement for this module. For example, to
// set the StorageClass value to "AWS EBS", add the following line to the
// assembly:
// :StorageClass: AWS EBS
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="storage-create-storage-class_{context}"]
= Creating the {StorageClass} storage class

Storage classes are used to differentiate and delineate storage levels and
usages. By defining a storage class, users can obtain dynamically provisioned
persistent volumes.

The _AWS EFS CSI Driver Operator (a Red Hat operator)_, after being installed, does not create a storage class by default. However, you can manually create the AWS EFS storage class.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws-efs-csi.adoc

[id="storage-create-storage-class-console_{context}"]
= Creating the {StorageClass} storage class using the console

[role="_abstract"]
.Procedure

. In the OpenShift Container Platform web console, click *Storage* -> *StorageClasses*.

. On the *StorageClasses* page, click *Create StorageClass*.

. On the *StorageClass* page, perform the following steps:

.. Enter a name to reference the storage class.

.. Optional: Enter the description.

.. Select the reclaim policy.

.. Select *`{Provisioner}`* from the *Provisioner* drop-down list.
+
[NOTE]
====
To create the storage class with the equivalent CSI driver, select `{CsiDriver}` from the drop-down list. For more details, see _AWS Elastic Block Store CSI Driver Operator_.
====

.. Optional: Set the configuration parameters for the selected provisioner.

. Click *Create*.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws-efs-csi.adoc

[id="storage-create-storage-class-cli_{context}"]
= Creating the {StorageClass} storage class using the CLI

[role="_abstract"]
.Procedure

* Create a `StorageClass` object:
+
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: efs-sc
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap <1>
  fileSystemId: fs-a5324911 <2>
  directoryPerms: "700" <3>
  gidRangeStart: "1000" <4>
  gidRangeEnd: "2000" <4>
  basePath: "/dynamic_provisioning" <5>
----
<1> `provisioningMode` must be `efs-ap` to enable dynamic provisioning.
<2> `fileSystemId` must be the ID of the EFS volume created manually.
<3> `directoryPerms` is the default permission of the root directory of the volume. In this example, the volume is accessible only by the owner.
<4> `gidRangeStart` and `gidRangeEnd` set the range of POSIX Group IDs (GIDs) that are used to set the GID of the AWS access point. If not specified, the default range is 50000-7000000. Each provisioned volume, and thus AWS access point, is assigned a unique GID from this range.
<5> `basePath` is the directory on the EFS volume that is used to create dynamically provisioned volumes. In this case, a PV is provisioned as “/dynamic_provisioning/<random uuid>” on the EFS volume. Only the subdirectory is mounted to pods that use the PV.
+
[NOTE]
====
A cluster admin can create several `StorageClass` objects, each using a different EFS volume.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//

[id="persistent-storage-csi-efs-cross-account_{context}"]
= AWS EFS CSI cross account support

Cross account support allows you to have
 a OpenShift Container Platform cluster
 an OpenShift Container Platform cluster
in one AWS account and mount your file system in another AWS account by using the AWS Elastic File System (EFS) Container Storage Interface (CSI) driver.

.Prerequisites

* Access to
 a OpenShift Container Platform cluster
 an OpenShift Container Platform cluster
with administrator rights

* Two valid AWS accounts

* The EFS CSI Operator has been installed. For information about installing the EFS CSI Operator, see the _Installing the AWS EFS CSI Driver Operator_ section.

* Both the OpenShift Container Platform cluster and EFS file system must be located in the same AWS region.

* Ensure that the two virtual private clouds (VPCs) used in the following procedure use different network Classless Inter-Domain Routing (CIDR) ranges.

* Access to OpenShift Container Platform CLI (`oc`).

* Access to AWS CLI.

* Access to `jq` command-line JSON processor.

.Procedure

The following procedure explains how to set up:

* OpenShift Container Platform AWS Account A: Contains a Red Hat OpenShift Container Platform cluster v4.16, or later, deployed within a VPC

* AWS Account B: Contains a VPC (including subnets, route tables, and network connectivity). The EFS filesystem will be created in this VPC.

To use AWS EFS across accounts:

. Set up the environment:

.. Configure environment variables by running the following commands:
+
[source,terminal]
----
export CLUSTER_NAME="<CLUSTER_NAME>" <1>
export AWS_REGION="<AWS_REGION>" <2>
export AWS_ACCOUNT_A_ID="<ACCOUNT_A_ID>" <3>
export AWS_ACCOUNT_B_ID="<ACCOUNT_B_ID>" <4>
export AWS_ACCOUNT_A_VPC_CIDR="<VPC_A_CIDR>" <5>
export AWS_ACCOUNT_B_VPC_CIDR="<VPC_B_CIDR>" <6>
export AWS_ACCOUNT_A_VPC_ID="<VPC_A_ID>" <7>
export AWS_ACCOUNT_B_VPC_ID="<VPC_B_ID>" <8>
export SCRATCH_DIR="<WORKING_DIRECTORY>" <9>
export CSI_DRIVER_NAMESPACE="openshift-cluster-csi-drivers" <10>
export AWS_PAGER="" <11>
----
<1> Cluster name of choice.
<2> AWS region of choice.
<3> AWS Account A ID.
<4> AWS Account B ID.
<5> CIDR range of VPC in Account A.
<6> CIDR range of VPC in Account B.
<7> VPC ID in Account A (cluster)
<8> VPC ID in Account B (EFS cross account)
<9> Any writeable directory of choice to use to store temporary files.
<10> If your driver is installed in a non-default namespace, change this value.
<11> Makes AWS CLI output everything directly to stdout.

.. Create the working directory by running the following command:
+
[source,terminal]
----
mkdir -p $SCRATCH_DIR
----

.. Verify cluster connectivity by running the following command in the OpenShift Container Platform CLI:
+
[source,terminal]
----
$ oc whoami
----

.. Determine the OpenShift Container Platform cluster type and set node selector:
+
The EFS cross account feature requires assigning AWS IAM policies to nodes running EFS CSI controller pods. However, this is
not consistent for every OpenShift Container Platform type.
+
* If your cluster is deployed as a Hosted Control Plane (HyperShift), set the `NODE_SELECTOR` environment variable to hold the worker node label by running the following command:
+
[source,terminal]
----
export NODE_SELECTOR=node-role.kubernetes.io/worker
----
+
* For all other OpenShift Container Platform types, set the `NODE_SELECTOR` environment variable to hold the master node label by running the following command:
+
[source,terminal]
----
export NODE_SELECTOR=node-role.kubernetes.io/master
----

.. Configure AWS CLI profiles as environment variables for account switching by running the following commands:
+
[source,terminal]
----
export AWS_ACCOUNT_A="<ACCOUNT_A_NAME>"
export AWS_ACCOUNT_B="<ACCOUNT_B_NAME>"
----

.. Ensure that your AWS CLI is configured with JSON output format as the default for both accounts by running the following commands:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_A}
aws configure get output
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
aws configure get output
----
+
If the preceding commands return:
+
* *No value*: The default output format is already set to JSON and no changes are required.
+
* *Any value*: Reconfigure your AWS CLI to use JSON format. For information about changing output formats, see _Setting the output format in the AWS CLI_ in the AWS documentation.

.. Unset `AWS_PROFILE` in your shell to prevent conflicts with `AWS_DEFAULT_PROFILE` by running the following command:
+
[source,terminal]
----
unset AWS_PROFILE
----

. Configure the AWS Account B IAM roles and policies:

.. Switch to your Account B profile by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
----

.. Define the IAM role name for the EFS CSI Driver Operator by running the following command:
+
[source,terminal]
----
export ACCOUNT_B_ROLE_NAME=${CLUSTER_NAME}-cross-account-aws-efs-csi-operator
----

.. Create the IAM trust policy file by running the following command:
+
[source,terminal]
----
cat <<EOF > $SCRATCH_DIR/AssumeRolePolicyInAccountB.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::${AWS_ACCOUNT_A_ID}:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}
EOF
----

.. Create the IAM role for the EFS CSI Driver Operator by running the following command:
+
[source,terminal]
----
ACCOUNT_B_ROLE_ARN=$(aws iam create-role \
  --role-name "${ACCOUNT_B_ROLE_NAME}" \
  --assume-role-policy-document file://$SCRATCH_DIR/AssumeRolePolicyInAccountB.json \
  --query "Role.Arn" --output text) \
&& echo $ACCOUNT_B_ROLE_ARN
----

.. Create the IAM policy file by running the following command:
+
[source,terminal]
----
cat << EOF > $SCRATCH_DIR/EfsPolicyInAccountB.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSubnets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:DescribeMountTargets",
                "elasticfilesystem:DeleteAccessPoint",
                "elasticfilesystem:ClientMount",
                "elasticfilesystem:DescribeAccessPoints",
                "elasticfilesystem:ClientWrite",
                "elasticfilesystem:ClientRootAccess",
                "elasticfilesystem:DescribeFileSystems",
                "elasticfilesystem:CreateAccessPoint",
                "elasticfilesystem:TagResource"
            ],
            "Resource": "*"
        }
    ]
}
EOF
----

.. Create the IAM policy by running the following command:
+
[source,terminal]
----
ACCOUNT_B_POLICY_ARN=$(aws iam create-policy --policy-name "${CLUSTER_NAME}-efs-csi-policy" \
   --policy-document file://$SCRATCH_DIR/EfsPolicyInAccountB.json \
   --query 'Policy.Arn' --output text) \
&& echo ${ACCOUNT_B_POLICY_ARN}
----

.. Attach the policy to the role by running the following command:
+
[source,terminal]
----
aws iam attach-role-policy \
   --role-name "${ACCOUNT_B_ROLE_NAME}" \
   --policy-arn "${ACCOUNT_B_POLICY_ARN}"
----

. Configure the AWS Account A IAM roles and policies:

.. Switch to your Account A profile by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_A}
----

.. Create the IAM policy document by running the following command:
+
[source,terminal]
----
cat << EOF > $SCRATCH_DIR/AssumeRoleInlinePolicyPolicyInAccountA.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "${ACCOUNT_B_ROLE_ARN}"
    }
  ]
}
EOF
----

.. In AWS Account A, attach the AWS-managed policy "AmazonElasticFileSystemClientFullAccess" to the OpenShift Container Platform cluster master role by running the following command:
+
[source,terminal]
----
EFS_CLIENT_FULL_ACCESS_BUILTIN_POLICY_ARN=arn:aws:iam::aws:policy/AmazonElasticFileSystemClientFullAccess
declare -A ROLE_SEEN
for NODE in $(oc get nodes --selector="${NODE_SELECTOR}" -o jsonpath='{.items[*].metadata.name}'); do
    INSTANCE_PROFILE=$(aws ec2 describe-instances \
        --filters "Name=private-dns-name,Values=${NODE}" \
        --query 'Reservations[].Instances[].IamInstanceProfile.Arn' \
        --output text | awk -F'/' '{print $NF}' | xargs)
    MASTER_ROLE_ARN=$(aws iam get-instance-profile \
        --instance-profile-name "${INSTANCE_PROFILE}" \
        --query 'InstanceProfile.Roles[0].Arn' \
        --output text | xargs)
    MASTER_ROLE_NAME=$(echo "${MASTER_ROLE_ARN}" | awk -F'/' '{print $NF}' | xargs)
    echo "Checking role: '${MASTER_ROLE_NAME}'"
    if [[ -n "${ROLE_SEEN[$MASTER_ROLE_NAME]:-}" ]]; then
        echo "Already processed role: '${MASTER_ROLE_NAME}', skipping."
        continue
    fi
    ROLE_SEEN["$MASTER_ROLE_NAME"]=1
    echo "Assigning policy ${EFS_CLIENT_FULL_ACCESS_BUILTIN_POLICY_ARN} to role ${MASTER_ROLE_NAME}"
    aws iam attach-role-policy --role-name "${MASTER_ROLE_NAME}" --policy-arn "${EEFS_CLIENT_FULL_ACCESS_BUILTIN_POLICY_ARN}"
done
----

. Attach the policy to the IAM entity to allow role assumption:
+
This step depends on your cluster configuration. In both of the following scenarios, the EFS CSI Driver Operator uses an entity to authenticate to AWS, and this entity must be granted permission to assume roles in Account B.
+
If your cluster:
+
* *Does not have STS enabled*: The EFS CSI Driver Operator uses an IAM User entity for AWS authentication. Continue with the step "Attach policy to IAM User to allow role assumption".
+
* *Has STS enabled*: The EFS CSI Driver Operator uses an IAM role entity for AWS authentication. Continue with the step "Attach policy to IAM Role to allow role assumption".

. Attach policy to IAM User to allow role assumption

.. Identify the IAM User used by the EFS CSI Driver Operator by running the following command:
+
[source,terminal]
----
EFS_CSI_DRIVER_OPERATOR_USER=$(oc -n openshift-cloud-credential-operator get credentialsrequest/openshift-aws-efs-csi-driver -o json | jq -r '.status.providerStatus.user')
----

.. Attach the policy to the IAM user by running the following command:
+
[source,terminal]
----
aws iam put-user-policy \
    --user-name "${EFS_CSI_DRIVER_OPERATOR_USER}"  \
    --policy-name efs-cross-account-inline-policy \
    --policy-document file://$SCRATCH_DIR/AssumeRoleInlinePolicyPolicyInAccountA.json
----

. Attach the policy to the IAM role to allow role assumption:

.. Identify the IAM role name currently used by the EFS CSI Driver Operator by running the following command:
+
[source,terminal]
----
EFS_CSI_DRIVER_OPERATOR_ROLE=$(oc -n ${CSI_DRIVER_NAMESPACE} get secret/aws-efs-cloud-credentials -o jsonpath='{.data.credentials}' | base64 -d | grep role_arn | cut -d'/' -f2) && echo ${EFS_CSI_DRIVER_OPERATOR_ROLE}
----

.. Attach the policy to the IAM role used by the EFS CSI Driver Operator by running the following command:
+
[source,terminal]
----
 aws iam put-role-policy \
    --role-name "${EFS_CSI_DRIVER_OPERATOR_ROLE}"  \
    --policy-name efs-cross-account-inline-policy \
    --policy-document file://$SCRATCH_DIR/AssumeRoleInlinePolicyPolicyInAccountA.json
----

. Configure VPC peering:

.. Initiate a peering request from Account A to Account B by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_A}
PEER_REQUEST_ID=$(aws ec2 create-vpc-peering-connection --vpc-id "${AWS_ACCOUNT_A_VPC_ID}" --peer-vpc-id "${AWS_ACCOUNT_B_VPC_ID}" --peer-owner-id "${AWS_ACCOUNT_B_ID}" --query VpcPeeringConnection.VpcPeeringConnectionId --output text)
----

.. Accept the peering request from Account B by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id "${PEER_REQUEST_ID}"
----

.. Retrieve the route table IDs for Account A and add routes to the Account B VPC by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_A}
for NODE in $(oc get nodes --selector=node-role.kubernetes.io/worker | tail -n +2 | awk '{print $1}')
do
    SUBNET=$(aws ec2 describe-instances --filters "Name=private-dns-name,Values=$NODE" --query 'Reservations[*].Instances[*].NetworkInterfaces[*].SubnetId' | jq -r '.[0][0][0]')
    echo SUBNET is ${SUBNET}
    ROUTE_TABLE_ID=$(aws ec2 describe-route-tables --filters "Name=association.subnet-id,Values=${SUBNET}" --query 'RouteTables[*].RouteTableId' | jq -r '.[0]')
    echo Route table ID is $ROUTE_TABLE_ID
    aws ec2 create-route --route-table-id ${ROUTE_TABLE_ID} --destination-cidr-block ${AWS_ACCOUNT_B_VPC_CIDR} --vpc-peering-connection-id ${PEER_REQUEST_ID}
done
----

.. Retrieve the route table IDs for Account B and add routes to the Account A VPC by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
for ROUTE_TABLE_ID in $(aws ec2 describe-route-tables   --filters "Name=vpc-id,Values=${AWS_ACCOUNT_B_VPC_ID}"   --query "RouteTables[].RouteTableId" | jq -r '.[]')
do
    echo Route table ID is $ROUTE_TABLE_ID
    aws ec2 create-route --route-table-id ${ROUTE_TABLE_ID} --destination-cidr-block ${AWS_ACCOUNT_A_VPC_CIDR} --vpc-peering-connection-id ${PEER_REQUEST_ID}
done
----

. Configure security groups in Account B to allow NFS traffic from Account A to EFS:

.. Switch to your Account B profile by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
----

.. Configure the VPC security groups for EFS access by running the following command:
+
[source,terminal]
----
SECURITY_GROUP_ID=$(aws ec2 describe-security-groups --filters Name=vpc-id,Values="${AWS_ACCOUNT_B_VPC_ID}" | jq -r '.SecurityGroups[].GroupId')
aws ec2 authorize-security-group-ingress \
 --group-id "${SECURITY_GROUP_ID}" \
 --protocol tcp \
 --port 2049 \
 --cidr "${AWS_ACCOUNT_A_VPC_CIDR}" | jq .
----

. Create a region-wide EFS filesystem in Account B:

.. Switch to your Account B profile by running the following command:
+
[source,terminal]
----
export AWS_DEFAULT_PROFILE=${AWS_ACCOUNT_B}
----

.. Create a region-wide EFS file system by running the following command:
+
[source,terminal]
----
CROSS_ACCOUNT_FS_ID=$(aws efs create-file-system --creation-token efs-token-1 \
--region ${AWS_REGION} \
--encrypted | jq -r '.FileSystemId') \
&& echo $CROSS_ACCOUNT_FS_ID
----

.. Configure region-wide mount targets for EFS by running the following command:
+
[source,terminal]
----
for SUBNET in $(aws ec2 describe-subnets \
  --filters "Name=vpc-id,Values=${AWS_ACCOUNT_B_VPC_ID}" \
  --region ${AWS_REGION} \
  | jq -r '.Subnets.[].SubnetId'); do \
    MOUNT_TARGET=$(aws efs create-mount-target --file-system-id ${CROSS_ACCOUNT_FS_ID} \
    --subnet-id ${SUBNET} \
    --region ${AWS_REGION} \
    | jq -r '.MountTargetId'); \
    echo ${MOUNT_TARGET}; \
done
----
+
This creates a mount point in each subnet of your VPC.

. Configure the EFS Operator for cross-account access:

.. Define custom names for the secret and storage class that you will create in subsequent steps by running the following command:
+
[source,terminal]
----
export SECRET_NAME=my-efs-cross-account
export STORAGE_CLASS_NAME=efs-sc-cross
----

.. Create a secret that references the role ARN in Account B by running the following command in the OpenShift Container Platform CLI:
+
[source,terminal]
----
oc create secret generic ${SECRET_NAME} -n ${CSI_DRIVER_NAMESPACE} --from-literal=awsRoleArn="${ACCOUNT_B_ROLE_ARN}"
----

.. Grant the CSI driver controller access to the newly created secret by running the following commands in the OpenShift Container Platform CLI:
+
[source,terminal]
----
oc -n ${CSI_DRIVER_NAMESPACE} create role access-secrets --verb=get,list,watch --resource=secrets
oc -n ${CSI_DRIVER_NAMESPACE} create rolebinding --role=access-secrets default-to-secrets --serviceaccount=${CSI_DRIVER_NAMESPACE}:aws-efs-csi-driver-controller-sa
----

.. Create a new storage class that references the EFS ID from Account B and the secret created previously by running the following command in the OpenShift Container Platform CLI:
+
[source,terminal]
----
cat << EOF | oc apply -f -
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: ${STORAGE_CLASS_NAME}
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap
  fileSystemId: ${CROSS_ACCOUNT_FS_ID}
  directoryPerms: "700"
  gidRangeStart: "1000"
  gidRangeEnd: "2000"
  basePath: "/dynamic_provisioning"
  csi.storage.k8s.io/provisioner-secret-name: ${SECRET_NAME}
  csi.storage.k8s.io/provisioner-secret-namespace: ${CSI_DRIVER_NAMESPACE}
EOF
----

[role="_additional-resources"]
.Additional resources
* Setting the output format in the AWS CLI

== One Zone file systems

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//
[id="efs-one-zone-overview_{context}"]
= One Zone file systems overview

OpenShift Container Platform supports AWS Elastic File System (EFS) One Zone file system, which is an EFS storage option that stores data redundantly within a single Availability Zone (AZ). This contrasts with the default EFS storage option, which stores data redundantly across multiple AZs within a region.

Clusters upgraded from OpenShift Container Platform 4.19 are compatible with the regional EFS volumes.

[NOTE]
====
Dynamic provisioning of One Zone volumes is supported only in single-zone clusters. All nodes in the cluster must be in the same AZ as the EFS volume that is used for the dynamic provisioning.

Manually provisioned One Zone volumes in regional clusters is supported, assuming that the persistent volumes (PVs) have correct `spec.nodeAffinity` that indicates the zone that the volume is in.
====

For Cloud Credential Operator (CCO) Mint mode or Passthrough, no extra configuration is required. However, for Security Token Service (STS), use the procedure in Section _Setting up One Zone file systems with STS_.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//
[id="efs-one-zone-procedure_{context}"]
= Setting up One Zone file systems with STS

The following procedure explains how to set up AWS One Zone file systems with Security Token Service (STS):

.Prerequisites
* Access to the cluster as a user with the cluster-admin role.

* AWS account credentials

.Procedure

To configure One Zone file systems with STS:

. Create *two* `CredentialsRequests` in the `credrequests` directory following the procedure under Section _Obtaining a role Amazon Resource Name for Security Token Service_.:
+
* For the *controller* `CredentialsRequest`, follow the procedure without any changes.

* For the *driver node* `CredentialsRequest` use the following example file:
+
.Example CredentialsRequest YAML file for driver node
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  annotations:
    credentials.openshift.io/role-arns-vars: NODE_ROLEARN <1>
  name: openshift-aws-efs-csi-driver-node
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - action:
      - elasticfilesystem:DescribeMountTargets
      - ec2:DescribeAvailabilityZones
      effect: Allow
      resource: '*'
  secretRef:
    name: node-aws-efs-cloud-credentials
    namespace: openshift-cluster-csi-drivers
  serviceAccountNames:
  - aws-efs-csi-driver-node-sa
----
<1> Set `metadata.annotations.credentials.openshift.io/role-arns-vars` to `NODE_ROLEARN`.
+
.Example `ccoctl` output
[source,terminal]
----
2025/08/26 14:05:24 Role arn:aws:iam::269733383066:role/my-arn-1-blll6-openshift-cluster-csi-drivers-aws-efs-cloud-cre created <1>
2025/08/26 14:05:24 Saved credentials configuration to: /home/my-arn/project/go/src/github.com/openshift/myinst/aws-sts-compact-1/manifests/openshift-cluster-csi-drivers-aws-efs-cloud-credentials-credentials.yaml
2025/08/26 14:05:24 Updated Role policy for Role my-arn-1-blll6-openshift-cluster-csi-drivers-aws-efs-cloud-cre
2025/08/26 14:05:24 Role arn:aws:iam::269733383066:role/my-arn-1-blll6-openshift-cluster-csi-drivers-node-aws-efs-clou created <2>
2025/08/26 14:05:24 Saved credentials configuration to: manifests/openshift-cluster-csi-drivers-node-aws-efs-cloud-credentials-credentials.yaml
2025/08/26 14:05:24 Updated Role policy for Role my-arn-1-blll6-openshift-cluster-csi-drivers-node-aws-efs-clou
----
<1> Controller Amazon Resource Name (ARN)
<2> Driver node ARN

. Install the AWS EFS CSI driver using the controller ARN created earlier in this procedure.

. Edit the operator's subscription and add `NODE_ROLEARN` with the driver node's ARN by running a command similar to the following:
+
[source,terminal]
----
$ oc -n openshift-cluster-csi-drivers edit subscription aws-efs-csi-driver-operator
...
  config:
    env:
    - name: ROLEARN
      value: arn:aws:iam::269733383066:role/my-arn-1-blll6-openshift-cluster-csi-drivers-aws-efs-cloud-cre <1>
    - name: NODE_ROLEARN
      value: arn:aws:iam::269733383066:role/my-arn-1-blll6-openshift-cluster-csi-drivers-node-aws-efs-clou <2>
...
----
<1> Controller ARN. Already exists.
<2> Driver node ARN

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-dynamic-provisioning-aws-efs_{context}"]
= Dynamic provisioning for Amazon Elastic File Storage

[role="_abstract"]
The AWS EFS CSI driver supports a different form of dynamic provisioning than other CSI drivers. It provisions new PVs as subdirectories of a pre-existing EFS volume. The PVs are independent of each other. However, they all share the same EFS volume. When the volume is deleted, all PVs provisioned out of it are deleted too.
The EFS CSI driver creates an AWS Access Point for each such subdirectory. Due to AWS AccessPoint limits, you can only dynamically provision 1000 PVs from a single `StorageClass`/EFS volume.

[IMPORTANT]
====
Note that `PVC.spec.resources` is not enforced by EFS.

In the example below, you request 5 GiB of space. However, the created PV is limitless and can store any amount of data (like petabytes). A broken application, or even a rogue application, can cause significant expenses when it stores too much data on the volume.

Using monitoring of EFS volume sizes in AWS is strongly recommended.
====

.Prerequisites

* You have created Amazon Elastic File Storage (Amazon EFS) volumes.
* You have created the AWS EFS storage class.

.Procedure

To enable dynamic provisioning:

* Create a PVC (or StatefulSet or Template) as usual, referring to the `StorageClass` created previously.
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test
spec:
  storageClassName: efs-sc
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
----

If you have problems setting up dynamic provisioning, see AWS EFS troubleshooting.
[role="_additional-resources"]
.Additional resources

* Creating the AWS EFS storage class

// Undefine {StorageClass} attribute, so that any mistakes are easily spotted

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="efs-create-static-pv_{context}"]
= Creating static PVs with Amazon Elastic File Storage

It is possible to use an Amazon Elastic File Storage (Amazon EFS) volume as a single PV without any dynamic provisioning. The whole volume is mounted to pods.

.Prerequisites

* You have created Amazon EFS volumes.

.Procedure

* Create the PV using the following YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity: <1>
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  csi:
    driver: efs.csi.aws.com
    volumeHandle: fs-ae66151a <2>
    volumeAttributes:
      encryptInTransit: "false" <3>
----
<1> `spec.capacity` does not have any meaning and is ignored by the CSI driver. It is used only when binding to a PVC. Applications can store any amount of data to the volume.
<2> `volumeHandle` must be the same ID as the EFS volume you created in AWS. If you are providing your own access point, `volumeHandle` should be ``<EFS volume ID>::<access point ID>``. For example: `fs-6e633ada::fsap-081a1d293f0004630`.
<3> If desired, you can disable encryption in transit. Encryption is enabled by default.

If you have problems setting up static PVs, see AWS EFS troubleshooting.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="efs-security_{context}"]
= Amazon Elastic File Storage security

The following information is important for Amazon Elastic File Storage (Amazon EFS) security.

When using access points, for example, by using dynamic provisioning as described earlier, Amazon automatically replaces GIDs on files with the GID of the access point. In addition, EFS considers the user ID, group ID, and secondary group IDs of the access point when evaluating file system permissions. EFS ignores the NFS client's IDs. For more information about access points, see https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html.

As a consequence, EFS volumes silently ignore FSGroup; OpenShift Container Platform is not able to replace the GIDs of files on the volume with FSGroup. Any pod that can access a mounted EFS access point can access any file on it.

Unrelated to this, encryption in transit is enabled by default. For more information, see https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html.

== AWS EFS storage CSI usage metrics
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//
[id="efs-metrics-overview_{context}"]
= Usage metrics overview

Amazon Web Services (AWS) Elastic File Service (EFS) storage Container Storage Interface (CSI) usage metrics allow you to monitor how much space is used by either dynamically or statically provisioned EFS volumes.

[IMPORTANT]
====
This features is disabled by default, because turning on metrics can lead to performance degradation.
====

The AWS EFS usage metrics feature collects volume metrics in the AWS EFS CSI Driver by recursively walking through the files in the volume. Because this effort can degrade performance, administrators must explicitly enable this feature.

//:FeatureName: AWS EFS usage metrics
// Commenting this out for now because we anticipate GA status.
// include::snippets/technology-preview.adoc[leveloffset=+2]

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//
[id="efs-metrics-procedure-gui_{context}"]
= Enabling usage metrics using the web console

To enable Amazon Web Services (AWS) Elastic File Service (EFS) Storage Container Storage Interface (CSI) usage metrics using the web console:

. Click *Administration* > *CustomResourceDefinitions*.

. On the *CustomResourceDefinitions* page next to the *Name* dropdown box, type `clustercsidriver`.

. Click *CRD ClusterCSIDriver*.

. Click the *YAML* tab.

. Under `spec.aws.efsVolumeMetrics.state`, set the value to `RecursiveWalk`.
+
`RecursiveWalk` indicates that volume metrics collection in the AWS EFS CSI Driver is performed by recursively walking through the files in the volume.
+
.Example ClusterCSIDriver efs.csi.aws.com YAML file
[source, yaml]
----
spec:
    driverConfig:
        driverType: AWS
        aws:
            efsVolumeMetrics:
              state: RecursiveWalk
              recursiveWalk:
                refreshPeriodMinutes: 100
                fsRateLimit: 10
----

. Optional: To define how the recursive walk operates, you can also set the following fields:
+
** `refreshPeriodMinutes`: Specifies the refresh frequency for volume metrics in minutes. If this field is left blank, a reasonable default is chosen, which is subject to change over time. The current default is 240 minutes. The valid range is 1 to 43,200 minutes.
** `fsRateLimit`: Defines the rate limit for processing volume metrics in goroutines per file system. If this field is left blank, a reasonable default is chosen, which is subject to change over time. The current default is 5 goroutines. The valid range is 1 to 100 goroutines.

. Click *Save*.

[NOTE]
====
To *disable* AWS EFS CSI usage metrics, use the preceding procedure, but for `spec.aws.efsVolumeMetrics.state`, change the value from `RecursiveWalk` to `Disabled`.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
//
[id="efs-metrics-procedure-cli_{context}"]
= Enabling usage metrics using the CLI

To enable Amazon Web Services (AWS) Elastic File Service (EFS) storage Container Storage Interface (CSI) usage metrics using the CLI:

. Edit ClusterCSIDriver by running the following command:
+
[source, terminal]
----
$ oc edit clustercsidriver efs.csi.aws.com
----

. Under `spec.aws.efsVolumeMetrics.state`, set the value to `RecursiveWalk`.
+
`RecursiveWalk` indicates that volume metrics collection in the AWS EFS CSI Driver is performed by recursively walking through the files in the volume.
+
.Example ClusterCSIDriver efs.csi.aws.com YAML file
[source, yaml]
----
spec:
    driverConfig:
        driverType: AWS
        aws:
            efsVolumeMetrics:
              state: RecursiveWalk
              recursiveWalk:
                refreshPeriodMinutes: 100
                fsRateLimit: 10
----

. Optional: To define how the recursive walk operates, you can also set the following fields:
+
** `refreshPeriodMinutes`: Specifies the refresh frequency for volume metrics in minutes. If this field is left blank, a reasonable default is chosen, which is subject to change over time. The current default is 240 minutes. The valid range is 1 to 43,200 minutes.
** `fsRateLimit`: Defines the rate limit for processing volume metrics in goroutines per file system. If this field is left blank, a reasonable default is chosen, which is subject to change over time. The current default is 5 goroutines. The valid range is 1 to 100 goroutines.

. Save the changes to the `efs.csi.aws.com` object.

[NOTE]
====
To *disable* AWS EFS CSI usage metrics, use the preceding procedure, but for `spec.aws.efsVolumeMetrics.state`, change the value from `RecursiveWalk` to `Disabled`.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="efs-troubleshooting_{context}"]
= Amazon Elastic File Storage troubleshooting

The following information provides guidance on how to troubleshoot issues with Amazon Elastic File Storage (Amazon EFS):

* The AWS EFS Operator and CSI driver run in namespace `openshift-cluster-csi-drivers`.

* To initiate gathering of logs of the AWS EFS Operator and CSI driver, run the following command:
+
[source,terminal]
----
$ oc adm must-gather
[must-gather      ] OUT Using must-gather plugin-in image: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:125f183d13601537ff15b3239df95d47f0a604da2847b561151fedd699f5e3a5
[must-gather      ] OUT namespace/openshift-must-gather-xm4wq created
[must-gather      ] OUT clusterrolebinding.rbac.authorization.k8s.io/must-gather-2bd8x created
[must-gather      ] OUT pod for plug-in image quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:125f183d13601537ff15b3239df95d47f0a604da2847b561151fedd699f5e3a5 created
----

* To show AWS EFS Operator errors, view the `ClusterCSIDriver` status:
+
[source,terminal]
----
$ oc get clustercsidriver efs.csi.aws.com -o yaml
----

* If a volume cannot be mounted to a pod (as shown in the output of the following command):
+
[source,terminal]
----
$ oc describe pod
...
  Type     Reason       Age    From               Message
  ----     ------       ----   ----               -------
  Normal   Scheduled    2m13s  default-scheduler  Successfully assigned default/efs-app to ip-10-0-135-94.ec2.internal
  Warning  FailedMount  13s    kubelet            MountVolume.SetUp failed for volume "pvc-d7c097e6-67ec-4fae-b968-7e7056796449" : rpc error: code = DeadlineExceeded desc = context deadline exceeded <1>
  Warning  FailedMount  10s    kubelet            Unable to attach or mount volumes: unmounted volumes=[persistent-storage], unattached volumes=[persistent-storage kube-api-access-9j477]: timed out waiting for the condition
----
<1> Warning message indicating volume not mounted.
+
This error is frequently caused by AWS dropping packets between an OpenShift Container Platform node and Amazon EFS.
+
Check that the following are correct:
+
--
* AWS firewall and Security Groups

* Networking: port number and IP addresses
--

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="persistent-storage-csi-olm-operator-uninstall_{context}"]
= Uninstalling the {FeatureName} CSI Driver Operator

All EFS PVs are inaccessible after uninstalling the AWS EFS CSI Driver Operator (a Red Hat operator).

.Prerequisites
* Access to the OpenShift Container Platform web console.

.Procedure
To uninstall the {FeatureName} CSI Driver Operator from the web console:

. Log in to the web console.

. Stop all applications that use {FeatureName} PVs.

. Delete all {FeatureName} PVs:

.. Click *Storage* -> *PersistentVolumeClaims*.

.. Select each PVC that is in use by the {FeatureName} CSI Driver Operator, click the drop-down menu on the far right of the PVC, and then click *Delete PersistentVolumeClaims*.

. Uninstall the https://github.com/openshift/aws-efs-csi-driver[{FeatureName} CSI driver]:
+
[NOTE]
====
Before you can uninstall the Operator, you must remove the CSI driver first.
====

.. Click *Administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.

.. On the *Instances* tab, for *{provisioner}*, on the far left side, click the drop-down menu, and then click *Delete ClusterCSIDriver*.

.. When prompted, click *Delete*.

. Uninstall the {FeatureName} CSI Operator:

.. Click *Ecosystem* -> *Installed Operators*.

.. On the *Installed Operators* page, scroll or type {FeatureName} CSI into the *Search by name* box to find the Operator, and then click it.

.. On the upper, right of the *Installed Operators > Operator details* page, click *Actions* -> *Uninstall Operator*.

.. When prompted on the *Uninstall Operator* window, click the *Uninstall* button to remove the Operator from the namespace. Any applications deployed by the Operator on the cluster need to be cleaned up manually.
+
After uninstalling, the {FeatureName} CSI Driver Operator is no longer listed in the *Installed Operators* section of the web console.

[NOTE]
====
Before you can destroy a cluster (`openshift-install destroy cluster`), you must delete the EFS volume in AWS.
A OpenShift Container Platform cluster cannot be destroyed when there is an EFS volume that uses the cluster's VPC. Amazon does not allow deletion of such a VPC.
An OpenShift Container Platform cluster cannot be destroyed when there is an EFS volume that uses the cluster's VPC. Amazon does not allow deletion of such a VPC.
====

[role="_additional-resources"]
== Additional resources
* Configuring CSI volumes
