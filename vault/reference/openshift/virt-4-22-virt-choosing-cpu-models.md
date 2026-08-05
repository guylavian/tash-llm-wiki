---
title: "Choose a CPU model"
type: reference
domain: openshift
slug: virt-4-22-virt-choosing-cpu-models
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-choosing-cpu-models
version: 4.22
family: virt
documentKind: "Documentation"
---

# Choose a CPU model

[id="virt-choosing-cpu-models"]
= Choose a CPU model

[role="_abstract"]
You can select the appropriate CPU model for your virtual machines based on your cluster configuration. Choose between the host-model CPU, which provides maximum performance and feature access in homogeneous clusters, or named CPU models, which ensure compatibility and migration flexibility in heterogeneous clusters with different CPU types.

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc

[id="virt-about-host-model_{context}"]
= Host-model CPU

[role="_abstract"]
`host-model` is the default CPU configuration in {VirtProductName}. When a virtual machine instance (VMI) is created with `host-model`, libvirt automatically selects a CPU model that is closest to the physical CPU of the node where the VMI first runs. The host model required CPU features present on this initial node are included in the VMI's domain definition.

The CPU model chosen by `host-model` is often not a standard named model supported by libvirt, which may  include additional CPU features. Libvirt creates a CPU definition that only includes the available features on the initial node. This approach ensures:

* The VMI can start successfully on the initial node.
* Future live migrations only require the subset of CPU features used in the host-model, even if target nodes have different or additional features.

[id="virt-cpu-model-homogeneous-clusters_{context}"]
== Homogeneous clusters

In a homogeneous cluster, all nodes have similar CPU features. The `host-model` CPU model is recommended for homogeneous clusters, and provides the following benefits:

* Provides VMs with the closest match to the physical CPU.
* VMs can use all CPU features available on the nodes.
* Live migration works smoothly because all nodes share the same CPU features.

[id="live-migration-with-host-model_{context}"]
== Live migration with host-model

Since the CPU model and features are determined by the initial node, all the host model required CPU features exposed to the VMI must also exist on any future live migration target nodes.

{VirtProductName} ensures compatibility by:

. Detecting all `host-model-required-features.node.kubevirt.io/<cpuFeature>` labels on the initial node.
. Storing these labels per VMI.
. Using these same required CPU features to set node selectors for all future live migrations.

This approach guarantees that VM migrations only target nodes that provide the CPU features actually needed by the VMI.

[IMPORTANT]
====
Target nodes may support more CPU features than required, but they must support at minimum all features used by the VMI.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc

[id="virt-about-named-cpu-models_{context}"]
= Named CPU models

[role="_abstract"]
Named CPU models allow you to explicitly select a CPU type for a virtual machine (VM). You can configure a named CPU model at the VM level or set a cluster-wide default using the `HyperConverged` custom resource (CR).

A node supports a named CPU model only if it includes all required CPU features defined by libvirt for that model. Nodes that support a specific CPU model are labeled with `cpu-model.node.kubevirt.io/<cpuModel>`. {VirtProductName} uses these labels to schedule VMs only to compatible nodes. When you configure a named CPU model, the VM receives a node selector that ensures it only runs on nodes labeled with that specific CPU model.

[id="virt-cpu-model-heterogeneous-clusters_{context}"]
== Heterogeneous clusters

In a heterogeneous cluster, nodes have different CPU generations or feature sets.

A virtual machine instance (VMI) inherits the host model CPU feature of the node where it is first scheduled. If the initial node has CPU features unsupported by other nodes, it can prevent the VM from being migrated to them.

Using a common named CPU model (for example, `EPYC-IBPB` or `Haswell`) is recommended for  CPU models in heterogeneous clusters, and provides the following benefits:

* Ensures that all nodes selected for migration support the required CPU features.
* Maximizes VM migratability across nodes with different CPU types.
* Prevents scheduling VMs on nodes that cannot support live migration targets.

[IMPORTANT]
====
In heterogeneous clusters, using `host-model` can limit live migration options if the initial scheduling node has host model required CPU features that are not available on all other nodes in the cluster.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
