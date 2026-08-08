---
title: "Configure an external gateway on the default network"
type: reference
domain: openshift
slug: networking-4-22-configuring-secondary-external-gateway
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-secondary-external-gateway
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configure an external gateway on the default network

[id="configuring-secondary-external-gateway"]
= Configure an external gateway on the default network

[role="_abstract"]
As a cluster administrator, you can configure an external gateway on the default network.

This feature offers the following benefits:

- Granular control over egress traffic on a per-namespace basis
- Flexible configuration of static and dynamic external gateway IP addresses
- Support for both IPv4 and IPv6 address families

[id="{context}_prerequisites"]
== Prerequisites

* Your cluster uses the OVN-Kubernetes network plugin.
* Your infrastructure is configured to route traffic from the secondary external gateway.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-secondary-external-gateway.adoc

[id="nw-secondary-ext-gw-about_{context}"]
= How OpenShift Container Platform determines the external gateway IP address

[role="_abstract"]
You configure a secondary external gateway with the `AdminPolicyBasedExternalRoute` custom resource (CR) from the `k8s.ovn.org` API group. The CR supports static and dynamic approaches for specifying an IP address for an external gateway.

Each namespace that an `AdminPolicyBasedExternalRoute` CR targets cannot be selected by any other `AdminPolicyBasedExternalRoute` CR. A namespace cannot have concurrent secondary external gateways.

Changes to policies are isolated in the controller. If a policy fails to apply, changes to other policies do not trigger a retry of other policies. Policies are re-evaluated when updates occur to the policy or to related objects such as target namespaces, pod gateways, or the namespaces that host them from dynamic hops. When re-evaluated, the policy applies any differences from the changes.

Static assignment:: You specify an IP address directly.
Dynamic assignment:: You specify an IP address indirectly, with namespace and pod selectors, and an optional network attachment definition.

[IMPORTANT]
====
If the name of a network attachment definition is provided, the external gateway IP address of the network attachment is used.

If the name of a network attachment definition is not provided, the external gateway IP address for the pod itself is used. However, this approach works only if the pod is configured with `hostNetwork` set to `true`.
====

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-secondary-external-gateway.adoc

[id="nw-secondary-ext-gw-object_{context}"]
= AdminPolicyBasedExternalRoute object configuration

[role="_abstract"]
You can define an `AdminPolicyBasedExternalRoute` object, which is cluster scoped, with specific properties.

A namespace can be selected by only one `AdminPolicyBasedExternalRoute` CR at a time.

The following tables detail supported fields for objects.

.`AdminPolicyBasedExternalRoute` object
[cols=".^3,.^2,.^5a",options="header"]

|====
|Field|Type|Description

|`metadata.name`
|`string`
|Specifies the name of the  `AdminPolicyBasedExternalRoute` object.

|`spec.from`
|`string`
|Specifies a namespace selector that the routing policies apply to. Only `namespaceSelector` is supported for external traffic. For example:

[source,yaml]
----
from:
  namespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059
----

A namespace can only be targeted by one `AdminPolicyBasedExternalRoute` CR. If a namespace is selected by more than one `AdminPolicyBasedExternalRoute` CR, a `failed` error status occurs on the second and subsequent CRs that target the same namespace. To apply updates, you must change the policy itself or related objects such as target namespaces, pod gateways, or namespaces hosting them from dynamic hops. The policy is then re-evaluated and your changes are applied.

|`spec.nextHops`
|`object`
| Specifies the destinations where the packets are forwarded to. Must be either or both of `static` and `dynamic`. You must have at least one next hop defined.

|====

.`nextHops` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`static`
|`array`
| Specifies an array of static IP addresses.

|`dynamic`
|`array`
| Specifies an array of pod selectors corresponding to pods configured with a network attachment definition to use as the external gateway target.

|====

.`nextHops.static` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`ip`
|`string`
| Specifies either an IPv4 or IPv6 address of the next destination hop.

|`bfdEnabled`
|`boolean`
|Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`.

|====

.`nextHops.dynamic` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`podSelector`
|`string`
|Specifies a set-based label selector to filter the pods in the namespace that match this network configuration. For more information, see "Set-based requirement" in the _Additional resources_ section.

|`namespaceSelector`
|`string`
|Specifies a `set-based` selector to filter the namespaces that the `podSelector` applies to. You must specify a value for this field.

|`bfdEnabled`
|`boolean`
|Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`.

|`networkAttachmentName`
|`string`
|Optional field. Specifies the name of a network attachment definition. The name must match the list of logical networks associated with the pod. If this field is not specified, the host network of the pod is used. However, the pod must be configured as a host network pod to use the host network.

|====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Set-based requirement (Kubernetes)

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-secondary-external-gateway.adoc

[id="example-secondary-external-gateway-configurations_{context}"]
= Example secondary external gateway configurations

[role="_abstract"]
Reference the `AdminPolicyBasedExternalRoute` objects to better understand secondary external gateway configurations.

