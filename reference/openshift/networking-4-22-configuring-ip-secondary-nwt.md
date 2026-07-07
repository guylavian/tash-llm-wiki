---
title: "Configuring IP address assignment on secondary networks"
type: reference
domain: openshift
slug: networking-4-22-configuring-ip-secondary-nwt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ip-secondary-nwt
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring IP address assignment on secondary networks

[id="configuring-ip-secondary-nwt"]
= Configuring IP address assignment on secondary networks

[role="_abstract"]
You can configure IP address assignments for secondary networks so that pods can connect to the secondary networks.

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
// * networking/multiple_networks/secondary_networks/configuring-ip-secondary-nwt.adoc

[id="nw-multus-creating-whereabouts-reconciler-daemon-set_{context}"]
= Creating a whereabouts-reconciler daemon set

[role="_abstract"]
The Whereabouts reconciler is responsible for managing dynamic IP address assignments for the pods within a cluster by using the Whereabouts IP Address Management (IPAM) solution. The Whereabouts reconciler ensures that each pod gets a unique IP address from the specified IP address range. The Whereabouts reconciler also handles IP address releases when pods are deleted or scaled down.

[NOTE]
====
You can also use a `NetworkAttachmentDefinition` custom resource definition (CRD) for dynamic IP address assignment.
====

The `whereabouts-reconciler` daemon set is automatically created when you configure a secondary network through the Cluster Network Operator. The `whereabouts-reconciler` DaemonSet does not get automatically created when you configure a secondary network from a YAML manifest.

To trigger the deployment of the `whereabouts-reconciler` daemon set, you must manually create a `whereabouts-shim` network attachment by editing the Cluster Network Operator custom resource (CR) file.

.Procedure

. Edit the `Network.operator.openshift.io` CR by running the following command:
+
[source,terminal]
----
$ oc edit network.operator.openshift.io cluster
----

. Include the `additionalNetworks` section shown in this example YAML extract within the `spec` definition of the CR:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
# ...
spec:
  additionalNetworks:
  - name: whereabouts-shim
    namespace: default
    rawCNIConfig: |-
      {
       "name": "whereabouts-shim",
       "cniVersion": "0.3.1",
       "type": "bridge",
       "ipam": {
         "type": "whereabouts"
       }
      }
    type: Raw
# ...
----

. Save the file and exit the text editor.

. Verify that the `whereabouts-reconciler` daemon set deployed successfully by running the following command:
+
[source,terminal]
----
$ oc get all -n openshift-multus | grep whereabouts-reconciler
----
+
[source,terminal]
----
pod/whereabouts-reconciler-jnp6g 1/1 Running 0 6s
pod/whereabouts-reconciler-k76gg 1/1 Running 0 6s
daemonset.apps/whereabouts-reconciler 6 6 6 6 6 kubernetes.io/os=linux 6s
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/secondary_networks/configuring-ip-secondary-nwt.adoc

[id="nw-multus-configuring-whereabouts-ip-reconciler-schedule_{context}"]
= Configuring the Whereabouts IP reconciler schedule

[role="_abstract"]
The Whereabouts IPAM CNI plugin runs the IP address reconciler daily. This process cleans up any stranded IP address allocations that might result in exhausting IP addresses and therefore prevent new pods from getting a stranded IP address allocated to them.

Use this procedure to change the frequency at which the IP reconciler runs.

.Prerequisites

* You installed the {oc-first}.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have deployed the `whereabouts-reconciler` daemon set, and the `whereabouts-reconciler` pods are up and running.

.Procedure

. Run the following command to create a `ConfigMap` object named `whereabouts-config` in the `openshift-multus` namespace with a specific cron expression for the IP reconciler:
+
[source,terminal]
----
$ oc create configmap whereabouts-config -n openshift-multus --from-literal=reconciler_cron_expression="*/15 * * * *"
----
+
This cron expression indicates the IP reconciler runs every 15 minutes. Adjust the expression based on your specific requirements.
+
[NOTE]
====
The `whereabouts-reconciler` daemon set can only consume a cron expression pattern that includes five asterisks. Red{nbsp} Hat does not support the sixth asterisk, which is used to denote seconds.
====

