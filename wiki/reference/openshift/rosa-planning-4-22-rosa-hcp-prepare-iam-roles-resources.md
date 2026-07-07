---
title: "Required IAM roles and resources"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-hcp-prepare-iam-roles-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-hcp-prepare-iam-roles-resources
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Required IAM roles and resources

[id="rosa-hcp-prepare-iam-roles-resources"]
= Required IAM roles and resources

[role="_abstract"]
You must create several role resources on your AWS account in order to create and manage a OpenShift Container Platform cluster.

// Module included in the following assemblies:
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-prereq-roles-overview_{context}"]
= Overview of required roles

[role="_abstract"]
To create and manage your OpenShift Container Platform cluster, you must create several account-wide and cluster-wide roles. If you intend to use {cluster-manager} to create or manage your cluster, you need some additional roles.

To create and manage clusters:: Several account-wide roles are required to create and manage OpenShift Container Platform clusters. These roles only need to be created once per AWS account, and do not need to be created fresh for each cluster. One or more AWS managed policies are attached to each role to grant that role the required capabilities. You can specify your own prefix, or use the default prefix (`ManagedOpenShift`).
+
[NOTE]
====
Role names are limited to a maximum length of 64 characters in AWS IAM. When the user-specified prefix for a cluster is longer than 20 characters, the role name is truncated to observe this 64-character maximum in AWS IAM.
====
+
For OpenShift Container Platform clusters, you must create the following account-wide roles and attach the indicated AWS managed policies:
+
.Required account roles and AWS policies for OpenShift Container Platform
[options="header"]
|===
| Role name | AWS policy names

| `<prefix>-HCP-ROSA-Worker-Role`
| `ROSAWorkerInstancePolicy` and `AmazonEC2ContainerRegistryReadOnly`

| `<prefix>-HCP-ROSA-Support-Role`
| `ROSASRESupportPolicy`

| `<prefix>-HCP-ROSA-Installer-Role`
| `ROSAInstallerPolicy`

|===
+
[IMPORTANT]
====
For enhanced security, you might want to include an external ID within the trust policies of the Support and Installer account-wide roles. For more information, see _About external ID_.
====
+
+
The following account-wide roles are required:

** `<prefix>-Worker-Role`
** `<prefix>-Support-Role`
** `<prefix>-Installer-Role`
** `<prefix>-ControlPlane-Role`

+
[NOTE]
====
Role creation does not request your AWS access or secret keys. AWS Security Token Service (STS) is used as the basis of this workflow. AWS STS uses temporary, limited-privilege credentials to provide authentication.
====

To use Operator-managed cluster capabilities:: Some cluster capabilities, including several capabilities provided by default, are managed using Operators. Cluster-specific Operator roles (`operator-roles` in the ROSA CLI) are required to use these capabilities. These roles are used to obtain the temporary permissions required to carry out cluster operations such as managing back-end storage, ingress, and registry. Obtaining these permissions requires the configuration of an OpenID Connect (OIDC) provider, which connects to AWS Security Token Service (STS) to authenticate Operator access to AWS resources.
+
The following Operator roles are required for OpenShift Container Platform clusters:

** `openshift-cluster-csi-drivers-ebs-cloud-credentials`
** `openshift-cloud-network-config-controller-cloud-credentials`
** `openshift-machine-api-aws-cloud-credentials`
** `openshift-cloud-credential-operator-cloud-credentials`
** `openshift-image-registry-installer-cloud-credentials`
** `openshift-ingress-operator-cloud-credentials`

+
+
For OpenShift Container Platform clusters, you must create the following Operator roles and attach the indicated AWS Managed policies:
+
.Required Operator roles and AWS Managed policies for OpenShift Container Platform
[options="header"]
|===
| Role name | AWS-managed policy name

| `openshift-cloud-network-config-controller-c`
| `ROSACloudNetworkConfigOperatorPolicy`

