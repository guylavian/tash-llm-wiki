---
title: "Configuring MetalLB address pools"
type: reference
domain: openshift
slug: networking-4-22-metallb-configure-address-pools
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/metallb-configure-address-pools
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring MetalLB address pools

[id="metallb-configure-address-pools"]
= Configuring MetalLB address pools

[role="_abstract"]
To allocate and manage the IP addresses assigned to load balancer services, configure MetalLB address pool custom resources. Defining these pools ensures that application workloads remain reachable through designated network ranges for consistent external access.

The namespaces used in the examples show `metallb-system` as the namespace.

For more information about how to install the MetalLB Operator, see About MetalLB and the MetalLB Operator.

// Address pool custom resource
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-address-pools.adoc

[id="nw-metallb-ipaddresspool-cr_{context}"]
= About the IPAddressPool custom resource

[role="_abstract"]
To define the IP address ranges available for load balancer services, configure the properties of the MetalLB `IPAddressPool` custom resource (CR).

The following table details the parameters for the `IPAddressPool` CR:

.MetalLB IPAddressPool pool custom resource
[cols="1,1,3a", options="header"]
|===

|Parameter
|Type
|Description

|`metadata.name`
|`string`
|Specifies the name for the address pool. When you add a service, you can specify this pool name in the `metallb.io/address-pool` annotation to select an IP address from a specific pool. The names `doc-example`, `silver`, and `gold` are used throughout the documentation.

|`metadata.namespace`
|`string`
|Specifies the namespace for the address pool. Specify the same namespace that the MetalLB Operator uses.

|`metadata.label`
|`string`
|Optional: Specifies the key-value pair assigned to the `IPAddressPool`. This can be referenced by the `ipAddressPoolSelectors` in the `BGPAdvertisement` and `L2Advertisement` CRD to associate the `IPAddressPool` with the advertisement

|`spec.addresses`
|`string`
|Specifies a list of IP addresses for the MetalLB Operator to assign to services. You can specify multiple ranges in a single pool, where these ranges all share the same settings. Specify each range in Classless Inter-Domain Routing (CIDR) notation or as starting and ending IP addresses separated with a hyphen.

|`spec.autoAssign`
|`boolean`
|Optional: Specifies whether the MetalLB Operator automatically assigns IP addresses from this pool.
Specify `false` if you want to explicitly request an IP address from this pool with the `metallb.io/address-pool` annotation. The default value is `true`.

[NOTE]
====
For IP address pool configurations, ensure the addresses parameter specifies only IP addresses that are available and not in use by other network devices, especially gateway addresses, to prevent conflicts when `autoAssign` is enabled.
====

|`spec.avoidBuggyIPs`
|`boolean`
|Optional: When you set the parameter to enabled, the IP addresses ending `.0` and `.255` are not allocated from the pool. The default value is `false`. Some older consumer network equipment mistakenly block IP addresses ending in `.0` and `.255`.

|===

You can assign IP addresses from an `IPAddressPool` to services and namespaces by configuring the `spec.serviceAllocation` specification.

.MetalLB IPAddressPool custom resource spec.serviceAllocation subfields
[cols="1,1,3a", options="header"]
|===

|Parameter
|Type
|Description

|`priority`
|`int`
|Optional: Defines the priority between IP address pools when more than one IP address pool matches a service or namespace. A lower number indicates a higher priority.

|`namespaces`
|`array (string)`
|Optional: Specifies a list of namespaces that you can assign to IP addresses in an IP address pool.

|`namespaceSelectors`
|`array (LabelSelector)`
|Optional: Specifies namespace labels that you can assign to IP addresses from an IP address pool by using label selectors in a list format.

|`serviceSelectors`
|`array (LabelSelector)`
|Optional: Specifies service labels that you can assign to IP addresses from an address pool by using label selectors in a list format.

|===

// Add an address pool
[id="nw-metallb-configure-address-pool_{context}"]
= Configuring an address pool

