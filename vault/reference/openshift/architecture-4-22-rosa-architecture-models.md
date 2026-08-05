---
title: "Architecture models"
type: reference
domain: openshift
slug: architecture-4-22-rosa-architecture-models
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/rosa-architecture-models
version: 4.22
family: architecture
documentKind: "Documentation"
---

# Architecture models

[id="rosa-architecture-models"]
= Architecture models

OpenShift Container Platform has a classic architecture cluster topology meaning the control plane and the worker nodes are deployed in the customer's AWS account.

// Module included in the following assemblies:
//
// * rosa-architecture-models.adoc

[id="rosa-hcp-classic-comparison_{context}"]
= Comparing {hcp-title-first} and {rosa-classic-title}

.{hcp-title-first} and {rosa-classic-title} architectures comparison table

[cols="3a,8a,8a",options="header"]
|===
| {nbsp} +
| *Hosted Control Plane (HCP)*
| *Classic*

| *Control plane hosting*
| Control plane components, such as the API server etcd database, are hosted in a Red{nbsp}Hat-owned AWS account.
| Control plane components, such as the API server etcd database, are hosted in a customer-owned AWS account.

| *Virtual Private Cloud (VPC)*
| Worker nodes communicate with the control plane over AWS PrivateLink.
| Worker nodes and control plane nodes are deployed in the customer's VPC.

| *Multi-zone deployment*
| The control plane is always deployed across multiple availability zones (AZs).
| The control plane can be deployed within a single AZ or across multiple AZs.

| *Machine pools*
| Each machine pool is deployed in a single AZ (private subnet).
| Machine pools can be deployed in single AZ or across multiple AZs.

| *Infrastructure nodes*
| Does not use any dedicated infrastructure nodes to host platform components, such as ingress and image registry.
| Uses 2 (single-AZ) or 3 (multi-AZ) dedicated infrastructure nodes to host platform components.

| *OpenShift capabilities*
| Platform monitoring, image registry, and the ingress controller are deployed in the worker nodes.
| Platform monitoring, image registry, and the ingress controller are deployed in the dedicated infrastructure nodes.

| *Cluster upgrades*
| The control plane and each machine pool can be upgraded separately.
| The entire cluster must be upgraded at the same time.

| *Minimum EC2 footprint*
| 2 EC2 instances are needed to create a cluster.
| 7 (single-AZ) or 9 (multi-AZ) EC2 instances are needed to create a cluster.
|===

.Additional resources

* Regions and availability zones

* Security and regulation compliance

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_architecture_sub/rosa-architecture-models.adoc

[id="rosa-hcp-architecture_{context}"]
= OpenShift Container Platform architecture

[role="_abstract"]
OpenShift Container Platform hosts a highly-available, single-tenant OpenShift control plane. The hosted control plane is deployed across 3 availability zones with 2 API server instances and 3 etcd instances.

You can create a OpenShift Container Platform cluster with or without an internet-facing API server, with the latter considered a “private” cluster and the former considered a “public” cluster. Private API servers are only accessible from your VPC subnets. You access the hosted control plane through an AWS PrivateLink endpoint regardless of API privacy.

The worker nodes are deployed in your AWS account and run on your VPC private subnets. You can add additional private subnets from one or more availability zones to ensure high availability. Worker nodes are shared by OpenShift components and applications. OpenShift components such as the ingress controller, image registry, and monitoring are deployed on the worker nodes hosted on your VPC.

.OpenShift Container Platform architecture
image::544_OpenShift_ROSA-HCP_architecture-model.png[OpenShift Container Platform architecture]

[id="rosa-hcp-network-architecture_{context}"]
== OpenShift Container Platform architecture on public and private networks
With OpenShift Container Platform, you can create your clusters on public or private networks. The following images depict the architecture of both public and private networks.

.OpenShift Container Platform deployed on a public network
image::544_OpenShift_ROSA-HCP-and-ROSA-Classic-public.png[OpenShift Container Platform deployed on a public network]

.OpenShift Container Platform deployed on a private network
image::544_OpenShift_ROSA-HCP-and-ROSA-Classic-private.png[OpenShift Container Platform deployed on a private network]

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_architecture_sub/rosa-architecture-models.adoc

[id="rosa-classic-architecture_{context}"]
= OpenShift Container Platform

In OpenShift Container Platform, both the control plane and the worker nodes are deployed in your VPC subnets.

[id="rosa-classic-architecture-networks_{context}"]
== OpenShift Container Platform on public and private networks

With OpenShift Container Platform, you can create clusters that are accessible over public or private networks.

You can customize access patterns for your API server endpoint and Red{nbsp}Hat SRE management in the following ways:

* Public - API server endpoint and application routes are internet-facing.