| `openshift-image-registry-installer-cloud-credentials`
| `ROSAImageRegistryOperatorPolicy`

| `kube-system-kube-controller-manager`
| `ROSAKubeControllerPolicy`

| `kube-system-capa-controller-manager`
| `ROSANodePoolManagementPolicy`

| `kube-system-control-plane-operator`
| `ROSAControlPlaneOperatorPolicy`

| `kube-system-kms-provider`
| `ROSAKMSProviderPolicy`

| `openshift-ingress-operator-cloud-credentials`
| `ROSAIngressOperatorPolicy`

| `openshift-cluster-csi-drivers-ebs-cloud-credentials`
| `ROSAAmazonEBSCSIDriverOperatorPolicy`

|===
+
When you create Operator roles using the `rosa create operator-role` command, the roles created are named using the pattern `<cluster_name>-<hash>-<role_name>`, for example, `test-abc1-kube-system-control-plane-operator`. When your cluster name is longer than 15 characters, the role name is truncated.

To use {cluster-manager}:: The web user interface, {cluster-manager}, requires you to create additional roles in your AWS account to create a trust relationship between that AWS account and the {cluster-manager}.
+
This trust relationship is achieved through the creation and association of the `ocm-role` AWS IAM role. This role has a trust policy with the AWS installer that links your Red{nbsp}Hat account to your AWS account. In addition, you also need a `user-role` AWS IAM role for each web UI user, which serves to identify these users. This `user-role` AWS IAM role has no permissions.
+
The following AWS IAM roles are required to use {cluster-manager}:

** `ocm-role`
** `user-role`

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-sts-creating-account-wide-sts-roles-and-policies_{context}"]
= Creating the account-wide STS roles and policies

[role="_abstract"]
Before you create a OpenShift Container Platform cluster, you must create the required account-wide IAM roles and policies by using the {rosa-cli-first}.

[NOTE]
====
Specific AWS-managed policies for OpenShift Container Platform must be attached to each role. Customer-managed policies must not be used with these required account roles. For more information regarding AWS-managed policies for OpenShift Container Platform clusters, see AWS managed policies for OpenShift Container Platform.
====

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform in the AWS Console.
* You have installed and configured the latest {rosa-cli-first} on your installation host.
* You have logged in to your Red{nbsp}Hat account by using the {rosa-cli}.

.Procedure

. If they do not exist in your AWS account, create the required account-wide STS roles and attach the policies by running the following command:
+
[source,terminal]
----
$ rosa create account-roles --hosted-cp
----
[source,terminal]
----
$ export PREFIX=<custom_prefix>; rosa create account-roles --hosted-cp --prefix $PREFIX
----
+
When using FIPS encryption, you need to set a custom prefix instead of using the default `ManagedOpenShift` prefix.

. Verify that your worker role has the correct AWS policy by running the following command:
+
[source,terminal]
----
$ aws iam attach-role-policy \
--role-name ManagedOpenShift-HCP-ROSA-Worker-Role \
--policy-arn "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
----
+
--
`--role-name ManagedOpenShift-HCP-ROSA-Worker-Role`::This role needs to include the prefix that was created in the previous step.
--

. Optional: Set your prefix as an environmental variable by running the following command:
+
[source,terminal]
----
$ export ACCOUNT_ROLES_PREFIX=<account_role_prefix>
----

** View the value of the variable by running the following command:
+
[source,terminal]
----
$ echo $ACCOUNT_ROLES_PREFIX
----
+
For example:
+
[source,terminal]
----
ManagedOpenShift
----

[NOTE]
====
As an additional safeguard, after role creation, you can manually update the trust policies of the Support and Installer account-wide roles to include an external ID. For more information, see _About external ID_.
====

[role="_additional-resources"]
.Additional resources

* AWS managed IAM policies for OpenShift Container Platform

// Module included in the following assemblies:
//
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-sts-byo-oidc_{context}"]
= Creating an OpenID Connect configuration

