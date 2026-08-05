---
title: "Creating a ROSA cluster with STS using the default options"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-sts-creating-a-cluster-quickly
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Creating a ROSA cluster with STS using the default options

[id="rosa-sts-creating-a-cluster-quickly"]
= Creating a ROSA cluster with STS using the default options

[role="_abstract"]
Create a OpenShift Container Platform cluster quickly by using the default options and automatic AWS Identity and Access Management (IAM) resource creation. You can deploy your cluster by using {cluster-manager-first} or the {rosa-cli-first}.

[NOTE]
====
If you are looking for a quickstart guide for ROSA, see OpenShift Container Platform quickstart guide.
====

The procedures in this document use the `auto` modes in the ROSA CLI (`rosa`) and {cluster-manager} to immediately create the required IAM resources using the current AWS account. The required resources include the account-wide IAM roles and policies, cluster-specific Operator roles and policies, and OpenID Connect (OIDC) identity provider.

Alternatively, you can use `manual` mode, which outputs the `aws` commands needed to create the IAM resources instead of deploying them automatically. For steps to deploy a OpenShift Container Platform cluster by using `manual` mode or with customizations, see Creating a cluster using customizations.

[id="prerequisites_{context}"]
== Prerequisites

* Ensure that you have completed the AWS prerequisites.

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-overview-of-the-default-cluster-specifications_{context}"]
= Overview of the default cluster specifications

[role="_abstract"]
You can quickly create a OpenShift Container Platform cluster by using the default installation options.

.Default OpenShift Container Platform cluster specifications

[cols=".^1,.^3a",options="header"]
|===

|Component
|Default specifications

|Accounts and roles
|
* Default IAM role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default IAM role prefix: `ManagedOpenShift`
* Default IAM role prefix: `HCP-ROSA`
* No cluster admin role created

|Cluster settings
|
* Default cluster version: `4.14`
* Cluster name: `rosa-<6-digit-alphanumeric-string>`
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-2 (US East, Ohio)
* Availability: Multi zone for the data plane
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Default cluster version: Latest
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-1 (US East, North Virginia)
* Default AWS region for installations using the {rosa-cli} (`rosa`): Defined by your `aws` CLI configuration
* Default EC2 IMDS endpoints (both v1 and v2) are enabled
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Availability: Single zone for the data plane
* Monitoring for user-defined projects: Enabled
* No cluster admin role created
|Encryption
|* Cloud storage is encrypted at rest
* Additional etcd encryption is not enabled
* The default AWS Key Management Service (KMS) key is used as the encryption key for persistent data

|Control plane node configuration
|* Control plane node instance type: m5.2xlarge (8 vCPU, 32 GiB RAM)
* Control plane node count: 3
|Infrastructure node configuration
|* Infrastructure node instance type: r5.xlarge (4 vCPU, 32 GiB RAM)
* Infrastructure node count: 2

|Compute node machine pool
|* Compute node instance type: m5.xlarge (4 vCPU 16, GiB RAM)
* Compute node count: 2
* Compute node count: 3
* Autoscaling: Not enabled
* No additional node labels

|Networking configuration
|
* Cluster privacy: Public
* Cluster privacy: public or private
* You can choose to create a new VPC during the Terraform cluster creation process.
* You must have configured your own Virtual Private Cloud (VPC)
* No cluster-wide proxy is configured

|Classless Inter-Domain Routing (CIDR) ranges
|
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Host prefix: /23
+
[NOTE]
====
The static IP address `172.20.0.1` is reserved for the internal Kubernetes API address. The machine, pod, and service CIDRs ranges must not conflict with this IP address.
====

|Cluster roles and policies
|* Mode used to create the Operator roles and the OpenID Connect (OIDC) provider: `auto`
* A configured `ocm-role`, which is required for all OpenShift Container Platform clusters.
+
[NOTE]
====
For installations that use {cluster-manager} on the {hybrid-console-second}, the `auto` mode requires an admin-privileged {cluster-manager} role (ocm-role).
====
* Default Operator role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default Operator role prefix: `<cluster_name>-<4_digit_random_string>`

|Storage
|* Node volumes:
** Type: AWS EBS GP3
** Default size: 300GiB (adjustable at creation time)
* Workload persistent volumes:
** Default StorageClass: gp3-csi
** Provisioner: ebs.csi.aws.com
** Dynamic persistent volume provisioning

|Cluster update strategy
|* Individual updates
* 1 hour grace period for node draining

|===

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

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-creating-a-cluster-quickly-ocm_{context}"]
= Creating a cluster quickly using {cluster-manager}

