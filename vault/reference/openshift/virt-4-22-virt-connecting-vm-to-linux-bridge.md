---
title: "Connecting a virtual machine to a Linux bridge network"
type: reference
domain: openshift
slug: virt-4-22-virt-connecting-vm-to-linux-bridge
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-connecting-vm-to-linux-bridge
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connecting a virtual machine to a Linux bridge network

[id="virt-connecting-vm-to-linux-bridge"]
= Connecting a virtual machine to a Linux bridge network

[role="_abstract"]
By default, {VirtProductName} is installed with a single, internal pod network. You can connect a virtual machine (VM) to the physical network by using a Linux bridge.

To create a Linux bridge network and attach a VM to the network, perform the following steps:

. Prepare the node network by creating a Linux bridge node network configuration policy (NNCP).
. Define the secondary Linux bridge network by creating a network attachment definition (NAD).
. Attach the VM to the Linux bridge network.

[NOTE]
====
{VirtProductName} does not support Linux bridge bonding modes 0, 5, and 6. For more information, see "Additional resources".
====

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="virt-creating-linux-bridge-nncp_{context}"]
= Creating a Linux bridge NNCP

[role="_abstract"]
After you install the Kubernetes NMState Operator, you can configure a Linux bridge network for live migration or external access to virtual machines (VMs).

You can create a `NodeNetworkConfigurationPolicy` (NNCP) manifest for a Linux bridge network.

.Prerequisites

* You have installed the Kubernetes NMState Operator.

.Procedure

