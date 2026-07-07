---
title: "Using UEFI mode for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-uefi-mode-for-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-uefi-mode-for-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using UEFI mode for virtual machines

[id="virt-uefi-mode-for-vms"]
= Using UEFI mode for virtual machines

[role="_abstract"]
You can boot a virtual machine (VM) in Unified Extensible Firmware Interface (UEFI) mode for faster boot times, the ability to boot to larger disks, and added security features.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

[id="virt-about-uefi-mode-for-vms_{context}"]
= About UEFI mode for virtual machines

[role="_abstract"]
Unified Extensible Firmware Interface (UEFI), like legacy BIOS, initializes hardware components and operating system image files when a computer starts. UEFI supports more modern features and customization options than BIOS, enabling faster boot times.

It stores all the information about initialization and startup in a file with a `.efi` extension, which is stored on a special partition called EFI System Partition (ESP). The ESP also contains the boot loader programs for the operating system that is installed on the computer.
// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

[id="virt-booting-vms-uefi-mode_{context}"]
= Booting virtual machines in UEFI mode

[role="_abstract"]
You can configure a virtual machine to boot in UEFI mode by editing the `VirtualMachine` manifest.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. To boot a virtual machine (VM) in UEFI mode with secure boot active, edit or create a `VirtualMachine` manifest file. Use the `spec.firmware.bootloader` stanza to configure UEFI mode:
+
[source,yaml]
----
apiversion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    special: vm-secureboot
  name: vm-secureboot
spec:
  template:
    metadata:
      labels:
        special: vm-secureboot
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: containerdisk
        features:
          acpi: {}
          smm:
            enabled: true
        firmware:
          bootloader:
            efi:
              secureBoot: true
# ...
----
+
* You must set `spec.template.spec.domain.features.ssm.enabled` to have a value of `true`.
* If `spec.template.spec.domain.firmware.bootloader.efi.secureBoot` is set to `true`, then UEFI mode is required. However, you can enable UEFI mode without using Secure Boot.

. Apply the manifest to your cluster by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

[id="virt-enabling-persistent-efi_{context}"]
= Enabling persistent EFI

[role="_abstract"]
You can enable EFI persistence in a VM by configuring a suitable storage class at the cluster level and adjusting the settings in the EFI section of the VM.
You can enable EFI persistence in a VM by configuring an RWX storage class at the cluster level and adjusting the settings in the EFI section of the VM.

.Prerequisites

* You must have cluster administrator privileges.
* You must have a storage class that supports filesystem (`FS`) volume mode and the access mode required for persistent EFI state.
* You must have a storage class that supports RWX access mode and FS volume mode.
* You have installed the {oc-first}.

.Procedure

* Enable the `VMPersistentState` feature gate by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op":"replace","path":"/spec/featureGates/VMPersistentState", "value": true}]'
----
// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-uefi-mode-for-vms.adoc

[id="configuring-vm-with-persistent-efi_{context}"]
= Configuring VMs with persistent EFI

[role="_abstract"]
You can configure a VM to have EFI persistence enabled by editing its manifest file.

.Prerequisites

* `VMPersistentState` feature gate enabled.

.Procedure

* Edit the VM manifest file and save to apply settings.
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm
spec:
  template:
    spec:
      domain:
        firmware:
          bootloader:
            efi:
              persistent: true
# ...
----
