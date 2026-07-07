---
title: "AWS prerequisites for {product-title}"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-aws-prereqs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-aws-prereqs
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# AWS prerequisites for {product-title}

[id="prerequisites"]
= AWS prerequisites for OpenShift Container Platform

[role="_abstract"]
OpenShift Container Platform provides a model that allows Red{nbsp}Hat to deploy clusters into a customer's existing Amazon Web Service (AWS) account.

You must ensure that the prerequisites are met before installing OpenShift Container Platform. This requirements document does not apply to AWS Security Token Service (STS). If you are using STS, see the STS-specific requirements.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="rosa-customer-requirements_{context}"]
= Customer Requirements

[role="_abstract"]
You must complete several prerequisites before deploying a OpenShift Container Platform cluster.

[NOTE]
====
In order to create the cluster, you must be logged in as an IAM user and not an assumed role or STS user.
====

[id="rosa-account_{context}"]
== Account
* The customer ensures that the AWS limits are sufficient to support OpenShift Container Platform provisioned within the customer's AWS account.
* The customer's AWS account should be in the customer’s AWS Organizations with the applicable service control policy (SCP) applied.
+
[NOTE]
====
It is not a requirement that the customer's account be within the AWS Organizations or for the SCP to be applied, however Red{nbsp}Hat must be able to perform all the actions listed in the SCP without restriction.
====

* The customer's AWS account should not be transferable to Red{nbsp}Hat.
* The customer may not impose AWS usage restrictions on Red{nbsp}Hat activities. Imposing restrictions will severely hinder Red{nbsp}Hat’s ability to respond to incidents.
* The customer may deploy native AWS services within the same AWS account.
+
[NOTE]
====
Customers are encouraged, but not mandated, to deploy resources in a Virtual Private Cloud (VPC) separate from the VPC hosting OpenShift Container Platform and other Red{nbsp}Hat supported services.
====

[id="rosa-access-requirements_{context}"]
== Access requirements
* To appropriately manage the OpenShift Container Platform service, Red{nbsp}Hat must have the `AdministratorAccess` policy applied to the administrator role at all times. This requirement does *not* apply if you are using AWS Security Token Service (STS).
+
[NOTE]
====
This policy only provides Red{nbsp}Hat with permissions and capabilities to change resources in the customer-provided AWS account.
====
* Red{nbsp}Hat must have AWS console access to the customer-provided AWS account. This access is protected and managed by Red{nbsp}Hat.
* The customer must not utilize the AWS account to elevate their permissions within the OpenShift Container Platform cluster.
* Actions available in the OpenShift Container Platform (ROSA) CLI, `rosa`, or {cluster-manager-url} console must not be directly performed in the customer's AWS account.

[id="rosa-support-requirements_{context}"]
== Support requirements
* Red{nbsp}Hat recommends that the customer have at least Business Support from AWS.
* Red{nbsp}Hat has authority from the customer to request AWS support on their behalf.
* Red{nbsp}Hat has authority from the customer to request AWS resource limit increases on the customer's account.
* Red{nbsp}Hat manages the restrictions, limitations, expectations, and defaults for all OpenShift Container Platform clusters in the same manner, unless otherwise specified in this requirements section.

[id="rosa-security-requirements_{context}"]
== Security requirements
* Volume snapshots will remain within the customer's AWS account and customer-specified region.
* Red{nbsp}Hat must have ingress access to EC2 hosts and the API server from allow-listed IP addresses.
* Red{nbsp}Hat must have egress allowed to forward system and audit logs to a Red{nbsp}Hat managed central logging stack.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="rosa-required-procedure_{context}"]
= Required customer procedure

[role="_abstract"]
Complete these steps before deploying OpenShift Container Platform.

.Procedure
. If you, as the customer, are utilizing AWS Organizations, then you must use an AWS account within your organization or create a new one.
. To ensure that Red{nbsp}Hat can perform necessary actions, you must either create a service control policy (SCP) or ensure that none is applied to the AWS account.
. Attach the SCP to the AWS account.
. Follow the ROSA procedures for setting up the environment.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="rosa-minimum-scp_{context}"]
= Minimum set of effective permissions for service control policies (SCP)

