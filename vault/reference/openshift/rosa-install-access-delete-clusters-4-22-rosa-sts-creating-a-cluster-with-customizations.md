---
title: "Creating a ROSA cluster with STS using customizations"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-sts-creating-a-cluster-with-customizations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Creating a ROSA cluster with STS using customizations

[id="rosa-sts-creating-a-cluster-with-customizations"]
= Creating a ROSA cluster with STS using customizations

[role="_abstract"]
Create a OpenShift Container Platform cluster with the AWS Security Token Service (STS) using customizations. You can deploy your cluster by using {cluster-manager-first} or the {rosa-cli-first}.

With the procedures in this document, you can also choose between the `auto` and `manual` modes when creating the required AWS Identity and Access Management (IAM) resources.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-creating-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-classic-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster, you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-understanding-deployment-modes_{context}"]
= Understanding the auto and manual deployment modes

[role="_abstract"]
When installing a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS), you can choose between the `auto` and `manual` modes to create the required AWS Identity and Access Management (IAM) resources.

`auto` mode:: With this mode, the ROSA CLI (`rosa`) immediately creates the required IAM roles and policies, and an OpenID Connect (OIDC) provider in your AWS account.

`manual` mode:: With this mode, `rosa` outputs the `aws` commands needed to create the IAM resources. The corresponding policy JSON files are also saved to the current directory. By using `manual` mode, you can review the generated `aws` commands before running them manually. `manual` mode also enables you to pass the commands to another administrator or group in your organization so that they can create the resources.

[IMPORTANT]
====
If you opt to use `manual` mode, the cluster installation waits until you create the cluster-specific Operator roles and OIDC provider manually. After you create the resources, the installation proceeds. For more information, see _Creating the Operator roles and OIDC provider using OpenShift Cluster Manager_.
====

For more information about the AWS IAM resources required to install ROSA with STS, see _About IAM resources for clusters that use STS_.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-creating-operator-roles-and-oidc-manually-ocm_{context}"]
= Creating the Operator roles and OIDC provider using {cluster-manager}

[role="_abstract"]
If you use {cluster-manager-first} to install your cluster and opt to create the required AWS IAM Operator roles and the OIDC provider using `manual` mode, you are prompted to select one of the following methods to install the resources. The options are provided to enable you to choose a resource creation method that suits the needs of your organization:

//CloudFormation:: You can use this method to create the Operator roles and the OIDC provider from the CLI using an AWS CloudFormation template and a parameter file. For more information about AWS CloudFormation, see the AWS documentation.

AWS CLI (`aws`):: With this method, you can download and extract an archive file that contains the `aws` commands and policy files required to create the IAM resources. Run the provided CLI commands from the directory that contains the policy files to create the Operator roles and the OIDC provider.

The OpenShift Container Platform (ROSA) CLI, `rosa`:: You can run the commands provided by this method to create the Operator roles and the OIDC provider for your cluster using `rosa`.

If you use `auto` mode, {cluster-manager} creates the Operator roles and the OIDC provider automatically, using the permissions provided through the {cluster-manager} IAM role. To use this feature, you must apply admin privileges to the role.

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
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-sts-understanding-aws-account-association_{context}"]
= AWS account association

[role="_abstract"]
Before you can use {cluster-manager-first} on the {hybrid-console-url} to create
{hcp-title}
OpenShift Container Platform (ROSA)
clusters that use the AWS Security Token Service (STS), you must associate your AWS account with your Red{nbsp}Hat organization. You can associate your account by creating and linking the following IAM roles.

{cluster-manager} role:: Create an {cluster-manager} IAM role and link it to your Red{nbsp}Hat organization.
+
You can apply basic or administrative permissions to the {cluster-manager} role. The basic permissions enable cluster maintenance using {cluster-manager}. The administrative permissions enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider using {cluster-manager}.
+
You can use the administrative permissions with the {cluster-manager} role to deploy a cluster quickly.

User role:: Create a user IAM role and link it to your Red{nbsp}Hat user account. The Red{nbsp}Hat user account must exist in the Red{nbsp}Hat organization that is linked to your {cluster-manager} role.
+
The user role is used by Red{nbsp}Hat to verify your AWS identity when you use the {cluster-manager} {hybrid-console-second} to install a cluster and the required STS resources.

[role="_additional-resources"]
.Additional resources

* Creating a cluster with customizations by using OpenShift Cluster Manager

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-arn-path-customization-for-iam-roles-and-policies_{context}"]
= ARN path customization for IAM roles and policies

[role="_abstract"]
When you create the AWS IAM roles and policies required for OpenShift Container Platform clusters that use the AWS Security Token Service (STS), you can specify custom Amazon Resource Name (ARN) paths. This enables you to use role and policy ARN paths that meet the security requirements of your organization.

You can specify custom ARN paths when you create your OCM role, user role, and account-wide roles and policies.

If you define a custom ARN path when you create a set of account-wide roles and policies, the same path is applied to all of the roles and policies in the set. The following example shows the ARNs for a set of account-wide roles and policies. In the example, the ARNs use the custom path `/test/path/dev/` and the custom role prefix `test-env`:

* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Worker-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Support-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Installer-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-ControlPlane-Role`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Worker-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Support-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Installer-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-ControlPlane-Role-Policy`

When you create the cluster-specific Operator roles, the ARN path for the relevant account-wide installer role is automatically detected and applied to the Operator roles.

For more information about ARN paths, see Amazon Resource Names (ARNs) in the AWS documentation.

[role="_additional-resources"]
.Additional resources

* Creating a cluster using customizations

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-support-considerations_{context}"]
= Support considerations for ROSA clusters with STS

[role="_abstract"]
The supported way of creating a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS) is by using the steps described in this product documentation.

[IMPORTANT]
====
You can use `manual` mode with the {rosa-cli-first} to generate the AWS Identity and Access Management (IAM) policy files and `aws` commands that are required to install the STS resources.

