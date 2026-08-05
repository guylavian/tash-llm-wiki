---
title: "Deleting a network policy"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-deleting-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-deleting-network-policy
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Deleting a network policy

[id="microshift-deleting-network-policy"]
= Deleting a network policy

[role="_abstract"]
You can delete a network policy from a namespace.

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
