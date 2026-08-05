---
title: "Granting admin privileges"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-admin-rights
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-admin-rights
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Granting admin privileges

[id="learning-getting-started-admin-rights"]
= Granting admin privileges

[role="_abstract"]
Administration (admin) privileges are not automatically granted to users that you add to your cluster. If you want to grant admin-level privileges to certain users, you will need to manually grant them to each user. You can grant admin privileges from either the {rosa-cli-first} or the {cluster-manager-first} web user interface (UI).

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-admin-rights.adoc
[id="learning-getting-started-admin-rights-cli_{context}"]
= Using the {rosa-cli}

[role="_abstract"]
To allow specific users to manage your environment, you can use the {rosa-cli} to grant administrative access to your user roles. Assigning these permissions ensures that authorized team members can effectively configure and monitor your cluster's resources.

Red{nbsp}Hat offers two types of admin privileges:

* `cluster-admin`: `cluster-admin` privileges give the admin user full privileges within the cluster.

* `dedicated-admin`: `dedicated-admin` privileges allow the admin user to complete most administrative tasks with certain limitations to prevent cluster damage. For best practice use `dedicated-admin` when elevated privileges are needed.

.Procedure
. Assuming you are the user who created the cluster, run one of the following commands to grant admin privileges:
+
* For `cluster-admin`:
+
[source,terminal]
----
$ rosa grant user cluster-admin --user <idp_user_name> --cluster=<cluster-name>
----
+
* For `dedicated-admin`:
+
[source,terminal]
----
$ rosa grant user dedicated-admin --user <idp_user_name> --cluster=<cluster-name>
----

. Verify that the admin privileges were added by running the following command:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster-name>
----
+
*Example output*:
+
[source,terminal]
----
$ rosa list users --cluster=my-rosa-cluster
ID                 GROUPS
<idp_user_name>    cluster-admins
----

. If you are currently logged into the {hybrid-console}, log out of the console and log back in to the cluster to see a new perspective with the "Administrator Panel". You might need an incognito or private window.
+
image:cloud-experts-getting-started-admin-rights-admin-panel.png[]

. You can also test that admin privileges were added to your account by running the following command. Only a `cluster-admin` users can run this command without errors.
+
[source,terminal]
----
$ oc get all -n openshift-apiserver
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-admin-rights.adoc
[id="learning-getting-started-admin-rights-web-ui_{context}"]
= Using the Red{nbsp}Hat {cluster-manager}

[role="_abstract"]
You can grant cluster administrative access by using the {cluster-manager}. Users with administrative access can create new clusters, schedule cluster upgrades, monitor health, and manage cluster resources.

.Procedure
. Log in to the {cluster-manager-url}.
. Select your cluster.
. Click the *Access control* tab.
. Click the *Cluster roles and Access* tab in the sidebar.
. Click *Add user*.
+
image::cloud-experts-getting-started-admin-rights-access-control.png[]

. On the pop-up screen, enter the user ID.
. Select whether you want to grant the user `cluster-admins` or `dedicated-admins` privileges.
+
image::cloud-experts-getting-started-admin-rights-add-user2.png[]

[role="_additional-resources"]
== Additional resources

* Granting cluster-admin access