The files and `aws` commands are generated for review purposes only and must not be modified in any way. Red{nbsp}Hat cannot provide support for OpenShift Container Platform clusters that have been deployed by using modified versions of the policy files or `aws` commands.
====
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
//
[id="osd-aws-vpc-required-resources_{context}"]
= Amazon VPC Requirements for non-PrivateLink ROSA clusters

[role="_abstract"]
To create an Amazon VPC, you must have the following:

* An internet gateway,
* An NAT gateway,
* Private and public subnets that have internet connectivity provided to install required components.

You must have at least one single private and public subnet for Single-AZ clusters, and you need at least three private and public subnets for Multi-AZ clusters.
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-vpc-troubleshooting_{context}"]
= Troubleshooting VPC configuration for ROSA clusters

[role="_abstract"]
If your cluster fails to install, check common VPC configuration issues.

Consider the following troubleshooting items:

* Make sure your DHCP option set includes a domain name, and ensure that the domain name does not include any spaces or capital letters.
* If your VPC uses a custom DNS resolver (the `domain name servers` field of your DHCP option set is not `AmazonProvideDNS`), make sure it is able to properly resolve the private hosted zones configured in Route53.

For more information about troubleshooting OpenShift Container Platform cluster installations, see Troubleshooting OpenShift Container Platform installations.

== Getting support

If you need additional support, visit the Red Hat Customer Portal to review knowledge base articles, submit a support case, and review additional product documentation and resources.

[role="_additional-resources"]
.Additional resources

* AWS documentation on default VPCs
* AWS documentation on how to Create a VPC

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
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-creating-cluster-using-customizations_{context}"]
= Creating a cluster using customizations

[role="_abstract"]
Deploy a OpenShift Container Platform (ROSA) with AWS Security Token Service (STS) cluster with a configuration that suits the needs of your environment. You can deploy your cluster with customizations by using {cluster-manager-first} or the {rosa-cli-first}.
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-creating-cluster-customizations-ocm_{context}"]
= Creating a cluster with customizations by using {cluster-manager}

[role="_abstract"]
When you create a OpenShift Container Platform cluster, you can customize your installation interactively by using {cluster-manager-first}.

[IMPORTANT]
====
Only public and AWS PrivateLink clusters are supported with STS. Regular private clusters (non-PrivateLink) are not available for use with STS.
====

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform with STS.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli-first} on your installation host. Run `rosa version` to see your currently installed version of the {rosa-cli}. If a newer version is available, the CLI provides a link to download this upgrade.
* You have verified that the AWS Elastic Load Balancing (ELB) service role exists in your AWS account.
* If you are configuring a cluster-wide proxy, you have verified that the proxy is accessible from the VPC that the cluster is being installed into. The proxy must also be accessible from the private subnets of the VPC.

.Procedure

. Navigate to {cluster-manager-url} and select *Create cluster*.

. On the *Create an OpenShift cluster* page, select *Create cluster* in the *OpenShift Container Platform (ROSA)* row.