[role="_abstract"]
Service control policies (SCP) are a type of organization policy that manages permissions within your organization. SCPs ensure that accounts within your organization stay within your defined access control guidelines. These policies are maintained in AWS organizations and control the services that are available within the attached AWS accounts. SCP management is the responsibility of the customer.

[NOTE]
====
When using AWS Security Token Service (STS), you must ensure that the service control policy does not block the following resources:

* `ec2:{}`
* `iam:{}`
* `tag:*`
====

[NOTE]
====
The minimum SCP requirement does not apply when using AWS Security Token Service (STS). For more information about STS, see AWS prerequisites for ROSA with STS.
====

Verify that your service control policy (SCP) does not restrict any of these required permissions.

[cols="2a,2a,2a,2a",options="header"]

|===
|
| Service
| Actions
| Effect

.18+| Required
|Amazon EC2 | All |Allow
|Amazon EC2 Auto Scaling | All |Allow
|Amazon S3| All |Allow
|Identity And Access Management | All |Allow
|Elastic Load Balancing | All |Allow
|Elastic Load Balancing V2| All |Allow
|Amazon CloudWatch | All |Allow
|Amazon CloudWatch Events | All |Allow
|Amazon CloudWatch Logs | All |Allow
|AWS EC2 Instance Connect | SendSerialConsoleSSHPublicKey |Allow
|AWS Support | All |Allow
|AWS Key Management Service | All |Allow
|AWS Security Token Service | All |Allow
|AWS Tiro | CreateQuery

GetQueryAnswer

GetQueryExplanation
| Allow
|AWS Marketplace | Subscribe

Unsubscribe

View Subscriptions
| Allow
|AWS Resource Tagging | All |Allow
|AWS Route53 DNS | All |Allow
|AWS Service Quotas | ListServices

GetRequestedServiceQuotaChange

GetServiceQuota

RequestServiceQuotaIncrease

ListServiceQuotas
| Allow

.3+|Optional | AWS Billing
| ViewAccount

Viewbilling

ViewUsage
| Allow

|AWS Cost and Usage Report
|All
|Allow

|AWS Cost Explorer Services
|All
|Allow

|===

[role="_additional-resources"]
.Additional resources

* Service control policies
* SCP effects on permissions

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="rosa-policy-iam_{context}"]
= Red{nbsp}Hat managed IAM references for AWS

[role="_abstract"]
Red{nbsp}Hat is responsible for creating and managing the following Amazon Web Services (AWS) resources: IAM policies, IAM users, and IAM roles.

[id="rosa-iam-policies_{context}"]
== IAM Policies

[NOTE]
====
IAM policies are subject to modification as the capabilities of OpenShift Container Platform change.
====

* The `AdministratorAccess` policy is used by the administration role. This policy provides Red{nbsp}Hat the access necessary to administer the OpenShift Container Platform (ROSA) cluster in the customer's AWS account.
+
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "*",
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
----

[id="rosa-iam-users_{context}"]
== IAM users

The `osdManagedAdmin` user is created immediately after installing ROSA into the customer's AWS account.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-aws-policy-provisioned_{context}"]
= Provisioned AWS Infrastructure

[role="_abstract"]
This is an overview of the provisioned {AWS} components on a deployed OpenShift Container Platform cluster.

[id="rosa-ec2-instances_{context}"]
== EC2 instances

AWS EC2 instances are required to deploy
the control plane and data plane functions for
OpenShift Container Platform.
Instance types can vary for control plane and infrastructure nodes, depending on the worker node count.

At a minimum, the following EC2 instances are deployed:

* Three `m5.2xlarge` control plane nodes
* Two `r5.xlarge` infrastructure nodes
* Two `m5.xlarge` worker nodes

