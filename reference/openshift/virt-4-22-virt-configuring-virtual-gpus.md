---
title: "Configuring virtual GPUs"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-virtual-gpus
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-virtual-gpus
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring virtual GPUs

[id="virt-configuring-virtual-gpus"]
= Configuring virtual GPUs

[role="_abstract"]
Use the NVIDIA GPU operator to create virtual GPUs (vGPUs) and assign them to virtual machines (VMs) in {VirtProductName}.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-about-using-virtual-gpus_{context}"]
= About using virtual GPUs with {VirtProductName}

[role="_abstract"]
You can create vGPUs for your VMs using supported GPU cards. You can use the NVIDIA GPU Operator to manage the lifecycle and creation of these vGPUs on the cluster nodes. You must add these devices to the `HyperConverged` custom resource (CR) so that {VirtProductName} can discover and make them available to virtual machines.

[NOTE]
====
Refer to your hardware vendor's documentation for functionality and support details.
====

Mediated device:: A physical device that is divided into one or more virtual devices. A vGPU is a type of mediated device (mdev); the performance of the physical GPU is divided among the virtual devices. You can assign mediated devices to one or more virtual machines (VMs), but the number of guests must be compatible with your GPU. Some GPUs do not support multiple guests.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/configuring-pci-passthrough.adoc
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-adding-kernel-arguments-enable-IOMMU_{context}"]
= Adding kernel arguments to enable the IOMMU driver

[role="_abstract"]
You must enable the Input-Output Memory Management Unit (IOMMU) driver before you can configure mediated devices. To enable the IOMMU driver in the kernel, create the `MachineConfig` object and add the kernel arguments.

.Prerequisites

* You have cluster administrator permissions.
* Your CPU hardware is Intel or AMD.
+
[NOTE]
====
Enabling IOMMU is not required on `s390x` architecture.
====
* You enabled Intel Virtualization Technology for Directed I/O extensions or AMD IOMMU in the BIOS.
* You have installed the {oc-first}.

.Procedure

. Create a `MachineConfig` object that identifies the kernel argument. The following example shows a kernel argument for an Intel CPU.

+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-worker-iommu
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
      - intel_iommu=on
# ...
----
** `metadata.labels.machineconfiguration.openshift.io/role` specifies that the new kernel argument is applied only to worker nodes.
** `metadata.name` specifies the ranking of this kernel argument (100) among the machine configs and its purpose. If you have an AMD CPU, specify the kernel argument as `amd_iommu=on`.
** `spec.kernelArguments` specifies the kernel argument as `intel_iommu` for an Intel CPU.

. Create the new `MachineConfig` object:
+
[source,terminal]
----
$ oc create -f 100-worker-kernel-arg-iommu.yaml
----

.Verification

.  Verify that the new `MachineConfig` object was added by entering the following command and observing the output:
+
[source,terminal]
----
$ oc get MachineConfig
----
+
Example output:
+
[source,terminal]
----
NAME                                       IGNITIONVERSION                    AGE
00-master                                   3.5.0                             164m
00-worker                                   3.5.0                             164m
01-master-container-runtime                 3.5.0                             164m
01-master-kubelet                           3.5.0                             164m
01-worker-container-runtime                 3.5.0                             164m
01-worker-kubelet                           3.5.0                             164m
100-master-chrony-configuration             3.5.0                             169m
100-master-set-core-user-password           3.5.0                             169m
100-worker-chrony-configuration             3.5.0                             169m
100-worker-iommu                            3.5.0                             14s
----

. Verify that IOMMU is enabled at the operating system (OS) level by entering the following command:
+
[source,terminal]
----
$ dmesg | grep -i iommu
----
* If IOMMU is enabled, output is displayed as shown in the following example:
+
Example output:
+
[source,terminal]
----
Intel: [ 0.000000] DMAR: Intel(R) IOMMU Driver
AMD: [ 0.000000] AMD-Vi: IOMMU Initialized
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="using-nvidia-gpu_{context}"]
= Using the NVIDIA GPU Operator

[role="_abstract"]
You can use the NVIDIA GPU Operator to provision worker nodes for running GPU-accelerated virtual machines (VMs) in {VirtProductName}.

The NVIDIA GPU Operator manages NVIDIA GPU resources in an OpenShift Container Platform cluster and automates tasks when preparing nodes for GPU workloads.
The NVIDIA GPU Operator can also facilitate provisioning complex artificial intelligence and machine learning (AI/ML) workloads.

[NOTE]
====
You can get support for the NVIDIA GPU Operator through NVIDIA. For more information, see "Obtaining Support from NVIDIA" in the Red{nbsp}Hat Knowledgebase.
====

.Procedure

