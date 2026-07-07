---
title: "Configuring PCI passthrough"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-pci-passthrough
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-pci-passthrough
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring PCI passthrough

[id="virt-configuring-pci-passthrough"]
= Configuring PCI passthrough

//This assembly contains the content for
//configuring PCI passthrough by using the CLI. There are
//plans to enable PCI passthrough configuration
//by using the web console (next release).
//When this feature is available in the web console, please
//add the new content to this assembly.

[role="_abstract"]
The Peripheral Component Interconnect (PCI) passthrough feature enables you to access and manage hardware devices from a virtual machine (VM). When PCI passthrough is configured, the PCI devices function as if they were physically attached to the guest operating system.

Cluster administrators can expose and manage host devices that are permitted to be used in the cluster by using the `oc` command-line interface (CLI).

[IMPORTANT]
====
For `vfio-pci` to allocate a PCI device, no other kernel driver can manage that device. If a driver already manages the device, you must add the specific kernel module to a blocklist.

Adding a kernel module to a blocklist makes all devices handled by that module unavailable to the host.
====
The following example shows a `MachineConfig` CR that adds the `enic` network driver to a blocklist by creating a configuration file in `/etc/modprobe.d/` and adding kernel arguments:

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-blacklist-enic
spec:
  config:
    ignition:
      version: 3.4.0
    storage:
      files:
      - contents:
          source: data:,blacklist%20enic%0A
        mode: 420
        overwrite: true
        path: /etc/modprobe.d/blacklist-enic.conf
  kernelArguments:
    - enic.blacklist=1
    - rd.driver.blacklist=enic
----

[id="virt-preparing-nodes-for-gpu-passthrough"]
== Preparing nodes for GPU passthrough

You can prevent GPU operands from deploying on worker nodes that you designated for GPU passthrough.

// Module included in the following assembly:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc
//

[id="virt-preventing-nvidia-gpu-operands-from-deploying-on-nodes_{context}"]
= Preventing NVIDIA GPU operands from deploying on nodes

[role="_abstract"]
If you use the NVIDIA GPU Operator in your cluster, you can apply the `nvidia.com/gpu.deploy.operands=false` label to nodes that you do not want to configure for GPU or vGPU operands. This prevents the creation of the pods that configure GPU or vGPU operands and terminates existing pods.

.Prerequisites

* The {oc-first} is installed.

.Procedure
// Cannot label nodes in ROSA/OSD, but can edit machine pools
* Label the node by running the following command:

+
[source,terminal]
----
$ oc label node <node_name> nvidia.com/gpu.deploy.operands=false
----
+
where:
+
`<node_name>`:: Specifies the name of a node where you do not want to install the NVIDIA GPU operands.

+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> <machinepool_ID> nvidia.com/gpu.deploy.operands=false
----

.Verification

. Verify that the label was added to the node by running the following command:
+
[source,terminal]
----
$ oc describe node <node_name>
----

. Optional: If GPU operands were previously deployed on the node, verify their removal.

.. Check the status of the pods in the `nvidia-gpu-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc get pods -n nvidia-gpu-operator
----
+
Example output:
+
[source,terminal]
----
NAME                             READY   STATUS        RESTARTS   AGE
gpu-operator-59469b8c5c-hw9wj    1/1     Running       0          8d
nvidia-sandbox-validator-7hx98   1/1     Running       0          8d
nvidia-sandbox-validator-hdb7p   1/1     Running       0          8d
nvidia-sandbox-validator-kxwj7   1/1     Terminating   0          9d
nvidia-vfio-manager-7w9fs        1/1     Running       0          8d
nvidia-vfio-manager-866pz        1/1     Running       0          8d
nvidia-vfio-manager-zqtck        1/1     Terminating   0          9d
----

.. Monitor the pod status until the pods with `Terminating` status are removed:
+
[source,terminal]
----
$ oc get pods -n nvidia-gpu-operator
----
+
Example output:
+
[source,terminal]
----
NAME                             READY   STATUS    RESTARTS   AGE
gpu-operator-59469b8c5c-hw9wj    1/1     Running   0          8d
nvidia-sandbox-validator-7hx98   1/1     Running   0          8d
nvidia-sandbox-validator-hdb7p   1/1     Running   0          8d
nvidia-vfio-manager-7w9fs        1/1     Running   0          8d
nvidia-vfio-manager-866pz        1/1     Running   0          8d
----

[id="virt-preparing-host-devices-for-pci-passthrough"]
== Preparing host devices for PCI passthrough

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc

[id="virt-about_pci-passthrough_{context}"]
= About preparing a host device for PCI passthrough

[role="_abstract"]
To prepare a host device for PCI passthrough by using the CLI, create a `MachineConfig` object and add kernel arguments to enable the Input-Output Memory Management Unit (IOMMU).

Bind the PCI device to the Virtual Function I/O (VFIO) driver and then expose it in the cluster by editing the `permittedHostDevices` field of the `HyperConverged` custom resource (CR). The `permittedHostDevices` list is empty when you first install the {VirtProductName} Operator.

To remove a PCI host device from the cluster by using the CLI, delete the PCI device information from the `HyperConverged` CR.

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
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc

[id="virt-binding-devices-vfio-driver_{context}"]
= Binding PCI devices to the VFIO driver

[role="_abstract"]
To bind PCI devices to the VFIO (Virtual Function I/O) driver, obtain the values for the vendor ID and the device ID from each device and create a list with the values. Add this list to the `MachineConfig` object.

The `MachineConfig` Operator generates the `/etc/modprobe.d/vfio.conf` on the nodes with the PCI devices, and binds the PCI devices to the VFIO driver.

.Prerequisites

* You added kernel arguments to enable IOMMU for the CPU.
+
[NOTE]
====
Enabling IOMMU is not required on `s390x` architecture.
====

* You have installed the {oc-first}.

.Procedure

. Run the `lspci` command with the name of the GPU accelerator to obtain the vendor ID and the device ID for the PCI device.
+
[NOTE]
====
NVIDIA GPU is supported on `x86` and `aarch64` architectures, Intel QAT is supported on `x86` architecture, and {ibm-name} Spyre is supported on `s390x` architecture.
====
+
[source,terminal]
----
$ lspci -nnv | grep -i <gpu_accelerator>
----
+
Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`.
+
Example output:
+
[source,terminal]
----
02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
----