[role="_abstract"]
When using {cluster-manager-first} to create a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS), you can select the default options to create the cluster quickly.

Before you can use {cluster-manager} to deploy OpenShift Container Platform clusters, you must associate your AWS account with your Red{nbsp}Hat organization and create the required account-wide STS roles and policies.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adocs

[id="rosa-sts-associating-your-aws-account_{context}"]
= Associate your AWS account with your Red{nbsp}Hat organization

[role="_abstract"]
Before using {cluster-manager-first} on the {hybrid-console-url} to create
{rosa-classic-short}
{rosa-short}
clusters that use the AWS Security Token Service (STS), create an {cluster-manager} IAM role and link it to your Red{nbsp}Hat organization. Then, create a user IAM role and link it to your Red{nbsp}Hat user account in the same Red{nbsp}Hat organization.

.Prerequisites

* You have completed the AWS prerequisites for {rosa-short}.
* You have completed the AWS prerequisites for OpenShift Container Platform with STS.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli} (`rosa`) on your installation host.
+
[NOTE]
====
To successfully install
{rosa-short}
ROSA
clusters, use the latest version of the ROSA CLI.
====
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.
* You have organization administrator privileges in your Red{nbsp}Hat organization.

.Procedure

. Create an {cluster-manager} role and link it to your Red{nbsp}Hat organization:
+
[NOTE]
====
To enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider using the {cluster-manager} {hybrid-console-second}, you must apply the administrative privileges to the role by choosing the _Admin OCM role_ command in the *Accounts and roles* step of creating a
{rosa-short}
ROSA
cluster. For more information about the basic and administrative privileges for the {cluster-manager} role, see _Understanding AWS account association_.
====
+
[NOTE]
====
If you choose the _Basic OCM role_ command in the *Accounts and roles* step of creating a
{rosa-short}
ROSA
cluster in the {cluster-manager} {hybrid-console-second}, you must deploy a
{rosa-short}
ROSA
cluster using manual mode. You will be prompted to configure the cluster-specific Operator roles and the OpenID Connect (OIDC) provider in a later step.
====
+
[source,terminal]
----
$ rosa create ocm-role
----
+
Select the default values at the prompts to quickly create and link the role.
+
. Create a user role and link it to your Red{nbsp}Hat user account:
+
[source,terminal]
----
$ rosa create user-role
----
+
Select the default values at the prompts to quickly create and link the role.
+
[NOTE]
====
The Red{nbsp}Hat user account must exist in the Red{nbsp}Hat organization that is linked to your {cluster-manager} role.
====

.Verification

* Verify that the OCM role and user role were created:
+
[source,terminal]
----
$ rosa list ocm-role
$ rosa list user-role
----

[role="_additional-resources"]
.Additional resources

* AWS prerequisites for ROSA with STS
* Understanding ROSA
* IAM roles in AWS

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-creating-account-wide-sts-roles-and-policies_{context}"]
= Create the account-wide STS roles and policies

[role="_abstract"]
Before using the {hybrid-console} to create OpenShift Container Platform clusters that use the AWS Security Token Service (STS), create the required account-wide STS roles and policies, including the Operator policies.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform with STS.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli} on your installation host. Run `rosa version` to see your currently installed version of the {rosa-cli}. If a newer version is available, the CLI provides a link to download this upgrade.
* You have logged in to your Red{nbsp}Hat account by using the {rosa-cli}.

.Procedure

. Check your AWS account for existing roles and policies:
+
[source,terminal]
----
$ rosa list account-roles
----

. If they do not exist in your AWS account, create the required account-wide AWS IAM STS roles and policies:
+
[source,terminal]
----
$ rosa create account-roles
----
[source,terminal]
----
$ rosa create account-roles --hosted-cp
----
+
Select the default values at the prompts to quickly create the roles and policies.

.Verification

* Verify that the account roles were created:
+
[source,terminal]
----
$ rosa list account-roles
----

[role="_additional-resources"]
.Additional resources

* About IAM resources for ROSA clusters that use STS
* AWS prerequisites for ROSA with STS
* IAM policies and permissions in AWS

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
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-sts-creating-a-cluster-using-defaults-ocm_{context}"]
= Create a cluster with the default options using {cluster-manager}

