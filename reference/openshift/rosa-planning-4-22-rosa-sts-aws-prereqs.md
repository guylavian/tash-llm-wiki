---
title: "Detailed requirements for deploying {product-title} using STS"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-sts-aws-prereqs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-sts-aws-prereqs
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Detailed requirements for deploying {product-title} using STS

[id="rosa-sts-aws-prereqs"]
= Detailed requirements for deploying OpenShift Container Platform using STS

[id="rosa-hcp-prereqs"]
= Detailed requirements for deploying OpenShift Container Platform

[role="_abstract"]
To deploy a OpenShift Container Platform cluster with {sts-first}, configure your AWS account with the required quotas, IAM permissions, and firewall egress rules, including an Amazon S3 gateway endpoint. Complete the requirements before deploying your cluster.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adocx
[id="rosa-account_{context}"]
= AWS account

[role="_abstract"]
You must have an AWS account with the following considerations to deploy a OpenShift Container Platform cluster.

* Your AWS account must allow sufficient quota to deploy your cluster.
* If your organization applies and enforces service control policies (SCPs), these policies must not be more restrictive than the roles and policies required by the cluster.
* You can deploy native AWS services within the same AWS account.
* Your account must have a service-linked role to allow the installation program to configure Elastic Load Balancing (ELB). See "Creating the Elastic Load Balancing (ELB) service-linked role" for more information.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-support-requirements_{context}"]
= Support requirements

[role="_abstract"]
To receive Red{nbsp}Hat support, your account must use a specific AWS plan and have the required permissions on your account.

* Red{nbsp}Hat recommends that the customer have at least Business Support from AWS.
* Red{nbsp}Hat may have permission from the customer to request AWS support on their behalf.
* Red{nbsp}Hat may have permission from the customer to request AWS resource limit increases on the customer's account.
* Red{nbsp}Hat manages the restrictions, limitations, expectations, and defaults for all OpenShift Container Platform clusters in the same manner, unless otherwise specified in this requirements section.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc

[id="rosa-security-requirements_{context}"]
= Security requirements

[role="_abstract"]
Before deploying your cluster, ensure that you plan for your egresses and ingresses to have access to certain domains and IP addresses.

* Red{nbsp}Hat must have ingress access to EC2 hosts and the API server from allow-listed IP addresses.
* Red{nbsp}Hat must have egress allowed to the domains documented in the "AWS Firewall prerequisites" section.
Clusters with {egress-zero} are exempt from this requirement.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-ocm-requirements_{context}"]
= Requirements for using {cluster-manager}

[role="_abstract"]
The following configuration details are required when using the {cluster-manager-url} or the CLI tools to manage your clusters.

[id="rosa-associating-concept_{context}"]
== AWS account association

When you provision OpenShift Container Platform using {cluster-manager} (`console.redhat.com`), you must associate the `ocm-role` and `user-role` IAM roles with your AWS account using your Amazon Resource Name (ARN). This association process is also known as _account linking_.

The `ocm-role` ARN is stored as a label in your Red{nbsp}Hat organization while the `user-role` ARN is stored as a label inside your Red{nbsp}Hat user account. Red{nbsp}Hat uses these ARN labels to confirm that the user is a valid account holder and that the correct permissions are available to perform provisioning tasks in the AWS account.

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
[id="rosa-associating-account_{context}"]
= Associating your AWS account with IAM roles

[role="_abstract"]
You can associate or link your AWS account with existing IAM roles by using the {rosa-cli-first}.

.Prerequisites

* You have an AWS account.
* You have the permissions required to install AWS account-wide roles. See the "Additional resources" of this section for more information.
* You have installed and configured the latest AWS CLI (`aws`) and {rosa-cli} on your installation host.
* You have created the `ocm-role` and `user-role` IAM roles, but have not yet linked them to your AWS account. You can check whether your IAM roles are already linked by running the following commands:
+
[source,terminal]
----
$ rosa list ocm-role
----
+
[source,terminal]
----
$ rosa list user-role
----
+
If `Yes` is displayed in the `Linked` column for both roles, you have already linked the roles to an AWS account.

.Procedure

