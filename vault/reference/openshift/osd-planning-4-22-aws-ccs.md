---
title: "Customer Cloud Subscriptions on AWS"
type: reference
domain: openshift
slug: osd-planning-4-22-aws-ccs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_planning/aws-ccs
version: 4.22
family: osd_planning
documentKind: "Documentation"
---

# Customer Cloud Subscriptions on AWS

[id="aws-ccs"]
= Customer Cloud Subscriptions on AWS

[role="_abstract"]
OpenShift Container Platform provides a Customer Cloud Subscription (CCS) model that allows Red Hat to deploy and manage clusters into a customer’s existing Amazon Web Service (AWS) account.

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-understand_{context}"]
= Understanding Customer Cloud Subscriptions on AWS

[role="_abstract"]
To deploy OpenShift Container Platform into your existing Amazon Web Services (AWS) account using the Customer Cloud Subscription (CCS) model, Red Hat requires several prerequisites be met.

Red Hat recommends the usage of an AWS Organization to manage multiple AWS accounts. The AWS Organization, managed by the customer, hosts multiple AWS accounts. There is a root account in the organization that all accounts will refer to in the account hierarchy.

It is recommended for the OpenShift Container Platform cluster using a CCS model to be hosted in an AWS account within an AWS Organizational Unit. A service control policy (SCP) is created and applied to the AWS Organizational Unit that manages what services the AWS sub-accounts are permitted to access. The SCP applies only to available permissions within a single AWS account for all AWS sub-accounts within the Organizational Unit. It is also possible to apply a SCP to a single AWS account. All other accounts in the customer’s AWS Organization are managed in whatever manner the customer requires. Red Hat Site Reliability Engineers (SRE) will not have any control over SCPs within the AWS Organization.

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-customer-requirements_{context}"]
= Customer requirements

[role="_abstract"]
OpenShift Container Platform clusters using a Customer Cloud Subscription (CCS) model on Amazon Web Services (AWS) must meet several prerequisites before they can be deployed.

[id="ccs-requirements-account_{context}"]
== Account

* The customer ensures that AWS limits are sufficient to support OpenShift Container Platform provisioned within the customer-provided AWS account.

* The customer-provided AWS account should be in the customer's AWS Organization with the applicable service control policy (SCP) applied.
+
[NOTE]
====
It is not a requirement that the customer-provided account be within an AWS Organization or for the SCP to be applied, however Red Hat must be able to perform all the actions listed in the SCP without restriction.
====

* The customer-provided AWS account must not be transferable to Red Hat.

* The customer may not impose AWS usage restrictions on Red Hat activities. Imposing restrictions severely hinders Red Hat's ability to respond to incidents.

* Red Hat deploys monitoring into AWS to alert Red Hat when a highly privileged account, such as a root account, logs into the customer-provided AWS account.

* The customer can deploy native AWS services within the same customer-provided AWS account.
+
[NOTE]
====
Customers are encouraged, but not mandated, to deploy resources in a Virtual Private Cloud (VPC) separate from the VPC hosting OpenShift Container Platform and other Red Hat supported services.
====

[id="ccs-requirements-access_{context}"]
== Access requirements

* To appropriately manage the OpenShift Container Platform service, Red Hat must have the `AdministratorAccess` policy applied to the administrator role at all times.
+
[NOTE]
====
This policy only provides Red Hat with permissions and capabilities to change resources in the customer-provided AWS account.
====

* Red Hat must have AWS console access to the customer-provided AWS account. This access is protected and managed by Red Hat.

* The customer must not utilize the AWS account to elevate their permissions within the OpenShift Container Platform cluster.

* Actions available in {cluster-manager-url} must not be directly performed in the customer-provided AWS account.

[id="ccs-requirements-support_{context}"]
== Support requirements

* Red Hat recommends that the customer have at least Business Support from AWS.

* Red Hat has authority from the customer to request AWS support on their behalf.

* Red Hat has authority from the customer to request AWS resource limit increases on the customer-provided account.

* Red Hat manages the restrictions, limitations, expectations, and defaults for all OpenShift Container Platform clusters in the same manner, unless otherwise specified in this requirements section.

[id="ccs-requirements-security_{context}"]
== Security requirements

* The customer-provided IAM credentials must be unique to the customer-provided AWS account and must not be stored anywhere in the customer-provided AWS account.

* Volume snapshots will remain within the customer-provided AWS account and customer-specified region.

