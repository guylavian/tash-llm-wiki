---
title: "Edit the configuration of a virtual machine"
type: reference
domain: openshift
slug: virt-4-22-virt-edit-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-edit-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Edit the configuration of a virtual machine

[id="virt-edit-vms"]
= Edit the configuration of a virtual machine

[role="_abstract"]
You can update virtual machine (VM) configuration details like CPU, memory, and networking by using the CLI or the OpenShift Container Platform web console. In the web console, you can modify settings on the *VirtualMachine details* page or by editing the YAML file directly.

To edit a VM to configure disk sharing by using virtual disks or LUN, see "Configuring shared volumes for virtual machines".

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-edit-vms.adoc

[id="virt-change-vm-instance-type_{context}"]
= Changing the instance type of a VM by using the web console

[role="_abstract"]
You can change the instance type associated with a running virtual machine (VM) by using the web console. The change takes effect immediately.

.Prerequisites

* You created the VM by using an instance type.

.Procedure

. In the OpenShift Container Platform web console, click *Virtualization* -> *VirtualMachines*.

. Select a VM to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. On the *Details* tab, click the instance type text to open the *Edit Instancetype* dialog. For example, click *1 CPU | 2 GiB Memory*.

. Edit the instance type by using the *Series* and *Size* lists.
.. Select an item from the *Series* list to show the relevant sizes for that series. For example, select *General Purpose*.
.. Select the new instance type for the VM from the *Size* list. For example, select *medium: 1 CPUs, 4Gi Memory*, which is available in the *General Purpose* series.

. Click *Save*.

.Verification

. Click the *YAML* tab.

. Click *Reload*.

. Review the VM YAML to confirm that the instance type changed.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-hot-plugging-memory_{context}"]

= Hot plugging memory on a virtual machine

[role="_abstract"]
You can add or remove the amount of memory allocated to a virtual machine (VM) without having to restart the VM by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Select the required VM to open the *VirtualMachine details* page.
. On the *Configuration* tab, click *Edit CPU|Memory*.
. Enter the required amount of memory and click *Save*.
+
[NOTE]
====
By hot plugging, you can increase the total amount of memory of a VM up to four times the default initial amount. Exceeding this limit requires a restart.
====
+
The system applies these changes immediately. If the VM is able to be migrated, a live migration is triggered. If not, or if the changes cannot be live-updated, a `RestartRequired` condition is added to the VM.
+
[NOTE]
====
Memory hot plugging for virtual machines requires guest operating system support for the `virtio-mem` driver. This support depends on the driver being included and enabled within the guest operating system, not on specific upstream kernel versions.

Supported guest operating systems:

* RHEL 9.4 and later
* RHEL 8.10 and later (hot-unplug is disabled by default)
* Other Linux guests require kernel version 5.16 or later and the `virtio-mem` kernel module
* Windows guests require `virtio-mem` driver version 100.95.104.26200 or later
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-hot-plugging-cpu_{context}"]

= Hot plugging CPUs on a virtual machine

[role="_abstract"]
You can increase or decrease the number of CPU sockets allocated to a virtual machine (VM) without having to restart the VM by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Select the required VM to open the *VirtualMachine details* page.
. On the *Configuration* tab, click *Edit CPU|Memory*.
. Select the *vCPU* radio button.
. Enter the required number of vCPU sockets and click *Save*.
+
[NOTE]
====
By hot plugging, you can increase the total number of vCPU sockets of a VM up to four times the default initial number. Exceeding this limit requires a restart.
====
+
If the VM is migratable, a live migration is triggered. If not, or if the changes cannot be live-updated, a `RestartRequired` condition is added to the VM.
+
[NOTE]
====
If a VM has the `spec.template.spec.domain.devices.networkInterfaceMultiQueue` field enabled and CPUs are hot plugged, the following behavior occurs:

