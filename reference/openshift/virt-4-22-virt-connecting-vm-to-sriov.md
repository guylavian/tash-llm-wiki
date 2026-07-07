---
title: "Connecting a virtual machine to an SR-IOV network"
type: reference
domain: openshift
slug: virt-4-22-virt-connecting-vm-to-sriov
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-connecting-vm-to-sriov
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connecting a virtual machine to an SR-IOV network

[id="virt-connecting-vm-to-sriov"]
= Connecting a virtual machine to an SR-IOV network

[role="_abstract"]
You can connect a virtual machine (VM) to the physical network by using a Single Root I/O Virtualization (SR-IOV) device.

To configure the SR-IOV network and attach the VM to that network, perform the following steps:

. Configure an SR-IOV physical network device.
. Define the secondary SR-IOV network.
. Attach the VM to the SR-IOV network.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-device.adoc
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="nw-sriov-configuring-device_{context}"]
= Configuring SR-IOV network devices

[role="_abstract"]
The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform.
You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR).

[NOTE]
=====
When applying the configuration specified in a `SriovNetworkNodePolicy` CR, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes.
Reboot only happens in the following cases:

* With Mellanox NICs (`mlx5` driver) a node reboot happens every time the number of virtual functions (VFs) increase on a physical function (PF).
* With Intel NICs, a reboot only happens if the kernel parameters do not include `intel_iommu=on` and `iommu=pt`.

It might take several minutes for a configuration change to apply.
=====

.Prerequisites

* You installed the {oc-first}.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the SR-IOV Network Operator.
* You have enough available nodes in your cluster to handle the evicted workload from drained nodes.
* You have not selected any control plane nodes for SR-IOV network device configuration.

.Procedure

. Create an `SriovNetworkNodePolicy` object, and then save the YAML in the `<name>-sriov-node-network.yaml` file. Replace `<name>` with the name for this configuration.
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  priority: <priority>
  mtu: <mtu>
  numVfs: <num>
  nicSelector:
    vendor: "<vendor_code>"
    deviceID: "<device_id>"
    pfNames: ["<pf_name>", ...]
    rootDevices: ["<pci_bus_id>", "..."]
  deviceType: vfio-pci
  isRdma: false
----
** `metadata.name` defines a name for the `SriovNetworkNodePolicy` object.
** `metadata.namespace` defines the namespace where the SR-IOV Network Operator is installed.
** `spec.resourceName` defines the resource name of the SR-IOV device plugin. You can create multiple `SriovNetworkNodePolicy` objects for a resource name.
** `spec.nodeSelector.feature.node.kubernetes.io/network-sriov.capable` defines the node selector to select which nodes are configured. Only SR-IOV network devices on selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed only on selected nodes.
** `spec.priority` is an optional field that defines an integer value between `0` and `99`. A smaller number gets higher priority, so a priority of `10` is higher than a priority of `99`. The default value is `99`.
** `spec.mtu` is an optional field that defines a value for the maximum transmission unit (MTU) of the virtual function. The maximum MTU value can vary for different NIC models.
** `spec.numVfs` defines the number of the virtual functions (VF) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`.
** `spec.nicSelector` defines the Ethernet device for the Operator to configure. You do not need to specify values for all the parameters.
+
[NOTE]
====
It is recommended to identify the Ethernet adapter with enough precision to minimize the possibility of selecting an Ethernet device unintentionally.
If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`.
====
+
If you specify both `pfNames` and `rootDevices` at the same time, ensure that they point to an identical device.
** `spec.nicSelector.vendor` is an optional field that defines the vendor hex code of the SR-IOV network device. The only allowed values are either `8086` or `15b3`.
** `spec.nicSelector.deviceID` is an optional field that defines the device hex code of SR-IOV network device. The only allowed values are `158b`, `1015`, `1017`.
** `spec.nicSelector.pfNames` is an optional field that defines an array of one or more physical function (PF) names for the Ethernet device.
** `spec.nicSelector.rootDevices` is an optional field that defines an array of one or more PCI bus addresses for the physical function of the Ethernet device. Provide the address in the following format: `0000:02:00.1`.
** `spec.deviceType` defines the driver type. The `vfio-pci` driver type is required for virtual functions in {VirtProductName}.
** `spec.isRdma` is an optional field that defines whether to enable remote direct memory access (RDMA) mode. For a Mellanox card, set `isRdma` to `false`. The default value is `false`.
+
[NOTE]
====
If `isRDMA` flag is set to `true`, you can continue to use the RDMA enabled VF as a normal network device.
A device can be used in either mode.
====

. Optional: Label the SR-IOV capable cluster nodes with `SriovNetworkNodePolicy.Spec.NodeSelector` if they are not already labeled. For more information about labeling nodes, see "Understanding how to update labels on nodes".

. Create the `SriovNetworkNodePolicy` object. When running the following command, replace `<name>` with the name for this configuration:
+
[source,terminal]
----
$ oc create -f <name>-sriov-node-network.yaml
----
+
After applying the configuration update, all the pods in the `sriov-network-operator` namespace change to the `Running` status.

. To verify your SR-IOV network device configuration, enter the following command and replace `<node_name>` with the name of the node where you configured the device.
+
[source,terminal]
----
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc

