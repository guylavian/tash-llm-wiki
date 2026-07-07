---
title: "Delete a virtual machine"
type: reference
domain: openshift
slug: virt-4-22-virt-delete-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-delete-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Delete a virtual machine

[id="virt-delete-vms"]
= Delete a virtual machine

[role="_abstract"]
You can remove virtual machines (VMs) from your cluster to free up resources using either the web console or CLI. Deleting a VM removes the virtual machine definition and optionally its associated storage resources.

// Module included in the following assemblies:
//
// * virt/managing-vms/virt-delete-vms.adoc

[id="virt-delete-vm-web_{context}"]

= Deleting a virtual machine using the web console

[role="_abstract"]
Deleting a virtual machine (VM) permanently removes it from the cluster.

If the VM is delete protected, the *Delete* action is disabled in the VM's *Actions* menu.

.Prerequisites

* You have disabled the VM's delete protection setting.
* You have stopped the VM.

.Procedure

. From the OpenShift Container Platform web console, choose your view:

    * For a virtualization-focused view, select *Administrator* → *Virtualization* → *VirtualMachines*.

    * For a general view, navigate to *Virtualization* → *VirtualMachines*.

. Click the *Options* menu {kebab} beside a VM and select *Delete*.
+
Alternatively, click the VM's name to open the *VirtualMachine details* page and click *Actions* -> *Delete*.
+
You can also right-click the VM in the tree view and select *Delete* from the pop-up menu.

. Optional: Select *With grace period* or clear *Delete disks*.

. Click *Delete* to permanently delete the VM.
// Module included in the following assemblies:
//
// * virt/managing-vms/virt-delete-vms.adoc

[id="virt-deleting-vms_{context}"]

= Deleting a virtual machine by using the CLI

[role="_abstract"]
You can delete a virtual machine (VM) by using the `oc` command-line interface (CLI). The `oc` client enables you to perform actions on multiple VMs.

.Prerequisites

* You have disabled the VM's delete protection setting.
* You have stopped the VM.
* You have installed the {oc-first}.

.Procedure

* Delete the VM by running the following command:
+
[source,terminal]
----
$ oc delete vm <vm_name>
----
+
[NOTE]
====
This command only deletes a VM in the current project. Specify the
`-n <project_name>` option if the VM you want to delete is in
a different project or namespace.
====