* Existing network interfaces that you attach before the CPU hot plug retain their original queue count, even after you add more virtual CPUs (vCPUs). The underlying virtualization technology causes this expected behavior.
* To update the queue count of existing interfaces to match the new vCPU configuration, you can restart the VM. A restart is only necessary if the update improves performance.
* New VirtIO network interfaces that you hot plugged after the CPU hot plug automatically receive a queue count that matches the updated vCPU configuration.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-editing-vm-cli_{context}"]
= Editing a virtual machine by using the CLI

[role="_abstract"]
You can edit a virtual machine (VM) by using the command line.

.Prerequisites

* You installed the `oc` CLI.

.Procedure

. Obtain the virtual machine configuration by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name>
----

. Edit the YAML configuration.
. If you edit a running virtual machine, you need to do one of the following:
* Restart the virtual machine.
* Run the following command for the new configuration to take effect:
+
[source,terminal]
----
$ oc apply vm <vm_name> -n <namespace>
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-add-disk-to-vm_{context}"]

= Adding a disk to a virtual machine

[role="_abstract"]
You can add a virtual disk to a virtual machine (VM) by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.

. On the *Disks* tab, click *Add disk*.

. Specify the *Source*, *Name*, *Size*, *Type*, *Interface*, and *Storage Class*.

.. Optional: You can enable preallocation if you use a blank disk source and require maximum write performance when creating data volumes. To do so, select the *Enable preallocation* checkbox.

.. Optional: You can clear *Apply optimized StorageProfile settings* to change the *Volume Mode* and *Access Mode* for the virtual disk. If you do not specify these parameters, the system uses the default values from the `kubevirt-storage-class-defaults` config map.

. Click *Add*.
+
[NOTE]
====
If the VM is running, you must restart the VM to apply the change.
====

// Module included in the following assemblies:
//
// * virt/creating_vm/virt-creating-vms-from-templates.adoc
// * virt/managing_vms/virt-edit-vms.adoc

[id="virt-storage-wizard-fields-web_{context}"]
= Storage fields

[role="_abstract"]
To optimize storage performance and ensure data availability for your workloads, configure the storage fields to define the source, size, and disk characteristics of your virtual machine (VM).

[cols="1a,3a"]
|===
|Field |Description

|Blank (creates PVC)
|Create an empty disk.

|Import via URL (creates PVC)
|Import content via URL (HTTP or HTTPS endpoint).

|Use an existing PVC
|Use a PVC that is already available in the cluster.

|Clone existing PVC (creates PVC)
|Select an existing PVC available in the cluster and clone it.

|Import via Registry (creates PVC)
|Import content via container registry.

|Container (ephemeral)
|Upload content from a container located in a registry accessible from the cluster. The container disk should be used only for read-only filesystems such as CD-ROMs or temporary virtual machines.

|Name
|Name of the disk. The name can contain lowercase letters (`a-z`), numbers (`0-9`), hyphens (`-`), and periods (`.`), up to a maximum of 253 characters. The first and last characters must be alphanumeric. The name must not contain uppercase letters, spaces, or special characters.

|Size
|Size of the disk in GiB.

|Type
|Type of disk. Example: Disk or CD-ROM

|Interface
|Type of disk device. Supported interfaces are *virtIO*, *SATA*, and *SCSI*.

|Storage Class
|The storage class that is used to create the disk.
|===

[id="virt-storage-wizard-fields-advanced-web_{context}"]
== Advanced storage settings

The following advanced storage settings are optional and available for *Blank*, *Import via URL*, and *Clone existing PVC* disks.

If you do not specify these parameters, the system uses the default storage profile values.

[cols="1a,1a,3a",options="header"]
|===
|Parameter |Option |Parameter description

.2+|Volume Mode

|Filesystem
|Stores the virtual disk on a file system-based volume.
|Block
|Stores the virtual disk directly on the block volume. Only use `Block` if the underlying storage supports it.

