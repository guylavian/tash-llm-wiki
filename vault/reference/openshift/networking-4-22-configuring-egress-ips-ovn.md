---
title: "Configuring an egress IP address"
type: reference
domain: openshift
slug: networking-4-22-configuring-egress-ips-ovn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-egress-ips-ovn
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring an egress IP address

[id="configuring-egress-ips-ovn"]
= Configuring an egress IP address

[role="_abstract"]
As a cluster administrator, you can configure the OVN-Kubernetes Container Network Interface (CNI) network plugin to assign one or more egress IP addresses to a namespace, or to specific pods in a namespace.

// Egress IP address architectural design and implementation
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-about_{context}"]
= Egress IP address architectural design and implementation

[role="_abstract"]
By using the OpenShift Container Platform egress IP address functionality, you can ensure that the traffic from one or more pods in one or more namespaces has a consistent source IP address for services outside the cluster network.

For example, you might have a pod that periodically queries a database that is hosted on a server outside of your cluster. To enforce access requirements for the server, a packet filtering device is configured to allow traffic only from specific IP addresses.

To ensure that you can reliably allow access to the server from only that specific pod, you can configure a specific egress IP address for the pod that makes the requests to the server.

An egress IP address assigned to a namespace is different from an egress router, which is used to send traffic to specific destinations.

In some cluster configurations,
In {hcp-title} clusters,
application pods and ingress router pods run on the same node. If you configure an egress IP address for an application project in this scenario, the IP address is not used when you send a request to a route from the application project.

[IMPORTANT]
====
Egress IP addresses must not be configured in any Linux network configuration files, such as `ifcfg-eth0`.
====

[IMPORTANT]
====
The assignment of egress IP addresses to control plane nodes with the EgressIP feature is
not supported.
not supported on a cluster provisioned on {aws-first}. For more information, see "BZ#2039656" in the _Additional resources_ section.
====

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability.

.Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS
[source,yaml]
----
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
----

The following sections describe the IP address capacity for supported public cloud environments for use in your capacity calculation.

{aws-first} IP address capacity limits::
{aws-first} IP address capacity limits::

On {aws-short}, constraints on IP address assignments depend on the instance type configured. For more information, see "IP addresses per network interface per instance type" in the _Additional resources_ section.

{gcp-first} IP address capacity limits::

On {gcp-short}, the networking model implements additional node IP addresses through IP address aliasing, rather than IP address assignments. However, IP address capacity maps directly to IP aliasing capacity.

The following capacity limits exist for IP aliasing assignment:

- Per node, the maximum number of IP aliases, both IPv4 and IPv6, is 100.
- Per VPC, the maximum number of IP aliases is unspecified, but OpenShift Container Platform scalability testing reveals the maximum to be approximately 15,000.

For more information, see "Per instance" quotas and "Alias IP ranges overview" in the _Additional resources_ section.

{azure-full} IP address capacity limits::

On {azure-short}, the following capacity limits exist for IP address assignment:

- Per NIC, the maximum number of assignable IP addresses, for both IPv4 and IPv6, is 256.
- Per virtual network, the maximum number of assigned IP addresses cannot exceed 65,536.

For more information, see "Networking limits" in the _Additional resources_ section.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* BZ#2039656 (Red Hat Bugzilla)
* Per instance ({gcp-full} documentation)
* Alias IP ranges overview ({gcp-full} documentation)
* Networking limits ({azure-full} documentation)
* IP addresses per network interface per instance type ({aws-short} documentation)

// Platform support
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-platform-support_{context}"]
= Platform support

[role="_abstract"]
The Egress IP address feature that runs on a primary host network is supported on specific platforms.

The following table shows supported platforms for egress IP on primary host networks:

[cols="1,1",options="header"]
|===
| Platform | Supported

| Bare metal | Yes
| {vmw-full} | Yes
| {rh-openstack-first} | Yes
| {aws-first} | Yes
| {gcp-first} | Yes
| {azure-full}| Yes
| {ibm-z-name} and {ibm-linuxone-name} | Yes
| {ibm-z-name} and {ibm-linuxone-name} for {op-system-base-full} KVM | Yes
| {ibm-power-name} | Yes
| Nutanix | Yes
|===

