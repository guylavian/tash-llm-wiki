---
title: "Overview of responsibilities for {product-title}"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-policy-responsibility-matrix
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-policy-responsibility-matrix
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# Overview of responsibilities for {product-title}

[id="rosa-policy-responsibility-matrix"]
= Overview of responsibilities for OpenShift Container Platform

[role="_abstract"]
This documentation outlines Red{nbsp}Hat, Amazon Web Services (AWS), and customer responsibilities for the OpenShift Container Platform managed service.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-responsibility-matrix.adoc

[id="rosa-policy-responsibilities_{context}"]
= Shared responsibilities for OpenShift Container Platform

While Red{nbsp}Hat and Amazon Web Services (AWS) manage the OpenShift Container Platform services, the customer shares certain responsibilities. The OpenShift Container Platform services are accessed remotely, hosted on public cloud resources, created in customer-owned AWS accounts, and have underlying platform and data security that is owned by Red{nbsp}Hat.

[IMPORTANT]
====
If the `cluster-admin` role is added to a user, see the responsibilities and exclusion notes in the Red{nbsp}Hat Enterprise Agreement Appendix 4 (Online Subscription Services).
====

[cols="2a,3a,3a,3a,3a,3a",options="header"]
|===

|Resource
|Incident and operations management
|Change management
|Access and identity authorization
|Security and regulation compliance
|Disaster recovery

|Customer data |Customer |Customer |Customer |Customer |Customer

|Customer applications |Customer |Customer |Customer |Customer |Customer

|Developer services |Customer |Customer |Customer |Customer |Customer

|Platform monitoring |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat

|Logging |Red{nbsp}Hat |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat

|Application networking |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat |Red{nbsp}Hat

|Cluster networking
|Red Hat ^[1]^
|Red Hat and Customer ^[2]^
|Red Hat and Customer
|Red Hat ^[1]^
|Red Hat ^[1]^

|Virtual networking management |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer |Red{nbsp}Hat and Customer

|Virtual compute management (control plane, infrastructure and worker nodes) |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat

|Cluster version |Red{nbsp}Hat |Red{nbsp}Hat and Customer |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat

|Capacity management |Red{nbsp}Hat |Red{nbsp}Hat and Customer |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat

|Virtual storage management |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat |Red{nbsp}Hat

|AWS software (public AWS services) |AWS |AWS
|AWS |AWS |AWS

|Hardware/AWS global infrastructure |AWS |AWS |AWS |AWS |AWS

|===
1. If the customer chooses to use their own CNI plugin, the responsibility shifts to the customer.
2. The customer must configure their firewall to grant access to the required OpenShift and AWS domains and ports before the cluster is provisioned. For more information, see "AWS firewall prerequisites".

[role="_additional-resources"]
.Additional resources
* Firewall prerequisites for ROSA (classic architecture) clusters using STS
* Firewall prerequisites

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-responsibility-matrix.adoc

[id="rosa-policy-shared-responsibility_{context}"]
= Tasks for shared responsibilities by area

Red{nbsp}Hat, AWS, and the customer all share responsibility for the monitoring, maintenance, and overall health of a OpenShift Container Platform (ROSA) cluster. This documentation illustrates the delineation of responsibilities for each of the listed resources as shown in the tables below.

[id="review-action-notifications_{context}"]
== Review and action cluster notifications

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-notifications.adoc
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="managed-cluster-notification-policy_{context}"]
= Cluster notification policy

[role="_abstract"]
Cluster notifications are designed to keep you informed about the health of your cluster and high impact events that affect it.

Most cluster notifications are generated and sent automatically to ensure that you are immediately informed of problems or important changes to the state of your cluster.

In certain situations, Red{nbsp}Hat Site Reliability Engineering (SRE) creates and sends cluster notifications to provide additional context and guidance for a complex issue.

Cluster notifications are not sent for low-impact events, low-risk security updates, routine operations and maintenance, or minor, transient issues that are quickly resolved by Red{nbsp}Hat SRE.

Red{nbsp}Hat services automatically send notifications when:

* Remote health monitoring or environment verification checks detect an issue in your cluster, for example, when a worker node has low disk space.
* Significant cluster life cycle events occur, for example, when scheduled maintenance or upgrades begin, or cluster operations are impacted by an event, but do not require customer intervention.
* Significant cluster management changes occur, for example, when cluster ownership or administrative control is transferred from one user to another.
* Your cluster subscription is changed or updated, for example, when Red{nbsp}Hat makes updates to subscription terms or features available to your cluster.

SRE creates and sends notifications when:

* An incident results in a degradation or outage that impacts your cluster's availability or performance, for example, your cloud provider has a regional outage. SRE sends subsequent notifications to inform you of incident resolution progress, and when the incident is resolved.
* A security vulnerability, security breach, or unusual activity is detected on your cluster.
* Red{nbsp}Hat detects that changes you have made are creating or may result in cluster instability.
* Red{nbsp}Hat detects that your workloads are causing performance degradation or instability in your cluster.

//---

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-shared-responsibility.adoc

[id="rosa-policy-incident_{context}"]
= Incident and operations management

Red{nbsp}Hat is responsible for overseeing the service components required for default platform networking.
AWS is responsible for protecting the hardware infrastructure that runs all of the services offered in the AWS Cloud. The customer is responsible for incident and operations management of customer application data and any custom networking the customer has configured for the cluster network or virtual network.

[cols= "2a,3a,3a",options="header"]
|===

|Resource
|Service responsibilities
|Customer responsibilities

|Application networking
|**Red{nbsp}Hat**

- Monitor native OpenShift router
service, and respond to alerts.
|- Monitor health of application routes, and the endpoints behind them.
- Report outages to Red{nbsp}Hat and AWS.

|Cluster networking
|**Red{nbsp}Hat**

- Monitor, alert, and address incidents related to cluster DNS, network plugin connectivity between cluster components, and the default Ingress Controller.
|- Monitor and address incidents related to optional Ingress Controllers, additional Operators installed through the software catalog, and network plugins replacing the default OpenShift CNI plugins.

|Virtual networking management
|**Red{nbsp}Hat**

- Monitor AWS load balancers, Amazon VPC subnets, and AWS service components necessary for default
platform networking. Respond to alerts.
|- Monitor health of AWS load balancer endpoints.
- Monitor network traffic that is optionally configured through Amazon VPC-to-VPC connection, AWS VPN connection, or AWS
Direct Connect for potential issues or
security threats.

|Virtual storage management
|**Red{nbsp}Hat**

- Monitor Amazon EBS volumes attached to cluster nodes and Amazon S3 buckets used for the ROSA service’s built-in container image
registry. Respond to alerts.
|- Monitor health of application data.
- If customer managed AWS KMS keys are
used, create and control the key lifecycle and
key policies for Amazon EBS encryption.

|Platform monitoring
|**Red{nbsp}Hat**

- Maintain a centralized monitoring and alerting system for all ROSA cluster components, site reliability engineer (SRE) services, and underlying AWS accounts.
|
- Monitor capacity of worker nodes.
- Configure cluster monitoring stack components for monitoring and alerts.

|Incident management
|**Red{nbsp}Hat**

- Raise and manage known incidents.
- Share root cause analysis (RCA) drafts with the customer.
|- Raise known incidents through a support case.

|Infrastructure and data resiliency
|**Red{nbsp}Hat**

- There is no Red{nbsp}Hat-provided backup method available for ROSA clusters with STS.
- Red{nbsp}Hat does not commit to any Recovery Point Objective (RPO) or Recovery Time Objective (RTO).
|- Take regular backups of data and deploy multi-AZ clusters with workloads that follow Kubernetes best practices to ensure high availability within a region.
- If an entire cloud region is unavailable, install a new cluster in a different region and restore apps using backup data.

|Cluster capacity
|**Red{nbsp}Hat**

- Manage the capacity of all control plane and infrastructure nodes on the cluster.
- Evaluate cluster capacity during upgrades and in response to cluster alerts.
|

|AWS software (public AWS services)
|**AWS**

- For information regarding AWS incident and operations management, see How AWS maintains operational resilience and continuity of service in the AWS whitepaper.
|- Monitor health of AWS resources in the
customer account.
- Use IAM tools to apply the appropriate
permissions to AWS resources in the customer account.

|Hardware/AWS global infrastructure
|**AWS**

- For information regarding AWS incident and operations management, see How AWS maintains operational
resilience and continuity of service in the AWS white paper.

|- Configure, manage, and monitor customer applications and data to ensure application and data security controls are properly enforced.

|===

[id="rosa-policy-platform-monitoring_{context}"]
== Platform monitoring
Platform audit logs are securely forwarded to a centralized security information and event monitoring (SIEM) system, where they may trigger configured alerts to the Red{nbsp}Hat SRE team and are also subject to manual review. Audit logs are retained in the SIEM system for one year. Audit logs for a given cluster are not deleted at the time the cluster is deleted.