.3+|Access Mode
|ReadWriteOnce (RWO)
|Volume can be mounted as read/write by a single node.
|ReadWriteMany (RWX)
|Volume can be mounted as read/write by many nodes at one time.
[NOTE]
====
This mode is required for live migration.
====
|ReadOnlyMany (ROX)
|Volume can be mounted as read only by many nodes.

[NOTE]
====
`ReadWriteMany` access mode is required for live migration.
====
.2+|Access Mode
|ReadWriteOnce (RWO)
|Volume can be mounted as read-write by a single node.
|ReadOnlyMany (ROX)
|Volume can be mounted as read only by many nodes.
|===

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-mounting-windows-driver-disk-on-vm_{context}"]

= Mounting a Windows driver disk on a virtual machine

[role="_abstract"]
You can mount a Windows driver disk on a virtual machine (VM) by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Select the required VM to open the *VirtualMachine details* page.
. On the *Configuration* tab, click *Storage*.
. Select the *Mount Windows drivers disk* checkbox.
+
The Windows driver disk is displayed in the list of mounted disks.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-adding-secret-configmap-service-account-to-vm_{context}"]

= Adding a secret, config map, or service account to a virtual machine

[role="_abstract"]
You can add a secret, config map, or service account to a virtual machine by using the OpenShift Container Platform web console.

These resources are added to the virtual machine as disks. You then mount the secret, config map, or service account as you would mount any other disk.

If the virtual machine is running, changes do not take effect until you restart the virtual machine. The newly added resources are marked as pending changes at the top of the page.

.Prerequisites

* The secret, config map, or service account that you want to add must exist in the same namespace as the target virtual machine.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.
. Select a virtual machine to open the *VirtualMachine details* page.
. Click *Configuration* -> *Environment*.
. Click *Add Config Map, Secret or Service Account*.
. Click *Select a resource* and select a resource from the list. A six character serial number is automatically generated for the selected resource.
. Optional: Click *Reload* to revert the environment to its last saved state.
. Click *Save*.

.Verification

. On the *VirtualMachine details* page, click *Configuration* -> *Disks* and verify that the resource is displayed in the list of disks.

. Restart the virtual machine by clicking *Actions* -> *Restart*.

You can now mount the secret, config map, or service account as you would mount any other disk.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

[id="virt-updating-multiple-vms_{context}"]
= Updating multiple virtual machines

[role="_abstract"]
You can use the command line interface (CLI) to update multiple virtual machines (VMs) at the same time.

.Prerequisites

* You installed the {oc-first}.
* You have access to the OpenShift Container Platform cluster, and you have `cluster-admin` permissions.

.Procedure

. Create a privileged service account by running the following commands:
+
[source,terminal]
----
$ oc adm new-project kubevirt-api-lifecycle-automation
----
+
[source,terminal]
----
$ oc create sa kubevirt-api-lifecycle-automation -n kubevirt-api-lifecycle-automation
----
+
[source,terminal]
----
$ oc create clusterrolebinding kubevirt-api-lifecycle-automation --clusterrole=cluster-admin --serviceaccount=kubevirt-api-lifecycle-automation:kubevirt-api-lifecycle-automation
----

. Determine the pull URL for the `kubevirt-api-lifecycle` image by running the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-cnv -l=operators.coreos.com/kubevirt-hyperconverged.openshift-cnv -ojson | jq '.items[0].spec.relatedImages[] | select(.name|test(".*kubevirt-api-lifecycle-automation.*")) | .image'
----

