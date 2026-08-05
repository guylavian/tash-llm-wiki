---
title: "{product-title} service definition"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-service-definition
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-service-definition
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# {product-title} service definition

[id="rosa-service-definition"]
= OpenShift Container Platform service definition

[role="_abstract"]
This documentation outlines the service definition for the OpenShift Container Platform managed service.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-account-management_{context}"]
= Account management

This section provides information about the service definition for OpenShift Container Platform account management.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-billing_{context}"]
= Billing and pricing

OpenShift Container Platform is billed directly to your {AWS} account. ROSA pricing is consumption based, with annual commitments or three-year commitments for greater discounting. The total cost of ROSA consists of two components:

* ROSA service fees
* AWS infrastructure fees

Visit the OpenShift Container Platform Pricing page on the AWS website for more details.
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-cluster-self-service_{context}"]
= Cluster self-service

Customers can self-service their clusters, including, but not limited to:

* Create a cluster
* Delete a cluster
* Add or remove an identity provider
* Add or remove a user from an elevated group
* Configure cluster privacy
* Add or remove machine pools and configure autoscaling
* Define upgrade policies

You can perform these self-service tasks using the OpenShift Container Platform (ROSA) CLI, `rosa`.

[role="_additional-resources"]
.Additional resources

* Red{nbsp}Hat Operator Support
* Configuring PID limits

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-instance-types_{context}"]
= Instance types

All {hcp-title} clusters require a minimum of 2 worker nodes. Shutting down the underlying (EC2 instance) infrastructure through the cloud provider console is unsupported and can lead to data loss and other risks.
Single availability zone clusters require a minimum of 3 control plane nodes, 2 infrastructure nodes, and 2 worker nodes deployed to a single availability zone.

Multiple availability zone clusters require a minimum of 3 control plane nodes, 3 infrastructure nodes, and 3 worker nodes.

Consider the following limitations when deploying and managing workloads:

* You must deploy workloads on worker nodes that exist in the cluster by using OpenShift Container Platform machine pools.
* Run workloads that you consider essential on the control plane and infrastructure nodes as daemonsets.
* You must ensure that any workloads running on these nodes are secure, scalable, and compatible with a version of OpenShift Container Platform, so that the Service Level Agreement (SLA) for API server availability is not impacted.

Red{nbsp}Hat might notify you and resize the control plane or infrastructure nodes if the OpenShift Container Platform components are impacted.

Control plane and infrastructure nodes are deployed and managed by Red{nbsp}Hat. These nodes are automatically resized based on the resource use. If you need to resize these nodes to meet cluster demands, open a support case.

[WARNING]
====
Shutting down the underlying infrastructure through the cloud provider console is unsupported and can lead to data loss.
====

See the following Red{nbsp}Hat Operator support section for more information about Red{nbsp}Hat workloads that must be deployed on worker nodes.

[NOTE]
====
Approximately one vCPU core and 1 GiB of memory are reserved on each worker node and removed from allocatable resources. This reservation of resources is necessary to run processes required by the underlying platform. These processes include system daemons such as udev, kubelet, and container runtime among others. The reserved resources also account for kernel reservations.

OpenShift/ROSA core systems such as audit log aggregation, metrics collection, DNS, image registry, CNI/OVN-Kubernetes, and others might consume additional allocatable resources to maintain the stability and maintainability of the cluster. The additional resources consumed might vary based on usage.

For additional information, see the Kubernetes documentation.
====

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform instance types

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-regions-az_{context}"]
= Regions and availability zones

The following AWS regions are currently available
for {hcp-title}.
for Red{nbsp}Hat OpenShift 4 and are supported for OpenShift Container Platform.

[NOTE]
====
Regions in China are not supported, regardless of their support on OpenShift Container Platform.
====

[NOTE]
====
For GovCloud (US) regions, you must submit an Access request for Red{nbsp}Hat OpenShift Service on AWS (ROSA) FedRAMP.

The following AWS GovCloud regions are supported:

* `us-gov-west-1`
* `us-gov-east-1`

For more information about AWS GovCloud regions, see the The AWS GovCloud (US) User Guide.
====

.AWS regions
[cols="4",options="header"]
|===
|Region
|Location
|Minimum ROSA version required
|AWS opt-in required

