---
title: "Revoking access to a ROSA cluster"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-sts-deleting-access-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Revoking access to a ROSA cluster

[id="rosa-sts-deleting-access-cluster"]
= Revoking access to a ROSA cluster

[role="_abstract"]
An identity provider (IDP) controls access to a OpenShift Container Platform cluster. To revoke access of a user to a cluster, you must configure that within the IDP that was set up for authentication.

[id="rosa-revoke-admin-access"]
== Revoking administrator access using the {rosa-cli}
You can revoke the administrator access of users so that they can access the cluster without administrator privileges. To remove the administrator access for a user, you must revoke the `dedicated-admin` or `cluster-admin` privileges. You can revoke the administrator privileges using the {rosa-cli-first}, or using {cluster-manager} console.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc

[id="rosa-delete-dedicated-admins_{context}"]
= Revoking `dedicated-admin` access using the ROSA CLI

[role="_abstract"]
You can revoke access for a `dedicated-admin` user if you are the user who created the cluster, the organization administrator user, or the super administrator user.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to the cluster.

.Procedure

. Enter the following command to revoke the `dedicated-admin` access of a user:
+
[source,terminal]
----
$ rosa revoke user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
. Enter the following command to verify that your user no longer has `dedicated-admin` access. The output does not list the revoked user.
+
[source,terminal]
----
$ oc get groups dedicated-admins
----

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc

[id="rosa-delete-cluster-admins_{context}"]
= Revoking `cluster-admin` access using the ROSA CLI

[role="_abstract"]
Only the user who created the cluster can revoke access for `cluster-admin` users.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to the cluster.

.Procedure

. Enter the following command to revoke the `cluster-admin` access of a user:
+
[source,terminal]
----
$ rosa revoke user cluster-admins --user=myusername --cluster=mycluster
----
+
. Enter the following command to verify that the user no longer has `cluster-admin` access. The output does not list the revoked user.
+
[source,terminal]
----
$ oc get groups cluster-admins
----

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc

[id="rosa-delete-users_{context}"]
= Revoking administrator access using {cluster-manager} console

[role="_abstract"]
You can revoke the `dedicated-admin` or `cluster-admin` access of users through {cluster-manager} console. Users will be able to access the cluster without administrator privileges.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to {cluster-manager} console using an {cluster-manager} account that you used to create the cluster, the organization administrator user, or the super administrator user.

.Procedure

. On the *Cluster List* tab of {cluster-manager}, select the name of your cluster to view the cluster details.
. Select *Access control* > *Cluster Roles and Access*.
. For the user that you want to remove, click the Options menu {kebab} to the right of the user and group combination and click *Delete*.
