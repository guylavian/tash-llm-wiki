---
title: "Creating a license-compliant AWS EC2 Windows VM"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-aws-li-windows
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-aws-li-windows
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating a license-compliant AWS EC2 Windows VM

[id="virt-creating-vms-aws-li-windows"]
= Creating a license-compliant AWS EC2 Windows VM

[role="_abstract"]
If you are running Windows virtual machines (VMs) on OpenShift Container Platform hosts, such as AMD64 bare metal EC2 instances with {aws-first} Windows License Included (LI) enabled, you must ensure that any VMs you create are compliant with licensing requirements.

When you configure your Windows VMs correctly, they activate automatically with the {aws-short} Key Management Service (KMS), and run using optimized drivers for the underlying bare-metal hardware. Proper configuration also ensures that billing is correct.

If you do not configure your Windows VMs so that they are license-compliant, they might fail to activate, suffer degraded system performance due to sub-optimal CPU pinning, and risk failing a licensing audit.

// Module included in the following assemblies:
//
// * virt/creating_vm/virt-creating-vms-aws-li-windows.adoc

[id="virt-create-aws-li-windows-vm-web-console_{context}"]
= Creating a license-compliant AWS EC2 Windows VM by using the web console

[role="_abstract"]
You can create license-compliant Windows virtual machines (VMs) by enabling the `dedicatedCpuPlacement` attribute. This attribute is enabled by default on *Dedicated vCPU* instance types. In the OpenShift Container Platform web console, you can create a compliant VM by selecting from a list of available bootable volumes.

.Procedure

. In the OpenShift Container Platform web console, go to *Virtualization* -> *Catalog*. The *InstanceTypes* tab opens by default.

. Click *Add volume* to create a Windows boot source. You can create a Windows boot source by uploading a new volume or by using an existing persistent volume claim (PVC), a volume snapshot, or a `containerDisk` volume.

. In the *Volume metadata* section, select a preference with a name that begins with `windows` and is followed by the Windows version of your choice. For example, `windows.11.virtio`. Click *Save*.

. Select a bootable volume from the list. If the list is truncated, click *Show all* to display the entire list. The bootable volume table contains the previously uploaded boot source.

. In the *User provided* tab, select a *Dedicated vCPU* instance type.

. Optional: You can mount a Windows driver disk by completing the following steps:
.. Click *Customize VirtualMachine*.
.. On the *VirtualMachine details* page, click *Storage*.
.. Select the *Mount Windows drivers* disk checkbox.

. Click *Create VirtualMachine*.