[id="nw-sriov-additional-network_{context}"]
= Configuring SR-IOV additional network

[role="_abstract"]
You can configure an additional network that uses SR-IOV hardware by creating an `{rs}` object.
When you create an `{rs}` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.

[NOTE]
=====
Do not modify or delete an `{rs}` object if it is attached to {object} in a `running` state.
=====

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create the following `SriovNetwork` object, and then save the YAML in the `<name>-sriov-network.yaml` file. Replace `<name>` with a name for this additional network.
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  vlan: <vlan>
  spoofChk: "<spoof_check>"
  linkState: <link_state>
  maxTxRate: <max_tx_rate>
  minTxRate: <min_rx_rate>
  vlanQoS: <vlan_qos>
  trust: "<trust_vf>"
  capabilities: <capabilities>
  ipam: {}
  linkState: <link_state>
  maxTxRate: <max_tx_rate>
  minTxRate: <min_tx_rate>
  vlanQoS: <vlan_qos>
  trust: "<trust_vf>"
  capabilities: <capabilities>
----
** `metadata.name` defines a name for the `SriovNetwork` object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name.
** `metadata.namespace` defines the namespace where the SR-IOV Network Operator is installed.
** `spec.resourceName` defines the value of the `.spec.resourceName` parameter in the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
** `spec.networkNamespace` defines the target namespace for the `SriovNetwork` object. Only {object} in the target namespace can attach to the `SriovNetwork` object.
** `spec.vlan` an optional field that defines a Virtual LAN (VLAN) ID for the additional network. The integer value must be from `0` to `4095`. The default value is `0`.
** `spec.spoofChk` an optional field that defines the spoof check mode of the VF. The allowed values are the strings `"on"` and `"off"`.
+
[IMPORTANT]
====
You must enclose the value you specify in quotes or the CR is rejected by the SR-IOV Network Operator.
====
** `spec.linkState` an optional field that defines the link state of virtual function (VF). Allowed values are `enable`, `disable` and `auto`.
** `spec.maxTxRate` an optional field that defines the maximum transmission rate, in Mbps, for the VF.
** `spec.minTxRate` an optional field that defines the minimum transmission rate, in Mbps, for the VF. This value should always be less than or equal to the maximum transmission rate.
+
[NOTE]
====
Intel NICs do not support the `minTxRate` parameter. For more information, see BZ#1772847.
====
** `spec.vlanQoS` an optional field that defines the IEEE 802.1p priority level for the VF. The default value is `0`.
** `spec.trust` an optional field that defines the trust mode of the VF. The allowed values are the strings `"on"` and `"off"`.
+
[IMPORTANT]
====
You must enclose the value you specify in quotes or the CR is rejected by the SR-IOV Network Operator.
====
** `spec.capabilities` an optional field that defines the capabilities to configure for this network.
You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support.
** `spec.capabilities` defines a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

. To create the object, enter the following command. Replace `<name>` with a name for this additional network.
+
[source,terminal]
----
$ oc create -f <name>-sriov-network.yaml
----

. Optional: To confirm that the `NetworkAttachmentDefinition` object associated with the `SriovNetwork` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the namespace you specified in the `SriovNetwork` object.
+
[source,terminal]
----
$ oc get net-attach-def -n <namespace>
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc

[id="virt-attaching-vm-to-sriov-network_{context}"]
= Connecting a virtual machine to an SR-IOV network by using the CLI

[role="_abstract"]
You can connect the virtual machine (VM) to the SR-IOV network by including the network details in the VM configuration.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Add the SR-IOV network details to the `spec.domain.devices.interfaces` and `spec.networks` stanzas of the VM configuration as in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  domain:
    devices:
      interfaces:
      - name: nic1
        sriov: {}
  networks:
  - name: nic1
    multus:
        networkName: sriov-network
# ...
----
** `spec.template.spec.domain.devices.interfaces.name` specifies a unique name for the SR-IOV interface.
** `spec.template.spec.networks.name` specifies the name of the SR-IOV interface. This must be the same as the `interfaces.name` that you defined earlier.
** `spec.template.spec.networks.multus.networkName` specifies the name of the SR-IOV network attachment definition.

. Apply the virtual machine configuration:
+
[source,terminal]
----
$ oc apply -f <vm_sriov>.yaml
----
+
where:
+
`<vm_sriov>`:: Specifies the name of the virtual machine YAML file.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc

[id="virt-attaching-vm-to-sriov-network-web-console_{context}"]
= Connecting a VM to an SR-IOV network by using the web console

[role="_abstract"]
You can connect a VM to the SR-IOV network by including the network details in the VM configuration.

.Prerequisites

* You must create a network attachment definition for the network.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Click a VM to view the *VirtualMachine details* page.
. On the *Configuration* tab, click the *Network interfaces* tab.
. Click *Add network interface*.
. Enter the interface name.
. Select an SR-IOV network attachment definition from the *Network* list.
. Select `SR-IOV` from the *Type* list.
. Optional: Add a network *Model* or *Mac address*.
. Click *Save*.
. Restart or live-migrate the VM to apply the changes.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring DPDK workloads for improved performance
