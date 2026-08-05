---
title: "{product-title} IAM role resources"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-sts-ocm-role
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-sts-ocm-role
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# {product-title} IAM role resources

[id="rosa-sts-ocm-role"]
= OpenShift Container Platform IAM role resources

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

//Roles required to use {cluster-manager}

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

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
[id="rosa-sts-about-user-role_{context}"]
= About the user-role IAM role

[role="_abstract"]
You need to create a `user-role` IAM role per web UI user to enable those users to create OpenShift Container Platform clusters.

Some considerations for your `user-role` IAM role are:

* You only need one `user-role` IAM role per Red{nbsp}Hat user account, but your Red{nbsp}Hat organization can have many of these IAM resources.
* Any user in a Red{nbsp}Hat organization may create and link an `user-role` IAM role.
* There can be numerous `user-role` IAM roles per AWS account per Red{nbsp}Hat organization.
* Red{nbsp}Hat uses the `user-role` IAM role to identify the user. This IAM resource has no AWS account permissions.
* Your AWS account can have multiple `user-role` IAM roles, but you must link each IAM role to each user in your Red{nbsp}Hat organization. No user can have more than one linked `user-role` IAM role.

[NOTE]
====
"Linking" or "associating" your IAM resources with your AWS account means creating a trust-policy with your `user-role` IAM role and the Red{nbsp}Hat {cluster-manager} AWS role. After creating and linking this IAM resource, you see a trust relationship from your `user-role` IAM role in AWS with the `arn:aws:iam::710019948333:role/RH-Managed-OpenShift-Installer` resource.
====

// Module included in the following assemblies:
//
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-user-role-iam-basic-role_{context}"]
= Creating a user-role IAM role

[role="_abstract"]
You can create your `user-role` IAM roles by using the {rosa-cli-first}.

.Prerequisites

* You have an AWS account.
* You have installed and configured the latest {rosa-cli}, `rosa`, on your installation host.

.Procedure
* To create a `user-role` IAM role with basic privileges, run the following command:
+
[source,terminal]
----
$ rosa create user-role
----
+
This command allows you to create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the {rosa-cli} (`rosa`) to create your Operator roles and policies. See "Understanding the auto and manual deployment modes" for more information. The following example shows what your creation flow might look like.
+
[source,terminal]
----
I: Creating User role
? Role prefix: ManagedOpenShift
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating ocm user role using 'arn:aws:iam::2066:user'
? Create the 'ManagedOpenShift-User.osdocs-Role' role? Yes
I: Created role 'ManagedOpenShift-User.osdocs-Role' with ARN 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role'
I: Linking User role
? User Role ARN: arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role
? Link the 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role' role with account '1AGE'? Yes
I: Successfully linked role ARN 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role' with account '1AGE'
----
+
where:
+
--
`Role prefix`:: A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
`Permissions boundary ARN (optional)`:: The Amazon Resource Name (ARN) of the policy to set permission boundaries.
`Role Path (optional)`:: Specify an IAM path for the user name.
`Role creation mode`:: Choose the method to create your AWS roles. By using `auto`, the {rosa-cli} generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
`Create the 'ManagedOpenShift-User.osdocs-Role' role?`:: The `auto` method asks if you want to create a specific `user-role` by using your prefix.
`Link the 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role' role with account '1AGE'?`:: Links the created role with your AWS organization.
--
+
[IMPORTANT]
====
If you unlink or delete your `user-role` IAM role before deleting your cluster, an error prevents you from deleting your cluster. You must create or relink this role to proceed with the deletion process.
====

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-ocm-requirements_{context}"]
= Requirements for using {cluster-manager}

[role="_abstract"]
The following configuration details are required when using the {cluster-manager-url} or the CLI tools to manage your clusters.

[id="rosa-associating-concept_{context}"]
== AWS account association

When you provision OpenShift Container Platform using {cluster-manager} (`console.redhat.com`), you must associate the `ocm-role` and `user-role` IAM roles with your AWS account using your Amazon Resource Name (ARN). This association process is also known as _account linking_.

The `ocm-role` ARN is stored as a label in your Red{nbsp}Hat organization while the `user-role` ARN is stored as a label inside your Red{nbsp}Hat user account. Red{nbsp}Hat uses these ARN labels to confirm that the user is a valid account holder and that the correct permissions are available to perform provisioning tasks in the AWS account.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
[id="rosa-associating-account_{context}"]
= Associating your AWS account with IAM roles

