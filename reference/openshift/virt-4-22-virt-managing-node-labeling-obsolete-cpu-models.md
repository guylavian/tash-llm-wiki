---
title: "Managing node labeling for obsolete CPU models"
type: reference
domain: openshift
slug: virt-4-22-virt-managing-node-labeling-obsolete-cpu-models
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-managing-node-labeling-obsolete-cpu-models
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing node labeling for obsolete CPU models

[id="virt-managing-node-labeling-obsolete-cpu-models"]
= Managing node labeling for obsolete CPU models

[role="_abstract"]
You can schedule a virtual machine (VM) on a node if the VM CPU model and policy are supported by the node.

// Module included in the following assemblies:
// * virt/nodes/virt-managing-node-labeling-obsolete-cpu-models.adoc

[id="virt-about-node-labeling-obsolete-cpu-models_{context}"]
= About node labeling for obsolete CPU models

[role="_abstract"]
The {VirtProductName} Operator uses a predefined list of obsolete CPU models to ensure that a node supports only valid CPU models for scheduled VMs.

By default, the following CPU models are eliminated from the list of labels generated for the node:

.Obsolete CPU models
[%collapsible]
====
----
"486"
Conroe
athlon
core2duo
coreduo
kvm32
kvm64
n270
pentium
pentium2
pentium3
pentiumpro
phenom
qemu32
qemu64
----
====

This predefined list is not visible in the `HyperConverged` CR. You cannot _remove_ CPU models from this list, but you can add to the list by editing the `spec.obsoleteCPUs.cpuModels` field of the `HyperConverged` CR.

// Module included in the following assemblies:
//
// * virt/nodes/virt-managing-node-labeling-obsolete-cpu-models.adoc

[id="virt-configuring-obsolete-cpu-models_{context}"]
= Configuring obsolete CPU models

[role="_abstract"]
You can configure a list of obsolete CPU models by editing the `HyperConverged` custom resource (CR).

.Procedure

* Edit the `HyperConverged` custom resource, specifying the obsolete CPU models in the `obsoleteCPUs` array. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  obsoleteCPUs:
    cpuModels:
      - "<obsolete_cpu_1>"
      - "<obsolete_cpu_2>"
----
+
Replace the example values in the `cpuModels` array with obsolete CPU models. Any value that you specify is added to a predefined list of obsolete CPU models. The predefined list is not visible in the CR.
