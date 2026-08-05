---
title: "Cluster notifications"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-cluster-notifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-cluster-notifications
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Cluster notifications

[id="rosa-cluster-notifications"]
= Cluster notifications

[role="_abstract"]
Use the following resources and information to understand the cluster notifications that you receive for your OpenShift Container Platform cluster, and to manage the recipients of cluster notification emails.

[id="rosa-expectations_{context}"]
= What to expect from cluster notifications

[role="_abstract"]
As a cluster administrator, you need to be aware of when and why cluster notifications are sent, as well as their types and severity levels, in order to effectively understand the health and administration needs of your cluster.

[id="rosa-cluster-notification-emails_{context}"]
= Cluster notification emails

[role="_abstract"]
By default, when a cluster notification is sent to the cluster, it is also sent as an email to the cluster owner. You can configure additional recipients for notification emails to ensure that all appropriate users remain informed about the state of the cluster.

[id="rosa-troubleshooting-cluster-notifications_{context}"]
= Troubleshooting cluster notifications

[role="_abstract"]
If you are not receiving cluster notification emails, you can troubleshoot the issue by completing the following steps.

* Ensure that emails sent from `@redhat.com` addresses are not filtered out of your email inbox.
* Ensure that your correct email address is listed as a notification contact for the cluster.
* Ask the cluster owner or administrator to add you as a notification contact.

If your cluster does not receive notifications:

* Ensure that your cluster can access resources at `api.openshift.com`.

[role="_additional-resources"]
.Additional resources

* Customer responsibilities: Review and action cluster notifications
