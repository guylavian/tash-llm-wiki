---
title: "Install VirtIO drivers on Windows VMs"
type: reference
domain: openshift
slug: virt-4-22-virt-install-virtio-drivers-on-windows-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-install-virtio-drivers-on-windows-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Install VirtIO drivers on Windows VMs

[id="virt-install-virtio-drivers-on-windows-vms"]
= Install VirtIO drivers on Windows VMs

[role="_abstract"]
VirtIO drivers are paravirtualized device drivers required for Microsoft Windows virtual machines (VMs) to run in {VirtProductName}. The drivers are shipped with the rest of the images and do not require a separate download.

The `container-native-virtualization/virtio-win` container disk must be attached to the VM as a SATA CD drive to enable driver installation. You can install VirtIO drivers during Windows installation or add them to an existing Windows installation.

After the drivers are installed, the `container-native-virtualization/virtio-win` container disk can be removed from the VM.

.Supported drivers
[options="header"]
|===
|Driver name |Hardware ID |Description

|*viostor*
|VEN_1AF4&DEV_1001, VEN_1AF4&DEV_1042
|The block driver. Sometimes labeled as an *SCSI Controller* in the *Other devices* group.

|*viorng*
|VEN_1AF4&DEV_1005, VEN_1AF4&DEV_1044
|The entropy source driver. Sometimes labeled as a *PCI Device* in the *Other devices* group.

|*NetKVM*
|VEN_1AF4&DEV_1000, VEN_1AF4&DEV_1041
|The network driver. Sometimes labeled as an *Ethernet Controller* in the *Other devices* group. Available only if a VirtIO NIC is configured.
|===

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms/virt-installing-qemu-guest-agent.adoc

[id="virt-attaching-virtio-disk-to-windows_{context}"]
= Attaching VirtIO container disk to Windows VMs during installation

[role="_abstract"]
You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done during creation of the VM.

.Procedure

. When creating a Windows VM from a template, click *Customize VirtualMachine*.
. Select *Mount Windows drivers disk*.
. Click the *Customize VirtualMachine parameters*.
. Click *Create VirtualMachine*.

.Result

After the VM is created, the `virtio-win` SATA CD disk will be attached to the VM.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms/virt-installing-qemu-guest-agent.adoc

[id="virt-attaching-virtio-disk-to-windows-existing_{context}"]
= Attaching VirtIO container disk to an existing Windows VM

[role="_abstract"]
You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done to an existing VM.

.Procedure

. Navigate to the existing Windows VM, and click *Actions* -> *Stop*.
. Go to *VM Details* -> *Configuration* -> *Storage*.
. Select the *Mount Windows drivers disk* checkbox.
. Click *Save*.
. Start the VM, and connect to a graphical console.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-installing-virtio-drivers-on-new-windows-vm.adoc

//This file contains UI elements and/or package names that need to be updated.

[id="virt-adding-container-disk-as-cd_{context}"]
= Installing VirtIO drivers from a container disk added as a SATA CD drive

[role="_abstract"]
You can install VirtIO drivers from a container disk that you add to a Windows virtual machine (VM) as a SATA CD drive.

[TIP]
====
Downloading the `container-native-virtualization/virtio-win` container disk from the Red Hat Ecosystem Catalog is not mandatory, because the container disk is downloaded from the Red Hat registry if it not already present in the cluster. However, downloading reduces the installation time.
====

.Prerequisites

* You must have access to the Red Hat registry or to the downloaded `container-native-virtualization/virtio-win` container disk in a restricted environment.
* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Add the `container-native-virtualization/virtio-win` container disk as a CD drive by editing the `VirtualMachine` manifest:
+
[source,yaml]
----
# ...
spec:
  domain:
    devices:
      disks:
        - name: virtiocontainerdisk
          bootOrder: 2
          cdrom:
            bus: sata
volumes:
  - containerDisk:
      image: container-native-virtualization/virtio-win
    name: virtiocontainerdisk
----
+
{VirtProductName} boots the VM disks in the order defined in the `VirtualMachine` manifest. You can either define other VM disks that boot before the `container-native-virtualization/virtio-win` container disk, or use the optional `bootOrder` parameter to ensure the VM boots from the correct disk. If you configure the boot order for a disk, you must configure the boot order for the other disks.

. Apply the changes:
* If the VM is not running, run the following command:
+
[source,terminal]
----
$ virtctl start <vm> -n <namespace>
----

* If the VM is running, reboot the VM or run the following command:
+
[source,terminal]
----
$ oc apply -f <vm.yaml>
----

. After the VM has started, install the VirtIO drivers from the SATA CD drive.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

[id="virt-installing-virtio-drivers-installing-windows_{context}"]
= Installing VirtIO drivers during Windows installation

[role="_abstract"]
You can install the VirtIO drivers while installing Windows on a virtual machine (VM).

[NOTE]
====
This procedure uses a generic approach to the Windows installation and the installation method might differ between versions of Windows. See the documentation for the version of Windows that you are installing.
====

.Prerequisites

* A storage device containing the `virtio` drivers must be attached to the VM.

.Procedure

. In the Windows operating system, use the `File Explorer` to navigate to the `virtio-win` CD drive.
. Double-click the drive to run the appropriate installer for your VM.
+
For a 64-bit vCPU, select the `virtio-win-gt-x64` installer. 32-bit vCPUs are no longer supported.

. Optional: During the *Custom Setup* step of the installer, select the device drivers you want to install. The recommended driver set is selected by default.
. After the installation is complete, select *Finish*.
. Reboot the VM.

.Verification

. Open the system disk on the PC. This is typically `C:`.
. Navigate to *Program Files* -> *Virtio-Win*.

If the *Virtio-Win* directory is present and contains a sub-directory for each driver, the installation was successful.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

[id="virt-installing-virtio-drivers-existing-windows_{context}"]
= Installing VirtIO drivers from a SATA CD drive on an existing Windows VM

[role="_abstract"]
You can install the VirtIO drivers from a SATA CD drive on an existing Windows virtual machine (VM).

[NOTE]
====
This procedure uses a generic approach to adding drivers to Windows. See the installation documentation for your version of Windows for specific installation steps.
====

.Prerequisites

* A storage device containing the virtio drivers must be attached to the VM as a SATA CD drive.

.Procedure

. Start the VM and connect to a graphical console.
. Log in to a Windows user session.
. Open *Device Manager* and expand *Other devices* to list any *Unknown device*.
.. Open the *Device Properties* to identify the unknown device.
.. Right-click the device and select *Properties*.
.. Click the *Details* tab and select *Hardware Ids* in the *Property* list.
.. Compare the *Value* for the *Hardware Ids* with the supported VirtIO drivers.

. Right-click the device and select *Update Driver Software*.
. Click *Browse my computer for driver software* and browse to the attached
SATA CD drive, where the VirtIO drivers are located. The drivers are arranged
hierarchically according to their driver type, operating system,
and CPU architecture.
. Click *Next* to install the driver.
. Repeat this process for all the necessary VirtIO drivers.
. After the driver installs, click *Close* to close the window.
. Reboot the VM to complete the driver installation.
