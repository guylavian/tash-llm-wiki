---
title: "Creating an admin user"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-admin
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-admin
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Creating an admin user

[id="learning-getting-started-admin"]
= Creating an admin user

[role="_abstract"]
Creating an administration (admin) user provides several key capabilities for cluster management and allows you to access your cluster quickly. Follow these steps to create an admin user.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-admin.adoc
[id="learning-getting-started-admin-cli_{context}"]
= Creating an admin user using the CLI

[role="_abstract"]
You can use the {rosa-cli-first} to create an admin user for your clusters. Admin users perform tasks such as creating new clusters, scheduling cluster upgrades, monitoring health, and managing cluster resources.

[NOTE]
====
An admin user works well in this tutorial setting. For actual deployment, use a formal identity provider to access the cluster and grant the user admin privileges. For more information on identity providers, see the _Additional resources_ section.
====

.Procedure
. Run the following command to create the admin user:
+
[source,terminal]
----
$ rosa create admin --cluster=<cluster-name>
----
+
*Example output*:
+
[source,terminal]
----
W: It is recommended to add an identity provider to login to this cluster. See 'rosa create idp --help' for more information.
I: Admin account has been added to cluster 'my-rosa-cluster'. It may take up to a minute for the account to become active.
I: To login, run the following command:
oc login https://api.my-rosa-cluster.abcd.p1.openshiftapps.com:6443 \
--username cluster-admin \
--password FWGYL-2mkJI-00000-00000
----

. Copy the log in command returned to you in the previous step and paste it into your terminal. This will log you in to the cluster using the CLI so you can start using the cluster.
+
[source,terminal]
----
$ oc login https://api.my-rosa-cluster.abcd.p1.openshiftapps.com:6443 \
>    --username cluster-admin \
>    --password FWGYL-2mkJI-00000-00000
----
+
*Example output*:
+
[source,terminal]
----
Login successful.

You have access to 79 projects, the list has been suppressed. You can list all projects with ' projects'

Using project "default".
----

. To check that you are logged in as the admin user, run one of the following commands:
+
* Option 1:
+
[source,terminal]
----
$ oc whoami
----
+
*For example*:
+
[source,terminal]
----
cluster-admin
----
+
* Option 2:
+
[source,terminal]
----
oc get all -n openshift-apiserver
----
+
Only an admin user can run this command without errors.

[role="_additional-resources"]
== Additional resources

* Identity providers
