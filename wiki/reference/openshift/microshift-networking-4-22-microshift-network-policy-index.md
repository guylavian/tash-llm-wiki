---
title: "About network policies"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-network-policy-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-network-policy-index
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# About network policies

[id="microshift-network-policies"]
= About network policies

[role="_abstract"]
Learn how network policies work for {microshift-short} to restrict or allow network traffic to pods in your node.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-network-policies.adoc

[id="microshift-nw-network-policy-intro_{context}"]
= How network policy works in {microshift-short}

[role="_abstract"]
In a node that is using the default OVN-Kubernetes Container Network Interface (CNI) plugin for {microshift-short}, network isolation is controlled by both firewalld, which is configured on the host, and by `NetworkPolicy` objects created within {microshift-short}. Simultaneous use of firewalld and `NetworkPolicy` is supported.

* Network policies work only within boundaries of OVN-Kubernetes-controlled traffic, so they can apply to every situation except for `hostPort/hostNetwork` enabled pods.

* Firewalld settings also do not apply to `hostPort/hostNetwork` enabled pods.

* Firewalld rules run before any `NetworkPolicy` is enforced.

[WARNING]
====
Network policy does not apply to the host network namespace. Pods with host networking enabled are unaffected by network policy rules. However, pods connecting to the host-networked pods might be affected by the network policy rules.

Network policies cannot block traffic from localhost.
====

By default, all pods in a {microshift-short} node are accessible from other pods and network endpoints. To isolate one or more pods in a node, you can create `NetworkPolicy` objects to indicate allowed incoming connections. You can create and delete `NetworkPolicy` objects.

If a pod is matched by selectors in one or more `NetworkPolicy` objects, then the pod accepts only connections that are allowed by at least one of those `NetworkPolicy` objects. A pod that is not selected by any `NetworkPolicy` objects is fully accessible.

A network policy applies to only the TCP, UDP, ICMP, and SCTP protocols. Other protocols are not affected.

The following example `NetworkPolicy` objects demonstrate supporting different scenarios:

* Deny all traffic:
+
To make a project deny by default, add a `NetworkPolicy` object that matches all pods but accepts no traffic:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: deny-by-default
spec:
  podSelector: {}
  ingress: []
----

* Allow connections from the default router, which is the ingress in {microshift-short}:
+
To allow connections from the {microshift-short} default router, add the following `NetworkPolicy` object:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-ingress
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          ingresscontroller.operator.openshift.io/deployment-ingresscontroller: default
  podSelector: {}
  policyTypes:
  - Ingress
----

* Only accept connections from pods within the same namespace:
+
To make pods accept connections from other pods in the same namespace, but reject all other connections from pods in other namespaces, add the following `NetworkPolicy` object:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-same-namespace
spec:
  podSelector: {}
  ingress:
  - from:
    - podSelector: {}
----

* Only allow HTTP and HTTPS traffic based on pod labels:
+
To enable only HTTP and HTTPS access to the pods with a specific label (`role=frontend` in following example), add a `NetworkPolicy` object similar to the following:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-http-and-https
spec:
  podSelector:
    matchLabels:
      role: frontend
  ingress:
  - ports:
    - protocol: TCP
      port: 80
    - protocol: TCP
      port: 443
----

* Accept connections by using both namespace and pod selectors:
+
To match network traffic by combining namespace and pod selectors, you can use a `NetworkPolicy` object similar to the following:
+
[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-pod-and-namespace-both
spec:
  podSelector:
    matchLabels:
      name: test-pods
  ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            project: project_name
        podSelector:
          matchLabels:
            name: test-pods
----

`NetworkPolicy` objects are additive, which means you can combine multiple `NetworkPolicy` objects together to satisfy complex network requirements.

For example, for the `NetworkPolicy` objects defined in previous examples, you can define both `allow-same-namespace` and `allow-http-and-https` policies. That configuration allows the pods with the label `role=frontend` to accept any connection allowed by each policy. That is, connections on any port from pods in the same namespace, and connections on ports `80` and `443` from pods in any namespace.

//OCP module, edit with conditionals
// Module included in the following assemblies:
//
// * networking/network_security/network_policy/about-network-policy.adoc

[id="nw-networkpolicy-optimize-ovn_{context}"]
= Optimizations for network policy with OVN-Kubernetes network plugin

[role="_abstract"]
Learn how to optimize OVN-Kubernetes network policies to reduce flow count and ensure external IP traffic is allowed when needed.

When designing your network policy, refer to the following guidelines:

* For network policies with the same `spec.podSelector` spec, it is more efficient to use one network policy with multiple `ingress` or `egress` rules, than multiple network policies with subsets of `ingress` or `egress` rules.
// TODO OSDOCS=11830 Why? Because each policy has to spin up its own resources?

* Every `ingress` or `egress` rule based on the `podSelector` or `namespaceSelector` spec generates the number of OVS flows proportional to `number of pods selected by network policy + number of pods selected by ingress or egress rule`. Therefore, it is preferable to use the `podSelector` or `namespaceSelector` spec that can select as many pods as you need in one rule, instead of creating individual rules for every pod.
+
For example, the following policy contains two rules:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
spec:
  podSelector: {}
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
  - from:
    - podSelector:
        matchLabels:
          role: backend
----
+
The following policy expresses those same two rules as one:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
spec:
  podSelector: {}
  ingress:
  - from:
    - podSelector:
        matchExpressions:
        - {key: role, operator: In, values: [frontend, backend]}
----
+
The same guideline applies to the `spec.podSelector` spec. If you have the same `ingress` or `egress` rules for different network policies, it might be more efficient to create one network policy with a common `spec.podSelector` spec. For example, the following two policies have different rules:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: policy1
spec:
  podSelector:
    matchLabels:
      role: db
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: policy2
spec:
  podSelector:
    matchLabels:
      role: client
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
----
+
The following network policy expresses those same two rules as one:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: policy3
spec:
  podSelector:
    matchExpressions:
    - {key: role, operator: In, values: [db, client]}
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
----
+
You can apply this optimization when only multiple selectors are expressed as one. In cases where selectors are based on different labels, it may not be possible to apply this optimization. In those cases, consider applying some new labels for network policy optimization specifically.

[id="nw-networkpolicy-external-ip-ovn_{context}"]
== NetworkPolicy CR and external IPs in OVN-Kubernetes

In OVN-Kubernetes, the `NetworkPolicy` custom resource (CR) enforces strict isolation rules. If a service is exposed using an external IP, a network policy can block access from other namespaces unless explicitly configured to allow traffic.

To allow access to external IPs across namespaces, create a `NetworkPolicy` CR that explicitly permits ingress from the required namespaces and ensures traffic is allowed to the designated service ports. Without allowing traffic to the required ports, access might still be restricted.

.Example output
[source,yaml]
----
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    annotations:
    name: <policy_name>
    namespace: openshift-ingress
  spec:
    ingress:
    - ports:
      - port: 80
        protocol: TCP
    - ports:
      - port: 443
        protocol: TCP
    - from:
      - namespaceSelector:
          matchLabels:
          kubernetes.io/metadata.name: <my_namespace>
    podSelector: {}
    policyTypes:
    - Ingress
----
where:

`<policy_name>`:: Specifies your name for the policy.
`<my_namespace>`:: Specifies the name of the namespace where the policy is deployed.

For more details, see "About network policy".
