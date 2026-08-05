---
title: "Getting your node ID"
type: reference
domain: openshift
slug: microshift-support-4-22-microshift-getting-node-id
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_support/microshift-getting-node-id
version: 4.22
family: microshift_support
documentKind: "Documentation"
---

# Getting your node ID

[id="microshift-getting-node-id"]
= Getting your node ID

[role="_abstract"]
When providing information to Red{nbsp}Hat Support, it is helpful to provide the unique identifier of your node. For {microshift-short}, you can get your node ID manually by using the {oc-first} or by retrieving the ID from a file.

[NOTE]
====
A node ID is created only after the {microshift-short} service runs for the first time after installation.
====

// Module included in the following assemblies:
//
// microshift_support/microshift-getting-node-id.adoc

[id="microshift-get-node-id-kubesystem_{context}"]
= Getting the node ID of a running node

[role="_abstract"]
Retrieving the node ID enables you to uniquely identify a device within your deployment. The node ID is required to register the node with central management systems, analyze system logs and alerts, and ensure that configuration updates are targeted accurately.

.Procedure

* Get the ID of a running node using `oc get` by entering the following command:
+
[source,terminal]
----
$ oc get namespaces kube-system -o jsonpath={.metadata.uid}
----
.Example output
+
[source,terminal]
----
7cf13853-68f4-454e-8f5c-1af748cbfb1a
----

* Get the ID of a running node by retrieving it from the `cluster-id` file by entering the following command:
+
[source,terminal]
----
$ sudo cat /var/lib/microshift/cluster-id
----
.Example output
+
[source,terminal]
----
7cf13853-68f4-454e-8f5c-1af748cbfb1a
----

// Module included in the following assemblies:
//
// microshift_support/microshift-getting-node-id.adoc

[id="microshift-get-nonrunning-node-id-kubesystem_{context}"]
= Getting the node ID of a stopped node

When the MicroShift service is inactive, you can prevent the use of standard API commands by retrieving the node ID from the file system. You can use this ID to identify offline nodes for disaster recovery, verify backup compatibility, and troubleshoot issues.

.Procedure

* Get the ID of a stopped node by retrieving it from the `cluster-id` file by entering the following command:
+
[source,terminal]
----
$ sudo cat /var/lib/microshift/cluster-id
----
.Example output
+
[source,terminal]
----
7cf13853-68f4-454e-8f5c-1af748cbfb1a
----
