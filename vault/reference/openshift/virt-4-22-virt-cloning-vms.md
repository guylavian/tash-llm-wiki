---
title: "Cloning VMs"
type: reference
domain: openshift
slug: virt-4-22-virt-cloning-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-cloning-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Cloning VMs

[id="virt-cloning-vms"]
= Cloning VMs

[role="_abstract"]
You can clone virtual machines (VMs) or create new VMs from snapshots.

[IMPORTANT]
====
Cloning a VM with a vTPM device attached to it or creating a new VM from its snapshot is not supported.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-cloning-vms.adoc

[id="virt-cloning-vm-snapshot_{context}"]
= Cloning a VM by using the web console

[role="_abstract"]
You can clone an existing VM by using the web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. Click *Actions*.
+
Alternatively, access the same menu in the tree view by right-clicking the VM.
. Select *Clone*.
. On the *Clone VirtualMachine* page, enter the name of the new VM.
. Optional: Select the *Start cloned VM* checkbox to start the cloned VM.
. Optional: In the *Volume name policy* section, select how cloned persistent volume claims (PVCs) are named:
** *Randomize names* - The cloned PVC names are randomly generated. This is the default setting.
** *Prefix target name* - The cloned PVC names use the target VM name as a prefix.
. Click *Clone*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-cloning-vms.adoc

[id="virt-creating-vm-from-snapshot-web_{context}"]
= Creating a VM from an existing snapshot by using the web console

[role="_abstract"]
You can create a new VM by copying an existing snapshot.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. Click the *Snapshots* tab.
. Click the Options menu {kebab} for the snapshot you want to copy.
. Select *Create VirtualMachine*.
. Enter the name of the VM.
. Optional: Select the *Start this VM after creation* checkbox to start the new VM.
. Optional: In the *Volume name policy* section, select how cloned persistent volume claims (PVCs) are named:
** *Randomize names* - The cloned PVC names are randomly generated. This is the default setting.
** *Prefix target name* - The cloned PVC names use the target VM name as a prefix.
. Click *Create*.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Creating VMs by cloning PVCs
