---
title: "Tutorial: Deleting your cluster"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-deleting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-deleting
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Deleting your cluster

[id="cloud-experts-getting-started-deleting"]
= Tutorial: Deleting your cluster

[role="_abstract"]
You can delete your OpenShift Container Platform cluster using either the command-line interface (CLI) or the user interface (UI).

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deleting.adoc

[id="cloud-experts-getting-started-deleting-cli_{context}"]
= Deleting a OpenShift Container Platform cluster using the CLI

[role="_abstract"]
You can delete your cluster by using the {rosa-cli-first} tool.

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
All AWS STS and IAM roles and policies will remain and must be deleted manually once the cluster deletion is complete by following the steps below.
====

. The CLI outputs the commands to delete the OpenID Connect (OIDC) provider and Operator IAM roles resources that were created. Wait until the cluster finishes deleting before deleting these resources. Perform a quick status check by running the following command:
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
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deleting.adoc

[id="cloud-experts-getting-started-deleting-ui_{context}"]
= Deleting a OpenShift Container Platform cluster using the UI

[role="_abstract"]
You can delete your cluster by using {cluster-manager}.

.Procedure
. Log in to the {cluster-manager-url}, and locate the cluster you want to delete.

. Click the three dots to the right of the cluster.
+
image::cloud-experts-getting-started-deleting1.png[]

. In the dropdown menu, click *Delete cluster*.
+
image::cloud-experts-getting-started-deleting2.png[]

. Enter the name of the cluster to confirm deletion, and click *Delete*.
