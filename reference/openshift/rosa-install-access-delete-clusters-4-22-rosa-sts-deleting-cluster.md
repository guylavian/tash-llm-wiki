---
title: "Deleting a ROSA cluster"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-sts-deleting-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-sts-deleting-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Deleting a ROSA cluster

[id="rosa-sts-deleting-cluster"]
= Deleting a ROSA cluster

[role="_abstract"]
This document provides steps to delete a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS). After deleting your cluster, you can also delete the AWS Identity and Access Management (IAM) resources that are used by the cluster.

[id="prerequisites_rosa-sts-deleting-cluster"]
== Prerequisites

* If OpenShift Container Platform created a VPC, you must remove the following items from your cluster before you can successfully delete your cluster:
** Network configurations, such as VPN configurations and VPC peering connections
** Any additional services that were added to the VPC

+
If these configurations and services remain, the cluster does not delete properly.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc

[id="rosa-deleting-cluster_{context}"]
= Deleting a ROSA cluster

= Deleting a ROSA cluster and the cluster-specific IAM resources

[role="_abstract"]
You can delete a OpenShift Container Platform (ROSA) cluster using the ROSA CLI (`rosa`).

[role="_abstract"]
You can delete a OpenShift Container Platform (ROSA) with AWS Security Token Service (STS) cluster by using the ROSA CLI (`rosa`) or {cluster-manager-first}.

After deleting the cluster, you can clean up the cluster-specific Identity and Access Management (IAM) resources in your AWS account by using the ROSA CLI (`rosa`). The cluster-specific resources include the Operator roles and the OpenID Connect (OIDC) provider.

[NOTE]
====
The cluster deletion must complete before you remove the IAM resources, because the resources are used in the cluster deletion and clean-up processes.
====

If add-ons are installed, the cluster deletion takes longer because add-ons are uninstalled before the cluster is deleted. The amount of time depends on the number and size of the add-ons.

[IMPORTANT]
====
If the cluster that created the VPC during the installation is deleted, the associated installation program-created VPC will also be deleted, resulting in the failure of all the clusters that are using the same VPC. Additionally, any resources created with the same `tagSet` key-value pair of the resources created by the installation program and labeled with a value of `owned` will also be deleted.
====
.Prerequisites

* You have installed a ROSA cluster.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.

.Procedure

. Obtain the cluster ID, the Amazon Resource Names (ARNs) for the cluster-specific Operator roles and the endpoint URL for the OIDC provider:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name:                       mycluster
ID:                         1s3v4x39lhs8sm49m90mi0822o34544a
...
Operator IAM Roles:
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-machine-api-aws-cloud-credentials
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-cloud-credential-operator-cloud-crede
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-image-registry-installer-cloud-creden
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-cluster-csi-drivers-ebs-cloud-credent
 - arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-cloud-network-config-controller-cloud
State:                      ready
Private:                    No
Created:                    May 13 2022 11:26:15 UTC
Details Page:               https://console.redhat.com/openshift/details/s/296kyEFwzoy1CREQicFRdZybrc0
OIDC Endpoint URL:          https://oidc.op1.openshiftapps.com/<oidc_config_id>
----
+
--
* The `ID` field lists the cluster ID.
* The `Operator IAM Roles` field specifies the ARNs for the cluster-specific Operator roles. For example, in the sample output the ARN for the role required by the Machine Config Operator is `arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-machine-api-aws-cloud-credentials`.
* The `OIDC Endpoint URL` field displays the endpoint URL for the cluster-specific OIDC provider.
--
+
[IMPORTANT]
====
You require the cluster ID to delete the cluster-specific STS resources using the ROSA CLI (`rosa`) after the cluster is deleted.
====

. Delete the cluster:
** To delete the cluster by using {cluster-manager-first}:
.. Navigate to {cluster-manager-url}.
.. Click the Options menu {kebab} next to your cluster and select *Delete cluster*.
.. Type the name of your cluster at the prompt and click *Delete*.
** To delete the cluster using the ROSA CLI (`rosa`):
.. Enter the following command to delete the cluster and watch the logs, replacing `<cluster_name>` with the name or ID of your cluster:
. Enter the following command to delete a cluster and watch the logs, replacing `<cluster_name>` with the name or ID of your cluster:
+
[source,terminal]
----
$ rosa delete cluster --cluster=<cluster_name> --watch
----
+
[IMPORTANT]
====
You must wait for the cluster deletion to complete before you remove the Operator roles and the OIDC provider. The cluster-specific Operator roles are required to clean-up the resources created by the OpenShift Operators. The Operators use the OIDC provider to authenticate.
====

