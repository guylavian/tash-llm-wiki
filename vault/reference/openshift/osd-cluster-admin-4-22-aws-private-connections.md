---
title: "Configure private connections for AWS"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-aws-private-connections
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/aws-private-connections
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# Configure private connections for AWS

[id="aws-private-connections_{context}"]
= Configure private connections for AWS

[role="_abstract"]
Configure AWS infrastructure access and establish private connections to your OpenShift Container Platform cluster using Virtual Private Cloud (VPC) peering, Virtual Private Network (VPN), or AWS Direct Connect. This enables secure, dedicated network communication between your on-premises infrastructure and AWS resources.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/aws-private-connections.adoc

[id="enable-aws-access_{context}"]
= AWS cloud infrastructure access

[role="_abstract"]
{AWS} infrastructure access enables AWS Identity and Access Management (IAM) users to have federated access to the AWS Management Console for your OpenShift Container Platform cluster. This allows you to configure VPC peering, VPN, and Direct Connect from the AWS console.

[NOTE]
====
AWS cloud infrastructure access does not apply to the Customer Cloud Subscription (CCS) infrastructure type that is chosen when you create a cluster because CCS clusters are deployed onto your account.
====

AWS access can be granted for customer AWS users, and private cluster access can be implemented to suit the needs of your OpenShift Container Platform environment.

To get started with configuring AWS infrastructure access for your OpenShift Container Platform cluster, create an AWS user and account and provide that user with access to the OpenShift Container Platform AWS account.

After you have access to the OpenShift Container Platform AWS account, use one or more of the following methods to establish a private connection to your cluster:

* *Configure AWS Virtual Private Cloud (VPC) peering*: Enable VPC peering to route network traffic between two private IP addresses.

* *Configure AWS Virtual Private Network (VPN)*: Establish a VPN to securely connect your private network to your Amazon VPC.

* *Configure AWS Direct Connect*: Establish a dedicated network connection between your private network and an AWS Direct Connect location.
// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/aws-private-connections.adoc

[id="config-aws-access_{context}"]
= Configure AWS infrastructure access

[role="_abstract"]
Configure AWS infrastructure access to enable AWS Identity and Access Management (IAM) users to have federated access to the AWS Management Console for your OpenShift Container Platform cluster.

.Prerequisites

* An AWS account with IAM permissions.

.Procedure

. Log in to your AWS account. If necessary, you can create a new AWS account by following the AWS documentation.

. Create an IAM user with `STS:AllowAssumeRole` permissions within the AWS account.

.. Open the IAM dashboard of the AWS Management Console.
.. In the *Policies* section, click *Create Policy*.
.. Select the *JSON* tab and replace the existing text with the following:
+
[source,json]
----
{
  "Version": "2012-10-17",
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "*"
      }
  ]
}
----

.. Click *Next:Tags*.
.. Optional: Add tags. Click *Next:Review*
.. Provide an appropriate name and description, then click *Create Policy*.
.. In the *Users* section, click *Add user*.
.. Provide an appropriate user name.
.. Select *AWS Management Console access* as the AWS access type.
.. Adjust the password requirements as necessary for your organization, then click *Next:Permissions*.
.. Click the *Attach existing policies directly* option. Search for and check the policy created in previous steps.
+
[NOTE]
====
It is not recommended to set a permissions boundary.
====

.. Click *Next: Tags*, then click *Next: Review*. Confirm the configuration is correct.
.. Click *Create user*, a success page appears.
.. Gather the IAM user’s Amazon Resource Name (ARN). The ARN has the following format: `arn:aws:iam::000111222333:user/username`. Click *Close*.

. Open {cluster-manager-url} in your browser and select the cluster you want to allow AWS infrastructure access.

. Select the *Access control* tab, and scroll to the *AWS Infrastructure Access* section.

. Paste the *AWS IAM ARN* and select *Network Management* or *Read-only* permissions, then click *Grant role*.

. Copy the *AWS OSD console URL* to your clipboard.

. Sign in to your AWS account with your Account ID or alias, IAM user name, and password.

. In a new browser tab, paste the AWS OSD Console URL that routes to the AWS Switch Role page.

. Your account number and role are filled in already. Choose a display name if necessary, then click *Switch Role*.
// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/aws-private-connections.adoc

[id="aws-vpc_{context}"]
= Configure AWS Virtual Private Cloud peering

