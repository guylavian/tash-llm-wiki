---
title: "Working with NUMA topology for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-numa-topology
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-NUMA-topology
version: 4.22
family: virt
documentKind: "Documentation"
---

# Working with NUMA topology for virtual machines

[id="virt-NUMA-topology"]
= Working with NUMA topology for virtual machines

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-using-NUMA_{context}"]
= Using NUMA topology with {VirtProductName}

[role="_abstract"]
You must enable the NUMA functionality for {VirtProductName} VMs to prevent performance degradation on nodes with multiple NUMA zones. This feature is vital for high-performance and latency-sensitive workloads.

Without NUMA awareness, a VM's virtual CPUs might run on one physical NUMA zone, while its memory is allocated on another. This "cross-node" communication significantly increases latency and reduces memory bandwidth, and can cause the interconnect buses which link the NUMA zones to become a bottleneck.

When you enable the NUMA functionality for {VirtProductName} VMs, you allow the host to pass its physical topology directly to the VM's guest operating system (OS).
The guest OS can then make intelligent, NUMA-aware decisions about scheduling and memory allocation. This ensures that process threads and memory are kept on the same physical NUMA node. By aligning the virtual topology with the physical one, you minimize latency and maximize performance.

VM owners can enable NUMA with `ComputeExclusive` (CX) instance types, which are specifically designed for high-performance, compute-intensive workloads, and are configured to use NUMA features. For information about creating VMs using a CX instance type, see "Creating virtual machines from instance types".

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-NUMA-prereqs_{context}"]
= Prerequisites

[role="_abstract"]
Before you can enable NUMA functionality with {VirtProductName} VMs, you must ensure that your environment meets the following prerequisites.

* Worker nodes must have huge pages enabled.
* The `KubeletConfig` object on worker nodes must be configured with the `cpuManagerPolicy: static` spec to guarantee dedicated CPU allocation, which is a prerequisite for NUMA pinning.
+
Example `cpuManagerPolicy: static` spec:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: cpu-numa-static-config
spec:
  kubeletConfig:
    cpuManagerPolicy: static
# ...
----

// Module included in the following assemblies:
//
// * virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-numa-check-config_{context}"]
= Verifying vNUMA status of a VM

[role="_abstract"]
VM administrators might need to confirm whether non-uniform memory access (NUMA) is configured for a VM, to verify the VM's resource allocation setup for high-performance, latency-sensitive workloads that rely on memory locality.

You can verify whether an already deployed VM is configured for vNUMA by checking the `spec.domain.cpu.numa` attribute. This is displayed as a *vNUMA* badge in the OpenShift Container Platform web console.

.Prerequisites

* You have access to an OpenShift Container Platform cluster with {VirtProductName} installed.
* If you want to use the command line for verification, you must have installed the {oc-first}. Otherwise, you only need access to the OpenShift Container Platform web console.

.Procedure

* To verify vNUMA status on the command line, check that the `spec.domain.cpu.numa` attribute is configured by using the {oc-first}. Run the following command:
+
[source,terminal]
----
$ oc get vm <vm_name> -n <namespace> -o jsonpath='{.spec.template.spec.domain.cpu.numa}'
----
+
If any output other than an empty string is returned, vNUMA is enabled for the VM.

* To verify vNUMA status in a GUI, check if the VM has a *vNUMA* badge in the OpenShift Container Platform web console. Go to *VirtualMachines* -> *Virtual machines* -> *VirtualMachine details*, and check either the *Overview* or the *Configuration* tabs.

// Module included in the following assemblies:
//
// * virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-NUMA-topology-disabling-hotplugs_{context}"]
= Disabling the hot plug capability for VMs

[role="_abstract"]
_Hot plugging_ is the ability to dynamically add resources such as memory or CPU to a VM while it is running. Default {VirtProductName} hot plug multipliers can cause VMs to request an excessive number of sockets. For example, if your VM requests 10 sockets, the default hot plug behavior multiplies this by 4, which means that the total request is 40 sockets. This can exceed the recommended CPUs supported by the Kernel-based Virtual Machine (KVM), which can cause deployment failures.

You can keep VM resource requests aligned with NUMA and optimize performance for resource-intensive workloads by disabling the VM's default hot plug capability.

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-disable-CPU-VM-hotplug-instancetype_{context}"]
= Disabling the CPU hot plug by instance type

[role="_abstract"]
As a cluster administrator, you can disable the CPU hot plug by instance type.
This is the recommended approach to standardize VM configurations and ensure NUMA-aware CPU allocation without hot plugs for specific instance types.

