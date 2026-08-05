---
title: "Destroying a hosted control plane on OpenStack"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-destroy-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-destroy-openstack
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Destroying a hosted control plane on OpenStack

[id="hcp-destroy-openstack"]
= Destroying a hosted control plane on OpenStack

[role="_abstract"]
You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

// Module included in the following assemblies:
//
// * hosted_control_planes/hypershift-openstack.adoc

[id="hosted-clusters-openstack-destroy_{context}"]
= Destroying a hosted cluster by using the CLI

[role="_abstract"]
You can destroy a hosted cluster and its associated resources on {rh-openstack-first} by using the `hcp` CLI tool.

.Prerequisites

* You installed the hosted control planes CLI, `hcp`.

.Procedure

* To destroy the cluster and its associated resources, run the following command:
+
[source,terminal]
----
$ hcp destroy cluster openstack --name=<cluster_name>
----
+
Replace `<cluster_name>` with the name of the hosted cluster.
+
After the process completes, your cluster and all resources that are associated with it are destroyed.
