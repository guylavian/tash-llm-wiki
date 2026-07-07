---
title: "Troubleshooting IAM roles"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-iam-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-iam-resources
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting IAM roles

[id="rosa-troubleshooting-iam-resources"]
= Troubleshooting IAM roles

[role="_abstract"]
Troubleshoot IAM role issues that prevent proper access to your OpenShift Container Platform cluster resources.

// Module included in the following assemblies:
//
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc

[id="rosa-sts-ocm-roles-and-permissions-troubleshooting_{context}"]
= Resolving issues with ocm-roles and user-role IAM resources

[role="_abstract"]
You might receive an error when trying to create a cluster by using the {rosa-cli-first}. This error means that the `user-role` IAM role is not linked to your AWS account. The most likely cause of this error is that another user in your Red{nbsp}Hat organization created the `ocm-role` IAM role. Your `user-role` IAM role needs to be created.

[NOTE]
====
After any user sets up an `ocm-role` IAM resource linked to a Red{nbsp}Hat account, any subsequent users wishing to create a cluster in that Red{nbsp}Hat organization must have a `user-role` IAM role to provision a cluster.
====

.Procedure

* Assess the status of your `ocm-role` and `user-role` IAM roles with the following commands:
+
[source,terminal]
----
$ rosa list ocm-role
----
+
.Example output
[source,terminal]
----
I: Fetching ocm roles
ROLE NAME                           ROLE ARN                                          LINKED  ADMIN
ManagedOpenShift-OCM-Role-1158  arn:aws:iam::2066:role/ManagedOpenShift-OCM-Role-1158   No      No
----
+
[source,terminal]
----
$ rosa list user-role
----
+
.Example output
[source,terminal]
----
I: Fetching user roles
ROLE NAME                                   ROLE ARN                                        LINKED
ManagedOpenShift-User.osdocs-Role  arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role  Yes
----
+
With the results of these commands, you can create and link the missing IAM resources.

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

// TODO: Add the additional resource to ROSA HCP when the Architecture book is added.
[role="_additional-resources"]
[id="additional-resources_aws-requirements_{context}"]
== Additional resources
* Methods of account-wide role creation
* Account-wide IAM role and policy reference