When a VM is created by using an instance type where the CPU hot plug is disabled, the VM inherits these settings and the CPU hot plug is disabled for that VM.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Create a YAML file for a `VirtualMachineClusterInstancetype` custom resource (CR). Add a `maxSockets` spec to the instance type that you want to configure.
+
Example `VirtualMachineClusterInstancetype` CR:
+
[source,yaml]
----
apiVersion: instancetype.kubevirt.io/v1beta1
kind: VirtualMachineClusterInstancetype
metadata:
  name: cx1.mycustom-numa-instance
spec:
  cpu:
    dedicatedCPUPlacement: true
    isolateEmulatorThread: true
    numa:
      guestMappingPassthrough: {}
    guest: 8
    maxSockets: 8
  memory:
    guest: 16Gi
    hugepages:
      pageSize: 1Gi
----
+
where:
+
--
`spec.cpu.dedicatedCPUPlacement`:: Specifies whether dedicated resources are allocated to the VM instance. If this is set to `true`, the VM's VCPUs are pinned to physical host CPUs. This is often used for high-performance workloads to minimize scheduling jitter.

`spec.cpu.isolateEmulatorThread`:: Specifies whether the QEMU emulator thread should be isolated and run on a dedicated physical CPU core. This is a performance optimization that is typically used alongside the `dedicatedCPUPlacement` spec.

`spec.cpu.numa`:: Specifies the NUMA topology configuration for the VM.

`spec.cpu.numa.guestMappingPassthrough`:: Specifies that the VM's NUMA topology should directly pass through the NUMA topology of the underlying host machine. This is critical for applications that are NUMA-aware and require optimal performance.

`spec.cpu.guest`:: Specifies the total number of vCPUs to be allocated to the VM.

`spec.cpu.maxSockets`:: Specifies the maximum number of CPU sockets the VM is allowed to have.

`spec.memory`:: Specifies the memory configuration for the VM.

`spec.memory.guest`:: Specifies the total amount of memory to be allocated to the VM.

`spec.memory.hugepages`:: Specifies configuration related to hugepages.

`spec.memory.hugepages.pageSize`:: Specifies the size of the hugepages to be used for the VM's memory.
--

. Create the `VirtualMachineClusterInstancetype` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

.Verification

. Create a VM that uses the updated `VirtualMachineClusterInstancetype` configuration.

. Inspect the configuration of the created VM by running the following command and inspecting the output:
+
[source,terminal]
----
$ oc get vmi <vm_name> -o yaml
----
+
*Example output*
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  name: example-vmi
  labels:
    instancetype.kubevirt.io/cluster-instancetype: cx1.example-numa-instance
spec:
  domain:
    cpu:
      dedicatedCPUPlacement: true
      isolateEmulatorThread: true
      sockets: 8
      cores: 1
      threads: 1
      numa:
        guestMappingPassthrough: {}
      guest: 8
      maxSockets: 8
# ...
----
+
The update has applied successfully if in the `spec.template.spec.domain.cpu` section:
+
* The `sockets` value matches the `maxSockets` and `guest` values from the instance type, which ensures that no extra hot plug slots are configured.
* The `dedicatedCPUPlacement` and `isolateEmulatorThread` fields are present and set to `true`.

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-disable-CPU-VM-hotplug_{context}"]
= Adjusting or disabling the CPU hot plug by VM

[role="_abstract"]
As a VM owner, you can adjust or disable the CPU hot plug for individual VMs.
This is the simplest solution for large, performance-critical VMs where you want to ensure a fixed CPU allocation from the start.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Modify the `VirtualMachine` custom resource (CR) for the VM that you want to configure to add a `maxSockets` and `sockets` spec:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: large-numa-vm
spec:
  template:
    spec:
      domain:
        cpu:
          maxSockets: 10
          sockets: 10
          cores: 1
          threads: 1
----
+
By explicitly setting `maxSockets` and `sockets` to a value of 10 or higher, you are specifying that additional capacity is not reserved for hot plugging, which ensures that the entire requested cores are the actual cores allocated.

. Apply the changes to the `VirtualMachine` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