[IMPORTANT]
====
Support for egress IP addresses in {azure-full} is restricted to the infra subnet. As a workaround for this limitation, you can use a Network Address Translation (NAT) gateway instead of a general purpose public load balancer.
====

The Egress IP address feature that runs on secondary host networks is supported on the following platform:

[cols="1,1",options="header"]
|===
| Platform | Supported

| Bare metal | Yes
|===

// Public cloud platform considerations
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-public-cloud-platform-considerations_{context}"]
= Public cloud platform considerations

[role="_abstract"]
Typically, public cloud providers place a limit on egress IP addresses. You must understand the existence of a constraint on the absolute number of assignable IP addresses per node for clusters provisioned on public cloud infrastructure.

The maximum number of assignable IP addresses per node, or the _IP capacity_, can be described in the following formula:

[source,text]
----
IP capacity = public cloud default capacity - sum(current IP assignments)
----

While the Egress IP addresses capability manages the IP address capacity per node, ensure you plan for this constraint in your deployments. For example, if a public cloud provider limits IP address capacity to 10 IP addresses per node, and you have 8 nodes, the total number of assignable IP addresses is only 80. To achieve a higher IP address capacity, you would need to allocate additional nodes. For example, if you needed 150 assignable IP addresses, you would need to allocate 7 additional nodes.

To confirm the IP capacity and subnets for any node in your public cloud environment, you can enter the `oc get node <node_name> -o yaml` command. The `cloud.network.openshift.io/egress-ipconfig` annotation includes capacity and subnet information for the node.

The annotation value is an array with a single object with fields that provide the following information for the primary network interface:

* `interface`: Specifies the interface ID on {aws-short} and {azure-short} and the interface name on {gcp-short}.
* `ifaddr`: Specifies the subnet mask for one or both IP address families.
* `capacity`: Specifies the IP address capacity for the node. On {aws-short}, the IP address capacity is provided per IP address family. On {azure-short} and {gcp-short}, the IP address capacity includes both IPv4 and IPv6 addresses.

Automatic attachment and detachment of egress IP addresses for traffic between nodes are available. Traffic from many pods in namespaces can have a consistent source IP address to locations outside of the cluster.

[NOTE]
====
The {rh-openstack} egress IP address feature creates a Neutron reservation port called `egressip-<IP address>`. Using the same {rh-openstack} user as the one used for the OpenShift Container Platform cluster installation, you can assign a floating IP address to this reservation port to have a predictable SNAT address for egress traffic. When an egress IP address on an {rh-openstack} network is moved from one node to another, because of a node failover, for example, the Neutron reservation port is removed and recreated. This means that the floating IP association is lost and you need to manually reassign the floating IP address to the new reservation port.
====

[NOTE]
====
When an {rh-openstack} cluster administrator assigns a floating IP to the reservation port, OpenShift Container Platform cannot delete the reservation port. The `CloudPrivateIPConfig` object cannot perform delete and move operations until an {rh-openstack} cluster administrator unassigns the floating IP from the reservation port.
====

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability.

.Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS
[source,yaml]
----
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
----

.Example `cloud.network.openshift.io/egress-ipconfig` annotation on {gcp-short}
[source,yaml]
----
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"nic0",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ip":14}
  }
]
----

// Considerations for using an egress IP address on additional network interfaces
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-multi-nic-considerations_{context}"]
= Considerations for using an egress IP address on additional network interfaces

[role="_abstract"]
In OpenShift Container Platform, egress IP addresses provide administrators a way to control network traffic. Egress IP addresses can be used with a `br-ex` Open vSwitch (OVS) bridge interface and any physical interface that has IP connectivity enabled.

You can inspect your network interface type by running the following command:

[source,terminal]
----
$ ip -details link show
----