[role="_abstract"]
OpenShift Container Platform clusters use OIDC and the AWS Security Token Service (STS) to authenticate Operator access to AWS resources they require to perform their functions. Each production cluster requires its own OIDC configuration. When creating a OpenShift Container Platform cluster, you can create the OpenID Connect (OIDC) configuration before creating your cluster.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have installed and configured the latest {rosa-cli-first} on your installation host.

.Procedure

. To create your OIDC configuration alongside the AWS resources, run the following command:
+
[source,terminal]
----
$ rosa create oidc-config --mode=auto --yes
----
+
This command returns the following information.
+
For example:
+
[source,terminal]
----
? Would you like to create a Managed (Red Hat hosted) OIDC Configuration Yes
I: Setting up managed OIDC configuration
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 13cdr6b
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/13cdr6b'
----
+
When creating your cluster, you must supply the OIDC config ID. The CLI output provides this value for `--mode auto`, otherwise you must determine these values based on `aws` CLI output for `--mode manual`.

. Optional: you can save the OIDC configuration ID as a variable to use later. Run the following command to save the variable:
+
--
[source,terminal]
----
$ export OIDC_ID=<oidc_config_id>
----
`<oidc_config_id>`:: In this example output, the OIDC configuration ID is `13cdr6b`.
--

** View the value of the variable by running the following command:
+
[source,terminal]
----
$ echo $OIDC_ID
----
+
For example:
+
[source,terminal]
----
13cdr6b
----

.Verification

* You can list the possible OIDC configurations available for your clusters that are associated with your user organization. Run the following command:
+
[source,terminal]
----
$ rosa list oidc-config
----
+
For example:
+
[source,terminal]
----
ID                                MANAGED  ISSUER URL                                                             SECRET ARN
2330dbs0n8m3chkkr25gkkcd8pnj3lk2  true     https://dvbwgdztaeq9o.cloudfront.net/2330dbs0n8m3chkkr25gkkcd8pnj3lk2
233hvnrjoqu14jltk6lhbhf2tj11f8un  false    https://oidc-r7u1.s3.us-east-1.amazonaws.com                           aws:secretsmanager:us-east-1:242819244:secret:rosa-private-key-oidc-r7u1-tM3MDN
----

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc

[id="rosa-sts-operator-roles_{context}"]
= Cluster-specific Operator IAM role reference

[role="_abstract"]
Use Operator roles to authenticate to your AWS resources through an OpenID Connect (OIDC) provider, and obtain temporary permissions for cluster operations. Securing these permissions helps you successfully manage capabilities like back-end storage, cloud ingress controllers, and external cluster access.

When you create the Operator roles, the account-wide Operator policies for the matching cluster version are attached to the roles.
The Operator policies are tagged with the Operator and version they are compatible with. The correct policy for an Operator role is determined by using the tags.
AWS managed Operator policies are versioned in AWS IAM. The latest version of an AWS managed policy is always used, so you do not need to manage or schedule upgrades for AWS managed policies used by OpenShift Container Platform.

[NOTE]
====
If more than one matching policy is available in your account for an Operator role, an interactive list of options is provided when you create the role.
====

.ROSA cluster-specific Operator roles
[cols="1,2",options="header"]
|===

|Resource|Description

|`<cluster_name>-<hash>-openshift-cluster-csi-drivers-ebs-cloud-credentials`
|An IAM role required by OpenShift Container Platform to manage back-end storage through the Container Storage Interface (CSI).

|`<cluster_name>-<hash>-openshift-machine-api-aws-cloud-credentials`
|An IAM role required by the ROSA Machine Config Operator to perform core cluster functionality.

|`<cluster_name>-<hash>-openshift-cloud-credential-operator-cloud-credentials`
|An IAM role required by the ROSA Cloud Credential Operator to manage cloud provider credentials.

