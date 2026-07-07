---
title: "Configuring AWS VPN"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-dedicated-aws-vpn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/dedicated-aws-vpn
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Configuring AWS VPN

[id="dedicated-aws-vpn"]
= Configuring AWS VPN

This sample process configures an Amazon Web Services (AWS) OpenShift Container Platform
cluster to use a customer's on-site hardware VPN device.

[NOTE]
====
AWS VPN does not currently provide a managed option to apply NAT to VPN traffic.
See the
AWS Knowledge Center
for more details.
====

[NOTE]
====
Routing all traffic, for example `0.0.0.0/0`, through a private connection is not supported. This requires deleting the internet gateway, which disables SRE management traffic.
====

For more information about connecting an AWS VPC to remote networks using a
hardware VPN device, see the Amazon VPC
VPN Connections
documentation.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-vpn.adoc

[id="dedicated-aws-vpn-creating"]
= Creating a VPN connection

You can configure an Amazon Web Services (AWS) OpenShift Container Platform cluster to use a customer's on-site hardware VPN device using the following procedures.

.Prerequisites

* Hardware VPN gateway device model and software version, for example Cisco ASA
running version 8.3. See the Amazon VPC
Network Administrator Guide
to confirm whether your gateway device is supported by AWS.
* Public, static IP address for the VPN gateway device.
* BGP or static routing: if BGP, the ASN is required. If static routing, you must
configure at least one static route.
* *Optional*: IP and Port/Protocol of a reachable service to test the VPN connection.

[id="dedicated-aws-vpn-creating-configuring"]
== Configuring the VPN connection

.Procedure

. Log in to the OpenShift Container Platform AWS Account Dashboard, and navigate to the VPC Dashboard.
. Under *Virtual private cloud* click on *Your VPCs* and identify the name and VPC ID for the VPC containing the OpenShift Container Platform cluster.
. Under *Virtual private network (VPN)* click *Customer gateways*.
. Click *Create customer gateway* and give it a meaningful name.
. Enter the ASN of your customer gateway device in the *BGP ASN* field.
. Enter the IP address for your customer gateway devices’s external interface in the *IP address* field.
. Click *Create customer gateway*.
. If you do not already have a Virtual Private Gateway attached to the intended VPC:
.. From the VPC Dashboard, click on *Virtual Private Gateways*.
.. Click *Create virtual private gateway*, give it a meaningful name.
.. Click *Create virtual private gateway*, leaving the *Amazon default ASN*.
.. Select the newly created gateway.
.. Select *Actions* from the list and click *Attach to VPC*.
.. Select the newly created gateway under Available VPC's and click *Attach to VPC* to attach it to the cluster VPC you identified earlier.

[id="dedicated-aws-vpn-creating-establishing"]
== Establishing the VPN Connection

.Procedure

. From the VPC dashboard, under Virtual private network (VPN) click on *Site-to-Site VPN connections*.
. Click *Create VPN connection*.
.. Give it a meaningful name tag.
.. Select the Virtual private gateway created previously.
.. For Customer gateway, select *Existing*.
.. Select the Customer gateway id by name.
.. If the VPN will use BGP, select *Dynamic*, otherwise select *Static* and enter the
Static IP CIDRs. If there are multiple CIDRs, add each CIDR as *Another Rule*.
.. Click *Create VPN connection*.
.. Under *State* wait for the VPN status to change from *Pending* to *Available*, approximately 5 to 10 minutes.
. Select the VPN you just created and click *Download configuration*.
.. From the list, select the vendor, platform, and version of the customer
gateway device, then click *Download*.
.. The *Generic* vendor configuration is also available for retrieving information
in a plain text format.

[NOTE]
====
After the VPN connection has been established, be sure to set up Route
Propagation or the VPN may not function as expected.
====

[NOTE]
====
Note the VPC subnet information, which you must add to your configuration as the
remote network.
====

[id="dedicated-aws-vpn-creating-propagation"]
== Enabling VPN route propagation

After you have set up the VPN connection, you must ensure that route propagation
is enabled so that the necessary routes are added to the VPC's route table.

.Procedure

. From the VPC Dashboard, under Virtual private cloud, click on *Route tables*.
. Select the private Route table associated with the VPC that contains your
OpenShift Container Platform cluster.
+
[NOTE]
====
On some clusters, there may be more than one route table for a particular VPC.
Select the private one that has a number of explicitly associated subnets.
====
. Click on the *Route Propagation* tab.
. In the table that appears, you should see the Virtual Private Gateway you
created previously. Check the value in the *Propagate* column.
.. If *Propagation* is set to *No*, click *Edit route propagation*, check the *Enable* checkbox in Propagation and click *Save*.

After you configure your VPN tunnel and AWS detects it as *Up*, your static or
BGP routes are automatically added to the route table.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-vpn.adoc

[id="dedicated-aws-vpn-verifying"]
= Verifying the VPN connection

After you have set up your side of the VPN tunnel, you can verify that the
tunnel is up in the AWS console and that connectivity across the tunnel is
working.

.Prerequisites

* Created a VPN connection.

.Procedure

. *Verify the tunnel is up in AWS*.

.. From the VPC Dashboard, under *Virtual private network (VPN)*, click on *Site-to-Site VPN connections*.
.. Select the VPN connection you created previously and click the *Tunnel details* tab.
.. You should see that at least one of the VPN tunnels is in an *Up* status.

. *Verify the connection*.
+
To test network connectivity to an endpoint device, `nc` (or `netcat`) is a
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
// Module included in the following assemblies:
//
// * rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-vpn.adoc

[id="dedicated-aws-vpn-troubleshooting"]
= Troubleshooting the VPN connection

[discrete]
[id="dedicated-aws-vpn-tunnel-down"]
== Tunnel does not connect

If the tunnel connection is still *Down*, there are several things you can verify:

* The AWS tunnel will not initiate a VPN connection. The connection attempt must be initiated from the Customer Gateway.
* Ensure that your source traffic is coming from the same IP as the configured customer gateway. AWS will silently drop all traffic to the gateway whose source IP address does not match.
* Ensure that your configuration matches values supported by AWS. This includes IKE versions, DH groups, IKE lifetime, and more.
* Recheck the route table for the VPC. Ensure that propagation is enabled and that there are entries in the route table that have the virtual private gateway you created earlier as a target.
* Confirm that you do not have any firewall rules that could be causing an interruption.
* Check if you are using a policy-based VPN as this can cause complications depending on how it is configured.
* Further troubleshooting steps can be found at the AWS Knowledge Center.

[discrete]
[id="dedicated-aws-vpn-tunnel-stay-connected"]
== Tunnel does not stay connected

If the tunnel connection has trouble staying *Up* consistently, know that all
AWS tunnel connections must be initiated from your gateway. AWS tunnels
do
not initiate tunneling.

Red Hat recommends setting up an SLA Monitor (Cisco ASA) or some device on your
side of the tunnel that constantly sends "interesting" traffic, for example
`ping`, `nc`, or `telnet`, at any IP address configured within the VPC CIDR
range. It does not matter whether the connection is successful, just that the
traffic is being directed at the tunnel.

[discrete]
[id="dedicated-aws-vpn-secondary-tunnel-down"]
== Secondary tunnel in Down state

When a VPN tunnel is created, AWS creates an additional failover tunnel.
Depending upon the gateway device, sometimes the secondary tunnel will be seen
as in the *Down* state.

The AWS Notification is as follows:

----
You have new non-redundant VPN connections

One or more of your vpn connections are not using both tunnels. This mode of
operation is not highly available and we strongly recommend you configure your
second tunnel. View your non-redundant VPN connections.
----