. Create a Butane config file, `100-worker-vfiopci.bu`, binding the PCI device to the VFIO driver.
+
[NOTE]
====
The Butane version you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `.0`. See "Creating machine configs with Butane" for information about Butane.
====
+
Example:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 100-worker-vfiopci
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/modprobe.d/vfio.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        options vfio-pci ids=<vendor_id>:<device_id>
  - path: /etc/modules-load.d/vfio-pci.conf
    mode: 0644
    overwrite: true
    contents:
      inline: vfio-pci
----
** `metadata.labels.machineconfiguration.openshift.io/role: worker` specifies that the new kernel argument is applied only to compute nodes.
** `storage.files.contents.inline`, where the path is `/etc/modprobe.d/vfio.conf`, specifies the previously determined hexadecimal vendor ID and device ID values to bind a device to the VFIO driver. You can add a list of multiple devices with their vendor and device information.
** `storage.files.path`, where the `contents.inline` is `vfio-pci`, specifies the file that loads the `vfio-pci` kernel module on the compute nodes.

. Use Butane to generate a `MachineConfig` object file, `100-worker-vfiopci.yaml`, containing the configuration to be delivered to the compute nodes:
+
[source,terminal]
----
$ butane 100-worker-vfiopci.bu -o 100-worker-vfiopci.yaml
----

. Apply the `MachineConfig` object to the compute nodes:
+
[source,terminal]
----
$ oc apply -f 100-worker-vfiopci.yaml
----

. Verify that the `MachineConfig` object was added.
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
NAME                             GENERATEDBYCONTROLLER                      IGNITIONVERSION  AGE
00-master                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
00-worker                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-master-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-master-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-worker-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-worker-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
100-worker-iommu                                                            3.5.0            30s
100-worker-vfiopci-configuration                                            3.5.0            30s
----

.Verification

* Verify that the VFIO driver is loaded.
+
[source,terminal]
----
$ lspci -nnk -d <vendor_id>:
----
+
The output confirms that the VFIO driver is being used.
+
Example output:
+
----
04:00.0 3D controller [0302]: NVIDIA Corporation GP102GL [Tesla P40] [10de:1eb8] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:1eb8]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc

[id="virt-exposing-pci-device-in-cluster-cli_{context}"]
= Exposing PCI host devices in the cluster using the CLI

[role="_abstract"]
To expose PCI host devices in the cluster, add details about the PCI devices to the `spec.permittedHostDevices.pciHostDevices` array of the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the PCI device information to the `spec.permittedHostDevices.pciHostDevices` array.
+
Example configuration file:
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
    pciHostDevices:
    - pciDeviceSelector: "10DE:1DB6"
      resourceName: "nvidia.com/GV100GL_Tesla_V100"
    - pciDeviceSelector: "10DE:1EB8"
      resourceName: "nvidia.com/TU104GL_Tesla_T4"
    - pciDeviceSelector: "8086:6F54"
      resourceName: "intel.com/qat"
      externalResourceProvider: true
