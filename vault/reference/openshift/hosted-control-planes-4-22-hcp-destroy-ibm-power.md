---
title: "Destroying a hosted cluster on {ibm-power-title}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-destroy-ibm-power
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-destroy-ibm-power
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Destroying a hosted cluster on {ibm-power-title}

[id="hcp-destroy-ibm-power"]
= Destroying a hosted cluster on {ibm-power-title}

[role="_abstract"]
You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-destroy/hcp-destroy-ibm-power.adoc

[id="destroy-hc-ibm-power-cli_{context}"]
= Destroying a hosted cluster on {ibm-power-title} by using the CLI

[role="_abstract"]
To destroy a hosted cluster on {ibm-power-title}, you can use the hcp command-line interface (CLI).

.Procedure

* Delete the hosted cluster by running the following command:
+
[source,terminal]
----
$ hcp destroy cluster agent
 --name=<hosted_cluster_name> \
 --namespace=<hosted_cluster_namespace> \
 --cluster-grace-period <duration>
----
+
** `<hosted_cluster_name>` specifies the name of your hosted cluster.
** `<hosted_cluster_namespace>` specifies the name of your hosted cluster namespace.
** `<duration>` specifies the duration to destroy the hosted cluster completely, for example, `20m0s`.
