---
title: "Configuring MetalLB BGP peers"
type: reference
domain: openshift
slug: networking-4-22-metallb-configure-bgp-peers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/metallb-configure-bgp-peers
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring MetalLB BGP peers

[id="metallb-configure-bgp-peers"]
= Configuring MetalLB BGP peers

[role="_abstract"]
As a cluster administrator, you can add, modify, and delete Border Gateway Protocol (BGP) peers. The MetalLB Operator uses the BGP peer custom resources to identify which peers that MetalLB `speaker` pods contact to start BGP sessions.

The peers receive the route advertisements for the load-balancer IP addresses that MetalLB assigns to services.

// BGP peer custom resource
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-bgp-peers.adoc

[id="nw-metallb-bgppeer-cr_{context}"]
= About the BGP peer custom resource

[role="_abstract"]
To establish network connectivity and advertise routes for load-balancer services, configure the properties of the MetalLB Border Gateway Protocol (BGP) peer custom resource (CR). Establishing these parameters ensures that your cluster authorizes specific routing peers to direct external traffic correctly to your application workloads.

The following table describes the parameters for the BGP peer CR:

.MetalLB BGP peer custom resource
[cols="1,1,3",options="header"]
|===

|Parameter
|Type
|Description

|`metadata.name`
|`string`
|Specifies the name for the BGP peer CR.

|`metadata.namespace`
|`string`
|Specifies the namespace for the BGP peer CR.

|`spec.myASN`
|`integer`
|Specifies the Autonomous System Number (ASN) for the local end of the BGP session. In all BGP peer CRs that you add, specify the same value. The range is `0` to `4294967295`.

|`spec.peerASN`
|`integer`
|Specifies the ASN for the remote end of the BGP session. The range is `0` to `4294967295`. If you use this parameter, you cannot specify a value in the `spec.dynamicASN` parameter.

|`spec.dynamicASN`
|`string`
| Detects the ASN to use for the remote end of the session without explicitly setting it. Specify `internal` for a peer with the same ASN, or `external` for a peer with a different ASN. If you use this parameter, you cannot specify a value in the `spec.peerASN` parameter.

|`spec.peerAddress`
|`string`
|Specifies the IP address of the peer to contact for establishing the BGP session. If you use this parameter, you cannot specify a value in the `spec.interface` parameter.

|`spec.interface`
|`string`
|Specifies the interface name to use when establishing a session. Use this parameter to configure unnumbered BGP peering.
You must establish a point-to-point, layer 2 connection between the two BGP peers. You can use unnumbered BGP peering with IPv4, IPv6, or dual-stack, but you must enable IPv6 RAs (Router Advertisements). Each interface is limited to one BGP connection.
If you use this parameter, you cannot specify a value in the `spec.peerAddress` parameter.

|`spec.sourceAddress`
|`string`
|Optional: Specifies the IP address to use when establishing the BGP session. The value must be an IPv4 address.

|`spec.peerPort`
|`integer`
|Optional: Specifies the network port of the peer to contact for establishing the BGP session. The range is `0` to `16384`.

|`spec.holdTime`
|`string`
|Optional: Specifies the duration for the hold time to propose to the BGP peer. The minimum value is 3 seconds (`3s`).
The common units are seconds and minutes, such as `3s`, `1m`, and `5m30s`. To detect path failures more quickly, also configure BFD.

|`spec.keepaliveTime`
|`string`
|Optional: Specifies the maximum interval between sending keep-alive messages to the BGP peer. If you specify this parameter, you must also specify a value for the `holdTime` parameter. The specified value must be less than the value for the `holdTime` parameter.

|`spec.routerID`
|`string`
|Optional: Specifies the router ID to advertise to the BGP peer. If you specify this parameter, you must specify the same value in every BGP peer custom resource that you add.

|`spec.password`
|`string`
|Optional: Specifies the MD5 password to send to the peer for routers that enforce TCP MD5 authenticated BGP sessions.

|`spec.passwordSecret`
|`string`
|Optional: Specifies name of the authentication secret for the BGP peer. The secret must live in the `metallb` namespace and be of type basic-auth.

|`spec.bfdProfile`
|`string`
|Optional: Specifies the name of a BFD profile.

|`spec.nodeSelectors`
|`object[]`
|Optional: Specifies a selector, using match expressions and match labels, to control which nodes can connect to the BGP peer.