. To clean up your CloudFormation stack, enter the following command:
+
[source,terminal]
----
$ rosa init --delete
----

.  Delete the OIDC provider that the cluster Operators use to authenticate:
+
[source,terminal]
----
$ rosa delete oidc-provider -c <cluster_id> --mode auto
----
+
[NOTE]
====
You can use the `-y` option to automatically answer yes to the prompts.
====
+
. Optional. Delete the cluster-specific Operator IAM roles:
+
[IMPORTANT]
====
The account-wide IAM roles can be used by other ROSA clusters in the same AWS account. Only remove the roles if they are not required by other clusters.
====
+
[source,terminal]
----
$ rosa delete operator-roles -c <cluster_id> --mode auto
----

[role="_additional-resources"]
.Additional resources

* Deleting the account-wide IAM roles and policies

* Unlinking and deleting the {cluster-manager} and user IAM roles

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc

[id="rosa-deleting-cluster-troubleshooting_{context}"]
= Troubleshooting cluster deletion

[role="_abstract"]
Troubleshooting issues that prevent cluster deletion involves verifying IAM configurations and confirming the removal of resource dependencies.

.Procedure

. If the cluster cannot be deleted because of missing IAM roles, see Repairing a cluster that cannot be deleted.

. If the cluster cannot be deleted for other reasons:
.. Check that there are no Add-ons for your cluster pending in the {hybrid-console-second}.
.. Check that all AWS resources and dependencies have been deleted in the Amazon Web Console.
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc
// *rosa_hcp/rosa-hcp-deleting-cluster.adoc

[id="rosa-deleting-sts-resources-account-wide_{context}"]
= Deleting the account-wide IAM resources

[role="_abstract"]
You can delete the account-wide AWS Identity and Access Management (IAM) resources. First, delete all OpenShift Container Platform clusters that depend on these resources.

If you no longer need {cluster-manager-first} to install OpenShift Container Platform clusters, you can delete the {cluster-manager} and user IAM roles.

[IMPORTANT]
====
The account-wide IAM roles and policies might be used by other OpenShift Container Platform clusters in the same AWS account. Only remove the resources if they are not required by other clusters.

The {cluster-manager} and user IAM roles are required for other OpenShift Container Platform clusters in the same AWS account. These roles enable you to install, manage, and delete clusters by using {cluster-manager}. Only remove them if you no longer need to manage OpenShift Container Platform clusters in your account. If these roles are removed before cluster deletion, see "Repairing a cluster that cannot be deleted" in _Troubleshooting cluster deployments_.
====
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc
// *rosa_hcp/rosa-hcp-deleting-cluster.adoc

[id="rosa-deleting-account-wide-iam-roles-and-policies_{context}"]
= Deleting the account-wide IAM roles and policies

[role="_abstract"]
You can delete the account-wide IAM roles and policies that you created for OpenShift Container Platform deployments, along with the account-wide Operator policies. You can delete the account-wide IAM roles and policies only after deleting all OpenShift Container Platform clusters that depend on them.

[IMPORTANT]
====
The account-wide IAM roles and policies might be used by other OpenShift Container Platform clusters in the same AWS account. Only remove the roles if they are not required by other clusters.
====

.Prerequisites

* You have account-wide IAM roles that you want to delete.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.

.Procedure

