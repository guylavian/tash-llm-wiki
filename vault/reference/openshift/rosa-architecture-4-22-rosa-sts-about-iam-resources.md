---
title: "About IAM resources for STS clusters"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-sts-about-iam-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-sts-about-iam-resources
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# About IAM resources for STS clusters

[id="rosa-sts-about-iam-resources"]
= About IAM resources for STS clusters

[id="rosa-hcp-about-iam-resources"]
= About IAM resources

[role="_abstract"]
To deploy a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS),
{hcp-title-first} uses the AWS Security Token Service (STS) to provide temporary, limited-permission credentials for your cluster. This means that before you deploy your cluster,
you must create the following AWS Identity Access Management (IAM) resources:

* Specific account-wide IAM roles and policies that provide the STS permissions required for ROSA support, installation,
control plane,
and compute functionality. This includes account-wide Operator policies.
* Cluster-specific Operator IAM roles that permit the ROSA cluster Operators to carry out core OpenShift functionality.
* An OpenID Connect (OIDC) provider that the cluster Operators use to authenticate.
* If you deploy and manage your cluster using {cluster-manager}, you must create the following additional resources:
** An {cluster-manager} IAM role to complete the installation on your cluster.
** A user role without any permissions to verify your AWS account identity.

This document provides reference information about the IAM resources that you must deploy
when you create a OpenShift Container Platform cluster that uses STS.
when you create a {hcp-title} cluster.
It also includes the `aws` CLI commands that are generated when you use `manual` mode with the `rosa create` command.

[id="rosa-sts-ocm-roles-and-permissions_{context}"]
== {cluster-manager} roles and permissions

If you create OpenShift Container Platform clusters by using {cluster-manager-url}, you must have the following AWS IAM roles linked to your AWS account to create and manage the clusters.

These AWS IAM roles are as follows:

* The OpenShift Container Platform user role (`user-role`) is an AWS role used by Red{nbsp}Hat to verify the customer's AWS identity. This role has no additional permissions, and the role has a trust relationship with the Red{nbsp}Hat installer account.
* An `ocm-role` resource grants the required permissions for installation of OpenShift Container Platform clusters in {cluster-manager}. You can apply basic or administrative permissions to the `ocm-role` resource. If you create an administrative `ocm-role` resource, {cluster-manager} can create the needed AWS Operator roles and OpenID Connect (OIDC) provider. This IAM role also creates a trust relationship with the Red{nbsp}Hat installer account as well.
+
[NOTE]
====
The `ocm-role` IAM resource refers to the combination of the IAM role and the necessary policies created with it.
====

You must create this user role as well as an administrative `ocm-role` resource, if you want to use the auto mode in {cluster-manager} to create your Operator role policies and OIDC provider.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
//
[id="rosa-sts-understanding-ocm-role_{context}"]
= Understanding the {cluster-manager} role

Creating OpenShift Container Platform clusters in {cluster-manager-url} requires an `ocm-role` IAM role. The standard `ocm-role` IAM role permissions let you perform cluster maintenance within {cluster-manager}. To automatically create the Operator roles and OpenID Connect (OIDC) provider, you must add the `--admin` option to the `rosa create` command. This command creates an `ocm-role` resource with additional permissions needed for administrative tasks. If you do not need to use {cluster-manager}, the `--no-console` profile creates an `ocm-role` IAM role with the minimum required permissions to create and manage clusters by using the CLI.

[NOTE]
====
This elevated IAM role allows {cluster-manager} to automatically create the cluster-specific Operator roles and OIDC provider during cluster creation. For more information about this automatic role and policy creation, see the "Methods of account-wide role creation" link in Additional resources.
====

[id="rosa-sts-understanding-user-role_{context}"]
== Understanding the user role

In addition to an `ocm-role` IAM role, you must create a user role so that OpenShift Container Platform can verify your AWS identity. This role has no permissions, and it is only used to create a trust relationship between the installer account and your `ocm-role` resources.

The following tables show the associated basic and administrative permissions for the `ocm-role` resource.

.Associated permissions for the basic `ocm-role` resource
[cols="1,2",options="header"]
|===

|Resource|Description

| `iam:GetOpenIDConnectProvider`
| This permission allows the basic role to retrieve information about the specified OpenID Connect (OIDC) provider.
| `iam:GetRole`
| This permission allows the basic role to retrieve any information for a specified role. Some of the data returned include the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role.
| `iam:ListRoles`
| This permission allows the basic role to list the roles within a path prefix.
| `iam:ListRoleTags`
| This permission allows the basic role to list the tags on a specified role.
| `ec2:DescribeRegions`
| This permission allows the basic role to return information about all of the enabled regions on your account.
| `ec2:DescribeRouteTables`
| This permission allows the basic role to return information about all of your route tables.
| `ec2:DescribeSubnets`
| This permission allows the basic role to return information about all of your subnets.
| `ec2:DescribeVpcs`
| This permission allows the basic role to return information about all of your virtual private clouds (VPCs).
| `sts:AssumeRole`
| This permission allows the basic role to retrieve temporary security credentials to access AWS resources that are beyond its normal permissions.
| `sts:AssumeRoleWithWebIdentity`
| This permission allows the basic role to retrieve temporary security credentials for users authenticated their account with a web identity provider.

