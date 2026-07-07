---
title: "Tutorial: What is ROSA"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-what-is-rosa
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-what-is-rosa
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: What is ROSA

[id="cloud-experts-getting-started-what-is-rosa"]
= Tutorial: What is ROSA

[role="_abstract"]
Red{nbsp}Hat OpenShift Service on AWS (ROSA) is a fully-managed turnkey application platform that allows you to focus on what matters most, delivering value to your customers by building and deploying applications. Red{nbsp}Hat and AWS SRE experts manage the underlying platform so you do not have to worry about infrastructure management. ROSA provides seamless integration with a wide range of AWS compute, database, analytics, machine learning, networking, mobile, and other services to further accelerate the building and delivering of differentiating experiences to your customers.

ROSA makes use of AWS Security Token Service (STS) to obtain credentials to manage infrastructure in your AWS account. AWS STS is a global web service that creates temporary credentials for IAM users or federated users. ROSA uses this to assign short-term, limited-privilege, security credentials. These credentials are associated with IAM roles that are specific to each component that makes AWS API calls. This method aligns with the principals of least privilege and secure practices in cloud service resource management. The ROSA command-line interface (CLI) tool manages the STS credentials that are assigned for unique tasks and takes action on AWS resources as part of OpenShift functionality.
//For a detailed explanation, see "ROSA with STS Explained" (add xref when page is migrated).

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc
[id="cloud-experts-key-features-rosa_{context}"]
= Key features of OpenShift Container Platform

[role="_abstract"]
The following sections show the key features of using OpenShift Container Platform. OpenShift Container Platform clusters also offer:

* *Native AWS service:* Access and use Red{nbsp}Hat OpenShift on-demand with a self-service onboarding experience through the AWS management console.
* *Flexible, consumption-based pricing:* Scale to your business needs and pay as you go with flexible pricing and an on-demand hourly or annual billing model.
* *Single bill for Red{nbsp}Hat OpenShift and AWS usage:* Customers will receive a single bill from AWS for both Red{nbsp}Hat OpenShift and AWS consumption.
* *Fully integrated support experience:* Installation, management, maintenance, and upgrades are performed by Red{nbsp}Hat site reliability engineers (SREs) with joint Red{nbsp}Hat and Amazon support and a 99.95% service-level agreement (SLA).
* *AWS service integration:* AWS has a robust portfolio of cloud services, such as compute, storage, networking, database, analytics, and machine learning. All of these services are directly accessible through OpenShift Container Platform. This makes it easier to build, operate, and scale globally and on-demand through a familiar management interface.
* *Maximum Availability:* Deploy clusters across multiple availability zones in supported regions to maximize availability and maintain high availability for your most demanding mission-critical applications and data.
* *Cluster node scaling:* Easily add or remove compute nodes to match resource demand.
* *Optimized clusters:* Choose from memory-optimized, compute-optimized, or general purpose EC2 instance types with clusters sized to meet your needs.
* *Global availability:* Refer to the _Additional Resources_ for information on availability regions.

== OpenShift Container Platform and Kubernetes
In OpenShift Container Platform, everything you need to deploy and manage containers is bundled, including container management, Operators, networking, load balancing, service mesh, CI/CD, firewall, monitoring, registry, authentication, and authorization capabilities. These components are tested together for unified operations as a complete platform. Automated cluster operations, including over-the-air platform upgrades, further enhance your Kubernetes experience.

== Basic responsibilities
In general, cluster deployment and upkeep is Red{nbsp}Hat's or AWS's responsibility, while applications, users, and data is the customer's responsibility.

== Roadmap and feature requests
Visit the OpenShift Container Platform roadmap to stay up-to-date with the status of features currently in development. Open a new issue if you have any suggestions for the product team.

== AWS region availability
See the _Additional Resources_ for the product regional availability page for an up-to-date view of where OpenShift Container Platform is available.

== Compliance certifications
OpenShift Container Platform is currently compliant with SOC-2 type 2, SOC 3, ISO-27001, ISO 27017, ISO 27018, HIPAA, GDPR, and PCI-DSS. We are also currently working towards FedRAMP High.

== Administrators
A OpenShift Container Platform customer's administrator can manage users and quotas in addition to accessing all user-created projects.

== OpenShift versions and upgrades
OpenShift Container Platform is a managed service which is based on OpenShift Container Platform. You can view the current version and life cycle dates in the _Additional resources_.

Customers can upgrade to the newest version of OpenShift and use the features from that version of OpenShift. Not all OpenShift features are be available on OpenShift Container Platform. See the Service Definition page in the _Additional resources_ for more information.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc

[id="cloud-experts-key-features-rosa-nodes_{context}"]
= Nodes

[role="_abstract"]
The following covers the various aspects about OpenShift Container Platform cluster nodes, including worker node requirements, operating system, supported instances, and scaling capabilities.