* Red Hat must have ingress access to EC2 hosts and the API server through white-listed Red Hat machines.

* Red Hat must have egress allowed to forward system and audit logs to a Red Hat managed central logging stack.

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-customer-procedure_{context}"]
= Required customer procedure

// TODO: Better procedure heading that tells you what this is doing
[role="_abstract"]
The Customer Cloud Subscription (CCS) model allows Red Hat to deploy and manage OpenShift Container Platform into a customer’s Amazon Web Services (AWS) account. Red Hat requires several prerequisites in order to provide these services.

.Procedure

. If the customer is using AWS Organizations, you must either use an AWS account within your organization or create a new one.

. To ensure that Red Hat can perform necessary actions, you must either create a service control policy (SCP) or ensure that none is applied to the AWS account.

. Attach the SCP to the AWS account.

. Within the AWS account, you must create an `osdCcsAdmin` IAM user with the following requirements:
** This user needs at least *Programmatic access* enabled.
** This user must have the `AdministratorAccess` policy attached to it.

. Provide the IAM user credentials to Red Hat.
** You must provide the *access key ID* and *secret access key* in {cluster-manager-url}.

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-scp_{context}"]
= Minimum required service control policy (SCP)

[role="_abstract"]
Service control policy (SCP) management is the responsibility of the customer. These policies are maintained in the AWS Organization and control what services are available within the attached AWS accounts.

[cols="2a,2a,2a,2a",options="header"]

|===
| Required/optional
| Service
| Actions
| Effect

.15+| Required
|Amazon EC2 | All |Allow
|Amazon EC2 Auto Scaling | All |Allow
|Amazon S3| All |Allow
|Identity And Access Management | All |Allow
|Elastic Load Balancing | All |Allow
|Elastic Load Balancing V2| All |Allow
|Amazon CloudWatch | All |Allow
|Amazon CloudWatch Events | All |Allow
|Amazon CloudWatch Logs | All |Allow
|AWS Support | All |Allow
|AWS Key Management Service | All |Allow
|AWS Security Token Service | All |Allow
|AWS Resource Tagging | All |Allow
|AWS Route53 DNS | All |Allow
|AWS Service Quotas | ListServices

GetRequestedServiceQuotaChange

GetServiceQuota

RequestServiceQuotaIncrease

ListServiceQuotas
| Allow

.3+|Optional

| AWS Billing
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

// TODO: Need some sort of intro into whatever this is
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "autoscaling:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "events:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "support:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sts:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "tag:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "servicequotas:ListServices",
                "servicequotas:GetRequestedServiceQuotaChange",
                "servicequotas:GetServiceQuota",
                "servicequotas:RequestServiceQuotaIncrease",
                "servicequotas:ListServiceQuotas"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
----

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-iam_{context}"]
= Red Hat managed IAM references for AWS

[role="_abstract"]
Red Hat is responsible for creating and managing the following Amazon Web Services (AWS) resources: IAM policies, IAM users, and IAM roles.

[id="aws-policy-iam-policies_{context}"]
== IAM policies

[NOTE]
====
IAM policies are subject to modification as the capabilities of OpenShift Container Platform change.
====

* The `AdministratorAccess` policy is used by the administration role. This policy provides Red Hat the access necessary to administer the OpenShift Container Platform cluster in the customer-provided AWS account.
+
[source,json]
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

* The `CustomerAdministratorAccess` role provides the customer access to administer a subset of services within the AWS account. At this time, the following are allowed:

** VPC Peering
** VPN Setup
** Direct Connect (only available if granted through the service control policy)
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AttachVpnGateway",
                "ec2:DescribeVpnConnections",
                "ec2:AcceptVpcPeeringConnection",
                "ec2:DeleteVpcPeeringConnection",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:CreateVpnConnectionRoute",
                "ec2:RejectVpcPeeringConnection",
                "ec2:DetachVpnGateway",
                "ec2:DeleteVpnConnectionRoute",
                "ec2:DeleteVpnGateway",
                "ec2:DescribeVpcs",
                "ec2:CreateVpnGateway",
                "ec2:ModifyVpcPeeringConnectionOptions",
                "ec2:DeleteVpnConnection",
                "ec2:CreateVpcPeeringConnection",
                "ec2:DescribeVpnGateways",
                "ec2:CreateVpnConnection",
                "ec2:DescribeRouteTables",
                "ec2:CreateTags",
                "ec2:CreateRoute",
          "directconnect:*"
            ],
            "Resource": "*"
        }
    ]
}
----

