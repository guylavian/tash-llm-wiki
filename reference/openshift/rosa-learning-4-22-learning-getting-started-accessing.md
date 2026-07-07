---
title: "Accessing your cluster"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-accessing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-accessing
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Accessing your cluster

[id="learning-getting-started-accessing"]
= Accessing your cluster

[role="_abstract"]
You can connect to your cluster using the {rosa-cli-first} or the {hybrid-console} user interface (UI). You can use the {rosa-cli} to authenticate with your service account credentials, and the {hybrid-console} to connect by using a user ID and password that you retrieve through the console.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-accessing.adoc
[id="learning-getting-started-accessing-cli_{context}"]
= Accessing your cluster using the CLI

[role="_abstract"]
To access the cluster using the command line interface (CLI), you must have the `oc` CLI installed. With the `oc` CLI, you can work directly with project source code, and manage projects in bandwidth-restricted environments where the web console might be unavailable. If you are following the tutorials, you already installed the `oc` CLI.

.Procedure
. Log in to the {cluster-manager-url}.
. Click your username in the top right corner.
. Click *Copy Login Command*.
+
image::cloud-experts-getting-started-accessing-copy-login.png[]

. This opens a new tab with a choice of identity providers (IDPs). Click the IDP you want to use. For example, "rosa-github".
+
image::cloud-experts-getting-started-accessing-copy-token.png[]

. A new tab opens. Click *Display token*.

. Run the following command in your terminal:
+
[source,terminal]
----
$ oc login --token=sha256~GBAfS4JQ0t1UTKYHbWAK6OUWGUkdMGz000000000000 --server=https://api.my-rosa-cluster.abcd.p1.openshiftapps.com:6443
----
+
*Example output*:
+
[source,terminal]
----
Logged into "https://api.my-rosa-cluster.abcd.p1.openshiftapps.com:6443" as "rosa-user" using the token provided.

You have access to 79 projects, the list has been suppressed. You can list all projects with ' projects'

Using project "default".
----

. Confirm that you are logged in by running the following command:
+
[source,terminal]
----
$ oc whoami
----
+
*Example output*:
+
[source,terminal]
----
rosa-user
----

. You can now access your cluster.
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-accessing.adoc
[id="learning-getting-started-accessing-hcm_{context}"]
= Accessing the cluster via the {hybrid-console-second}

[role="_abstract"]
You can access your cluster by using the {hybrid-console-second}, which serves as a primary portal for managing OpenShift Container Platform environments. Use {hybrid-console-second} to access tools for cluster provisioning, registration, and health monitoring.

.Procedure
. Log in to the {cluster-manager-url}.
. To retrieve the {hybrid-console-second} URL run:
+
[source,terminal]
----
$ rosa describe cluster -c <cluster-name> | grep Console
----

. Click your IDP. For example, "rosa-github".
+
image::cloud-experts-getting-started-accessing-copy-token.png[]

. Enter your user credentials.
. You should be logged in. If you are following the tutorials, you will be a cluster-admin and should see the {hybrid-console-second} webpage with the *Administrator* panel visible.
+
image::cloud-experts-getting-started-accessing-logged.png[]
