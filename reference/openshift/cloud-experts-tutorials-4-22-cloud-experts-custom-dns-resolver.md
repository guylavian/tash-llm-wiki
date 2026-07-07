---
title: "Tutorial: Deploying {product-title} with a Custom DNS Resolver"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-custom-dns-resolver
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-custom-dns-resolver
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Deploying {product-title} with a Custom DNS Resolver

[id="cloud-experts-custom-dns-resolver"]
= Tutorial: Deploying OpenShift Container Platform with a Custom DNS Resolver

[role="_abstract"]
A custom DHCP option set enables you to customize your VPC with your own DNS server, domain name, and more. OpenShift Container Platform clusters support using custom DHCP option sets. By default, OpenShift Container Platform clusters require setting the "domain name servers" option to `AmazonProvidedDNS` to ensure successful cluster creation and operation. Customers who want to use custom DNS servers for DNS resolution must do additional configuration to ensure successful OpenShift Container Platform cluster creation and operation.

In this tutorial, we will configure our DNS server to forward DNS lookups for specific DNS zones (further detailed below) to an Amazon Route 53 Inbound Resolver.

[NOTE]
====
This tutorial uses the open-source BIND DNS server (`named`) to demonstrate the configuration necessary to forward DNS lookups to an Amazon Route 53 Inbound Resolver located in the VPC you plan to deploy a OpenShift Container Platform cluster into. Refer to the documentation of your preferred DNS server for how to configure zone forwarding.
====

== Prerequisites

* ROSA CLI (`rosa`)
* AWS CLI (`aws`)
* A manually created AWS VPC
* A manually created AWS VPC
* A DHCP option set configured to point to a custom DNS server and set as the default for your VPC

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-custom-dns-resolver.adoc

[id="cloud-experts-custom-dns-resolver-environment-setup_{context}"]
= Setting up your environment

[role="_abstract"]
You can use environment variables to ensure consistency across the commands within this lab.

.Procedure
. In your terminal, configure the following environment variables:
+
[source,terminal]
----
$ export VPC_ID=<vpc_ID>
$ export REGION=<region>
$ export VPC_CIDR=<vpc_CIDR>
----
+
--
where:

`<vpc_ID>`:: Replace with the ID of the VPC you want to install your cluster into.
`<region>`:: Replace with the AWS region you want to install your cluster into.
`<vpc_CIDR>`:: Replace with the CIDR range of your VPC.
--
+
. Ensure all fields output correctly before moving to the next section:
+
[source,terminal]
----
$ echo "VPC ID: ${VPC_ID}, VPC CIDR Range: ${VPC_CIDR}, Region: ${REGION}"
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-custom-dns-resolver.adoc

[id="cloud-experts-custom-dns-resolver-create-inbound-resolver_{context}"]
= Create an Amazon Route 53 Inbound Resolver

[role="_abstract"]
Use the following procedure to deploy an Amazon Route 53 Inbound Resolver in the VPC we plan to deploy the cluster into.

[WARNING]
====
In this example, we deploy the Amazon Route 53 Inbound Resolver into the same VPC the cluster will use. If you want to deploy it into a separate VPC, you must manually associate the private hosted zone(s) detailed below *once cluster creation is started*. You cannot associate the zone before the cluster creation process begins. Failure to associate the private hosted zone during the cluster creation process will result in cluster creation failures.
====