|`spec.ebgpMultiHop`
|`boolean`
|Optional: Specifies that the BGP peer is multiple network hops away. If the BGP peer is not directly connected to the same network, the speaker cannot establish a BGP session unless this parameter is set to `true`. This parameter applies to _external BGP_.External BGP is the term that is used to describe when a BGP peer belongs to a different Autonomous System.

|`connectTime`
|`duration`
|Specifies how long BGP waits between connection attempts to a neighbor.

|===

[NOTE]
====
The `passwordSecret` parameter is mutually exclusive with the `password` parameter, and contains a reference to a secret containing the password to use. Setting both parameters results in a failure of the parsing.
====

// Add a BGP peer
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-bgp-peers.adoc

[id="nw-metallb-configure-bgppeer_{context}"]
= Configuring a BGP peer

[role="_abstract"]
To exchange routing information and advertise IP addresses for load balancer services, configure MetalLB BGP peer CRs. Establishing these peers ensures that your network infrastructure can reach and correctly route traffic to cluster application workloads.

You can add a BGP peer custom resource to exchange routing information with network routers and advertise the IP addresses for services.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.
* Configure MetalLB with a BGP advertisement.

.Procedure

. Create a file, such as `bgppeer.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: doc-example-peer
spec:
  peerAddress: 10.0.0.1
  peerASN: 64501
  myASN: 64500
  routerID: 10.10.10.10
# ...
----

. Apply the BGP peer configuration by entering the following command:
+
[source,terminal]
----
$ oc apply -f bgppeer.yaml
----

// Add a BGP peer
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-bgp-peers.adoc

[id="nw-metallb-example-assign-specific-address-pools-specific-bgp-peers_{context}"]
= Configure a specific set of BGP peers for a given address pool

[role="_abstract"]
To assign specific IP address pools to designated BGP peers, configure MetalLB BGP advertisements. Establishing these mappings ensures that your cluster advertises designated network ranges only to authorized routing peers for precise external traffic control.

This procedure demonstrates the following tasks:

* Configure a set of address pools: `pool1` and `pool2`.
* Configure a set of BGP peers: `peer1` and `peer2`.
* Configure BGP advertisement to assign `pool1` to `peer1` and `pool2` to `peer2`.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create address pool `pool1`.
+
.. Create a file, such as `ipaddresspool1.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: pool1
spec:
  addresses:
    - 4.4.4.100-4.4.4.200
    - 2001:100:4::200-2001:100:4::400
# ...
----
+
.. Apply the configuration for the IP address pool `pool1`:
+
[source,terminal]
----
$ oc apply -f ipaddresspool1.yaml
----

. Create address pool `pool2`.
+
.. Create a file, such as `ipaddresspool2.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: pool2
spec:
  addresses:
    - 5.5.5.100-5.5.5.200
    - 2001:100:5::200-2001:100:5::400
# ...
----
+
.. Apply the configuration for the IP address pool `pool2`:
+
[source,terminal]
----
$ oc apply -f ipaddresspool2.yaml
----

. Create BGP `peer1`.
+
.. Create a file, such as `bgppeer1.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: peer1
spec:
  peerAddress: 10.0.0.1
  peerASN: 64501
  myASN: 64500
  routerID: 10.10.10.10
# ...
----
+
.. Apply the configuration for the BGP `peer1`:
+
[source,terminal]
----
$ oc apply -f bgppeer1.yaml
----

. Create BGP `peer2`.
+
.. Create a file, such as `bgppeer2.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: peer2
spec:
  peerAddress: 10.0.0.2
  peerASN: 64501
  myASN: 64500
  routerID: 10.10.10.10
# ...
----
+
.. Apply the configuration for the BGP `peer2`:
+
[source,terminal]
----
$ oc apply -f bgppeer2.yaml
----

. Create BGP advertisement 1.
+
.. Create a file, such as `bgpadvertisement1.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgpadvertisement-1
  namespace: metallb-system
spec:
  ipAddressPools:
    - pool1
  peers:
    - peer1
  communities:
    - 65535:65282
  aggregationLength: 32
  aggregationLengthV6: 128
  localPref: 100
# ...
----
+
.. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f bgpadvertisement1.yaml
----