. In the ROSA CLI, link your `ocm-role` resource to your Red{nbsp}Hat organization by using your Amazon Resource Name (ARN):
+
[NOTE]
====
You must have Red{nbsp}Hat Organization Administrator privileges to run the `rosa link` command. After you link the `ocm-role` resource with your AWS account, it takes effect and is visible to all users in the organization.
====
+
[source,terminal]
----
$ rosa link ocm-role --role-arn <arn>
----
+
For example:
+
[source,terminal]
----
I: Linking OCM role
? Link the '<AWS ACCOUNT ID>` role with organization '<ORG ID>'? Yes
I: Successfully linked role-arn '<AWS ACCOUNT ID>' with organization account '<ORG ID>'
----
. In the ROSA CLI, link your `user-role` resource to your Red{nbsp}Hat user account by using your Amazon Resource Name (ARN):
+
[source,terminal]
----
$ rosa link user-role --role-arn <arn>
----
+
For example:
+
[source,terminal]
----
I: Linking User role
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-User-Role-125' role with organization '<AWS ID>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-User-Role-125' with organization account '<AWS ID>'
----

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-associating-multiple-account_{context}"]
= Associating multiple AWS accounts with your Red{nbsp}Hat organization

[role="_abstract"]
You can associate multiple AWS accounts with your Red{nbsp}Hat organization. Associating multiple accounts lets you create OpenShift Container Platform clusters on any of the associated AWS accounts from your Red{nbsp}Hat organization.

With this capability, you can create clusters on different AWS profiles according to characteristics that make sense for your business, for example, by using one AWS profile for each region to create region-bound environments.

.Prerequisites

* You have an AWS account.
* You are using {cluster-manager-url} to create clusters.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest AWS CLI (`aws`) and {rosa-cli-first} on your installation host.
* You have created the `ocm-role` and `user-role` IAM roles for OpenShift Container Platform.

.Procedure

* To specify an AWS account profile when creating an {cluster-manager} role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> ocm-role
----

* To specify an AWS account profile when creating a user role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> user-role
----

* To specify an AWS account profile when creating the account roles:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> account-roles
----
+
[NOTE]
====
If you do not specify a profile, the default AWS profile and its associated AWS region are used.
====

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc

[id="rosa-requirements-deploying-in-opt-in-regions_{context}"]
= Requirements for deploying a cluster in an opt-in region

[role="_abstract"]
An AWS opt-in region is a region that is not enabled in your AWS account by default. If you want to deploy a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS) in an opt-in region, you must meet the following requirements:

* The region must be enabled in your AWS account. For more information about enabling opt-in regions, see Managing AWS Regions in the AWS documentation.
* The security token version in your AWS account must be set to version 2. You cannot use version 1 security tokens for opt-in regions.
+
[IMPORTANT]
====
Updating to security token version 2 can impact the systems that store the tokens, due to the increased token length. For more information, see the AWS documentation on setting STS preferences.
====

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc
[id="rosa-setting-the-aws-security-token-version_{context}"]
= Setting the AWS security token version

[role="_abstract"]
If you want to create a OpenShift Container Platform cluster with the AWS Security Token Service (STS) in an AWS opt-in region, you must set the security token version to version 2 in your AWS account.

.Prerequisites

* You have installed and configured the latest AWS CLI on your installation host.

.Procedure

. List the ID of the AWS account that is defined in your AWS CLI configuration:
+
[source,terminal]
----
$ aws sts get-caller-identity --query Account --output json
----
+
Ensure that the output matches the ID of the relevant AWS account.

. List the security token version that is set in your AWS account:
+
[source,terminal]
----
$ aws iam get-account-summary --query SummaryMap.GlobalEndpointTokenVersion --output json
----
+
For example:
+
[source,terminal]
----
1
----

. To update the security token version to version 2 for all regions in your AWS account, run the following command:
+
[source,terminal]
----
$ aws iam set-security-token-service-preferences --global-endpoint-token-version v2Token
----
+
[IMPORTANT]
====
Updating to security token version 2 can impact the systems that store the tokens, due to the increased token length. For more information, see the AWS documentation on setting STS preferences.
====

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
[id="rosa-security-groups-custom_{context}"]
= Additional custom security groups

[role="_abstract"]
When you create a cluster using an existing non-managed VPC, you
You
can add additional custom security groups during cluster creation. Custom security groups are subject to the following limitations:

* You must create the custom security groups in AWS before you create the cluster. For more information, see Amazon EC2 security groups for Linux instances.
* You must associate the custom security groups with the VPC that the cluster will be installed into. Your custom security groups cannot be associated with another VPC.
* You might need to request additional quota for your VPC if you are adding additional custom security groups. For information on AWS quota requirements for OpenShift Container Platform see _Required AWS service quotas_ in _Prepare your environment_. For information on requesting an AWS quota increase, see Requesting a quota increase.

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

// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc
// * rosa_planning/rosa-hcp-prereqs.adoc <-- this is a symlink
[id="rosa-hcp-firewall-prerequisites_{context}"]
= Firewall prerequisites for OpenShift Container Platform

[role="_abstract"]
If you are using a firewall to control egress traffic from OpenShift Container Platform, your Virtual Private Cloud (VPC) must be able to complete requests from the cluster to the Amazon S3 service, for example, via an Amazon S3 gateway. You must also configure your firewall to grant access to the following domain and port combinations.
//TODO OSDOCS-11789: From your deploy machine? From your cluster?

== Domains for installation packages and tools
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
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

|`quayio-production-s3.s3.amazonaws.com`
|443
|Provides core container images.

|`registry.redhat.io`
|443
|Provides core container images.

|`registry.access.redhat.com`
|443
|Required. Hosts all the container images that are stored on the Red{nbsp}Hat Ecosytem Catalog. Additionally, the registry provides access to the `odo` CLI tool that helps developers build on OpenShift and Kubernetes.

|`access.redhat.com`
|443
|Required. Hosts a signature store that a container client requires for verifying images when pulling them from `registry.access.redhat.com`.

|`api.openshift.com`
|443
|Required. Used to check for available updates to the cluster.

|`mirror.openshift.com`
|443
|Required. Used to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator (CVO) needs only a single functioning source.

|`api.openshiftusgov.com`
|443
|This is for GovCloud only.
|===

== Domains for telemetry
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
|`infogw.api.openshift.com`
|443
|Required for telemetry.

|`console.redhat.com`
|443
|Required. Allows interactions between the cluster and OpenShift Console Manager to enable functionality, such as scheduling upgrades.

|`sso.redhat.com`
|443
|Required. The `https://console.redhat.com/openshift` site uses authentication from `sso.redhat.com` to download the pull secret and use Red{nbsp}Hat SaaS solutions to facilitate monitoring of your subscriptions, cluster inventory, chargeback reporting, etc.

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

Managed clusters require enabling telemetry to allow Red{nbsp}Hat to react more quickly to problems, better support the customers, and better understand how product upgrades impact clusters.
For more information about how remote health monitoring data is used by Red{nbsp}Hat, see _About remote health monitoring_ in the _Additional resources_ section.

== Domains for Amazon Web Services (AWS) APIs
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`sts.<aws_region>.amazonaws.com`
|443
|Required. Used to access the AWS Secure Token Service (STS) regional endpoint. Ensure that you replace `<aws-region>` with the region that your cluster is deployed in. This can also be accomplished by configuring a private interface endpoint in your AWS Virtual Private Cloud (VPC) to the regional AWS STS endpoint.
|===

== Domains for your workload

Your workload may require access to other sites that provide resources for programming languages or frameworks.

* Allow access to sites that provide resources required by your builds.
* Allow access to outbound URLs required for your workload, for example, OpenShift Outbound URLs to Allow.

== Optional domains to enable third-party content
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
|`registry.connect.redhat.com`
| 443
| Optional. Required for all third-party-images and certified operators.

|`rhc4tp-prod-z8cxf-image-registry-us-east-1-evenkyleffocxqvofrk.s3.dualstack.us-east-1.amazonaws.com`
| 443
| Optional. Provides access to container images hosted on `registry.connect.redhat.com`.

|`oso-rhc4tp-docker-registry.s3-us-west-2.amazonaws.com`
| 443
| Optional. Required for Sonatype Nexus, F5 Big IP operators.
|===

[id="firewall-cli-bastion_{context}"]
== Outbound firewall rules for the {rosa-cli} for clusters with egress zero

If you use a bastion host to connect to a private cluster with egress zero, you must add the following rules to your firewall so that it can connect and authenticate to the cluster.

[cols="6,1,6,6",options="header"]
|===
|Domain | Port | From/To | Function
|`sso.redhat.com`
|443
|ROSA CLI running on bastion host
|The OpenShift console uses authentication from `sso.redhat.com` to download the pull secret and use Red Hat SaaS solutions to facilitate monitoring of your subscriptions, cluster inventory, chargeback reporting, etc.

|`api.openshift.com`
|443
|ROSA CLI running on bastion host
|Required for registering a OpenShift Container Platform cluster into {hybrid-console}.