. Delete the account-wide roles:
.. List the account-wide roles in your AWS account by using the ROSA CLI (`rosa`):
+
[source,terminal]
----
$ rosa list account-roles
----
+
.Example output
[source,terminal]
----
I: Fetching account roles
ROLE NAME                           ROLE TYPE      ROLE ARN                                                           OPENSHIFT VERSION
ManagedOpenShift-ControlPlane-Role  Control plane  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-ControlPlane-Role  4.22
ManagedOpenShift-Installer-Role     Installer      arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Installer-Role     4.22
ManagedOpenShift-Support-Role       Support        arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Support-Role       4.22
ManagedOpenShift-Worker-Role        Worker         arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-Worker-Role        4.22
----
+
[source,terminal]
----
I: Fetching account roles
ROLE NAME                                 ROLE TYPE      ROLE ARN                                                                 OPENSHIFT VERSION  AWS Managed
ManagedOpenShift-HCP-ROSA-Installer-Role  Installer      arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-HCP-ROSA-Installer-Role  4.22               Yes
ManagedOpenShift-HCP-ROSA-Support-Role    Support        arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-HCP-ROSA-Support-Role    4.22               Yes
ManagedOpenShift-HCP-ROSA-Worker-Role     Worker         arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-HCP-ROSA-Worker-Role     4.22               Yes
----
+
.. Delete the account-wide roles by running one of the following commands:
*** For clusters without a shared Virtual Private Cloud (VPC):
+
[source,terminal]
----
$ rosa delete account-roles --prefix <prefix> --mode auto
----
+
You must include the `--<prefix>` argument. Replace `<prefix>` with the prefix of the account-wide roles to delete. If you did not specify a custom prefix when you created the account-wide roles, specify the default prefix, `ManagedOpenShift`.
+
*** For clusters with a shared VPC:
+
[source,terminal]
----
$ rosa delete account-roles --prefix <prefix> --delete-hosted-shared-vpc-policies --mode auto
----
+
You must include the `--<prefix>` argument. Replace `<prefix>` with the prefix of the account-wide roles to delete. If you did not specify a custom prefix when you created the account-wide roles, specify the default prefix, `ManagedOpenShift`.
+
[IMPORTANT]
====
The account-wide IAM roles might be used by other OpenShift Container Platform clusters in the same AWS account. Only remove the roles if they are not required by other clusters.
====
+
.Example output
[source,terminal]
----
W: There are no classic account roles to be deleted
I: Deleting hosted CP account roles
? Delete the account role 'delete-rosa-HCP-ROSA-Installer-Role'? Yes
I: Deleting account role 'delete-rosa-HCP-ROSA-Installer-Role'
? Delete the account role 'delete-rosa-HCP-ROSA-Support-Role'? Yes
I: Deleting account role 'delete-rosa-HCP-ROSA-Support-Role'
? Delete the account role 'delete-rosa-HCP-ROSA-Worker-Role'? Yes
I: Deleting account role 'delete-rosa-HCP-ROSA-Worker-Role'
I: Successfully deleted the hosted CP account roles
----

. Delete the account-wide in-line and Operator policies:
.. Under the *Policies* page in the AWS IAM Console, filter the list of policies by the prefix that you specified when you created the account-wide roles and policies.
+
[NOTE]
====
If you did not specify a custom prefix when you created the account-wide roles, search for the default prefix, `ManagedOpenShift`.
====
+
.. Delete the account-wide policies and Operator policies by using the AWS IAM Console. For more information about deleting IAM policies by using the AWS IAM Console, see Deleting IAM policies in the AWS documentation.
+
[IMPORTANT]
====
The account-wide and Operator IAM policies might be used by other OpenShift Container Platform clusters in the same AWS account. Only remove the roles if they are not required by other clusters.
====
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc
// * rosa_hcp/rosa-hcp-deleting-cluster.adoc

[id="rosa-unlinking-and-deleting-ocm-and-user-iam-roles_{context}"]
= Unlinking and deleting the {cluster-manager} and user IAM roles

[role="_abstract"]
When you install a OpenShift Container Platform cluster by using {cluster-manager-first}, you also create {cluster-manager} and user Identity and Access Management (IAM) roles linked to your Red{nbsp}Hat organization. After deleting your cluster, you can unlink and delete the roles by using the {rosa-cli-first}.

[IMPORTANT]
====
The {cluster-manager} and user IAM roles are required to install and manage other OpenShift Container Platform clusters in the same AWS account using {cluster-manager}. Only remove the roles if you no longer need to use the {cluster-manager} to install OpenShift Container Platform clusters.
====

.Prerequisites

