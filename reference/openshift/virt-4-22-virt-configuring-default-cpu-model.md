---
title: "Configure CPU models"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-default-cpu-model
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-default-cpu-model
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configure CPU models

[id="virt-configuring-default-cpu-model"]
= Configure CPU models

[role="_abstract"]
You can configure CPU models for your virtual machines at both the cluster level and individual VM level. Set a cluster-wide default CPU model to automatically apply to all new VMs, or configure a specific CPU model for individual VMs to override the cluster default.

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-configuring-default-cpu-model.adoc

[id="virt-configuring-default-cpu-model_{context}"]
= Configure the default CPU model

[role="_abstract"]
Use the `defaultCPUModel` setting in the `HyperConverged` custom resource (CR) to define a cluster-wide default CPU model.

When you set a cluster-wide default CPU model:

* Every new virtual machine (VM) that does not have an explicit CPU model defined receives a node selector for the chosen CPU model.
* Only nodes labeled with `cpu-model.node.kubevirt.io/<cpuModel>` are eligible to run VMs using the default model.
* Nodes that do not support the selected CPU model are not considered during VM scheduling.

[NOTE]
====
The `defaultCPUModel` is case sensitive and must match a CPU model supported by nodes in your cluster.
====

A CPU model configured at the VM level always takes precedence over the cluster-wide default CPU model.

.Prerequisites

* Install the {oc-first}.

.Procedure

. Open the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `defaultCPUModel` field to the CR and set the value to the name of a CPU model that exists in the cluster:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
 name: kubevirt-hyperconverged
 namespace: {CNVNamespace}
spec:
  defaultCPUModel: "EPYC-IBPB"
----
+
where:
+
`EPYC-IBPB`:: Specifies a CPU model that is supported by nodes in your cluster.

. Apply the YAML file to your cluster.

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-configuring-default-cpu-model.adoc

[id="virt-per-vm-cpu-model-configuration_{context}"]
= Configure a CPU model per-VM

[role="_abstract"]
You can specify a named CPU model in the virtual machine (VM) specification. This per-VM configuration takes precedence over any cluster-wide default CPU model.

The VM CPU model depends on the availability of CPU models within the VM and the cluster.

* If the VM does not have a defined CPU model, the `defaultCPUModel` is automatically set using the CPU model defined at the cluster-wide level.
* If both the VM and the cluster have a defined CPU model, the VM’s CPU model takes precedence.
* If neither the VM nor the cluster have a defined CPU model, the host-model is automatically set using the CPU model defined at the host level.

.Prerequisites

* Install the {oc-first}.

.Procedure

. To configure a named CPU model for a specific VM, edit the `VirtualMachine` custom resource (CR):
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          model: Conroe
----
+
* `spec.template.spec.domain.cpu.model` defines the named CPU model for the VM.

. Apply the CR to your cluster.
