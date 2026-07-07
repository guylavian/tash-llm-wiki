---
title: "Configuring ingress cluster traffic overview"
type: reference
domain: openshift
slug: networking-4-22-overview-traffic
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/overview-traffic
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring ingress cluster traffic overview

[id="overview-traffic"]
= Configuring ingress cluster traffic overview

[role="_abstract"]
To enable communication between external networks and services in OpenShift Container Platform, configure ingress cluster traffic.

// Module included in the following assemblies:
//
// *networking/ingress_load_balancing/configuring_ingress_cluster_traffic/overview-traffic.adoc

[id="nw-ingresscontroller-communication-service-methods_{context}"]
= Methods for communicating from outside the cluster

[role="_abstract"]
To enable communication between external networks and services in OpenShift Container Platform, configure the appropriate ingress method.

OpenShift Container Platform provides the following methods for communicating from outside the cluster with services running in the cluster. Note that the methods are listed in order of preference.

* If you have HTTP/HTTPS, use an Ingress Controller.
* If you have a TLS-encrypted protocol other than HTTPS. For example, for TLS
with the SNI header, use an Ingress Controller.
* Otherwise, use a Load Balancer, an External IP, or a `NodePort`.

[options="header"]
|===
|Method |Purpose

|Use an Ingress Controller
|Allows access to HTTP/HTTPS traffic and TLS-encrypted protocols other than HTTPS (for example, TLS with the SNI header).

|Automatically assign an external IP using a load balancer service
|Allows traffic to non-standard ports through an IP address assigned from a pool.
Most cloud platforms offer a method to start a service with a load-balancer IP address.

|About MetalLB and the MetalLB Operator
|Allows traffic to a specific IP address or address from a pool on the machine network.
For bare-metal installations or platforms that are like bare metal, MetalLB provides a way to start a service with a load-balancer IP address.

|Manually assign an external IP to a service
|Allows traffic to non-standard ports through a specific IP address.

|Configure a `NodePort`
|Expose a service on all nodes in the cluster.
|===

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Use an Ingress Controller

* Automatically assign an external IP using a load balancer service

* About MetalLB and the MetalLB Operator

* Manually assign an external IP to a service

* Configure a `NodePort`

// Module included in the following assemblies:
//
// *networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-nodeport.adoc

[id="overview-traffic-comparision_{context}"]
= Comparison: Fault-tolerant access to external IP addresses

[role="_abstract"]
To ensure continuous service availability and maintain external IP access in OpenShift Container Platform, configure fault-tolerant networking features.

For the communication methods that provide access to an external IP address, fault tolerant access to the IP address is another consideration. The following features provide fault tolerant access to an external IP address.

IP failover::
IP failover manages a pool of virtual IP addresses for a set of nodes. IP failover gets implemented with Keepalived and Virtual Router Redundancy Protocol (VRRP). IP failover is a layer 2 mechanism only and relies on multicast. Multicast can have disadvantages for some networks.

MetalLB::
MetalLB has a layer 2 mode, but it does not use multicast. Layer 2 mode has a disadvantage that it transfers all traffic for an external IP address through one node.

Manually assigning external IP addresses::
You can configure your cluster with an IP address block that is used to assign external IP addresses to services. By default, this feature is disabled. This feature is flexible, but places the largest burden on the cluster or network administrator. The cluster is prepared to receive traffic that is destined for the external IP, but you must decide how to route traffic to nodes.