The primary network interface is assigned a node IP address which also contains a subnet mask. Information for this node IP address can be retrieved from the Kubernetes node object for each node within your cluster by inspecting the `k8s.ovn.org/node-primary-ifaddr` annotation. In an IPv4 cluster, this annotation is similar to the following example: `"k8s.ovn.org/node-primary-ifaddr: {"ipv4":"192.168.111.23/24"}"`.

If the egress IP address is not within the subnet of the primary network interface subnet, you can use an egress IP address on another Linux network interface that is not of the primary network interface type. By doing so, OpenShift Container Platform administrators are provided with a greater level of control over networking aspects such as routing, addressing, segmentation, and security policies. This feature provides users with the option to route workload traffic over specific network interfaces for purposes such as traffic segmentation or meeting specialized requirements.

If the egress IP address is not within the subnet of the primary network interface, then the selection of another network interface for egress traffic might occur if they are present on a node.

You can determine which other network interfaces might support egress IP address addresses by inspecting the `k8s.ovn.org/host-cidrs` Kubernetes node annotation. This annotation contains the addresses and subnet mask found for the primary network interface. The annotation also contains additional network interface addresses and subnet mask information. These addresses and subnet masks are assigned to network interfaces that use the longest prefix match routing mechanism to determine which network interface supports the egress IP address. For more information, see "Longest prefix match routing" in the _Additional resources_ section.

[NOTE]
====
OVN-Kubernetes provides a mechanism to control and direct outbound network traffic from specific namespaces and pods. This ensures that it exits the cluster through a particular network interface and with a specific egress IP address.
====

As an administrator who wants an egress IP address and traffic to route over a particular interface that is not the primary network interface, you must meet the following conditions:

* OpenShift Container Platform is installed on a bare-metal cluster. This feature is disabled within a cloud or a hypervisor environment.

* Your OpenShift Container Platform pods are not configured as _host-networked_.

* You understand that if a network interface is removed or if the IP address and subnet mask which allows the egress IP address to be hosted on the interface is removed, reconfiguration of the egress IP address occurs. Consequently, the egress IP address might get assigned to another node and interface.

* If you use an Egress IP address on a secondary network interface card (NIC), you must use the Node Tuning Operator to enable IP forwarding on the secondary NIC.

* You configured a NIC with routes by ensuring a gateway exists in the main routing table. As a postinstallation task, Red Hat does not support configuring a NIC on a cluster that uses OVN-Kubernetes.

* Routes associated with an egress interface get copied from the main routing table to the routing table that was created to support the Egress IP object.

* Longest prefix match routing (NetworkLessons documentation)

// Architectural diagram of an egress IP address configuration
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-node-architecture_{context}"]
= Architectural diagram of an egress IP address configuration

[role="_abstract"]
To better understand egress IP address configuration, reference the architectural diagram.

The following diagram shows an egress IP address configuration. The diagram describes four pods in two different namespaces running on three nodes in a cluster. The nodes are assigned IP addresses from the `192.168.126.0/18` CIDR block on the host network.

// Source: https://github.com/redhataccess/documentation-svg-assets/blob/master/for-web/121_OpenShift/121_OpenShift_engress_IP_Topology_1020.svg
image::nw-egress-ips-diagram.svg[Architectural diagram for the egress IP feature]

Both Node 1 and Node 3 are labeled with `k8s.ovn.org/egress-assignable: ""` and thus available for the assignment of egress IP addresses.

The dashed lines in the diagram depict the traffic flow from pod1, pod2, and pod3 traveling through the pod network to egress the cluster from Node 1 and Node 3. When an external service receives traffic from any of the pods selected by the example `EgressIP` object, the source IP address is either `192.168.126.10` or `192.168.126.102`. The traffic is balanced roughly equally between these two nodes.

Based on the diagram, the following manifest file defines namespaces:

.Namespace objects
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
  labels:
    env: prod
---
apiVersion: v1
kind: Namespace
metadata:
  name: namespace2
  labels:
    env: prod
----

Based on the diagram, the following `EgressIP` object describes a configuration that selects all pods in any namespace with the `env` label set to `prod`. The egress IP addresses for the selected pods are `192.168.126.10` and `192.168.126.102`.

