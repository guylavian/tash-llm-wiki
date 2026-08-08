---
title: "Deleting your cluster"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-deleting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-deleting
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Deleting your cluster

[id="learning-getting-started-deleting"]
= Deleting your cluster

[role="_abstract"]
You might want to delete your OpenShift Container Platform cluster if you created it for testing purposes only or no longer need it for other reasons. You can delete your cluster using either the {rosa-cli-first} or the user interface (UI).

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-deleting-cli_{context}"]
= Deleting a OpenShift Container Platform cluster using the {rosa-cli}

[role="_abstract"]
To free up system resources and avoid unnecessary costs when an environment is no longer needed, you can delete your OpenShift Container Platform cluster. You can easily perform this complete removal process by using the {rosa-cli-first}.

.Procedure
. *Optional:* List your clusters to make sure you are deleting the correct one by running the following command:
+
[source,terminal]
----
$ rosa list clusters
----

. Delete a cluster by running the following command:
+
[source,terminal]
----
$ rosa delete cluster --cluster <cluster-name>
----
+
[WARNING]
====
This command is non-recoverable.
====

. The CLI prompts you to confirm that you want to delete the cluster. Press *y* and then *Enter*. The cluster and all its associated infrastructure will be deleted.
+
[NOTE]
====
All AWS Security Token Service (STS) and Identity and Access Managmenet (IAM) roles and policies will remain and must be deleted manually once the cluster deletion is complete by following the steps below.
====

. The {rosa-cli} outputs the commands to delete the OpenID Connect (OIDC) provider and Operator IAM roles resources that were created. Wait until the cluster finishes deleting before deleting these resources. Perform a quick status check by running the following command:
+
[source,terminal]
----
$ rosa list clusters
----

. Once the cluster is deleted, delete the OIDC provider by running the following command:
+
[source,terminal]
----
$ rosa delete oidc-provider -c <clusterID> --mode auto --yes
----

. Delete the Operator IAM roles by running the following command:
+
[source,terminal]
----
$ rosa delete operator-roles -c <clusterID> --mode auto --yes
----
+
[NOTE]
====
This command requires the cluster ID and not the cluster name.
====

. Only remove the remaining account roles if they are no longer needed by other clusters in the same account. If you want to create other OpenShift Container Platform clusters in this account, do not perform this step.
+
To delete the account roles, you need to know the prefix used when creating them. The default is "ManagedOpenShift" unless you specified otherwise.
+
Delete the account roles by running the following command:
+
[source,terminal]
----
$ rosa delete account-roles --prefix <prefix> --mode auto --yes
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-deleting-web-ui_{context}"]
= Deleting a OpenShift Container Platform cluster using the UI

[role="_abstract"]
To free up system resources when an environment is no longer needed, you can delete your OpenShift Container Platform cluster by using the {cluster-manager}.

.Procedure
. Log in to the {cluster-manager-url}, and locate the cluster you want to delete.

. Click the three dots to the right of the cluster.
+
image::cloud-experts-getting-started-deleting1.png[]

. In the dropdown menu, click *Delete cluster*.
+
image::cloud-experts-getting-started-deleting2.png[]

. Enter the name of the cluster to confirm deletion, and click *Delete*.