Red{nbsp}Hat monitors the cluster using monitoring and alerting systems that run on Red{nbsp}Hat managed infrastructure and operate independently of the cluster. Customers retain full access to the Cluster Monitoring Operator stack for their own in-cluster monitoring, alerting, and observability needs.

[id="rosa-policy-incident-management_{context}"]
== Incident management
An incident is an event that results in a degradation or outage of one or more Red{nbsp}Hat services.

An incident can be raised by a customer or a Customer Experience and Engagement (CEE) member through a support case, directly by the centralized monitoring and alerting system, or directly by a member of the SRE team.

Depending on the impact on the service and customer, the incident is categorized in terms of severity.

When managing a new incident, Red{nbsp}Hat uses the following general workflow:

. An SRE first responder is alerted to a new incident and begins an initial investigation.
. After the initial investigation, the incident is assigned an incident lead, who coordinates the recovery efforts.
. The incident lead manages all communication and coordination around recovery, including any relevant notifications and support case updates.
. When the incident is resolved a brief summary of the incident and resolution are provided in the customer-initiated support ticket. This summary helps the customers understand the incident and its resolution in more detail.

If customers require more information in addition to what is provided in the support ticket, they can request the following workflow:

. The customer must make a request for the additional information within 5 business days of the incident resolution.
. Depending on the severity of the incident, Red{nbsp}Hat may provide customers with a root cause summary, or a root cause analysis (RCA) in the support ticket. The additional information will be provided within 7 business days for root cause summary and 30 business days for root cause analysis from the incident resolution.

Red{nbsp}Hat also assists with customer incidents raised through support cases.
Red{nbsp}Hat can assist with activities including but not limited to:

* Forensic gathering, including isolating virtual compute
* Guiding compute image collection
* Providing collected audit logs

//Note: The following content will be used again in the future (per OSDOCS:4654)
//[id="backup-recovery_{context}"]
//== Backup and recovery
//All Red Hat OpenShift Service on AWS cluster metadata from OpenShift Cluster Manager is securely backed up by Red Hat. The following table outlines backup and recovery strategies:

//Verify if the corresponding tables in rosa-sdpolicy-platform.adoc and policy-incident.adoc also need to be updated.

//[cols= "3a,2a,2a,3a",options="header"]

//|===
//|Component
//|Snapshot frequency
//|Retention
//|Notes

//.2+|Full object store backup, all cluster persistent volumes (PVs)
//|Daily
//|7 days
//.2+|This is a full backup of all Kubernetes objects like etcd, as well as all PVs in the cluster.

//|Weekly
//|30 days

//|Full object store backup
//|Hourly
//|24 hour
//|This is a full backup of all Kubernetes objects like etcd. No PVs are backed up in this backup schedule.

//|Node root volume
//|Never
//|N/A
//|Nodes are considered to be short-term. Nothing critical should be stored on a node's root volume.

//|===

[id="rosa-policy-cluster-capacity_{context}"]
== Cluster capacity

The impact of a cluster upgrade on capacity is evaluated as part of the upgrade testing process to ensure that capacity is not negatively impacted by new additions to the cluster. During a cluster upgrade, additional worker nodes are added to make sure that total cluster capacity is maintained during the upgrade process.

Capacity evaluations by the Red{nbsp}Hat SRE staff also happen in response to alerts from the cluster, after usage thresholds are exceeded for a certain period of time. Such alerts can also result in a notification to the customer.

[role="_additional-resources"]
.Additional resources
* Cluster notifications

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-shared-responsibility.adoc

[id="rosa-policy-change-management_{context}"]
= Change management

[role="_abstract"]
This section describes the policies about how cluster and configuration changes, patches, and releases are managed.

Red{nbsp}Hat is responsible for enabling changes to the cluster infrastructure and services that the customer will control, as well as maintaining versions for the control plane nodes, infrastructure nodes and services, and worker nodes. AWS is responsible for protecting the hardware infrastructure that runs all of the services offered in the
AWS Cloud. The customer is responsible for initiating infrastructure change requests and installing and maintaining optional services and networking configurations on the cluster, as well as all changes to customer data and customer applications.

[id="rosa-policy-customer-initiated-changes_{context}"]
== Customer-initiated changes

You can initiate changes using self-service capabilities such as cluster deployment, worker node scaling, or cluster deletion.

Change history is captured in the *Cluster History* section in the OpenShift Cluster Manager *Overview tab*, and is available for you to view. The change history includes, but is not limited to, logs from the following changes:

* Adding or removing identity providers
* Adding or removing users to or from the `dedicated-admins` group
* Scaling the cluster compute nodes
* Scaling the cluster load balancer
* Scaling the cluster persistent storage
* Upgrading the cluster

