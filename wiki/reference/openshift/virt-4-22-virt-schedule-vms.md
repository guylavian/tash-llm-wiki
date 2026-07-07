---
title: "Schedule virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-schedule-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-schedule-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Schedule virtual machines

[id="virt-schedule-vms"]
= Schedule virtual machines

[role="_abstract"]
You can schedule a virtual machine (VM) on a node by ensuring that the VM's CPU model and policy attribute are matched for compatibility with the CPU models and policy attributes supported by the node.

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc

[id="virt-schedule-cpu-host-model-vms_{context}"]
= Scheduling virtual machines with the host model

[role="_abstract"]
When the CPU model for a virtual machine (VM) is set to `host-model`, the VM inherits the CPU model of the node where it is scheduled.

.Procedure

* Edit the `domain` spec of your VM configuration file. The following example shows `host-model` being specified for the virtual machine:
+
[source,yaml]
----
apiVersion: kubevirt/v1alpha3
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          model: host-model
----
** `spec.template.spec.domain.cpu.model` defines the VM that inherits the CPU model of the node where it is scheduled.

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc

[id="virt-schedule-supported-cpu-model-vms_{context}"]
= Scheduling virtual machines with the supported CPU model

[role="_abstract"]
You can configure a CPU model for a virtual machine (VM) to schedule it on a node where its CPU model is supported.

.Procedure

* Edit the `domain` spec of your virtual machine configuration file. The following example shows a specific CPU model defined for a VM:
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
# ...
----
** `spec.template.spec.domain.cpu.model` defines the CPU model for the VM.

// Module included in the following assembly:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc
//

[id="policy-attributes_{context}"]
= Policy attributes

[role="_abstract"]
You can schedule a virtual machine (VM) by specifying a policy attribute and a CPU feature that is matched for compatibility when the VM is scheduled on a node. A policy attribute specified for a VM determines how that VM is scheduled on a node.

[cols="30,70"]
|===
|Policy attribute | Description

|force
|The VM is forced to be scheduled on a node. This is true even if the host CPU does not support the VM's CPU.

|require
|Default policy that applies to a VM if the VM is not configured with a specific CPU model and feature specification. If a node is not configured to support CPU node discovery with this default policy attribute or any one of the other policy attributes, VMs are not scheduled on that node. Either the host CPU must support the VM's CPU or the hypervisor must be able to emulate the supported CPU model.

|optional
|The VM is added to a node if that VM is supported by the host's physical machine CPU.

|disable
|The VM cannot be scheduled with CPU node discovery.

|forbid
|The VM is not scheduled even if the feature is supported by the host CPU and CPU node discovery is enabled.
|===

// Module included in the following assemblies:
//
// * virt/managing_vms/cpu_models/virt-schedule-vms.adoc

[id="virt-setting-policy-attributes_{context}"]
= Setting a policy attribute and CPU feature

[role="_abstract"]
You can set a policy attribute and CPU feature for each virtual machine (VM) to ensure that it is scheduled on a node according to policy and feature. The CPU feature that you set is verified to ensure that it is supported by the host CPU or emulated by the hypervisor.

.Procedure

* Edit the `domain` spec of your VM configuration file. The following example sets the CPU feature and the `require` policy for a virtual machine (VM):
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
          features:
            - name: apic
              policy: require
----
** `spec.template.spec.domain.cpu.features.name` defines the name of the CPU feature for the VM.
** `spec.template.spec.domain.cpu.features.policy` defines the policy attribute for the VM.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-schedule-vms.adoc

[id="virt-vm-custom-scheduler_{context}"]
= Scheduling virtual machines with a custom scheduler

[role="_abstract"]
You can use a custom scheduler to schedule a virtual machine (VM) on a node.

.Prerequisites

* A secondary scheduler is configured for your cluster.
* You have installed the {oc-first}.

.Procedure

* Add the custom scheduler to the VM configuration by editing the `VirtualMachine` manifest. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-fedora
spec:
  runStrategy: Always
  template:
    spec:
      schedulerName: my-scheduler
      domain:
        devices:
          disks:
            - name: containerdisk
              disk:
                bus: virtio
# ...
----
+
`schedulerName`:: The name of the custom scheduler. If the `schedulerName` value does not match an existing scheduler, the `virt-launcher` pod stays in a `Pending` state until the specified scheduler is found.

.Verification

* Verify that the VM is using the custom scheduler specified in the `VirtualMachine` manifest by checking the `virt-launcher` pod events:

.. View the list of pods in your cluster by entering the following command:
+
[source,terminal]
----
$ oc get pods
----
+
Example output:
+
[source,terminal]
----
NAME                             READY   STATUS    RESTARTS   AGE
virt-launcher-vm-fedora-dpc87    2/2     Running   0          24m
----

.. Run the following command to display the pod events:
+
[source,terminal]
----
$ oc describe pod virt-launcher-vm-fedora-dpc87
----
+
The value of the `From` field in the output verifies that the scheduler name matches the custom scheduler specified in the `VirtualMachine` manifest:
+
Example output:
+
[source,terminal]
----
[...]
Events:
  Type    Reason     Age   From              Message
  ----    ------     ----  ----              -------
  Normal  Scheduled  21m   my-scheduler  Successfully assigned default/virt-launcher-vm-fedora-dpc87 to node01
[...]
----

// Hiding in ROSA/OSD, not supported
[role="_additional-resources"]
.Additional resources
* Deploying a secondary scheduler
