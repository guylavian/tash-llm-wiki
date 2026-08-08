---
title: "Assigning compute resources"
type: reference
domain: openshift
slug: virt-4-22-virt-assigning-compute-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-assigning-compute-resources
version: 4.22
family: virt
documentKind: "Documentation"
---

# Assigning compute resources

[id="virt-assigning-compute-resources"]
= Assigning compute resources

[role="_abstract"]
In {VirtProductName}, compute resources assigned to virtual machines (VMs) are backed by either guaranteed CPUs or time-sliced CPU shares.

Guaranteed CPUs, also known as CPU reservation, dedicate CPU cores or threads to a specific workload, which makes them unavailable to any other workload. Assigning guaranteed CPUs to a VM ensures that the VM will have sole access to a reserved physical CPU. Enable dedicated resources for VMs to use a guaranteed CPU.

Time-sliced CPUs dedicate a slice of time on a shared physical CPU to each workload. You can specify the size of the slice during VM creation, or when the VM is offline. By default, each vCPU receives 100 milliseconds, or 1/10 of a second, of physical CPU time.

The type of CPU reservation depends on the instance type or VM configuration.

[role="_overcommitting"]
[id="overcommitting_{context}"]
== Overcommitting CPU resources

Time-slicing allows multiple virtual CPUs (vCPUs) to share a single physical CPU. This is known as _CPU overcommitment_. Guaranteed VMs can not be overcommitted.

Configure CPU overcommitment to prioritize VM density over performance when assigning CPUs to VMs. With a higher CPU over-commitment of vCPUs, more VMs fit onto a given node.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-assigning-compute-resources.adoc

[id="virt-setting-cpu-allocation-ratio_{context}"]
= Setting the CPU allocation ratio

[role="_abstract"]
The CPU Allocation Ratio specifies the degree of overcommitment by mapping vCPUs to time slices of physical CPUs.

For example, a mapping or ratio of 10:1 maps 10 virtual CPUs to 1 physical CPU by using time slices.

To change the default number of vCPUs mapped to each physical CPU, set the `vmiCPUAllocationRatio` value in the `HyperConverged` CR. The pod CPU request is calculated by multiplying the number of vCPUs by the reciprocal of the CPU allocation ratio. For example, if `vmiCPUAllocationRatio` is set to 10, {VirtProductName} will request 10 times fewer CPUs on the pod for that VM.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Set the `vmiCPUAllocationRatio`:

+
[source,yaml]
----
...
spec:
  resourceRequirements:
    vmiCPUAllocationRatio: 1
# ...
----
+
When `vmiCPUAllocationRatio` is set to `1`, the maximum amount of vCPUs are requested for the pod.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Enabling dedicated resources for virtual machines
* Pod Quality of Service Classes