|us-east-1
|N. Virginia
|4.14
|No

|us-east-2
|Ohio
|4.14
|No

|us-west-1
|N. California
|4.14
|No

|us-west-2
|Oregon
|4.14
|No

|af-south-1
|Cape Town
|4.14
|Yes

|ap-east-1
|Hong Kong
|4.14
|Yes

|ap-south-2
|Hyderabad
|4.14
|Yes

|ap-southeast-3
|Jakarta
|4.14
|Yes

|ap-southeast-4
|Melbourne
|4.14
|Yes

|ap-southeast-5
|Malaysia
|4.16.34; 4.17.15
|Yes

|ap-southeast-6
|Auckland
|4.19.18
|Yes

|ap-southeast-7
|Thailand
|4.18
|Yes

|ap-south-1
|Mumbai
|4.14
|No

|ap-northeast-3
|Osaka
|4.14
|No

|ap-northeast-2
|Seoul
|4.14
|No

|ap-southeast-1
|Singapore
|4.14
|No

|ap-southeast-2
|Sydney
|4.14
|No

|ap-northeast-1
|Tokyo
|4.14
|No

|ca-central-1
|Central Canada
|4.14
|No

|eu-central-1
|Frankfurt
|4.14
|No

|mx-central-1
|Mexico
|4.18
|Yes

|eu-north-1
|Stockholm
|4.14
|No

|eu-west-1
|Ireland
|4.14
|No

|eu-west-2
|London
|4.14
|No

|eu-south-1
|Milan
|4.14
|Yes

|eu-west-3
|Paris
|4.14
|No

|eu-south-2
|Spain
|4.14
|Yes

|eu-central-2
|Zurich
|4.14
|Yes

|me-south-1
|Bahrain
|4.14
|Yes

|me-central-1
|UAE
|4.14
|Yes

|sa-east-1
|São Paulo
|4.14
|No

|il-central-1
|Tel Aviv
|4.15
|Yes

|ca-west-1
|Calgary
|4.14
|Yes

|us-gov-east-1
|AWS GovCloud - US-East
|4.14
|No

|us-gov-west-1
|AWS GovCloud - US-West
|4.14
|No
|===

Clusters can only be deployed in regions with at least 3 availability zones. For more information, see the Regions and Availability Zones section in the AWS documentation.

Each new
OpenShift Container Platform
{hcp-title}
cluster is installed within
a
an installer-created or
preexisting Virtual Private Cloud (VPC) in a single region, with the option to deploy
into a single availability zone (Single-AZ) or across multiple availability zones (Multi-AZ).
up to the total number of availability zones for the given region.
This provides cluster-level network and resource isolation, and enables cloud-provider VPC settings, such as VPN connections and VPC Peering. Persistent volumes (PVs) are backed by Amazon Elastic Block Storage (Amazon EBS), and are specific to the availability zone in which they are provisioned. Persistent volume claims (PVCs) do not bind to a volume until the associated pod resource is assigned into a specific availability zone to prevent unschedulable pods. Availability zone-specific resources are only usable by resources in the same availability zone.

[WARNING]
====
The region
and the choice of single or multiple availability zone
cannot be changed after a cluster has been deployed.
====

[role="_additional-resources"]
.Additional resources

* Red{nbsp}Hat OpenShift Service on AWS endpoints and quotas

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-am-local-zones_{context}"]
= Local Zones

{hcp-title-first} does not support the use of AWS Local Zones.
OpenShift Container Platform supports the use of AWS Local Zones, which are metropolis-centralized availability zones where customers can place latency-sensitive application workloads. Local Zones are extensions of AWS Regions that have their own internet connection. For more information about AWS Local Zones, see the AWS documentation How Local Zones work.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-sla_{context}"]
= Service Level Agreement (SLA)

//Note for writers: Do not link directly to the appendix 4 PDF, as each PDF is dated at generation and will not be kept up to date.
Any SLAs for the service itself are defined in Appendix 4 of the Red{nbsp}Hat Enterprise Agreement Appendix 4 (Online Subscription Services).

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-limited-support_{context}"]
= Limited support status