|`<cluster_name>-<hash>-openshift-cloud-network-config-controller-credentials`
|An IAM role required by the cloud network config controller to manage cloud network configuration for a cluster.

|`<cluster_name>-<hash>-openshift-image-registry-installer-cloud-credentials`
|An IAM role required by the ROSA Image Registry Operator to manage the {product-registry} storage in AWS S3 for a cluster.

|`<cluster_name>-<hash>-openshift-ingress-operator-cloud-credentials`
|An IAM role required by the ROSA Ingress Operator to manage external access to a cluster.

|`<cluster_name>-<hash>-openshift-cloud-network-config-controller-cloud-credentials`
|An IAM role required by the cloud network config controller to manage cloud network credentials for a cluster.

|===

.Required Operator roles and AWS Managed policies for OpenShift Container Platform
[options="header"]
|===
| Role name | AWS Managed policy name | Role description

| `openshift-cloud-network-config-controller-credentials`
| `ROSACloudNetworkConfigOperatorPolicy`
| An IAM role required by the cloud network config controller to manage cloud network credentials for a cluster.

| `openshift-image-registry-installer-cloud-credentials`
| `ROSAImageRegistryOperatorPolicy`
| An IAM role required by the OpenShift Container Platform Image Registry Operator to manage the {product-registry} storage in AWS S3 for a cluster.

| `kube-system-kube-controller-manager`
| `ROSAKubeControllerPolicy`
| An IAM role required for OpenShift management on hosted control planes (HCP) clusters.

| `kube-system-capa-controller-manager`
| `ROSANodePoolManagementPolicy`
| An IAM role required for node management on HCP clusters.

| `kube-system-control-plane-operator`
| `ROSAControlPlaneOperatorPolicy`
| An IAM role required for control plane management on HCP clusters.

| `kube-system-kms-provider`
| `ROSAKMSProviderPolicy`
| An IAM role required for OpenShift management on HCP clusters.

| `openshift-ingress-operator-cloud-credentials`
| `ROSAIngressOperatorPolicy`
|An IAM role required by the OpenShift Container Platform Ingress Operator to manage external access to a cluster.

| `openshift-cluster-csi-drivers-ebs-cloud-credentials`
| `ROSAAmazonEBSCSIDriverOperatorPolicy`
| An IAM role required by OpenShift Container Platform to manage back-end storage through the Container Storage Interface (CSI).

|===

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-operator-config_{context}"]
= Creating Operator roles and policies

[role="_abstract"]
When you deploy a OpenShift Container Platform cluster, you must create the Operator IAM roles. The cluster Operators use the Operator roles and policies to obtain temporary permissions to perform cluster operations, such as managing storage and external access.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have installed and configured the latest {rosa-cli-first} on your installation host.
* You created the account-wide AWS roles.

.Procedure
. To create your Operator roles, run the following command:
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp --prefix=$PREFIX --oidc-config-id=$OIDC_ID
----
+
The Operator roles are now created and ready to use for creating your OpenShift Container Platform cluster.
. To create your Operator roles, run the following command:
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp --prefix=$OPERATOR_ROLES_PREFIX --oidc-config-id=$OIDC_ID --installer-role-arn arn:aws:iam::$AWS_ACCOUNT_ID:role/${ACCOUNT_ROLES_PREFIX}-HCP-ROSA-Installer-Role
----
+
The following breakdown provides options for the Operator role creation.
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp
	--prefix=$OPERATOR_ROLES_PREFIX
	--oidc-config-id=$OIDC_ID
	--installer-role-arn arn:aws:iam::$AWS_ACCOUNT_ID:role/$ACCOUNT_ROLES_PREFIX-HCP-ROSA-Installer-Role