. Configure your `ClusterPolicy` manifest. Your `ClusterPolicy` manifest must match the provided example:
+
[source,yaml]
----
apiVersion: nvidia.com/v1
kind: ClusterPolicy
metadata:
  name: gpu-cluster-policy
spec:
  daemonsets:
    updateStrategy: RollingUpdate
  dcgm:
    enabled: true
  dcgmExporter: {}
  devicePlugin: {}
  driver:
    enabled: false
    kernelModuleType: auto
  gfd: {}
  mig:
    strategy: single
  migManager:
    enabled: true
  nodeStatusExporter:
    enabled: true
  operator:
    defaultRuntime: crio
    initContainer: {}
    runtimeClass: nvidia
    use_ocp_driver_toolkit: true
  sandboxDevicePlugin:
    enabled: true
  sandboxWorkloads:
    defaultWorkload: vm-vgpu
    enabled: true
  toolkit:
    enabled: true
    installDir: /usr/local/nvidia
  validator:
    plugin:
      env:
      - name: WITH_WORKLOAD
        value: "true"
  vfioManager:
    enabled: true
  vgpuDeviceManager:
    config:
      default: default
      name: vgpu-devices-config
    enabled: true
  vgpuManager:
    enabled: true
    image: <vgpu_image_name>
    repository: <vgpu_container_registry>
    version: <nvidia_vgpu_manager_version>
----
+
where:
+
`<vgpu_image_name>`:: Specifies the vGPU image name.
`<vgpu_container_registry>`:: Specifies the vGPU container registry value.
`<nvidia_vgpu_manager_version>`:: Specifies the version of the vGPU driver you have downloaded from the NVIDIA website and used to build the image.

. Use the NVIDIA GPU Operator to configure mediated devices. For more information see NVIDIA GPU Operator with OpenShift Virtualization.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-label-nodes-with-mig-backed-profile_{context}"]
= Labeling nodes with a MIG-backed vGPU profile

[role="_abstract"]
If you have GPUs that support NVIDIA Multi-Instance GPU (MIG), you can select a MIG-backed vGPU instance instead of time-sliced vGPU instances. When you use MIG, you give a partition of dedicated hardware to selected VMs.

.Prerequisites

* You have configured vGPU support.
* You have the NVIDIA GPU Operator version 25.10 or higher.
* You are using the NVIDIA AI Enterprise (AIE) vGPU Manager image.

.Procedure

* Label the node with the name of the MIG-backed vGPU profile:
+
[source,terminal]
----
$ oc label node <node> --overwrite nvidia.com/vgpu.config=<profile>
----
** Replace `<node>` with the fully qualified domain name (FQDN) of your compute node.
** Replace `<profile>` with a supported MIG profile.
+
Example command:
+
[source,terminal]
----
$ oc label node worker_1 --overwrite nvidia.com/vgpu.config=A30-1-6C
----

// Module included in the following assemblies:
//
// * virt/managing_vms/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-creating-exposing-mediated-devices_{context}"]
= Creating and exposing mediated devices

[role="_abstract"]
As an administrator, you can create mediated devices and expose them to the cluster by editing the `HyperConverged` custom resource (CR). Before you edit the CR, explore a worker node to find the configuration values that are specific to your hardware devices.

.Prerequisites

* You installed the {oc-first}.
* You enabled the Input-Output Memory Management Unit (IOMMU) driver.
* If your hardware vendor provides drivers, you installed them on the nodes where you want to create mediated devices.
** If you use NVIDIA cards, you installed the NVIDIA GRID driver.

// [IMPORTANT]
// ====
// Before {VirtProductName} 4.14, the `mediatedDeviceTypes` field was named `mediatedDevicesTypes`. Ensure that you use the correct field name when configuring mediated devices.
// ====

.Procedure

. Identify the name selector and resource name values for the mediated devices by exploring a worker node:

.. Start a debugging session with the worker node by using the `oc debug` command. For example:
+
[source,terminal]
----
$ oc debug node/node-11.redhat.com
----

.. Change the root directory of the shell process to the file system of the host node by running the following command:
+
[source,terminal]
----
# chroot /host
----

.. Navigate to the `mdev_bus` directory and view its contents. Each subdirectory name is a PCI address of a physical GPU. For example:
+
[source,terminal]
----
# cd sys/class/mdev_bus && ls
----
+
Example output:
+
[source,terminal]
----
0000:4b:00.4
----

.. Go to the directory for your physical device and list the supported mediated device types as defined by the hardware vendor. For example:
+
[source,terminal]
----
# cd 0000:4b:00.4 && ls mdev_supported_types
----
+
Example output:
+
[source,terminal]
----
nvidia-742  nvidia-744	nvidia-746  nvidia-748	nvidia-750  nvidia-752
nvidia-743  nvidia-745	nvidia-747  nvidia-749	nvidia-751  nvidia-753
----