When a cluster transitions to a _Limited Support_ status, Red{nbsp}Hat no longer proactively monitors the cluster, the SLA is no longer applicable, and credits requested against the SLA are denied. It does not mean that you no longer have product support. In some cases, the cluster can return to a fully-supported status if you remediate the violating factors. However, in other cases, you might have to delete and recreate the cluster.

A cluster might move to a Limited Support status for many reasons, including the following scenarios:

If you do not upgrade a cluster to a supported version before the end-of-life date:: Red{nbsp}Hat does not make any runtime or SLA guarantees for versions after their end-of-life date. To receive continued support, upgrade the cluster to a supported version prior to the end-of-life date. If you do not upgrade the cluster prior to the end-of-life date, the cluster transitions to a Limited Support status until it is upgraded to a supported version.
+
Red{nbsp}Hat provides commercially reasonable support to upgrade from an unsupported version to a supported version. However, if a supported upgrade path is no longer available, you might have to create a new cluster and migrate your workloads.

If you remove or replace any native OpenShift Container Platform components or any other component that is installed and managed by Red{nbsp}Hat:: If cluster administrator permissions were used, Red{nbsp}Hat is not responsible for any of your or your authorized users’ actions, including those that affect infrastructure services, service availability, or data loss. If Red{nbsp}Hat detects any such actions, the cluster might transition to a Limited Support status. Red{nbsp}Hat notifies you of the status change and you should either revert the action or create a support case to explore remediation steps that might require you to delete and recreate the cluster.

If you have questions about a specific action that might cause a cluster to move to a Limited Support status or need further assistance, open a support ticket.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-support_{context}"]
= Support

OpenShift Container Platform includes Red{nbsp}Hat Premium Support, which can be accessed by using the Red{nbsp}Hat Customer Portal.

See the Red{nbsp}Hat Production Support Terms of Service for support response times.

AWS support is subject to a customer's existing support contract with AWS.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc

[id="rosa-sdpolicy-logging_{context}"]
= Logging

OpenShift Container Platform provides optional integrated log forwarding to Amazon (AWS) CloudWatch.

[id="rosa-sdpolicy-cluster-audit-logging_{context}"]
== Cluster audit logging
Cluster audit logs are available through AWS CloudWatch, if the integration is enabled. If the integration is not enabled, you can request the audit logs by opening a support case.

[id="rosa-sdpolicy-application-logging_{context}"]
== Application logging
Application logs sent to `STDOUT` are collected by Fluentd and forwarded to AWS CloudWatch through the cluster logging stack, if it is installed.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc

[id="rosa-sdpolicy-monitoring_{context}"]
= Monitoring

This section provides information about the service definition for OpenShift Container Platform monitoring.

[id="rosa-sdpolicy-cluster-metrics_{context}"]
== Cluster metrics

OpenShift Container Platform clusters come with an integrated Prometheus stack for cluster monitoring including CPU, memory, and network-based metrics. This is accessible through the web console. These metrics also allow for horizontal pod autoscaling based on CPU or memory metrics provided by a ROSA user.

[id="rosa-sdpolicy-cluster-status-notifications_{context}"]
== Cluster notifications

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-networking_{context}"]
= Networking

This section provides information about the service definition for ROSA networking.

[id="rosa-sdpolicy-custom-domains_{context}"]
== Custom domains for applications

[WARNING]
====
Starting with OpenShift Container Platform 4.14, the Custom Domain Operator is deprecated. To manage Ingress in ROSA 4.14 or later, use the Ingress Operator.
====
To use a custom hostname for a route, you must update your DNS provider by creating a canonical name (CNAME) record. Your CNAME record should map the OpenShift canonical router hostname to your custom domain. The OpenShift canonical router hostname is shown on the _Route Details_ page after a route is created. Alternatively, a wildcard CNAME record can be created once to route all subdomains for a given hostname to the cluster's router.

[id="rosa-sdpolicy-validated-certificates_{context}"]
== Domain validated certificates
ROSA includes TLS security certificates needed for both internal and external services on the cluster. For external routes, there are two separate TLS wildcard certificates that are provided and installed on each cluster: one is for the web console and route default hostnames, and the other is for the API endpoint. Let’s Encrypt is the certificate authority used for certificates. Routes within the cluster, such as the internal API endpoint, use TLS certificates signed by the cluster's built-in certificate authority and require the CA bundle available in every pod for trusting the TLS certificate.