.`EgressIP` object
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egressips-prod
spec:
  egressIPs:
  - 192.168.126.10
  - 192.168.126.102
  namespaceSelector:
    matchLabels:
      env: prod
status:
  items:
  - node: node1
    egressIP: 192.168.126.10
  - node: node3
    egressIP: 192.168.126.102
----

For the configuration in the previous example, OpenShift Container Platform assigns both egress IP addresses to the available nodes. The `status` field reflects whether and where the egress IP addresses are assigned.

// EgressIP object
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-object_{context}"]
= EgressIP object

[role="_abstract"]
You can view YAML files to better understand how you can effectively configure an `EgressIP` object to better meet your needs.

When the `EgressIP` namespace selector matches the label on multiple namespaces, consider the following behaviors:

* All traffic for selected pods must pass through a single node. During times of high traffic, the network interface of the node might experience performance issues.
* An error in a label selector might change the outbound IP address for many cluster namespaces.
* Only a cluster administrator can create or change cluster-scoped objects.
* Packets must move from a pod that exists in a node to the named host node that is referenced in the `EgressIP` object. This approach adds a network hop.

[IMPORTANT]
====
Do not create egress rules, such as a single label selector, that forces all namespaces that exist in a cluster to use the same outbound IP address. This configuration can cause the node that hosts the IP address to crash during times of high network traffic.
====

The following YAML describes the API for the `EgressIP` object. The scope of the object is cluster-wide and is not created in a namespace.

