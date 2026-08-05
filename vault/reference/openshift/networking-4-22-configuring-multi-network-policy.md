---
title: "Configuring multi-network policy"
type: reference
domain: openshift
slug: networking-4-22-configuring-multi-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-multi-network-policy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring multi-network policy

[id="configuring-multi-network-policy"]
= Configuring multi-network policy

[role="_abstract"]
As an administrator, you can use the `MultiNetworkPolicy` API to create multiple network policies that manage traffic for pods that are attached to secondary networks. For example, you can create policies that allow or deny traffic based on specific ports, IPs and ranges, or labels.

Multi-network policies can be used to manage traffic on secondary networks in the cluster. These policies cannot manage the default cluster network or primary network of user-defined networks.

As a cluster administrator, you can configure a multi-network policy for any of the following network types:

* Single-Root I/O Virtualization (SR-IOV)
* MAC Virtual Local Area Network (MacVLAN)
* IP Virtual Local Area Network (IPVLAN)
* Bond Container Network Interface (CNI) over SR-IOV
* OVN-Kubernetes secondary networks

[NOTE]
====
Support for configuring multi-network policies for SR-IOV secondary networks is only supported with kernel network interface controllers (NICs). SR-IOV is not supported for Data Plane Development Kit (DPDK) applications.
====

[IMPORTANT]
====
In OpenShift Container Platform 4.22 and later, the multi-network policy backend uses `nftables`.
The `iptables` backend has been removed and there is no option to revert to it.
The `MultiNetworkPolicy` API and user-facing configuration are unchanged.
====

// Module included in the following assemblies:
//
// * networking/multiple_networks/secondary_networks/configuring-multi-network-policy.adoc

[id="nw-multi-network-policy-differences_{context}"]
= Differences between multi-network policy and network policy

[role="_abstract"]
Although the `MultiNetworkPolicy` API implements the `NetworkPolicy` API, ensure that you understand the following key differences between the two policies:

* You must use the `MultiNetworkPolicy` API, as demonstrated in the following example configuration:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
# ...
----

* You must use the `multi-networkpolicy` resource name when using the CLI to interact with multi-network policies. For example, you can view a multi-network policy object with the `oc get multi-networkpolicy <name>` command where `<name>` is the name of a multi-network policy.

* You can use the `k8s.v1.cni.cncf.io/policy-for` annotation on a `MultiNetworkPolicy` object to point to a `NetworkAttachmentDefinition` (NAD) custom resource (CR). The NAD CR defines the network to which the policy applies. The following example multi-network policy includes the `k8s.v1.cni.cncf.io/policy-for` annotation:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
# ...
----
+
where:
+
`<namespace_name>`:: Specifies the namespace name.
`<network_name>`:: Specifies the name of a network attachment definition.

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc

[id="nw-multi-network-policy-enable_{context}"]
= Enabling multi-network policy for the cluster

[role="_abstract"]
As a cluster administrator, you can enable multi-network policy support on your cluster.

.Prerequisites

* Install the {oc-first}.
* Log in to the cluster with a user with `cluster-admin` privileges.

.Procedure

. Create the `multinetwork-enable-patch.yaml` file with the following YAML:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  useMultiNetworkPolicy: true
# ...
----

. Configure the cluster to enable multi-network policy. Successful output lists the name of the policy object and the `patched` status.
+
[source,terminal]
----
$ oc patch network.operator.openshift.io cluster --type=merge --patch-file=multinetwork-enable-patch.yaml
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/secondary_networks/configuring-multi-network-policy.adoc

[id="nw-multi-network-policy-ipv6-support_{context}"]
= Supporting multi-network policies in IPv6 networks

[role="_abstract"]
The ICMPv6 Neighbor Discovery Protocol (NDP) is a set of messages and processes that enable devices to discover and maintain information about neighboring nodes. NDP is essential in IPv6 networks, facilitating the interaction between devices on the same link.

The Cluster Network Operator (CNO) deploys the `nftables` implementation of multi-network policy when the `useMultiNetworkPolicy` parameter is set to `true`.

To support multi-network policies in IPv6 networks, the Cluster Network Operator deploys the following predefined `nftables` rules in every pod affected by a multi-network policy. The CNO automatically creates and manages the following `ConfigMap`. You do not need to create this resource.

