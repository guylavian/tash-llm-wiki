---
title: "Configuring community alias"
type: reference
domain: openshift
slug: networking-4-22-metallb-configure-community-alias
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/metallb-configure-community-alias
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring community alias

[id="metallb-configure-community-alias"]
= Configuring community alias

[role="_abstract"]
As a cluster administrator, you can configure a community alias and use it across different advertisements.

// Address pool custom resource
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-community-alias.adoc

[id="nw-metallb-community-cr_{context}"]
= About the community custom resource

[role="_abstract"]
To simplify BGP configuration, define named aliases for community values by using the community custom resource. You can reference these aliases when advertising `ipAddressPools` with the `BGPAdvertisement` resource.

The fields for the `community` custom resource are described in the following table.

[NOTE]
====
The `community` CRD applies only to BGPAdvertisement.
====

.MetalLB community custom resource
[cols="1,1,3a", options="header"]
|===

|Field
|Type
|Description

|`metadata.name`
|`string`
|Specifies the name for the `community`.

|`metadata.namespace`
|`string`
|Specifies the namespace for the `community`.
Specify the same namespace that the MetalLB Operator uses.

|`spec.communities`
|`string`
|Specifies a list of BGP community aliases that can be used in BGPAdvertisements. A community alias consists of a pair of name (alias) and value (number:number). Link the BGPAdvertisement to a community alias by referring to the alias name in its `spec.communities` field.

|===

.CommunityAlias
[cols="1,1,3a", options="header"]
|===

|Field
|Type
|Description

|`name`
|`string`
|The name of the alias for the `community`.

|`value`
|`string`
|The BGP `community` value corresponding to the given name.
|===

// Configure advertisement with community alias
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-community-alias.adoc

[id="nw-metallb-configure-BGP-advertisement-community-alias_{context}"]
= Configuring MetalLB with a BGP advertisement and community alias

[role="_abstract"]
To advertise an `IPAddressPool` by using the BGP protocol, configure MetalLB with a community alias. This configuration sets the alias to the numeric value of the `NO_ADVERTISE` community.

In the following example, the peer BGP router `doc-example-peer-community` receives one `203.0.113.200/32` route and one `fc00:f853:ccd:e799::1/128` route for each load-balancer IP address that MetalLB assigns to a service. A community alias is configured with the `NO_ADVERTISE` community.

.Prerequisites

* Install the {oc-first}
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create an IP address pool.
+
.. Create a file, such as `ipaddresspool.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: doc-example-bgp-community
spec:
  addresses:
    - 203.0.113.200/30
    - fc00:f853:ccd:e799::/124
----
+
.. Apply the configuration for the IP address pool:
+
[source,terminal]
----
$ oc apply -f ipaddresspool.yaml
----

. Create a community alias named `community1`.
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: Community
metadata:
  name: community1
  namespace: metallb-system
spec:
  communities:
    - name: NO_ADVERTISE
      value: '65535:65282'
----

. Create a BGP peer named `doc-example-bgp-peer`.
+
.. Create a file, such as `bgppeer.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  namespace: metallb-system
  name: doc-example-bgp-peer
spec:
  peerAddress: 10.0.0.1
  peerASN: 64501
  myASN: 64500
  routerID: 10.10.10.10
----
+
.. Apply the configuration for the BGP peer:
+
[source,terminal]
----
$ oc apply -f bgppeer.yaml
----

. Create a BGP advertisement with the community alias.
+
.. Create a file, such as `bgpadvertisement.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgp-community-sample
  namespace: metallb-system
spec:
  aggregationLength: 32
  aggregationLengthV6: 128
  communities:
    - NO_ADVERTISE
  ipAddressPools:
    - doc-example-bgp-community
  peers:
    - doc-example-peer
----
+
where:
+
`NO_ADVERTISE`: Specifies the `CommunityAlias.name` here and not the community custom resource (CR) name.
+
.. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f bgpadvertisement.yaml
----