[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: <name>
spec:
  egressIPs:
  - <ip_address>
  namespaceSelector:
    ...
  podSelector:
    ...
----

--
where:

`<name>`:: Specifies the name for the `EgressIPs` object.

`<egressIPs>`:: Specifies an array of one or more IP addresses.

`<namespaceSelector>`:: Specifies one or more selectors for the namespaces to associate the egress IP addresses with.

`<podSelector>`:: Optional parameter. Specifies one or more selectors for pods in the specified namespaces to associate egress IP addresses with. Applying these selectors allows for the selection of a subset of pods within a namespace.
--

The following YAML describes the stanza for the namespace selector:

.Namespace selector stanza
[source,yaml]
----
namespaceSelector:
  matchLabels:
    <label_name>: <label_value>
----

--
where:

`<namespaceSelector>`:: Specifies one or more matching rules for namespaces. If more than one match rule is provided, all matching namespaces are selected.
--

The following YAML describes the optional stanza for the pod selector:

.Pod selector stanza
[source,yaml]
----
podSelector:
  matchLabels:
    <label_name>: <label_value>
----

--
where:

`<podSelector>`:: Optional parameter. Specifies one or more matching rules for pods in the namespaces that match the specified `namespaceSelector` rules. If specified, only pods that match are selected. Others pods in the namespace are not selected.
--

In the following example, the `EgressIP` object associates the `192.168.126.11` and `192.168.126.102` egress IP addresses with pods that have the `app` label set to `web` and are in the namespaces that have the `env` label set to `prod`:

.Example `EgressIP` object
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group1
spec:
  egressIPs:
  - 192.168.126.11
  - 192.168.126.102
  podSelector:
    matchLabels:
      app: web
  namespaceSelector:
    matchLabels:
      env: prod
----

In the following example, the `EgressIP` object associates the `192.168.127.30` and `192.168.127.40` egress IP addresses with any pods that do not have the `environment` label set to `development`:

.Example `EgressIP` object
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group2
spec:
  egressIPs:
  - 192.168.127.30
  - 192.168.127.40
  namespaceSelector:
    matchExpressions:
    - key: environment
      operator: NotIn
      values:
      - development
----

// Assignment of egress IPs to a namespace, nodes, and pods
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-considerations_{context}"]
= Assignment of egress IPs to a namespace, nodes, and pods

[role="_abstract"]
To assign one or more egress IPs to a namespace or specific pods in a namespace, you must meet specific conditions.

- At least one node in your cluster must have the `k8s.ovn.org/egress-assignable: ""` label.
- An `EgressIP` object exists that defines one or more egress IP addresses to use as the source IP address for traffic leaving the cluster from pods in a namespace.

[IMPORTANT]
====
If you create `EgressIP` objects prior to labeling any nodes in your cluster for egress IP assignment, OpenShift Container Platform might assign every egress IP address to the first node with the `k8s.ovn.org/egress-assignable: ""` label.

To ensure that egress IP addresses are widely distributed across nodes in the cluster, always apply the label to the nodes you intend to host the egress IP addresses before creating any `EgressIP` objects.
====

When creating an `EgressIP` object, the following conditions apply to nodes that are labeled with the `k8s.ovn.org/egress-assignable: ""` label:

- An egress IP address is never assigned to more than one node at a time.
- An egress IP address is equally balanced between available nodes that can host the egress IP address.
- If the `spec.EgressIPs` array in an `EgressIP` object specifies more than one IP address, the following conditions apply:
* No node will ever host more than one of the specified IP addresses.
* Traffic is balanced roughly equally between the specified IP addresses for a given namespace.
- If a node becomes unavailable, any egress IP addresses assigned to it are automatically reassigned, subject to the previously described conditions.

[IMPORTANT]
====
If the number of nodes labeled with `k8s.ovn.org/egress-assignable` is less than the number of egress IP addresses specified in the `EgressIP` object, the additional egress IP addresses remain unassigned. To ensure all specified egress IP addresses are active and traffic is balanced as expected, verify that the number of egress-assignable nodes is equal to or greater than the number of egress IP addresses defined in the `EgressIP` object.
====

When a pod matches the selector for multiple `EgressIP` objects, there is no guarantee which of the egress IP addresses that are specified in the `EgressIP` objects is assigned as the egress IP address for the pod.

Additionally, if an `EgressIP` object specifies multiple egress IP addresses, there is no guarantee which of the egress IP addresses might be used. For example, if a pod matches a selector for an `EgressIP` object with two egress IP addresses, `10.10.20.1` and `10.10.20.2`, either might be used for each TCP connection or UDP conversation.

// Assigning an egress IP address to a namespace
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-assign_{context}"]
= Assigning an egress IP address to a namespace

[role="_abstract"]
You can assign one or more egress IP addresses to a namespace or to specific pods in a namespace.

.Prerequisites

* The {oc-first} is installed.
* You are logged in to the cluster as a cluster administrator.
* At least one node is configured to host an egress IP address.

.Procedure

. Create an `EgressIP` object.
+
.. Create a `<egressips_name>.yaml` file where `<egressips_name>` is the name of the object.
+
.. In the file that you created, define an `EgressIP` object, as in the following example:
+
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-project1
spec:
  egressIPs:
  - 192.168.127.10
  - 192.168.127.11
  namespaceSelector:
    matchLabels:
      env: qa
# ...
----

. To create the object, enter the following command.
+
[source,terminal]
----
$ oc apply -f <egressips_name>.yaml
----
+
--
where:

`<egressips_name>`:: Replace `<egressips_name>` with the name of the object.
--
+
.Example output
[source,terminal]
----
egressips.k8s.ovn.org/<egressips_name> created
----

. Optional: Store the `<egressips_name>.yaml` file so that you can make changes later.

. Add labels to the namespace that requires egress IP addresses. To add a label to the namespace of an `EgressIP` object defined in a previous step, run the following command:
+
[source,terminal]
----
$ oc label ns <namespace> env=qa
----
+
--
where:

`<namespace>`:: Replace `<namespace>` with the namespace that requires egress IP addresses.
--

.Verification

* To show all egress IP addresses that are in use in your cluster, enter the following command:
+
[source,terminal]
----
$ oc get egressip -o yaml
----
+
[NOTE]
====
The command `oc get egressip` only returns one egress IP address regardless of how many are configured. This is not a bug and is a limitation of Kubernetes. As a workaround, you can pass in the `-o yaml` or `-o json` flags to return all egress IPs addresses in use.
====
+
.Example output
[source,terminal]
----
# ...
spec:
  egressIPs:
  - 192.168.127.10
  - 192.168.127.11
# ...
----

// START: Conditional block for EgressIP Failover Configuration (Replaces nw-egress-ips-config-object.adoc)

// Explains the 'Why' and 'What' of failover control (The Job to be Done)
// Module included in the following assembly:
//
// *networking/ovn_kubernetes_network_provider/egressip_failover_assembly.adoc

[id="egressip_failover_concept_{context}"]
= Understanding EgressIP failover control

[role="_abstract"]
The `reachabilityTotalTimeoutSeconds` parameter controls how quickly the system detects a failing `egressIP` node and initiates a failover. This parameter directly determines the maximum time the platform waits before declaring a node unreachable.

[IMPORTANT]
====
When you configure `egressIP` with multiple egress nodes, the complete failover time from node failure to recovery on a new node is expected to be on the order of seconds or longer. This is because the new IP assignment can only begin after the `reachabilityTotalTimeoutSeconds` period has fully elapsed without a successful check.
====

To ensure traffic uses the correct external path, `egressIP` traffic on a node will always egress through the network interface on which the `egressIP` address has been assigned.

// Provides the step-by-step instructions (The How-To)
// Module included in the following assembly:
//
// *networking/ovn_kubernetes_network_provider/egressip_failover_assembly.adoc

[id="egressip_configure_failover_task_{context}"]
= Configuring the EgressIP failover time limit

[role="_abstract"]
You can configure the `reachabilityTotalTimeoutSeconds` parameter to control how quickly the system detects a failing `egressIP` node and initiates a failover.

.Prerequisites

* You installed the {oc-first}.
* You logged in to the cluster as a cluster administrator.

.Procedure

. Edit the `Network` custom resource by running the following command:
+
[source,bash]
----
$ oc edit network.operator cluster
----

. Navigate to the `egressIPConfig: {}` section under `spec:defaultNetwork:ovnKubernetesConfig:`

. Modify the block to include the `reachabilityTotalTimeoutSeconds` parameter with your chosen value, 5 seconds for example. Make sure to use the correct indentation:
+
[source,yaml]
----
  defaultNetwork:
    ovnKubernetesConfig:
      egressIPConfig:
        reachabilityTotalTimeoutSeconds: 5
----
+
[NOTE]
====
The value must be an integer between 0 and 60. For details on possible values, see the "EgressIP failover settings" section.
====

. Save and exit the editor. The operator automatically applies the changes.

.Verification

. Verify that the system correctly accepted the `reachabilityTotalTimeoutSeconds` parameter by running the following command:
+
[source,terminal]
----
$ oc get network.operator cluster -o yaml
----

. Inspect the output and confirm that the `reachabilityTotalTimeoutSeconds` parameter is correctly nested under `spec:defaultNetwork:ovnKubernetesConfig:egressIPConfig:` with your intended value:
+
[source,yaml]
----
 # ...
  spec:
    # ...
    defaultNetwork:
      ovnKubernetesConfig:
        egressIPConfig:
          reachabilityTotalTimeoutSeconds: 5
        gatewayConfig:
  # ...
----

// REFERENCE: Describes the parameters (The table of values)
// Module included in the following assembly:
//
// *networking/ovn_kubernetes_network_provider/egressip_failover_assembly.adoc

[id="egressip_failover_reference_{context}"]
= EgressIP failover settings

[role="_abstract"]
The `reachabilityTotalTimeoutSeconds` parameter defines the total time limit in seconds for the platform health check process before a node is declared down.

The following table summarizes the acceptable values and their implications:

[cols="1,1,2a", options="header"]
|===
|Parameter Value (Seconds) |Effect on reachability check |Failover impact and use case
|`0` |Disables the reachability check. |No automatic failover: Use only if an external system handles node health monitoring and failover. The platform will not automatically react to node failures.
|`1 - 60` |Sets the total time limit for reachability probing. |Directly controls detection time: This value defines the lower limit for your overall failover time. A smaller value leads to faster failover but might increase network traffic. Default: 1 second. The maximum accepted integer value is 60.
|===

// Labeling a node to host egress IP addresses
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-node_{context}"]
= Labeling a node to host egress IP addresses

[role="_abstract"]
You can apply the `k8s.ovn.org/egress-assignable=""` label to a node in your cluster so that OpenShift Container Platform can assign one or more egress IP addresses to the node.

.Prerequisites

* You installed the {oc-first}.
* You installed the ROSA CLI (`rosa`).
* You logged in to the cluster as a cluster administrator.

.Procedure

* To label a node so that it can host one or more egress IP addresses, enter the following command:
+
[source,terminal]
----
$ oc label nodes <node_name> k8s.ovn.org/egress-assignable=""
----
+
`<node_name>`:: Specifies the name of the node to label.
+
[TIP]
====
You can alternatively apply the following YAML to add the label to a node:

[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  labels:
    k8s.ovn.org/egress-assignable: ""
  name: <node_name>
----
====
[source,terminal]
----
$ rosa edit machinepool <machinepool_name> --cluster=<cluster_name> --labels "k8s.ovn.org/egress-assignable="
----
+
[IMPORTANT]
====
This command replaces any existing node labels on your machinepool. You should include any of the desired labels to the `--labels` field to ensure that your existing node labels persist.
====

// Configuring dual-stack networking for an EgressIP object
// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-egress-ips-ovn.adoc

[id="nw-egress-ips-object-dual-stack_{context}"]
= Configuring dual-stack networking for an EgressIP object

[role="_abstract"]
For a cluster configured for dual-stack networking, you can apply dual-stack networking to a single `EgressIP` object. The `EgressIP` object can then extend dual-stack networking capabilities to a pod.

[IMPORTANT]
====
KNOWN ISSUE FROM https://issues.redhat.com/browse/OCPBUGS-61833
====

[IMPORTANT]
====
Red{nbsp}Hat does not support creating two `EgressIP` objects to represent dual-stack networking capabilities. For example, specifying IPv4 addresses with one object and using another object to specify IPv6 addresses. This configuration limit impacts address-type assignments to pods.
====

.Prerequisites

* You created two egress nodes so that an `EgressIP` object can allocate IPv4 addresses to one node and IPv6 addresses to the other node. For more information, see "Assignment of egress IP addresses to nodes".

.Procedure

* Create an `EgressIP` object and configure IPv4 and IPv6 addresses for the object. The following example `EgressIP` object uses selectors to identify which pods use the specified egress IP addresses for their outbound traffic:
+
[source,yaml]
----
kind: EgressIP
metadata:
  name: egressip-dual
spec:
  egressIPs:
    - 192.168.118.30
    - 2600:52:7:94::30
  namespaceSelector:
    matchLabels:
      env: qa
  podSelector:
    matchLabels:
      egressip: ds
# ...
----

.Verification

. Create a `Pod` manifest file to test and validate your `EgressIP` object. The pod serves as a client workload that sends outbound traffic to verify that your `EgressIP` policy works as expected.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: ubi-egressip-pod
  namespace: test
  labels:
    egressip: ds
spec:
  containers:
  - name: fedora-curl
    image: registry.redhat.io/ubi9/ubi
    command: ["/bin/bash", "-c", "sleep infinity"]
# ...
----
+
--
where:

`<labels>`:: Sets custom identifiers so that the `EgressIP` object can use these labels to apply egress IP address to target pods.
--

. Run a `curl` request from inside a pod to an external server. This action verifies that outbound traffic correctly uses an address that you specified in the `EgressIP` object.
+
[source,terminal]
----
$ curl <ipv_address>
----
+
--
where:

`<ipv_address>`:: Depending on the `EgressIP` object, enter an IPv4 or IPv6 address.
--

[role="_additional-resources"]
== Additional resources

* LabelSelector meta/v1
* LabelSelectorRequirement meta/v1
* LabelSelector meta/v1
* LabelSelectorRequirement meta/v1