[role="_abstract"]
To precisely manage external access to application workloads, configure MetalLB address pools for your cluster. By defining these pools, you can control the specific IP address ranges assigned to load balancer services for consistent network routing.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a file, such as `ipaddresspool.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: doc-example
  labels:
    zone: east
spec:
  addresses:
  - 203.0.113.1-203.0.113.10
  - 203.0.113.65-203.0.113.75
# ...
----
+
where:
+
`labels`:: The label assigned to the `IPAddressPool` can be referenced by the `ipAddressPoolSelectors` in the `BGPAdvertisement` CRD to associate the `IPAddressPool` with the advertisement.

. Apply the configuration for the IP address pool by entering the following command:
+
[source,terminal]
----
$ oc apply -f ipaddresspool.yaml
----

.Verification

. View the address pool by entering the following command:
+
[source,terminal]
----
$ oc describe -n metallb-system IPAddressPool doc-example
----
+
.Example output
[source,terminal]
----
Name:         doc-example
Namespace:    metallb-system
Labels:       zone=east
Annotations:  <none>
API Version:  metallb.io/v1beta1
Kind:         IPAddressPool
Metadata:
  ...
Spec:
  Addresses:
    203.0.113.1-203.0.113.10
    203.0.113.65-203.0.113.75
  Auto Assign:  true
Events:         <none>
----

. Confirm that the address pool name, such as `doc-example`, and the IP address ranges exist in the output.

// Supporting VLAN setup
[id="nw-metallb-configure-address-pool-vlan_{context}"]
= Configure MetalLB address pool for VLAN

[role="_abstract"]
To precisely manage external access across a specific VLAN, configure MetalLB address pools for your cluster. Defining these pools ensures that load balancer services receive authorized IP addresses from designated network ranges for secure and consistent routing.

.Prerequisites

* Install the {oc-first}.
* Configure a separate VLAN.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a file, such as `ipaddresspool-vlan.yaml`, that is similar to the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: doc-example-vlan
  labels:
    zone: east
spec:
  addresses:
  - 192.168.100.1-192.168.100.254
# ...
----
+
where:
+
`labels.zone`:: This label assigned to the `IPAddressPool` can be referenced by the `ipAddressPoolSelectors` in the `BGPAdvertisement` CRD to associate the `IPAddressPool` with the advertisement.
`spec.addresses`:: This IP range must match the subnet assigned to the VLAN on your network. To support layer 2 (L2) mode, the IP address range must be within the same subnet as the cluster nodes.

. Apply the configuration for the IP address pool:
+
[source,terminal]
----
$ oc apply -f ipaddresspool-vlan.yaml
----

. To ensure this configuration applies to the VLAN, you need to set the `spec` `gatewayConfig.ipForwarding` to `Global`.
+
.. Run the following command to edit the network configuration custom resource (CR):
+
[source,terminal]
----
$ oc edit network.operator.openshift/cluster
----
+
.. Update the `spec.defaultNetwork.ovnKubernetesConfig` section to include the `gatewayConfig.ipForwarding` set to `Global`. The following example demonstrates this configuration:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
    - cidr: 10.128.0.0/14
      hostPrefix: 23
  defaultNetwork:
    type: OVNKubernetes
    ovnKubernetesConfig:
      gatewayConfig:
        ipForwarding: Global
# ...
----

// Examples
// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-address-pools.adoc

[id="nw-metallb-example-addresspool_{context}"]
= Example address pool configurations

[role="_abstract"]
To precisely allocate IP address ranges for cluster services, configure MetalLB address pools by using Classless Inter-Domain Routing (CIDR) notation or hyphenated bounds. Defining these specific ranges ensures that application workloads receive valid IP assignments that align with your existing network infrastructure requirements.

Example of IPv4 and CIDR ranges::

You can specify a range of IP addresses in classless inter-domain routing (CIDR) notation. You can combine CIDR notation with the notation that uses a hyphen to separate lower and upper bounds.
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-cidr
  namespace: metallb-system
spec:
  addresses:
  - 192.168.100.0/24
  - 192.168.200.0/24
  - 192.168.255.1-192.168.255.5
# ...
----

Example of assigning IP addresses::

You can set the `autoAssign` parameter to `false` to prevent MetalLB from automatically assigning IP addresses from the address pool. You can then assign a single IP address or multiple IP addresses from an IP address pool. To assign an IP address, append the `/32` CIDR notation to the target IP address in the `spec.addresses` parameter. This setting ensures that only the specific IP address is available for assignment, leaving non-reserved IP addresses for application use.
+
.Example `IPAddressPool` CR that assigns multiple IP addresses
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-reserved
  namespace: metallb-system
spec:
  addresses:
  - 192.168.100.1/32
  - 192.168.200.1/32
  autoAssign: false
# ...
----
+
[NOTE]
====
When you add a service, you can request a specific IP address from the address pool or you can specify the pool name in an annotation to request any IP address from the pool.
====

Example of IPv4 and IPv6 addresses::

You can add address pools that use IPv4 and IPv6. You can specify multiple ranges in the `addresses` list, just like several IPv4 examples.
+
How the service is assigned to a single IPv4 address, a single IPv6 address, or both is determined by how you add the service. The `spec.ipFamilies` and `spec.ipFamilyPolicy` parameters control how IP addresses are assigned to the service.
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-combined
  namespace: metallb-system
spec:
  addresses:
  - 10.0.100.0/28
  - 2002:2:2::1-2002:2:2::100
# ...
----
+
`spec.addresses`: This list defines the IP ranges that MetalLB manages. This specific example is a dual-stack configuration, meaning it provides both IPv4 and IPv6 addresses.

Example of assigning IP address pools to services or namespaces::

You can assign IP addresses from an `IPAddressPool` to services and namespaces that you specify.
+
If you assign a service or namespace to more than one IP address pool, MetalLB uses an available IP address from the higher-priority IP address pool. If no IP addresses are available from the assigned IP address pools with a high priority, MetalLB uses available IP addresses from an IP address pool with lower priority or no priority.
+
[NOTE]
====
You can use the `matchLabels` label selector, the `matchExpressions` label selector, or both, for the `namespaceSelectors` and `serviceSelectors` specifications. This example demonstrates one label selector for each specification.
====
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-service-allocation
  namespace: metallb-system
spec:
  addresses:
    - 192.168.20.0/24
  serviceAllocation:
    priority: 50
    namespaces:
      - namespace-a
      - namespace-b
    namespaceSelectors:
      - matchLabels:
          zone: east
    serviceSelectors:
      - matchExpressions:
        - key: security
          operator: In
          values:
          - S1
# ...
----
+
where:

`serviceAllocation.priority`:: Assign a priority to the address pool. A lower number indicates a higher priority.
`serviceAllocation.namespaces`:: Assign one or more namespaces to the IP address pool in a list format.
`serviceAllocation.namespaceSelectors`:: Assign one or more namespace labels to the IP address pool by using label selectors in a list format.
`serviceAllocation.serviceSelectors`:: Assign one or more service labels to the IP address pool by using label selectors in a list format.

[id="additional-resources_metallb-configure-address-pools"]
[role="_additional-resources"]
== Additional resources

* Configuring MetalLB with an L2 advertisement and label

* Configuring MetalLB BGP peers

* Configuring services to use MetalLB
