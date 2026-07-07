---
title: "Destroying a hosted cluster on {VirtProductName}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-destroy-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-destroy-virt
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Destroying a hosted cluster on {VirtProductName}

[id="hcp-destroy-virt"]
= Destroying a hosted cluster on {VirtProductName}

[role="_abstract"]
You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-virt.adoc

[id="destroy-hc-virt-cli_{context}"]
= Destroying a hosted cluster on {VirtProductName} by using the CLI

[role="_abstract"]
You can use the command-line interface (CLI) to destroy a hosted cluster and its managed cluster resource on {VirtProductName}.

.Procedure

. Delete the managed cluster resource on {mce-short} by running the following command:
+
[source,terminal]
----
$ oc delete managedcluster <hosted_cluster_name>
----

. Delete the hosted cluster and its backend resources by running the following command:
+
[source,terminal]
----
$ hcp destroy cluster kubevirt --name <hosted_cluster_name>
----