.Procedure
. Create a security group and allow access to ports `53/tcp` and `53/udp` from the VPC:
+
[source,terminal]
----
$ SG_ID=$(aws ec2 create-security-group --group-name rosa-inbound-resolver --description "Security group for ROSA inbound resolver" --vpc-id ${VPC_ID} --region ${REGION} --output text)
$ aws ec2 authorize-security-group-ingress --group-id ${SG_ID} --protocol tcp --port 53 --cidr ${VPC_CIDR} --region ${REGION}
$ aws ec2 authorize-security-group-ingress --group-id ${SG_ID} --protocol udp --port 53 --cidr ${VPC_CIDR} --region ${REGION}
----
+
. Create an Amazon Route 53 Inbound Resolver in your VPC:
+
[source,terminal]
----
$ RESOLVER_ID=$(aws route53resolver create-resolver-endpoint \
  --name rosa-inbound-resolver \
  --creator-request-id rosa-$(date '+%Y-%m-%d') \
  --security-group-ids ${SG_ID} \
  --direction INBOUND \
  --ip-addresses $(aws ec2 describe-subnets --filter Name=vpc-id,Values=${VPC_ID} --region ${REGION} | jq -jr '.Subnets | map("SubnetId=\(.SubnetId) ") | .[]') \
  --region ${REGION} \
  --output text \
  --query 'ResolverEndpoint.Id')
----
+
[NOTE]
====
The above command attaches Amazon Route 53 Inbound Resolver endpoints to _all subnets_ in the provided VPC using dynamically allocated IP addresses. If you prefer to manually specify the subnets and/or IP addresses, run the following command instead:

[source,terminal]
----
$ RESOLVER_ID=$(aws route53resolver create-resolver-endpoint \
  --name rosa-inbound-resolver \
  --creator-request-id rosa-$(date '+%Y-%m-%d') \
  --security-group-ids ${SG_ID} \
  --direction INBOUND \
  --ip-addresses SubnetId=<subnet_ID>,Ip=<endpoint_IP> SubnetId=<subnet_ID>,Ip=<endpoint_IP> \//
  --region ${REGION} \
  --output text \
  --query 'ResolverEndpoint.Id')
----
Replace `<subnet_ID>` with the subnet IDs and `<endpoint_IP>` with the static IP addresses you want inbound resolver endpoints added to.
====
+
. Get the IP addresses of your inbound resolver endpoints to configure in your DNS server configuration:
+
[source,terminal]
----
$ aws route53resolver list-resolver-endpoint-ip-addresses \
  --resolver-endpoint-id ${RESOLVER_ID} \
  --region=${REGION} \
  --query 'IpAddresses[*].Ip'
----
+
.Example output
[source,text]
----
[
    "10.0.45.253",
    "10.0.23.131",
    "10.0.148.159"
]
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-custom-dns-resolver.adoc

[id="cloud-experts-custom-dns-resolver-configure-dns-server-hcp_{context}"]
= Configure your DNS server

[role="_abstract"]
OpenShift Container Platform clusters require you to configure DNS server to forward the necessary private hosted zones to your Amazon Route 53 Inbound Resolver:

* `<cluster-name>.hypershift.local`
* `rosa.<domain-prefix>.<unique-ID>.p3.openshiftapps.com`

These Amazon Route 53 private hosted zones are created during cluster creation. The `cluster-name` and `domain-prefix` are customer-specified values, but the `unique-ID` is randomly generated during cluster creation and cannot be preselected. As such, you must wait for the cluster creation process to begin before configuring forwarding for the `p3.openshiftapps.com` private hosted zone.

.Procedure
. Before the cluster is created, configure your DNS server to forward all DNS requests for `<cluster-name>.hypershift.local` to your Amazon Route 53 Inbound Resolver endpoints. For BIND DNS servers, edit your `/etc/named.conf` file in your favorite text editor and add a new zone using the below example:
+
**For example**
+
[source,terminal]
----
zone "<cluster-name>.hypershift.local" {
  type forward;
  forward only;
  forwarders {
    10.0.45.253;
    10.0.23.131;
    10.0.148.159;
  };
};
----
+
--
* Replace `<cluster-name>` with your OpenShift Container Platform cluster name.
* Replace with the IP addresses of your inbound resolver endpoints collected above, ensuring that following each IP address there is a `;`.
--
+
. Create your cluster.
+
. Once your cluster has begun the creation process, locate the newly created private hosted zone:
+
[source,terminal]
----
$ aws route53 list-hosted-zones-by-vpc \
  --vpc-id ${VPC_ID} \
  --vpc-region ${REGION} \
  --query 'HostedZoneSummaries[*].Name' \
  --output table