|===

.Additional permissions for the admin `ocm-role` resource
[cols="1,2",options="header"]
|===

|Resource|Description

| `iam:AttachRolePolicy`
| This permission allows the admin role to attach a specified policy to the desired IAM role.
| `iam:CreateOpenIDConnectProvider`
| This permission creates a resource that describes an identity provider, which supports OpenID Connect (OIDC). When you create an OIDC provider with this permission, this provider establishes a trust relationship between the provider and AWS.
| `iam:CreateRole`
| This permission allows the admin role to create a role for your AWS account.
| `iam:ListPolicies`
| This permission allows the admin role to list any policies associated with your AWS account.
| `iam:ListPolicyTags`
| This permission allows the admin role to list any tags on a designated policy.
| `iam:PutRolePermissionsBoundary`
| This permission allows the admin role to change the permissions boundary for a user based on a specified policy.
| `iam:TagRole`
| This permission allows the admin role to add tags to an IAM role.

|===

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
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-account-wide-roles-and-policies_{context}"]
= Account-wide IAM role and policy reference

This section provides details about the account-wide IAM roles and policies that are required for ROSA deployments that use STS, including the Operator policies. It also includes the JSON files that define the policies.

The account-wide roles and policies are specific to an OpenShift Container Platform minor release version, for example OpenShift Container Platform , and are compatible with earlier versions. You can minimize the required STS resources by reusing the account-wide roles and policies for multiple clusters of the same minor version, regardless of their patch version.

[id="rosa-sts-account-wide-roles-and-policies-creation-methods_{context}"]
== Methods of account-wide role creation

You can create account-wide roles by using the OpenShift Container Platform (ROSA) CLI, `rosa`, or the {cluster-manager-url} guided installation. You can create the roles manually or by using an automatic process that uses predefined names for these roles and policies.

[id="rosa-sts-account-wide-roles-and-policies-creation-methods-manual_{context}"]
=== Manual ocm-role resource creation

You can use the manual creation method if you have the necessary CLI access to create these roles on your system. You can run this option in your desired CLI tool or from {cluster-manager}. After you start the manual creation process, the CLI presents a series of commands for you to run that create the roles and link them to the needed policies.

[id="rosa-sts-account-wide-roles-and-policies-creation-methods-auto_{context}"]
=== Automatic ocm-role resource creation

After you created an `ocm-role` resource with administrative permissions, you can use the automatic creation method from {cluster-manager}. Selecting this method creates the roles and policies that use the default names.

If you use the OpenShift Container Platform guided installation on {cluster-manager}, you must have created an `ocm-role` resource with administrative permissions in the first step of the guided cluster installation.

[NOTE]
====
The account number present in the `sts_installer_trust_policy.json` and `sts_support_trust_policy.json` samples represents the Red{nbsp}Hat account that is allowed to assume the required roles.
====

