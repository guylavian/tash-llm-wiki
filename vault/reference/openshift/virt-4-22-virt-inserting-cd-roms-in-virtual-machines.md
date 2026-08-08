---
title: "Insert a CD-ROM ISO image into a live virtual machine"
type: reference
domain: openshift
slug: virt-4-22-virt-inserting-cd-roms-in-virtual-machines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-inserting-cd-roms-in-virtual-machines
version: 4.22
family: virt
documentKind: "Documentation"
---

# Insert a CD-ROM ISO image into a live virtual machine

[id="virt-inserting-cd-roms-in-virtual-machines"]
= Insert a CD-ROM ISO image into a live virtual machine

[role="_abstract"]
To attach a storage device to a virtual machine (VM) without rebooting the VM, you can configure a VM to use a virtual CD-ROM drive, and insert an ISO image in the drive.

This also makes it possible to install an operating system from a CD-ROM in the VM.

// Module included in the following assemblies:
//
// * virt/managing_vms/virtual_disks/virt-inserting-cd-roms-in-virtual-machines.adoc

[id="virt-inserting-a-cd-rom-in-a-vm-by-using-the-command-line_{context}"]
= Inserting a CD-ROM in a live VM by using the command line

[role="_abstract"]
To make data on a CD-ROM storage device available to a running virtual machine (VM), create a virtual CD-ROM drive in the VM and insert the CD-ROM into the drive as an ISO image.

Setting up a virtual CD-ROM drive requires rebooting the VM, but afterwards, you can insert and eject ISO images in the drive while the VM is running.
// See https://kubevirt.io/user-guide/storage/hotplug_volumes/#inject-cd-rom for upstream info

.Prerequisites

* You have an ISO image of a CD-ROM available in the cluster.

.Procedure

. Run the following command to edit the configuration of the VM in which you want to insert the CD-ROM:
+
[source,terminal]
----
$ oc edit vm <vm-name> -n <namespace>
----
+
where:

* `<vm-name>` is the name of the VM
* `<namespace>` is the name of the project name space that contains the VM

. Add a `cdrom` disk to the `spec.template.spec.domains.devices.disks` section of the VM configuration. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  runStrategy: Always
  template:
    spec:
      domain:
        devices:
          disks:
          - cdrom:
              bus: sata
              name: cdrom
----

. If the VM is running, shut it down.

. Insert a CD-ROM volume in the `spec.template.spec.volumes` section of the VM configuration. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      volumes:
      - dataVolume:
          name: cdrom-example
          hotpluggable: true
        name: cdrom
----
+
You can insert a CD-ROM this way while the VM is running, but the dataVolume must have the `hotpluggable: true` parameter set.

. Optional: In the guest operating system, verify that the CD-ROM has been detected.

. Optional: Eject the CD-ROM volume. To do so, remove the `cdrom` volume from the `spec.template.spec.volumes` section of the VM configuration. You can do this while the VM is running.

// Module included in the following assemblies:
//
// * virt/managing_vms/virtual_disks/virt-inserting-cd-roms-in-virtual-machines.adoc

[id="virt-inserting-a-cd-rom-in-a-vm-by-using-the-web-console_{context}"]
= Inserting a CD-ROM in a live VM by using the web console

[role="_abstract"]
To make data on a CD-ROM storage device available to a running virtual machine (VM), create a virtual CD-ROM drive in the VM and insert the CD-ROM into the drive as an ISO image.

Setting up a virtual CD-ROM drive requires rebooting the VM, but you can insert and eject ISO images in the drive while the VM is running.

.Prerequisites

.Procedure

. In the OpenShift Container Platform web console, go to *Virtualization* → *VirtualMachines*.

. Click the name of the VM in which you want to insert the CD-ROM.

. On the VM details page, click the *Configuration* tab.

. Open the *Storage* pane.

. Click *Add*.
+
A drop-down menu opens.

. Click *CD-ROM*.

. In the *Name* field, add a name for the CD-ROM drive device.

. Select the ISO image to add to the drive as a CD-ROM volume. To do so, click the drop-down button, and select from the volumes available in the cluster.
+
Alternatively, you can upload a new ISO file and insert it into the CD-ROM drive after it is created. To do so:

.. Ensure that the *Upload a new ISO file to the cluster* line is checked.
.. Drag and drop an ISO file in the *Upload ISO* field, or click *Upload* and select the ISO image that you want to upload.
.. In the *Upload mode* field, select *Mount uploaded ISO as DataVolume*.

. Click *Add*.
+
The CD-ROM drive is added to the *Storage* list.

. If the VM is running, shut it down or restart it.

. To insert the ISO file attached to the CD-ROM drive as a CD-ROM volume into the VM, click the Options menu {kebab} next to the CD-ROM drive, and click *Inject*. You can do this while the VM is running.

. Optional: In the guest operating system, verify that the CD-ROM has been detected.

. Optional: To eject the CD-ROM from the VM, click the Options menu {kebab} next to the CD-ROM device in the web console, and select *Eject*. You can do this while the VM is running.