# ...
----
** `spec.permittedHostDevices` specifies the host devices that are permitted to be used in the cluster.
** `spec.permittedHostDevices.pciHostDevices` specifies the list of PCI devices available on the node.
** `spec.permittedHostDevices.pciHostDevices.pciDeviceSelector` specifies the vendor ID and the device ID required to identify the PCI device.
** `spec.permittedHostDevices.pciHostDevices.resourceName` specifies the name of a PCI host device.
** `spec.permittedHostDevices.pciHostDevices.externalResourceProvider` is an optional setting. Setting this field to `true` indicates that the resource is provided by an external device plugin. {VirtProductName} allows the usage of this device in the cluster but leaves the allocation and monitoring to an external device plugin.
+
[NOTE]
====
The above example snippet shows two PCI host devices that are named `nvidia.com/GV100GL_Tesla_V100` and `nvidia.com/TU104GL_Tesla_T4` added to the list of permitted host devices in the `HyperConverged` CR. These devices have been tested and verified to work with {VirtProductName}.
====
+
Example configuration file for an {ibm-name} Spyre device on `s390x` architecture:
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
    pciHostDevices:
    - pciDeviceSelector: "1014:06a8"
      resourceName: "ibm.com/spyre"
# ...
----

. Save your changes and exit the editor.

.Verification

* Verify that the PCI host devices were added to the node by running the following command. The example output shows that there is one device each associated with the `nvidia.com/GV100GL_Tesla_V100`, `nvidia.com/TU104GL_Tesla_T4`, and `intel.com/qat` resource names.
+
[source,terminal]
----
$ oc describe node <node_name>
----
+
Example output:
+
[source,terminal]
----
Capacity:
  cpu:                            64
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              915128Mi
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         131395264Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     1
  intel.com/qat:                  1
  pods:                           250
Allocatable:
  cpu:                            63500m
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              863623130526
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         130244288Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     1
  intel.com/qat:                  1
  pods:                           250
----
+
[NOTE]
====
When using an {ibm-name} Spyre device on `s390x` architecture, the allocated device is shown as follows: `ibm.com/spyre:         1`.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc

[id="virt-removing-pci-device-from-cluster_{context}"]
= Removing PCI host devices from the cluster using the CLI

[role="_abstract"]
To remove a PCI host device from the cluster, delete the information for that device from the `HyperConverged` custom resource (CR).

.Prerequisites
* You have installed the {oc-first}.

.Procedure
. Edit the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Remove the PCI device information from the `spec.permittedHostDevices.pciHostDevices` array by deleting the `pciDeviceSelector`, `resourceName` and `externalResourceProvider` (if applicable), fields for the appropriate device. In this example, the user deletes the `nvidia.com/TU104GL_Tesla_T4`.
+
Example configuration file:
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
    pciHostDevices:
    - pciDeviceSelector: "10DE:1DB6"
      resourceName: "nvidia.com/GV100GL_Tesla_V100"
# ...
----

. Save your changes and exit the editor.

.Verification
* Verify that you removed the PCI host device from the node by running the following command. The example output shows that there are zero devices associated with the `nvidia.com/TU104GL_Tesla_T4` resource name.
+
[source,terminal]
----
$ oc describe node <node_name>
----
+
Example output:
+
[source,terminal]
----
Capacity:
  cpu:                            64
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              915128Mi
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         131395264Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     0
  pods:                           250
Allocatable:
  cpu:                            63500m
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              863623130526
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         130244288Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     0
  pods:                           250
----

[id="virt-configuring-vms-for-pci-passthrough"]
== Configuring virtual machines for PCI passthrough

After the PCI devices have been added to the cluster, you can assign them to virtual machines. The PCI devices are now available as if they are physically connected to the virtual machines.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc

[id="virt-assigning-pci-device-virtual-machine_{context}"]
= Assigning a PCI device to a virtual machine

[role="_abstract"]
When a PCI device is available in a cluster, you can assign it to a virtual machine and enable PCI passthrough.

.Procedure

* Assign the PCI device to a virtual machine as a host device.
+
Example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  domain:
    devices:
      hostDevices:
      - deviceName: nvidia.com/TU104GL_Tesla_T4
        name: hostdevices1
----
** `spec.template.spec.domain.devices.hostDevices.deviceName` specifies the name of the PCI device that is permitted on the cluster as a host device. The virtual machine can access this host device. When using an {ibm-name} Spyre device on `s390x` architecture, specify `ibm.com/spyre:`.

.Verification

* Use the following command to verify that the host device is available from the virtual machine.
+
[source,terminal]
----
$ lspci -nnk | grep <gpu_accelerator>
----
Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`.
+
Example output:
+
[source,terminal]
----
$ 02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
----

[id="additional-resources_configuring-pci-passthrough"]
[role="_additional-resources"]
== Additional resources
* Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS
* Managing file permissions
* Machine Config Overview
* {ibm-name} Spyre Accelerator User's Guide
