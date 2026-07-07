---
title: "Preventing node reconciliation"
type: reference
domain: openshift
slug: virt-4-22-virt-preventing-node-reconciliation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-preventing-node-reconciliation
version: 4.22
family: virt
documentKind: "Documentation"
---

# Preventing node reconciliation

[id="virt-using-skip-node"]
= Preventing node reconciliation

[role="_abstract"]
Use `skip-node` annotation to prevent the `node-labeller` from reconciling a node.

// Module included in the following assembly:
//
// * virt/nodes/virt-preventing-node-reconciliation.adoc
//

[id="virt-using-skip-node_{context}"]
= Using skip-node annotation

[role="_abstract"]
If you want the `node-labeller` to skip a node, annotate that node by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Annotate the node that you want to skip by running the following command:
+
[source,terminal]
----
$ oc annotate node <node_name> node-labeller.kubevirt.io/skip-node=true
----
+
Replace `<node_name>` with the name of the relevant node to skip.
+
Reconciliation resumes on the next cycle after the node annotation is removed or set to false.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Managing node labeling for obsolete CPU models