[id="rosa-sdpolicy-custom-certificates_{context}"]
== Custom certificate authorities for builds
ROSA supports the use of custom certificate authorities to be trusted by builds when pulling images from an image registry.

[id="rosa-sdpolicy-load-balancers_{context}"]
== Load balancers

{hcp-title-first} only deploys load balancers from the default ingress controller. All other load balancers can be optionally deployed by a customer for secondary ingress controllers or service load balancers.
OpenShift Container Platform uses up to five different load balancers:

- An internal control plane load balancer that is internal to the cluster and used to balance traffic for internal cluster communications.
- An external control plane load balancer that is used for accessing the OpenShift and Kubernetes APIs. This load balancer can be disabled in {cluster-manager}. If this load balancer is disabled, Red{nbsp}Hat reconfigures the API DNS to point to the internal control plane load balancer.
- An external control plane load balancer for Red{nbsp}Hat that is reserved for cluster management by Red{nbsp}Hat. Access is strictly controlled, and communication is only possible from whitelisted bastion hosts.
- A default external router/ingress load balancer that is the default application load balancer, denoted by `apps` in the URL. The default load balancer can be configured in {cluster-manager} to be either publicly accessible over the Internet or only privately accessible over a pre-existing private connection. All application routes on the cluster are exposed on this default router load balancer, including cluster services such as the logging UI, metrics API, and registry.
- Optional: A secondary router/ingress load balancer that is a secondary application load balancer, denoted by `apps2` in the URL. The secondary load balancer can be configured in {cluster-manager} to be either publicly accessible over the Internet or only privately accessible over a pre-existing private connection. If a `Label match` is configured for this router load balancer, then only application routes matching this label are exposed on this router load balancer; otherwise, all application routes are also exposed on this router load balancer.
- Optional: Load balancers for services. Enable non-HTTP/SNI traffic and non-standard ports for services. These load balancers can be mapped to a service running on OpenShift Container Platform to enable advanced ingress features, such as non-HTTP/SNI traffic or the use of non-standard ports. Each AWS account has a quota which limits the number of Classic Load Balancers that can be used within each cluster.

[id="rosa-sdpolicy-cluster-ingress_{context}"]
== Cluster ingress
Project administrators can add route annotations for many different purposes, including ingress control through IP allow-listing.

Ingress policies can also be changed by using `NetworkPolicy` objects, which leverage the `ovs-networkpolicy` plugin. This allows for full control over the ingress network policy down to the pod level, including between pods on the same cluster and even in the same namespace.

All cluster ingress traffic will go through the defined load balancers. Direct access to all nodes is blocked by cloud configuration.

[id="rosa-sdpolicy-cluster-egress_{context}"]
== Cluster egress
Pod egress traffic control through `EgressNetworkPolicy` objects can be used to prevent or limit outbound traffic in
ROSA with hosted control planes (HCP).
OpenShift Container Platform.

Public outbound traffic from the control plane and infrastructure nodes is required and necessary to maintain cluster image security and cluster monitoring. This requires that the `0.0.0.0/0` route belongs only to the Internet gateway; it is not possible to route this range over private connections.

OpenShift 4 clusters use NAT gateways to present a public, static IP for any public outbound traffic leaving the cluster. Each availability zone a cluster is deployed into receives a distinct NAT gateway, therefore up to 3 unique static IP addresses can exist for cluster egress traffic. Any traffic that remains inside the cluster, or that does not go out to the public Internet, will not pass through the NAT gateway and will have a source IP address belonging to the node that the traffic originated from. Node IP addresses are dynamic; therefore, a customer must not rely on whitelisting individual IP addresses when accessing private resources.

Customers can determine their public static IP addresses by running a pod on the cluster and then querying an external service. For example:
[source,terminal]
----
$ oc run ip-lookup --image=busybox -i -t --restart=Never --rm -- /bin/sh -c "/bin/nslookup -type=a myip.opendns.com resolver1.opendns.com | grep -E 'Address: [0-9.]+'"
----

