---
title: "Understanding process and security for {product-title}"
type: reference
domain: openshift
slug: osd-architecture-4-22-policy-process-security
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_architecture/policy-process-security
version: 4.22
family: osd_architecture
documentKind: "Documentation"
---

# Understanding process and security for {product-title}

[id="policy-process-security"]
= Understanding process and security for OpenShift Container Platform

[id="review-action-notifications_{context}"]
== Review and action cluster notifications

[role="_abstract"]

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

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/policy-process-security.adoc

[id="policy-incident_{context}"]
= Incident and operations management

[role="_abstract"]
This documentation details the Red{nbsp}Hat responsibilities for the OpenShift Container Platform managed service.
The cloud provider is responsible for protecting the hardware infrastructure that runs the services offered by the cloud provider.
The customer is responsible for incident and operations management of customer application data and any custom networking the customer has configured for the cluster network or virtual network.

[id="platform-monitoring_{context}"]
== Platform monitoring
A Red{nbsp}Hat Site Reliability Engineer (SRE) maintains a centralized monitoring and alerting system for all OpenShift Container Platform cluster components, SRE services, and underlying cloud provider accounts. Platform audit logs are securely forwarded to a centralized SIEM (Security Information and Event Monitoring) system, where they might trigger configured alerts to the SRE team and are also subject to manual review. Audit logs are retained in the SIEM for one year. Audit logs for a given cluster are not deleted at the time the cluster is deleted.

[id="incident-management_{context}"]
== Incident management
An incident is an event that results in a degradation or outage of one or more Red{nbsp}Hat services.

An incident can be raised by a customer or Customer Experience and Engagement (CEE) member through a support case, directly by the centralized monitoring and alerting system, or directly by a member of the SRE team.

Depending on the impact on the service and customer, the incident is categorized in terms of severity.

When managing a new incident, Red{nbsp}Hat uses the following general workflow:

. An SRE first responder is alerted to a new incident, and begins an initial investigation.
. After the initial investigation, the incident is assigned an incident lead, who coordinates the recovery efforts.
. The incident lead manages all communication and coordination around recovery, including any relevant notifications or support case updates.
. When the incident is resolved a brief summary of the incident and resolution are provided in the customer-initiated support ticket. This summary helps the customers understand the incident and its resolution in more detail.

If customers require more information in addition to what is provided in the support ticket, they can request the following workflow:

. The customer must make a request for the additional information within 5 business days of the incident resolution.
. Depending on the severity of the incident, Red{nbsp}Hat may provide customers with a root cause summary, or a root cause analysis (RCA) in the support ticket. The additional information will be provided within 7 business days for root cause summary and 30 business days for root cause analysis from the incident resolution.

Red{nbsp}Hat also assists with customer incidents raised through support cases.
Red{nbsp}Hat can assist with activities including but not limited to:

* Forensic gathering, including isolating virtual compute
* Guiding compute image collection
* Providing collected audit logs

[id="backup-recovery_{context}"]
== Backup and recovery
All OpenShift Container Platform clusters are backed up using cloud provider snapshots. Notably, this does not include customer data stored on persistent volumes (PVs). All snapshots are taken using the appropriate cloud provider snapshot APIs and are uploaded to a secure object storage bucket (S3 in AWS, and GCS in {gcp-full}) in the same account as the cluster.

//Verify if the corresponding tables in rosa-sdpolicy-platform.adoc and rosa-policy-incident.adoc also need to be updated.

[cols= "3a,2a,2a,3a",options="header"]

|===
|Component
|Snapshot frequency
|Retention
|Notes

.2+|Full object store backup
|Daily
|7 days
.2+|This is a full backup of all Kubernetes objects like etcd. No PVs are backed up in this backup schedule.

|Weekly
|30 days

|Full object store backup
|Hourly
|24 hour
|This is a full backup of all Kubernetes objects like etcd. No PVs are backed up in this backup schedule.

|Node root volume
|Never
|N/A
|Nodes are considered to be short-term. Nothing critical should be stored on a node's root volume.

|===

* Red Hat does not commit to any Recovery Point Objective (RPO) or Recovery Time Objective (RTO).
* Customers are responsible for taking regular backups of their data
* Customers should deploy multi-AZ clusters with workloads that follow Kubernetes best practices to ensure high availability within a region.
* If an entire cloud region is unavailable, customers must install a new cluster in a different region and restore their apps using their backup data.

