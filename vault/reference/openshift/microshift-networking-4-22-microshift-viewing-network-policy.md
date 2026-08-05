---
title: "Viewing a network policy"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-viewing-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-viewing-network-policy
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Viewing a network policy

[id="microshift-viewing-network-policy"]
= Viewing a network policy

[role="_abstract"]
Use the following procedure to view a network policy for a namespace.

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
