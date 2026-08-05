---
title: "Edit the boot order of a virtual machine"
type: reference
domain: openshift
slug: virt-4-22-virt-edit-boot-order
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-edit-boot-order
version: 4.22
family: virt
documentKind: "Documentation"
---

# Edit the boot order of a virtual machine

[id="virt-edit-boot-order"]
= Edit the boot order of a virtual machine

[role="_abstract"]
You can configure the boot order of disks and network devices on your virtual machine (VM) by using the web console or the CLI.

With *Boot Order* in the *VirtualMachine details* page, you can:

* Select a disk or network interface controller (NIC) and add it to the boot order list.
* Edit the order of the disks or NICs in the boot order list.
* Remove a disk or NIC from the boot order list, and return it back to the inventory of bootable sources.

// Module included in the following assembly:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc
//

[id="virt-add-boot-order-web_{context}"]
= Adding items to a boot order list in the web console

[role="_abstract"]
You can add items to a boot order list by using the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Click the *Virtual machines* tab.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. Expand *Boot management*.

. Click the pencil icon that is located on the right side of *Boot Order*. If a YAML configuration does not exist, or if this is the first time that you are creating a boot order list, the following message displays: *No resource selected. VM will attempt to boot from disks by order of appearance in YAML file.*

. Click *Add Source* and select a bootable disk or network interface controller (NIC) for the virtual machine.

. Add any additional disks or NICs to the boot order list.

. Click *Save*.
+
[NOTE]
====
If the virtual machine is running, changes to *Boot Order* will not take effect until you restart the virtual machine.

You can view pending changes by clicking *View Pending Changes* on the right side of the *Boot Order* field. The *Pending Changes* banner at the
top of the page displays a list of all changes that will be applied when the virtual machine restarts.
====
// Module included in the following assemblies:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc

[id="virt-edit-boot-order-web_{context}"]
= Editing a boot order list in the web console

[role="_abstract"]
You can edit the boot order list in the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Click the *Virtual machines* tab.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. Expand *Boot management*.

. Click the pencil icon that is located on the right side of *Boot Order*.

. Choose the appropriate method to move the item in the boot order list:

* If you do not use a screen reader, hover over the arrow icon next to the item that you want to move, drag the item up or down, and drop it in a location of your choice.

* If you use a screen reader, press the Up Arrow key or Down Arrow key to move the item in the boot order list. Then, press the *Tab* key to drop the item in a location of your choice.

. Click *Save*.
+
[NOTE]
====
If the virtual machine is running, changes to the boot order list will not take effect until you restart the virtual machine.

You can view pending changes by clicking *View Pending Changes* on the right side of the *Boot Order* field. The *Pending Changes* banner
at the top of the page displays a list of all changes that will be applied when the virtual machine restarts.
====
// Module included in the following assemblies:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc
//

[id="virt-edit-boot-order-yaml-web_{context}"]
= Editing a boot order list in the YAML configuration file

[role="_abstract"]
You can edit the boot order list in a YAML configuration file by using the CLI.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the YAML configuration file for the virtual machine by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name> -n <namespace>
----

. Edit the YAML file and modify the values for the boot order associated with a disk or network interface controller (NIC). For example:
+
[source,yaml]
----
disks:
  - bootOrder: 1
    disk:
      bus: virtio
    name: containerdisk
  - disk:
      bus: virtio
    name: cloudinitdisk
  - cdrom:
      bus: virtio
    name: cd-drive-1
interfaces:
  - boot Order: 2
    macAddress: '02:96:c4:00:00'
    masquerade: {}
    name: default
----
+
* `disks.bootOrder` defines the boot order value specified for the disk.
* `interfaces.bootOrder` defines the boot order value specified for the network interface controller.

. Save the YAML file.
// Module included in the following assembly:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc
//

[id="virt-remove-boot-order-item-web_{context}"]
= Removing items from a boot order list in the web console

[role="_abstract"]
Remove items from a boot order list by using the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Click the *Virtual machines* tab.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. Expand *Boot management*.

. Click the pencil icon that is located on the right side of *Boot Order*.

. Click the *Remove* icon {delete} next to the item. The item is removed from the boot order list and saved in the list of available boot sources. If you remove all items from the boot order list, the following message displays: *No resource selected. VM will attempt to boot from disks by order of appearance in YAML file.*
+
[NOTE]
====
If the virtual machine is running, changes to *Boot Order* will not take effect until you restart the virtual machine.

You can view pending changes by clicking *View Pending Changes* on the right side of the *Boot Order* field. The *Pending Changes* banner at the top of the page displays a list of all changes that will be applied when the virtual machine restarts.
====
