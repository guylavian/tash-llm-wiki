---
title: "Enabling dedicated resources for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-dedicated-resources-vm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-dedicated-resources-vm
version: 4.22
family: virt
documentKind: "Documentation"
---

# Enabling dedicated resources for virtual machines

[id="virt-dedicated-resources-vm"]
= Enabling dedicated resources for virtual machines

[role="_abstract"]
To improve performance, you can dedicate node resources, such as CPU, to a virtual machine.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-dedicated-resources-vm.adoc

[id="virt-about-dedicated-resources_{context}"]

= About dedicated resources

[role="_abstract"]
When you enable dedicated resources for your virtual machine, your virtual
machine's workload is scheduled on CPUs that will not be used by other
processes.

By using dedicated resources, you can improve the performance of the
virtual machine and the accuracy of latency predictions.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-dedicated-resources-vm.adoc

// Establishing conditionals so content can be re-used for editing VMs
// and VM templates.

[id="virt-enabling-dedicated-resources_{context}"]
= Enabling dedicated resources for a {object}

[role="_abstract"]
You can enable dedicated resources for a {object} in the *Details* tab. Virtual machines that were created from a Red Hat template can be configured with dedicated resources.

.Prerequisites

* The CPU Manager must be configured on the node. Verify that the node has the `cpumanager = true` label before scheduling virtual machine workloads.

* The virtual machine must be powered off.

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* -> *{object-gui}s* from the side menu.
. Select a {object} to open the *{object-gui} details* page.
. On the *{tab}* tab, click the edit icon beside *Dedicated Resources*.
. Select *Schedule this workload with dedicated resources (guaranteed policy)*.
. Click *Save*.

// Unsetting all conditionals used in module
