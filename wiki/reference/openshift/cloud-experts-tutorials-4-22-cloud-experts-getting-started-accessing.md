---
title: "Tutorial: Accessing your cluster"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-accessing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-accessing
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Accessing your cluster

[id="cloud-experts-getting-started-accessing"]
= Tutorial: Accessing your cluster

[role="_abstract"]
You can connect to your cluster using the {rosa-cli-first} or the {hybrid-console} user interface (UI).

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-accessing.adoc

[id="cloud-experts-getting-started-accessing-cli_{context}"]
= Accessing your cluster using the CLI

[role="_abstract"]
To access the cluster using the CLI, you must have the `oc` CLI installed. If you are following the tutorials, you already installed the `oc` CLI.

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
**Example output**
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
**Example output**
+
[source,terminal]
----
rosa-user
----

. You can now access your cluster.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-accessing.adoc

[id="cloud-experts-getting-started-accessing-ui_{context}"]
= Accessing the cluster via the {hybrid-console-second}

[role="_abstract"]
Access your OpenShift Container Platform cluster through the {hybrid-console-second} web interface by logging in with your identity provider credentials.

.Procedure
. Log in to the {cluster-manager-url}.
.. To retrieve the {hybrid-console-second} URL run:
+
[source,terminal]
----
rosa describe cluster -c <cluster-name> | grep Console
----

. Click your IDP. For example, "rosa-github".
+
image::cloud-experts-getting-started-accessing-copy-token.png[]

. Enter your user credentials.
. You should be logged in. If you are following the tutorials, you will be a cluster-admin and should see the {hybrid-console-second} webpage with the *Administrator* panel visible.
+
image::cloud-experts-getting-started-accessing-logged.png[]
