---
title: "Tutorial: Simple UI guide"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-simple-ui-guide
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-simple-ui-guide
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Simple UI guide

[id="cloud-experts-getting-started-simple-ui-guide"]
= Tutorial: Simple UI guide

[role="_abstract"]
This page outlines the minimum list of commands to deploy a OpenShift Container Platform cluster using the user interface (UI).

[NOTE]
====
While this simple deployment works well for a tutorial setting, clusters used in production should be deployed with a more detailed method.
====

== Prerequisites

* You have completed the prerequisites in the Setup tutorial.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-simple-ui-guide.adoc// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-simple-ui-guide.adoc

[id="cloud-experts-getting-started-simple-guide-create_{context}"]
= Creating required cluster creation roles

[role="_abstract"]
You create your required cluster creation roles using {rosa-cli-first}.

.Procedure
. Run the following command _once_ for each AWS account and y-stream OpenShift version:
+
[source,terminal]
----
rosa create account-roles --mode auto --yes
----

. Create one {cluster-manager} role for each AWS account by running the following command:
+
[source,terminal]
----
rosa create ocm-role --mode auto --admin --yes
----

. Create one {cluster-manager} user role for each AWS account by running the following command:
+
[source,terminal]
----
rosa create user-role --mode auto --yes
----

. Use the {cluster-manager-url} to select your AWS account, cluster options, and begin deployment.

. {cluster-manager} UI displays cluster status.
+
image:cloud-experts-getting-started-deployment-ui-cluster-create.png[]
