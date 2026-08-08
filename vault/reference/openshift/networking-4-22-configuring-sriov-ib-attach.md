---
title: "Configuring an SR-IOV InfiniBand network attachment"
type: reference
domain: openshift
slug: networking-4-22-configuring-sriov-ib-attach
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-sriov-ib-attach
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring an SR-IOV InfiniBand network attachment

[id="configuring-sriov-ib-attach"]
= Configuring an SR-IOV InfiniBand network attachment

[role="_abstract"]
You can configure an InfiniBand (IB) network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

Before you perform any tasks in the following documentation, ensure that you installed the SR-IOV Network Operator.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc

[id="nw-sriov-ibnetwork-object_{context}"]
= InfiniBand device configuration object

[role="_abstract"]
You can configure an InfiniBand (IB) network device by defining an `SriovIBNetwork` object.

The following YAML describes an `SriovIBNetwork` object:

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovIBNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  ipam: |-
    {}
  linkState: <link_state>
  capabilities: <capabilities>
----

where:

`name`:: A name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name.
`namespace`:: The namespace where the SR-IOV Operator is installed.
`resourceName`:: The value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
`networkNamespace`:: The target namespace for the `SriovIBNetwork` object. Only pods in the target namespace can attach to the network device.
`ipam`:: Optional parameter. A configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.
`linkState`:: Optional parameter. The link state of virtual function (VF). Allowed values are `enable`, `disable` and `auto`.
`capabilities`:: Optional parameter. The capabilities to configure for this network. You can specify `'{ "ips": true }'` to enable IP address support or `'{ "infinibandGUID": true }'` to enable IB Global Unique Identifier (GUID) support.

// Module included in the following assemblies:
//
// * networking/multiple_networks/secondary_networks/configuring-ip-secondary-nwt.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc

[id="nw-multus-configure-dualstack-ip-address_{context}"]
= Creating a configuration for assignment of dual-stack IP addresses dynamically

[role="_abstract"]
You can dynamically assign dual-stack IP addresses to a secondary network so that pods can communicate over both IPv4 and IPv6 addresses.

You can configure the following IP address assignment types in the `ipRanges` parameter:

* IPv4 addresses
* IPv6 addresses
* multiple IP address assignment

.Procedure

. Set `type` to `whereabouts`.

. Use `ipRanges` to allocate IP addresses as shown in the following example:
+
[source,yaml]
----
cniVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: whereabouts-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
       "name": "whereabouts-dual-stack",
       "cniVersion": "0.3.1,
       "type": "bridge",
       "ipam": {
         "type": "whereabouts",
         "ipRanges": [
                  {"range": "192.168.10.0/24"},
                  {"range": "2001:db8::/64"}
              ]
       }
      }

----

. Attach the secondary network to a pod. For more information, see "Adding a pod to a secondary network".

.Verification

* Verify that all IP addresses got assigned to the network interfaces within the network namespace of a pod by entering the following command:
+
[source,yaml]
----
$ oc exec -it <pod_name> -- ip a
----
+
where:
+
`<pod_name>`:: The name of the pod.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc
// * networking/multiple_networks/secondary_networks/configuring-ip-secondary-nwt.adoc

// Because the Cluster Network Operator abstracts the configuration for
// Macvlan, including IPAM configuration, this must be provided as YAML
// for the Macvlan CNI plugin only. In the future other Multus plugins
// might be managed the same way by the CNO.

[id="nw-multus-ipam-object_{context}"]
= Configuration of IP address assignment for a network attachment

[role="_abstract"]
For secondary networks, you can assign IP addresses by using an IP Address Management (IPAM) CNI plugin, which supports various assignment methods, including Dynamic Host Configuration Protocol (DHCP) and static assignment.

The DHCP IPAM CNI plugin responsible for dynamic assignment of IP addresses operates with two distinct components:

* CNI Plugin: Responsible for integrating with the Kubernetes networking stack to request and release IP addresses.
* DHCP IPAM CNI Daemon: A listener for DHCP events that coordinates with existing DHCP servers in the environment to handle IP address assignment requests. This daemon is not a DHCP server itself.

For networks requiring `type: dhcp` in their IPAM configuration, ensure the DHCP server meets the following conditions:

* A DHCP server is available and running in the environment.
* The DHCP server is external to the cluster and you expect the server to form part of the existing network infrastructure for the customer.
* The DHCP server is appropriately configured to serve IP addresses to the nodes.

In cases where a DHCP server is unavailable in the environment, consider using the Whereabouts IPAM CNI plugin. The Whereabouts CNI provides similar IP address management capabilities without the need for an external DHCP server.