[role="_abstract"]
You can associate or link your AWS account with existing IAM roles by using the {rosa-cli-first}.

.Prerequisites

* You have an AWS account.
* You have the permissions required to install AWS account-wide roles. See the "Additional resources" of this section for more information.
* You have installed and configured the latest AWS CLI (`aws`) and {rosa-cli} on your installation host.
* You have created the `ocm-role` and `user-role` IAM roles, but have not yet linked them to your AWS account. You can check whether your IAM roles are already linked by running the following commands:
+
[source,terminal]
----
$ rosa list ocm-role
----
+
[source,terminal]
----
$ rosa list user-role
----
+
If `Yes` is displayed in the `Linked` column for both roles, you have already linked the roles to an AWS account.

.Procedure

. In the ROSA CLI, link your `ocm-role` resource to your Red{nbsp}Hat organization by using your Amazon Resource Name (ARN):
+
[NOTE]
====
You must have Red{nbsp}Hat Organization Administrator privileges to run the `rosa link` command. After you link the `ocm-role` resource with your AWS account, it takes effect and is visible to all users in the organization.
====
+
[source,terminal]
----
$ rosa link ocm-role --role-arn <arn>
----
+
For example:
+
[source,terminal]
----
I: Linking OCM role
? Link the '<AWS ACCOUNT ID>` role with organization '<ORG ID>'? Yes
I: Successfully linked role-arn '<AWS ACCOUNT ID>' with organization account '<ORG ID>'
----
. In the ROSA CLI, link your `user-role` resource to your Red{nbsp}Hat user account by using your Amazon Resource Name (ARN):
+
[source,terminal]
----
$ rosa link user-role --role-arn <arn>
----
+
For example:
+
[source,terminal]
----
I: Linking User role
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-User-Role-125' role with organization '<AWS ID>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-User-Role-125' with organization account '<AWS ID>'
----

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-associating-multiple-account_{context}"]
= Associating multiple AWS accounts with your Red{nbsp}Hat organization

[role="_abstract"]
You can associate multiple AWS accounts with your Red{nbsp}Hat organization. Associating multiple accounts lets you create OpenShift Container Platform clusters on any of the associated AWS accounts from your Red{nbsp}Hat organization.

With this capability, you can create clusters on different AWS profiles according to characteristics that make sense for your business, for example, by using one AWS profile for each region to create region-bound environments.

.Prerequisites

* You have an AWS account.
* You are using {cluster-manager-url} to create clusters.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest AWS CLI (`aws`) and {rosa-cli-first} on your installation host.
* You have created the `ocm-role` and `user-role` IAM roles for OpenShift Container Platform.

.Procedure

* To specify an AWS account profile when creating an {cluster-manager} role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> ocm-role
----

* To specify an AWS account profile when creating a user role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> user-role
----

* To specify an AWS account profile when creating the account roles:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> account-roles
----
+
[NOTE]
====
If you do not specify a profile, the default AWS profile and its associated AWS region are used.
====

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
[id="rosa-sts-aws-requirements-attaching-boundary-policy_{context}"]
= Permission boundaries for the installer role

[role="_abstract"]
You can apply a policy as a _permissions boundary_ on an installer role. You can use an AWS-managed policy or a customer-managed policy to set the boundary for an Amazon Web Services (AWS) Identity and Access Management (IAM) entity (user or role). The combination of policy and boundary policy limits the maximum permissions for the user or role. OpenShift Container Platform includes a set of three prepared permission boundary policy files, with which you can restrict permissions for the installer role since changing the installer policy itself is not supported.

[NOTE]
====
This feature is only supported on {rosa-classic-title} clusters.
====

The permission boundary policy files are as follows:

* The _Core_ boundary policy file contains the minimum permissions needed for OpenShift Container Platform installer to install an OpenShift Container Platform cluster.
The installer does not have permissions to create a virtual private cloud (VPC) or PrivateLink (PL). A VPC needs to be provided.
* The _VPC_ boundary policy file contains the minimum permissions needed for OpenShift Container Platform installer to create/manage the VPC. It does not include permissions for PL or core installation. If you need to install a cluster with enough permissions for the installer to install the cluster and create/manage the VPC, but you do not need to set up PL, then use the core and VPC boundary files together with the installer role.
* The _PrivateLink (PL)_ boundary policy file contains the minimum permissions needed for OpenShift Container Platform installer to create the AWS PL with a cluster. It does not include permissions for VPC or core installation. Provide a pre-created VPC for all PL clusters during installation.