You can implement a maintenance exclusion by avoiding changes in {cluster-manager} for the following components:

* Deleting a cluster
* Adding, modifying, or removing identity providers
* Adding, modifying, or removing a user from an elevated group
* Installing or removing add-ons
* Modifying cluster networking configurations
* Adding, modifying, or removing machine pools
* Enabling or disabling user workload monitoring
* Initiating an upgrade

[IMPORTANT]
====
To enforce the maintenance exclusion, ensure machine pool autoscaling or automatic upgrade policies have been disabled. After the maintenance exclusion has been lifted, proceed with enabling machine pool autoscaling or automatic upgrade policies as desired.
====

[id="rosa-policy-red-hat-initiated-changes_{context}"]
== Red{nbsp}Hat-initiated changes

Red{nbsp}Hat site reliability engineering (SRE) manages the infrastructure, code, and configuration of OpenShift Container Platform using a GitOps workflow and fully automated CI/CD pipelines. This process ensures that Red{nbsp}Hat can safely introduce service improvements on a continuous basis without negatively impacting customers.

Every proposed change undergoes a series of automated verifications immediately upon check-in. Changes are then deployed to a staging environment where they undergo automated integration testing. Finally, changes are deployed to the production environment. Each step is fully automated.

An authorized Red{nbsp}Hat SRE reviewer must approve advancement to each step. The reviewer cannot be the same individual who proposed the change. All changes and approvals are fully auditable as part of the GitOps workflow.

Some changes are released to production incrementally, using feature flags to control availability of new features to specified clusters or customers, such as private or public previews.

[id="rosa-policy-patch-management_{context}"]
== Patch management

OpenShift Container Platform software and the underlying immutable Red{nbsp}Hat CoreOS (RHCOS) operating system image are patched for bugs and vulnerabilities in regular z-stream upgrades. Read more about RHCOS architecture in the OpenShift Container Platform documentation.

[id="rosa-policy-release-management_{context}"]
== Release management

Red{nbsp}Hat does not automatically upgrade your clusters. You can schedule to upgrade the clusters at regular intervals (recurring upgrade) or just once (individual upgrade) using the {cluster-manager} web console. Red{nbsp}Hat might forcefully upgrade a cluster to a new z-stream version only if the cluster is affected by a critical impact CVE.

[NOTE]
====
Because the required permissions can change between y-stream releases, the AWS managed policies are automatically updated before an upgrade can be performed.
====

You can review the history of all cluster upgrade events in the {cluster-manager} web console.
You can review the history of all cluster upgrade events in the {cluster-manager} web console. For more information about releases, see the Life Cycle policy.

[id="rosa-policy-resource-responsibilities_{context}"]
== Service and Customer resource responsibilities

The following table defines the responsibilities for cluster resources.

[cols="2a,3a,3a",options="header"]
|===

|Resource
|Service responsibilities
|Customer responsibilities

|Logging
|**Red{nbsp}Hat**

- Centrally aggregate and monitor platform audit logs.

- Provide and maintain a logging Operator to enable the customer to deploy a logging stack for default application logging.

- Provide audit logs upon customer request.

|- Install the optional default application logging Operator on the cluster.
- Install, configure, and maintain any optional application logging solutions, such as logging sidecar containers or third-party logging applications.
- Tune size and frequency of application logs being produced by customer applications if they are affecting the stability of the logging stack or the cluster.
- Request platform audit logs through a support case for researching specific incidents.

|Application networking
|**Red{nbsp}Hat**

- Set up public load balancers. Provide the ability to set up private load balancers and up to one additional load balancer when required.

- Set up native OpenShift router service. Provide the ability to set the router as private and add up to one additional router shard.

- Install, configure, and maintain OVN-Kubernetes components for default internal pod traffic.

- Provide the ability for the customer to manage `NetworkPolicy` and `EgressNetworkPolicy` (firewall) objects.

|- Configure non-default pod network permissions for project and pod networks, pod ingress, and pod egress using `NetworkPolicy` objects.
- Use {cluster-manager} to request a private load balancer for default application routes.
- Use {cluster-manager} to configure up to one additional public or private router shard and corresponding load balancer.
- Request and configure any additional service load balancers for specific services.
- Configure any necessary DNS forwarding rules.

|Cluster networking
|**Red{nbsp}Hat**

- Set up cluster management components, such as public or private service endpoints and necessary integration with Amazon VPC components.

- Set up internal networking components required for internal cluster communication between worker
clusters and control planes.

