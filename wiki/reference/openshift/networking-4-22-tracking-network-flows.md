---
title: "Tracking network flows"
type: reference
domain: openshift
slug: networking-4-22-tracking-network-flows
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/tracking-network-flows
version: 4.22
family: networking
documentKind: "Documentation"
---

# Tracking network flows

[id="tracking-network-flows"]
= Tracking network flows

As a cluster administrator, you can collect information about pod network flows from your cluster to assist with the following areas:

* Monitor ingress and egress traffic on the pod network.

* Troubleshoot performance issues.

* Gather data for capacity planning and security audits.

When you enable the collection of the network flows, only the metadata about the traffic is collected.
For example, packet data is not collected, but the protocol, source address, destination address, port numbers, number of bytes, and other packet-level information is collected.

The data is collected in one or more of the following record formats:

* NetFlow

* sFlow

* IPFIX

When you configure the Cluster Network Operator (CNO) with one or more collector IP addresses and port numbers, the Operator configures Open vSwitch (OVS) on each node to send the network flows records to each collector.

You can configure the Operator to send records to more than one type of network flow collector. For example, you can send records to NetFlow collectors and also send records to sFlow collectors.

When OVS sends data to the collectors, each type of collector receives identical records. For example, if you configure two NetFlow collectors, OVS on a node sends identical records to the two collectors. If you also configure two sFlow collectors, the two sFlow collectors receive identical records. However, each collector type has a unique record format.

Collecting the network flows data and sending the records to collectors affects performance. Nodes process packets at a slower rate. If the performance impact is too great, you can delete the destinations for collectors to disable collecting network flows data and restore performance.

[NOTE]
====
Enabling network flow collectors might have an impact on the overall performance of the cluster network.
====

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

[id="nw-network-flows-object_{context}"]
= Network object configuration for tracking network flows

The fields for configuring network flows collectors in the Cluster Network Operator (CNO) are shown in the following table:

.Network flows configuration
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CNO object. This name is always `cluster`.

|`spec.exportNetworkFlows`
|`object`
|One or more of `netFlow`, `sFlow`, or `ipfix`.

|`spec.exportNetworkFlows.netFlow.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.

|`spec.exportNetworkFlows.sFlow.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.

|`spec.exportNetworkFlows.ipfix.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.
|====

After applying the following manifest to the CNO, the Operator configures Open vSwitch (OVS) on each node in the cluster to send network flows records to the NetFlow collector that is listening at `192.168.1.99:2056`.

.Example configuration for tracking network flows
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  exportNetworkFlows:
    netFlow:
      collectors:
        - 192.168.1.99:2056
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

[id="nw-network-flows-create_{context}"]
= Adding destinations for network flows collectors

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to send network flows metadata about the pod network to a network flows collector.

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* You have a network flows collector and know the IP address and port that it listens on.

.Procedure

. Create a patch file that specifies the network flows collector type and the IP address and port information of the collectors:
+
[source,terminal]
----
spec:
  exportNetworkFlows:
    netFlow:
      collectors:
        - 192.168.1.99:2056
----

. Configure the CNO with the network flows collectors:
+
[source,terminal]
----
$ oc patch network.operator cluster --type merge -p "$(cat <file_name>.yaml)"
----
+
.Example output
[source,terminal]
----
network.operator.openshift.io/cluster patched
----

.Verification

Verification is not typically necessary. You can run the following command to confirm that Open vSwitch (OVS) on each node is configured to send network flows records to one or more collectors.

. View the Operator configuration to confirm that the `exportNetworkFlows` field is configured:
+
[source,terminal]
----
$ oc get network.operator cluster -o jsonpath="{.spec.exportNetworkFlows}"
----
+
.Example output
[source,terminal]
----
{"netFlow":{"collectors":["192.168.1.99:2056"]}}
----

. View the network flows configuration in OVS from each node:
+
[source,terminal]
----
$ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node -o jsonpath='{range@.items[*]}{.metadata.name}{"\n"}{end}');
  do ;
    echo;
    echo $pod;
    oc -n openshift-ovn-kubernetes exec -c ovnkube-controller $pod \
      -- bash -c 'for type in ipfix sflow netflow ; do ovs-vsctl find $type ; done';
done
----
+
.Example output
[source,terminal]
----
ovnkube-node-xrn4p
_uuid               : a4d2aaca-5023-4f3d-9400-7275f92611f9
active_timeout      : 60
add_id_to_interface : false
engine_id           : []
engine_type         : []
external_ids        : {}
targets             : ["192.168.1.99:2056"]

ovnkube-node-z4vq9
_uuid               : 61d02fdb-9228-4993-8ff5-b27f01a29bd6
active_timeout      : 60
add_id_to_interface : false
engine_id           : []
engine_type         : []
external_ids        : {}
targets             : ["192.168.1.99:2056"]-

...
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

[id="nw-network-flows-delete_{context}"]
= Deleting all destinations for network flows collectors

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to stop sending network flows metadata to a network flows collector.

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.

.Procedure

. Remove all network flows collectors:
+
[source,terminal]
----
$ oc patch network.operator cluster --type='json' \
    -p='[{"op":"remove", "path":"/spec/exportNetworkFlows"}]'
----
+
.Example output
[source,terminal]
----
network.operator.openshift.io/cluster patched
----

[role="_additional-resources"]
[id="additional-resources_tracking-network-flows"]
== Additional resources

* Network [operator.openshift.io/v1\]
