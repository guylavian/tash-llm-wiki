---
title: "Destroying a hosted cluster on non-bare-metal agent machines"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-destroy-non-bm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-destroy-non-bm
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Destroying a hosted cluster on non-bare-metal agent machines

[id="hcp-destroy-non-bm"]
= Destroying a hosted cluster on non-bare-metal agent machines

[role="_abstract"]
You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-non-bm.adoc

[id="destroy-hc-non-bm-cli_{context}"]
= Destroying a hosted cluster on non-bare-metal agent machines

[role="_abstract"]
You can use the `hcp` command-line interface (CLI) to destroy a hosted cluster on non-bare-metal agent machines.

.Procedure

* Delete the hosted cluster and its backend resources by running the following command:
+
[source,terminal]
----
$ hcp destroy cluster agent --name <hosted_cluster_name>
----
+
Replace `<hosted_cluster_name>` with the name of your hosted cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-non-bm.adoc

[id="destroy-hc-non-bm-console_{context}"]
= Destroying a hosted cluster on non-bare-metal agent machines by using the web console

[role="_abstract"]
You can use the {mce-short} web console to destroy a hosted cluster on non-bare-metal agent machines.

.Procedure

. In the console, click *Infrastructure* -> *Clusters*.

. On the *Clusters* page, select the cluster that you want to destroy.

. In the *Actions* menu, select *Destroy clusters* to remove the cluster.