* If enabled, the `BillingReadOnlyAccess` role provides read-only access to view billing and usage information for the account.
+
Billing and usage access is only granted if the root account in the AWS Organization has it enabled. This is an optional step the customer must perform to enable read-only billing and usage access and does not impact the creation of this profile and the role that uses it. If this role is not enabled, users will not see billing and usage information. See this tutorial on how to enable access to billing data.
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-portal:ViewAccount",
                "aws-portal:ViewBilling"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="aws-policy-iam-users_{context}"]
== IAM users

The `osdManagedAdmin` user is created immediately after taking control of the customer-provided AWS account. This is the user that will perform the OpenShift Container Platform cluster installation.

[id="aws-policy-iam-roles_{context}"]
== IAM roles

* The `network-mgmt` role provides customer-federated administrative access to the AWS account through a separate AWS account. It also has the same access as a read-only role. The `network-mgmt` role only applies to non-Customer Cloud Subscription (CCS) clusters. The following policies are attached to the role:

** AmazonEC2ReadOnlyAccess
** CustomerAdministratorAccess

* The `read-only` role provides customer-federated read-only access to the AWS account through a separate AWS account. The following policies are attached to the role:

** AWSAccountUsageReportAccess
** AmazonEC2ReadOnlyAccess
** AmazonS3ReadOnlyAccess
** IAMReadOnlyAccess
** BillingReadOnlyAccess

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="ccs-aws-provisioned_{context}"]
= Provisioned AWS Infrastructure

[role="_abstract"]
This is an overview of the provisioned Amazon Web Services (AWS) components on a deployed OpenShift Container Platform cluster. For a more detailed listing of all provisioned AWS components, see the {OCP} documentation.

[id="aws-policy-ec2_{context}"]
== AWS Elastic Computing (EC2) instances

AWS EC2 instances are required to deploy the control plane and data plane functions of OpenShift Container Platform in the AWS public cloud. Instance types might vary for control plane and infrastructure nodes depending on worker node count.

* Single availability zone
** 3 m5.2xlarge minimum (control plane nodes)
** 2 r5.xlarge minimum (infrastructure nodes)
** 2 m5.xlarge minimum but highly variable (worker nodes)

* Multiple availability zones
** 3 m5.2xlarge minimum (control plane nodes)
** 3 r5.xlarge minimum (infrastructure nodes)
** 3 m5.xlarge minimum but highly variable (worker nodes)

[id="aws-policy-ebs-storage_{context}"]
== AWS Elastic Block Store (EBS) storage

Amazon EBS block storage is used for both local node storage and persistent volume storage.

Volume requirements for each EC2 instance:

- Control plane volumes
* Size: 350 GB
* Type: io1
* Input/output operations per second: 1000

- Infrastructure volumes
* Size: 300 GB
* Type: gp2
* Input/output operations per second: 900

- Worker volumes
* Size: 300 GB
* Type: gp2
* Input/output operations per second: 900

[id="aws-policy-elastic-load-balancers_{context}"]
== Elastic Load Balancing (ELB) load balancers

Up to two Network Load Balancers for API and up to two Classic Load Balancers for application router. For more information, see the ELB documentation for AWS.

[id="aws-policy-s3-storage_{context}"]
== S3 storage
The image registry and Elastic Block Store (EBS) volume snapshots are backed by AWS S3 storage. Pruning of resources is performed regularly to optimize S3 usage and cluster performance.

[NOTE]
====
Two buckets are required with a typical size of 2 TB each.
====

[id="aws-policy-vpc_{context}"]
== VPC
Customers should expect to see one VPC per cluster. Additionally, the VPC needs the following configurations:

* *Subnets*: Two subnets for a cluster with a single availability zone, or six subnets for a cluster with multiple availability zones.
+
[NOTE]
====
A *public subnet* connects directly to the internet through an internet gateway. A *private subnet* connects to the internet through a network address translation (NAT) gateway.
====
+
* *Route tables*: One route table per private subnet, and one additional table per cluster.

* *Internet gateways*: One Internet Gateway per cluster.

* *NAT gateways*: One NAT Gateway per public subnet.

== Sample VPC Architecture

image::VPC-Diagram.png[VPC Reference Architecture]