----
+
where:
+
--
`--prefix=`:: You must supply a prefix when creating these Operator roles. Failing to do so produces an error. See the Additional resources of this section for information on the Operator prefix.
`--oidc-config-id=`:: This value is the OIDC configuration ID that you created for your OpenShift Container Platform cluster.
`--installer-role-arn`:: This value is the installer role ARN that you created when you created the OpenShift Container Platform account roles.
--
+
You must include the `--hosted-cp` parameter to create the correct roles for OpenShift Container Platform clusters. This command returns the following information.
+
For example:
+
[source,terminal]
----
? Role creation mode: auto
? Operator roles prefix: <pre-filled_prefix>
? OIDC Configuration ID: 23soa2bgvpek9kmes9s7os0a39i13qm4 | https://dvbwgdztaeq9o.cloudfront.net/23soa2bgvpek9kmes9s7os0a39i13qm4
? Create hosted control plane operator roles: Yes
W: More than one Installer role found
? Installer role ARN: arn:aws:iam::4540112244:role/<prefix>-HCP-ROSA-Installer-Role
? Permissions boundary ARN (optional):
I: Reusable OIDC Configuration detected. Validating trusted relationships to operator roles:
I: Creating roles using 'arn:aws:iam::4540112244:user/<userName>'
I: Created role '<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials'
I: Created role '<prefix>-openshift-cloud-network-config-controller-cloud-credenti' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-cloud-network-config-controller-cloud-credenti'
I: Created role '<prefix>-kube-system-kube-controller-manager' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-kube-controller-manager'
I: Created role '<prefix>-kube-system-capa-controller-manager' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-capa-controller-manager'
I: Created role '<prefix>-kube-system-control-plane-operator' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-control-plane-operator'
I: Created role '<prefix>-kube-system-kms-provider' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-kms-provider'
I: Created role '<prefix>-openshift-image-registry-installer-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-image-registry-installer-cloud-credentials'
I: Created role '<prefix>-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-ingress-operator-cloud-credentials'
I: To create a cluster with these roles, run the following command:
	rosa create cluster --sts --oidc-config-id 23soa2bgvpek9kmes9s7os0a39i13qm4 --operator-roles-prefix <prefix> --hosted-cp
----
+
where:
+
--
`Operator roles prefix`:: This field is prepopulated with the prefix that you set in the initial creation command.
`OIDC Configuration ID`:: This field requires you to select an OIDC configuration that you created for your OpenShift Container Platform cluster.
--
+
The Operator roles are now created and ready to use for creating your OpenShift Container Platform cluster.

.Verification

* You can list the Operator roles associated with your OpenShift Container Platform account. Run the following command:
+
[source,terminal]
----
$ rosa list operator-roles
----
+
For example:
+
[source,terminal]
----
I: Fetching operator roles
ROLE PREFIX  AMOUNT IN BUNDLE
<prefix>      8
? Would you like to detail a specific prefix Yes
? Operator Role Prefix: <prefix>
ROLE NAME                                                         ROLE ARN                                                                                         VERSION  MANAGED
<prefix>-kube-system-capa-controller-manager                       arn:aws:iam::4540112244:role/<prefix>-kube-system-capa-controller-manager                       4.13     No
<prefix>-kube-system-control-plane-operator                        arn:aws:iam::4540112244:role/<prefix>-kube-system-control-plane-operator                        4.13     No
<prefix>-kube-system-kms-provider                                  arn:aws:iam::4540112244:role/<prefix>-kube-system-kms-provider                                  4.13     No
<prefix>-kube-system-kube-controller-manager                       arn:aws:iam::4540112244:role/<prefix>-kube-system-kube-controller-manager                       4.13     No
<prefix>-openshift-cloud-network-config-controller-cloud-credenti  arn:aws:iam::4540112244:role/<prefix>-openshift-cloud-network-config-controller-cloud-credenti  4.13     No
<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials       arn:aws:iam::4540112244:role/<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials       4.13     No
<prefix>-openshift-image-registry-installer-cloud-credentials      arn:aws:iam::4540112244:role/<prefix>-openshift-image-registry-installer-cloud-credentials      4.13     No
<prefix>-openshift-ingress-operator-cloud-credentials              arn:aws:iam::4540112244:role/<prefix>-openshift-ingress-operator-cloud-credentials              4.13     No
----
+
After the command runs, it displays all the prefixes associated with your AWS account and notes how many roles are associated with this prefix. If you need to see all of these roles and their details, enter "Yes" on the detail prompt to have these roles listed out with specifics.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
[id="rosa-sts-about-ocm-role_{context}"]
= About the ocm-role IAM resource

