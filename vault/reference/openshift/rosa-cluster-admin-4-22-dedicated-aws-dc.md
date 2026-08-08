---
title: "Configuring AWS Direct Connect"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-dedicated-aws-dc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/dedicated-aws-dc
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Configuring AWS Direct Connect

[id="dedicated-aws-dc"]
= Configuring AWS Direct Connect

This process describes accepting an AWS Direct Connect virtual interface with
OpenShift Container Platform. For more information about AWS Direct Connect types and
configuration, see the
AWS Direct Connect components
documentation.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-dc.adoc

[id="dedicated-aws-dc-methods"]
= AWS Direct Connect methods

A Direct Connect connection requires a hosted Virtual Interface (VIF) connected
to a Direct Connect Gateway (DXGateway), which is in turn associated to a
Virtual Gateway (VGW) or a Transit Gateway in order to access a remote VPC in
the same or another account.

If you do not have an existing DXGateway, the typical process involves creating
the hosted VIF, with the DXGateway and VGW being created in the OpenShift Container Platform AWS Account.

If you have an existing DXGateway connected to one or more existing VGWs, the
process involves the OpenShift Container Platform AWS Account sending an Association Proposal
to the DXGateway owner. The DXGateway owner must ensure that the proposed CIDR
will not conflict with any other VGWs they have associated.

See the following AWS documentation for more details:

* Virtual Interfaces
* Direct Connect Gateways
* Associating a VGW across accounts

[IMPORTANT]
====
When connecting to an existing DXGateway, you are responsible for the
costs.
====

There are two configuration options available:

[horizontal]
Method 1:: Create the hosted VIF and then the DXGateway and VGW.
Method 2:: Request a connection via an existing Direct Connect Gateway that you own.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-dc.adoc

[id="dedicated-aws-dc-hvif"]
= Creating the hosted Virtual Interface

.Prerequisites

* Gather OpenShift Container Platform AWS Account ID.

[id="dedicated-aws-dc-hvif-type"]
== Determining the type of Direct Connect connection

View the Direct Connect Virtual Interface details to determine the type of
connection.

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard and select the correct region.
. Select *Direct Connect* from the *Services* menu.
. There will be one or more Virtual Interfaces waiting to be accepted, select one of them to view the *Summary*.
. View the Virtual Interface type: private or public.
. Record the *Amazon side ASN* value.

If the Direct Connect Virtual Interface type is Private, a Virtual Private
Gateway is created. If the Direct Connect Virtual Interface is Public, a Direct
Connect Gateway is created.

[id="dedicated-aws-dc-hvif-private"]
== Creating a Private Direct Connect

A Private Direct Connect is created if the Direct Connect Virtual Interface type is Private.

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard and select the correct region.
. From the AWS region, select *VPC* from the *Services* menu.
. From *Virtual private network (VPN)*, select *Virtual private gateways*.
. Click *Create virtual private gateway*.
. Give the Virtual Private Gateway a suitable name.
. Select *Custom ASN* in the *Enter custom ASN* field enter the *Amazon side ASN* value gathered previously.
. Click *Create virtual private gateway*.
. Click the newly created Virtual Private Gateway and choose *Attach to VPC* from the *Actions* tab.
. Select the *OpenShift Container Platform Cluster VPC* from the list, and click *Attach VPC*.

Note: Editing the kubelet config will cause the nodes for your machine pool to be recreated. This ma???

[id="dedicated-aws-dc-hvif-public"]
== Creating a Public Direct Connect

A Public Direct Connect is created if the Direct Connect Virtual Interface type
is Public.

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard and select the correct region.
. From the OpenShift Container Platform AWS Account region, select *Direct Connect* from the *Services* menu.
. Select *Direct Connect gateways* and *Create Direct Connect gateway*.
. Give the Direct Connect gateway a suitable name.
. In the *Amazon side ASN*, enter the Amazon side ASN value gathered previously.
. Click *Create the Direct Connect gateway*.

[id="dedicated-aws-dc-hvif-verifying"]
== Verifying the Virtual Interfaces

After the Direct Connect Virtual Interfaces have been accepted, wait a short
period and view the status of the Interfaces.

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard and select the correct region.
. From the OpenShift Container Platform AWS Account region, select *Direct Connect* from the *Services* menu.
. Select one of the Direct Connect Virtual Interfaces from the list.
. Check the Interface State has become *Available*
. Check the Interface BGP Status has become *Up*.
. Repeat this verification for any remaining Direct Connect Interfaces.

After the Direct Connect Virtual Interfaces are available, you can log in to the
OpenShift Container Platform AWS Account Dashboard and download the Direct Connect configuration file for
configuration on your side.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-dc.adoc

[id="dedicated-aws-dc-existing"]
= Connecting to an existing Direct Connect Gateway

.Prerequisites

* Confirm the CIDR range of the OpenShift Container Platform VPC will not conflict with any other VGWs you have associated.
* Gather the following information:
** The Direct Connect Gateway ID.
** The AWS Account ID associated with the virtual interface.
** The BGP ASN assigned for the DXGateway. Optional: the Amazon default ASN may also be used.

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard and select the correct region.
. From the OpenShift Container Platform AWS Account region, select *VPC* from the *Services* menu.
. From *Virtual private network (VPN)*, select *Virtual private gateways*.
. Select *Create virtual private gateway*.
. Give the virtual private gateway a suitable name in the *Details* field.
. Click *Custom ASN* and enter the *Amazon side ASN* value gathered previously or use the Amazon Provided ASN.
. Click *Create virtual private gateway*.
. From the OpenShift Container Platform AWS Account region, select *Direct Connect* from the *Services* menu.
. Click *virtual private gateways* and select the virtual private gateway.
. Click *View details*.
. Click the *Direct Connect gateway associations* tab.
. Click *Associate Direct Connect gateway*
. Under *Association account type*, for Account owner, click *Another account*.
. Under *Association settings*, for Direct Connect gateway ID, enter the ID of the Direct Connect gateway.
. For *Direct Connect gateway owner*, enter the ID of the AWS account that owns the Direct Connect gateway.
. Optional: Add prefixes to *Allowed prefixes*, separating them using commas or put them on separate lines.
. Click *Associate Direct Connect gateway*.
. After the Association Proposal has been sent, it will be waiting for your acceptance. The final steps you must perform are available in the
AWS Documentation.

[id="dedicated-aws-dc-tshooting"]
== Troubleshooting Direct Connect

Further troubleshooting can be found in the
Troubleshooting AWS Direct Connect
documentation.