. If an AWS account is automatically detected, the account ID is listed in the *Associated AWS accounts* drop-down menu. If no AWS accounts are automatically detected, click *Select an account* -> *Associate AWS account* and follow these steps:
+
.. On the *Authenticate* page, click the copy button next to the `rosa login` command. The command includes your {cluster-manager} API login token.
+
[NOTE]
====
You can also load your API token on the OpenShift Cluster Manager API Token page on {cluster-manager}.
====
+
.. Run the copied command in the CLI to log in to your ROSA account.
+
[source,terminal]
----
$ rosa login --token=<api_login_token>
----
+
Replace `<api_login_token>` with the token that is provided in the copied command.
+
The following example shows sample output:
+
[source,terminal]
----
I: Logged in as '<username>' on 'https://api.openshift.com'
----
.. On the *Authenticate* page in {cluster-manager}, click *Next*.
.. On the *OCM role* page, click the copy button next to the *Basic OCM role* or the *Admin OCM role* commands.
+
The basic role enables {cluster-manager} to detect the AWS IAM roles and policies required by ROSA. The admin role also enables the detection of the roles and policies. In addition, the admin role enables automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider by using {cluster-manager}.
.. Run the copied command in the CLI and follow the prompts to create the {cluster-manager} IAM role. The following example creates a basic {cluster-manager} IAM role using the default options:
+
[source,terminal]
----
$ rosa create ocm-role
----
+
The following example shows sample output:
+
[source,terminal]
----
I: Creating ocm role
? Role prefix: ManagedOpenShift
? Enable admin capabilities for the OCM role (optional): No
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::<aws_account_id>:user/<aws_username>'
? Create the 'ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' role? Yes
I: Created role 'ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' with ARN 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>
? Link the 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' role with organization '<red_hat_organization_id>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' with organization account '<red_hat_organization_id>'
----
+
The prompts in this output include the following options:
+
--
Role prefix:: Specify the prefix to include in the OCM IAM role name. The default is `ManagedOpenShift`. You can create only one OCM role per AWS account for your Red{nbsp}Hat organization.
Enable admin capabilities:: Enable the admin {cluster-manager} IAM role, which is equivalent to specifying the `--admin` argument. The admin role is required if you want to use *Auto* mode to automatically provision the cluster-specific Operator roles and the OIDC provider by using {cluster-manager}.
Permissions boundary ARN:: Optional. Specify a permissions boundary Amazon Resource Name (ARN) for the role. For more information, see Permissions boundaries for IAM entities in the AWS documentation.
Role Path:: Specify a custom ARN path for your OCM role. The path must contain alphanumeric characters only and start and end with `/`, for example `/test/path/dev/`. For more information, see _ARN path customization for IAM roles and policies_.
Role creation mode:: Select the role creation mode. You can use `auto` mode to automatically create the {cluster-manager} IAM role and link it to your Red{nbsp}Hat organization account. In `manual` mode, the ROSA CLI generates the `aws` commands needed to create and link the role. In `manual` mode, the corresponding policy JSON files are also saved to the current directory. `manual` mode enables you to review the details before running the `aws` commands manually.
Link role prompt:: Link the {cluster-manager} IAM role to your Red{nbsp}Hat organization account.
--
.. If you opted not to link the {cluster-manager} IAM role to your Red{nbsp}Hat organization account in the preceding command, copy the `rosa link` command from the {cluster-manager} *OCM role* page and run it:
+
[source,terminal]
----
$ rosa link ocm-role <arn>
----
+
Replace `<arn>` with the ARN of the {cluster-manager} IAM role that is included in the output of the preceding command.
.. Select *Next* on the {cluster-manager} *OCM role* page.
.. On the *User role* page, click the copy button for the *User role* command and run the command in the CLI. Red{nbsp}Hat uses the user role to verify your AWS identity when you install a cluster and the required resources with {cluster-manager}.
+
Follow the prompts to create the user role:
+
[source,terminal]
----
$ rosa create user-role
----
+
The following example shows sample output:
+
[source,terminal]
----
I: Creating User role
? Role prefix: ManagedOpenShift
? Permissions boundary ARN (optional):
? Role Path (optional): [? for help]
? Role creation mode: auto
I: Creating ocm user role using 'arn:aws:iam::<aws_account_id>:user/<aws_username>'
? Create the 'ManagedOpenShift-User-<red_hat_username>-Role' role? Yes
I: Created role 'ManagedOpenShift-User-<red_hat_username>-Role' with ARN 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<red_hat_username>-Role'
I: Linking User role
? User Role ARN: arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<red_hat_username>-Role
? Link the 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<red_hat_username>-Role' role with account '<red_hat_user_account_id>'? Yes
I: Successfully linked role ARN 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<red_hat_username>-Role' with account '<red_hat_user_account_id>'
----
+
The prompts in this output include the following options:
+
--
Role prefix:: Specify the prefix to include in the user role name. The default is `ManagedOpenShift`.
Permissions boundary ARN:: Optional. Specify a permissions boundary Amazon Resource Name (ARN) for the role. For more information, see Permissions boundaries for IAM entities in the AWS documentation.
Role Path:: Specify a custom ARN path for your user role. The path must contain alphanumeric characters only and start and end with `/`, for example `/test/path/dev/`. For more information, see _ARN path customization for IAM roles and policies_.
Role creation mode:: Select the role creation mode. You can use `auto` mode to automatically create the user role and link it to your {cluster-manager} user account. In `manual` mode, the ROSA CLI generates the `aws` commands needed to create and link the role. In `manual` mode, the corresponding policy JSON files are also saved to the current directory. `manual` mode enables you to review the details before running the `aws` commands manually.
Link role prompt:: Link the user role to your {cluster-manager} user account.
--
.. If you opted not to link the user role to your {cluster-manager} user account in the preceding command, copy the `rosa link` command from the {cluster-manager} *User role* page and run it:
+
[source,terminal]
----
$ rosa link user-role <arn>
----
+
Replace `<arn>` with the ARN of the user role that is included in the output of the preceding command.
.. On the {cluster-manager} *User role* page, click *Ok*.
.. Verify that the AWS account ID is listed in the *Associated AWS accounts* drop-down menu on the *Accounts and roles* page.
.. If the required account roles do not exist, a notification is provided stating that *Some account roles ARNs were not detected*. You can create the AWS account-wide roles and policies, including the Operator policies, by clicking the copy buffer next to the `rosa create account-roles` command and running the command in the CLI:
+
[source,terminal]
----
$ rosa create account-roles
----
+
--
The following example shows sample output:

[source,terminal,subs="attributes+"]
----
I: Logged in as '<red_hat_username>' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: .0
I: Creating account roles
? Role prefix: ManagedOpenShift
? Permissions boundary ARN (optional):
? Path (optional): [? for help]
? Role creation mode: auto
I: Creating roles using 'arn:aws:iam::<aws_account_number>:user/<aws_username>'
? Create the 'ManagedOpenShift-Installer-Role' role? Yes
I: Created role 'ManagedOpenShift-Installer-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Installer-Role'
? Create the 'ManagedOpenShift-ControlPlane-Role' role? Yes
I: Created role 'ManagedOpenShift-ControlPlane-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-ControlPlane-Role'
? Create the 'ManagedOpenShift-Worker-Role' role? Yes
I: Created role 'ManagedOpenShift-Worker-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Worker-Role'
? Create the 'ManagedOpenShift-Support-Role' role? Yes
I: Created role 'ManagedOpenShift-Support-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Support-Role'
I: To create a cluster with these roles, run the following command:
rosa create cluster --sts
----

The prompts in this output include the following options:

Role prefix:: Specify the prefix to include in the {cluster-manager} IAM role name. The default is `ManagedOpenShift`.
+
[IMPORTANT]
====
You must specify an account-wide role prefix that is unique across your AWS account, even if you use a custom ARN path for your account roles.
====

Permissions boundary ARN:: Optional. Specify a permissions boundary Amazon Resource Name (ARN) for the role. For more information, see Permissions boundaries for IAM entities in the AWS documentation.
Path:: Specify a custom ARN path for your account-wide roles. The path must contain alphanumeric characters only and start and end with `/`, for example `/test/path/dev/`. For more information, see _ARN path customization for IAM roles and policies_.
Role creation mode:: Select the role creation mode. You can use `auto` mode to automatically create the account wide roles and policies. In `manual` mode, the ROSA CLI generates the `aws` commands needed to create the roles and policies. In `manual` mode, the corresponding policy JSON files are also saved to the current directory. `manual` mode enables you to review the details before running the `aws` commands manually.
Create role prompts:: Creates the account-wide installer, control plane, worker and support roles and corresponding IAM policies. For more information, see _Account-wide IAM role and policy reference_.

[NOTE]
====
In this step, the ROSA CLI also automatically creates the account-wide Operator IAM policies that are used by the cluster-specific Operator policies to permit the ROSA cluster Operators to carry out core OpenShift functionality. For more information, see _Account-wide IAM role and policy reference_.
====
--
.. On the *Accounts and roles* page, click *Refresh ARNs* and verify that the installer, support, worker, and control plane account role ARNs are listed.
+
If you have more than one set of account roles in your AWS account for your cluster version, a drop-down list of *Installer role* ARNs is provided. Select the ARN for the installer role that you want to use with your cluster. The cluster uses the account-wide roles and policies that relate to the selected installer role.

