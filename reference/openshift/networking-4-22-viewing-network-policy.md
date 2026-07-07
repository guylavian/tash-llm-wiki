---
title: "Viewing a network policy"
type: reference
domain: openshift
slug: networking-4-22-viewing-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/viewing-network-policy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Viewing a network policy

[id="viewing-network-policy"]
= Viewing a network policy

[role="_abstract"]
As a cluster administrator, you can view a network policy for a namespace.

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/creating-network-policy.adoc
// * networking/network_security/network_policy/viewing-network-policy.adoc
// * networking/network_security/network_policy/editing-network-policy.adoc
// * post_installation_configuration/network-configuration.adoc
// * microshift_networking/microshift-creating-network-policy.adoc
// * microshift_networking/microshift-network-policy/microshift-editing-network-policy.adoc

[id="nw-networkpolicy-object_{context}"]
= Example NetworkPolicy object

[role="_abstract"]
Reference the example `NetworkPolicy` object to understand how to configure this object.

[source,yaml]
----
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-27107
spec:
  podSelector:
    matchLabels:
      app: mongodb
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: app
    ports:
    - protocol: TCP
      port: 27017
----

where:

`name`:: The name of the NetworkPolicy object.
`spec.podSelector`:: A selector that describes the pods to which the policy applies.
The policy object can only select pods in the project that defines the NetworkPolicy object.
`ingress.from.podSelector`:: A selector that matches the pods from which the policy object allows ingress traffic. The selector matches pods in the same namespace as the NetworkPolicy.
`ingress.ports`:: A list of one or more destination ports on which to accept traffic.

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
// * networking/network_security/network_policy/viewing-network-policy.adoc

[id="nw-networkpolicy-view-ocm_{context}"]
= Viewing network policies using {cluster-manager}

[role="_abstract"]
You can view the configuration details of your network policy in {cluster-manager-first}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You created a OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.
* You added your user account to the configured identity provider.
* You created a network policy.

.Procedure

. From the *Administrator* perspective in the {cluster-manager} web console, under *Networking*, click *`NetworkPolicies`*.

. Select the required network policy to view.

. In the *Network Policy* details page, you can view all of the associated ingress and egress rules.

. Select *YAML* on the network policy details to view the policy configuration in YAML format.
+
[NOTE]
====
You can only view the details of these policies. You cannot edit these policies.
====
