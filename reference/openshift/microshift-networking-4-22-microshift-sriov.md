---
title: "Using the SR-IOV Network Operator"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-sriov
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-sriov
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Using the SR-IOV Network Operator

[id="microshift-sriov"]
= Using the SR-IOV Network Operator

[role="_abstract"]
When you run network-intensive workloads on {microshift-short}, you need a simplified and declarative method to configure and access high-performance networking interfaces. You can optionally install the SR-IOV Network Operator so that you can expose SR-IOV devices as resources and use NetworkAttachmentDefinitions to access Virtual Functions (VFs).

// Module included in the following assemblies:
//
// microshift_networking/microshift-sriov.adoc

[id="microshift-understanding-sriov-con_{context}"]

= Understanding the SR-IOV Network Operator

[role="_abstract"]
SR-IOV (Single Root I/O Virtualization) is a specification that allows a single physical Peripheral Component Interconnect Express (PCIe) device that supports SR-IOV, for example, a Physical Function (PF), to appear as multiple separate physical devices known as Virtual Functions (VFs). You can directly assign VFs to pods, which bypasses the host operating system network stack, improves throughput, and reduces latency for network intensive workloads.

The integration of the SR-IOV Network Operator and CNI provider into {microshift-short} enables declarative access to VFs. As a result, you can expose supported SR-IOV devices as specialized resources within your {microshift-short} pod for more predictable high-speed networking for demanding workloads. The deployed SR-IOV resources operate in the `sriov-network-operator` namespace.

You do not need to manually configure SR-IOV through the operating system. You can also treat VFs as resources that can be reliably mapped to your containerized applications. These resources reduce manual error and ensure consistent, low-latency networking for critical applications.

Here are the components of SR-IOV functionality:

* SR-IOV Network Operator: The SR-IOV Network Operator is a Kubernetes component that detects and manages SR-IOV devices. This component exposes the SR-IOV devices as schedulable resources within {microshift-short}.
* SR-IOV CNI Provider: This Container Network Interface (CNI) provider works with Multus to assign the exposed VFs to the application pods.
* Virtual Functions (VFs): VFs are lightweight PCIe functions exposed by the PF that are assigned to pods.
* NetworkAttachment Definitions: NetworkAttachmentDefinitions are custom resources (CRs) that are used to define the specific network configuration so that application developers can specify the VFs they need access. NetworkAttachmentDefinitions provide the declarative method for accessing VFs.

// Module included in the following assemblies:
//
// microshift_networking/microshift-sriov.adoc

[id="microshift-installing-sriov-proc_{context}"]
= Installing the SR-IOV Network Operator

[role="_abstract"]
Install the necessary SR-IOV components to enable {microshift-short} to discover SR-IOV devices and expose them as resources for scheduling.

.Prerequisites

* You have the required RPM package containing the SR-IOV Network Operator.

.Procedure

. If provided as an optional RPM, install the required `microshift-sriov` RPM package.

. Restart the {microshift-short} service to deploy the SR-IOV resources in the `sriov-network-operator` namespace.

. To specify the required VF configuration based on the available hardware, create an `SriovNetworkNodePolicy` custom resource (CR). For example, save the following YAML as the file `policyoneflag-sriov-node-network.yaml`:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policyoneflag
  namespace: sriov-network-operator
spec:
  resourceName: policyoneflag
  nodeSelector:
    node.kubernetes.io/instance-type: rhde
  priority: 10
  numVfs: 5
  nicSelector:
    pfNames: ["ens5"]
  deviceType: "netdevice"
  isRdma: false
----
+
** The `metadata.name` parameter specifies the name for the custom resource object.
** The `metadata.namespace` parameter specifies the namespace where the SR-IOV Network Operator is installed.
** The `spec.resourceName` parameter specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name.
** (Optional) The `spec.priority` parameter specifies a priority value. The priority is an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`.
** The `spec.numVfs` parameter specifies the number of the virtual functions (VFs) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`.
** The `spec.nicSelector` parameter identifies the device for the Operator to configure. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally. If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique.
** (Optional) The `spec.nicSelector.pfNames` parameter specifies an array of one or more physical function (PF) names for the device.
** (Optional) The `spec.deviceType` parameter specifies the driver type for the virtual functions. The only allowed value is `netdevice`.
** (Optional) The `spec.isRDMA` parameter configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`. If the `spec.isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode. to configure a Mellanox NIC for use with Fast Datapath DPDK applications, set `spec.isRdma` to `true` and additionally set the `needVhostNet` parameter to `true`
+
[NOTE]
====
The `vfio-pci` driver type is not supported.
====
+
. Create the `SriovNetworkNodePolicy` object by entering the following command:
+
[source,terminal]
----
$ oc create -f policyoneflag-sriov-node-network.yaml
----
+
After applying the configuration update, the workload contains the required resources and dependencies for VF access.