|- Configure your firewall to grant access to the required OpenShift and AWS domains and ports before the cluster is provisioned. For more information, see "AWS firewall prerequisites".
- Provide optional non-default IP address ranges for machine CIDR, service CIDR, and pod CIDR if needed through {cluster-manager} when the cluster is provisioned.
- Request that the API service endpoint be made public or private on cluster creation or after cluster creation through {cluster-manager}.
- Create additional Ingress Controllers to publish additional application routes.
- Install, configure, and upgrade optional CNI plugins if clusters are installed without the default OpenShift CNI plugins.

|Virtual networking management
|**Red{nbsp}Hat**

- Set up and configure Amazon VPC components required to provision the cluster, such as subnets, load balancers, internet gateways, and NAT gateways.

- Provide the ability for the customer to
manage AWS VPN connectivity with on-premise resources, Amazon VPC-to-VPC connectivity, and AWS Direct Connect as required through  {cluster-manager}.

- Enable customers to create and deploy AWS load balancers for use with service load balancers.

|- Set up and maintain optional Amazon VPC components, such as Amazon VPC-to-VPC connection, AWS VPN connection, or AWS Direct Connect.
- Request and configure any additional service load balancers for specific services.

|Virtual compute management
|**Red{nbsp}Hat**

- Set up and configure the ROSA control plane and data plane to use Amazon EC2 instances for cluster compute.

- Monitor and manage the deployment of Amazon EC2 control plane and infrastructure nodes on the cluster.

|- Monitor and manage Amazon EC2 worker nodes by creating a
machine pool using the OpenShift Cluster Manager or the ROSA CLI (`rosa`).
- Manage changes to customer-deployed applications and application data.

|Cluster version
|**Red{nbsp}Hat**

- Enable upgrade scheduling process.

- Monitor upgrade progress and remedy any issues encountered.

- Publish change logs and release notes for patch release upgrades.

|- Either set up automatic upgrades or schedule patch release upgrades immediately or for the future.
- Acknowledge and schedule minor version upgrades.
- Test customer applications on patch releases to ensure compatibility.

|Capacity management
|**Red{nbsp}Hat**

- Monitor the use of the control plane.
Control planes include control plane nodes and infrastructure nodes.
- Scale and resize control plane to maintain quality of service.

| - Monitor worker node utilization and, if appropriate, enables the auto-scaling feature.
- Determine the scaling strategy of the cluster. See the additional resources for more information on machine pools.
- Use the provided {cluster-manager} controls to add or remove additional worker nodes as required.
- Respond to Red{nbsp}Hat notifications regarding cluster resource requirements.

|Virtual storage management
|**Red{nbsp}Hat**

- Set up and configure Amazon EBS to provision local node storage and persistent volume storage for the cluster.

- Set up and configure the built-in image registry to use Amazon S3 bucket storage. ^[1]^

- Regularly prune image registry resources in
Amazon S3 to optimize Amazon S3 usage and cluster performance. ^[2]^

| - Optionally configure the Amazon EBS CSI driver or the Amazon
EFS CSI driver to provision persistent volumes on the cluster.

|AWS software (public AWS services)
|**AWS**

**Compute:** Provide the Amazon EC2 service, used for ROSA relevant resources.

**Storage:** Provide Amazon EBS, used by ROSA to provision local node storage and persistent volume storage for the cluster.

**Storage:** Provide Amazon S3, used for the ROSA
built-in image registry.

**Networking:**
Provide the following AWS Cloud services, used by ROSA
to satisfy virtual networking
infrastructure needs:

** Amazon VPC
** Elastic Load Balancing
** AWS IAM
** AWS STS

**Networking:**
Provide the following AWS services, which customers can optionally integrate with ROSA:

- AWS VPN
- AWS Direct Connect
- AWS PrivateLink
- AWS Transit Gateway

| - Sign requests using an access key ID and secret access key
associated with an IAM principal or STS temporary security
credentials.
- Specify VPC subnets for the cluster to use during cluster
creation.
- Optionally configure a customer-managed VPC for use with ROSA clusters (required for PrivateLink and HCP clusters).

|Hardware/AWS global infrastructure
|**AWS**

- For information regarding  management controls for AWS data centers, see Our Controls on the AWS Cloud Security page.

- For information regarding change management best practices, see Guidance for Change Management on AWS in the AWS Solutions Library.

|- Implement change management best practices for customer
applications and data hosted on the AWS Cloud.

|===

1. For more information on authentication flow for AWS STS, see Authentication flow for AWS STS.

2. For more information on pruning images, see Automatically pruning Images.

