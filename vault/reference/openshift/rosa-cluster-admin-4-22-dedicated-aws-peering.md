---
title: "Configuring AWS VPC peering"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-dedicated-aws-peering
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/dedicated-aws-peering
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Configuring AWS VPC peering

[id="dedicated-aws-peering"]
= Configuring AWS VPC peering

This sample process configures an Amazon Web Services (AWS) VPC containing an
OpenShift Container Platform cluster to peer with another AWS VPC network. For more
information about creating an AWS VPC Peering connection or for other possible
configurations, see the
AWS VPC Peering
guide.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc

[id="dedicated-aws-vpc-peering-terms"]
= VPC peering terms

When setting up a VPC peering connection between two VPCs on two separate AWS
accounts, the following terms are used:

[horizontal]
OpenShift Container Platform AWS Account:: The AWS account that contains the OpenShift Container Platform cluster.
OpenShift Container Platform Cluster VPC:: The VPC that contains the OpenShift Container Platform cluster.
Customer AWS Account:: Your non-OpenShift Container Platform AWS Account that you would like to peer with.
Customer VPC:: The VPC in your AWS Account that you would like to peer with.
Customer VPC Region:: The region where the customer's VPC resides.

[NOTE]
====
As of July 2018, AWS supports inter-region VPC peering between all commercial regions excluding China.
====
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc

[id="dedicated-aws-vpc-initiating-peering"]
= Initiating the VPC peer request

You can send a VPC peering connection request from the OpenShift Container Platform AWS Account to the
Customer AWS Account.

.Prerequisites

* Gather the following information about the Customer VPC required to initiate the
peering request:
** Customer AWS account number
** Customer VPC ID
** Customer VPC Region
** Customer VPC CIDR
* Check the CIDR block used by the OpenShift Container Platform Cluster VPC. If it overlaps or
matches the CIDR block for the Customer VPC, then peering between these two VPCs
is not possible; see the Amazon VPC
Unsupported VPC Peering Configurations
documentation for details. If the CIDR blocks do not overlap, you can continue
with the procedure.

.Procedure

. Log in to the Web Console for the OpenShift Container Platform AWS Account and navigate to the
*VPC Dashboard* in the region where the cluster is being hosted.
. Go to the *Peering Connections* page and click the *Create Peering Connection*
button.
. Verify the details of the account you are logged in to and the details of the
account and VPC you are connecting to:
.. *Peering connection name tag*: Set a descriptive name for the VPC Peering Connection.
.. *VPC (Requester)*: Select the OpenShift Container Platform Cluster VPC ID from the list.
.. *Account*: Select *Another account* and provide the Customer AWS Account number
*(without dashes).
.. *Region*: If the Customer VPC Region differs from the current region, select
*Another Region* and select the customer VPC Region from the list.
.. *VPC (Accepter)*: Set the Customer VPC ID.
. Click *Create Peering Connection*.
. Confirm that the request enters a *Pending* state. If it enters a *Failed*
state, confirm the details and repeat the process.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc

[id="dedicated-aws-vpc-accepting-peering"]
= Accepting the VPC peer request

After you create the VPC peering connection, you must accept the request in the
Customer AWS Account.

.Prerequisites

* Initiate the VPC peer request.

.Procedure

. Log in to the AWS Web Console.
. Navigate to *VPC Service*.
. Go to *Peering Connections*.
. Click on *Pending peering connection*.
. Confirm the AWS Account and VPC ID that the request originated from. This should
be from the OpenShift Container Platform AWS Account and OpenShift Container Platform Cluster VPC.
. Click *Accept Request*.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc

[id="dedicated-aws-vpc-configuring-routing-tables"]
= Configuring the routing tables

After you accept the VPC peering request, both VPCs must configure their routes
to communicate across the peering connection.

.Prerequisites

* Initiate and accept the VPC peer request.

.Procedure

. Log in to the AWS Web Console for the OpenShift Container Platform AWS Account.
. Navigate to the *VPC Service*, then *Route tables*.
. Select the Route Table for the OpenShift Container Platform Cluster VPC.
+
[NOTE]
====
On some clusters, there may be more than one route table for a particular VPC.
Select the private one that has a number of explicitly associated subnets.
====

. Select the *Routes* tab, then *Edit*.
. Enter the Customer VPC CIDR block in the *Destination* text box.
. Enter the Peering Connection ID in the *Target* text box.
. Click *Save*.

. You must complete the same process with the other VPC's CIDR block:
.. Log into the Customer AWS Web Console → *VPC Service* → *Route Tables*.
.. Select the Route Table for your VPC.
.. Select the *Routes* tab, then *Edit*.
.. Enter the OpenShift Container Platform Cluster VPC CIDR block in the *Destination* text box.
.. Enter the Peering Connection ID in the *Target* text box.
.. Click *Save changes*.

The VPC peering connection is now complete. Follow the verification procedure to
ensure connectivity across the peering connection is working.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc

[id="dedicated-aws-vpc-verifying-troubleshooting"]
= Verifying and troubleshooting VPC peering

After you set up a VPC peering connection, it is best to confirm it has been
configured and is working correctly.

.Prerequisites

* Initiate and accept the VPC peer request.
* Configure the routing tables.

.Procedure

* In the AWS console, look at the route table for the cluster VPC that is peered.
Ensure that the steps for configuring the routing tables were followed and that
there is a route table entry pointing the VPC CIDR range destination to the
peering connection target.
+
If the routes look correct on both the OpenShift Container Platform Cluster VPC route table
and Customer VPC route table, then the connection should be tested using the
`netcat` method below. If the test calls are successful, then VPC peering is
working correctly.

* To test network connectivity to an endpoint device, `nc` (or `netcat`) is a
helpful troubleshooting tool. It is included in the default image and provides
quick and clear output if a connection can be established:

.. Create a temporary pod using the `busybox` image, which cleans up after itself:
+
[source,terminal]
----
$ oc run netcat-test \
    --image=busybox -i -t \
    --restart=Never --rm \
    -- /bin/sh
----

.. Check the connection using `nc`.
+
--
* Example successful connection results:
+
[source,terminal]
----
/ nc -zvv 192.168.1.1 8080
10.181.3.180 (10.181.3.180:8080) open
sent 0, rcvd 0
----

* Example failed connection results:
+
[source,terminal]
----
/ nc -zvv 192.168.1.2 8080
nc: 10.181.3.180 (10.181.3.180:8081): Connection refused
sent 0, rcvd 0
----
--

.. Exit the container, which automatically deletes the Pod:
+
[source,terminal]
----
/ exit
----