At a minimum, two `m5.xlarge` EC2 instances are deployed for use as worker nodes.

The instance type shown for worker nodes is the default value, but you can customize the instance type for worker nodes according to the needs of your workload.

[id="rosa-ebs-storage_{context}"]
== Amazon Elastic Block Store storage

Amazon Elastic Block Store (Amazon EBS) block storage is used for both local node storage and persistent volume storage. By default, the following storage is provisioned for each EC2 instance:

* Control Plane Volume
** Size: 350GB
** Type: gp3
** Input/Output Operations Per Second: 1000

* Infrastructure Volume
** Size: 300GB
** Type: gp3
** Input/Output Operations Per Second: 900

* Worker Volume
** Default size: 300{nbsp}GiB (adjustable at creation time)
** Minimum size: 128GB
** Type: gp3
** Input/Output Operations Per Second: 900

[NOTE]
====
Clusters deployed before the release of {OCP} 4.11 use gp2 type storage by default.
====
* Node volumes
** Type: `AWS EBS GP3`
** Default size: 300{nbsp}GiB (adjustable at creation time)
** Minimum size: 75{nbsp}GiB

* Workload persistent volumes
** Default storage class: `gp3-csi`
** Provisioner: `ebs.csi.aws.com`
** Dynamic persistent volume provisioning

[id="rosa-elastic-load-balancers_{context}"]
== Elastic Load Balancing

Each cluster can use up to two Classic Load Balancers for application router and up to two Network Load Balancers for API.
By default, one Network Load Balancer is created for use by the default ingress controller. You can create additional load balancers of the following types according to the needs of your workload:

* Classic Load Balancer
* Network Load Balancer
* Application Load Balancer

For more information, see the ELB documentation for AWS.

[id="rosa-s3-storage_{context}"]
== S3 storage

The image registry is backed by AWS S3 storage. Resources are pruned regularly to optimize S3 usage and cluster performance.

[NOTE]
====
Two buckets are required with a typical size of 2TB each.
====

[id="rosa-vpc_{context}"]
== VPC

Configure your VPC according to the following requirements:

* *Subnets*: Every cluster requires a minimum of one private subnet for every availability zone. For example, 1 private subnet is required for a single-zone cluster, and 3 private subnets are required for a cluster with 3 availability zones.
+
If your cluster needs direct access to a network that is external to the cluster, including the public internet, you require at least one public subnet.
+
Red{nbsp}Hat strongly recommends using unique subnets for each cluster. Sharing subnets between multiple clusters is not recommended.
+
[NOTE]
====
A *public subnet* connects directly to the internet through an internet gateway.

A *private subnet* connects to the internet through a network address translation (NAT) gateway.
====

* *Route tables*: One route table per private subnet, and one additional table per cluster.

* *Internet gateways*: One Internet Gateway per cluster.

* *NAT gateways*: One NAT Gateway per public subnet.

.Sample VPC Architecture
image::VPC-Diagram.png[VPC Reference Architecture]

[id="rosa-security-groups_{context}"]
== Security groups

AWS security groups provide security at the protocol and port access level; they are associated with EC2 instances and Elastic Load Balancing (ELB) load balancers. Each security group contains a set of rules that filter traffic coming in and out of one or more EC2 instances.

Ensure that the ports required for cluster installation and operation are open on your network and configured to allow access between hosts. The requirements for the default security groups are listed in Required ports for default security groups.

[id="required-secgroup-ports_{context}"]
.Required ports for default security groups
[cols="2a,2a,2a,2a",options="header"]
|===

|Group
|Type
|IP Protocol
|Port range

.4+|MasterSecurityGroup
.4+|`AWS::EC2::SecurityGroup`
|`icmp`
|`0`

|`tcp`
|`22`

|`tcp`
|`6443`

|`tcp`
|`22623`

.2+|WorkerSecurityGroup
.2+|`AWS::EC2::SecurityGroup`
|`icmp`
|`0`

|`tcp`
|`22`