. To verify that the SR-IOV network device is configured, enter the following command. Replace `<node_name>` with the name of a node with the SR-IOV network device that you just configured. Expected output shows `Succeeded`.
+
[source,terminal]
----
$ oc get sriovnetworknodestates -n sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
----

. Deploy an `SriovNetwork` custom resource (CR) which references the `SriovNetworkNodePolicy` CR and insert the `metaPlugins` configuration, as in the following example CR. The Operator generates a `NetworkAttachmentDefinition` CR and the VFs become available to the pods. Save the YAML as the file `sriov-network-interface-sysctl.yaml`.
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: onevalidflag
  namespace: sriov-network-operator
spec:
  resourceName: policyoneflag
  networkNamespace: sysctl-tuning-test
  ipam: '{ "type": "static" }'
  capabilities: '{ "mac": true, "ips": true }'
  metaPlugins : |
    {
      "type": "tuning",
      "capabilities":{
        "mac":true
      },
      "sysctl":{
         "net.ipv4.conf.IFNAME.accept_redirects": "1"
      }
    }
----
+
** The `metadata.name` parameter specifies the name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with the same name.
** The `metadata.namespace` parameter specifies the namespace where the SR-IOV Network Operator is installed.
** The `spec.resourceName` parameter displays the value from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
** The `spec.networkNamespace` parameter specifies the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network.
** The `spec.ipam` parameter specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.
** (Optional) The `spec.capabilities` parameter sets capabilities for the additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support.
** (Optional) The `spec.metaPlugins` parameter is used to add additional capabilities to the device. In this use case set the `type` field to `tuning`. Specify the interface-level network `sysctl` you want to set in the `sysctl` field.

. Create the `SriovNetwork` resource by entering the following command:
+
[source,terminal]
----
$ oc create -f sriov-network-interface-sysctl.yaml
----

.Verification

. Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command:
+
[source,terminal]
----
$ oc get network-attachment-definitions -n <namespace>
----
+
Replace `<namespace>` with the value for `networkNamespace` parameter that you specified in the `SriovNetwork` object, for example, `sysctl-tuning-test`. The expected output shows the name of the NAD CRD and the creation age in minutes.
+
[NOTE]
====
There might be a delay before the SR-IOV Network Operator creates the CR.
====
+
. Verify that the tuning CNI is correctly configured and the additional SR-IOV network is attached:

.. Create a `Pod` CR. Save the following YAML as the file `examplepod.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: tunepod
  namespace: sysctl-tuning-test
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "onevalidflag",
          "mac": "0a:56:0a:83:04:0c",
          "ips": ["10.100.100.200/24"]
       }
      ]
spec:
  containers:
  - name: podexample
    image: centos
    command: ["/bin/bash", "-c", "sleep INF"]
    securityContext:
      runAsUser: 2000
      runAsGroup: 3000
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
----
+
** The `annotations.name` parameter specifies the name of the SR-IOV network attachment definition CR.
** (Optional) The `annotations.mac` parameter specifies the MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the `SriovNetwork` object.
** (Optional) The `annotations.ips` parameter specifies the IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object.
+
.. Create the `Pod` CR by entering the following command:
+
[source,terminal]
----
$ oc apply -f examplepod.yaml
----
+
.. Verify that the pod is created by running the following command:
+
[source,terminal]
----
$ oc get pod -n sysctl-tuning-test
----
+
.Example output:
[source,terminal]
----
NAME      READY   STATUS    RESTARTS   AGE
tunepod   1/1     Running   0          47s
----
+
.. Log in to the pod by running the following command:
+
[source,terminal]
----
$ oc rsh -n sysctl-tuning-test tunepod
----
+
.. Verify the values of the configured sysctl flag. Find the value  `net.ipv4.conf.IFNAME.accept_redirects` by running the following command:
+
[source,terminal]
----
$ sysctl net.ipv4.conf.net1.accept_redirects
----

// Module included in the following assemblies:
//
// microshift_networking/microshift-sriov.adoc

[id="supported-devices_{context}"]
= SR-IOV Network Operator supported devices

[role="_abstract"]
The `config.yaml` file lists the supported network devices for the SR-IOV Network Operator.

.SR-IOV Network Operator configuration file

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: supported-nic-ids
data:
  Intel_i40e_XXV710: "8086 158a 154c"
  Intel_i40e_25G_SFP28: "8086 158b 154c"
  Intel_i40e_10G_X710_SFP: "8086 1572 154c"
  Intel_ixgbe_10G_X550: "8086 1563 1565"
  Intel_ixgbe_82576: "8086 10c9 10ca"
  Intel_i40e_X710_X557_AT_10G: "8086 1589 154c"
  Intel_i40e_10G_X710_BACKPLANE: "8086 1581 154c"
  Intel_i40e_10G_X710_BASE_T: "8086 15ff 154c"
  Intel_i40e_XXV710_N3000: "8086 0d58 154c"
  Intel_i40e_40G_XL710_QSFP: "8086 1583 154c"
  Intel_ice_Columbiaville_E810-CQDA2_2CQDA2: "8086 1592 1889"
  Intel_ice_Columbiaville_E810-XXVDA4: "8086 1593 1889"
  Intel_ice_Columbiaville_E810-XXVDA2: "8086 159b 1889"
  Intel_ice_Columbiaville_E810-XXV_BACKPLANE: "8086 1599 1889"
  Intel_ice_Columbiaville_E810: "8086 1591 1889"
  Intel_ice_Columbiapark_E823C: "8086 188a 1889"
  Intel_ice_Columbiapark_E823L_SFP: "8086 124d 1889"
  Intel_ice_Columbiapark_E823L_BACKPLANE: "8086 124c 1889"
  Intel_ice_Columbiapark_E825C_BACKPLANE: "8086 579c 1889"
  Intel_ice_Columbiapark_E825C_QSFP: "8086 579d 1889"
  Intel_ice_Columbiapark_E825C_SFP: "8086 579e 1889"
  Intel_ice_Connorsville_E830_QSFP: "8086 12d2 1889"
  Intel_ice_Connorsville_E830_SFP: "8086 12d3 1889"
  Intel_ice_Connorsville_E835CC_QSFP: "8086 1249 1889"
  Intel_ice_Connorsville_E835CC_SFP: "8086 124a 1889"
  Nvidia_mlx5_ConnectX-4: "15b3 1013 1014"
  Nvidia_mlx5_ConnectX-4LX: "15b3 1015 1016"
  Nvidia_mlx5_ConnectX-5: "15b3 1017 1018"
  Nvidia_mlx5_ConnectX-5_Ex: "15b3 1019 101a"
  Nvidia_mlx5_ConnectX-6: "15b3 101b 101c"
  Nvidia_mlx5_ConnectX-6_Dx: "15b3 101d 101e"
  Nvidia_mlx5_ConnectX-6_Lx: "15b3 101f 101e"
  Nvidia_mlx5_ConnectX-7: "15b3 1021 101e"
  Nvidia_mlx5_ConnectX-8: "15b3 1023 101e"
  Nvidia_mlx5_MT42822_BlueField-2_integrated_ConnectX-6_Dx: "15b3 a2d6 101e"
  Nvidia_mlx5_MT43244_BlueField-3_integrated_ConnectX-7_Dx: "15b3 a2dc 101e"
  Broadcom_bnxt_BCM57414_2x25G: "14e4 16d7 16dc"
  Broadcom_bnxt_BCM75508_2x100G: "14e4 1750 1806"
  Qlogic_qede_QL45000_50G: "1077 1654 1664"
  Red_Hat_Virtio_network_device: "1af4 1000 1000"
  Red_Hat_Virtio_1_0_network_device: "1af4 1041 1041"
  Marvell_OCTEON_TX2_CN96XX: "177d b200 b203"
  Marvell_OCTEON_TX2_CN98XX: "177d b100 b103"
  Marvell_OCTEON_Fusion_CNF95XX: "177d b600 b603"
  Marvell_OCTEON10_CN10XXX: "177d b900 b903"
  Marvell_OCTEON_Fusion_CNF105XX: "177d ba00 ba03"
  Amazon_Elastic_Network_Adapter: "1d0f ec20 ec20"
----

[NOTE]
====
For the most up-to-date list of supported cards and compatible OpenShift Container Platform versions available, see Openshift Single Root I/O Virtualization (SR-IOV) and PTP hardware networks Support Matrix.
====

[id="_additional-resources_microshift-sriov_{context}"]
== Additional resources

* Understanding networking settings
* About using multiple networks
* About network policies