[id="rosa-sdpolicy-cloud-network-config_{context}"]
== Cloud network configuration
{Product-title} allows for the configuration of a private network connection through AWS-managed technologies, such as:

- VPN connections
- VPC peering
- Transit Gateway
- Direct Connect

[IMPORTANT]
====
Red{nbsp}Hat site reliability engineers (SREs) do not monitor private network connections. Monitoring of these connections is the responsibility of the customer.
====

[id="rosa-sdpolicy-dns-forwarding_{context}"]
== DNS forwarding
For ROSA clusters that have a private cloud network configuration, a customer can specify internal DNS servers available on that private connection that should be queried for explicitly provided domains.

[id="rosa-sdpolicy-network-verification_{context}"]
== Network verification

Network verification checks run automatically when you deploy a ROSA cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster. The checks validate your network configuration and highlight errors, enabling you to resolve configuration issues prior to deployment.

You can also run the network verification checks manually to validate the configuration for an existing cluster.

[role="_additional-resources"]
.Additional resources

* Network verification

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-storage_{context}"]
= Storage

This section provides information about the service definition for
{hcp-title-first}
OpenShift Container Platform
storage.

[id="rosa-sdpolicy-encrytpted-at-rest-storage_{context}"]
== Encrypted-at-rest OS and node storage

Worker
Control plane, infrastructure, and worker
nodes use encrypted-at-rest Amazon Elastic Block Store (Amazon EBS) storage.

[id="rosa-sdpolicy-encrytpted-at-rest-pv_{context}"]
== Encrypted-at-rest PV
EBS volumes that are used for PVs are encrypted-at-rest by default.

[id="rosa-sdpolicy-block-storage_{context}"]
== Block storage (RWO)
Persistent volumes (PVs) are backed by Amazon Elastic Block Store (Amazon EBS), which is Read-Write-Once.

PVs can be attached only to a single node at a time and are specific to the availability zone in which they were provisioned. However, PVs can be attached to any node in the availability zone.

Each cloud provider has its own limits for how many PVs can be attached to a single node. See AWS instance type limits for details.

== Shared Storage (RWX)

The AWS CSI Driver can be used to provide RWX support for
{hcp-title-first}.
OpenShift Container Platform.
A community Operator is provided to simplify setup. See Amazon Elastic File Storage Setup for Red Hat OpenShift Service on AWS for details.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-platform_{context}"]
= Platform

This section provides information about the service definition for the
{hcp-title-first} platform.
OpenShift Container Platform (ROSA) platform.

[id="rosa-sdpolicy-autoscaling_{context}"]
== Autoscaling
Node autoscaling is available on
{hcp-title}.
OpenShift Container Platform.
You can configure the autoscaler option to automatically scale the number of machines in a cluster.

[id="rosa-sdpolicy-daemonsets_{context}"]
== Daemonsets

Customers can create and run daemonsets onOpenShift Container Platform.
 To restrict daemonsets to only running on worker nodes, use the following `nodeSelector`:

[source,yaml]
----
spec:
  nodeSelector:
    role: worker
----
[id="rosa-sdpolicy-multiple-availability-zone_{context}"]
== Multiple availability zone

Control plane components are always deployed across multiple availability zones, regardless of a customer's worker node configuration.
In a multiple availability zone cluster, control plane nodes are distributed across availability zones and at least one worker node is required in each availability zone.

[id="rosa-sdpolicy-node-labels_{context}"]
== Node labels
Custom node labels are created by Red{nbsp}Hat during node creation and cannot be changed on
{hcp-title}
OpenShift Container Platform
clusters at this time. However, custom labels are supported when creating new machine pools.

[id="rosa-sdpolicy-node-lifecycle_{context}"]
== Node lifecycle

Worker nodes are not guaranteed longevity, and may be replaced at any time as part of the normal operation and management of OpenShift.

A worker node might be replaced in the following circumstances:

* Machine health checks are deployed and configured to ensure that a worker node with a `NotReady` status is replaced to ensure smooth operation of the cluster.
* AWS EC2 instances may be terminated when AWS detects irreparable failure of the underlying hardware that hosts the instance.
* During upgrades, a new node is first provisioned to account for any loss of cluster resources during the upgrade process. Once this new node has been successfully integrated into the cluster via the previously described automated health checks, an older node is then removed from the cluster.
* During upgrades, a new, upgraded node is first created and joined to the cluster. Once this new node has been successfully integrated into the cluster via the previously described automated health checks, an older node is then removed from the cluster.

