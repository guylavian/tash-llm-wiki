---
title: "Prerequisites checklist for deploying {product-title}"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-cloud-expert-prereq-checklist
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-cloud-expert-prereq-checklist
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Prerequisites checklist for deploying {product-title}

[id="rosa-cloud-expert-prereq-checklist"]
= Prerequisites checklist for deploying OpenShift Container Platform

//Mobb content metadata
//Brought into ROSA product docs 2023-09-15; does not follow typical OpenShift documentation formatting
//---
//date: '2023-07-27'
//title: Prerequisites Checklist to Deploy ROSA Cluster with STS
//tags: ["ROSA", "STS"]
//authors:
//  - Byron Miller
//  - Connor Wooley
//  - Diana Sari
//---

[role="_abstract"]
This is a high level checklist of prerequisites needed to create a OpenShift Container Platform cluster with STS.
This is a high level checklist of prerequisites needed to create a OpenShift Container Platform cluster.

//TODO OSDOCS-11789: Consider adding the following to a subsection about the initiating/control machine, along with CLI sections?
The machine that you run the installation process from must have access to the following:

* Amazon Web Services API and authentication service endpoints
* Red{nbsp}Hat OpenShift API and authentication service endpoints (`api.openshift.com` and `sso.redhat.com`)
* Internet connectivity to obtain installation artifacts during deployment
//TODO OSDOCS-13133 update when zero egress is GA: "either during deployment or prior to deploying a cluster with egress zero enabled"

//TODO OSDOCS-11789: This needs to be accessible from parts of the cluster, but not the deploying machine - omit entirely, or leave in place for Classic?
[IMPORTANT]
====
Starting with version 1.2.7 of the {rosa-cli-first}, all OIDC provider endpoint URLs on new clusters use Amazon CloudFront and the oidc.op1.openshiftapps.com domain. This change improves access speed, reduces latency, and improves resiliency for new clusters created with the {rosa-cli} 1.2.7 or later. There are no supported migration paths for existing OIDC provider configurations.
====

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-accounts_{context}"]
= Accounts and permissions

[role="_abstract"]
Ensure that you have the following accounts, credentials, and permissions.
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-aws-account_{context}"]
= AWS account

[role="_abstract"]
You must have an AWS account with certain permissions before creating your cluster.

* Create an AWS account if you do not already have one.
* Gather the credentials required to log in to your AWS account.
* Ensure that your AWS account has sufficient permissions to use the {rosa-cli}.
//OSDOCS-11789: Moving these here because it is a permission / account level enablement
* Enable OpenShift Container Platform for your AWS account on the AWS console.
** If your account is the management account for your organization (used for AWS billing purposes), you must have `aws-marketplace:Subscribe` permissions available on your account. See _Service control policy (SCP) prerequisites_ for more information, or see the AWS documentation for troubleshooting: AWS Organizations service control policy denies required AWS Marketplace permissions.
* Ensure you have not enabled restrictive tag policies. For more information, see Tag policies in the AWS documentation.

[role="_additional-resources"]
[id="additional-resources_mos-checklist-aws-account"]
.Additional resources

* Least privilege permissions for common {rosa-cli} commands

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-rh-account_{context}"]
= Red{nbsp}Hat account

[role="_abstract"]
Create your Red{nbsp}Hat account to maintain your Red{nbsp}Hat resources.

//TODO OSDOCS-11789: Do we need to mention RH Organization here also?
* Create a Red{nbsp}Hat account for the {hybrid-console} if you do not already have one.
* Gather the credentials required to log in to your Red{nbsp}Hat account.
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-cli-requirements_{context}"]
= CLI requirements

[role="_abstract"]
You need to download and install several CLI (command-line interface) tools to be able to deploy a cluster.
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-aws-cli_{context}"]
= AWS CLI (`aws`)

[role="_abstract"]
The AWS CLI tool allows you to interact with AWS resources directly.

.Procedure
. Install the AWS Command Line Interface.
. Log in to your AWS account using the AWS CLI: Sign in through the AWS CLI
. Verify your account identity:
+
[source,terminal]
----
 $ aws sts get-caller-identity
----
. Check whether the service role for ELB (Elastic Load Balancing) exists:
+
[source,terminal]
----
$ aws iam get-role --role-name "AWSServiceRoleForElasticLoadBalancing"
----
+
If the role does not exist, create it by running the following command:
+
[source,terminal]
----
$ aws iam create-service-linked-role --aws-service-name "elasticloadbalancing.amazonaws.com"
----
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-_{context}"]
= {rosa-cli-first}

[role="_abstract"]
Install the {rosa-cli} on in your local environment.

.Procedure

. Install the {rosa-cli} from the web console.
. Log in to your Red{nbsp}Hat account by running `rosa login` and following the instructions in the command output:
+
[source,terminal]
----
$ rosa login
To login to your Red{nbsp}Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
? Copy the token and paste it here:
----
+
Alternatively, you can copy the full `$ rosa login --token=abc...` command and paste that in the terminal:
+
[source,terminal]
----
$ rosa login --token=<abc..>
----
. Confirm you are logged in using the correct account and credentials:
+
[source,terminal]
----
$ rosa whoami
----

[role="_additional-resources"]
[id="additional-resources_mos-checklist-rosa-cli"]
.Additional resources

* Installing the {rosa-cli}

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-oc-cli_{context}"]
= OpenShift CLI (`oc`)

[role="_abstract"]
The OpenShift CLI (`oc`) is not required to deploy a OpenShift Container Platform cluster, but is a useful tool for interacting with your cluster after it is deployed.

.Procedure
. Download and install `oc` from the {cluster-manager} Command-line interface (CLI) tools page, or follow the instructions in the _Additional resources_.
. Verify that the OpenShift CLI has been installed correctly by running the following command:
+
[source,terminal]
----
$ rosa verify openshift-client
----