[role="_additional-resources"]
.Additional resources
* Firewall prerequisites for OpenShift Container Platform
* Firewall prerequisites for OpenShift Container Platform clusters
* Firewall prerequisites

//Modules included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-shared-responsibility.adoc

[id="rosa-policy-security-compliance_{context}"]
= Security and regulation compliance
The following table outlines the  the responsibilities in regards to security and regulation compliance:

[cols="2a,3a,3a",options="header"]
|===

|Resource
|Service responsibilities
|Customer responsibilities

|Logging
|**Red{nbsp}Hat**

- Send cluster audit logs to a Red{nbsp}Hat SIEM to analyze for security events. Retain audit logs for a defined period of time to support forensic analysis.
|- Analyze application logs for security events.
- Send application logs to an external endpoint through logging sidecar containers or third-party logging applications if longer retention is required than is offered by the default logging stack.

|Virtual networking management
|**Red{nbsp}Hat**

- Monitor virtual networking components for potential issues and security threats.

- Use public AWS tools for additional monitoring and protection.

|- Monitor optional configured virtual networking components for potential issues and security threats.
- Configure any necessary firewall rules or customer data center protections as required.

|Virtual storage management
|**Red{nbsp}Hat**

- Monitor virtual storage components for potential issues and security threats.

- Use public AWS tools for additional monitoring and protection.

- Configure the ROSA service to encrypt control plane, infrastructure, and worker node volume data by default using the
AWS managed Key Management Service (KMS) key that Amazon EBS provides.

- Configure the ROSA service to encrypt customer persistent volumes that use the default storage class with the AWS
managed KMS key that Amazon EBS provides.

- Provide the ability for the customer to use a customer managed AWS KMS key to encrypt persistent volumes.

- Configure the container image registry to encrypt image registry data at rest using server-side encryption with Amazon S3 managed keys (SSE-3).

- Provide the ability for the customer to create a public or private Amazon S3 image registry to protect their container
images from unauthorized user access.

|- Provision Amazon EBS volumes.
- Manage Amazon EBS volume storage to ensure enough storage is available to mount as a volume in ROSA.
- Create the persistent volume claim and generate a
persistent volume though OpenShift Cluster Manager.

|Virtual compute management
|**Red{nbsp}Hat**

- Monitor virtual compute components for potential issues and security threats.

- Use public AWS tools for additional monitoring and protection.

|- Monitor optional configured virtual networking components for
potential issues and security threats.
- Configure any necessary firewall rules or customer data center protections as required.

|AWS  software (public AWS services)
|**AWS**

**Compute:** Secure Amazon EC2, used for ROSA
used for ROSA
control plane, infrastructure, and worker nodes.
control plane and worker nodes.
For more information, see 
Infrastructure security in Amazon EC2 in the Amazon EC2 User Guide.

**Storage:** Secure Amazon Elastic Block Store (EBS),
used for ROSA
control plane, infrastructure, and worker node volumes,
control plane and worker node volumes,
as well as Kubernetes persistent volumes. For more information, see Data protection in Amazon EC2 in the Amazon EC2 User Guide.

**Storage:** Provide AWS KMS, which ROSA uses to
encrypt control plane, infrastructure, worker node volumes and persistent volumes.
encrypt control plane, worker node volumes and persistent volumes.
For more information, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html[Amazon EBS encryption] in the Amazon EC2 User Guide.

**Storage:** Secure Amazon S3, used for the ROSA service’s built-in container image registry. For more information, see Amazon S3 security in the S3 User Guide.

**Networking:** Provide security capabilities and services
to increase privacy and control network access on AWS global infrastructure, including network firewalls built into
Amazon VPC, private or dedicated network connections, and automatic encryption of all traffic on the AWS global
and regional networks between AWS secured facilities. For more information, see the AWS Shared Responsibility Model
and Infrastructure security in the Introduction to AWS Security whitepaper.

|- Ensure security best practices and the principle of least
privilege are followed to protect data on the Amazon EC2
instance. For more information, see Infrastructure security in Amazon EC2
 and Data protection in Amazon EC2.
- Monitor optional configured virtual networking components for
potential issues and security threats.
- Configure any necessary firewall rules or customer data center protections as required.
- Create an optional customer managed KMS key and encrypt
the Amazon EBS persistent volume using the KMS key.
- Monitor the customer data in virtual storage
for potential issues and security threats. For more information,
see the shared responsibility model.

|Hardware/AWS global infrastructure
|**AWS**

- Provide the AWS global infrastructure that ROSA uses to deliver service functionality. For more information regarding AWS security
controls, see Security of the AWS Infrastructure in the AWS whitepaper.