For all containerized workloads running on a Kubernetes based system, it is best practice to configure applications to be resilient of node replacements.

[id="rosa-sdpolicy-backup-policy_{context}"]
== Cluster backup policy

Red Hat recommends object-level backup solutions for ROSA clusters. OpenShift API for Data Protection (OADP) is included in OpenShift but not enabled by default. Customers can configure OADP on their clusters to achieve object-level backup and restore capabilities.

//Omitted until XCMSTRAT-480 is complete
//While Red Hat takes frequent backups of etcd, this is for use by Red Hat for maintenance and service restoration purposes, and is never provided to customers for any reason.

Red Hat does not back up customer applications or application data. Customers are solely responsible for applications and their data, and must put their own backup and restore capabilities in place.

[WARNING]
====
Customers are solely responsible for backing up and restoring their applications and application data. For more information about customer responsibilities, see "Shared responsibility matrix".
====

[id="rosa-sdpolicy-openshift-version_{context}"]
== OpenShift version
{hcp-title}
OpenShift Container Platform
is run as a service. Red{nbsp}Hat SRE team will force upgrade when end of life (EOL) is reached.
is run as a service and is kept up to date with
the latest OpenShift Container Platform version.
Upgrade scheduling to the latest version is available.

[id="rosa-sdpolicy-upgrades_{context}"]
== Upgrades
Upgrades can be scheduled using the ROSA CLI, `rosa`, or through {cluster-manager}.

See the OpenShift Container Platform Life Cycle for more information on the upgrade policy and procedures.

[id="rosa-sdpolicy-window-containers_{context}"]
== Windows Containers
{productwinc} is not available on OpenShift Container Platform at this time.
Alternatively, it is supported to run Windows based virtual machines on OpenShift Virtualization running on a ROSA cluster.

[id="rosa-sdpolicy-container-engine_{context}"]
== Container engine
{hcp-title}
OpenShift Container Platform
runs on OpenShift 4 and uses CRI-O as the only available container engine
(container runtime interface).
[id="rosa-sdpolicy-operating-system_{context}"]
== Operating system
{hcp-title}
OpenShift Container Platform
runs on OpenShift 4 and uses Red{nbsp}Hat CoreOS (RHCOS) as the operating system for all cluster nodes.

[id="rosa-sdpolicy-red-hat-operator_{context}"]
== Red{nbsp}Hat Operator support
Red{nbsp}Hat workloads typically refer to Red{nbsp}Hat-provided Operators made available through Operator Hub. Red{nbsp}Hat workloads are not managed by the Red{nbsp}Hat SRE team, and must be deployed on worker nodes. These Operators may require additional Red{nbsp}Hat subscriptions, and may incur additional cloud infrastructure costs. Examples of these Red{nbsp}Hat-provided Operators are:

* {rhq-short}
* Red{nbsp}Hat Advanced Cluster Management
* Red{nbsp}Hat Advanced Cluster Security
* {SMProductName}
* {ServerlessProductName}
* {logging-sd}
* {pipelines-title}
* {VirtProductName}

[id="rosa-sdpolicy-kubernetes-operator_{context}"]
== Kubernetes Operator support

All Operators listed in the software catalog marketplace should be available for installation. These Operators are considered customer workloads, and are not monitored nor managed by Red{nbsp}Hat SRE. Operators authored by Red{nbsp}Hat are supported by Red{nbsp}Hat.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

[id="rosa-sdpolicy-security_{context}"]
= Security

This section provides information about the service definition for
{hcp-title-first}
OpenShift Container Platform
security.

[id="rosa-sdpolicy-auth-provider_{context}"]
== Authentication provider
Authentication for the cluster can be configured using either {cluster-manager-url} or cluster creation process or using the ROSA CLI, `rosa`. ROSA is not an identity provider, and all access to the cluster must be managed by the customer as part of their integrated solution. The use of multiple identity providers provisioned at the same time is supported. The following identity providers are supported:

- GitHub or GitHub Enterprise
- GitLab
- Google
- LDAP
- OpenID Connect
- htpasswd

[id="rosa-sdpolicy-privileged-containers_{context}"]
== Privileged containers
Privileged containers are available for users with the `cluster-admin` role. Usage of privileged containers as `cluster-admin` is subject to the responsibilities and exclusion notes in the Red{nbsp}Hat Enterprise Agreement Appendix 4 (Online Subscription Services).

[id="rosa-sdpolicy-customer-admin-user_{context}"]
== Customer administrator user
In addition to normal users,
{hcp-title-first}
OpenShift Container Platform
provides access to a
{hcp-title}-specific
ROSA-specific
group called `dedicated-admin`. Any users on the cluster that are members of the `dedicated-admin` group:

- Have administrator access to all customer-created projects on the cluster.
- Can manage resource quotas and limits on the cluster.
- Can add and manage `NetworkPolicy` objects.
- Are able to view information about specific nodes and PVs in the cluster, including scheduler information.
- Can access the reserved `dedicated-admin` project on the cluster, which allows for the creation of service accounts with elevated privileges and also gives the ability to update default limits and quotas for projects on the cluster.
- Can install Operators from the software catalog and perform all verbs in all `*.operators.coreos.com` API groups.

[id="rosa-sdpolicy-cluster-admin-role_{context}"]
== Cluster administration role
The administrator of
{hcp-title-first}
OpenShift Container Platform
has default access to the `cluster-admin` role for your organization's cluster. While logged into an account with the `cluster-admin` role, users have increased permissions to run privileged security contexts.

[id="rosa-sdpolicy-project-self-service_{context}"]
== Project self-service
By default, all users have the ability to create, update, and delete their projects. This can be restricted if a member of the `dedicated-admin` group removes the `self-provisioner` role from authenticated users:
[source,terminal]
----
$ oc adm policy remove-cluster-role-from-group self-provisioner system:authenticated:oauth
----

Restrictions can be reverted by applying:
[source,terminal]
----
$ oc adm policy add-cluster-role-to-group self-provisioner system:authenticated:oauth
----

[id="rosa-sdpolicy-regulatory-compliance_{context}"]
== Regulatory compliance
//removing conditionals and first sentence as rosa-with-hcp has now obtained compliance certifications
See the _Compliance_ table in _Understanding process and security for ROSA_ for the latest compliance information.

[id="rosa-sdpolicy-network-security_{context}"]
== Network security
With OpenShift Container Platform, AWS provides a standard DDoS protection on all load balancers, called AWS Shield. This provides 95% protection against most commonly used level 3 and 4 attacks on all the public facing load balancers used for ROSA. A 10-second timeout is added for HTTP requests coming to the `haproxy` router to receive a response or the connection is closed to provide additional protection.

[id="rosa-sdpolicy-etcd-encryption_{context}"]
== etcd encryption

In OpenShift Container Platform, the control plane storage is encrypted at rest by default, including encryption of the etcd volumes. This storage-level encryption is provided through the storage layer of the cloud provider.

Customers can also opt to encrypt the etcd database at build time or provide their own custom AWS KMS keys for the purpose of encrypting the etcd database.

Etcd encryption will encrypt the following Kubernetes API server and OpenShift API server resources:
You can also enable etcd encryption, which encrypts the key values in etcd, but not the keys. If you enable etcd encryption, the following Kubernetes API server and OpenShift API server resources are encrypted:

* Secrets
* Config maps
* Routes
* OAuth access tokens
* OAuth authorize tokens

The etcd encryption feature is not enabled by default and it can be enabled only at cluster installation time. Even with etcd encryption enabled, the etcd key values are accessible to anyone with access to the control plane nodes or `cluster-admin` privileges.

[IMPORTANT]
====
By enabling etcd encryption for the key values in etcd, you will incur a performance overhead of approximately 20%. The overhead is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Red{nbsp}Hat recommends that you enable etcd encryption only if you specifically require it for your use case.
====

[role="_additional-resources"]
[id="additional-resources_rosa-service-definition"]
== Additional resources
* Understanding process and security for OpenShift Container Platform
* OpenShift Container Platform life cycle