[role="_abstract"]
You must create the `ocm-role` IAM resource to enable a Red{nbsp}Hat organization of users to create OpenShift Container Platform clusters. Within the context of linking to AWS, a Red{nbsp}Hat organization is a single user within {cluster-manager}.

Some considerations for your `ocm-role` IAM resource are:

* Only one `ocm-role` IAM role can be linked per Red{nbsp}Hat organization; however, you can have any number of `ocm-role` IAM roles per AWS account. The web UI requires that only one of these roles can be linked at a time.
* Any user in a Red{nbsp}Hat organization may create and link an `ocm-role` IAM resource.
* You must create an `ocm-role` before you can create a OpenShift Container Platform cluster.
+
[NOTE]
====
If you are not using {cluster-manager} to create and manage clusters, you can use the `--no-console` profile to satisfy the `ocm-role` IAM resource requirement.
====
+
* Only the Red{nbsp}Hat Organization Administrator can unlink an `ocm-role` IAM resource. This limitation is to protect other Red{nbsp}Hat organization members from disturbing the interface capabilities of other users.
+
[NOTE]
====
If you just created a Red{nbsp}Hat account that is not part of an existing organization, this account is also the Red{nbsp}Hat Organization Administrator.
====
+
* See "Understanding the {cluster-manager} role" in the Additional resources of this section for a list of the AWS permissions policies for the basic and admin `ocm-role` IAM resources.

Using the {rosa-cli-first}, you can link your IAM resource when you create it.

[NOTE]
====
"Linking" or "associating" your IAM resources with your AWS account means creating a trust-policy with your `ocm-role` IAM role and the Red{nbsp}Hat {cluster-manager} AWS role. After creating and linking your IAM resource, you see a trust relationship from your `ocm-role` IAM resource in AWS with the `arn:aws:iam::12345678abcd:role/RH-Managed-OpenShift-Installer` resource.
====

After a Red{nbsp}Hat Organization Administrator has created and linked an `ocm-role` IAM resource, all organization members may want to create and link their own `user-role` IAM role. This IAM resource only needs to be created and linked only once per user. If another user in your Red{nbsp}Hat organization has already created and linked an `ocm-role` IAM resource, you need to ensure you have created and linked your own `user-role` IAM role.

[id="rosa-sts-about-ocm-role-profiles_{context}"]
== ocm-role IAM resource profiles

The `ocm-role` IAM resource exists with three profiles: no-console, standard, and admin. Each profile provides different levels of permissions and capabilities for managing OpenShift Container Platform clusters.

No-console profile::
+
--
The no-console profile provides the minimum permissions required for OpenShift Container Platform to function with the {rosa-cli-first}. This profile is insufficient for creating clusters by using the {cluster-manager} console.

* Available in {rosa-cli} version 1.2.64 and higher
* Allows cluster creation only through the {rosa-cli}, Terraform, or CAPA
* If you do not intend to use {cluster-manager} console for cluster creation, you can use the no-console profile and still comply with the requirement to create and link an `ocm-role` IAM resource

The no-console profile allows OpenShift Container Platform to assume the `ocm-role` IAM role and fetch details about the role itself so that the service can validate if your `ocm-role` is configured correctly.
--

Standard profile::
The standard profile is designed to support provisioning clusters through the {cluster-manager} console. This profile allows you to create OpenShift Container Platform clusters through {cluster-manager}, but the standard profile does not automatically create your OIDC configs and Operator roles.