[role="_additional-resources"]
[id="additional-resources_mos-checklist-oc-cli"]
.Additional resources

* Getting started with the OpenShift CLI

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-aws-infra-prereqs_{context}"]
//TODO OSDOCS-11789: Moved quota check to the point where it is actually useful - yes, this is checked during install, but it's also worth checking ahead of time so that any issues are known during preparation rather than deployment.
= AWS infrastructure prerequisites

[role="_abstract"]
Before you create your cluster, you need to have sufficient AWS quota.

.Procedure
* To verify that your AWS account has sufficient quota available to deploy a cluster, run the following command:
+
[source,terminal]
----
$ rosa verify quota
----
+
This command only checks the total quota allocated to your account; it does not reflect the amount of quota already consumed from that quota. Running this command is optional because your quota is verified during cluster deployment. However, Red{nbsp}Hat recommends running this command to confirm your quota ahead of time so that deployment is not interrupted by issues with quota availability.

[role="_additional-resources"]
[id="additional-resources_mos-checklist-aws-infra-prereqs"]
.Additional resources

* Provisioned AWS Infrastructure
* Required AWS service quotas
* Provisioned AWS Infrastructure
* Required AWS service quotas

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-scp-prereqs_{context}"]
= Service Control Policy (SCP) prerequisites

[role="_abstract"]
OpenShift Container Platform clusters are hosted in an AWS account within an AWS organizational unit. A service control policy (SCP) is created and applied to the AWS organizational unit that manages what services the AWS sub-accounts are permitted to access.

* Ensure that your organization's SCPs are not more restrictive than the roles and policies required by the cluster.
* When you create a OpenShift Container Platform cluster, an associated AWS OpenID Connect (OIDC) identity provider is created.

[role="_additional-resources"]
[id="additional-resources_mos-checklist-scp-prereqs"]
.Additional resources

* Minimum set of effective permissions for SCPs

[id="mos-checklist-networking-prereqs"]
== Networking prerequisites
// include::modules/mos-checklist-networking-prereqs.adoc[leveloffset=+1]
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-_firewall_{context}"]
= Firewall

[role="_abstract"]
You must configure your firewall so that your cluster can access the required domains and ports.

* Configure your firewall to allow access to the domains and ports listed in
AWS firewall prerequisites.
AWS firewall prerequisites.
//Moving up prereqs that are actually required for deployment
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-vpc-privatelink_{context}"]
= VPC requirements for PrivateLink clusters

[role="_abstract"]
If you choose to deploy a PrivateLink cluster, then be sure to deploy the cluster in the pre-existing BYO VPC:

.Procedure
. Create a public and private subnet for each AZ that your cluster uses.
* Alternatively, implement transit gateway for internet and egress with appropriate routes.
. The VPC's CIDR block must contain the `Networking.MachineCIDR` range, which is the IP address for cluster machines.
* The subnet CIDR blocks must belong to the machine CIDR that you specify.
. Set both `enableDnsHostnames` and `enableDnsSupport` to `true`.
* That way, the cluster can use the Route 53 zones that are attached to the VPC to resolve cluster internal DNS records.
. Verify route tables by running:
+
[source,terminal]
 ----
 $ aws ec2 describe-route-tables --filters "Name=vpc-id,Values=<vpc-id>"
 ----
+
.. Ensure that the cluster can egress either through NAT gateway in public subnet or through transit gateway.
.. Ensure whatever UDR you want to follow is set up.
. You can also configure a cluster-wide proxy during or after install.
+
[NOTE]
====
You can install a non-PrivateLink OpenShift Container Platform cluster in a pre-existing BYO VPC.
====

[role="_additional-resources"]
[id="additional-resources_mos-checklist-vpc-privatelink"]
.Additional resources

* Configuring a cluster-wide proxy
// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-vpc-post-install_{context}"]
= Create VPC before cluster deployment

[role="_abstract"]
OpenShift Container Platform clusters must be deployed into an existing AWS Virtual Private Cloud (VPC).

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-add-custom-sgs_{context}"]
= Additional custom security groups

[role="_abstract"]
During cluster creation, you can add additional custom security groups to a cluster that has an existing non-managed VPC. To do so, complete these prerequisites before you create the cluster:

* Create the custom security groups in AWS before you create the cluster.
* Associate the custom security groups with the VPC that you are using to create the cluster. Do not associate the custom security groups with any other VPC.
* You may need to request additional AWS quota for `Security groups per network interface`.

[role="_additional-resources"]
[id="additional-resources_mos-checklist-add-custom-sgs"]
.Additional resources

* Security groups
* Security groups

// Module included in the following assemblies:
//
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
[id="mos-checklist-custom-dns-domains_{context}"]
= Custom DNS and domains

[role="_abstract"]
You can configure a custom domain name server and custom domain name for your cluster.

.Prerequisites
* By default, OpenShift Container Platform clusters require you to set the `domain name servers` option to `AmazonProvidedDNS` to ensure successful cluster creation and operation.
* To use a custom DNS server and domain name for your cluster, the OpenShift Container Platform installer must be able to use VPC DNS with default DHCP options so that it can resolve internal IPs and services. This means that you must create a custom DHCP option set to forward DNS lookups to your DNS server, and associate this option set with your VPC before you create the cluster.

.Procedure
* Confirm that your VPC is using VPC Resolver by running the following command:
+
[source,terminal]
----
$ aws ec2 describe-dhcp-options
----

[role="_additional-resources"]
[id="additional-resources_mos-checklist-custom-dns-domains"]
.Additional resources

* Deploying OpenShift Container Platform with a custom DNS resolver