== Worker nodes across multiple AWS regions
All nodes in a OpenShift Container Platform cluster must be located in the same AWS region. For clusters configured for multiple availability zones, control plane nodes and worker nodes will be distributed across the availability zones.

== Minimum number of worker nodes
For a OpenShift Container Platform cluster, the minimum is 2 worker nodes for single availability zone and 3 worker nodes for multiple availability zones.

== Underlying node operating system
As with all OpenShift v4.x offerings, the control plane, infra and worker nodes run Red{nbsp}Hat Enterprise Linux CoreOS (RHCOS).

== Node hibernation or shut-down
At this time, OpenShift Container Platform does not have a hibernation or shut-down feature for nodes. The shutdown and hibernation feature is an OpenShift platform feature that is not yet mature enough for widespread cloud services use.

== Supported instances for worker nodes
For a complete list of supported instances for worker nodes see the _Additional Resources_ for the AWS instance types. Spot instances are also supported.

== Node autoscaling
Autoscaling allows you to automatically adjust the size of the cluster based on the current workload.

== Maximum number of worker nodes
The maximum number of worker nodes in OpenShift Container Platform clusters versions 4.14.14 and later is 249. For earlier versions, the limit is 180 nodes.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc

[id="cloud-experts-key-features-rosa-support_{context}"]
= Support

[role="_abstract"]
You can open a ticket directly from the {cluster-manager-url} or visit the Red{nbsp}Hat Customer Portal to search or browse through the Red{nbsp}Hat knowledge base of articles and solutions relating to Red{nbsp}Hat products or submit a support case to Red{nbsp}Hat Support.

You can open a ticket directly from the {cluster-manager-url}.

You can also visit the Red{nbsp}Hat Customer Portal to search or browse through the Red{nbsp}Hat knowledge base of articles and solutions relating to Red{nbsp}Hat products or submit a support case to Red{nbsp}Hat Support.

== Limited support
If a OpenShift Container Platform cluster is not upgraded before the "end of life" date, the cluster continues to operate in a limited support status. The SLA for that cluster will no longer be applicable, but you can still get support for that cluster.

Additional support resources:

* Red{nbsp}Hat Support
* AWS Support
+
AWS support customers must have a valid AWS support contract.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc

[id="cloud-experts-key-features-rosa-sla_{context}"]
= Service-level agreement (SLA)

[role="_abstract"]
See the _Additional resources_ for the OpenShift Container Platform service-level agreement.

See the _Additional resources_ for the OpenShift Container Platform service-level agreement.

== Notifications and communication
Red{nbsp}Hat will provide notifications regarding new Red{nbsp}Hat and AWS features, updates, and scheduled maintenance through email and the {hybrid-console-second} service log.

== Open Service Broker for AWS (OBSA)
You can use OSBA with OpenShift Container Platform. However, the preferred method is the more recent AWS Controller for Kubernetes. See Open Service Broker for AWS for more information on OSBA.

== Offboarding
Customers can stop using OpenShift Container Platform at any time and move their applications to on-premise, a private cloud, or other cloud providers. Standard reserved instances (RI) policy applies for unused RI.

== Authentication
OpenShift Container Platform supports the following authentication mechanisms: OpenID Connect (a profile of OAuth2), Google OAuth, GitHub OAuth, GitLab, and LDAP.

== SRE cluster access
All SRE cluster access is secured by MFA.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc

[id="cloud-experts-key-features-rosa-encryption_{context}"]
= Encryption

[role="_abstract"]
OpenShift Container Platform uses encryption keys stored in KMS to encrypt EBS volumes, with options for customer-provided keys, data encryption at rest, and etcd encryption.

== Encryption keys
OpenShift Container Platform uses a key stored in KMS to encrypt EBS volumes. Customers also have the option to provide their own KMS keys at cluster creation.

== KMS keys
If you specify a KMS key, the control plane, infrastructure and worker node root volumes and the persistent volumes are encrypted with the key.

== Data encryption
By default, there is encryption at rest. The AWS Storage platform automatically encrypts your data before persisting it and decrypts the data before retrieval. See AWS EBS Encryption for more details.

You can also encrypt etcd in the cluster, combining it with AWS storage encryption. This results in double the encryption which adds up to a 20% performance hit.

== etcd encryption
etcd encryption can only be enabled at cluster creation.

[NOTE]
====
etcd encryption incurs additional overhead with negligible security risk mitigation.
====

== etcd encryption configuration
etcd encryption is configured the same as in OpenShift Container Platform. The aescbc cypher is used and the setting is patched during cluster deployment. For more details, see the Kubernetes documentation.

== Multi-region KMS keys for EBS encryption
Currently, the {rosa-cli} does not accept multi-region KMS keys for EBS encryption. This feature is in our backlog for product updates. The {rosa-cli} accepts single region KMS keys for EBS encryption if it is defined at cluster creation.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-what-is-rosa.adoc

