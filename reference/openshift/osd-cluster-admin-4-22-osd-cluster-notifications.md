---
title: "Cluster notifications"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-osd-cluster-notifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/osd-cluster-notifications
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# Cluster notifications

[id="osd-cluster-notifications"]
= Cluster notifications

[role="_abstract"]
Cluster notifications are messages about the status, health, or performance of your cluster. Red Hat Site Reliability Engineering (SRE) uses cluster notifications to communicate with you about your managed cluster and to prompt you to perform actions to resolve or prevent issues.

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
// * rosa_cluster_admin/rosa-cluster-notifications.adoc
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="managed-cluster-notification-severity_{context}"]
= Cluster notification severity levels

[role="_abstract"]
Each cluster notification has an associated severity level to help you identify notifications with the greatest impact to your business.

Red{nbsp}Hat uses the following severity levels for cluster notifications, from most to least severe:

Critical:: Immediate action is required. One or more key functions of a service or cluster is not working, or will stop working soon. A critical alert is important enough to page on-call staff and interrupt regular workflows.
Major:: Immediate action is strongly recommended. One or more key functions of the cluster will soon stop working. A major issue may lead to a critical issue if it is not addressed in a timely manner.
Warning:: Action is required as soon as possible. One or more key functions of the cluster are not working optimally and may degrade further, but do not pose an immediate danger to the functioning of the cluster.
Info:: No action necessary. This severity does not describe problems that need to be addressed, only important information about meaningful or important life cycle, service, or cluster events.
Debug:: No action necessary. Debug notifications provide low-level information about less important lifecycle, service, or cluster events to aid in debugging unexpected behavior.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-notifications.adoc
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="managed-cluster-notification-types_{context}"]
= Cluster notification types

[role="_abstract"]
Each cluster notification has an associated notification type to help you identify notifications that are relevant to your role and responsibilities.

Red{nbsp}Hat uses the following notification types to indicate notification relevance:

Capacity management:: Notifications for events related to updating, creating, or deleting node pools, machine pools, compute replicas or quotas (load balancer, storage, etc.).
Cluster access:: Notifications for events related to adding or deleting groups, roles or identity providers, for example, when SRE cannot access your cluster because STS credentials have expired, when there is a configuration problem with your AWS roles, or when you add or remove identity providers.
Cluster add-ons:: Notifications for events related to add-on management or upgrade maintenance for add-ons, for example, when an add-on is installed, upgraded, or removed, or cannot be installed due to unmet requirements.
Cluster configuration:: Notifications for cluster tuning events, workload monitoring, and inflight checks.
Cluster lifecycle:: Notifications for cluster or cluster resource creation, deletion, and registration, or change in cluster or resource status (for example, ready or hibernating).
Cluster networking:: Notifications related to cluster networking, including HTTP/S proxy, router, and ingress state.
Cluster ownership:: Notifications related to cluster ownership transfer from one user to another.
Cluster scaling:: Notifications related to updating, creating, or deleting node pools, machine pools, compute replicas or quota.
Cluster security:: Events related to cluster security, for example, an increased number of failed access attempts, updates to trust bundles, or software updates with security impact.
Cluster subscription:: Cluster expiration, trial cluster notifications, or switching from free to paid.
Cluster updates:: Anything relating to upgrades, such as upgrade maintenance or enablement.
Customer support:: Updates on support case status.
General notification:: The default notification type. This is only used for notifications that do not have a more specific category.
// Omitted, as no definition provided as part of OSDOCS-8938
// cluster-state-updates
// clustercreate-details
// clustercreate-high-level
// clusterremove-details
// clusterremove-high-level

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-notifications.adoc
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="managed-cluster-notification-view-hcc_{context}"]
= View cluster notifications using the {hybrid-console}

[role="_abstract"]
Cluster notifications give important information about the health of your cluster. You can view notifications sent to your cluster in the **Cluster history** tab on the {hybrid-console}.

.Prerequisites
* You have logged in to the {hybrid-console-second}.

.Procedure
. Navigate to the Clusters page of the {hybrid-console-second}.
. Click the name of your cluster to go to the cluster details page.
. Click the **Cluster history** tab.
+
Cluster notifications appear under the Cluster history heading.
. Optional: Filter for relevant cluster notifications.
+
Use the filter controls to hide cluster notifications that are not relevant to you, so that you can focus on your area of expertise or on resolving a critical issue. You can filter notifications based on text in the notification description, severity level, notification type, when you received the notification, and the system or person that triggered the notification.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="add-notification-contact_{context}"]
= Add notification contacts to your cluster

[role="_abstract"]
Configure additional users as notification contacts to ensure that all appropriate users receive cluster notification emails.

.Prerequisites
* Your cluster is deployed and registered to the {hybrid-console}.
* You are logged in to the {hybrid-console-second} as the cluster owner or as a user with the cluster editor role.
* The intended notification recipient has a Red{nbsp}Hat Customer Portal account associated with the same organization as the cluster owner.

.Procedure
. Navigate to the Clusters page of the {hybrid-console-second}.
. Click the name of your cluster to go to the cluster details page.
. Click the **Support** tab.
. On the **Support** tab, find the **Notification contacts** section.
. Click **Add notification contact**.
. In the **Red{nbsp}Hat username or email** field, enter the email address or the user name of the new recipient.
//. In the type field, select the types of cluster notification to send to this recipient.
. Click **Add contact**.

.Verification

* The "Notification contact added successfully" message is displayed.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-notifications.adoc
// * osd_cluster_admin/osd-cluster-notifications.adoc

[id="remove-notification-contact_{context}"]
= Remove notification contacts from your cluster

[role="_abstract"]
Remove notification contacts from your cluster support settings to prevent them from receiving notification emails.

.Prerequisites
* Your cluster is deployed and registered to the {hybrid-console}.
* You are logged in to the {hybrid-console-second} as the cluster owner or as a user with the cluster editor role.

.Procedure
. Navigate to the Clusters page of the {hybrid-console-second}.
. Click the name of your cluster to go to the cluster details page.
. Click the **Support** tab.
. On the **Support** tab, find the **Notification contacts** section.
. Click the options menu (**&#9881;**) beside the recipient you want to remove.
. Click **Delete**.

.Verification

* The "Notification contact deleted successfully" message is displayed.

[role="_additional-resources"]
== Additional resources

* Customer responsibilities: Review and action cluster notifications
* Red Hat Customer Portal account management