----
+
**Example output**
+
[source,text]
----
--------------------------------------------------
|             ListHostedZonesByVPC               |
+------------------------------------------------+
|  rosa.domain-prefix.lkmb.p3.openshiftapps.com. |
|  cluster-name.hypershift.local.                |
+------------------------------------------------+
----
+
[NOTE]
====
It may take a few minutes for the cluster creation process to create the private hosted zones in Route 53. If you do not see an `p3.openshiftapps.com` domain, wait a few minutes and run the command again.
====
+
. Once you know the unique ID of the cluster domain, configure your DNS server to forward all DNS requests for `rosa.<domain-prefix>.<unique-ID>.p3.openshiftapps.com` to your Amazon Route 53 Inbound Resolver endpoints. For BIND DNS servers, edit your `/etc/named.conf` file in your favorite text editor and add a new zone using the below example:
+
**For example**
+
[source,terminal]
----
zone "rosa.<domain-prefix>.<unique-ID>.p3.openshiftapps.com" {
  type forward;
  forward only;
  forwarders {
    10.0.45.253;
    10.0.23.131;
    10.0.148.159;
  };
};
----
--
* Replace `<domain-prefix>` with your cluster domain prefix and `<unique-ID>` with your unique ID collected above.
* Replace with the IP addresses of your inbound resolver endpoints collected above, ensuring that following each IP address there is a `;`.
--
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-custom-dns-resolver.adoc

[id="cloud-experts-custom-dns-resolver-configure-dns-server-classic_{context}"]
= Configure your DNS server

[role="_abstract"]
OpenShift Container Platform clusters require you to configure DNS server to forward the necessary private hosted zones to your Amazon Route 53 Inbound Resolver:

* `<domain-prefix>.<unique-ID>.p1.openshiftapps.com`

This Amazon Route 53 private hosted zones is created during cluster creation. The `domain-prefix` is a customer-specified value, but the `unique-ID` is randomly generated during cluster creation and cannot be preselected. As such, you must wait for the cluster creation process to begin before configuring forwarding for the `p1.openshiftapps.com` private hosted zone.

.Procedure
. Create your cluster.
+
. Once your cluster has begun the creation process, locate the newly created private hosted zone:
+
[source,terminal]
----
$ aws route53 list-hosted-zones-by-vpc \
  --vpc-id ${VPC_ID} \
  --vpc-region ${REGION} \
  --query 'HostedZoneSummaries[*].Name' \
  --output table
----
+
.Example output
[source,text]
----
----------------------------------------------
|           ListHostedZonesByVPC             |
+--------------------------------------------+
|  domain-prefix.agls.p3.openshiftapps.com.  |
+--------------------------------------------+
----
+
[NOTE]
====
It may take a few minutes for the cluster creation process to create the private hosted zones in Route 53. If you do not see an `p1.openshiftapps.com` domain, wait a few minutes and run the command again.
====
+
. Once you know the unique ID of the cluster domain, configure your DNS server to forward all DNS requests for `<domain-prefix>.<unique-ID>.p1.openshiftapps.com` to your Amazon Route 53 Inbound Resolver endpoints. For BIND DNS servers, edit your `/etc/named.conf` file in your favorite text editor and add a new zone using the below example:
+
.Example
[source,terminal]
----
zone "<domain-prefix>.<unique-ID>.p1.openshiftapps.com" {
  type forward;
  forward only;
  forwarders {
    10.0.45.253;
    10.0.23.131;
    10.0.148.159;
  };
};
----
+
--
* Replace `<domain-prefix>` with your cluster domain prefix and `<unique-ID>` with your unique ID collected above.
* Replace with the IP addresses of your inbound resolver endpoints collected above, ensuring that following each IP address there is a `;`.
--

[role="_additional-resources"]
== Additional resources
* Create your cluster
* Create your cluster
