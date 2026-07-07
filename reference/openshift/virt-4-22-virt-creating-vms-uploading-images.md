---
title: "Creating VMs by uploading images"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-uploading-images
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-uploading-images
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating VMs by uploading images

[id="virt-creating-vms-uploading-images"]
= Creating VMs by uploading images

[role="_abstract"]
You can create virtual machines (VMs) by uploading operating system images from your local machine.

You can create a Windows VM by uploading a Windows image to a PVC. Then you clone the PVC when you create the VM.

[IMPORTANT]
====
You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red Hat.

You must also install VirtIO drivers on Windows VMs.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-creating-vm-uploaded-image-web_{context}"]
= Creating a VM from an uploaded image by using the web console

[role="_abstract"]
You can create a virtual machine (VM) from an uploaded operating system image by using the OpenShift Container Platform web console.

.Prerequisites

* You must have an `IMG`, `ISO`, or `QCOW2` image file.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click a template tile without an available boot source.
. Click *Customize VirtualMachine*.
. On the *Customize template parameters* page, expand *Storage* and select *Upload (Upload a new file to a PVC)* from the *Disk source* list.
. Browse to the image on your local machine and set the disk size.
. Click *Customize VirtualMachine*.
. Click *Create VirtualMachine*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-generalizing-linux-vm-image_{context}"]
= Generalizing a VM image

[role="_abstract"]
You can generalize a {op-system-base-full} image to remove all system-specific configuration data before you use the image to create a golden image, a preconfigured snapshot of a virtual machine (VM). You can use a golden image to deploy new VMs.

You can generalize a {op-system-base} VM by using the `virtctl`, `guestfs`, and `virt-sysprep` tools.

.Prerequisites

* You have a {op-system-base} virtual machine (VM) to use as a base VM.
* You have installed the OpenShift CLI (`oc`).
* You have installed the `virtctl` tool.

.Procedure

. Stop the {op-system-base} VM if it is running, by entering the following command:
+
[source,terminal]
----
$ virtctl stop <my_vm_name>
----

. Optional: Clone the virtual machine to avoid losing the data from your original VM. You can then generalize the cloned VM.