In the following example, the `AdminPolicyBasedExternalRoute` object configures two static IP addresses as external gateways for pods in namespaces with the `kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059` label:

[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: default-route-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
# ...
----

In the following example, the `AdminPolicyBasedExternalRoute` object configures a dynamic external gateway. The IP addresses used for the external gateway are derived from the additional network attachments associated with each of the selected pods.

[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: shadow-traffic-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        externalTraffic: ""
  nextHops:
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          shadowTraffic: ""
      networkAttachmentName: shadow-gateway
    - podSelector:
        matchLabels:
          gigabyteGW: ""
      namespaceSelector:
        matchLabels:
          gatewayNamespace: ""
      networkAttachmentName: gateway
# ...
----

In the following example, the `AdminPolicyBasedExternalRoute` object configures both static and dynamic external gateways:

[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: multi-hop-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        trafficType: "egress"
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          egressTraffic: ""
      networkAttachmentName: gigabyte
# ...
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-secondary-external-gateway.adoc

[id="nw-secondary-ext-gw-configure_{context}"]
= Configure a secondary external gateway

[role="_abstract"]
You can configure an external gateway on the default network for a namespace in your cluster.

.Prerequisites

* You installed the {oc-first}.
* You are logged in to the cluster with a user with `cluster-admin` privileges.

.Procedure

. Create a YAML file that contains an `AdminPolicyBasedExternalRoute` object. For more information, see "AdminPolicyBasedExternalRoute object configuration".

. To create an admin policy based external route, enter the following command:
+
[source,terminal]
----
$ oc create -f <file>.yaml
----
+
** `<file>`: Specifies the name of the YAML file that you created in a previous step.
+
.Example output
[source,text]
----
adminpolicybasedexternalroute.k8s.ovn.org/default-route-policy created
----

. To confirm that the admin policy based external route was created, enter the following command:
+
[source,terminal]
----
$ oc describe apbexternalroute <name> | tail -n 6
----
+
** `<name>`: Specifies the name of the `AdminPolicyBasedExternalRoute` object.
+
.Example output
[source,text]
----
Status:
  Last Transition Time:  2023-04-24T15:09:01Z
  Messages:
  Configured external gateway IPs: 172.18.0.8
  Status:  Success
Events:  <none>
----

.Verification

If you created an `AdminPolicyBasedExternalRoute` object that selects a host-network pod IP address as the secondary external gateway, you can confirm that the next hop is correct for a pod with the following steps:

. To get the IP address of the pod, enter the following command:
+
[source,terminal]
----
oc get pods/<pod_name> -n <namespace> -o wide
----
+
--
where:

`<pod_name>`:: Specifies the name of the pod.
`<namespace>`:: Specifies the namespace of the pod.
--
+
.Example output
[source,text]
----
NAMESPACE  NAME   READY   STATUS      RESTARTS      AGE   IP            NODE      NOMINATED NODE   READINESS GATES
ns1        pod1   1/1     Running     1 (37m ago)   41m   10.130.0.8    node1     <none>           <none>
----

. Confirm that the IP address from the previous step is available as an external gateway.

.. To find the OVN-Kubernetes control plane pod that manages the next hop for the pod, enter the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-ovn-kubernetes \
  --field-selector spec.nodeName=<node_name> \
  -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}' | \
    grep ovnkube-node-
----
+
--
where:

`<node_name>`:: Specifies the name of the node from the `NODE` column that the pod from the previous step is running on.
--
+
.Example output
[source,text]
----
ovnkube-node-rpt55
----

.. To confirm that the OVN-Kubernetes node pod includes the correct next hop, enter the following command:
+
[source,terminal]
----
$ oc exec -t <pod_name> -n openshift-ovn-kubernetes  -c nbdb \
    -- ovn-nbctl lr-route-list GR_ovn-work | grep <pod_ip> -A 6 -B 4

oc exec -ti <pod_name> -n openshift-ovn-kubernetes -c nbdb -- ovn-nbctl lr-route-list GR_<node_name> | grep <pod_id> -A6 -B4
----
+
--
where:

`<pod_name>`:: Specifies the name of the OVN-Kubernetes node pod from the previous step.
`<node_name>`:: Specifies the name of the cluster node that the OVN-Kubernetes node pod is running on.
`<pod_ip>`:: Specifies the name of the pod IP address.
--
+
.Example output
[source,text]
----
IPv4 Routes
Route Table

:
10.128.2.206 172.18.0.10 src-ip rtoe-GR_worker-0-1 ecmp-symmetric-reply bfd
10.128.3.229 172.18.0.10 src-ip rtoe-GR_worker-0-1 ecmp-symmetric-reply bfd
169.254.169.0/29 169.254.169.4 dst-ip rtoe-GR_worker-0-1
10.128.0.0/14 100.64.0.1 dst-ip
0.0.0.0/0 192.168.123.1 dst-ip rtoe-GR_worker-0-1
----

[role="_additional-resources"]
== Additional resources
* Understanding multiple networks
