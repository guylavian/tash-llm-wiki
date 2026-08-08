---
title: "Deleting access to a ROSA cluster"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-deleting-access-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-deleting-access-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Deleting access to a ROSA cluster

[id="rosa-deleting-access-cluster"]
= Deleting access to a ROSA cluster

[role="_abstract"]
Delete access to a OpenShift Container Platform cluster using the {rosa-cli}.

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
