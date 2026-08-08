---
title: "Destroying a hosted cluster on bare metal"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-destroy-bm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-destroy-bm
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Destroying a hosted cluster on bare metal

[id="hcp-destroy-bm"]
= Destroying a hosted cluster on bare metal

[role="_abstract"]
You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-bm.adoc

[id="destroy-hc-bm-cli_{context}"]
= Destroying a hosted cluster on bare metal by using the CLI

[role="_abstract"]
If you created a hosted cluster by using the command-line interface (CLI), you can destroy that hosted cluster and its back-end resources by running a command.

.Procedure

* Delete the hosted cluster and its back-end resources by running the following command:
+
[source,terminal]
----
$ oc delete -f <hosted_cluster_config>.yaml
----
+
Specify the name of the configuration YAML file that was rendered when you created the hosted cluster.
+
[NOTE]
====
If you created the hosted cluster without specifying the `--render` and `--render-sensitive` flags in its configuration file, you must remove its back-end resources manually.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-bm.adoc

[id="destroy-hc-bm-console_{context}"]
= Destroying a hosted cluster on bare metal by using the web console

[role="_abstract"]
You can use the {mce-short} web console to destroy a hosted cluster on bare metal.

.Procedure

. In the console, click *Infrastructure* -> *Clusters*.

. On the *Clusters* page, select the cluster that you want to destroy.

. In the *Actions* menu, select *Destroy clusters* to remove the cluster.