.ROSA installer role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-Installer-Role`
|An IAM role used by the ROSA installer.

|`ManagedOpenShift-Installer-Role-Policy`
|An IAM policy that provides the ROSA installer with the permissions required to complete cluster installation tasks.

|===

.`sts_installer_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_installer_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA control plane role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-ControlPlane-Role`
|An IAM role used by the ROSA control plane.

|`ManagedOpenShift-ControlPlane-Role-Policy`
|An IAM policy that provides the ROSA control plane with the permissions required to manage its components.

|===

.`sts_instance_controlplane_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_instance_controlplane_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA compute node role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-Worker-Role`
|An IAM role used by the ROSA compute instances.

|`ManagedOpenShift-Worker-Role-Policy`
|An IAM policy that provides the ROSA compute instances with the permissions required to manage their components.

|===

.`sts_instance_worker_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_instance_worker_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA support role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-Support-Role`
|An IAM role used by the Red{nbsp}Hat Site Reliability Engineering (SRE) support team.

|`ManagedOpenShift-Support-Role-Policy`
|An IAM policy that provides the Red{nbsp}Hat SRE support team with the permissions required to support ROSA clusters.

|===

.`sts_support_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_support_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA OCM role and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-OCM-Role`
|You use this IAM role to create and maintain ROSA clusters in  {cluster-manager}.

|===

.`sts_ocm_role_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA user role and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-User-<OCM_user>-Role`
|An IAM role used by Red{nbsp}Hat to verify the customer's AWS identity.

|===

.`sts_user_role_trust_policy.json`
[%collapsible]
====
[source,json]
----

----
====

[id="rosa-sts-account-wide-roles-and-policies-example-cli-output-for-policies-attached-to-a-role_{context}"]
==== Example CLI output for policies attached to a role

When a policy is attached to a role, the ROSA CLI displays a confirmation output. The output depends on the type of policy.

* If the policy is a trust policy, the ROSA CLI outputs the role name and the content of the policy.
** For the target role with policy attached, ROSA CLI outputs the role name and the console URL of the target role.
+
.Target role with policy attached example output
[source,terminal]
----
I: Attached trust policy to role 'testrole-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/testrole-Worker-Role)': ******************
----
+
** If the attached policy is a trust policy, the ROSA CLI outputs the content of this policy.
+
.Trust policy example output
[source,terminal]
----
I: Attached trust policy to role 'test-Support-Role': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::000000000000:role/RH-Technical-Support-00000000"]}}]}
----
* If the policy is a permission policy, the ROSA CLI outputs the name and public link of this policy or the ARN depending on whether or not the policy is an AWS managed policy or customer-managed policy.
** If the attached policy is an AWS managed policy, the ROSA CLI outputs the name and public link of this policy and the role it is attached to.
+
.AWS managed policy example output
[source,terminal]
----
I: Attached policy 'ROSASRESupportPolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSASRESupportPolicy)' to role 'test-HCP-ROSA-Support-Role(https://console.aws.amazon.com/iam/home?#/roles/test-HCP-ROSA-Support-Role)'
----
** If the attached policy is an AWS managed policy, the ROSA CLI outputs the name and public link of this policy and the role it is attached to.
+
.Customer-managed policy example output
[source,terminal]
----
I: Attached policy 'arn:aws:iam::000000000000:policy/testrole-Worker-Role-Policy' to role 'testrole-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/testrole-Worker-Role)'
----

.ROSA Ingress Operator IAM policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-openshift-ingress-operator-cloud-credentials`
|An IAM policy that provides the ROSA Ingress Operator with the permissions required to manage external access to a cluster.

|===

.`openshift_ingress_operator_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA back-end storage IAM policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credentials`
|An IAM policy required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

|===

.`openshift_cluster_csi_drivers_ebs_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Machine Config Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-openshift-machine-api-aws-cloud-credentials`
|An IAM policy that provides the ROSA Machine Config Operator with the permissions required to perform core cluster functionality.

|===

.`openshift_machine_api_aws_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Cloud Credential Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-openshift-cloud-credential-operator-cloud-credentials`
|An IAM policy that provides the ROSA Cloud Credential Operator with the permissions required to manage cloud provider credentials.

|===

.`openshift_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Image Registry Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ManagedOpenShift-openshift-image-registry-installer-cloud-credentials`
|An IAM policy that provides the ROSA Image Registry Operator with the permissions required to manage the {product-registry} storage in AWS S3 for a cluster.

|===

.`openshift_image_registry_installer_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Manage Subscription policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`ROSAManageSubscription`
|This policy streamlines permission setup by packaging necessary access rights, giving entities appropriate control over the ROSA subscription while preventing excessive permissions.

|===

.ROSA installer role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`HCP-ROSA-Installer-Role`
|An IAM role used by the ROSA installer.

|ROSAInstallerPolicy
|An IAM policy that provides the ROSA installer with the permissions required to complete cluster installation tasks.

|`HCP-ROSA-Installer-Role` trust policy
|Grants the Red{nbsp} Hat installer temporary permission to act within your AWS account for the sole purpose of setting up a OpenShift Container Platform cluster.

|===
.`sts_hcp_installer_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_hcp_installer_trust_policy.json`
[%collapsible]
====
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::710019948333:role/RH-Managed-OpenShift-Installer"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
----
====

.ROSA worker node role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`HCP-ROSA-Worker-Role`
|An IAM role used by the compute instances.

|ROSAWorkerInstancePolicy
|An IAM policy that provides the ROSA compute instances with the permissions required to manage their components.

|`HCP-ROSA-Worker-Role` trust policy
|Allows essential software on your worker nodes to securely connect and talk to the cluster's control plane, which is managed remotely by Red{nbsp}Hat.
|===

.`sts_hcp_worker_instance_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_hcp_worker_instance_trust_policy.json`
[%collapsible]
====
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
----
====

.ROSA support role, policy, and policy files
[cols="1,2",options="header"]
|===

|Resource|Description

|`HCP-ROSA-Support-Role`
|An IAM role used by the Red Hat Site Reliability Engineering (SRE) support team.

|ROSASRESupportPolicy
|An IAM policy that provides the Red Hat SRE support team with the permissions required to support ROSA clusters.

|`HCP-ROSA-Support-Role` trust policy
|Provides a secure mechanism for authorized Red Hat Site Reliability Engineers (SREs) to perform diagnostic and support functions on the cluster.

|===
.`sts_hcp_support_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.`sts_hcp_support_trust_policy.json`
[%collapsible]
====
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::710019948333:role/RH-Technical-Support-15234082"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
----
====