.. Select the mediated device type that you want to use and identify its name selector value by viewing the contents of its `name` file. For example:
+
[source,terminal]
----
# cat nvidia-745/name
----
+
Example output:
+
[source,terminal]
----
NVIDIA A2-2Q
----

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Create and expose the mediated devices by updating the configuration:

.. Expose the mediated devices to the cluster by adding the `mdevNameSelector` and `resourceName` values to the `spec.permittedHostDevices.mediatedDevices` stanza. The `resourceName` value is based on the `mdevNameSelector` value, but you use underscores instead of spaces.
+
Example `HyperConverged` CR:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  permittedHostDevices:
    mediatedDevices:
    - mdevNameSelector: NVIDIA A2-2Q
      resourceName: nvidia.com/NVIDIA_A2-2Q
      externalResourceProvider: true
    - mdevNameSelector: NVIDIA A2-4Q
      resourceName: nvidia.com/NVIDIA_A2-4Q
      externalResourceProvider: true
# ...
----
+
where:

`mdevNameSelector`:: Specifies the mediated devices that map to this value on the host.

`resourceName`:: Specifies the matching resource name that is allocated on the node.

`externalResourceProvider`:: Specifies that the device is handled by an external provider, such as the NVIDIA GPU Operator.

. Save your changes and exit the editor.

.Verification

* Confirm that the virtual GPU is attached to the node by running the following command:
+
[source,terminal]
----
$ oc get node <node_name> -o json \
  | jq '.status.allocatable \
  | with_entries(select(.key | startswith("nvidia.com/"))) \
  | with_entries(select(.value != "0"))'
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-removing-mediated-device-from-cluster-cli_{context}"]
= Removing mediated devices from the cluster

[role="_abstract"]
As a cluster administrator you can remove mediated devices from the cluster so that you can reallocate GPU hardware. To remove a mediated device from the cluster, delete the information for that device from the `HyperConverged` CR.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Remove the device information from the `spec.permittedHostDevices` stanza of the `HyperConverged` CR. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  permittedHostDevices:
    mediatedDevices:
    - mdevNameSelector: GRID T4-2Q
      resourceName: nvidia.com/GRID_T4-2Q
      externalResourceProvider: true
----
** To remove the `GRID T4-2Q` device, delete the `mdevNameSelector` field and its corresponding `resourceName` field.

. Save your changes and exit the editor.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-assigning-mdev-vm-cli_{context}"]
= Assigning a vGPU to a VM by using the CLI

[role="_abstract"]
Assign mediated devices such as virtual GPUs (vGPUs) to virtual machines (VMs).

.Prerequisites

* The mediated device is configured in the `HyperConverged` custom resource.
* The virtual machine (VM) is stopped.

.Procedure

* Assign the mediated device to a VM by editing the `spec.domain.devices.gpus` stanza of the `VirtualMachine` manifest.
+
Example virtual machine manifest:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  domain:
    devices:
      gpus:
      - deviceName: nvidia.com/TU104GL_Tesla_T4
        name: gpu1
      - deviceName: nvidia.com/GRID_T4-2Q
        name: gpu2
----
** `spec.template.spec.domain.devices.gpus.deviceName` specifies the resource name associated with the mediated device.
** `spec.template.spec.domain.devices.gpus.name` specifies a name to identify the device on the VM.

.Verification

* To verify that the device is available from the virtual machine, run the following command, substituting `<device_name>` with the `deviceName` value from the `VirtualMachine` manifest:
+
[source,terminal]
----
$ lspci -nnk | grep <device_name>
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-virtual-gpus.adoc

[id="virt-assigning-vgpu-vm-web_{context}"]
= Assigning a vGPU to a VM by using the web console

[role="_abstract"]
You can assign virtual GPUs to virtual machines by using the OpenShift Container Platform web console.

[NOTE]
====
You can add hardware devices to virtual machines created from customized templates or a YAML file. You cannot add devices to pre-supplied boot source templates for specific operating systems.
====

.Prerequisites

* The vGPU is configured as a mediated device in your cluster.
** To view the devices that are connected to your cluster, click *Compute* -> *Hardware Devices* from the side menu.
* The VM is stopped.

.Procedure

. In the OpenShift Container Platform web console, click *Virtualization* -> *VirtualMachines* from the side menu.
. Select the VM that you want to assign the device to.
. On the *Details* tab, click *GPU devices*.
. Click *Add GPU device*.
. Enter an identifying value in the *Name* field.
. From the *Device name* list, select the device that you want to add to the VM.
. Click *Save*.

.Verification
* To confirm that the devices were added to the VM, click the *YAML* tab and review the `VirtualMachine` configuration. Mediated devices are added to the `spec.domain.devices` stanza.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS
* MIG Support in OpenShift Container Platform
* Configuring PCI passthrough
* Obtaining Support from NVIDIA
* MIG User Guide