* Create the `NodeNetworkConfigurationPolicy` manifest. This example includes sample values that you must replace with your own information.
+
[source,yaml]
----
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-policy
spec:
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4:
          enabled: false
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
----
** `metadata.name` defines the name of the node network configuration policy.
** `spec.desiredState.interfaces.name` defines the name of the new Linux bridge.
** `spec.desiredState.interfaces.description` is an optional field that can be used to define a human-readable description for the bridge.
** `spec.desiredState.interfaces.type` defines the interface type. In this example, the type is a Linux bridge.
** `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
** `spec.desiredState.interfaces.ipv4.enabled` defines whether the ipv4 protocol is active. Setting this to `false` disables IPv4 addressing on this bridge.
** `spec.desiredState.interfaces.bridge.options.stp.enabled` defines whether Spanning Tree Protocol (STP) is active. Setting this to `false` disables STP on this bridge.
** `spec.desiredState.interfaces.bridge.port.name` defines the node NIC that the bridge is attached to.
+
[NOTE]
====
To create the NNCP manifest for a Linux bridge using Open Systems Adapter (OSA) with {ibm-z-name}, you must disable VLAN filtering by the setting the `rx-vlan-filter` to `false` in the `NodeNetworkConfigurationPolicy` manifest.

Alternatively, if you have SSH access to the node, you can disable VLAN filtering by running the following command:

[source,terminal]
----
$ sudo ethtool -K <osa-interface-name> rx-vlan-filter off
----
====

// Creating a Linux bridge NAD by using the web console
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc
//This file contains UI elements and/or package names that need to be updated.

[id="virt-creating-linux-bridge-nad-web_{context}"]
= Creating a Linux bridge NAD by using the web console

[role="_abstract"]
Use the OpenShift Container Platform web console to create a network attachment definition (NAD) that connects pods and virtual machines to a layer-2 network.

[WARNING]
====
Configuring IP address management (IPAM) in a network attachment definition for virtual machines is not supported.
====

.Procedure

. In the web console, click *Networking* -> *NetworkAttachmentDefinitions*.
. Click *Create Network Attachment Definition*.
+
[NOTE]
====
The network attachment definition must be in the same namespace as the pod or virtual machine.
====
+
. Enter a unique *Name* and optional *Description*.
. Select *CNV Linux bridge* from the *Network Type* list.
. Enter the name of the bridge in the *Bridge Name* field.
. Optional: If the resource has VLAN IDs configured, enter the ID numbers in the *VLAN Tag Number* field.
+
[NOTE]
====
Open Systems Adapter (OSA) interfaces on {ibm-z-name} do not support VLAN filtering and drop VLAN-tagged traffic. Avoid using VLAN-tagged NADs with OSA interfaces.
====
+
. Optional: Select *MAC Spoof Check* to enable MAC spoof filtering. This feature provides security against a MAC spoofing attack by allowing only a single MAC address to exit the pod.
. Click *Create*.

// Creating a Linux bridge NAD by using the command line
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-creating-linux-bridge-nad-cli_{context}"]
= Creating a Linux bridge NAD by using the CLI

[role="_abstract"]
You can create a network attachment definition (NAD) to provide layer-2 networking to pods and virtual machines (VMs) by using the command line.

The NAD and the VM must be in the same namespace.

[WARNING]
====
Configuring IP address management (IPAM) in a network attachment definition for virtual machines is not supported.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Add the VM to the `NetworkAttachmentDefinition` configuration, as in the following example:
+
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: bridge-network
  annotations:
    k8s.v1.cni.cncf.io/resourceName: bridge.network.kubevirt.io/br1
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "name": "bridge-network",
      "type": "bridge",
      "bridge": "br1",
      "macspoofchk": false,
      "vlan": 100,
      "disableContainerInterface": true,
      "preserveDefaultVlan": false
    }
----
+
[NOTE]
====
OSA interfaces on {ibm-z-name} do not support VLAN filtering and VLAN-tagged traffic is dropped. Avoid using VLAN-tagged NADs with OSA interfaces.
====
+
** `metadata.name` defines the name for the `NetworkAttachmentDefinition` object.
** `metadata.annotations.k8s.v1.cni.cncf.io/resourceName` is optional and defines the annotation key-value pair for node selection for the bridge configured on some nodes. If you add this annotation to your network attachment definition, your virtual machine instances will only run on the nodes that have the defined bridge connected.
** `spec.config.name` defines the name for the configuration. It is recommended to match the configuration name to the `name` value of the network attachment definition.
** `spec.config.type` defines the actual name of the Container Network Interface (CNI) plugin that provides the network for this network attachment definition. Do not change this field unless you want to use a different CNI.
** `spec.config.bridge` defines the name of the Linux bridge configured on the node. The name should match the interface bridge name defined in the `NodeNetworkConfigurationPolicy` manifest.
** `spec.config.macspoofchk` is optional and defines a flag to enable the MAC spoof check. When set to `true`, you cannot change the MAC address of the pod or guest interface. This attribute allows only a single MAC address to exit the pod, which provides security against a MAC spoofing attack.
** `spec.config.vlan` is optional and defines the VLAN tag. No additional VLAN configuration is required on the node network configuration policy.
** `spec.config.preserveDefaultVlan` is optional and defines whether the VM connects to the bridge through the default VLAN. The default value is `true`.

. Optional: If you want to connect a VM to the native network, configure the Linux bridge `NetworkAttachmentDefinition` manifest without specifying any VLAN:
+
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: bridge-network
  annotations:
    k8s.v1.cni.cncf.io/resourceName: bridge.network.kubevirt.io/br1
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "name": "bridge-network",
      "type": "bridge",
      "bridge": "br1",
      "macspoofchk": false,
      "disableContainerInterface": true
    }
----

. Create the network attachment definition:
+
[source,terminal]
----
$ oc create -f network-attachment-definition.yaml
----
+
where:
+
`network-attachment-definition.yaml`:: Specifies the file name of the network attachment definition manifest.

.Verification

* Verify that the network attachment definition was created by running the following command:
+
[source,terminal]
----
$ oc get network-attachment-definition bridge-network
----

// Enabling port isolation for a Linux bridge NAD
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-linux-bridge-nad-port-isolation_{context}"]
= Enabling port isolation for a Linux bridge NAD

[role="_abstract"]
You can enable port isolation for a Linux bridge network attachment definition (NAD) so that virtual machines (VMs) or pods that run on the same virtual LAN (VLAN) can operate in isolation from one another.

The Linux bridge NAD creates a virtual bridge, or _virtual switch_, between network interfaces and the physical network.

Isolating ports in this way can provide enhanced security for VM workloads that run on the same node.

.Prerequisites

* For VMs, you configured either a static or dynamic IP address for each VM. See "Configuring IP addresses for virtual machines".
* You created a Linux bridge NAD by using either the web console or the command-line interface.
* You have installed the {oc-first}.

.Procedure

. Edit the Linux bridge NAD by setting `portIsolation` to `true`:
+
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: bridge-network
  annotations:
    k8s.v1.cni.cncf.io/resourceName: bridge.network.kubevirt.io/br1
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "name": "bridge-network",
      "type": "bridge",
      "bridge": "br1",
      "preserveDefaultVlan": false,
      "vlan": 100,
      "disableContainerInterface": false,
      "portIsolation": true
    }
# ...
----
** `spec.config.name` specifies the name for the configuration. The name must match the value in the `metadata.name` of the NAD.
** `spec.config.type` specifies the actual name of the Container Network Interface (CNI) plugin that provides the network for this network attachment definition. Do not change this field unless you want to use a different CNI.
** `spec.config.bridge` specifies the name of the Linux bridge that is configured on the node. The name must match the interface bridge name defined in the `NodeNetworkConfigurationPolicy` manifest.
** `spec.config.portIsolation` specifies whether port isolation on the virtual bridge is enabled or disabled. The default value is `false`. When set to `true`, each VM or pod is assigned to an isolated port. The virtual bridge prevents traffic from one isolated port from reaching another isolated port.

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f example-vm.yaml
----

. Optional: If you edited a running virtual machine, you must restart it for the changes to take effect.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/managing_vms/ssh/virt-using-secondary-networks-ssh.adoc

[id="virt-vm-creating-nic-web_{context}"]
= Configuring a VM network interface by using the web console

[role="_abstract"]
You can configure a network interface for a virtual machine (VM) by using the OpenShift Container Platform web console.

.Prerequisites

* You created a network attachment definition for the network.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Click a VM to view the *VirtualMachine details* page.
. On the *Configuration* tab, click the *Network interfaces* tab.
. Click *Add network interface*.
. Enter the interface name and select the network attachment definition from the *Network* list.
. Click *Save*.
. Restart or live migrate the VM to apply the changes.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-creating-vms-from-templates.adoc
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-networking-wizard-fields-web_{context}"]
= Networking fields

[role="_abstract"]
The following table describes the networking fields in the virtual machine wizard.

|===
|Name | Description

|Name
|Name for the network interface controller.

|Model
|Indicates the model of the network interface controller. Supported values are *e1000e* and *virtio*.

For {ibm-z-name} (`s390x`) and ARM64 (`arm64`) systems, use the *virtio* NIC model option. The *e1000e* model is not supported on these architectures.

|Network
|List of available network attachment definitions.

|Type
a|List of available binding methods. Select the binding method suitable for the network interface:

* Default pod network: `masquerade`
* Linux bridge network: `bridge`
* SR-IOV network: `SR-IOV`
+
On {ibm-z-name}, `SR-IOV` is not supported.

|MAC Address
|MAC address for the network interface controller. If a MAC address is not specified, one is assigned automatically.
|===

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-attaching-vm-secondary-network-cli_{context}"]
= Configuring a VM network interface by using the CLI

[role="_abstract"]
You can configure a virtual machine (VM) network interface for a bridge network by using the command line.

.Prerequisites

* You have installed the {oc-first}.
* Shut down the virtual machine before editing the configuration. If you edit a running virtual machine, you must restart the virtual machine for the changes to take effect.

.Procedure

. Add the bridge interface and the network attachment definition to the VM configuration as in the following example:
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
      domain:
        devices:
          interfaces:
            - bridge: {}
              name: bridge-net
# ...
      networks:
        - name: bridge-net
          multus:
            networkName: bridge-network
----
+
where:

`spec.template.spec.domain.devices.interface`:: Specifies the name of the bridge interface.
`spec.template.spec.networks.name`:: Specifies the name of the network. This value must match the `name` value of the corresponding `spec.template.spec.domain.devices.interfaces` entry.
`spec.template.spec.networks.multus.networkName`:: Specifies the name of the network attachment definition.

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f example-vm.yaml
----

. Optional: If you edited a running virtual machine, you must restart it for the changes to take effect.
+
[NOTE]
====
When running {VirtProductName} on {ibm-z-name} using OSA, RoCE, or HiperSockets interfaces, you must register the MAC address of the device. For more information, see OSA interface traffic forwarding (IBM documentation).
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring IP addresses for virtual machines
* Which bonding modes work when used with a bridge that virtual machine guests or containers connect to?