. Click *Next*.
+
[NOTE]
====
If the *Accounts and roles* page was refreshed, you might need to select the checkbox again to acknowledge that you have read and completed all of the prerequisites.
====

. On the *Cluster details* page, provide a name for your cluster and specify the cluster details:
.. Add a *Cluster name*.
.. Optional: Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated to a 15 character string.
+
To customize the subdomain, select the *Create custom domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field. The domain prefix cannot be longer than 15 characters, must be unique within your organization, and cannot be changed after cluster creation.
.. Select a cluster version from the *Version* drop-down menu.
.. Select a channel group from the *Channel group* drop-down menu.
+
--
--
+
.. Select a cloud provider region from the *Region* drop-down menu.
.. Select a *Single zone* or *Multi-zone* configuration.
.. Leave *Enable user workload monitoring* selected to monitor your own projects in isolation from Red{nbsp}Hat Site Reliability Engineer (SRE) platform metrics. This option is enabled by default.
.. Optional: Expand *Advanced Encryption* to make changes to encryption settings.
... Accept the default setting *Use default KMS Keys* to use your default AWS KMS key, or select *Use Custom KMS keys* to use a custom KMS key.
.... With *Use Custom KMS keys* selected, enter the AWS Key Management Service (KMS) custom key Amazon Resource Name (ARN) ARN in the *Key ARN* field.
The key is used for encrypting all control plane, infrastructure, worker node root volumes, and persistent volumes in your cluster.
.... Optional: To create a customer managed KMS key, follow the procedure for Creating symmetric encryption KMS keys.
+
[IMPORTANT]
====
The EBS Operator role is required in addition to the account roles to successfully create your cluster.

This role must be attached with the `ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credentials` policy, an IAM policy required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

For more information about the policies and permissions that the cluster Operators require, see _Methods of account-wide role creation_.

The following example shows an EBS Operator role:

`"arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"`

After you create your Operator roles, you must edit the _Key Policy_ in the *Key Management Service (KMS)* page of the AWS Console to add the roles.
====
... Optional: Select *Enable FIPS cryptography* if you require your cluster to be FIPS validated.
+
[NOTE]
====
If *Enable FIPS cryptography* is selected, *Enable additional etcd encryption* is enabled by default and cannot be disabled. You can select *Enable additional etcd encryption* without selecting *Enable FIPS cryptography*.
====
... Optional: Select *Enable additional etcd encryption* if you require etcd key value encryption. With this option, the etcd key values are encrypted, but the keys are not. This option is in addition to the control plane storage encryption that encrypts the etcd volumes in OpenShift Container Platform clusters by default.
+
[NOTE]
====
By enabling etcd encryption for the key values in etcd, you will incur a performance overhead of approximately 20%. The overhead is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Consider enabling etcd encryption only if you specifically require it for your use case.
====
.. Click *Next*.

. On the *Default machine pool* page, select a *Compute node instance type*.
+
[NOTE]
====
After your cluster is created, you can change the number of compute nodes in your cluster, but you cannot change the compute node instance type in the default machine pool. The number and types of nodes available to you depend on whether you use single or multiple availability zones. They also depend on what is enabled and available in your AWS account and the selected region.
====

. Optional: Configure autoscaling for the default machine pool:
.. Select *Enable autoscaling* to automatically scale the number of machines in your default machine pool to meet the deployment needs.
.. Set the minimum and maximum node count limits for autoscaling. The cluster autoscaler does not reduce or increase the default machine pool node count beyond the limits that you specify.
+
--
** If you deployed your cluster using a single availability zone, set the *Minimum node count* and *Maximum node count*. This defines the minimum and maximum compute node limits in the availability zone.
** If you deployed your cluster using multiple availability zones, set the *Minimum nodes per zone* and *Maximum nodes per zone*. This defines the minimum and maximum compute node limits per zone.
--
+
[NOTE]
====
Alternatively, you can set your autoscaling preferences for the default machine pool after the machine pool is created.
====

. If you did not enable autoscaling, select a compute node count for your default machine pool:
** If you deployed your cluster using a single availability zone, select a *Compute node count* from the drop-down menu. This defines the number of compute nodes to provision to the machine pool for the zone.
** If you deployed your cluster using multiple availability zones, select a *Compute node count (per zone)* from the drop-down menu. This defines the number of compute nodes to provision to the machine pool per zone.

. Optional: Select an EC2 Instance Metadata Service (IMDS) configuration - `optional` (default) or `required` - to enforce use of IMDSv2. For more information regarding IMDS, see Instance metadata and user data in the AWS documentation.
+
[IMPORTANT]
====
The Instance Metadata Service settings cannot be changed after your cluster is created.
====

. Optional: Expand *Edit node labels* to add labels to your nodes. Click *Add label* to add more node labels and select *Next*.

. In the *Cluster privacy* section of the *Network configuration* page, select *Public* or *Private* to use either public or private API endpoints and application routes for your cluster.
+
[IMPORTANT]
====
The API endpoint cannot be changed between public and private after your cluster is created.
====
+
Public API endpoint:: Select *Public* if you do not want to restrict access to your cluster. You can access the Kubernetes API endpoint and application routes from the internet.

Private API endpoint:: Select *Private* if you want to restrict network access to your cluster. The Kubernetes API endpoint and application routes are accessible from direct private connections only.
+
[IMPORTANT]
====
If you are using private API endpoints, you cannot access your cluster until you update the network settings in your cloud provider account.
====

. Optional: If you opted to use public API endpoints, by default a new VPC is created for your cluster. If you want to install your cluster in an existing VPC instead, select *Install into an existing VPC*.
+
[WARNING]
====
You cannot install a ROSA cluster into an existing VPC that was created by the OpenShift installer. These VPCs are created during the cluster deployment process and must only be associated with a single cluster to ensure that cluster provisioning and deletion operations work correctly.