. Deploy `Kubevirt-Api-Lifecycle-Automation` by creating a job object as shown in the following example:
+
[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
 name: kubevirt-api-lifecycle-automation
 namespace: kubevirt-api-lifecycle-automation
spec:
 template:
  spec:
   containers:
   - name: kubevirt-api-lifecycle-automation
     image: quay.io/openshift-virtualization/kubevirt-api-lifecycle-automation:v4.22
     imagePullPolicy: Always
     env:
     - name: MACHINE_TYPE_GLOB
       value: smth-glob9.10.0
     - name: RESTART_REQUIRED
       value: "true"
     - name: NAMESPACE
       value: "default"
     - name: LABEL_SELECTOR
       value: my-vm
     securityContext:
      allowPrivilegeEscalation: false
      capabilities:
       drop:
       - ALL
      privileged: false
      runAsNonRoot: true
      seccompProfile:
       type: RuntimeDefault
   restartPolicy: Never
   serviceAccountName: kubevirt-api-lifecycle-automation
----
+
where:
+
`quay.io/openshift-virtualization/kubevirt-api-lifecycle-automation:v4.22`:: Specifies the pull URL for your image. Replace the image value in this example with your pull URL for the image.
`MACHINE_TYPE_GLOB`:: Specifies the pattern that is used to detect deprecated machine types that need to be upgraded. Replace the `MACHINE_TYPE_GLOB` value with your own pattern.
`RESTART_REQUIRED`:: Specifies whether VMs should be restarted after the machine type is updated. If the `RESTART_REQUIRED` environment variable is set to `true`, VMs are restarted after the machine type is updated. If you do not want VMs to be restarted, set this value to `false`.
`NAMESPACE`:: Specifies the namespace to look for VMs in. Leave the parameter empty for the job to go over all namespaces in the cluster.
`LABEL_SELECTOR`:: Specifies which VMs receive the job action. If you want the job to go over all VMs in the cluster, do not assign a value to the parameter.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-edit-vms.adoc

[id="virt-performing-actions-on-multiple-virtual-machines_{context}"]
= Performing bulk actions on virtual machines

[role="_abstract"]
You can perform bulk actions on multiple virtual machines (VMs) simultaneously by using the *VirtualMachines* list view in the web console. This allows you to efficiently manage a group of VMs with minimal manual effort.

Available bulk actions:

* *Label VMs* - Add, edit, or remove labels that are applied across selected VMs.
* *Delete VMs* - Select multiple VMs to delete. The confirmation dialog displays the number of VMs selected for deletion.
* *Move VMs to folder* - Move selected VMs to a folder. All VMs must belong to the same namespace.
* *LiveMigration* - Perform live migration of multiple selected VMs. The confirmation dialog displays the number of VMs selected for migration. The target node is chosen automatically; there is no option of specifying it.
* *Take snapshot* - Take snapshots of multiple VMs. The *Take snapshots* dialog allows you to enter a suffix for the names of the resulting snapshots.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-edit-vms.adoc

[id="virt-configure-multiple-iothreads_{context}"]
= Configuring multiple I/O threads for fast storage access

[role="_abstract"]
You can improve storage performance by configuring multiple I/O threads for a virtual machine (VM) that uses fast storage, such as solid-state drive (SSD) or non-volatile memory express (NVMe). This configuration option is only available by editing YAML of the VM.

[NOTE]
====
Multiple I/O threads are supported only when `blockMultiQueue` is enabled and the disk bus is set to `virtio`. You must set this configuration for the configuration to work correctly.
====

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *YAML* tab to open the VM manifest.

. In the YAML editor, locate the `spec.template.spec.domain` section and add or modify the following fields:
+
[source,yaml]
----
domain:
  ioThreadsPolicy: supplementalPool
  ioThreads:
    supplementalPoolThreadCount: 4
  devices:
    blockMultiQueue: true
    disks:
    - name: datavolume
      disk:
        bus: virtio
# ...
----

. Click *Save*.
+
[IMPORTANT]
====
The `spec.template.spec.domain` setting cannot be changed while the VM is running. You must stop the VM before applying the changes, and then restart the VM for the new settings to take effect.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring shared volumes for virtual machines
* Understanding config maps
* Providing sensitive data to pods
* Understanding and creating service accounts
