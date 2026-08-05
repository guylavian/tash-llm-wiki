---
title: "Editing a network policy"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-editing-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-editing-network-policy
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Editing a network policy

[id="microshift-editing-network-policy"]
= Editing a network policy

[role="_abstract"]
You can edit an existing network policy for a namespace.

Typical edits might include changes to the pods to which the policy applies, allowed ingress traffic, and the destination ports on which to accept traffic. The `apiVersion`, `kind`, and `name` fields must not be changed when editing `NetworkPolicy` objects, as these define the resource itself.

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