. Retrieve information about resources related to the `whereabouts-reconciler` daemon set and pods within the `openshift-multus` namespace by running the following command:
+
[source,terminal]
----
$ oc get all -n openshift-multus | grep whereabouts-reconciler
----
+
[source,terminal]
----
pod/whereabouts-reconciler-2p7hw                   1/1     Running   0             4m14s
pod/whereabouts-reconciler-76jk7                   1/1     Running   0             4m14s
daemonset.apps/whereabouts-reconciler          6         6         6       6            6           kubernetes.io/os=linux   4m16s
----

. Run the following command to verify that the `whereabouts-reconciler` pod runs the IP reconciler with the configured interval:
+
[source,terminal]
----
$ oc -n openshift-multus logs whereabouts-reconciler-2p7hw
----
+
[source,terminal]
----
2024-02-02T16:33:54Z [debug] event not relevant: "/cron-schedule/..2024_02_02_16_33_54.1375928161": CREATE
2024-02-02T16:33:54Z [debug] event not relevant: "/cron-schedule/..2024_02_02_16_33_54.1375928161": CHMOD
2024-02-02T16:33:54Z [debug] event not relevant: "/cron-schedule/..data_tmp": RENAME
2024-02-02T16:33:54Z [verbose] using expression: */15 * * * *
2024-02-02T16:33:54Z [verbose] configuration updated to file "/cron-schedule/..data". New cron expression: */15 * * * *
2024-02-02T16:33:54Z [verbose] successfully updated CRON configuration id "00c2d1c9-631d-403f-bb86-73ad104a6817" - new cron expression: */15 * * * *
2024-02-02T16:33:54Z [debug] event not relevant: "/cron-schedule/config": CREATE
2024-02-02T16:33:54Z [debug] event not relevant: "/cron-schedule/..2024_02_02_16_26_17.3874177937": REMOVE
2024-02-02T16:45:00Z [verbose] starting reconciler run
2024-02-02T16:45:00Z [debug] NewReconcileLooper - inferred connection data
2024-02-02T16:45:00Z [debug] listing IP pools
2024-02-02T16:45:00Z [debug] no IP addresses to cleanup
2024-02-02T16:45:00Z [verbose] reconciler success
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-additional-network.adoc
// * networking/hardware_networks/configuring-sriov-net-attach.adoc
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc

[id="nw-multus-whereabouts-fast-ipam_{context}"]
= Fast IPAM configuration for the Whereabouts IPAM CNI plugin

[role="_abstract"]
Wherabouts is an IP Address Management (IPAM) Container Network Interface (CNI) plugin that assigns IP addresses at a cluster-wide level. Whereabouts does not require a Dynamic Host Configuration Protocol (DHCP) server.

A typical Wherabouts workflow is described as follows:

. Whereabouts takes an address range in classless inter-domain routing (CIDR) notation, such as `192.168.2.0/24`, and assigns IP addresses within that range, such as `192.168.2.1` to `192.168.2.254`.
. Whereabouts assigns an IP address, the lowest value address in a CIDR range, to a pod and tracks the IP address in a data store for the lifetime of that pod.
. When the pod is removed, Whereabouts frees the address from the pod so that the address is available for assignment.

To improve the performance of Whereabouts, especially if nodes in your cluster run a high amount of pods, you can enable the Fast IPAM feature.

The Fast IPAM feature uses `nodeslicepools`, which are managed by the Whereabouts Controller, to optimize IP allocation for nodes.

.Prerequisites

* You added the `whereabouts-shim` configuration to the `Network.operator.openshift.io` custom resource (CR), so that the Cluster Network Operator (CNO) can deploy the Whereabouts Controller. See "Creating a Whereabouts reconciler daemon set".
* For the Fast IPAM feature to work, ensure that the `NetworkAttachmentDefinition` (NAD) and the pod exist in the same `openshift-multus` namespace.

.Procedure