. Create BGP advertisement 2.
+
.. Create a file, such as `bgpadvertisement2.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgpadvertisement-2
  namespace: metallb-system
spec:
  ipAddressPools:
    - pool2
  peers:
    - peer2
  communities:
    - 65535:65282
  aggregationLength: 32
  aggregationLengthV6: 128
  localPref: 100
# ...
----
+
.. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f bgpadvertisement2.yaml
----

// Add a BGP peer with VRF
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-bgp-peers.adoc

[id="nw-metallb-bgp-peer-vrf_{context}"]
= Exposing a service through a network VRF

[role="_abstract"]
To isolate network traffic and manage multiple routing tables, expose a service through a virtual routing and forwarding (VRF) instance. Associating a VRF with a MetalLB BGP peer ensures that external traffic is segmented and correctly routed to the intended application workloads.

By using a VRF on a network interface to expose a service through a BGP peer, you can segregate traffic to the service, configure independent routing decisions, and enable multi-tenancy support on a network interface.

[NOTE]
====
By establishing a BGP session through an interface belonging to a network VRF, MetalLB can advertise services through that interface and enable external traffic to reach the service through this interface. However, the network VRF routing table is different from the default VRF routing table used by OVN-Kubernetes. Therefore, the traffic cannot reach the OVN-Kubernetes network infrastructure.

To enable the traffic directed to the service to reach the OVN-Kubernetes network infrastructure, you must configure routing rules to define the next hops for network traffic. See the `NodeNetworkConfigurationPolicy` resource in "Managing symmetric routing with MetalLB" in the _Additional resources_ section for more information.
====

The following high-level steps demonstrate how to expose a service through a network VRF with a BGP peer:

. Define a BGP peer and add a network VRF instance.
. Specify an IP address pool for MetalLB.
. Configure a BGP route advertisement for MetalLB to advertise a route by using the specified IP address pool and the BGP peer associated with the VRF instance.
. Deploy a service to test the configuration.

.Prerequisites

* You installed the {oc-first}.
* You logged in as a user with `cluster-admin` privileges.
* You defined a `NodeNetworkConfigurationPolicy` (NNCP) to associate a Virtual Routing and Forwarding (VRF) instance with a network interface. For more information about completing this prerequisite, see the _Additional resources_ section.
* You installed MetalLB on your cluster.

.Procedure

. Create a `BGPPeer` custom resource (CR):
+
.. Create a file, such as `frrviavrf.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: frrviavrf
  namespace: metallb-system
spec:
  myASN: 100
  peerASN: 200
  peerAddress: 192.168.130.1
  vrf: ens4vrf
# ...
----
`spec.vrf`: Specifies the network VRF instance to associate with the BGP peer. MetalLB can advertise services and make routing decisions based on the routing information in the VRF.
+
[NOTE]
====
You must configure this network VRF instance in a `NodeNetworkConfigurationPolicy` CR. See the _Additional resources_ for more information.
====
+
.. Apply the configuration for the BGP peer by running the following command:
+
[source,terminal]
----
$ oc apply -f frrviavrf.yaml
----

. Create an `IPAddressPool` CR:
+
.. Create a file, such as `first-pool.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.169.10.0/32
# ...
----
+
.. Apply the configuration for the IP address pool by running the following command:
+
[source,terminal]
----
$ oc apply -f first-pool.yaml
----

. Create a `BGPAdvertisement` CR:
+
.. Create a file, such as `first-adv.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: first-adv
  namespace: metallb-system
spec:
  ipAddressPools:
    - first-pool
  peers:
    - frrviavrf
# ...
----
`peers.frrviavrf`: In this example, MetalLB advertises a range of IP addresses from the `first-pool` IP address pool to the `frrviavrf` BGP peer.
+
.. Apply the configuration for the BGP advertisement by running the following command:
+
[source,terminal]
----
$ oc apply -f first-adv.yaml
----