- Provide documentation for the customer to
manage compliance needs and check their
security state in AWS using tools such as
AWS Artifact and AWS Security Hub. For
more information, see Compliance
validation for ROSA in the ROSA User
Guide.

|- Configure, manage, and monitor customer applications and data
to ensure application and data security controls are properly
enforced.
- Use IAM tools to apply the appropriate permissions to AWS
resources in the customer account.
|===
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-shared-responsibility.adoc

[id="rosa-policy-disaster-recovery_{context}"]
= Disaster recovery
Disaster recovery includes data and configuration backup, replicating data and configuration to the disaster recovery environment, and failover on disaster events.

OpenShift Container Platform (ROSA) provides disaster recovery for failures that occur at the pod, node, and availability zone levels.

All disaster recovery requires that the customer use best practices for deploying highly available applications, storage, and cluster architecture, such as multiple machine pools across multiple availability zones, to account for the level of desired availability.

One cluster with a single machine pool will not provide disaster avoidance or recovery in the event of an availability zone or region outage. Multiple clusters with single machine pools with customer-maintained failover can account for outages at the zone or at the regional level.

One cluster with multiple machine pools across multiple availability zones will not provide disaster avoidance or recovery in the event of a full region outage. Multiple clusters in several regions with multiple machine pools in more than one availability-zone with customer-maintained failover can account for outages at the regional level.

[cols="2a,3a,3a" ,options="header"]
|===
|Resource
|Service responsibilities
|Customer responsibilities

|Virtual networking management
|**Red{nbsp}Hat**

- Recreate affected virtual network components that are necessary for the platform to function.
|- Configure virtual networking connections with more than one tunnel where possible for protection against outages as recommended by the public cloud provider.
- Maintain failover DNS and load balancing if using a global load balancer with multiple clusters.
//waiting to hear back from Will G. if RH responsibilities below should have just been conditionalized out per the migration review for hcp or Classic as well.
|Virtual Storage management
|**Red{nbsp}Hat**
- For ROSA clusters created with IAM user credentials, back up all Kubernetes objects on the cluster through hourly, daily, and weekly volume snapshots. Hourly backups are retained for 24 hrs (1 day), daily backups are retained for 168 hrs (1 week), and weekly backups are retained for 720 hrs (30 days).

|- Back up customer applications and application data.

|Virtual compute management
|**Red{nbsp}Hat**
- Monitor the cluster and replace failed Amazon EC2 control plane or infrastructure nodes.
- Provide the ability for the customer to manually or automatically replace failed worker nodes.

|- Replace failed Amazon EC2 worker nodes by editing the
machine pool configuration through OpenShift Cluster Manager or the ROSA CLI.

|AWS software (public AWS services)
|**AWS**

**Compute:** Provide Amazon EC2 features that support data resiliency such as Amazon EBS snapshots and Amazon EC2 Auto Scaling. For more information, see Resilience in Amazon EC2 in the EC2 User Guide.

**Storage:** Provide the ability for the ROSA service
and customers to back up the Amazon EBS volume on the cluster through Amazon EBS volume snapshots.

**Storage:** For information about Amazon S3 features that support data resiliency, see Resilience in Amazon S3.

**Networking:** For information about Amazon VPC features that support data resiliency, see Resilience in Amazon Virtual Private
Cloud in the Amazon VPC User Guide.

|- Configure ROSA clusters with multiple machine pools across multiple availability zones to improve fault tolerance and cluster availability.

- Provision persistent
volumes using the
Amazon EBS CSI
driver to enable
volume snapshots.

- Create CSI volume snapshots of Amazon
EBS persistent volumes.
|Hardware/AWS global infrastructure
|**AWS**

- Provide AWS global infrastructure that allows ROSA to scale
control plane, infrastructure, and worker nodes
nodes
across
Availability Zones. This functionality enables ROSA to orchestrate automatic failover between zones without interruption.

- For more information about disaster recovery best practices, see Disaster recovery options in the cloud in the AWS
Well-Architected Framework.

|- Configure ROSA clusters with multiple machine pools across multiple availability zones to improve fault tolerance and cluster availability.

|===

//[id="sd-managed-resources"]
[id="sd-redhat-managed-resources_{context}"]
= Red{nbsp}Hat managed resources

[id="sd-managed-resources-overview_{context}"]
== Overview

The following covers all OpenShift Container Platform resources that are managed or protected by the Service Reliability Engineering Platform (SRE-P) Team. Customers should not try to change these resources because doing so can lead to cluster instability.

[id="sd-managed-resources-all_{context}"]
== Managed resources

