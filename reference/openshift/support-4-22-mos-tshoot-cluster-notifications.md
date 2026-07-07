---
title: "Review your cluster notifications"
type: reference
domain: openshift
slug: support-4-22-mos-tshoot-cluster-notifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/mos-tshoot-cluster-notifications
version: 4.22
family: support
documentKind: "Documentation"
---

# Review your cluster notifications

[id="mos-tshoot-cluster-notifications"]
= Review your cluster notifications

[role="_abstract"]
Use cluster notifications to help you resolve cluster problems. Cluster notifications are messages about the status, health, or performance of your cluster. Red Hat Site Reliability Engineering (SRE) uses these notifications to communicate about the health and problem resolution of your clusters.

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