. Retrieve the `dataVolume` that stores the root filesystem for the VM by running the following command:
+
[source,terminal]
----
$ oc get vm <my_vm_name> -o jsonpath="{.spec.template.spec.volumes}{'\n'}"
----
+
Example output:
+
[source,terminal]
----
[{"dataVolume":{"name":"<my_vm_volume>"},"name":"rootdisk"},{"cloudInitNoCloud":{...}]
----

. Retrieve the persistent volume claim (PVC) that matches the listed `dataVolume` by running the followimg command:
+
[source,terminal]
----
$ oc get pvc
----
+
Example output:
+
[source,terminal]
----
NAME            STATUS   VOLUME  CAPACITY   ACCESS MODES  STORAGECLASS     AGE
<my_vm_volume> Bound  …
----
+
[NOTE]
====
If your cluster configuration does not enable you to clone a VM, to avoid losing the data from your original VM, you can clone the VM PVC to a data volume instead. You can then use the cloned PVC to create a golden image.

If you are creating a golden image by cloning a PVC, continue with the next steps, using the cloned PVC.
====

. Deploy a new interactive container with `libguestfs-tools` and attach the PVC to it by running the following command:
+
[source,terminal]
----
$ virtctl guestfs <my-vm-volume> --uid 107
----
+
This command opens a shell for you to run the next command.

. Remove all configurations specific to your system by running the following command:
+
[source,terminal]
----
$ virt-sysprep -a disk.img
----

. In the OpenShift Container Platform console, click *Virtualization* -> *Catalog*.

. Click *Add volume*.

. In the *Add volume* window:

.. From the *Source type* list, select *Use existing Volume*.

.. From the *Volume project* list, select your project.

.. From the *Volume name* list, select the correct PVC.

.. In the *Volume name* field, enter a name for the new golden image.

.. From the *Preference* list, select the {op-system-base} version you are using.

.. From the *Default Instance Type* list, select the instance type with the correct CPU and memory requirements for the version of {op-system-base} you selected previously.

.. Heterogeneous clusters only: From the *Architecture* list, select the architecture that corresponds with the selected volume.

.. Click *Save*.

.Result

The new volume appears in the *Select volume to boot from* list. This is your new golden image. You can use this volume to create new VMs.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-creating-windows-vm_{context}"]
= Creating a Windows VM

[role="_abstract"]
You can create a Windows virtual machine (VM) by uploading a Windows image to a persistent volume claim (PVC) and then cloning the PVC when you create a VM by using the OpenShift Container Platform web console.

.Prerequisites

* You created a Windows installation DVD or USB with the Windows Media Creation Tool. See Create Windows 10 installation media in the Microsoft documentation.
* You created an `autounattend.xml` answer file. See Answer files (unattend.xml) in the Microsoft documentation.

.Procedure

. Upload the Windows image as a new PVC:

.. Navigate to *Storage* -> *PersistentVolumeClaims* in the web console.
.. Click *Create PersistentVolumeClaim* -> *With Data upload form*.
.. Browse to the Windows image and select it.
.. Enter the PVC name, select the storage class and size and then click *Upload*.
+
The Windows image is uploaded to a PVC.

. Configure a new VM by cloning the uploaded PVC:

.. Navigate to *Virtualization* -> *Catalog*.
.. Select a Windows template tile and click *Customize VirtualMachine*.
.. Select *Clone (clone PVC)* from the *Disk source* list.
.. Select the PVC project, the Windows image PVC, and the disk size.

. Apply the answer file to the VM:

.. Click *Customize VirtualMachine parameters*.
.. On the *Sysprep* section of the *Scripts* tab, click *Edit*.
.. Browse to the `autounattend.xml` answer file and click *Save*.

. Set the run strategy of the VM:

.. Clear *Start this VirtualMachine after creation* so that the VM does not start immediately.
.. Click *Create VirtualMachine*.
.. On the *YAML* tab, replace `running:false` with `runStrategy: RerunOnFailure` and click *Save*.

. Click the Options menu {kebab} and select *Control* -> *Start*.
+
The VM boots from the `sysprep` disk containing the `autounattend.xml` answer file.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-generalizing-windows-sysprep_{context}"]
= Generalizing a Windows VM image

[role="_abstract"]
You can generalize a Windows operating system image to remove all system-specific configuration data before you use the image to create a new virtual machine (VM).

Before generalizing the VM, you must ensure the `sysprep` tool cannot detect an answer file after the unattended Windows installation.

.Prerequisites

* A running Windows VM with the QEMU guest agent installed.

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* -> *VirtualMachines*.
. Select a Windows VM to open the *VirtualMachine details* page.
. Click *Configuration* -> *Disks*.
. Click the Options menu {kebab} beside the `sysprep` disk and select *Detach*.
. Click *Detach*.
. Rename `C:\Windows\Panther\unattend.xml` to avoid detection by the `sysprep` tool.

. Start the `sysprep` program by running the following command:
+
[source,terminal]
----
%WINDIR%\System32\Sysprep\sysprep.exe /generalize /shutdown /oobe /mode:vm
----
. After the `sysprep` tool completes, the Windows VM shuts down. The disk image of the VM is now available to use as an installation image for Windows VMs.

.Result

You can now specialize the VM.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-specializing-windows-sysprep_{context}"]
= Specializing a Windows VM image

[role="_abstract"]
Specializing a Windows virtual machine (VM) configures the computer-specific information from a generalized Windows image onto the VM.

.Prerequisites

* You must have a generalized Windows disk image.
* You must create an `unattend.xml` answer file. See the Microsoft documentation for details.

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* -> *Catalog*.
. Select a Windows template and click *Customize VirtualMachine*.
. Select *PVC (clone PVC)* from the *Disk source* list.
. Select the PVC project and PVC name of the generalized Windows image.
. Click *Customize VirtualMachine parameters*.
. Click the *Scripts* tab.
. In the *Sysprep* section, click *Edit*, browse to the `unattend.xml` answer file, and click *Save*.
. Click *Create VirtualMachine*.

.Result

During the initial boot, Windows uses the `unattend.xml` answer file to specialize the VM. The VM is now ready to use.

// uploading image with cli
// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

[id="virt-uploading-image-virtctl_{context}"]
= Creating a VM from an uploaded image by using the CLI

[role="_abstract"]
You can upload an operating system image by using the `virtctl` command-line tool. You can use an existing data volume or create a new data volume for the image.

.Prerequisites

* You must have an `ISO`, `IMG`, or `QCOW2` operating system image file.
* For best performance, compress the image file by using the virt-sparsify tool or the `xz` or `gzip` utilities.
* The client machine must be configured to trust the OpenShift Container Platform router's
certificate.
* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Upload the image by running the `virtctl image-upload` command:
+
[source,terminal]
----
$ virtctl image-upload dv <datavolume_name> \
  --size=<datavolume_size> \
  --image-path=</path/to/image>
----
+
`<datavolume_name>`:: The name of the data volume.
`<datavolume_size>`:: The size of the data volume. For example: `--size=500Mi`, `--size=1G`
`</path/to/image>`:: The file path of the image.
+
[NOTE]
====
* If you do not want to create a new data volume, omit the `--size` parameter and include the `--no-create` flag.
* When uploading a disk image to a PVC, the PVC size must be larger than the size of the uncompressed virtual disk.
* To allow insecure server connections when using HTTPS, use the `--insecure` parameter. When you use the `--insecure` flag, the authenticity of the upload endpoint is *not* verified.
====

. Optional. To verify that a data volume was created, view all data volumes by running the following command:
+
[source,terminal]
----
$ oc get dvs
----

// To do: Editing VM spec to include DV from uploaded image

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Installing the QEMU guest agent
* Installing VirtIO drivers on Windows VMs
* Cloning VMs
* Cloning a PVC to a data volume
* Sysprep (Generalize) a Windows installation
* Configuration pass of Windows Setup (generalize)
* Configuration pass of Windows Setup (specialize)