To verify whether a VPC was created by the OpenShift installer, check for the `owned` value on the `kubernetes.io/cluster/<infra-id>` tag. For example, when viewing the tags for the VPC named `mycluster-12abc-34def`, the `kubernetes.io/cluster/mycluster-12abc-34def` tag has a value of `owned`. Therefore, the VPC was created by the installer and must not be modified by the administrator.
====
+
[NOTE]
====
If you opted to use private API endpoints, you must use an existing VPC and PrivateLink and the *Install into an existing VPC* and *Use a PrivateLink* options are automatically selected. With these options, the Red{nbsp}Hat Site Reliability Engineering (SRE) team can connect to the cluster to assist with support by using only AWS PrivateLink endpoints.
====

. Optional: If you are installing your cluster into an existing VPC, select *Configure a cluster-wide proxy* to enable an HTTP or HTTPS proxy to deny direct access to the internet from your cluster.

. Click *Next*.

. If you opted to install the cluster in an existing AWS VPC, provide your *Virtual Private Cloud (VPC) subnet settings*.
+
[NOTE]
====
You must ensure that your VPC is configured with a public and a private subnet for each availability zone that you want the cluster installed into. If you opted to use PrivateLink, only private subnets are required.
====
.. Optional: Expand *Additional security groups* and select additional custom security groups to apply to nodes in the machine pools created by default. You must have already created the security groups and associated them with the VPC you selected for this cluster. You cannot add or edit security groups to the default machine pools after you create the cluster.
+
By default, the security groups you specify will be added for all node types. Uncheck the *Apply the same security groups to all node types (control plane, infrastructure and worker)* checkbox to select different security groups for each node type.
+
For more information, see the requirements for _Security groups_ under _Additional resources_.

. If you opted to configure a cluster-wide proxy, provide your proxy configuration details on the *Cluster-wide proxy* page:
+
.. Enter a value in at least one of the following fields:
** Specify a valid *HTTP proxy URL*.
** Specify a valid *HTTPS proxy URL*.
** In the *Additional trust bundle* field, provide a PEM encoded X.509 certificate bundle. The bundle is added to the trusted certificate store for the cluster nodes. An additional trust bundle file is required if you use a TLS-inspecting proxy unless the identity certificate for the proxy is signed by an authority from the {op-system-first} trust bundle. This requirement applies regardless of whether the proxy is transparent or requires explicit configuration using the `http-proxy` and `https-proxy` arguments.
.. Click *Next*.
+
For more information about configuring a proxy with OpenShift Container Platform, see _Configuring a cluster-wide proxy_.

. In the *CIDR ranges* dialog, configure custom classless inter-domain routing (CIDR) ranges or use the defaults that are provided and click *Next*.
+
[NOTE]
====
If you are installing into a VPC, the *Machine CIDR* range must match the VPC subnets.
====
+
[IMPORTANT]
====
CIDR configurations cannot be changed later. Confirm your selections with your network administrator before proceeding.
====

. Under the *Cluster roles and policies* page, select your preferred cluster-specific Operator IAM role and OIDC provider creation mode.
+
//With *Manual* mode, you can use either AWS CloudFormation, `rosa` CLI commands, or `aws` CLI commands to generate the required Operator roles and OIDC provider for your cluster. *Manual* mode enables you to review the details before using your preferred option to create the IAM resources manually and complete your cluster installation.
With *Manual* mode, you can use either the `rosa` CLI commands or the `aws` CLI commands to generate the required Operator roles and OIDC provider for your cluster. *Manual* mode enables you to review the details before using your preferred option to create the IAM resources manually and complete your cluster installation.
+
Alternatively, you can use *Auto* mode to automatically create the Operator roles and OIDC provider. To enable *Auto* mode, the {cluster-manager} IAM role must have administrator capabilities.
+
[NOTE]
====
If you specified custom ARN paths when you created the associated account-wide roles, the custom path is automatically detected and applied to the Operator roles. The custom ARN path is applied when the Operator roles are created by using either *Manual* or *Auto* mode.
====

. Optional: Specify a *Custom operator roles prefix* for your cluster-specific Operator IAM roles.
+
[NOTE]
====
By default, the cluster-specific Operator role names are prefixed with the cluster name and random 4-digit hash. You can optionally specify a custom prefix to replace `<cluster_name>-<hash>` in the role names. The prefix is applied when you create the cluster-specific Operator IAM roles. For information about the prefix, see _About custom Operator IAM role prefixes_.
====

. Select *Next*.

. On the *Cluster update strategy* page, configure your update preferences:
.. Choose a cluster update method:
** Select *Individual updates* if you want to schedule each update individually. This is the default option.
** Select *Recurring updates* to update your cluster on your preferred day and start time, when updates are available.
+
[IMPORTANT]
====
Even when you opt for recurring updates, you must update the account-wide and cluster-specific IAM resources before you upgrade your cluster between minor releases.
====
+
[NOTE]
====
You can review the end-of-life dates in the update life cycle documentation for OpenShift Container Platform. For more information, see _OpenShift Container Platform update life cycle_.
====
+
.. If you opted for recurring updates, select a preferred day of the week and upgrade start time in UTC from the drop-down menus.
.. Optional: You can set a grace period for *Node draining* during cluster upgrades. A *1 hour* grace period is set by default.
.. Click *Next*.
+
[NOTE]
====
If there are critical security concerns that significantly impact the security or stability of a cluster, Red{nbsp}Hat Site Reliability Engineering (SRE) might schedule automatic updates to the latest z-stream version that is not impacted. The updates are applied within 48 hours after customer notifications are provided. For a description of the critical impact security rating, see Understanding Red{nbsp}Hat security ratings.
====

. Review the summary of your selections and click *Create cluster* to start the cluster installation.