.2+|BootstrapSecurityGroup
.2+|`AWS::EC2::SecurityGroup`

|`tcp`
|`22`

|`tcp`
|`19531`

|===

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc
// * rosa_planning/rosa-cloud-expert-prereq-checklist.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc

[id="network-prereqs_{context}"]
= Networking prerequisites

[role="_abstract"]
During cluster deployment, OpenShift Container Platform requires a minimum bandwidth of 120{nbsp}Mbps between cluster infrastructure and the public internet or private network locations that give deployment resources. When network connectivity is slower than 120{nbsp}Mbps, the cluster installation process times out, and deployment fails. After cluster deployment, your workloads determine network requirements. A minimum bandwidth of 120{nbsp}Mbps helps to ensure timely cluster and Operator upgrades.

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-classic-firewall-prerequisites_{context}"]
= Firewall AllowList requirements for OpenShift Container Platform clusters using STS

[role="_abstract"]
You must AllowList several URLs to download required packages and tools for your cluster.

[IMPORTANT]
====
Only OpenShift Container Platform clusters deployed with PrivateLink can use a firewall to control egress traffic.
====
[id="osd-aws-privatelink-firewall-prerequisites_{context}"]
= Firewall AllowList requirements

[role="_abstract"]
If you are using a firewall to control egress traffic from OpenShift Container Platform, you must configure your firewall to grant access to the certain domain and port combinations below. OpenShift Container Platform requires this access to provide a fully managed OpenShift service.

.Domains for installation packages and tools
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
|`registry.redhat.io`
|443
|Provides core container images.

|`quay.io`
|443
|Provides core container images.

|`cdn01.quay.io`
|443
|Provides core container images.

|`cdn02.quay.io`
|443
|Provides core container images.

|`cdn03.quay.io`
|443
|Provides core container images.

|`cdn04.quay.io`
|443
|Provides core container images.

|`cdn05.quay.io`
|443
|Provides core container images.

|`cdn06.quay.io`
|443
|Provides core container images.

|`sso.redhat.com`
|443
|Required. The `https://console.redhat.com/openshift` site uses authentication from `sso.redhat.com` to download the pull secret and use Red{nbsp}Hat SaaS solutions to facilitate monitoring of your subscriptions, cluster inventory, chargeback reporting, and so on.

|`quay-registry.s3.amazonaws.com`
|443
|Provides core container images.

|`quayio-production-s3.s3.amazonaws.com`
|443
|Provides core container images.

|`registry.access.redhat.com`
|443
|Hosts all the container images that are stored on the Red{nbsp}Hat Ecosytem Catalog. Additionally, the registry provides access to the `odo` CLI tool that helps developers build on OpenShift and Kubernetes.

|`access.redhat.com`
|443
|Required. Hosts a signature store that a container client requires for verifying images when pulling them from `registry.access.redhat.com`.

|`registry.connect.redhat.com`
|443
|Required for all third-party images and certified Operators.

|`console.redhat.com`
|443
|Required. Allows interactions between the cluster and OpenShift Console Manager to enable functionality, such as scheduling upgrades.

|`sso.redhat.com`
|443
|The `https://console.redhat.com/openshift` site uses authentication from `sso.redhat.com`.

|`pull.q1w2.quay.rhcloud.com`
|443
|Provides core container images as a fallback when quay.io is not available.

|`catalog.redhat.com`
|443
|The `registry.access.redhat.com` and `https://registry.redhat.io` sites redirect through `catalog.redhat.com`.

|`oidc.op1.openshiftapps.com`
|443
|Used by OpenShift Container Platform  for STS implementation with managed OIDC configuration.

|`api.openshiftusgov.com`
|443
|This is for GovCloud only.

|`goalert-api.goalert-prod.appsrefrp01ugw1.p1.openshiftusgov.com`
|443
|This is for GovCloud only.

|`splunk.y0j2v8m5s2h4t0v.jciv.p1.openshiftusgov.com`
|443
|This is for GovCloud only.