|`iam.amazonaws.com`
|443
|ROSA CLI running on bastion host
|Used for creating IAM roles and attaching permissions.

|`servicequotas.<your region>.amazonaws.com`
|443
|ROSA CLI running on bastion host
|Checks AWS quotas to ensure they satisfy ROSA installation requirements. Alternatively, you can create a VPC endpoint for servicequota service to avoid whitelisting this URL from your firewall.

|`sts.<your region>.amazonaws.com`
|443
|ROSA CLI running on bastion host
|Used to get short-lived token to access AWS service. Alternatively, you can create a VPC endpoint for STS service to avoid whitelisting this url from your firewall.

|`ec2.<your region>.amazonaws.com`
|443
|ROSA CLI running on bastion host
|Used to retrieve EC2 instance related information such as subnets. Alternatively, you can create a VPC endpoint for EC2 service to avoid whitelisting this URL from your firewall.
|===

[id="firewall-hcm-bastion_{context}"]
== Outbound firewall rules from {hybrid-console} for clusters with egress zero
[cols="6,1,6,6",options="header"]
|===
|Domain | Port | From/To | Function

|`sts.<your region>.amazonaws.com`
|443
|OpenShift Container Platform cluster
|Used to access the AWS Secure Token Service (STS) regional endpoint to retrieve a short-lived token to access AWS services. Alternatively, you can create a VPC endpoint for STS service to avoid whitelisting this URL from your firewall.

|`console.redhat.com`
|443
|Any browser to access {hybrid-console}
|To manage a OpenShift Container Platform cluster from {hybrid-console-second}.

|`sso.redhat.com`
|443
|Any browser to access {hybrid-console}
|The {hybrid-console} site uses authentication from `sso.redhat.com` to download the pull secret and use Red Hat SaaS solutions to facilitate monitoring of your subscriptions, cluster inventory, chargeback reporting, etc.
|===

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc

[id="rosa-hcp-vpc-subnet-tagging_{context}"]
= Tagging your subnets

[role="_abstract"]
If you created your own VPC to create a OpenShift Container Platform cluster, you must tag your VPC subnets.
Before you can use your VPC to create a OpenShift Container Platform cluster, you must tag your VPC subnets.
Automated service preflight checks verify that these resources are tagged correctly before you can use these resources for a cluster.

.Required subnet tags
[cols="3a,8a,8a", options="header"]
|===
| Resource
| Key
| Value

| Public subnet
| `kubernetes.io/role/elb`
| `1` (or no value)

| Private subnet
| `kubernetes.io/role/internal-elb`
| `1` (or no value)

|===

[NOTE]
====
You must tag at least one private subnet and, if applicable, one public subnet.
====

.Prerequisites

* You have created a VPC.
* You have installed the `aws` CLI.

.Procedure

* Tag your resources in your terminal by running the following commands:
.. For public subnets, run:
+
[source,terminal]
----
$ aws ec2 create-tags --resources <public-subnet-id> --region <aws_region> --tags Key=kubernetes.io/role/elb,Value=1
----
.. For private subnets, run:
+
[source,terminal]
----
$ aws ec2 create-tags --resources <private-subnet-id> --region <aws_region> --tags Key=kubernetes.io/role/internal-elb,Value=1
----

.Verification

* Verify that the tag is correctly applied by running the following command:
+
[source,terminal]
----
$ aws ec2 describe-tags --filters "Name=resource-id,Values=<subnet_id>"
----
+
For example:
+
[source,text]
----
TAGS    Name                    <subnet-id>        subnet  <prefix>-subnet-public1-us-east-1a
TAGS    kubernetes.io/role/elb  <subnet-id>        subnet  1
----

//Adding conditions around these in case the Additional resources don't get ported to HCP or have different file names / locations; keeping all included for now
[role="_additional-resources"]
[id="additional-resources_aws-prerequisites_{context}"]
== Additional resources

* Cluster-specific Operator IAM role reference
* Account-wide IAM role and policy reference
* OpenShift Container Platform IAM role resources
* Required IAM roles and resources
* About remote health monitoring
* SRE access to all OpenShift Container Platform clusters
* Configuring custom domains for applications
* Instance types
* Instance types
* SRE and service account access
//Omitted until Applications has been ported for HCP
//* xref ../applications/deployments/rosa-config-custom-domains-applications.adoc#rosa-applications-config-custom-domains[Configuring custom domains for applications]
* Review the required AWS service quotas