[id="cluster-capacity_{context}"]
== Cluster capacity
Evaluating and managing cluster capacity is a responsibility that is shared between Red Hat and the customer. Red Hat SRE is responsible for the capacity of all control plane and infrastructure nodes on the cluster.

Red Hat SRE also evaluates cluster capacity during upgrades and in response to cluster alerts. The impact of a cluster upgrade on capacity is evaluated as part of the upgrade testing process to ensure that capacity is not negatively impacted by new additions to the cluster. During a cluster upgrade, additional worker nodes are added to make sure that total cluster capacity is maintained during the upgrade process.

Capacity evaluations by SRE staff also happen in response to alerts from the cluster, once usage thresholds are exceeded for a certain period of time. Such alerts can also result in a notification to the customer.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/policy-process-security.adoc

[id="policy-change-management_{context}"]
= Change management

[role="_abstract"]
Manage changes to your cluster and its configuration.

[id="policy-customer-initiated-changes_{context}"]
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

[id="policy-red-hat-initiated-changes_{context}"]
== Red Hat-initiated changes

Red Hat site reliability engineering (SRE) manages the infrastructure, code, and configuration of OpenShift Container Platform using a GitOps workflow and fully automated CI/CD pipelines. This process ensures that Red Hat can safely introduce service improvements on a continuous basis without negatively impacting customers.

Every proposed change undergoes a series of automated verifications immediately upon check-in. Changes are then deployed to a staging environment where they undergo automated integration testing. Finally, changes are deployed to the production environment. Each step is fully automated.

An authorized SRE reviewer must approve advancement to each step. The reviewer cannot be the same individual who proposed the change. All changes and approvals are fully auditable as part of the GitOps workflow.

Some changes are released to production incrementally, using feature flags to control availability of new features to specified clusters or customers.

[id="patch-management_{context}"]
== Patch management

OpenShift Container Platform software and the underlying immutable Red Hat Enterprise Linux CoreOS (RHCOS) operating system image are patched for bugs and vulnerabilities in regular z-stream upgrades. Read more about RHCOS architecture in the OpenShift Container Platform documentation.

// TODO: checking whether the OCP reference above should be dedicated? Either way, the attribute version should probably be used throughout the above paragraph

[id="release-management_{context}"]
== Release management

Red Hat does not automatically upgrade your clusters. You can schedule to upgrade the clusters at regular intervals (recurring upgrade) or just once (individual upgrade) using the {cluster-manager} web console. Red Hat might forcefully upgrade a cluster to a new z-stream version only if the cluster is affected by a critical impact CVE. You can review the history of all cluster upgrade events in the {cluster-manager} web console. For more information about releases, see the Life Cycle policy.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/policy-process-security.adoc

[id="policy-security-regulation-compliance_{context}"]
= Security and regulation compliance

[role="_abstract"]
Security and regulation compliance includes tasks, such as the implementation of security controls and compliance certification.

[id="data-classification_{context}"]
== Data classification
Red Hat defines and follows a data classification standard to determine the sensitivity of data and highlight inherent risk to the confidentiality and integrity of that data while it is collected, used, transmitted stored, and processed. Customer-owned data is classified at the highest level of sensitivity and handling requirements.

[id="data-management_{context}"]
== Data management
OpenShift Container Platform uses cloud provider services such as AWS Key Management Service (KMS) and {gcp-full} KMS to help securely manage encryption keys for persistent data. These keys are used for encrypting all control plane, infrastructure, and worker node root volumes. Customers can specify their own KMS key for encrypting root volumes at installation time. Persistent volumes (PVs) also use KMS for key management. Customers can specify their own KMS key for encrypting PVs by creating a new `StorageClass` referencing the KMS key Amazon Resource Name (ARN) or ID.

When a customer deletes their OpenShift Container Platform cluster, all cluster data is permanently deleted, including control plane data volumes and customer application data volumes, such a persistent volumes (PV).

[id="vulnerability-management_{context}"]
== Vulnerability management
Red Hat performs periodic vulnerability scanning of OpenShift Container Platform using industry standard tools. Identified vulnerabilities are tracked to their remediation according to timelines based on severity. Vulnerability scanning and remediation activities are documented for verification by third-party assessors in the course of compliance certification audits.