[id="cloud-experts-key-features-rosa-infrastructure_{context}"]
= Infrastructure

[role="_abstract"]
OpenShift Container Platform uses several different cloud services such as virtual machines, storage, and load balancers. This section covers infrastructure components, credential methods, storage, networking, monitoring, and other infrastructure-related features.

== Infrastructure
OpenShift Container Platform uses several different cloud services such as virtual machines, storage, and load balancers. You can see a defined list on the AWS prerequisites page in the _Additional resources_.
// This section needs to remain hidden until the HCP migration is published
// OpenShift Container Platform uses several different cloud services such as virtual machines, storage, and load balancers. You can see a defined list in the AWS prerequisites.

== Credential methods
There are two credential methods to grant Red{nbsp}Hat the permissions needed to perform the required actions in your AWS account: AWS with STS or an IAM user with admin permissions. AWS with STS is the preferred method, and the IAM user method will eventually be deprecated. AWS with STS better aligns with the principles of least privilege and secure practices in cloud service resource management.
//See the section [OpenShift Container Platform with STS Explained] section for a detailed explanation.

== Prerequisite permission or failure errors
Check for a newer version of the {rosa-cli}. Every release of the {rosa-cli} is located in two places: Github and the Red{nbsp}Hat signed binary releases.

== Storage
See the _Additional resources_ for the Storage documentation. OpenShift includes the CSI driver for AWS EFS.

== Using a VPC
At installation you can select to deploy to an existing VPC or bring your own VPC. You can then select the required subnets and provide a valid CIDR range that encompasses the subnets for the installation program when using those subnets.

OpenShift Container Platform allows multiple clusters to share the same VPC. The number of clusters on one VPC is limited by the remaining AWS resource quota and CIDR ranges that cannot overlap.

== Network plugin
OpenShift Container Platform uses the OpenShift OVN-Kubernetes default CNI network provider.

== Cross-namespace networking
Cluster admins can customize, and deny, cross-namespace on a project basis using NetworkPolicy objects. Refer to  for more information.

== Using Prometheus and Grafana
You can use Prometheus and Grafana to monitor containers and manage capacity using OpenShift User Workload Monitoring. This is a check-box option in the {cluster-manager-url}.

== Audit logs output from the cluster control-plane
If the Cluster Logging Operator Add-on has been added to the cluster then audit logs are available through CloudWatch. If it has not, then a support request would allow you to request some audit logs. Small targeted and time-boxed logs can be requested for export and sent to a customer. The selection of audit logs available are at the discretion of SRE in the category of platform security and compliance. Requests for exports of a cluster's entirety of logs will be rejected.

== AWS Permissions Boundary
You can use an AWS Permissions Boundary around the policies for your cluster.

== AMI
OpenShift Container Platform worker nodes use a different AMI from OSD and OpenShift Container Platform. Control Plane and Infra node AMIs are common across products in the same version.

== Cluster backups
OpenShift Container Platform STS clusters do not have backups. Users must have their own backup policies for applications and data.

== Custom domain
You can define a custom domain for your applications.

== OpenShift Container Platform domain certificates
Red{nbsp}Hat infrastructure (Hive) manages certificate rotation for default application ingress.

== Disconnected environments
OpenShift Container Platform does not support an air-gapped, disconnected environment. The OpenShift Container Platform cluster must have egress to the internet to access our registry, S3, and send metrics. The service requires a number of egress endpoints.
Ingress can be limited to a PrivateLink for Red{nbsp}Hat SREs and a VPN for customer access.

//== Creating your first ROSA cluster

//Watch this demo for a short preview of the cluster deployment process:
//Red{nbsp}Hat product page
* AWS product page
* Red{nbsp}Hat Customer Portal
* AWS ROSA getting started guide
* About OpenShift Container Platform
* ROSA service definition
* ROSA responsibility assignment matrix
* Understanding Process and Security
* About Availability
* Backup policy
* Updates Lifecycle
* Configuring multitenant isolation with network policy
* Configuring custom domains for applications
* OpenShift Container Platform regional availability
* Responsibility matrix
* Product regional availability
* AWS instance types
* About autoscaling nodes on a cluster
* List of the account-wide and per-cluster roles for OpenShift Container Platform
* OpenShift Container Platform life cycle
* Service Definition
* OpenShift Container Platform support documentation
* Limited support status
* OpenShift Container Platform service-level agreement
* SRE access
* etcd encryption
* AWS prerequisites
* Storage
* Setting up AWS EFS for Red{nbsp}Hat OpenShift Service on AWS
* CIDR Range Definitions
* ROSA roadmap
* Learn about OpenShift
* {cluster-manager-url}
* Red{nbsp}Hat Support
