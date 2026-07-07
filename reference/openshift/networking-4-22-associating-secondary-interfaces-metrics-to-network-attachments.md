---
title: "Associating secondary interfaces metrics to network attachments"
type: reference
domain: openshift
slug: networking-4-22-associating-secondary-interfaces-metrics-to-network-attachments
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/associating-secondary-interfaces-metrics-to-network-attachments
version: 4.22
family: networking
documentKind: "Documentation"
---

# Associating secondary interfaces metrics to network attachments

[id="associating-secondary-interfaces-metrics-to-network-attachments"]
= Associating secondary interfaces metrics to network attachments

[role="_abstract"]
To gain better visibility into cluster traffic, you can associate secondary interface metrics with specific network attachments. By using the `pod_network_info` metric to label interfaces based on their `NetworkAttachmentDefinition` resource, you can more easily monitor performance and troubleshoot connectivity issues across your network.

// Module included in the following assemblies:
//
// *networking/associating-secondary-interfaces-metrics-to-network-attachments.adoc

[id="cnf-associating-secondary-interfaces-metrics-to-network-attachments_{context}"]
= Extending secondary network metrics for monitoring

[role="_abstract"]
To monitor and manage network traffic effectively, you can extend secondary network metrics with identifying information. By using the `pod_network_name_info` metric to label interfaces based on their `NetworkAttachmentDefinition` resource, you can classify interface types to enable precise metric aggregation and alerting.

Secondary devices, or interfaces, are used for different purposes. Metrics from secondary network interfaces need to be classified to allow for effective aggregation and monitoring.

Exposed metrics contain the interface but do not specify where the interface originates. This is workable when there are no additional interfaces. However, relying on interface names alone becomes problematic when secondary interfaces are added because it is difficult to identify their purpose and use their metrics effectively..

When adding secondary interfaces, their names depend on the order in which they are added. Secondary interfaces can belong to distinct networks that can each serve a different purposes.

With `pod_network_name_info` it is possible to extend the current metrics with additional information that identifies the interface type. In this way, it is possible to aggregate the metrics and to add specific alarms to specific interface types.

The network type is generated from the name of the `NetworkAttachmentDefinition` resource, which distinguishes different secondary network classes. For example, different interfaces belonging to different networks or using different CNIs use different network attachment definition names.

// Module included in the following assemblies:
//
// *networking/associating-secondary-interfaces-metrics-to-network-attachments.adoc

[id="cnf-network-metrics-daemon_{context}"]
= Network Metrics Daemon

[role="_abstract"]
The Network Metrics Daemon collects and publishes network-related metrics to support performance management in complex pod environments. This component provides metadata for secondary interfaces, which is required for accurate traffic monitoring across distinct network attachments.

The kubelet is already publishing network related metrics you can observe. These metrics are:

* `container_network_receive_bytes_total`
* `container_network_receive_errors_total`
* `container_network_receive_packets_total`
* `container_network_receive_packets_dropped_total`
* `container_network_transmit_bytes_total`
* `container_network_transmit_errors_total`
* `container_network_transmit_packets_total`
* `container_network_transmit_packets_dropped_total`

The labels in these metrics contain, among others:

* Pod name
* Pod namespace
* Interface name (such as `eth0`)

These metrics work well until new interfaces are added to the pod, for example via https://github.com/intel/multus-cni[Multus], as it is not clear what the interface names refer to.

The interface label refers to the interface name, but it is not clear what that interface is meant for. In case of many different interfaces, it would be impossible to understand what network the metrics you are monitoring refer to.

This is addressed by introducing the new `pod_network_name_info` described in the following section.

// Module included in the following assemblies:
//
// *networking/associating-secondary-interfaces-metrics-to-network-attachments.adoc

[id="cnf-metrics-secondary-interfaces-by-name_{context}"]
= Metrics with network name

[role="_abstract"]
To simplify the monitoring of secondary networks, you can use the `pod_network_name_info` metric to correlate network performance data with specific network names. By joining this metric with container network metrics, you can identify traffic patterns and errors across distinct network attachment definitions.

.Example of `pod_network_name_info`
[source,bash]
----
pod_network_name_info{interface="net0",namespace="namespacename",network_name="nadnamespace/firstNAD",pod="podname"} 0
----

The network name label is produced using the annotation added by Multus. It is the concatenation of the namespace the network attachment definition belongs to, plus the name of the network attachment definition. The Network Metrics daemonset publishes a `pod_network_name_info` gauge metric, with a fixed value of `0`.

The new metric alone does not provide much value, but combined with the network related `container_network_*` metrics, it offers better support for monitoring secondary networks.

Using a `promql` query like the following ones, it is possible to get a new metric containing the value and the network name retrieved from the `k8s.v1.cni.cncf.io/network-status` annotation:

[source,bash]
----
(container_network_receive_bytes_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_receive_errors_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_receive_packets_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_receive_packets_dropped_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_transmit_bytes_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_transmit_errors_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_transmit_packets_total) + on(namespace,pod,interface) group_left(network_name) ( pod_network_name_info )
(container_network_transmit_packets_dropped_total) + on(namespace,pod,interface) group_left(network_name)
----