[NOTE]
====
Use the Whereabouts CNI plugin when no external DHCP server exists or where static IP address management is preferred. The Whereabouts plugin includes a reconciler daemon to manage stale IP address allocations.
====

Ensure the periodic renewal of a DHCP lease throughout the lifetime of a container by including a separate daemon, the DHCP IPAM CNI Daemon. To deploy the DHCP IPAM CNI daemon, change the Cluster Network Operator (CNO) configuration to trigger the deployment of this daemon as part of the secondary network setup.

[id="nw-multus-static_{context}"]
== Static IP address assignment configuration

The following table describes the configuration for static IP address assignment:

.`ipam` static configuration object
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`type`
|`string`
|The IPAM address type. The value `static` is required.

|`addresses`
|`array`
|An array of objects specifying IP addresses to assign to the virtual interface. Both IPv4 and IPv6 IP addresses are supported.

|`routes`
|`array`
|An array of objects specifying routes to configure inside the pod.

|`dns`
|`array`
|Optional: An array of objects specifying the DNS configuration.

|====

The `addresses` array requires objects with the following fields:

.`ipam.addresses[]` array
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`address`
|`string`
|An IP address and network prefix that you specify. For example, if you specify `10.10.21.10/24`, the secondary network gets assigned an IP address of `10.10.21.10` and the subnet mask of `255.255.255.0`.

|`gateway`
|`string`
|The default gateway to route egress network traffic to.

|====

.`ipam.routes[]` array
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`dst`
|`string`
|The IP address range in CIDR format, such as `192.168.17.0/24` or `0.0.0.0/0` for the default route.

|`gw`
|`string`
|The gateway that routes network traffic.

|====

.`ipam.dns` object
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`nameservers`
|`array`
|An array of one or more IP addresses where DNS queries get sent.

|`domain`
|`array`
|The default domain to append to a hostname. For example, if the domain is set to `example.com`, a DNS lookup query for `example-host` is rewritten as `example-host.example.com`.

|`search`
|`array`
|An array of domain names to append to an unqualified hostname, such as `example-host`, during a DNS lookup query.

|====

.Static IP address assignment configuration example
[source,json]
----
{
  "ipam": {
    "type": "static",
      "addresses": [
        {
          "address": "191.168.1.7/24"
        }
      ]
  }
}
----

[id="nw-multus-dhcp_{context}"]
== Dynamic IP address (DHCP) assignment configuration

A pod obtains its original DHCP lease when the pod gets created. The lease must be periodically renewed by a minimal DHCP server deployment running on the cluster.

[IMPORTANT]
====
For an Ethernet network attachment, the SR-IOV Network Operator does not create a DHCP server deployment; the Cluster Network Operator is responsible for creating the minimal DHCP server deployment.
====

To trigger the deployment of the DHCP server, you must create a shim network attachment by editing the Cluster Network Operator configuration, as in the following example:

.Example shim network attachment definition
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: dhcp-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
        "name": "dhcp-shim",
        "cniVersion": "0.3.1",
        "type": "bridge",
        "ipam": {
          "type": "dhcp"
        }
      }
  # ...
----

where:

`type`:: Specifies dynamic IP address assignment for the cluster.

// Module included in the following assemblies:
//
// * networking/multiple_networks/secondary_networks/configuring-ip-secondary-nwt.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc

[id="nw-multus-whereabouts_{context}"]
= Dynamic IP address assignment configuration with Whereabouts

[role="_abstract"]
The Whereabouts CNI plugin helps the dynamic assignment of an IP address to a secondary network without the use of a DHCP server.

The Whereabouts CNI plugin also supports overlapping IP address ranges and configuration of the same CIDR range multiple times within separate `NetworkAttachmentDefinition` CRDs. This provides greater flexibility and management capabilities in multitenant environments.

[id="dynamic-ip-address-assignment-objects_{context}"]
== Dynamic IP address configuration parameters

The following table describes the configuration objects for dynamic IP address assignment with Whereabouts:

.`ipam` whereabouts configuration parameters
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`type`
|`string`
|The IPAM address type. The value `whereabouts` is required.

|`range`
|`string`
|An IP address and range in CIDR notation. IP addresses are assigned from within this range of addresses.

|`exclude`
|`array`
|Optional: A list of zero or more IP addresses and ranges in CIDR notation. IP addresses within an excluded address range are not assigned.

|`network_name`
|`string`
| Optional: Helps ensure that each group or domain of pods gets its own set of IP addresses, even if they share the same range of IP addresses. Setting this field is important for keeping networks separate and organized, notably in multitenant environments.

|====