.ROSA Kube Controller Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-kube-controller-manager-credentials`
|An IAM policy that grants permissions to the kube controller to manage Amazon EC2, Elastic Load Balancing, and AWS KMS resources.

|===
.`openshift-hcp_kube-controller-manager-credentials-policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Control Plane Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-control-plane-operator-credentials-policy`
|An IAM policy that grants required permissions to the Control Plane Operator to manage Amazon EC2 and Route 53 resources.

|===
.`openshift_hcp_control_plane_operator_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Node Pool Management Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-capa-controller-manager-credentials-policy`
|An IAM policy that grants required permissions to the NodePool controller to describe, run, and terminate Amazon EC2 instances managed as worker nodes. This policy also grants permissions to allow for disk encryption of the worker node root volume using AWS KMS keys, and to tag the elastic network interface that is attached to the worker node.

|===
.`openshift_hcp_capa_controller_manager_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Image Registry Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-image-registry-operator-permission-policy`
|An IAM policy that grants required permissions to the Image Registry Operator to provision and manage resources for the ROSA in-cluster image registry and dependent services, including S3. This is required so that the operator can install and maintain the internal registry of a ROSA cluster.

|===
.`openshift_hcp_image_registry_operator_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Amazon EBSCI Driver Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-cluster-csi-driver-ebs-operator-cloud-credentials-policy`
|An IAM policy that grants necessary permissions to the Amazon EBS CSI Driver Operator to install and maintain the Amazon EBS CSI driver on a ROSA cluster.

|===
.`openshift_hcp_cluster_csi_driver_ebs_operator_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====
.ROSA Cloud Network Config Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-cloud-network-config-cloud-credentials-permission-policy`
|An IAM policy that grants necessary permissions to the Amazon EBS CSI Driver Operator to install and maintain the Amazon EBS CSI driver on a ROSA cluster.

|===
.`openshift_hcp_cloud_network_config_cloud_credentials_permission_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA Ingress Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-cluster-ingress-operator-cloud-credentials-policy`
|An IAM policy that provides the ROSA Ingress Operator with the permissions required to manage external access to a cluster.

|===
.`openshift_hcp_cluster_ingress_operator_cloud_credentials_policy.json`
[%collapsible]
====
[source,json]
----

----
====

.ROSA KMS Provider Operator policy and policy file
[cols="1,2",options="header"]
|===

|Resource|Description

|`openshift-hcp-kms-provider-credential-policy.`
|An IAM policy grants required permissions to the built-in AWS Encryption Provider to manage AWS KMS keys that support etcd data encryption. This policy allows Amazon EC2 to use KMS keys that the AWS Encryption Provider provides to encrypt and decrypt etcd data.

|===
.`openshift_hcp_kms_provider_credential_policy.json`
[%collapsible]
====
[source,json]
----

----
====

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-account-wide-role-and-policy-aws-cli_{context}"]
= Account-wide IAM role and policy AWS CLI reference

This section lists the `aws` CLI commands that the `rosa` command generates in the terminal. You can run the command in either manual or automatic mode.

[id="rosa-sts-account-wide-role-and-policy-aws-cli-manual-mode_{context}"]
== Using manual mode for account role creation

The manual role creation mode generates the `aws` commands for you to review and run. The following command starts that process, where `<openshift_version>` refers to your version of OpenShift Container Platform (ROSA), such as ``.

[source,terminal]
----
$ rosa create account-roles --mode manual
----

[NOTE]
====
The provided command examples include the `ManagedOpenShift` prefix. The `ManagedOpenShift` prefix is the default value, if you do not specify a custom prefix by using the `--prefix` option.
====

.Command output
[source,terminal]
----
aws iam create-role \
	--role-name ManagedOpenShift-Installer-Role \
	--assume-role-policy-document file://sts_installer_trust_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=installer

aws iam put-role-policy \
	--role-name ManagedOpenShift-Installer-Role \
	--policy-name ManagedOpenShift-Installer-Role-Policy \
	--policy-document file://sts_installer_permission_policy.json

aws iam create-role \
	--role-name ManagedOpenShift-ControlPlane-Role \
	--assume-role-policy-document file://sts_instance_controlplane_trust_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=instance_controlplane

aws iam put-role-policy \
	--role-name ManagedOpenShift-ControlPlane-Role \
	--policy-name ManagedOpenShift-ControlPlane-Role-Policy \
	--policy-document file://sts_instance_controlplane_permission_policy.json

aws iam create-role \
	--role-name ManagedOpenShift-Worker-Role \
	--assume-role-policy-document file://sts_instance_worker_trust_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=instance_worker

aws iam put-role-policy \
	--role-name ManagedOpenShift-Worker-Role \
	--policy-name ManagedOpenShift-Worker-Role-Policy \
	--policy-document file://sts_instance_worker_permission_policy.json

aws iam create-role \
	--role-name ManagedOpenShift-Support-Role \
	--assume-role-policy-document file://sts_support_trust_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=support

aws iam put-role-policy \
	--role-name ManagedOpenShift-Support-Role \
	--policy-name ManagedOpenShift-Support-Role-Policy \
	--policy-document file://sts_support_permission_policy.json

aws iam create-policy \
	--policy-name ManagedOpenShift-openshift-ingress-operator-cloud-credentials \
	--policy-document file://openshift_ingress_operator_cloud_credentials_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-ingress-operator Key=operator_name,Value=cloud-credentials

aws iam create-policy \
	--policy-name ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credent \
	--policy-document file://openshift_cluster_csi_drivers_ebs_cloud_credentials_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-cluster-csi-drivers Key=operator_name,Value=ebs-cloud-credentials

aws iam create-policy \
	--policy-name ManagedOpenShift-openshift-machine-api-aws-cloud-credentials \
	--policy-document file://openshift_machine_api_aws_cloud_credentials_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-machine-api Key=operator_name,Value=aws-cloud-credentials

aws iam create-policy \
	--policy-name ManagedOpenShift-openshift-cloud-credential-operator-cloud-crede \
	--policy-document file://openshift_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-cloud-credential-operator Key=operator_name,Value=cloud-credential-operator-iam-ro-creds

aws iam create-policy \
	--policy-name ManagedOpenShift-openshift-image-registry-installer-cloud-creden \
	--policy-document file://openshift_image_registry_installer_cloud_credentials_policy.json \
	--tags Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-image-registry Key=operator_name,Value=installer-cloud-credentials
----

[id="rosa-sts-account-wide-role-and-policy-aws-cli-auto-mode_{context}"]
== Using auto mode for role creation

When you add the `--mode auto` argument, the OpenShift Container Platform (ROSA) CLI, `rosa`, creates your roles and policies. The following command starts that process:

[source,terminal]
----
$ rosa create account-roles --mode auto
----

[NOTE]
====
The provided command examples include the `ManagedOpenShift` prefix. The `ManagedOpenShift` prefix is the default value, if you do not specify a custom prefix by using the `--prefix` option.
====

.Command output
[source,terminal]
----
I: Creating roles using 'arn:aws:iam::<ARN>:user/<UserID>'
? Create the 'ManagedOpenShift-Installer-Role' role? Yes
I: Created role 'ManagedOpenShift-Installer-Role' with ARN 'arn:aws:iam::<ARN>:role/ManagedOpenShift-Installer-Role'
? Create the 'ManagedOpenShift-ControlPlane-Role' role? Yes
I: Created role 'ManagedOpenShift-ControlPlane-Role' with ARN 'arn:aws:iam::<ARN>:role/ManagedOpenShift-ControlPlane-Role'
? Create the 'ManagedOpenShift-Worker-Role' role? Yes
I: Created role 'ManagedOpenShift-Worker-Role' with ARN 'arn:aws:iam::<ARN>:role/ManagedOpenShift-Worker-Role'
? Create the 'ManagedOpenShift-Support-Role' role? Yes
I: Created role 'ManagedOpenShift-Support-Role' with ARN 'arn:aws:iam::<ARN>:role/ManagedOpenShift-Support-Role'
? Create the operator policies? Yes
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-machine-api-aws-cloud-credentials'
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-cloud-credential-operator-cloud-crede'
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-image-registry-installer-cloud-creden'
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-ingress-operator-cloud-credentials'
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credent'
I: Created policy with ARN 'arn:aws:iam::<ARN>:policy/ManagedOpenShift-openshift-cloud-network-config-controller-cloud'
I: To create a cluster with these roles, run the following command:
rosa create cluster --sts
----

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
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-operator-role-aws-cli_{context}"]
= Operator IAM role AWS CLI reference

This section lists the `aws` CLI commands that are shown in the terminal when you run the following `rosa` command using `manual` mode:

[source,terminal]
----
$ rosa create operator-roles --mode manual --cluster <cluster_name>
----

[NOTE]
====
When using `manual` mode, the `aws` commands are printed to the terminal for your review. After reviewing the `aws` commands, you must run them manually. Alternatively, you can specify `--mode auto` with the `rosa create` command to run the `aws` commands immediately.
====

.Command output
[source,terminal]
----
aws iam create-role \
	--role-name <cluster_name>-<hash>-openshift-cluster-csi-drivers-ebs-cloud-credent \
	--assume-role-policy-document file://operator_cluster_csi_drivers_ebs_cloud_credentials_policy.json \
	--tags Key=rosa_cluster_id,Value=<id> Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value= Key=operator_namespace,Value=openshift-cluster-csi-drivers Key=operator_name,Value=ebs-cloud-credentials

aws iam attach-role-policy \
	--role-name <cluster_name>-<hash>-openshift-cluster-csi-drivers-ebs-cloud-credent \
	--policy-arn arn:aws:iam::<aws_account_id>:policy/ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credent

aws iam create-role \
	--role-name <cluster_name>-<hash>-openshift-machine-api-aws-cloud-credentials \
	--assume-role-policy-document file://operator_machine_api_aws_cloud_credentials_policy.json \
	--tags Key=rosa_cluster_id,Value=<id> Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value= Key=operator_namespace,Value=openshift-machine-api Key=operator_name,Value=aws-cloud-credentials

aws iam attach-role-policy \
	--role-name <cluster_name>-<hash>-openshift-machine-api-aws-cloud-credentials \
	--policy-arn arn:aws:iam::<aws_account_id>:policy/ManagedOpenShift-openshift-machine-api-aws-cloud-credentials

aws iam create-role \
	--role-name <cluster_name>-<hash>-openshift-cloud-credential-operator-cloud-crede \
	--assume-role-policy-document file://operator_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json \
	--tags Key=rosa_cluster_id,Value=<id> Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value= Key=operator_namespace,Value=openshift-cloud-credential-operator Key=operator_name,Value=cloud-credential-operator-iam-ro-creds

aws iam attach-role-policy \
	--role-name <cluster_name>-<hash>-openshift-cloud-credential-operator-cloud-crede \
	--policy-arn arn:aws:iam::<aws_account_id>:policy/ManagedOpenShift-openshift-cloud-credential-operator-cloud-crede

aws iam create-role \
	--role-name <cluster_name>-<hash>-openshift-image-registry-installer-cloud-creden \
	--assume-role-policy-document file://operator_image_registry_installer_cloud_credentials_policy.json \
	--tags Key=rosa_cluster_id,Value=<id> Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value= Key=operator_namespace,Value=openshift-image-registry Key=operator_name,Value=installer-cloud-credentials

aws iam attach-role-policy \
	--role-name <cluster_name>-<hash>-openshift-image-registry-installer-cloud-creden \
	--policy-arn arn:aws:iam::<aws_account_id>:policy/ManagedOpenShift-openshift-image-registry-installer-cloud-creden

aws iam create-role \
	--role-name <cluster_name>-<hash>-openshift-ingress-operator-cloud-credentials \
	--assume-role-policy-document file://operator_ingress_operator_cloud_credentials_policy.json \
	--tags Key=rosa_cluster_id,Value=<id> Key=rosa_openshift_version,Value=<openshift_version> Key=rosa_role_prefix,Value= Key=operator_namespace,Value=openshift-ingress-operator Key=operator_name,Value=cloud-credentials

aws iam attach-role-policy \
	--role-name <cluster_name>-<hash>-openshift-ingress-operator-cloud-credentials \
	--policy-arn arn:aws:iam::<aws_account_id>:policy/ManagedOpenShift-openshift-ingress-operator-cloud-credentials
----

[NOTE]
====
The command examples provided in the table include Operator roles that use the `ManagedOpenShift` prefix. If you defined a custom prefix when you created the account-wide roles and policies, including the Operator policies, you must reference it by using the `--prefix <prefix_name>` option when you create the Operator roles.
====

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-about-operator-role-prefixes_{context}"]
= About custom Operator IAM role prefixes

Each OpenShift Container Platform (ROSA) cluster
requires cluster-specific Operator IAM roles.
that uses the AWS Security Token Service (STS) requires cluster-specific Operator IAM roles.

By default, the Operator role names are prefixed with the cluster name and a random 4-digit hash. For example, the Ingress Cloud Credentials Operator IAM role for a cluster named `mycluster` has the default name `mycluster-<hash>-openshift-ingress-operator-cloud-credentials`, where `<hash>` is a random 4-digit string.

This default naming convention enables you to easily identify the Operator IAM roles for a cluster in your AWS account.

When you create the Operator roles for a cluster, you can optionally specify a custom prefix to use instead of `<cluster_name>-<hash>`. By using a custom prefix, you can prepend logical identifiers to your Operator role names to meet the requirements of your environment. For example, you might prefix the cluster name and the environment type, such as `mycluster-dev`. In that example, the Ingress Cloud Credentials Operator role name with the custom prefix is `mycluster-dev-openshift-ingress-operator-cloud-credenti`.

[NOTE]
====
The role names are truncated to 64 characters.
====

[id="rosa-sts-oidc-provider-requirements-for-operators_{context}"]
== Open ID Connect (OIDC) requirements for Operator authentication

For OpenShift Container Platform installations that use STS, you must create a cluster-specific OIDC provider that is used by the cluster Operators to authenticate or create your own OIDC configuration for your own OIDC provider.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-oidc-overview.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-oidc-provider-for-operators-aws-cli_{context}"]
= Creating an OIDC provider using the CLI

You can create an OIDC provider that is hosted in your AWS account with the OpenShift Container Platform (ROSA) CLI, `rosa`.

.Prerequisites

* You have installed the latest version of the ROSA CLI.

.Procedure

* To create an OIDC provider, by using an unregistered or a registered OIDC configuration.
** Unregistered OIDC configurations require you to create the OIDC provider through the cluster. Run the following to create the OIDC provider:
+
[source,terminal]
----
$ rosa create oidc-provider --mode manual --cluster <cluster_name>
----
+
[NOTE]
====
When using `manual` mode, the `aws` command is printed to the terminal for your review. After reviewing the `aws` command, you must run it manually. Alternatively, you can specify `--mode auto` with the `rosa create` command to run the `aws` command immediately.
====
+
.Command output
[source,terminal]
----
aws iam create-open-id-connect-provider \
	--url https://oidc.op1.openshiftapps.com/<oidc_config_id> \// <1>
	--client-id-list openshift sts.<aws_region>.amazonaws.com \
	--thumbprint-list <thumbprint> <2>
----
<1> The URL used to reach the OpenID Connect (OIDC) identity provider after the cluster is created.
<2> The thumbprint is generated automatically when you run the `rosa create oidc-provider` command. For more information about using thumbprints with AWS Identity and Access Management (IAM) OIDC identity providers, see the AWS documentation.

** Registered OIDC configurations use an OIDC configuration ID. Run the following command with your OIDC configuration ID:
+
[source,terminal]
----
$ rosa create oidc-provider --oidc-config-id <oidc_config_id> --mode auto -y
----
+
.Command output
[source,terminal]
----
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/241rh9ql5gpu99d7leokhvkp8icnalpf'
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-byo-odic-overview_{context}"]
= Creating an OpenID Connect Configuration

When using a cluster hosted by Red{nbsp}Hat, you can create a managed or unmanaged OpenID Connect (OIDC) configuration by using the OpenShift Container Platform (ROSA) CLI, `rosa`. A managed OIDC configuration is stored within Red{nbsp}Hat's AWS account, while a generated unmanaged OIDC configuration is stored within your AWS account. The OIDC configuration is registered to be used with {cluster-manager}. When creating an unmanaged OIDC configuration, the CLI provides the private key for you.

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
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-byo-oidc-options_{context}"]
= Parameter options for creating your own OpenID Connect configuration

The following options may be added to the `rosa create oidc-config` command. All of these parameters are optional. Running the `rosa create oidc-config` command without parameters creates an unmanaged OIDC configuration.

[NOTE]
====
You are required to register the unmanaged OIDC configuration by posting a request to `/oidc_configs` through OpenShift Cluster Manager. You receive an ID in the response. Use this ID to create a cluster.
====

[id="rosa-sts-byo-oidc-raw-files_{context}"]
== raw-files

Allows you to provide raw files for the private RSA key. This key is named `rosa-private-key-oidc-<random_label_of_length_4>.key`. You also receive a discovery document, named `discovery-document-oidc-<random_label_of_length_4>.json`, and a JSON Web Key Set, named `jwks-oidc-<random_label_of_length_4>.json`.

You use these files to set up the endpoint. This endpoint responds to `/.well-known/openid-configuration` with the discovery document and on `keys.json` with the JSON Web Key Set. The private key is stored in Amazon Web Services (AWS) Secrets Manager Service (SMS) as plaintext.

.Example
[source,terminal]
----
$ rosa create oidc-config --raw-files
----

[id="rosa-sts-byo-oidc-mode_{context}"]
== mode

Allows you to specify the mode to create your OIDC configuration. With the `manual` option, you receive AWS commands that set up the OIDC configuration in an S3 bucket. This option stores the private key in the Secrets Manager. With the `manual` option, the OIDC Endpoint URL is the URL for the S3 bucket. You must retrieve the Secrets Manager ARN to register the OIDC configuration with OpenShift Cluster Manager.

You receive the same OIDC configuration and AWS resources as the `manual` mode when using the `auto` option. A significant difference between the two options is that when using the `auto` option, ROSA calls AWS, so you do not need to take any further actions. The OIDC Endpoint URL is the URL for the S3 bucket. The CLI retrieves the Secrets Manager ARN, registers the OIDC configuration with OpenShift Cluster Manager, and reports the second `rosa` command that the user can run to continue with the creation of the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --mode=<auto|manual>
----

[id="rosa-sts-byo-oidc-managed_{context}"]
== managed

Creates an OIDC configuration that is hosted under Red{nbsp}Hat's AWS account. This command creates a private key that responds directly with an OIDC Config ID for you to use when creating the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --managed
----

.Example output
[source,terminal]
----
W: For a managed OIDC Config only auto mode is supported. However, you may choose the provider creation mode
? OIDC Provider creation mode: auto
I: Setting up managed OIDC configuration
I: Please run the following command to create a cluster with this oidc config
rosa create cluster --sts --oidc-config-id 233jnu62i9aphpucsj9kueqlkr1vcgra
I: Creating OIDC provider using 'arn:aws:iam::242819244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::242819244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/233jnu62i9aphpucsj9kueqlkr1vcgra'
----

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="rosa-minimum-scp_{context}"]
= Minimum set of effective permissions for service control policies (SCP)

[role="_abstract"]
Service control policies (SCP) are a type of organization policy that manages permissions within your organization. SCPs ensure that accounts within your organization stay within your defined access control guidelines. These policies are maintained in AWS organizations and control the services that are available within the attached AWS accounts. SCP management is the responsibility of the customer.

[NOTE]
====
When using AWS Security Token Service (STS), you must ensure that the service control policy does not block the following resources:

* `ec2:{}`
* `iam:{}`
* `tag:*`
====

[NOTE]
====
The minimum SCP requirement does not apply when using AWS Security Token Service (STS). For more information about STS, see AWS prerequisites for ROSA with STS.
====

Verify that your service control policy (SCP) does not restrict any of these required permissions.

[cols="2a,2a,2a,2a",options="header"]

|===
|
| Service
| Actions
| Effect

.18+| Required
|Amazon EC2 | All |Allow
|Amazon EC2 Auto Scaling | All |Allow
|Amazon S3| All |Allow
|Identity And Access Management | All |Allow
|Elastic Load Balancing | All |Allow
|Elastic Load Balancing V2| All |Allow
|Amazon CloudWatch | All |Allow
|Amazon CloudWatch Events | All |Allow
|Amazon CloudWatch Logs | All |Allow
|AWS EC2 Instance Connect | SendSerialConsoleSSHPublicKey |Allow
|AWS Support | All |Allow
|AWS Key Management Service | All |Allow
|AWS Security Token Service | All |Allow
|AWS Tiro | CreateQuery

GetQueryAnswer

GetQueryExplanation
| Allow
|AWS Marketplace | Subscribe

Unsubscribe

View Subscriptions
| Allow
|AWS Resource Tagging | All |Allow
|AWS Route53 DNS | All |Allow
|AWS Service Quotas | ListServices

GetRequestedServiceQuotaChange

GetServiceQuota

RequestServiceQuotaIncrease

ListServiceQuotas
| Allow

.3+|Optional | AWS Billing
| ViewAccount

Viewbilling

ViewUsage
| Allow

|AWS Cost and Usage Report
|All
|Allow

|AWS Cost Explorer Services
|All
|Allow

|===

[role="_additional-resources"]
.Additional resources

* Service control policies
* SCP effects on permissions

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-aws-customer-managed-policies_{context}"]
= Customer-managed policies
OpenShift Container Platform (ROSA) users are able to attach customer-managed policies to the IAM roles required to run and maintain ROSA clusters. This capability is not uncommon with AWS IAM roles.
The ability to attach these policies to ROSA-specific IAM roles extends a ROSA cluster’s permission capabilities; for example, as a way to allow cluster components to access additional AWS resources that are otherwise not part of the ROSA-specific IAM policies.

To ensure that any critical customer applications that rely on customer-managed policies are not modified in any way during cluster or role upgrades, ROSA utilizes the `ListAttachedRolesPolicies` permission to retrieve the list of permission policies from roles and the `ListRolePolicies` permission to retrieve the list of policies from ROSA-specific roles. This information ensures that customer-managed policies are not impacted during cluster events, and allows Red Hat SREs to monitor both ROSA and customer-managed policies attached to ROSA-specific IAM roles, enhancing their ability to troubleshoot any cluster issues more effectively.

[WARNING]
====
Attaching permission boundary policies to IAM roles that restrict ROSA-specific policies is not supported, as these policies could interrupt the functionality of the basic permissions necessary to successfully run and maintain your ROSA cluster. There are prepared permissions boundary policies for the ROSA (classic architecture) installer role. See the Additional resources section for more information.
====

[role="_additional-resources"]
.Additional resources

// * Permission boundaries for the installer role
* Permissions boundaries for IAM entities

[role="_additional-resources"]
[id="additional-resources_about-iam-resources"]
== Additional resources

* Creating a OpenShift Container Platform cluster with STS using the default options
* Creating a OpenShift Container Platform cluster with STS using customizations
* Creating a OpenShift Container Platform cluster quickly
* OpenShift Container Platform update life cycle
* Creating account-wide roles and policies
* Methods of account-wide role creation
* AWS Identity and Access Management Data Types
* Amazon Elastic Computer Cloud Data Types
* AWS Token Security Service Data Types
* OpenShift Container Platform update life cycle
* Creating the account-wide STS roles and policies
* Creating a cluster with customizations using the CLI
* Creating a cluster with customizations by using {cluster-manager}
* AWS documentation about permissions boundaries for IAM entities
* Associating your AWS account