. Confirm that the Whereabouts Controller is running by entering the following command.
+
[source,terminal]
----
$ oc get pods -n openshift-multus | grep whereabouts-controller
----
+
[source,terminal]
----
whereabouts-controller-5cbfd6c475-fr7d7        1/1     Running            0               22s
...
----
+
[IMPORTANT]
====
If the Whereabouts Controller is not running, the Fast IPAM does not work.
====

. Create a NAD file for your cluster and add the Fast IPAM details to the file as demonstrated in the following example configuration:
+
[source,yaml,subs="attributes+,quotes"]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: wb-ipam
  namespace: openshift-multus
spec:
  config: '{
    "cniVersion": "0.3.0",
    "name": "wb-ipam-cni-name",
    "type": "bridge",
    "bridge": "cni0",
    "ipam": {
      "type": "whereabouts",
      "range": "10.5.0.0/20",
      "node_slice_size": "/24"
    }
  }'
# ...
----
+
where:
+
`namespace`:: The namespace where CNO deploys the NAD.
`name`:: The name of the Whereabouts IPAM CNI plugin.
`type`:: The type of IPAM CNI plugin, such as `whereabouts`.
`range`:: The IP address range for the IP pool that the Whereabouts IPAM CNI plugin uses for allocating IP addresses to pods.
`node_slice_size`:: Sets the slice size of IP addresses available to each node.

. Add the Whereabouts IPAM CNI plugin annotation details to the YAML file for the pod:
+
[source,yaml,subs="attributes+,quotes"]
----
apiVersion: v1
kind: Pod
metadata:
  name: samplepod
  annotations:
  k8s.v1.cni.cncf.io/networks: openshift-multus/wb-ipam
spec:
  containers:
  - name: samplecontainer
  command: ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
  image: registry.redhat.io/ubi9/ubi-minimal
# ...
----
+
where:
+
`name`:: The name of the pod.
`k8s.v1.cni.cncf.io/networks`:: The annotation details that references the Whereabouts IPAM CNI plugin name that exists in the `openshift-multus` namespace.
`- name`:: The name of the container for the pod.
`command`:: Defines the entry point for the container and controls the behavior of the container in the Whereabouts IPAM CNI plugin.

. Apply the NAD file configuration to pods that exist on nodes that run in your cluster:
+
[source,terminal]
----
$ oc create -f <NAD_file_name>.yaml
----

.Verification

. Show the IP address details of the pod by entering the following command:
+
[source,terminal,subs="attributes+,quotes"]
----
$ oc describe pod <pod_name>
----
+
[source,terminal]
----
...
k8s.v1.cni.cncf.io/network-status:
  [{
      "name": "ovn-kubernetes",
      "interface": "eth0",
      "ips": [
          "10.128.3.174"
      ],
      "mac": "0a:58:0a:80:03:ae",
      "default": true,
      "dns": {}
  },{
      "name": "openshift-multus/wb-ipam",
      "interface": "net1",
      "ips": [
          "10.5.0.1"
      ],
      "mac": "1a:04:6f:a4:15:3c",
      "dns": {}
  }]
k8s.v1.cni.cncf.io/networks: openshift-multus/wb-ipam
...
----

. Access the pod and confirm its interfaces by entering the following command:
+
[source,terminal]
----
$ oc exec <pod_name> -- ip a
----
+
[source,terminal]
----
...
3: net1@if439: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 1a:04:6f:a4:15:3c brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.5.0.1/20 brd 10.5.15.255 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::1804:6fff:fea4:153c/64 scope link
       valid_lft forever preferred_lft forever
...
----
+
where:
+
`inet`: Pod is attached to the `10.5.0.1` IP address on the `net1` interface as expected.

. Check that the node selector pool exists in the `openshift-multus` namespace by entering the following command. The expected output shows the name of the node selector pool, such as `nodeslicepool, and the creation age in minutes, such as `32m`.
+
[source,terminal]
----
$ oc get nodeslicepool -n openshift-multus
----
+
.Example output
[source,terminal]
----
NAME               AGE
wb-ipam-cni-name   32m
----

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