* Private - API server endpoint and application routes are private. Private OpenShift Container Platform clusters use some public subnets, but no control plane or worker nodes are deployed in public subnets.

* Private with AWS PrivateLink - API server endpoint and application routes are private. Public subnets or NAT gateways are not required in your VPC for egress. OpenShift Container Platform SRE management uses AWS PrivateLink.

The following image depicts the architecture of a OpenShift Container Platform cluster deployed on both public and private networks.

.OpenShift Container Platform deployed on public and private networks
image::156_OpenShift_ROSA_Arch_0621_private_public_classic.png[OpenShift Container Platform on public and private networks]

OpenShift Container Platform clusters include infrastructure nodes where OpenShift components such as the ingress controller, image registry, and monitoring are deployed. The infrastructure nodes and the OpenShift components deployed on them are managed by OpenShift Container Platform SREs.

The following types of clusters are available with OpenShift Container Platform:

* Single zone cluster - The control plane and worker nodes are hosted on a single availability zone.

* Multi-zone cluster - The control plane is hosted on three availability zones with an option to run worker nodes on one or three availability zones.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_architecture_sub/rosa-architecture-models.adoc
[id="osd-aws-privatelink-architecture_{context}"]
= AWS PrivateLink architecture

The Red{nbsp}Hat managed infrastructure that creates AWS PrivateLink clusters is hosted on private subnets. The connection between Red{nbsp}Hat and the customer-provided infrastructure is created through AWS PrivateLink VPC endpoints.

[NOTE]
====
AWS PrivateLink is supported on existing VPCs only.
====

The following diagram shows network connectivity of a PrivateLink cluster.

.Multi-AZ AWS PrivateLink cluster deployed on private subnets

image::156_OpenShift_ROSA_Arch_1221_privatelink.png[Multi-AZ AWS PrivateLink cluster deployed on private subnets]

[id="osd-aws-reference-architecture_{context}"]
== AWS reference architectures

AWS provides multiple reference architectures that can be useful to customers when planning how to set up a configuration that uses AWS PrivateLink. Here are three examples:

[NOTE]
====
A *public subnet* connects directly to the internet through an internet gateway. A *private subnet* connects to the internet through a network address translation (NAT) gateway.
====

* VPC with a private subnet and AWS Site-to-Site VPN access.
+
This configuration enables you to extend your network into the cloud without exposing your network to the internet.
+
To enable communication with your network over an Internet Protocol Security (IPsec) VPN tunnel, this configuration contains a virtual private cloud (VPC) with a single private subnet and a virtual private gateway. Communication over the internet does not use an internet gateway.
+
For more information, see VPC with a private subnet only and AWS Site-to-Site VPN access in the AWS documentation.

* VPC with public and private subnets (NAT)
+
This configuration enables you to isolate your network so that the public subnet is reachable from the internet but the private subnet is not.
+
Only the public subnet can send outbound traffic directly to the internet. The private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet. This allows database servers to connect to the internet for software updates using the NAT gateway, but does not allow connections to be made directly from the internet to the database servers.
+
For more information, see VPC with public and private subnets (NAT) in the AWS documentation.

* VPC with public and private subnets and AWS Site-to-Site VPN access
+
This configuration enables you to extend your network into the cloud and to directly access the internet from your VPC.
+
You can run a multi-tiered application with a scalable web front end in a public subnet, and house your data in a private subnet that is connected to your network by an IPsec AWS Site-to-Site VPN connection.
+
For more information, see https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario3.html[VPC with public and private subnets and AWS Site-to-Site VPN access] in the AWS documentation.
// Module included in the following assemblies:
//
// * architecture/rosa-architecture-models.adoc
[id="rosa-architecture-local-zones_{context}"]
= OpenShift Container Platform with Local Zones

OpenShift Container Platform supports the use of AWS Local Zones, which are metropolis-centralized availability zones where customers can place latency-sensitive application workloads within a VPC. Local Zones are extensions of AWS Regions and are not enabled by default. When Local Zones are enabled and configured, the traffic is extended into the Local Zones for greater flexibility and lower latency. For more information, see "Configuring machine pools in Local Zones".

The following diagram displays a OpenShift Container Platform cluster without traffic routed into a Local Zone.

.OpenShift Container Platform cluster without traffic routed into Local Zones
image::../images/354_OpenShift_ROSA_Local_Zones_0923_1.png[OpenShift Container Platform cluster without traffic routed into Local Zones]

The following diagram displays a OpenShift Container Platform cluster with traffic routed into a Local Zone.

.OpenShift Container Platform cluster with traffic routed into Local Zones
image::../images/354_OpenShift_ROSA_Local_Zones_0923_2.png[OpenShift Container Platform cluster with traffic routed into Local Zones]

.Additional resources

* Configuring machine pools in Local Zones
