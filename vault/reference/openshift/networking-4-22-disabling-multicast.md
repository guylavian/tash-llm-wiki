---
title: "Disabling multicast for a project"
type: reference
domain: openshift
slug: networking-4-22-disabling-multicast
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/disabling-multicast
version: 4.22
family: networking
documentKind: "Documentation"
---

# Disabling multicast for a project

[id="nw-ovn-kubernetes-disabling-multicast"]
= Disabling multicast for a project

[role="_abstract"]
In OpenShift Container Platform with OVN-Kubernetes, you can disable IP multicast on a per-project basis so pods no longer receive multicast traffic.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/disabling-multicast.adoc

[id="nw-disabling-multicast_{context}"]
= Disabling multicast between pods

[role="_abstract"]
To disable multicast between pods in a project, you can remove the `k8s.ovn.org/multicast-enabled` annotation from the namespace by using the `oc annotate` command or a namespace manifest.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* You must log in to the cluster with a user that has the `cluster-admin` role.

.Procedure

* Disable multicast by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc annotate {namespace} <namespace> \
    {annotation}
----
+
For `<namespace>`, specify the namespace for the project you want to disable multicast for.
+
[TIP]
====
You can alternatively apply the following YAML to delete the annotation:

[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/multicast-enabled: null
----
====