[role="_abstract"]
Configure an {AWS} Virtual Private Cloud (VPC) peering connection to route traffic between two VPCs using private IPv4 or IPv6 addresses.

[IMPORTANT]
====
Before you attempt to uninstall a cluster, you must remove any VPC peering connections from the cluster's VPC. Failure to do so might result in a cluster not completing the uninstall process.
====

[NOTE]
====
AWS supports inter-region VPC peering between all commercial regions excluding China. For more information, see AWS VPC FAQs.
====

.Prerequisites

* Gather the following information about the Customer VPC that is required to initiate the peering request:
** Customer AWS account number
** Customer VPC ID
** Customer VPC Region
** Customer VPC Classless Inter-Domain Routing (CIDR)
* The CIDR block of the OpenShift Container Platform Cluster VPC does not overlap or match the Customer VPC CIDR block. See the Amazon VPC Unsupported VPC peering configurations documentation for details on invalid configurations.

.Procedure

. Initiate the VPC peering request.

. Accept the VPC peering request.

. Update your Route tables for the VPC peering connection.

[role="_additional-resources"]
.Additional resources

* AWS VPC guide
// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/aws-private-connections.adoc

[id="aws-vpn_{context}"]
= Configure an AWS Virtual Private Network

[role="_abstract"]
Configure an AWS Site-to-Site Virtual Private Network (VPN) connection to enable secure communication between your OpenShift Container Platform cluster Virtual Private Cloud (VPC) and your remote on-site network.

[NOTE]
====
AWS VPN does not currently provide a managed option to apply Network Address Translation (NAT) to VPN traffic. See the AWS Knowledge Center for more details.

Routing all traffic, for example `0.0.0.0/0`, through a private connection is not supported. This requires deleting the internet gateway, which disables SRE management traffic.
====

.Prerequisites

* Hardware VPN gateway device model and software version, for example Cisco Adaptive Security Appliance (ASA) running version 8.3. See the AWS documentation to confirm whether your gateway device is supported by AWS.
* Public, static IP address for the VPN gateway device.
* Border Gateway Protocol (BGP) or static routing: if BGP, the Autonomous System Number (ASN) is available. If static routing, at least one static route is configured.
* Optional: Internet Protocol (IP) address and port/protocol of a reachable service to test the VPN connection.

.Procedure

. Create a customer gateway to configure the VPN connection.

. If you do not already have a Virtual Private Gateway attached to the intended VPC, create and attach a Virtual Private Gateway.

. Configure routing and enable VPN route propagation.

. Update your security group.

. Establish the Site-to-Site VPN connection.
+
[NOTE]
====
Note the VPC subnet information, which you must add to your configuration as the remote network.
====

[role="_additional-resources"]
.Additional resources

* AWS VPN guide
// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/aws-private-connections.adoc

[id="aws-direct-connect_{context}"]
= Configure AWS Direct Connect

[role="_abstract"]
Configure AWS Direct Connect to establish a dedicated network connection between your remote network and your OpenShift Container Platform cluster Virtual Private Cloud (VPC).

{AWS} Direct Connect requires a hosted Virtual Interface (VIF) connected to a Direct Connect Gateway (DXGateway), which is in turn associated to a Virtual Gateway (VGW) or a Transit Gateway. This allows you to access a remote VPC in the same or another account.

.Prerequisites

* The Classless Inter-Domain Routing (CIDR) range of the OpenShift Container Platform VPC does not conflict with any other associated VGWs.
* Gather the following information:
** The Direct Connect Gateway ID.
** The AWS Account ID associated with the virtual interface.
** The Border Gateway Protocol (BGP) Autonomous System Number (ASN) assigned for the DXGateway. Optional: the Amazon default ASN may also be used.

.Procedure

. Create a VIF or view your existing VIFs to determine the type of direct connection you need to create.

. Create your gateway.
.. If the Direct Connect VIF type is *Private*, create a virtual private gateway.
.. If the Direct Connect VIF is *Public*, create a Direct Connect gateway.

. If you have an existing gateway you want to use, create an association proposal and send the proposal to the DXGateway owner for approval.
+
[WARNING]
====
When connecting to an existing DXGateway, you are responsible for the costs.
====

[role="_additional-resources"]
== Additional resources

* Amazon Virtual Private Cloud
* Customer Portal Organization Administrators
* AWS account prerequisites
* AWS Direct Connect guide
