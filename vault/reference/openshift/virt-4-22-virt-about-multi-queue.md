---
title: "About multi-queue functionality"
type: reference
domain: openshift
slug: virt-4-22-virt-about-multi-queue
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-about-multi-queue
version: 4.22
family: virt
documentKind: "Documentation"
---

# About multi-queue functionality

[id="virt-about-multi-queue"]
= About multi-queue functionality

[role="_abstract"]
Use multi-queue functionality to scale network throughput and performance on virtual machines (VMs) with multiple vCPUs.

By default, the `queueCount` value, which is derived from the domain XML, is determined by the number of vCPUs allocated to a VM. Network performance does not scale as the number of vCPUs increases. Additionally, because `virtio-net` has only one transmit and receive queue, guests cannot send or receive packs in parallel.

[NOTE]
====
Enabling `virtio-net` multi-queue does not offer significant improvements when the number of vNICs in a guest instance is proportional to the number of vCPUs.
====

[id="known-limitations_{context}"]
== Known limitations

* Message signaled interrupt (MSI) vectors are still consumed if `virtio-net` multi-queue is enabled in the host but not enabled in the guest operating system by the administrator.
* Each `virtio-net` queue consumes 64 KiB of kernel memory for the `vhost` driver.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-configuring-shared-volumes-for-vms.adoc

[id="virt-enabling-multi-queue_{context}"]
= Enabling multi-queue functionality

[role="_abstract"]
You can enable multi-queue functionality for interfaces configured with a VirtIO model.

.Procedure

. Set the `networkInterfaceMultiqueue` value to `true` in the `VirtualMachine` manifest file of your VM to enable multi-queue functionality:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VM
spec:
  domain:
    devices:
      networkInterfaceMultiqueue: true
----

. Save the `VirtualMachine` manifest file to apply your changes.