[role="_abstract"]
When using {cluster-manager-first} on the {hybrid-console-url} to create a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS), you can select the default options to create the cluster quickly. You can also use the admin {cluster-manager} IAM role to enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform with STS.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli}, `rosa`, on your installation host. Run `rosa version` to see your currently installed version of the {rosa-cli}. If a newer version is available, the CLI provides a link to download this upgrade.
* You have verified that the AWS Elastic Load Balancing (ELB) service role exists in your AWS account.
* You have associated your AWS account with your Red{nbsp}Hat organization. When you associated your account, you applied the administrative permissions to the {cluster-manager} role. For detailed steps, see _Associating your AWS account with your Red{nbsp}Hat organization_.
* You have created the required account-wide STS roles and policies. For detailed steps, see _Creating the account-wide STS roles and policies_.

.Procedure

. Navigate to {cluster-manager-url} and select *Create cluster*.

. On the *Create an OpenShift cluster* page, select *Create cluster* in the *OpenShift Container Platform (ROSA)* row.

. Verify that your AWS account ID is listed in the *Associated AWS accounts* drop-down menu and that the installation program, support, worker, and control plane account role Amazon Resource Names (ARNs) are listed on the *Accounts and roles* page.
+
[NOTE]
====
If your AWS account ID is not listed, check that you have successfully associated your AWS account with your Red{nbsp}Hat organization. If your account role ARNs are not listed, check that the required account-wide STS roles exist in your AWS account.
====

. Click *Next*.

. On the *Cluster details* page, provide a name for your cluster in the *Cluster name* field. Leave the default values in the remaining fields and click *Next*.
+
[NOTE]
====
Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated as a 15-character string. To customize the subdomain, select the *Create custom domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field.
====
. To deploy a cluster quickly, leave the default options in the *Cluster settings*, *Networking*, *Cluster roles and policies*, and *Cluster updates* pages and click *Next* on each page.

. On the *Review your OpenShift Container Platform cluster* page, review the summary of your selections and click *Create cluster* to start the installation.
+
. Optional: On the *Overview* tab, you can enable the delete protection feature by selecting *Enable*, which is located directly under *Delete Protection: Disabled*. This will prevent your cluster from being deleted. To disable delete protection, select *Disable*.
By default, clusters are created with the delete protection feature disabled.
+

.Verification

* You can check the progress of the installation in the *Overview* page for your cluster. You can view the installation logs on the same page. Your cluster is ready when the *Status* in the *Details* section of the page is listed as *Ready*.
+
[NOTE]
====
If the installation fails or the cluster *State* does not change to *Ready* after about 40 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for Red{nbsp}Hat OpenShift Service on AWS_.
====

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-creating-a-cluster-quickly-cli_{context}"]
= Creating a cluster quickly using the CLI

[role="_abstract"]
When using the {rosa-cli-first}, to create a cluster that uses the AWS Security Token Service (STS), you can select the default options to create the cluster quickly.

.Prerequisites

* You have completed the AWS prerequisites for ROSA with STS.
* You have available AWS service quotas.
* You have enabled the ROSA service in the AWS Console.
* You have installed and configured the latest {rosa-cli} on your installation host. Run `rosa version` to see your currently installed version of the {rosa-cli}. If a newer version is available, the CLI provides a link to download this upgrade.
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.
* You have verified that the AWS Elastic Load Balancing (ELB) service role exists in your AWS account.

.Procedure

. Create the required account-wide roles and policies, including the Operator policies:
+
[source,terminal]
----
$ rosa create account-roles --mode auto
----
+
[NOTE]
====
When using `auto` mode, you can optionally specify the `-y` argument to bypass the interactive prompts and automatically confirm operations.
====

. Create a cluster with STS using the defaults. When you use the defaults, the latest stable OpenShift version is installed:
+
--
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> \
--sts --mode auto
----

* Replace `<cluster_name>` with the name of your cluster.
* When you specify `--mode auto`, the `rosa create cluster` command creates the cluster-specific Operator IAM roles and the OIDC provider automatically. The Operators use the OIDC provider to authenticate.

--

. Check the status of your cluster:
+
[source,terminal]
----
$ rosa describe cluster --cluster <cluster_name|cluster_id>
----
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
[id="additional-resources_rosa-sts-creating-a-cluster-quickly"]
== Additional resources

* Associating your AWS account with your Red{nbsp}Hat organization
* AWS documentation on default VPCs
* AWS documentation on how to Create a VPC
* Accessing a OpenShift Container Platform cluster
* Adding notification contacts
* Creating a cluster using customizations
* About IAM resources for clusters that use STS
* About custom Operator IAM role prefixes
* AWS prerequisites for OpenShift Container Platform with STS
* Understanding the auto and manual deployment modes
* Creating OpenID Connect (OIDC) identity providers
* Troubleshooting OpenShift Container Platform cluster installations
* Getting support for Red Hat OpenShift Service on AWS
