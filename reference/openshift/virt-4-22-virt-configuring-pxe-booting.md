---
title: "Configuring PXE booting for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-pxe-booting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-pxe-booting
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring PXE booting for virtual machines

[id="configuring-pxe-booting"]
= Configuring PXE booting for virtual machines

[role="_abstract"]
PXE booting, or network booting, is available in {VirtProductName}. Network booting allows a computer to boot and load an operating system or other program without requiring a locally attached storage device. For example, you can use it to choose your desired OS image from a PXE server when deploying a new host.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pxe-booting.adoc

[id="virt-pxe-booting-with-mac-address_{context}"]
= PXE booting with a specified MAC address

[role="_abstract"]
As an administrator, you can boot a client over the network by first creating a `NetworkAttachmentDefinition` object for your PXE network.
Then, reference the network attachment definition in your virtual machine instance configuration file before you start the virtual machine instance.

You can also specify a MAC address in the virtual machine instance configuration file, if required by the PXE server.

.Prerequisites

* A Linux bridge must be connected.
* The PXE server must be connected to the same VLAN as the bridge.
* You have installed the {oc-first}.

.Procedure

. Configure a PXE network on the cluster:

.. Create the network attachment definition file for PXE network `pxe-net-conf`:
+
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: pxe-net-conf
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "name": "pxe-net-conf",
      "type": "bridge",
      "bridge": "bridge-interface",
      "macspoofchk": false,
      "vlan": 100,
      "disableContainerInterface": true,
      "preserveDefaultVlan": false
    }
----
** `metadata.name` specifies the name for the `NetworkAttachmentDefinition` object.
** `spec.config.name` specifies the name for the configuration. It is recommended to match the configuration name to the `name` value of the network attachment definition.
** `spec.config.type` specifies the actual name of the Container Network Interface (CNI) plugin that provides the network for this network attachment definition. This example uses a Linux bridge CNI plugin. You can also use an OVN-Kubernetes localnet or an SR-IOV CNI plugin.
** `spec.config.bridge` specifies the name of the Linux bridge configured on the node.
** `spec.config.macspoofchk` is an optional flag to enable the MAC spoof check. When set to `true`, you cannot change the MAC address of the pod or guest interface. This attribute allows only a single MAC address to exit the pod, which provides security against a MAC spoofing attack.
** `spec.config.vlan` is an optional VLAN tag. No additional VLAN configuration is required on the node network configuration policy.
** `spec.config.preserveDefaultVlan` is an optional flag that indicates whether the VM connects to the bridge through the default VLAN. The default value is `true`.

. Create the network attachment definition by using the file you created in the previous step:
+
[source,terminal]
----
$ oc create -f pxe-net-conf.yaml
----

. Edit the virtual machine instance configuration file to include the details of the interface and network.

.. Specify the network and MAC address, if required by the PXE server.
If the MAC address is not specified, a value is assigned automatically.
+
Ensure that `bootOrder` is set to `1` so that the interface boots first.
In this example, the interface is connected to a network called
`<pxe-net>`:
+
[source,yaml]
----
interfaces:
- masquerade: {}
  name: default
- bridge: {}
  name: pxe-net
  macAddress: de:00:00:00:00:de
  bootOrder: 1
----
+
[NOTE]
====
Boot order is global for interfaces and disks.
====

.. Assign a boot device number to the disk to ensure proper booting after operating system provisioning.
+
Set the disk `bootOrder` value to `2`:
+
[source,yaml]
----
devices:
  disks:
  - disk:
      bus: virtio
    name: containerdisk
    bootOrder: 2
----

.. Specify that the network is connected to the previously created network attachment definition. In this scenario, `<pxe-net>` is connected to the network attachment definition called `<pxe-net-conf>`:
+
[source,yaml]
----
networks:
- name: default
  pod: {}
- name: pxe-net
  multus:
    networkName: pxe-net-conf
----

. Create the virtual machine instance:
+
[source,terminal]
----
$ oc create -f vmi-pxe-boot.yaml
----
+
Example output:
+
[source,terminal]
----
  virtualmachineinstance.kubevirt.io "vmi-pxe-boot" created
----

. Wait for the virtual machine instance to run:
+
[source,terminal]
----
$ oc get vmi vmi-pxe-boot -o yaml | grep -i phase
  phase: Running
----

. View the virtual machine instance using VNC:
+
[source,terminal]
----
$ virtctl vnc vmi-pxe-boot
----

. Watch the boot screen to verify that the PXE boot is successful.

. Log in to the virtual machine instance:
+
[source,terminal]
----
$ virtctl console vmi-pxe-boot
----

.Verification

. Verify the interfaces and MAC address on the virtual machine and that the interface connected to the bridge has the specified MAC address.
In this case, we used `eth1` for the PXE boot, without an IP address. The other interface, `eth0`, got an IP address from OpenShift Container Platform.
+
[source,terminal]
----
$ ip addr
----
+
Example output:
+
[source,terminal]
----
...
3. eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
   link/ether de:00:00:00:00:de brd ff:ff:ff:ff:ff:ff
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pxe-booting.adoc
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-networking-glossary_{context}"]
= {VirtProductName} networking glossary

[role="_abstract"]
The following terms are used throughout {VirtProductName} documentation.

Container Network Interface (CNI):: A Cloud Native Computing Foundation
project, focused on container network connectivity.
{VirtProductName} uses CNI plugins to build upon the basic Kubernetes networking functionality.

Multus:: A "meta" CNI plugin that allows multiple CNIs to exist so that a pod or virtual machine can use the interfaces it needs.

Custom resource definition (CRD):: A Kubernetes
API resource that allows you to define custom resources, or an object defined by using the CRD API resource.

`NetworkAttachmentDefinition`:: A CRD introduced by the Multus project that allows you to attach pods, virtual machines, and virtual machine instances to one or more networks.

`UserDefinedNetwork`:: A namespace-scoped CRD introduced by the user-defined network (UDN) API that can be used to create a tenant network that isolates the tenant namespace from other namespaces.

`ClusterUserDefinedNetwork`:: A cluster-scoped CRD introduced by the user-defined network API that cluster administrators can use to create a shared network across multiple namespaces.

`NodeNetworkConfigurationPolicy`:: A CRD introduced by the nmstate project, describing the requested network configuration on nodes.
You update the node network configuration, including adding and removing interfaces, by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.
