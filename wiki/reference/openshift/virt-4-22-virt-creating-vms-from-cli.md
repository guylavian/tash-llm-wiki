---
title: "Creating virtual machines by using the CLI"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-from-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-from-cli
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating virtual machines by using the CLI

[id="virt-creating-vms-from-cli"]
= Creating virtual machines by using the CLI

[role="_abstract"]
You can create virtual machines (VMs) from the command line by editing or creating a `VirtualMachine` manifest. You can simplify VM configuration by using an instance type in your VM manifest.

[NOTE]
====
You can also create VMs from instance types by using the OpenShift Container Platform web console.
====

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_cli/virt-creating-vms-from-cli.adoc

[id="virt-creating-vm-cli_{context}"]
= Creating a VM from a VirtualMachine manifest

[role="_abstract"]
You can create a virtual machine (VM) from a `VirtualMachine` manifest. To simplify the creation of these manifests, you can use the `virtctl` command-line tool.

.Prerequisites

* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal {op-system-base-full} VM, run the following command:
+
[source,terminal]
----
$ virtctl create vm --name rhel-9-minimal --volume-import type:ds,src:openshift-virtualization-os-images/rhel9
----

. Review the `VirtualMachine` manifest for your VM:
+
[NOTE]
====
This example manifest does not configure VM authentication.
====
+
.Example manifest for a {op-system-base} VM
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: rhel-9-minimal
spec:
  dataVolumeTemplates:
  - metadata:
      name: imported-volume-mk4lj
    spec:
      sourceRef:
        kind: DataSource
        name: rhel9
        namespace: openshift-virtualization-os-images
      storage:
        resources: {}
  instancetype:
    inferFromVolume: imported-volume-mk4lj
    inferFromVolumeFailurePolicy: Ignore
  preference:
    inferFromVolume: imported-volume-mk4lj
    inferFromVolumeFailurePolicy: Ignore
  runStrategy: Always
  template:
    spec:
      domain:
        devices:
          video:
            type: virtio
        memory:
          guest: 512Mi
        resources: {}
      terminationGracePeriodSeconds: 180
      volumes:
      - dataVolume:
          name: imported-volume-mk4lj
        name: imported-volume-mk4lj
----
+

* `name: rhel-9-minimal` specifies the name of the VM.
* `name: rhel9` specifies the boot source for the guest operating system in the `sourceRef` section.
* `namespace: openshift-virtualization-os-images` specifies the namespace for the boot source. Golden images are stored in the `openshift-virtualization-os-images` namespace.
* `instancetype: inferFromVolume: imported-volume-mk4lj` specifies the instance type inferred from the selected `DataSource` object.
* `preference: inferFromVolume: imported-volume-mk4lj` specifies that the preference is inferred from the selected `DataSource` object.
* `type: virtio` specifies the use of a custom video device (a VirtIO device in this example) to enable hardware graphics acceleration. Enabling a custom video device is in Technology Preview for {VirtProductName} 4.21.

. Create a virtual machine by using the manifest file:
+
[source,terminal]
----
$ oc create -f <vm_manifest_file>.yaml
----

. Optional: Start the virtual machine:
+
[source,terminal]
----
$ virtctl start <vm_name>
----

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_cli/virt-creating-vms-from-cli.adoc

[id="virt-supported-custom-video-devices_{context}"]
= Supported custom video device types

[role="_abstract"]
When creating a virtual machine (VM), you can configure a custom video device type to override the default video configuration.

Configuring a custom video device allows you to specify different video devices, based on your guest operating system requirements and performance needs.

[IMPORTANT]
====
Custom video device support is a Technology Preview feature only. Technology Preview features are not supported with Red{nbsp}Hat production service level agreements (SLAs) and might not be functionally complete. Red{nbsp}Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red{nbsp}Hat Technology Preview features, see Technology Preview Features Support Scope.
====

Using a custom video device  provides several advantages:

Performance:: Certain video devices provide better performance than the default configuration. For example, VirtIO is a more efficient video device on AMD/x86_64 architecture than legacy VGA.
Resolution flexibility:: With some video device types, you can set custom display resolutions.
Memory efficiency:: Some video types are more memory efficient for headless or console-only operations.

You can configure the following video device types:

* VirtIO: provides improved performance, and hardware-accelerated video decoding and encoding by offloading tasks to the host. Recommended for modern guest operating systems with available `VirtIO` drivers.
* VGA: the standard for analog video display (default on AMD/x86_64 with BIOS).
* Bochs: an emulated graphics adapter that provides a simple interface for guest operating systems to manage display settings (default on AMD/x86_64 with EFI).
* Cirrus: a legacy video device that provides stable video output.
* ramfb:  a simple, unaccelerated virtual display device primarily used in the QEMU emulator, and useful for ARM architecture.

[cols="1,1,1,1",options="header"]
.Video device support by architecture
|====
|Architecture |Boot mode |Default type |Supported types
| AMD/x86_64  | BIOS     | `vga`       | `virtio`, `vga`, `bochs`, `cirrus`, `ramfb``
| AMD/x86_64  | EFI      | `bochs`     | `virtio`, `vga`, `bochs`, `cirrus`, `ramfb``
| ARM64       | BIOS/EFI | `virtio`    | `virtio`, `ramfb`
| s390x       | BIOS/EFI | `virtio`    | `virtio`
|====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* SSH access for virtual machines
* Creating virtual machines from instance types