[id="aws-policy-security-groups_{context}"]
== Security groups

AWS security groups provide security at the protocol and port-access level; they are associated with EC2 instances and Elastic Load Balancing. Each security group contains a set of rules that filter traffic coming in and out of an EC2 instance. You must ensure the ports required for the {OCP} installation are open on your network and configured to allow access between hosts.

[id="osd-security-groups-custom_{context}"]
== Additional custom security groups
When you create a cluster by using a non-managed VPC, you can add custom security groups during cluster creation. Custom security groups are subject to the following limitations:

* You must create the custom security groups in AWS before you create the cluster. For more information, see Amazon EC2 security groups for Linux instances.
* You must associate the custom security groups with the VPC that the cluster will be installed into. Your custom security groups cannot be associated with another VPC.
* You might need to request additional quota for your VPC if you are adding additional custom security groups. For information on requesting an AWS quota increase, see Requesting a quota increase.

[id="aws-ccs-networking-prereqs_{context}"]
== Networking prerequisites

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

// Module included in the following assemblies:
//
// * osd_planning/aws-ccs.adoc

[id="aws-limits_{context}"]
= AWS account limits

[role="_abstract"]
The OpenShift Container Platform cluster uses a number of Amazon Web Services (AWS) components, and the default service limits affect your ability to install OpenShift Container Platform clusters. If you use certain cluster configurations, deploy your cluster in certain AWS regions, or run multiple clusters from your account, you might need to request additional resources for your AWS account.

The following table summarizes the AWS components whose limits can impact your ability to install and run OpenShift Container Platform clusters.

[cols="3a,3a,3a,8a",options="header"]
|===
|Component |Number of clusters available by default| Default AWS limit |Description

|Instance Limits
|Varies
|Varies
|At a minimum, each cluster creates the following instances:

* One bootstrap machine, which is removed after installation
* Three control plane nodes
* Two infrastructure nodes for a single availability zone; three infrascture nodes for multi-availability zones
* Two worker nodes for a single availability zone; three worker nodes for multi-availability zones

These instance type counts are within a new account's default limit. To deploy more worker nodes, deploy large workloads, or use a different instance type, review your account limits to ensure that your cluster can deploy the machines that you need.

In most regions, the bootstrap and worker machines uses an `m4.large` machines and the control plane machines use `m4.xlarge` instances. In some regions, including all regions that do not support these instance types, `m5.large` and `m5.xlarge` instances are used instead.

|Elastic IPs (EIPs)
|0 to 1
|5 EIPs per account
|To provision the cluster in a highly available configuration, the installation program creates a public and private subnet for each availability zone within a region. Each private subnet requires a NAT Gateway, and each NAT gateway requires a separate
elastic IP. Review the AWS region map to determine how many availability zones are in each region. To take advantage of the default high availability, install the cluster in a region with at least three availability zones. To install a cluster in a region with more than five availability zones, you must increase the EIP limit.

// TODO: The above elastic IP link is redirected. Find new link. Is it https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html ?

[IMPORTANT]
====
To use the `us-east-1` region, you must increase the EIP limit for your account.
====

|Virtual Private Clouds (VPCs)
|5
|5 VPCs per region
|Each cluster creates its own VPC.

|Elastic Load Balancing (ELB)
|3
|20 per region
|By default, each cluster creates internal and external Network Load Balancers for the primary API server and a single Classic Load Balancer for the router. Deploying more Kubernetes LoadBalancer Service objects will create additional load balancers.

|NAT Gateways
|5
|5 per availability zone
|The cluster deploys one NAT gateway in each availability zone.

|Elastic Network Interfaces (ENIs)
|At least 12
|350 per region
|The default installation creates 21 ENIs and an ENI for each availability zone in your region. For example, the `us-east-1` region contains six availability zones, so a cluster that is deployed in that zone uses 27 ENIs. Review the AWS region map to determine how many availability zones are in each region.

Additional ENIs are created for additional machines and load balancers that are created by cluster usage and deployed workloads.

|VPC Gateway
|20
|20 per account
|Each cluster creates a single VPC Gateway for S3 access.

|S3 buckets
|99
|100 buckets per account
|Because the installation process creates a temporary bucket and the registry component in each cluster creates a bucket, you can create only 99 OpenShift Container Platform clusters per AWS account.

|Security Groups
|250
|2,500 per account
|Each cluster creates 10 distinct security groups.
|===