. If you opted to use *Manual* mode, create the cluster-specific Operator roles and OIDC provider manually to continue the installation:
+
--
//.. In the *Action required to continue installation* dialog, select either the *AWS CloudFormation*, *AWS CLI*, or *ROSA CLI* tab and manually create the resources:
.. In the *Action required to continue installation* dialog, select either the *AWS CLI* or the *ROSA CLI* tab and manually create the resources:
//** If you opted to use the *AWS CloudFormation* method, click the copy button next to the `aws cloudformation` commands and run them in the CLI.
** If you opted to use the *AWS CLI* method, click *Download .zip*, save the file, and then extract the AWS CLI command and policy files. Then, run the provided `aws` commands in the CLI.
+
[NOTE]
====
You must run the `aws` commands in the directory that contains the policy files.
====
** If you opted to use the *ROSA CLI* method, click the copy button next to the `rosa create` commands and run them in the CLI.
+
[NOTE]
====
If you specified custom ARN paths when you created the associated account-wide roles, the custom path is automatically detected and applied to the Operator roles when you create them by using these manual methods.
====
.. In the *Action required to continue installation* dialog, click *x* to return to the *Overview* page for your cluster.
.. Verify that the cluster *Status* in the *Details* section of the *Overview* page for your cluster has changed from *Waiting* to *Installing*. There might be a short delay of approximately two minutes before the status changes.
--
+
[NOTE]
====
If you opted to use *Auto* mode, {cluster-manager} creates the Operator roles and the OIDC provider automatically.
====
+
[IMPORTANT]
====
The EBS Operator role is required in addition to the account roles to successfully create your cluster.

This role must be attached with the `ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credentials` policy, an IAM policy required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

For more information about the policies and permissions that the cluster Operators require, see _Methods of account-wide role creation_.

The following example shows an EBS Operator role:

`"arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"`

After you create your Operator roles, you must edit the _Key Policy_ in the *Key Management Service (KMS)* page of the AWS Console to add the roles.
====

.Verification

* You can monitor the progress of the installation in the *Overview* page for your cluster. You can view the installation logs on the same page. Your cluster is ready when the *Status* in the *Details* section of the page is listed as *Ready*.
+
[NOTE]
====
If the installation fails or the cluster *State* does not change to *Ready* after about 40 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for Red{nbsp}Hat OpenShift Service on AWS_.
====

[role="_additional-resources"]
.Additional resources
* `rosa create cluster` command reference
* Methods of account-wide role creation

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-sts-creating-cluster-customizations-cli_{context}"]
= Creating a cluster with customizations using the CLI

[role="_abstract"]
When you create a OpenShift Container Platform (ROSA) cluster that uses the AWS Security Token Service (STS), you can customize your installation interactively.

When you run the `rosa create cluster --interactive` command at cluster creation time, you are presented with a series of interactive prompts that enable you to customize your deployment. For more information, see _Interactive cluster creation mode reference_.

After a cluster installation using the interactive mode completes, a single command is provided in the output that enables you to deploy further clusters using the same custom configuration.

[IMPORTANT]
====
Only public and AWS PrivateLink clusters are supported with STS. Regular private clusters (non-PrivateLink) are not available for use with STS.
====

.Prerequisites

* You have completed the AWS prerequisites for ROSA with STS.
* You have available AWS service quotas.
* You have enabled the ROSA service in the AWS Console.
* You have installed and configured the latest ROSA CLI, `rosa`, on your installation host. Run `rosa version` to see your currently installed version of the ROSA CLI. If a newer version is available, the CLI provides a link to download this upgrade.
* If you want to use a customer managed AWS Key Management Service (KMS) key for encryption, you must create a symmetric KMS key. You must provide the Amazon Resource Name (ARN) when creating your cluster. To create a customer managed KMS key, follow the procedure for Creating symmetric encryption KMS keys.
+
[IMPORTANT]
====
The EBS Operator role is required in addition to the account roles to successfully create your cluster.

This role must be attached with the `ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credentials` policy, an IAM policy required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

For more information about the policies and permissions that the cluster Operators require, see _Methods of account-wide role creation_.

For example:

`"arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"`

After you create your Operator roles, you must edit the _Key Policy_ in the *Key Management Service (KMS)* page of the AWS Console to add the roles.
====

.Procedure

. Create the required account-wide roles and policies, including the Operator policies:
.. Generate the IAM policy JSON files in the current working directory and output the `aws` CLI commands for review:
+
--
[source,terminal]
----
$ rosa create account-roles --interactive \
  --mode manual
----

* The `--interactive` option enables you to specify configuration options at the interactive prompts. For more information, see _Interactive cluster creation mode reference_.
* The `--mode manual` option generates the `aws` CLI commands and JSON files needed to create the account-wide roles and policies. After review, you must run the commands manually to create the resources.

The following example shows sample output:

[source,terminal,subs="attributes+"]
----
I: Logged in as '<red_hat_username>' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: .0
I: Creating account roles
? Role prefix: ManagedOpenShift
? Permissions boundary ARN (optional):
? Path (optional): [? for help]
? Role creation mode: auto
I: Creating roles using 'arn:aws:iam::<aws_account_number>:user/<aws_username>'
? Create the 'ManagedOpenShift-Installer-Role' role? Yes
I: Created role 'ManagedOpenShift-Installer-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Installer-Role'
? Create the 'ManagedOpenShift-ControlPlane-Role' role? Yes
I: Created role 'ManagedOpenShift-ControlPlane-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-ControlPlane-Role'
? Create the 'ManagedOpenShift-Worker-Role' role? Yes
I: Created role 'ManagedOpenShift-Worker-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Worker-Role'
? Create the 'ManagedOpenShift-Support-Role' role? Yes
I: Created role 'ManagedOpenShift-Support-Role' with ARN 'arn:aws:iam::<aws_account_number>:role/ManagedOpenShift-Support-Role'
I: To create a cluster with these roles, run the following command:
rosa create cluster --sts
----

where:

`Role prefix`:: Specify the prefix to include in the {cluster-manager} IAM role name. The default is `ManagedOpenShift`.
+
[IMPORTANT]
====
You must specify an account-wide role prefix that is unique across your AWS account, even if you use a custom ARN path for your account roles.
====
`Permissions boundary ARN (optional)`:: Optional: Specifies a permissions boundary Amazon Resource Name (ARN) for the role. For more information, see Permissions boundaries for IAM entities in the AWS documentation.
`Path (optional)`:: Specify a custom ARN path for your account-wide roles. The path must contain alphanumeric characters only and start and end with `/`, for example `/test/path/dev/`. For more information, see _ARN path customization for IAM roles and policies_.
`Role creation mode`:: Select the role creation mode. You can use `auto` mode to automatically create the account wide roles and policies. In `manual` mode, the `rosa` CLI generates the `aws` commands needed to create the roles and policies. In `manual` mode, the corresponding policy JSON files are also saved to the current directory. `manual` mode enables you to review the details before running the `aws` commands manually.

After specifying the configuration options, the account-wide installer, control plane, worker and support roles and corresponding IAM policies are created. For more information, see _Account-wide IAM role and policy reference_.

[NOTE]
====
In this step, the ROSA CLI also automatically creates the account-wide Operator IAM policies that are used by the cluster-specific Operator policies to permit the ROSA cluster Operators to run core OpenShift functionality. For more information, see _Account-wide IAM role and policy reference_.
====
--

.. After review, run the `aws` commands manually to create the roles and policies. Alternatively, you can run the preceding command using `--mode auto` to run the `aws` commands immediately.

. Optional: If you are using your own AWS KMS key to encrypt the control plane, infrastructure, worker node root volumes, and persistent volumes (PVs), add the ARN for the account-wide installer role to your KMS key policy.
+
[IMPORTANT]
====
Only persistent volumes (PVs) created from the default storage class are encrypted with this specific key.

PVs created by using any other storage class are still encrypted, but the PVs are not encrypted with this key unless the storage class is specifically configured to use this key.
====

.. Save the key policy for your KMS key to a file on your local machine. The following example saves the output to `kms-key-policy.json` in the current working directory:
+
[source,terminal]
----
$ aws kms get-key-policy --key-id <key_id_or_arn> --policy-name default --output text > kms-key-policy.json
----
.. Add the ARN for the account-wide installer role that you created in the preceding step to the `Statement.Principal.AWS` section in the file. In the following example, the ARN for the default `ManagedOpenShift-Installer-Role` role is added:
+
--
[source,json]
----
{
    "Version": "2012-10-17",
    "Id": "key-rosa-policy-1",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<aws_account_id>:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow ROSA use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role",
                    "arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role",
                    "arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role",
                    "arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"
                ]
            },
            "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        }
    ]
}
----

* In the `Sid: "Allow ROSA use of the key"` and `Sid: "Allow attachment of persistent resources"` statements, add the ARN for the account-wide role that will be used when you create the OpenShift Container Platform cluster (for example, `arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role`).

* In the `Sid: "Allow ROSA use of the key"` and `Sid: "Allow attachment of persistent resources"` statements, add the ARN for the operator role that will be used when you create the OpenShift Container Platform cluster (for example, `arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent`).
--

.. Apply the changes to your KMS key policy:
+
[source,terminal]
----
$ aws kms put-key-policy --key-id <key_id_or_arn> \
    --policy file://kms-key-policy.json \
    --policy-name default
----
+
You can reference the ARN of your KMS key when you create the cluster in the next step.

. Create a cluster with STS using custom installation options. You can use the `--interactive` mode to interactively specify custom settings:
+
[WARNING]
====
You cannot install a ROSA cluster into an existing VPC that was created by the OpenShift installer. These VPCs are created during the cluster deployment process and must only be associated with a single cluster to ensure that cluster provisioning and deletion operations work correctly.

To verify whether a VPC was created by the OpenShift installer, check for the `owned` value on the `kubernetes.io/cluster/<infra-id>` tag. For example, when viewing the tags for the VPC named `mycluster-12abc-34def`, the `kubernetes.io/cluster/mycluster-12abc-34def` tag has a value of `owned`. Therefore, the VPC was created by the installer and must not be modified by the administrator.
====
+
[source,terminal]
----
$ rosa create cluster --interactive --sts
----
+
.Example output
[source,terminal]
----
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: <cluster_name>
? Domain prefix: <domain_prefix>
? Deploy cluster with Hosted Control Plane (optional): No
? Create cluster admin user: Yes
? Create custom password for cluster admin: No
I: cluster admin user is cluster-admin
I: cluster admin password is password
? OpenShift version: <openshift_version>
? Configure the use of IMDSv2 for ec2 instances optional/required (optional):
I: Using arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role for the Installer role
I: Using arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role for the ControlPlane role
I: Using arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role for the Worker role
I: Using arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role for the Support role
? External ID (optional):
? Operator roles prefix: <cluster_name>-<random_string>
? Deploy cluster using pre registered OIDC Configuration ID:
? Tags (optional)
? Multiple availability zones (optional): No
? AWS region: us-east-1
? PrivateLink cluster (optional): No
? Machine CIDR: 10.0.0.0/16
? Service CIDR: 172.30.0.0/16
? Pod CIDR: 10.128.0.0/14
? Install into an existing VPC (optional): Yes
? Subnet IDs (optional):
? Select availability zones (optional): No
? Enable Customer Managed key (optional): No
? Compute nodes instance type (optional):
? Enable autoscaling (optional): No
? Compute nodes: 2
? Worker machine pool labels (optional):
? Host prefix: 23
? Additional Security Group IDs (optional):
? > [*]  sg-0e375ff0ec4a6cfa2 ('sg-1')
? > [ ]  sg-0e525ef0ec4b2ada7 ('sg-2')
? Enable FIPS support: No
? Encrypt etcd data: No
? Disable Workload monitoring (optional): No
I: Creating cluster '<cluster_name>'
I: To create this cluster again in the future, you can run:
   rosa create cluster --cluster-name <cluster_name> --role-arn arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role --support-role-arn arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role --master-iam-role arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role --worker-iam-role arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role --operator-roles-prefix <cluster_name>-<random_string> --region us-east-1 --version 4.22.0 --additional-compute-security-group-ids sg-0e375ff0ec4a6cfa2 --additional-infra-security-group-ids sg-0e375ff0ec4a6cfa2 --additional-control-plane-security-group-ids sg-0e375ff0ec4a6cfa2 --replicas 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23
