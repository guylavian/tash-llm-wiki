---
title: "{product-title} clusters without a CNI plugin"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-cluster-no-cni
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-cluster-no-cni
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# {product-title} clusters without a CNI plugin

[id="rosa-hcp-cluster-no-cni"]
= OpenShift Container Platform clusters without a CNI plugin

[role="_abstract"]
You can create a OpenShift Container Platform cluster without a Container Network Interface (CNI) plugin so that you can install a third-party CNI plugin that meets your specific networking requirements. After cluster creation, you install your chosen CNI plugin to provide pod networking.

[IMPORTANT]
====
For customers who choose to use their own CNI, the responsibility of CNI plugin support belongs to the customer in coordination with their chosen CNI vendor.
====

The default plugin for OpenShift Container Platform is the OVN-Kubernetes network plugin. This plugin is the only Red Hat supported CNI plugin for OpenShift Container Platform.

If you use your own CNI for OpenShift Container Platform clusters, you must obtain commercial support from the plugin vendor before creating your clusters. Red{nbsp}Hat cannot assist with CNI-related issues, such as pod-to-pod traffic, but continues to provide support for all non-CNI issues. To receive CNI-related support from Red{nbsp}Hat, install the cluster with the default OVN-Kubernetes network plugin. For more information, see the responsibility matrix.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-fips-encryption.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster,  you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Configure a virtual private cloud (VPC)
* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

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
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc

[id="rosa-hcp-sts-creating-a-cluster-cli_{context}-no-cni"]
= Creating the cluster without a CNI plugin

[role="_abstract"]
You can create a OpenShift Container Platform cluster without a CNI plugin by using the `--no-cni` flag with the {rosa-cli-first}.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform in the AWS Console.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host. Run `rosa version` to see your currently installed version of the ROSA CLI. If a newer version is available, the CLI provides a link to download this upgrade.
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.
* You have created an OIDC configuration.
* You have verified that the AWS Elastic Load Balancing (ELB) service role exists in your AWS account.

.Procedure

. You can create your OpenShift Container Platform cluster with one of the following commands.
+
[NOTE]
====
When creating a OpenShift Container Platform cluster, the default machine Classless Inter-Domain Routing (CIDR) is `10.0.0.0/16`. If this does not correspond to the CIDR range for your VPC subnets, add `--machine-cidr <address_block>` to the following commands.
====
+
** Create a cluster with a single, initial machine pool, publicly available API, publicly available Ingress, and no CNI plugin by running the following command:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> \
    --sts --mode=auto --hosted-cp --operator-roles-prefix <operator-role-prefix> \
    --oidc-config-id <ID-of-OIDC-configuration> --subnet-ids=<public-subnet-id>,<private-subnet-id> --no-cni
----

** Create a cluster with a single, initial machine pool, privately available API, privately available Ingress, and no CNI plugin by running the following command:
+
[source,terminal]
----
$ rosa create cluster --private --cluster-name=<cluster_name> \
    --sts --mode=auto --hosted-cp --subnet-ids=<private-subnet-id> --no-cni
----

** If you used the `OIDC_ID`, `SUBNET_IDS`, and `OPERATOR_ROLES_PREFIX` variables to prepare your environment, you can continue to use those variables when creating your cluster without a CNI plugin. For example, run the following command:
+
[source,terminal]
----
$ rosa create cluster --hosted-cp --subnet-ids=$SUBNET_IDS --oidc-config-id=$OIDC_ID --cluster-name=<cluster_name> --operator-roles-prefix=$OPERATOR_ROLES_PREFIX --no-cni
----

. Check the status of your cluster by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
[IMPORTANT]
====
When you first log in to the cluster after it reaches `ready` status, the nodes are still in the `not ready` state until you install your own CNI plugin. After CNI installation, the nodes change to `ready`.
====
+
The following `State` field changes are listed in the output as the cluster installation progresses:
+
* `pending (Preparing account)`
* `installing (DNS setup in progress)`
* `installing`
* `ready`
+
[NOTE]
====
If the installation fails or the `State` field does not change to `ready` after more than 10 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for OpenShift Container Platform_.
====

. Track the progress of the cluster creation by watching the OpenShift Container Platform installation program logs. To check the logs, run the following command:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----
+
Optional: To watch for new log messages as the installation progresses, use the `--watch` argument.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc

[id="rosa-hcp-no-cni-install-cni-plugin_{context}"]
= Installing a CNI plugin

[role="_abstract"]
After creating a OpenShift Container Platform cluster without a CNI plugin, you must install the CNI plugin before the cluster nodes are ready and workloads can deploy. Until you install a CNI provider, components such as the web console, Ingress Controller, image registry, and monitoring stack are not available.

.Procedure

* Install your CNI plugin.
+
The nodes change from the `not ready` to `ready` state.

[role="_additional-resources"]
[id="additional-resources_rosa-hcp-cluster-no-cni"]
== Additional resources

* About custom Operator IAM role prefixes
* OVN-Kubernetes network plugin
* Responsibility matrix
* AWS prerequisites