[id="firewall_{context}"]
== Network security: Firewall and DDoS protection
Each OpenShift Container Platform cluster is protected by a secure network configuration at the cloud infrastructure level using firewall rules (AWS Security Groups or {gcp-full} Compute Engine firewall rules). OpenShift Container Platform customers on AWS are also protected against DDoS attacks with AWS Shield Standard.
Similarly, all {gcp-short} load balancers and public IP addresses used by OpenShift Container Platform on {gcp-short} are protected against DDoS attacks with {gcp-full} Armor Standard.

[id="Component-traffic-flow-encryption_{context}"]
== Network security: Component and traffic flow encryption
OpenShift Container Platform components are configured to use Transport Layer Security (TLS) for secure communication, prioritizing TLS 1.3 for its performance and security enhancements. For components not yet supporting TLS 1.3, robust TLS 1.2 cipher suites are configured. This comprehensive TLS configuration ensures the encryption of various traffic flows within and to the OpenShift Dedicated environment. For more information, refer to TLS configuration on OpenShift and Appendix 4(Online Subscription Services).

** Starting with version 4.7, the OpenShift API server (port 6443), kube-controller (port 10257), and kube-scheduler (port 10259) are configured to use TLS 1.3 with a reduced set of secure cipher suites.
** The Web Console and etcd also use secure default cipher suites. As OpenShift is updated, older and more vulnerable cipher options are deprecated for these components.
** The Kubelet (ports 10248, 10250) secures node-level operations using TLS 1.3, while also allowing the explicit configuration of specific TLS 1.2 cipher suites.
** Ingress traffic is secured by the OpenShift Container Platform Router through a robust TLS configuration. By default, it uses a hardened set of TLS 1.2 cipher suites, and in OpenShift 4.6 and later, it also supports TLS 1.3 for enhanced security.
** By default, OpenShift 4 enables secure TLS configurations on numerous internal services to protect their communications. These services include the Machine Config Server (ports 22623-22624), Node Exporter (ports 9100-9101), and Kube RBAC Proxy (port 9192).

[id="private-clusters_{context}"]
== Network security: Private clusters and network connectivity
Customers can optionally configure their OpenShift Container Platform cluster endpoints (web console, API, and application router) to be made private so that the cluster control plane or applications are not accessible from the Internet.

For AWS, customers can configure a private network connection to their OpenShift Container Platform cluster through AWS VPC peering, AWS VPN, or AWS Direct Connect.

[id="network-access-controls_{context}"]
== Network security: Cluster network access controls
Fine-grained network access control rules can be configured by customers per project.

[id="penetration-testing_{context}"]
== Penetration testing
Red Hat performs periodic penetration tests against OpenShift Container Platform. Tests are performed by an independent internal team using industry standard tools and best practices.

Any issues that are discovered are prioritized based on severity. Any issues found belonging to open source projects are shared with the community for resolution.

[id="compliance_{context}"]
== Compliance
OpenShift Container Platform follows common industry best practices for security and controls. The certifications are outlined in the following table.

.Security and control certifications for OpenShift Container Platform
[cols= "3,3,3",options="header"]
|===
| Compliance | OpenShift Container Platform on AWS | OpenShift Container Platform on {gcp-short}

| HIPAA Qualified | Yes (Only Customer Cloud Subscriptions) | Yes (Only Customer Cloud Subscriptions)

| ISO 27001 | Yes | Yes

| ISO 27017 | Yes | Yes

| ISO 27018 | Yes | Yes

| PCI DSS 4.0 | Yes | Yes

| SOC 1 Type 2 | Yes | Yes

| SOC 2 Type 2 | Yes | Yes

| SOC 3 | Yes | Yes

|===

//This table exists in sdpolicy-security.adoc file also.

[role="_additional-resources"]
== Additional resources

* Red Hat Subprocessor List
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/policy-process-security.adoc

[id="policy-disaster-recovery_{context}"]
= Disaster recovery

[role="_abstract"]
OpenShift Container Platform provides disaster recovery for failures that occur at the pod, worker node, infrastructure node, control plane node, and availability zone levels.

All disaster recovery requires that the customer use best practices for deploying highly available applications, storage, and cluster architecture (for example, single-zone deployment vs. multi-zone deployment) to account for the level of desired availability.

One single-zone cluster will not provide disaster avoidance or recovery in the event of an availability zone or region outage. Multiple single-zone clusters with customer-maintained failover can account for outages at the zone or region levels.

One multi-zone cluster will not provide disaster avoidance or recovery in the event of a full region outage. Multiple multi-zone clusters with customer-maintained failover can account for outages at the region level.

[role="_additional-resources"]
== Additional resources

* Identity and access management
