---
title: "Tutorial: Simple CLI guide"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-simple-cli-guide
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-simple-cli-guide
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Simple CLI guide

[id="cloud-experts-getting-started-simple-cli-guide"]
= Tutorial: Simple CLI guide

[role="_abstract"]
This page outlines the minimum list of commands to deploy a OpenShift Container Platform (ROSA) cluster using the command-line interface (CLI).

[NOTE]
====
While this simple deployment works well for a tutorial setting, clusters used in production should be deployed with a more detailed method.
====

== Prerequisites

* You have completed the prerequisites in the Setup tutorial.

== Creating account roles
Run the following command _once_ for each AWS account and y-stream OpenShift version:

[source,terminal]
----
rosa create account-roles --mode auto --yes
----

== Deploying the cluster

. Create the cluster with the default configuration by running the following command substituting your own cluster name:
+
[source,terminal]
----
rosa create cluster --cluster-name <cluster-name> --sts --mode auto --yes
----

. Check the status of your cluster by running the following command:
+
[source,terminal]
----
rosa list clusters
----