Admin profile::
+
--
The admin profile is designed to provide support for automatically provisioning OIDC configs and Operator roles for your clusters.

* Enabled using the `--admin` parameter with the `rosa create ocm-role` command
* Supports auto mode configuration for {rosa-classic-title} clusters
* Provisions OIDC configuration and Operator roles on behalf of customers
* Requires a wider set of permissions than the standard profile
--

// Module included in the following assemblies:
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-ocm-roles-and-permissions-iam-basic-role_{context}"]
= Creating an ocm-role IAM role

[role="_abstract"]
You create your `ocm-role` IAM roles by using the {rosa-cli-first}. If you want to create and manage clusters by using only the {rosa-cli-first} and the OpenShift CLI (`oc`), you can use the `--no-console` profile for the `ocm-role` IAM resource. For more information about the `ocm-role` IAM resource permissions profile, see the _Additional resources_.

[IMPORTANT]
====
You must create the `ocm-role` IAM role before you can create your OpenShift Container Platform cluster.
====

.Prerequisites

* You have an AWS account.
* You have Red{nbsp}Hat Organization Administrator privileges in the {cluster-manager} organization.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest {rosa-cli}, `rosa`, on your installation host.

.Procedure
* Run one of the following commands to create the required `ocm-role` IAM resource:
+
[IMPORTANT]
====
The process to change your `ocm-role` IAM resource profile requires you to unlink and delete the current `ocm-role` IAM resource and create a new one with the required profile.
====

** To create an `ocm-role` IAM role with standard privileges, run the following command:
+
[source,terminal]
----
$ rosa create ocm-role
----
+
** To create an `ocm-role` IAM role with admin privileges, run the following command:
+
[IMPORTANT]
====
The admin profile supports "auto" mode configuration for OpenShift Container Platform clusters which provisions OIDC Configuration and Operator roles automatically. To achieve this automatic flow, the profile has a wider set of permissions than the standard profile.
====
+
[source,terminal]
----
$ rosa create ocm-role --admin
----
+
This command allows you to create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the {rosa-cli} (`rosa`) create your Operator roles and policies.
See "Methods of account-wide role creation" for more information. The following example shows what your creation flow might look like.
+
[source,terminal]
----
I: Creating ocm role
? Role prefix: ManagedOpenShift
? Enable admin capabilities for the OCM role (optional): No
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::<ARN>:user/<UserName>'
? Create the 'ManagedOpenShift-OCM-Role-182' role? Yes
I: Created role 'ManagedOpenShift-OCM-Role-182' with ARN  'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' with organization account '<AWS ARN>'
----
+
where:
+
--
`Role prefix`:: A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
`Enable admin capabilities for the OCM role (optional)`:: Choose if you want this role to have the additional admin permissions.
+
[NOTE]
====
You do not see this prompt if you used the `--admin` option.
====
+
`Permissions boundary ARN (optional)`:: The Amazon Resource Name (ARN) of the policy to set permission boundaries.
`Role Path (optional)`:: Specify an IAM path for the user name.
`Role creation mode`:: Choose the method to create your AWS roles. By using `auto`, the {rosa-cli} generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
`Create the 'ManagedOpenShift-OCM-Role-182' role?`:: The `auto` method asks if you want to create a specific `ocm-role` by using your prefix.
`OCM Role ARN`:: Confirm that you want to associate your IAM role with your {cluster-manager}.
`Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'?`:: Links the created role with your AWS organization.
--

** To create an `ocm-role` IAM role with the minimum required privileges, run the following command:
+
[NOTE]
====
While the `no-console` profile offers the minimum permissions policy that can still create OpenShift Container Platform clusters, the permissions are insufficient if you want to use {cluster-manager-url} for cluster creation.
====
+
[source,terminal]
----
$ rosa create ocm-role --no-console
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Methods of account-wide role creation
* AWS documentation for Managed IAM policies for OpenShift Container Platform clusters
* About external ID
