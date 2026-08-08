---
title: "Deleting a {product-title} cluster"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-deleting-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-deleting-cluster
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# Deleting a {product-title} cluster

[id="rosa-hcp-deleting-cluster"]
= Deleting a OpenShift Container Platform cluster

[role="_abstract"]
You can delete a OpenShift Container Platform cluster by using either the {cluster-manager-first} or the {rosa-cli-first}. After deleting the cluster, you can clean up the AWS Identity and Access Management (IAM) resources that were used by the cluster.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-deleting-cluster.adoc

[id="rosa-hcp-deleting-cluster_{context}"]
= Deleting a OpenShift Container Platform cluster and the cluster-specific IAM resources

[role="_abstract"]
If you no longer need a OpenShift Container Platform cluster, you can delete it to stop incurring costs. After deleting the cluster, you must also remove the cluster-specific Operator roles and OpenID Connect (OIDC) provider to avoid leaving unused IAM resources in your AWS account.

[NOTE]
====
The cluster deletion must complete before you remove the IAM resources, because the resources are used in the cluster deletion and clean up processes.
====

If add-ons are installed, the cluster deletion takes longer because add-ons are uninstalled before the cluster is deleted. The amount of time depends on the number and size of the add-ons.

.Prerequisites

* You have installed a OpenShift Container Platform cluster.
* You have installed and configured the latest {rosa-cli} on your installation host.

.Procedure

. Get the cluster ID, the Amazon Resource Names (ARNs) for the cluster-specific Operator roles, and the endpoint URL for the OIDC provider by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name:                       test_cluster
Domain Prefix:              test_cluster
Display Name:               test_cluster
ID:                         <cluster_id>
External ID:                <external_id>
Control Plane:              ROSA Service Hosted
OpenShift Version:          4.22.0
Channel Group:              stable
DNS:                        test_cluster.l3cn.p3.openshiftapps.com
AWS Account:                <AWS_id>
AWS Billing Account:        <AWS_id>
API URL:                    https://api.test_cluster.l3cn.p3.openshiftapps.com:443
Console URL:
Region:                     us-east-1
Availability:
 - Control Plane:           MultiAZ
 - Data Plane:              SingleAZ

Nodes:
 - Compute (desired):       2
 - Compute (current):       0
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            172.30.0.0/16
 - Machine CIDR:            10.0.0.0/16
 - Pod CIDR:                10.128.0.0/14
 - Host Prefix:             /23
 - Subnets:                 <subnet_ids>
EC2 Metadata Http Tokens:   optional
Role (STS) ARN:             arn:aws:iam::<AWS_id>:role/test_cluster-HCP-ROSA-Installer-Role
Support Role ARN:           arn:aws:iam::<AWS_id>:role/test_cluster-HCP-ROSA-Support-Role
Instance IAM Roles:
 - Worker:                  arn:aws:iam::<AWS_id>:role/test_cluster-HCP-ROSA-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<AWS_id>:role/test_cluster-openshift-cloud-network-config-controller-cloud-crede
 - arn:aws:iam::<AWS_id>:role/test_cluster-openshift-image-registry-installer-cloud-credentials
 - arn:aws:iam::<AWS_id>:role/test_cluster-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<AWS_id>:role/test_cluster-kube-system-kube-controller-manager
 - arn:aws:iam::<AWS_id>:role/test_cluster-kube-system-capa-controller-manager
 - arn:aws:iam::<AWS_id>:role/test_cluster-kube-system-control-plane-operator
 - arn:aws:iam::<AWS_id>:role/hcpcluster-kube-system-kms-provider
 - arn:aws:iam::<AWS_id>:role/test_cluster-openshift-cluster-csi-drivers-ebs-cloud-credentials
Managed Policies:           Yes
State:                      ready
Private:                    No
Created:                    Apr 16 2024 20:32:06 UTC
User Workload Monitoring:   Enabled
Details Page:               https://console.redhat.com/openshift/details/s/<cluster_id>
OIDC Endpoint URL:          https://oidc.op1.openshiftapps.com/<cluster_id> (Managed)
Audit Log Forwarding:       Disabled
External Authentication:    Disabled
----
+
--
where:

* The `ID` field lists the cluster ID.
* The `Operator IAM Roles` field specifies the ARNs for the cluster-specific Operator roles. For example, in the sample output the ARN for the role required by the Machine Config Operator is `arn:aws:iam::<aws_account_id>:role/mycluster-x4q9-openshift-machine-api-aws-cloud-credentials`.
* The `OIDC Endpoint URL` field displays the endpoint URL for the cluster-specific OIDC provider.
+
[IMPORTANT]
====
After the cluster is deleted, you need the cluster ID to delete the cluster-specific STS resources using the {rosa-cli}.
====
--

. Delete the cluster by using either the {cluster-manager} or the {rosa-cli}:
** To delete the cluster by using the {cluster-manager}:
.. Navigate to the {cluster-manager-url}.
.. Click the Options menu {kebab} next to your cluster and select *Delete cluster*.
.. Type the name of your cluster into the prompt and click *Delete*.
** To delete the cluster using the {rosa-cli}:
.. Run the following command, replacing `<cluster_name>` with the name or ID of your cluster:
+
[source,terminal]
----
$ rosa delete cluster --cluster=<cluster_name> --watch
----
+
[IMPORTANT]
====
You must wait for cluster deletion to complete before you remove the Operator roles and the OIDC provider.
====

. Delete the cluster-specific Operator IAM roles by running one of the following commands:
** For clusters without a shared Virtual Private Cloud (VPC):
+
[source,terminal]
----
$ rosa delete operator-roles --prefix <operator_role_prefix>
----
+
** For clusters with a shared VPC:
+
[source,terminal]
----
$ rosa delete operator-roles --prefix <operator_role_prefix> --delete-hosted-shared-vpc-policies
----

.  Delete the OIDC provider by running the following command:
+
[source,terminal]
----
$ rosa delete oidc-provider --oidc-config-id <oidc_config_id>
----

.Troubleshooting
* Verify that there are no add-ons for your cluster pending in the Hybrid Cloud Console.
* Verify that all AWS resources and dependencies have been deleted in the Amazon Web Console.

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

[role="_additional-resources"]
.Additional resources

* About IAM resources

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