When using the permission boundary policy files, the following combinations apply:

* No permission boundary policies means that the full installer policy permissions apply to your cluster.
* *Core* only sets the most restricted permissions for the installer role. The VPC and PL permissions are not included in the *Core only* boundary policy.
** Installer cannot create or manage the VPC or PL.
** You must have a customer-provided VPC, and PrivateLink (PL) is not available.
* *Core + VPC* sets the core and VPC permissions for the installer role.
** Installer cannot create or manage the PL.
** Assumes you are not using custom/BYO-VPC.
** Assumes the installer will create and manage the VPC.
* *Core + PrivateLink (PL)* means the installer can provision the PL infrastructure.
** You must have a customer-provided VPC.
** This is for a private cluster with PL.

This example procedure is applicable for an installer role and policy with the most restriction of permissions, using only the _core_ installer permission boundary policy for OpenShift Container Platform. You can complete this with the AWS console or the AWS CLI. This example uses the AWS CLI and the following policy:

The following example shows `sts_installer_core_permission_boundary_policy.json`:
[source,json]
----

----

[IMPORTANT]
====
To use the permission boundaries, you will need to prepare the permission boundary policy and add it to your relevant installer role in AWS IAM. While the {rosa-cli-first} offers a permission boundary function, it applies to all roles and not just the installer role, which means it does not work with the provided permission boundary policies (which are only for the installer role).
====

.Prerequisites

* You have an AWS account.
* You have the permissions required to administer AWS roles and policies.
* You have installed and configured the latest AWS (`aws`) CLI and {rosa-cli} on your workstation.
* You have already prepared your OpenShift Container Platform account-wide roles, includes the installer role, and the corresponding policies. If these do not exist in your AWS account, see "Creating the account-wide STS roles and policies" in _Additional resources_.

.Procedure

. Prepare the policy file by entering the following command in the {rosa-cli}:
+
[source,terminal]
----
$ curl -o ./rosa-installer-core.json https://raw.githubusercontent.com/openshift/managed-cluster-config/master/resources/sts/4.21/sts_installer_core_permission_boundary_policy.json
----

. Create the policy in AWS and gather its Amazon Resource Name (ARN) by entering the following command:
+
[source,terminal]
----
$ aws iam create-policy \
--policy-name rosa-core-permissions-boundary-policy \
--policy-document file://./rosa-installer-core.json \
--description "ROSA installer core permission boundary policy, the minimum permission set, allows BYO-VPC, disallows PrivateLink"
----
+
For example:
+
[source,terminal]
----
{
    "Policy": {
        "PolicyName": "rosa-core-permissions-boundary-policy",
        "PolicyId": "<Policy ID>",
        "Arn": "arn:aws:iam::<account ID>:policy/rosa-core-permissions-boundary-policy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "<CreateDate>",
        "UpdateDate": "<UpdateDate>"
    }
}
----

. Add the permission boundary policy to the installer role you want to restrict by entering the following command:
+
[source,terminal]
----
$ aws iam put-role-permissions-boundary \
--role-name ManagedOpenShift-Installer-Role \
--permissions-boundary arn:aws:iam::<account ID>:policy/rosa-core-permissions-boundary-policy
----

. Display the installer role to validate attached policies (including permissions boundary) by entering the following command in the {rosa-cli}:
+
[source,terminal]
----
$ aws iam get-role --role-name ManagedOpenShift-Installer-Role \
--output text | grep PERMISSIONSBOUNDARY
----
+
For example:
+
[source,terminal]
----
PERMISSIONSBOUNDARY	arn:aws:iam::<account ID>:policy/rosa-core-permissions-boundary-policy	Policy
----
+
For more examples of PL and VPC permission boundary policies see:
+
The following example shows `sts_installer_privatelink_permission_boundary_policy.json`:
+
[source,json]
----

----
+
The following example shows `sts_installer_vpc_permission_boundary_policy.json`:
+
[source,json]
----

----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Permissions boundaries for IAM entities (AWS documentation)
* Repairing a cluster that cannot be deleted
* `ocm-role` IAM resource profiles
* Methods of account-wide role creation
* Account-wide IAM role and policy reference
* Cluster-specific Operator IAM role reference
* Creating the account-wide STS roles and policies
* Troubleshooting IAM roles
* Account-wide IAM role and policy reference