I: To view a list of clusters and their status, run 'rosa list clusters'
I: Cluster '<cluster_name>' has been created.
I: Once the cluster is installed you will need to add an Identity Provider before you can login into the cluster. See 'rosa create idp --help' for more information.
...
----
+
For more information about the customization options, see _Interactive cluster creation mode options_ in _Interactive cluster creation mode reference_.
+
The output includes a custom command that you can run to create another cluster with the same configuration.
+
As an alternative to using the `--interactive` mode, you can specify the customization options directly when you run the `rosa create cluster` command. Run the `rosa create cluster --help` command to view a list of available CLI options.

+
[IMPORTANT]
====
You must complete the following steps to create the Operator IAM roles and the OpenID Connect (OIDC) provider to move the state of the cluster to `ready`.
====

. Create the cluster-specific Operator IAM roles:
.. Generate the Operator IAM policy JSON files in the current working directory and output the `aws` CLI commands for review:
+
[source,terminal]
----
$ rosa create operator-roles --mode manual --cluster <cluster_name|cluster_id>
----
+
The `manual` mode generates the `aws` CLI commands and JSON files needed to create the Operator roles. After review, you must run the commands manually to create the resources.

.. After review, run the `aws` commands manually to create the Operator IAM roles and attach the managed Operator policies to them. Alternatively, you can run the preceding command again using `--mode auto` to run the `aws` commands immediately.
+
[NOTE]
====
A custom prefix is applied to the Operator role names if you specified the prefix in the preceding step.

If you specified custom ARN paths when you created the associated account-wide roles, the custom path is automatically detected and applied to the Operator roles.
====
+
[IMPORTANT]
====
The EBS Operator role is required in addition to the account roles to successfully create your cluster.

This role must be attached with the `ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credentials` policy, an IAM policy required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

For more information about the policies and permissions that the cluster Operators require, see _Methods of account-wide role creation_.

For example:

`"arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent"`

After you create your Operator roles, you must edit the _Key Policy_ in the *Key Management Service (KMS)* page of the AWS Console to add the roles.
====

. Create the OpenID Connect (OIDC) provider that the cluster Operators use to authenticate:
+
[source,terminal]
----
$ rosa create oidc-provider --mode auto --cluster <cluster_name|cluster_id>
----
+
The `auto` mode immediately runs the `aws` CLI command that creates the OIDC provider.

. Check the status of your cluster:
+
[source,terminal]
----
$ rosa describe cluster --cluster <cluster_name|cluster_id>
----
+
.Example output
[source,terminal]
----
Name:                       <cluster_name>
ID:                         <cluster_id>
External ID:                <external_id>
OpenShift Version:          <version>
Channel Group:              stable
DNS:                        <cluster_name>.xxxx.p1.openshiftapps.com
AWS Account:                <aws_account_id>
API URL:                    https://api.<cluster_name>.xxxx.p1.openshiftapps.com:6443
Console URL:                https://console-openshift-console.apps.<cluster_name>.xxxx.p1.openshiftapps.com
Region:                     <aws_region>
Multi-AZ:                   false
Nodes:
 - Master:                  3
 - Infra:                   2
 - Compute:                 2
Network:
 - Service CIDR:            172.30.0.0/16
 - Machine CIDR:            10.0.0.0/16
 - Pod CIDR:                10.128.0.0/14
 - Host Prefix:             /23
STS Role ARN:               arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role
Support Role ARN:           arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role
Instance IAM Roles:
 - Master:                  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role
 - Worker:                  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent
 - arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-machine-api-aws-cloud-credentials
 - arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-cloud-credential-operator-cloud-crede
 - arn:aws:iam::<aws_account_id>:role/<cluster_name>-xxxx-openshift-image-registry-installer-cloud-creden
Ec2 Metadata Http Tokens:   optional
State:                      ready
Private:                    No
Created:                    Oct  1 2021 08:12:25 UTC
Details Page:               https://console.redhat.com/openshift/details/s/<subscription_id>
OIDC Endpoint URL:          https://oidc.op1.openshiftapps.com/<cluster_id>|<oidc_config_id>
----
+
The `OIDC Endpoint URL` depends on the BYO OIDC configuration. If you are pre-creating the OIDC configuration, the URL ends with the `<oidc_config_id>` value; otherwise, the URL ends with the `<cluster-ID>` value.
+
The following `State` field changes are listed in the output as the cluster installation progresses:
+
* `waiting (Waiting for OIDC configuration)`
* `pending (Preparing account)`
* `installing (DNS setup in progress)`
* `installing`
* `ready`
+
[NOTE]
====
If the installation fails or the `State` field does not change to `ready` after about 40 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for Red{nbsp}Hat OpenShift Service on AWS_.
====

. Track the progress of the cluster creation by watching the OpenShift installer logs:
+
[source,terminal]
----
$ rosa logs install --cluster <cluster_name|cluster_id> --watch
----
+
Specify the `--watch` flag to watch for new log messages as the installation progresses. This argument is optional.

[role="_additional-resources"]
.Additional resources
* Interactive cluster creation mode reference
* Security groups
* Methods of account-wide role creation
* About custom Operator IAM role prefixes

[role="_additional-resources"]
[id="additional-resources_rosa-sts-creating-a-cluster-with-customizations"]
== Additional resources

* Accessing a OpenShift Container Platform cluster
* Adding notification contacts
* Configuring a shared VPC for OpenShift Container Platform clusters
* About IAM resources for clusters that use STS
* About custom Operator IAM role prefixes
* Interactive cluster creation mode reference
* AWS prerequisites for OpenShift Container Platform with STS
* Creating OpenID Connect (OIDC) identity providers (AWS documentation)
* etcd encryption service definition
* Configuring a cluster-wide proxy
* Troubleshooting cluster deployments
* Getting support for OpenShift Container Platform