[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: multi-networkpolicy-custom-rules
  namespace: openshift-multus
data:
  custom-v6-rules.txt: |
    # accept NDP
    icmpv6 type nd-neighbor-solicit accept
    icmpv6 type nd-neighbor-advert accept
    # accept RA/RS
    icmpv6 type nd-router-advert accept
    icmpv6 type nd-router-solicit accept
----

where:

`icmpv6 type nd-neighbor-solicit`:: This rule allows incoming ICMPv6 neighbor solicitation messages, which are part of the Neighbor Discovery Protocol (NDP). These messages help determine the link-layer addresses of neighboring nodes. In a multi-network setup, this allows other pods or the secondary interface gateway to resolve the pod's MAC address. Without this, the pod becomes 'invisible' to its neighbors on the secondary network.
`icmpv6 type nd-neighbor-advert`:: This rule allows incoming ICMPv6 neighbor advertisement messages, which are part of NDP and provide information about the link-layer address of the sender. This ensures the pod can receive MAC address updates from other nodes.
`icmpv6 type nd-router-advert`:: This rule allows incoming ICMPv6 router advertisement messages, which provide configuration information to hosts. This allows the pod to receive its default gateway and routing prefix dynamically from the network infrastructure.
`icmpv6 type nd-router-solicit`:: This rule allows incoming ICMPv6 router solicitation messages. Hosts use these messages to request router configuration information. This ensures that when a pod's interface comes online, it can immediately request network parameters rather than waiting for the next scheduled broadcast, reducing container startup latency.

[NOTE]
====
You cannot edit the predefined rules.
====

The rules collectively enable essential ICMPv6 traffic for correct network functioning, including address resolution and router communication in an IPv6 environment. With these rules in place and a multi-network policy denying traffic, applications are not expected to experience connectivity issues.

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc

[id="working-with-multi-network-policy_{context}"]
= Working with multi-network policy

[role="_abstract"]
To manage network traffic isolation and security for pods on secondary networks, you can create, edit, view, and delete multi-network policies. Before you work with multi-network policies, you must enable multi-network policy support for your cluster.

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_security/network_policy/creating-network-policy.adoc
// * post_installation_configuration/network-configuration.adoc
// * microshift_networking/microshift-creating-network-policy.adoc

[id="nw-networkpolicy-create-cli_{context}"]
= Creating a {name} policy using the CLI

[role="_abstract"]
To define granular rules describing ingress or egress network traffic allowed for namespaces in your cluster, you can create a {name} policy.

[NOTE]
====
If you log in with a user with the `cluster-admin` role, then you can create a network policy in any namespace in the cluster.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

.Procedure

. Create a policy rule.
+
.. Create a `<policy_name>.yaml` file:
+
[source,terminal]
----
$ touch <policy_name>.yaml
----
+
where:
+
`<policy_name>`:: Specifies the {name} policy file name.
+
.. Define a {name} policy in the created file. The following example denies ingress traffic from all pods in all namespaces. This is a fundamental policy, blocking all cross-pod networking other than cross-pod traffic allowed by the configuration of other Network Policies.
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress: []
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: deny-by-default
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress: []
----
+
where:
+
`<network_name>`:: Specifies the name of a network attachment definition.
+
The following example configuration allows ingress traffic  from all pods in the same namespace:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-same-namespace
spec:
  podSelector:
  ingress:
  - from:
    - podSelector: {}
# ...
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: allow-same-namespace
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector:
  ingress:
  - from:
    - podSelector: {}
# ...
----
+
where:
+
`<network_name>`:: Specifies the name of a network attachment definition.
+
The following example allows ingress traffic to one pod from a particular namespace. This policy allows traffic to pods that have the `pod-a` label from pods running in `namespace-y`.
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-traffic-pod
spec:
  podSelector:
   matchLabels:
      pod: pod-a
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
           kubernetes.io/metadata.name: namespace-y
# ...
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: allow-traffic-pod
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector:
   matchLabels:
      pod: pod-a
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
           kubernetes.io/metadata.name: namespace-y
# ...
----
+
where:
+
`<network_name>`:: Specifies the name of a network attachment definition.
+
The following example configuration restricts traffic to a service. This policy when applied ensures every pod with both labels `app=bookstore` and `role=api` can only be accessed by pods with label `app=bookstore`. In this example the application could be a REST API server, marked with labels `app=bookstore` and `role=api`.
+
This example configuration addresses the following use cases:
+
* Restricting the traffic to a service to only the other microservices that need to use it.
* Restricting the connections to a database to only permit the application using it.
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: api-allow
spec:
  podSelector:
    matchLabels:
      app: bookstore
      role: api
  ingress:
  - from:
      - podSelector:
          matchLabels:
            app: bookstore
# ...
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: api-allow
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector:
    matchLabels:
      app: bookstore
      role: api
  ingress:
  - from:
      - podSelector:
          matchLabels:
            app: bookstore
# ...
----
+
where:
+
`<network_name>`:: Specifies the name of a network attachment definition.

. To create the {name} policy object, enter the following command. Successful output lists the name of the policy object and the `created` status.
+
[source,terminal]
----
$ oc apply -f <policy_name>.yaml -n <namespace>
----
+
--
where:

`<policy_name>`:: Specifies the {name} policy file name.
`<namespace>`:: Optional parameter. If you defined the object in a different namespace than the current namespace, the parameter specifices the namespace.
--
+
Successful output lists the name of the policy object and the `created` status.

+
[NOTE]
====
If you log in to the web console with `cluster-admin` privileges, you have a choice of creating a network policy in any namespace in the cluster directly in YAML or from a form in the web console.
====

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/editing-network-policy.adoc
// * microshift_networking/microshift-network-policy/microshift-editing-network-policy.adoc

[id="nw-networkpolicy-edit_{context}"]
= Editing a {name} policy

[role="_abstract"]
To modify existing policy configurations, you can edit a {name} policy in a namespace. Edit policies by modifying the policy file and applying it with `oc apply`, or by using the `oc edit` command directly.

[NOTE]
====
If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster.
====

[NOTE]
====
If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster. In the web console, you can edit policies directly in YAML or by using the *Actions* menu.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You are logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace where the {name} policy exists.

.Procedure

. Optional: To list the {name} policy objects in a namespace, enter the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {name} policy -n <namespace>
----
+
where:
+
`<namespace>`:: Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace.

. Edit the {name} policy object.
+
.. If you saved the {name} policy definition in a file, edit the file and make any necessary changes, and then enter the following command.
+
[source,terminal]
----
$ oc apply -n <namespace> -f <policy_file>.yaml
----
+
where:
+
`<namespace>`:: Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace.
`<policy_file>`:: Specifies the name of the file containing the network policy.
+
.. If you need to update the {name} policy object directly, enter the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {name} policy <policy_name> -n <namespace>
----
+
where:
+
`<policy_name>`:: Specifies the name of the network policy.
`<namespace>`:: Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace.

. Confirm that the {name} policy object is updated.
+
[source,terminal,subs="attributes+"]
----
$ oc describe {name}policy <policy_name> -n <namespace>
----
+
where:
+
`<policy_name>`:: Specifies the name of the {name} policy.
`<namespace>`:: Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace.

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/viewing-network-policy.adoc
// * post_installation_configuration/network-configuration.adoc
// * networking/multiple_networks/configuring-multi-network-policy.adoc

[id="nw-networkpolicy-view-cli_{context}"]
= Viewing {name} policies using the CLI

[role="_abstract"]
You can examine the {name} policies in a namespace.

[NOTE]
====
If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster.
====

[NOTE]
====
If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster. In the web console, you can edit policies directly in YAML or by using the *Actions* menu.
====

.Prerequisites

* You installed the {oc-first}.
* You are logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace where the {name} policy exists.

.Procedure

. List {name} policies in a namespace.
+
.. To view {name} policy objects defined in a namespace enter the following
command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {name}policy
----
+
.. Optional: To examine a specific {name} policy enter the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc describe {name}policy <policy_name> -n <namespace>
----
+
where:
+
`<policy_name>`:: Specifies the name of the {name} policy to inspect.
`<namespace>`:: Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace.
+
[source,terminal]
----
$ oc describe networkpolicy allow-same-namespace
----
+
[source,text]
----
Name:         allow-same-namespace
Namespace:    ns1
Created on:   2021-05-24 22:28:56 -0400 EDT
Labels:       <none>
Annotations:  <none>
Spec:
  PodSelector:     <none> (Allowing the specific traffic to all pods in this namespace)
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      PodSelector: <none>
  Not affecting egress traffic
  Policy Types: Ingress
----

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/deleting-network-policy.adoc
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * microshift_networking/microshift-network-policy/microshift-editing-network-policy.adoc

[id="nw-networkpolicy-delete-cli_{context}"]
= Deleting a {name} policy using the CLI

[role="_abstract"]
You can delete a {name} policy in a namespace.

[NOTE]
====
If you log in with `cluster-admin` privileges, you can delete network policies in any namespace in the cluster.
====

[NOTE]
====
If you log in with `cluster-admin` privileges, you can delete network policies in any namespace in the cluster. In the web console, you can delete policies directly in YAML or by using the *Actions* menu.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the OpenShift CLI (`oc`).
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace where the {name} policy exists.

.Procedure

* To delete a {name} policy object, enter the following command. Successful output lists the name of the policy object and the `deleted` status.
+
[source,terminal,subs="attributes+"]
----
$ oc delete {name}policy <policy_name> -n <namespace>
----
+
where:
+
`<policy_name>`:: Specifies the name of the {name} policy.
`<namespace>`:: Optional parameter. If you defined the object in a different namespace than the current namespace, the parameter specifices the namespace.

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_security/network_policy/creating-network-policy.adoc
// * microshift_networking/microshift-creating-network-policy.adoc

[id="nw-networkpolicy-deny-all-multi-network-policy_{context}"]
= Creating a default deny all {name} policy

[role="_abstract"]
The default deny all {name} policy blocks all cross-pod networking other than network traffic allowed by the configuration of other deployed network policies and traffic between host-networked pods.

The steps in the procedure enforces a strong deny policy by applying a `deny-by-default` policy in the `my-project` namespace.

[WARNING]
====
Without configuring a `NetworkPolicy` custom resource (CR) that allows traffic communication, the following policy might cause communication problems across your cluster.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

.Procedure

. Create the following YAML that defines a `deny-by-default` policy to deny ingress from all pods in all namespaces. Save the YAML in the `deny-by-default.yaml` file:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: deny-by-default
  namespace: my-project
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress: []
----
+
where:
+
`namespace`:: Specifies the namespace in which to deploy the policy. For example, the `my-project` namespace.
`annotations`:: Specifies the name of namespace project followed by the network attachment definition name.
`podSelector`:: If this field is empty, the configuration matches all the pods. Therefore, the policy applies to all pods in the `my-project` namespace.
`policyTypes`:: Specifies a list of rule types that the `NetworkPolicy` relates to.
`- Ingress`:: Specifies `Ingress` only `policyTypes`.
`ingress`:: Specifies ingress rules. If not specified, all incoming traffic is dropped to all pods.
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: deny-by-default
  namespace: my-project
spec:
  podSelector: {}
  ingress: []
----
+
where:
+
`namespace`:: Specifies the namespace in which to deploy the policy. For example, the `my-project` namespace.
`podSelector`:: If this field is empty, the configuration matches all the pods. Therefore, the policy applies to all pods in the `my-project` namespace.
`ingress`:: Where `[]` indicates that no `ingress` rules are specified. This causes incoming traffic to be dropped to all pods.

. Apply the policy by entering the following command. Successful output lists the name of the policy object and the `created` status.
+
[source,terminal]
----
$ oc apply -f deny-by-default.yaml
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_security/network_policy/creating-network-policy.adoc

[id="nw-networkpolicy-allow-external-clients_{context}"]
= Creating a {name} policy to allow traffic from external clients

[role="_abstract"]
With the `deny-by-default` policy in place you can proceed to configure a policy that allows traffic from external clients to a pod with the label `app=web`.

[NOTE]
====
If you log in with a user with the `cluster-admin` role, then you can create a network policy in any namespace in the cluster.
====
[NOTE]
====
Firewalled rules run before any `NetworkPolicy` is enforced.
====

Follow this procedure to configure a policy that allows external service from the public Internet directly or by using a Load Balancer to access the pod. Traffic is only allowed to a pod with the label `app=web`.

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

.Procedure

. Create a policy that allows traffic from the public Internet directly or by using a load balancer to access the pod. Save the YAML in the `web-allow-external.yaml` file:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
spec:
  policyTypes:
  - Ingress
  podSelector:
    matchLabels:
      app: web
  ingress:
    - {}
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: web-allow-external
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  policyTypes:
  - Ingress
  podSelector:
    matchLabels:
      app: web
  ingress:
    - {}
----

. Apply the policy by entering the following command. Successful output lists the name of the policy object and the `created` status.
+
[source,terminal]
----
$ oc apply -f web-allow-external.yaml
----
+
This policy allows traffic from all resources, including external traffic as illustrated in the following diagram:
+
image::292_OpenShift_Configuring_multi-network_policy_1122.png[Allow traffic from external clients]

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_security/network_policy/creating-network-policy.adoc
// * microshift_networking/microshift-creating-network-policy.adoc

[id="nw-networkpolicy-allow-traffic-from-all-applications_{context}"]
= Creating a {name} policy allowing traffic to an application from all namespaces

[role="_abstract"]
You can configure a policy that allows traffic from all pods in all namespaces to a particular application.

[NOTE]
====
If you log in with a user with the `cluster-admin` role, then you can create a network policy in any namespace in the cluster.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

.Procedure

. Create a policy that allows traffic from all pods in all namespaces to a particular application. Save the YAML in the `web-allow-all-namespaces.yaml` file:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: web-allow-all-namespaces
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector: {}
----
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: web-allow-all-namespaces
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector:
    matchLabels:
     app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector: {}
----
+
where:
+
`app`:: Applies the policy only to `app:web` pods in default namespace.
`namespaceSelector`:: Selects all pods in all namespaces.
+
[NOTE]
====
By default, if you do not specify a `namespaceSelector` parameter in the policy object, no namespaces get selected. This means the policy allows traffic only from the namespace where the network policy deployes.
====

. Apply the policy by entering the following command. Successful output lists the name of the policy object and the `created` status.
+
[source,terminal]
----
$ oc apply -f web-allow-all-namespaces.yaml
----

.Verification

. Start a web service in the `default` namespace by entering the following command:
+
[source,terminal]
----
$ oc run web --namespace=default --image=nginx --labels="app=web" --expose --port=80
----

. Run the following command to deploy an `alpine` image in the `secondary` namespace and to start a shell:
+
[source,terminal]
----
$ oc run test-$RANDOM --namespace=secondary --rm -i -t --image=alpine -- sh
----

. Run the following command in the shell and observe that the service allows the request:
+
[source,terminal]
----
# wget -qO- --timeout=2 http://web.default
----
+
[source,terminal]
----
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
----

// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_security/network_policy/creating-network-policy.adoc
// * microshift_networking/microshift-creating-network-policy.adoc

[id="nw-networkpolicy-allow-traffic-from-a-namespace_{context}"]
= Creating a {name} policy allowing traffic to an application from a namespace

[role="_abstract"]
You can configure a policy that allows traffic to a pod with the label `app=web` from a particular namespace.

This configuration is useful in the following use cases:

* Restrict traffic to a production database only to namespaces that have production workloads deployed.
* Enable monitoring tools deployed to a particular namespace to scrape metrics from the current namespace.

[NOTE]
====
If you log in with a user with the `cluster-admin` role, then you can create a network policy in any namespace in the cluster.
====

.Prerequisites
* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the {oc-first}.
* You logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

[WARNING]
====
Do not apply the `network.openshift.io/policy-group: ingress` label to custom namespace or projects. This label is Operator-managed and reserved for OpenShift Container Platform networking functions. It should not be altered on system-created namespaces.

Using this label can result in intermittent network connectivity drops, unintended application of system `NetworkPolicies` resource, or configuration drift as the operator attempts to reconcile the state. For custom traffic grouping, always use unique, user-defined labels as shown in the following procedure.
====

.Procedure

. Create a policy that allows traffic from all pods in a particular namespaces with a label `purpose=production`. Save the YAML in the `web-allow-prod.yaml` file:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: web-allow-prod
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/policy-for:<namespace_name>/<network_name>
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          purpose: production
----
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: web-allow-prod
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          purpose: production
----
+
where:
+
`app`:: Applies the policy only to `app:web` pods in the default namespace.
`purpose`:: Restricts traffic to only pods in namespaces that have the label `purpose=production`.

. Apply the policy by entering the following command. Successful output lists the name of the policy object and the `created` status.
+
[source,terminal]
----
$ oc apply -f web-allow-prod.yaml
----

.Verification

. Start a web service in the `default` namespace by entering the following command:
+
[source,terminal]
----
$ oc run web --namespace=default --image=nginx --labels="app=web" --expose --port=80
----

. Run the following command to create the `prod` namespace:
+
[source,terminal]
----
$ oc create namespace prod
----

. Run the following command to label the `prod` namespace:
+
[source,terminal]
----
$ oc label namespace/prod purpose=production
----

. Run the following command to create the `dev` namespace:
+
[source,terminal]
----
$ oc create namespace dev
----

. Run the following command to label the `dev` namespace:
+
[source,terminal]
----
$ oc label namespace/dev purpose=testing
----

. Run the following command to deploy an `alpine` image in the `dev` namespace and to start a shell:
+
[source,terminal]
----
$ oc run test-$RANDOM --namespace=dev --rm -i -t --image=alpine -- sh
----

. Run the following command in the shell and observe the reason for the blocked request. For example, expected output states `wget: download timed out`.
+
[source,terminal]
----
# wget -qO- --timeout=2 http://web.default
----

. Run the following command to deploy an `alpine` image in the `prod` namespace and start a shell:
+
[source,terminal]
----
$ oc run test-$RANDOM --namespace=prod --rm -i -t --image=alpine -- sh
----

. Run the following command in the shell and observe that the request is allowed:
+
[source,terminal]
----
# wget -qO- --timeout=2 http://web.default
----
+
[source,terminal]
----
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
----

[id="{context}_additional-resources"]
[role="_additional-resources"]
== Additional resources

* About network policy
* Understanding multiple networks
* Configuring a macvlan network
* Configuring an SR-IOV network device
