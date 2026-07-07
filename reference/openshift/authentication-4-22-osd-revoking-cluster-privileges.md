---
title: "Revoking privileges and access to an {product-title} cluster"
type: reference
domain: openshift
slug: authentication-4-22-osd-revoking-cluster-privileges
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/osd-revoking-cluster-privileges
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Revoking privileges and access to an {product-title} cluster

[id="osd-revoking-cluster-privileges"]
= Revoking privileges and access to an OpenShift Container Platform cluster

[role="_abstract"]
As a cluster owner, you can revoke admin privileges and user access to a OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/osd-revoking-cluster-privileges.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="osd-revoke-admin-privileges_{context}"]
= Revoking administrator privileges from a user

[role="_abstract"]
After you have granted `dedicated-admin` privileges to a user, you can revoke those privileges when they are no longer needed.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.
* You granted `dedicated-admin` privileges to a user.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Click the *Access control* tab.

. In the *Cluster Roles and Access* tab, select {kebab} next to a user and click *Delete*.

.Verification

* After revoking the privileges, the user is no longer listed as part of the `dedicated-admins` group under *Access control* -> *Cluster Roles and Access* on the {cluster-manager} page for your cluster.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/osd-revoking-cluster-privileges.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="osd-revoke-user-access_{context}"]
= Revoking user access to a cluster

[role="_abstract"]
You can revoke cluster access from an identity provider user by removing them from your configured identity provider.

You can configure different types of identity providers for your OpenShift Container Platform cluster. The following example procedure revokes cluster access for a member of a GitHub organization or team that is configured for identity provision to the cluster.

.Prerequisites

* You have an OpenShift Container Platform cluster.
* You have a GitHub user account.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.

.Procedure

. Navigate to github.com and log in to your GitHub account.

. Remove the user from your GitHub organization or team:
* If your identity provider configuration uses a GitHub organization, follow the steps in Removing a member from your organization in the GitHub documentation.
* If your identity provider configuration uses a team within a GitHub organization, follow the steps in Removing organization members from a team in the GitHub documentation.

.Verification

* After removing the user from your identity provider, the user cannot authenticate into the cluster.