|`ocm-prod.rosa-public-nlb.appsrefrp01ugw1.p1.openshiftusgov.com`
|443
|This is for GovCloud only.
|===

.Domains for telemetry
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`cert-api.access.redhat.com`
|443
|Required for telemetry.

|`api.access.redhat.com`
|443
|Required for telemetry.

|`infogw.api.openshift.com`
|443
|Required for telemetry.

|`console.redhat.com`
|443
|Required for telemetry and {red-hat-lightspeed}.

|`observatorium-mst.api.openshift.com`
|443
|Required for managed OpenShift-specific telemetry.

|`observatorium.api.openshift.com`
|443
|Required for managed OpenShift-specific telemetry.

|`console.openshiftusgov.com`
|443
|This is for GovCloud only.

|`time-a-g.nist.gov`
|443
|This is for GovCloud only.

|`time-a-wwv.nist.gov`
|443
|This is for GovCloud only.

|`time-a-b.nist.gov`
|443
|This is for GovCloud only.
|===

Managed clusters require enabling telemetry to allow Red{nbsp}Hat to react more quickly to problems, better support the customers, and better understand how product upgrades impact clusters. For more information about how remote health monitoring data is used by Red{nbsp}Hat, see _About remote health monitoring_ in the _Additional resources_ section.

.Domains for Amazon Web Services (AWS) APIs
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`.amazonaws.com`
|443
|Required to access AWS services and resources.
|===

Alternatively, if you choose to not use a wildcard for Amazon Web Services (AWS) APIs, you must allowlist the following URLs:

[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
|`ec2.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`events.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`iam.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`route53.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`sts.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment, for clusters configured to use the global endpoint for AWS STS.

|`sts.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment, for clusters configured to use regionalized endpoints for AWS STS. See AWS STS regionalized endpoints for more information.

|`tagging.us-east-1.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment. This endpoint is always us-east-1, regardless of the region the cluster is deployed in.

|`ec2.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`elasticloadbalancing.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

//|`servicequotas.<aws_region>.amazonaws.com`
//|443
//|Required. Used to confirm quotas for deploying the service.

|`tagging.<aws_region>.amazonaws.com`
|443
|Allows the assignment of metadata about AWS resources in the form of tags.
|===

.Domains for OpenShift
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`mirror.openshift.com`
|443
|Used to access mirrored installation content and images. This site is also a source of release image signatures.

|`api.openshift.com`
|443
|Used to check if updates are available for the cluster.
|===

.Domains for your Site Reliability Engineering (SRE) and management
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`api.pagerduty.com`
|443
|This alerting service is used by the in-cluster alertmanager to send alerts notifying Red{nbsp}Hat SRE of an event to take action on.

|`events.pagerduty.com`
|443
|This alerting service is used by the in-cluster alertmanager to send alerts notifying Red{nbsp}Hat SRE of an event to take action on.

|`api.deadmanssnitch.com`
|443
|Alerting service used by OpenShift Container Platform to send periodic pings that indicate whether the cluster is available and running.

|`nosnch.in`
|443
|Alerting service used by OpenShift Container Platform to send periodic pings that indicate whether the cluster is available and running.

|`http-inputs-osdsecuritylogs.splunkcloud.com`
|443
|Required. Used by the `splunk-forwarder-operator` as a logging forwarding endpoint to be used by Red{nbsp}Hat SRE for log-based alerting.

|`sftp.access.redhat.com` (Recommended)
|22
|The SFTP server used by `must-gather-operator` to upload diagnostic logs to help troubleshoot issues with the cluster.
|===

[role="_additional-resources"]
.Additional resources

* About remote health monitoring
* Security groups
* Required AWS service quotas

[role="_additional-resources"]
== Additional resources
// Removed as part of OSDOCS-13310, until figures are verified.
//* Limits and scalability
* SRE access to all Red{nbsp}Hat OpenShift Service on AWS clusters
* Understanding the ROSA deployment workflow