The following list displays the OpenShift Container Platform resources managed by OpenShift Hive, the centralized fleet configuration management system. These resources are in addition to the OpenShift/ROSA platform resources created during installation. OpenShift Hive continually reconciles consistency across all OpenShift Container Platform clusters. Changes to OpenShift Container Platform resources should be made through {cluster-manager} so that {cluster-manager} and Hive are synchronized. Contact ocm-feedback@redhat.com if {cluster-manager} does not support modifying the resources in question.

.List of Red{nbsp}Hat managed resources
(Note that the following may not be visible in your ROSA cluster)
[%collapsible]
====
[source,yaml]
----

----
====

[id="sd-core-namespaces_{context}"]
== OpenShift Container Platform core namespaces

OpenShift Container Platform core namespaces are installed by default during cluster installation.

.List of core namespaces
(Note that the following may not be visible in your ROSA cluster)

[%collapsible]
====
[source,yaml]
----

----
====

[id="sd-add-on-managed-namespaces_{context}"]
== OpenShift Container Platform add-on namespaces

OpenShift Container Platform add-ons are services available for installation after cluster installation. These additional services include {openshift-dev-spaces-productname}, Red{nbsp}Hat OpenShift API Management, and Cluster Logging Operator. Any changes to resources within the following namespaces can be overridden by the add-on during upgrades, which can lead to unsupported configurations for the add-on functionality.

.List of add-on managed namespaces
[%collapsible]
====
[source,yaml]
----

----
====

[id="sd-validating-webhooks_{context}"]
== OpenShift Container Platform validating webhooks

OpenShift Container Platform validating webhooks are a set of dynamic admission controls maintained by the OpenShift SRE team. These HTTP callbacks, also known as webhooks, are called for various types of requests to ensure cluster stability. The following list describes the various webhooks with rules containing the registered operations and resources that are controlled. Any attempt to circumvent these validating webhooks could affect the stability and supportability of the cluster.

.List of validating webhooks
[%collapsible]
====
[source,json]
----

----
====

[role="_additional-resources"]
.Additional resources

* About machine pools

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-responsibility-matrix.adoc

[id="rosa-policy-customer-responsibility_{context}"]
= Additional customer responsibilities for data and applications

The customer is responsible for the applications, workloads, and data that they deploy to Red{nbsp}Hat
OpenShift Service on AWS. However, Red{nbsp}Hat and AWS provide various tools to help the customer
manage data and applications on the platform.

[cols="2a,3a,3a",options="header"]
|===

|Resource
|Red{nbsp}Hat and AWS
|Customer responsibilities

|Customer data
|**Red{nbsp}Hat**

- Maintain platform-level standards for data encryption as defined by industry security and
compliance standards.
- Provide OpenShift components to help manage application data, such as secrets.
- Enable integration with data services such as
Amazon RDS to store and manage data outside of the cluster and/or AWS.

**AWS**

- Provide Amazon RDS to allow customers to store and manage data outside of the cluster and/or AWS.
|- Maintain responsibility for all customer data stored on the platform and how customer applications consume and expose this data.

|Customer applications
|**Red{nbsp}Hat**

- Provision clusters with OpenShift components installed so that customers can access the OpenShift and Kubernetes APIs to deploy and manage containerized applications.
- Create clusters with image pull secrets so that customer deployments can pull images from the Red{nbsp}Hat Container Catalog registry.
- Provide access to OpenShift APIs that a customer can use to set up Operators to add community, third-party, and Red{nbsp}Hat services to the cluster.
- Provide storage classes and plugins to support persistent volumes for use with customer applications.
- Provide a container image registry so customers can securely store application container images on the cluster to deploy and manage applications.

**AWS**

- Provide Amazon EBS to support persistent volumes for use with customer applications.

- Provide Amazon S3 to support Red{nbsp}Hat provisioning of the container image registry.

|- Maintain responsibility for customer and third-party applications, data, and their complete lifecycle.
- If a customer adds Red{nbsp}Hat, community, third-party, their own, or other services to the cluster by using Operators or external images, the customer is responsible for these services and for working with the appropriate provider, including Red{nbsp}Hat, to troubleshoot any issues.
- Use the provided tools and features to configure and deploy; keep up to date; set up resource requests and limits; size the cluster to have enough resources to run apps; set up permissions; integrate with other services; manage any image streams or templates that the customer deploys; externally serve; save, back up, and restore data; and otherwise manage their highly available and resilient workloads.
- Maintain responsibility for monitoring the applications run on OpenShift Container Platform, including
installing and operating software to gather metrics, create alerts, and protect secrets in the application.

|===
