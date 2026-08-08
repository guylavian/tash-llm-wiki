---
title: "Creating an AWS PrivateLink cluster on ROSA"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-aws-privatelink-creating-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Creating an AWS PrivateLink cluster on ROSA

[id="rosa-aws-privatelink-creating-cluster"]
= Creating an AWS PrivateLink cluster on ROSA

[role="_abstract"]
You can create a OpenShift Container Platform cluster using AWS PrivateLink.

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
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
[id="osd-aws-privatelink-about_{context}"]
= Understanding AWS PrivateLink

[role="_abstract"]
AWS PrivateLink enables private connectivity for OpenShift Container Platform clusters without requiring public networking infrastructure.

All {hcp-title} clusters are created with an AWS PrivateLink connection to expose the private Kubernetes API server to the customer's virtual private cloud (VPC).
A OpenShift Container Platform cluster can be created without any requirements on public subnets, internet gateways, or network address translation (NAT) gateways. In this configuration, Red{nbsp}Hat uses AWS PrivateLink to manage and monitor a cluster to avoid all public ingress network traffic. Without a public subnet, it is not possible to configure an application router as public. Configuring private application routers is the only option.

For more information, see AWS PrivateLink on the AWS website.

[IMPORTANT]
====
You can only make a PrivateLink cluster at installation time. You cannot change a cluster to PrivateLink after installation.
====

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
[id="osd-aws-privatelink-required-resources_{context}"]
= Requirements for using AWS PrivateLink clusters

[role="_abstract"]
AWS PrivateLink clusters require specific AWS resources including VPC, private subnets, and network access controls.

For {hcp-title} private clusters, internet gateways, NAT gateways, and public subnets are not required, but the private subnets must have internet connectivity to install the required components. At least one private subnet is required. The following table shows the AWS resources that are required for a successful installation:
For AWS PrivateLink clusters, internet gateways, NAT gateways, and public subnets are not required, but the private subnets must have internet connectivity provided to install required components. At least one single private subnet is required for Single-AZ clusters and at least 3 private subnets are required for Multi-AZ clusters. The following table shows the AWS resources that are required for a successful installation:

.Required AWS resources
[cols="1a,2a,3a",options="header"]
|===
| Component | AWS Type | Description
| VPC
|* AWS::EC2::VPC
* AWS::EC2::VPCEndpoint
| You must provide a VPC for the cluster to use.

| Network access control
|* AWS::EC2::NetworkAcl
* AWS::EC2::NetworkAclEntry
|
You must allow access to the following ports:
[cols="35%,65%",options="header"]
!===
!Port !Reason
! 80
! Inbound HTTP traffic
! 443
! Inbound HTTPS traffic
! 22
! Inbound SSH traffic
! 1024-65535
! Inbound ephemeral traffic
! 0-65535
! Outbound ephemeral traffic
!===

| Private subnets
|* AWS::EC2::Subnet
* AWS::EC2::RouteTable
* AWS::EC2::SubnetRouteTableAssociation
|
Your VPC must have private subnets in at least 1 availability zone.
Your VPC must have private subnets in 1 availability zone for Single-AZ deployments or 3 availability zones for Multi-AZ deployments.
You must provide appropriate routes and route tables.
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
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc

[id="rosa-aws-privatelink-create-cluster_{context}"]
= Creating an AWS PrivateLink cluster

[role="_abstract"]
Creating a OpenShift Container Platform cluster with AWS PrivateLink establishes a private connection for cluster management and operations.

[NOTE]
====
AWS PrivateLink is supported on existing VPCs only.
====

.Prerequisites

* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli}, on your installation host.

.Procedure

. With AWS PrivateLink, you can create a cluster with a single availability zone (Single-AZ) or multiple availability zones (Multi-AZ). In either case, your machine's classless inter-domain routing (CIDR) must match your virtual private cloud's CIDR. See https://docs.openshift.com/container-platform/4.14/installing/installing_aws/installing-aws-vpc.html#installation-custom-aws-vpc-requirements_installing-aws-vpc[Requirements for using your own VPC] and VPC Validation for more information.
+
[IMPORTANT]
====
If you use a firewall, you must configure it so that OpenShift Container Platform can access the sites that it requires to function.

For more information, see the AWS PrivateLink firewall prerequisites section.
====
+
--
--
+
** To create a Single-AZ cluster:
+
[source,terminal]
----
$ rosa create cluster --private-link --cluster-name=<cluster-name> [--machine-cidr=<VPC CIDR>/16] --subnet-ids=<private-subnet-id>
----
** To create a Multi-AZ cluster:
+
[source,terminal]
----
$ rosa create cluster --private-link --multi-az --cluster-name=<cluster-name> [--machine-cidr=<VPC CIDR>/16] --subnet-ids=<private-subnet-id1>,<private-subnet-id2>,<private-subnet-id3>
----

. Enter the following command to check the status of your cluster. During cluster creation, the `State` field from the output will transition from `pending` to `installing`, and finally to `ready`.
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
[NOTE]
====
If installation fails or the `State` field does not change to `ready` after 40 minutes, check the installation troubleshooting documentation for more details.
====

. Enter the following command to follow the OpenShift installer logs to track the progress of your cluster:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc

[id="osd-aws-privatelink-config-dns-forwarding_{context}"]
= Configuring AWS PrivateLink DNS forwarding

[role="_abstract"]
Configure DNS forwarding to enable resolution of cluster DNS records from outside the VPC.

With AWS PrivateLink clusters, a public hosted zone and a private hosted zone are created in Route 53. With the private hosted zone, records within the zone are resolvable only from within the VPC to which it is assigned.

The _Let's Encrypt DNS-01_ validation requires a public zone so that valid, publicly trusted certificates can be issued for the domain. The validation records are deleted after _Let's Encrypt_ validation is complete; however, the zone is still required for issuing and renewing these certificates, which are typically required every 60 days. While these zones usually appear empty, it is serving a critical role in the validation process.

For more information about private hosted zones, see AWS private hosted zones documentation. For more information about public hosted zones, see AWS public hosted zones documentation.

.Prerequisites

* Your corporate network or other VPC has connectivity
* UDP port 53 and TCP port 53 ARE enabled across your networks to allow for DNS queries
* You have created an AWS PrivateLink cluster using OpenShift Container Platform

.Procedure

. To allow for records such as `api.<cluster_domain>` and `*.apps.<cluster_domain>` to resolve outside of the VPC, configure a Route 53 Resolver Inbound Endpoint.

. When you configure the inbound endpoint, select the VPC and private subnets that were used when you created the cluster.

. After the endpoints are operational and associated, configure your corporate network to forward DNS queries to those IP addresses for the top-level cluster domain, such as `drow-pl-01.htno.p1.openshiftapps.com`.

. If you are forwarding DNS queries from one VPC to another VPC, configure forwarding rules.

. If you are configuring your remote network DNS server, see your specific DNS server documentation to configure selective DNS forwarding for the installed cluster domain.

[role="_additional-resources"]
== Additional resources

* Configure identity providers
* Adding notification contacts
* Firewall prerequisites for OpenShift Container Platform
* Firewall prerequisites for OpenShift Container Platform clusters using STS
* Firewall prerequisites
* Overview of the OpenShift Container Platform deployment workflow
* Deleting a OpenShift Container Platform cluster
* OpenShift Container Platform architecture models