[id="dynamic-ip-address-assignment-whereabouts_{context}"]
== Dynamic IP address assignment configuration with Whereabouts that excludes IP address ranges

The following example shows a dynamic address assignment configuration in a NAD file that uses Whereabouts:

.Whereabouts dynamic IP address assignment that excludes specific IP address ranges
[source,json]
----
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/27",
    "exclude": [
       "192.0.2.192/30",
       "192.0.2.196/32"
    ]
  }
}
----

[id="dynamic-ip-address-assignment-whereabouts-overlapping-ip-ranges_{context}"]
== Dynamic IP address assignment that uses Whereabouts with overlapping IP address ranges

The following example shows a dynamic IP address assignment that uses overlapping IP address ranges for multitenant networks.

.NetworkAttachmentDefinition 1
[source,json]
----
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/29",
    "network_name": "example_net_common",
  }
}
----

where:

`network_name`:: Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 2`.

.NetworkAttachmentDefinition 2
[source,json]
----
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/24",
    "network_name": "example_net_common",
  }
}
----

where:

`network_name`:: Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 1`.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-net-attach.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

// Note: IB does not support ipam with `type=dhcp`.

[id="nw-sriov-network-attachment_{context}"]
= Configuring SR-IOV additional network

[role="_abstract"]
You can configure an additional network that uses SR-IOV hardware by creating an `{rs}` object.
When you create an `{rs}` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.

[NOTE]
=====
Do not modify or delete an `{rs}` object if it is attached to any {object} in a `running` state.
=====

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a `{rs}` object, and then save the YAML in the `<name>.yaml` file, where `<name>` is a name for this additional network. The object specification might resemble the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: {rs}
metadata:
  name: attach1
  namespace: openshift-sriov-network-operator
spec:
  resourceName: net1
  networkNamespace: project2
  ipam: |-
    {
      "type": "host-local",
      "subnet": "10.56.217.0/24",
      "rangeStart": "10.56.217.171",
      "rangeEnd": "10.56.217.181",
      "gateway": "10.56.217.1"
    }
----

. To create the object, enter the following command:
+
[source,terminal]
----
$ oc create -f <name>.yaml
----
+
where:
+
`<name>`:: Specifies the name of the additional network.

. Optional: To confirm that the `NetworkAttachmentDefinition` object that is associated with the `{rs}` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the `networkNamespace` value you specified in the `{rs}` object.
+
[source,terminal]
----
$ oc get net-attach-def -n <namespace>
----

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc

[id="nw-sriov-runtime-config-sriov-ib_{context}"]
= Runtime configuration for an InfiniBand-based SR-IOV attachment

[role="_abstract"]
When attaching a pod to an additional network, you can specify a runtime configuration to make specific customizations for the pod. For example, you can request a specific MAC hardware address.

You specify the runtime configuration by setting an annotation in the pod specification. The annotation key is `k8s.v1.cni.cncf.io/networks`, and it accepts a JSON object that describes the runtime configuration.

The following JSON describes the runtime configuration options for an InfiniBand-based SR-IOV network attachment.

[source,json]
----
[
  {
    "name": "<network_attachment>",
    "infiniband-guid": "<guid>",
    "ips": ["<cidr_range>"]
  }
]
----

where:

`name`:: The name of the SR-IOV network attachment definition CR.
`infiniband-guid`:: The InfiniBand GUID for the SR-IOV device. To use this feature, you also must specify `{ "infinibandGUID": true }` in the `SriovIBNetwork` object.
`ips`:: The IP addresses for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovIBNetwork` object.

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "ib1",
          "infiniband-guid": "c2:11:22:33:44:55:66:77",
          "ips": ["192.168.10.1/24", "2001::1/64"]
        }
      ]
spec:
  containers:
  - name: sample-container
    image: <image>
    imagePullPolicy: IfNotPresent
    command: ["sleep", "infinity"]
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/attaching-pod.adoc
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc

[id="nw-multus-add-pod_{context}"]
= Adding a pod to a secondary network

[role="_abstract"]
To enable a pod to use additional network interfaces in OpenShift Container Platform, you can attach the pod to a secondary network. The pod continues to send normal cluster-related network traffic over the default network.

When a pod is created, a secondary network is attached to the pod. However, if a pod already exists, you cannot attach a secondary network to it.

The pod must be in the same namespace as the secondary network.

[NOTE]
=====
The SR-IOV Network Resource Injector adds the `resource` field to the first container in a pod automatically.

If you are using an Intel network interface controller (NIC) in Data Plane Development Kit (DPDK) mode, only the first container in your pod is configured to access the NIC. Your SR-IOV secondary network is configured for DPDK mode if the `deviceType` is set to `vfio-pci` in the `SriovNetworkNodePolicy` object.

You can work around this issue by either ensuring that the container that needs access to the NIC is the first container defined in the `Pod` object or by disabling the Network Resource Injector. For more information, see BZ#1990953.
=====

.Prerequisites

* Install the {oc-first}.
* Log in to the cluster.
* Install the SR-IOV Operator.
* Create either an `SriovNetwork` object or an `SriovIBNetwork` object to attach the pod to.

.Procedure

. Add an annotation to the `Pod` object. Only one of the following annotation formats can be used:
+
.. To attach a secondary network without any customization, add an annotation with the following format:
+
[source,yaml]
----
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
----
+
where:
+
`k8s.v1.cni.cncf.io/networks`:: Specifies the name of the secondary network to associate with the pod. To specify more than one secondary network, separate each network with a comma. Do not include whitespace between the comma. If you specify the same secondary network multiple times, that pod will have multiple network interfaces attached to that network.
+
.. To attach a secondary network with customizations, add an annotation with the following format:
+
[source,yaml]
----
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "<network>",
          "namespace": "<namespace>",
          "default-route": ["<default_route>"]
        }
      ]
----
+
where:
+
`<network>`:: Specifies the name of the secondary network defined by a `NetworkAttachmentDefinition` object.
`<namespace>`:: Specifies the namespace where the `NetworkAttachmentDefinition` object is defined.
`<default-route>`:: Optional parameter. Specifies an override for the default route, such as `192.168.17.1`.

. Create the pod by entering the following command.
+
[source,terminal]
----
$ oc create -f <name>.yaml
----
+
Replace `<name>` with the name of the pod.

. Optional: Confirm that the annotation exists in the `pod` CR by entering the following command. Replace `<name>` with the name of the pod.
+
[source,terminal]
----
$ oc get pod <name> -o yaml
----
+
In the following example, the `example-pod` pod is attached to the `net1` secondary network:
+
[source,terminal]
----
$ oc get pod example-pod -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: macvlan-bridge
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.128.2.14"
          ],
          "default": true,
          "dns": {}
      },{
          "name": "macvlan-bridge",
          "interface": "net1",
          "ips": [
              "20.2.2.100"
          ],
          "mac": "22:2f:60:a5:f8:00",
          "dns": {}
      }]
  name: example-pod
  namespace: default
spec:
  ...
status:
  ...
----
+
where:
+
`k8s.v1.cni.cncf.io/network-status`:: Specifies a JSON array of objects. Each object describes the status of a secondary network attached to the pod. The annotation value is stored as a plain text value.

// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-ib-attach.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc

[id="nw-sriov-expose-mtu_{context}"]
= Exposing MTU for vfio-pci SR-IOV devices to pod

[role="_abstract"]
After adding a pod to an additional network, you can check that the MTU is available for the SR-IOV network.

.Procedure

. Check that the pod annotation includes MTU by running the following command:
+
[source,terminal]
----
$ oc describe pod example-pod
----
+
The following example shows the sample output:
+
[source,text]
----
"mac": "20:04:0f:f1:88:01",
       "mtu": 1500,
       "dns": {},
       "device-info": {
         "type": "pci",
         "version": "1.1.0",
         "pci": {
           "pci-address": "0000:86:01.3"
    }
  }
----

. Verify that the MTU is available in `/etc/podnetinfo/` inside the pod by running the following command:
+
[source,terminal]
----
$ oc exec example-pod -n sriov-tests -- cat /etc/podnetinfo/annotations | grep mtu
----
+
The following example shows the sample output:
+
[source,text]
----
k8s.v1.cni.cncf.io/network-status="[{
    \"name\": \"ovn-kubernetes\",
    \"interface\": \"eth0\",
    \"ips\": [
        \"10.131.0.67\"
    ],
    \"mac\": \"0a:58:0a:83:00:43\",
    \"default\": true,
    \"dns\": {}
    },{
    \"name\": \"sriov-tests/sriov-nic-1\",
    \"interface\": \"net1\",
    \"ips\": [
        \"192.168.10.1\"
    ],
    \"mac\": \"20:04:0f:f1:88:01\",
    \"mtu\": 1500,
    \"dns\": {},
    \"device-info\": {
        \"type\": \"pci\",
        \"version\": \"1.1.0\",
        \"pci\": {
            \"pci-address\": \"0000:86:01.3\"
        }
    }
    }]"
----

[role="_additional-resources"]
[id="configuring-sriov-ib-attach-additional-resources"]
== Additional resources

* Configuring an SR-IOV network device
* Using CPU Manager
* Exclude SR-IOV network topology for NUMA-aware scheduling
