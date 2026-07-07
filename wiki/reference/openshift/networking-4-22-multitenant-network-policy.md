---
title: "Configuring multitenant isolation with network policy"
type: reference
domain: openshift
slug: networking-4-22-multitenant-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/multitenant-network-policy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring multitenant isolation with network policy

[id="multitenant-network-policy"]
= Configuring multitenant isolation with network policy

[role="_abstract"]
You can configure network policies to isolate network traffic between projects in a multitenant cluster. This isolation helps prevent unauthorized communication between workloads in different namespaces.

//TODO OSDOCS-11830 should this not be done with adminnetworkpolicy now?
As a cluster administrator, you can configure your network policies to provide multitenant network isolation.

[NOTE]
====
Configuring network policies as described in this section provides network isolation similar to the multitenant mode of OpenShift SDN in previous versions of OpenShift Container Platform.
====

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/multitenant-network-policy.adoc

[id="nw-networkpolicy-multitenant-isolation_{context}"]
= Configuring multitenant isolation by using network policy

[role="_abstract"]
You can configure network policies to isolate workloads in a project from pods and services in other namespaces. This isolation helps control network traffic between projects and improves multitenant security in your cluster.

.Prerequisites

* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.
* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `admin` privileges.

.Procedure

. Create the following `NetworkPolicy` objects:
.. A policy named `allow-from-openshift-ingress`.
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-ingress
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          policy-group.network.openshift.io/ingress: ""
  podSelector: {}
  policyTypes:
  - Ingress
EOF
----
+
[NOTE]
====
`policy-group.network.openshift.io/ingress: ""` is the preferred namespace selector label for OVN-Kubernetes.
====
.. A policy named `allow-from-openshift-monitoring`:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-monitoring
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          network.openshift.io/policy-group: monitoring
  podSelector: {}
  policyTypes:
  - Ingress
EOF
----

.. A policy named `allow-same-namespace`:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-same-namespace
spec:
  podSelector:
  ingress:
  - from:
    - podSelector: {}
EOF
----

.. A policy named `allow-from-kube-apiserver-operator`:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-kube-apiserver-operator
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-kube-apiserver-operator
      podSelector:
        matchLabels:
          app: kube-apiserver-operator
  policyTypes:
  - Ingress
EOF
----
+
For more details, see New `kube-apiserver-operator` webhook controller validating health of webhook.

. Optional: To confirm that the network policies exist in your current project, enter the following command:
+
[source,terminal]
----
$ oc describe networkpolicy
----
+
.Example output
[source,text]
----
Name:         allow-from-openshift-ingress
Namespace:    example1
Created on:   2020-06-09 00:28:17 -0400 EDT
Labels:       <none>
Annotations:  <none>
Spec:
  PodSelector:     <none> (Allowing the specific traffic to all pods in this namespace)
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      NamespaceSelector: policy-group.network.openshift.io/ingress:
  Not affecting egress traffic
  Policy Types: Ingress

Name:         allow-from-openshift-monitoring
Namespace:    example1
Created on:   2020-06-09 00:29:57 -0400 EDT
Labels:       <none>
Annotations:  <none>
Spec:
  PodSelector:     <none> (Allowing the specific traffic to all pods in this namespace)
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      NamespaceSelector: network.openshift.io/policy-group: monitoring
  Not affecting egress traffic
  Policy Types: Ingress
----

[id="multitenant-network-policy-additional-resources"]
== Additional resources

* Defining a default network policy for a project
