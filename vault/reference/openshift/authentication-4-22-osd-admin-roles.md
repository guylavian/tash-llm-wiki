---
title: "Managing administration roles and users"
type: reference
domain: openshift
slug: authentication-4-22-osd-admin-roles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/osd-admin-roles
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Managing administration roles and users

[id="osd-admin-roles"]
= Managing administration roles and users

[role="_abstract"]
Keep your OpenShift Container Platform cluster secure and up-to-date by managing administration roles and users effectively.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd-admin-roles.adoc

[id="understanding-admin-roles_{context}"]
= Understanding administration roles

[role="_abstract"]
As an administrator of an OpenShift Container Platform cluster, you have access to the `cluster-admin` and `dedicated-admin` roles. These roles have different permissions and access levels that allow you to manage and configure your cluster effectively. Understanding the differences between these roles can help you assign the appropriate permissions to users and manage your cluster more efficiently.

== The cluster-admin role
As an administrator of an OpenShift Container Platform cluster with Customer Cloud Subscriptions (CCS), you have access to the `cluster-admin` role. The user who created the cluster can add the `cluster-admin` user role to an account to have the maximum administrator privileges. These privileges are not automatically assigned to your user account when you create the cluster. While logged in to an account with the cluster-admin role, users have mostly unrestricted access to control and configure the cluster. There are some configurations that are blocked with webhooks to prevent destabilizing the cluster, or because they are managed in {cluster-manager-url} and any in-cluster changes would be overwritten. Usage of the cluster-admin role is subject to the restrictions listed in your Appendix 4 agreement with Red Hat. As a best practice, limit the number of `cluster-admin` users to as few as possible.

== The dedicated-admin role
As an administrator of an OpenShift Container Platform cluster, your account has additional permissions and access to all user-created projects in your organization’s cluster. While logged in to an account with the `dedicated-admin` role, the developer CLI commands (under the `oc` command) allow you increased visibility and management capabilities over objects across projects, while the administrator CLI commands (under the `oc adm` command) allow you to complete additional operations.

[NOTE]
====
While your account does have these increased permissions, the actual cluster maintenance and host configuration is still performed by the Red{nbsp}Hat Site Reliability Engineering (SRE) team.
====

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd-admin-roles.adoc

[id="managing-dedicated-administrators_{context}"]
=  Managing OpenShift Container Platform administrators

[role="_abstract"]
Administrator roles are managed using a `cluster-admin` or `dedicated-admin` group on the cluster. Existing members of this group can edit membership through {cluster-manager-url}.

.Procedure

. Navigate to the *Cluster Details* page and select the *Access Control* tab.
. Select the *Cluster Roles and Access* tab and click *Add user*.
. Enter the user name and select your group.
. Click *Add user*.
+
[NOTE]
====
Adding a user to the `cluster-admin` group can take several minutes to complete.
====
+
. Optional: To remove a OpenShift Container Platform administrator, click the Options menu {kebab} to the right of the user and group combination and click *Delete*.