. Create a `Namespace`, `Deployment`, and `Service` CR:
+
.. Create a file, such as `deploy-service.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: test
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: server
  namespace: test
spec:
  selector:
    matchLabels:
      app: server
  template:
    metadata:
      labels:
        app: server
    spec:
      containers:
      - name: server
        image: nginx
        ports:
        - name: http
          containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: server1
  namespace: test
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: server
  type: LoadBalancer
# ...
----
+
.. Apply the configuration for the namespace, deployment, and service by running the following command:
+
[source,terminal]
----
$ oc apply -f deploy-service.yaml
----

.Verification

. Identify a MetalLB speaker pod by running the following command:
+
[source,terminal]
----
$ oc get -n metallb-system pods -l component=speaker
----
+
.Example output
[source,terminal]
----
NAME            READY   STATUS    RESTARTS   AGE
speaker-c6c5f   6/6     Running   0          69m
----

. Verify that the state of the BGP session is `Established` in the speaker pod by running the following command, replacing the variables to match your configuration:
+
[source,terminal]
----
$ oc exec -n metallb-system <speaker_pod> -c frr -- vtysh -c "show bgp vrf <vrf_name> neigh"
----
+
.Example output
[source,terminal]
----
BGP neighbor is 192.168.30.1, remote AS 200, local AS 100, external link
  BGP version 4, remote router ID 192.168.30.1, local router ID 192.168.30.71
  BGP state = Established, up for 04:20:09

...
----

. Verify that the service is advertised correctly by running the following command:
+
[source,terminal]
----
$ oc exec -n metallb-system <speaker_pod> -c frr -- vtysh -c "show bgp vrf <vrf_name> ipv4"
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About virtual routing and forwarding

* Example: Network interface with a VRF instance node network configuration policy

* Configuring an egress service

* Managing symmetric routing with MetalLB

// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-bgp-peers.adoc

[id="nw-metallb-example-bgppeer_{context}"]
= Example BGP peer configurations

[role="_abstract"]
To precisely manage network topology and improve routing resilience, configure MetalLB BGP peer settings that limit node connectivity and incorporate BFD profiles. Defining these parameters ensures that your cluster maintains secure peer relationships and rapidly detects path failures for high service availability.

Example of limiting which nodes connect to a BGP peer::

You can specify the `nodeSelectors` parameter to control which nodes can connect to a BGP peer.

[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: doc-example-nodesel
  namespace: metallb-system
spec:
  peerAddress: 10.0.20.1
  peerASN: 64501
  myASN: 64500
  nodeSelectors:
  - matchExpressions:
    - key: kubernetes.io/hostname
      operator: In
      values: [compute-1.example.com, compute-2.example.com]
# ...
----

Example of specifying a BFD profile for a BGP peer::

You can specify a BFD profile to associate with BGP peers. BFD complements BGP by providing faster detection of communication failures between peers than BGP alone.

[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: doc-example-peer-bfd
  namespace: metallb-system
spec:
  peerAddress: 10.0.20.1
  peerASN: 64501
  myASN: 64500
  holdTime: "10s"
  bfdProfile: doc-example-bfd-profile-full
# ...
----

//Dependency on RHEL bug 2054160 being addressed.Remove note when fixed.
[NOTE]
====
Deleting the bidirectional forwarding detection (BFD) profile and removing the `bfdProfile` added to the border gateway protocol (BGP) peer resource does not disable the BFD. Instead, the BGP peer starts using the default BFD profile. To disable BFD from a BGP peer resource, delete the BGP peer configuration and recreate it without a BFD profile. For more information, see *BZ#2050824*.
====

Example of specifying BGP peers for dual-stack networking::

To support dual-stack networking, add one BGP peer custom resource for IPv4 and one BGP peer custom resource for IPv6.

[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: doc-example-dual-stack-ipv4
  namespace: metallb-system
spec:
  peerAddress: 10.0.20.1
  peerASN: 64500
  myASN: 64500
---
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: doc-example-dual-stack-ipv6
  namespace: metallb-system
spec:
  peerAddress: 2620:52:0:88::104
  peerASN: 64500
  myASN: 64500
# ...
----

Example of specifying BGP peers for unnumbered BGP peering::

To configure unnumbered BGP peering, specify the interface in the `spec.interface` parameter by using the following example configuration:

[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: peer-unnumber
  namespace: metallb-system
spec:
  myASN: 64512
  ASN: 645000
  interface: net0
# ...
----

[NOTE]
====
To use the `interface` parameter, you must establish a point-to-point layer 2 connection between the two BGP peers.
You can use unnumbered BGP peering with IPv4, IPv6, or dual-stack, but you must enable IPv6 Router Advertisements (RAs).
Each interface is limited to one BGP connection.

If you use this parameter, you cannot specify a value in the `spec.bgp.routers.neighbors.address` parameter.
====

[role="_additional-resources"]
== Additional resources

* Configuring services to use MetalLB