. Check that you have configured the `maxSockets` and `sockets` values correctly, by running the following commands:
+
[source,terminal]
----
$ oc get vmi -o jsonpath='{.spec.domain.cpu.maxSockets}'
----
+
[source,terminal]
----
$ oc get vmi -o jsonpath='{.spec.domain.cpu.sockets}'
----
+
If the configuration was successful, the outputs are the `maxSockets` and `sockets` values that you set in the previous procedure:
+
*Example output*
+
[source,terminal]
----
10
----

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-disable-kubervirt-hotplug-ratio_{context}"]
= Disabling hot plugging for all VMs on a cluster

[role="_abstract"]
If you are a cluster administrator and want to disable hot plugging for an entire cluster, you must modify the `spec.configuration.kubevirtConfiguration.developerConfiguration.maxHotplugRatio` setting in the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.
* You have installed the {CNVOperatorDisplayName}.

.Procedure

. Modify the `HyperConverged` CR and set the `maxHotplugRatio` value to `1.0`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  # ...
  kubevirtConfiguration:
    developerConfiguration:
      maxHotplugRatio: 1.0
# ...
----

. Apply the changes to the `HyperConverged` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

. Check that you have configured the `maxHotplugRatio` value correctly, by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} -n {CNVNamespace} -o jsonpath='{.spec.liveUpdateConfiguration.maxHotplugRatio}'
----
+
If the configuration was successful, the output is the `maxHotplugRatio` value that you set in the previous procedure:
+
*Example output*
+
[source,terminal]
----
1.0
----

// Module included in the following assemblies:
//
// * /virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-NUMA-limitations_{context}"]
= Limitations of NUMA for {VirtProductName}

[role="_abstract"]
When you use NUMA topology with {VirtProductName} VMs, certain limitations can impact performance and VM management.

Asymmetrical topology:: The host scheduler cannot guarantee assigning specific NUMA nodes to a VM. For example, if a VM is rescheduled to a different host machine because of a restart or maintenance, the new host might have a different physical NUMA layout. This means that the VM could be presented with an asymmetrical NUMA topology that reflects the new host's configuration, rather than its original or desired layout. This change can have a negative impact on the VM's performance.

Live migration challenges:: Migrating a NUMA-enabled VM to a different host node can be challenging if the destination node's NUMA topology differs significantly from the source node's. A mismatch between the NUMA layouts of the source and destination can lead to a degradation of the VM's performance after the migration is complete.

No support for PCI NUMA nodes:: There is no explicit support for passing GPU NUMA zone information to the VM. This means that the VM's guest operating system is not aware of the NUMA locality of PCI devices such as GPUs. For workloads that heavily rely on these devices, this lack of awareness could potentially lead to reduced performance if the GPU's memory is not local to the accessing CPU within the NUMA architecture.

// Module included in the following assemblies:
//
// * virt/managing_vms/advanced_vm_management/virt-NUMA-topology.adoc

[id="virt-NUMA-live-migration_{context}"]
= Live migration outcomes using vNUMA

[role="_abstract"]
Migration outcomes for VMs are dependent on the configured Topology Manager policies.
These policies determine how CPU and memory resources are allocated with respect to the physical NUMA nodes of the host.
There are four available policies: `None`, `single-numa-node`, `best-effort`, and `restricted`.

The following table outlines which policies are supported for different VM configurations, and their effect on live migration.

* A small VM is defined as a VM with less total cores than half of cores in NUMA node.
* A large VM is defined as a VM with more total cores than half of cores in NUMA node.
* An extra large VM is defined as a VM with more cores than 1 NUMA node.

[cols="3",options="header"]
|===
|VM size
|Topology Manager policy
|Tested support status

|Any
|single-numa-node
|The VM fails to start because the pod requests more cpus than a single NUMA node on the host can provide. This triggers a topology affinity error during scheduling, which is expected behavior given the node’s hardware limits.

|Any
|None
|Live migration does not work. This is a known issue. The process ends with an incorrect memnode allocation error, and libvirt rejects the XML manifest generated by KubeVirt. See release notes for additional information.
// OCP 4.20 - this may need to be updated later if the issue is resolved in a future release

|Small
|None
|Live migration works, as expected.

|Small
|single-numa-node
|Live migration works, as expected.

|Small
|best-effort
|Live migration works, as expected.

|Small
|restricted
|Live migration works, as expected.

|Large
|single-numa-node
|Live migration works, as expected.

|Large
|best-effort
|Live migration works, as expected.

|Large
|restricted
|Live migration works, as expected.

|Extra large
|None
|Live migration works, as expected.

|Extra large
|best-effort
|Live migration works, as expected.

|Extra large
|restricted
|VMs do not work, as expected.
|===

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Topology Manager policies
* Creating virtual machines from instance types