* You created {cluster-manager} and user IAM roles and linked them to your Red{nbsp}Hat organization.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.
* You have organization administrator privileges in your Red{nbsp}Hat organization.

.Procedure

. Unlink the {cluster-manager} IAM role from your Red{nbsp}Hat organization and delete the role:
.. List the {cluster-manager} IAM roles in your AWS account:
+
[source,terminal]
----
$ rosa list ocm-roles
----
+
.Example output
[source,terminal]
----
I: Fetching ocm roles
ROLE NAME                           ROLE ARN                                                                      LINKED  ADMIN
ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>  Yes     Yes
----
+
.Example output
[source,terminal]
----
I: Fetching ocm roles
ROLE NAME                                                     ROLE ARN                                                                                         LINKED  ADMIN  AWS Managed
ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>  Yes      Yes     Yes
----
+
.. If your {cluster-manager} IAM role is listed as linked, unlink it from your Red{nbsp}Hat organization by running the following command:
+
[source,terminal]
----
$ rosa unlink ocm-role --role-arn <arn>
----
+
Replace `<arn>` with the Amazon Resource Name (ARN) for your {cluster-manager} IAM role. The ARN is specified in the output of the preceding command. In the preceding example, the ARN is in the format `arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>`.
+
.Example output
[source,terminal]
----
I: Unlinking OCM role
? Unlink the 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' role from organization '<red_hat_organization_id>'? Yes
I: Successfully unlinked role-arn 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' from organization account '<red_hat_organization_id>'
----
+
.. Delete the {cluster-manager} IAM role and policies:
+
[source,terminal]
----
$ rosa delete ocm-role --role-arn <arn>
----
+
.Example output
[source,terminal]
----
I: Deleting OCM role
? OCM Role ARN: arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>
? Delete 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-OCM-Role-<red_hat_organization_external_id>' ocm role? Yes
? OCM role deletion mode: auto
I: Successfully deleted the OCM role
----
+
The `OCM role deletion mode` field specifies the deletion mode. You can use `auto` mode to automatically delete the {cluster-manager} IAM role and policies. In `manual` mode, the ROSA CLI generates the `aws` commands needed to delete the role and policies. `manual` mode enables you to review the details before running the `aws` commands manually.

. Unlink the user IAM role from your Red{nbsp}Hat organization and delete the role:
.. List the user IAM roles in your AWS account:
+
[source,terminal]
----
$ rosa list user-roles
----
+
.Example output
[source,terminal]
----
I: Fetching user roles
ROLE NAME                                  ROLE ARN                                                                  LINKED
ManagedOpenShift-User-<ocm_user_name>-Role  arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role  Yes
----
+
.. If your user IAM role is listed as linked in the output of the preceding command, unlink the role from your Red{nbsp}Hat organization:
+
[source,terminal]
----
$ rosa unlink user-role --role-arn <arn>
----
+
Replace `<arn>` with the Amazon Resource Name (ARN) for your user IAM role. The ARN is specified in the output of the preceding command. In the preceding example, the ARN is in the format `arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role`.
+
.Example output
[source,terminal]
----
I: Unlinking user role
? Unlink the 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role' role from the current account '<ocm_user_account_id>'? Yes
I: Successfully unlinked role ARN 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role' from account '<ocm_user_account_id>'
----
+
.. Delete the user IAM role:
+
[source,terminal]
----
$ rosa delete user-role --role-arn <arn>
----
+
.Example output
[source,terminal]
----
I: Deleting user role
? User Role ARN: arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role
? Delete the 'arn:aws:iam::<aws_account_id>:role/ManagedOpenShift-User-<ocm_user_name>-Role' role from the AWS account? Yes
? User role deletion mode: auto
I: Successfully deleted the user role
----
The `User role deletion mode` field specifies the deletion mode. You can use `auto` mode to automatically delete the user IAM role. In `manual` mode, the ROSA CLI generates the `aws` command needed to delete the role. `manual` mode enables you to review the details before running the `aws` command manually.

[role="_additional-resources"]
[id="additional-resources_rosa-sts-deleting-cluster"]
== Additional resources

* ROSA CLI command reference
* About IAM resources
* Repairing a cluster that cannot be deleted
