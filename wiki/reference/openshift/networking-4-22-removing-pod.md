---
title: "Removing a pod from a secondary network"
type: reference
domain: openshift
slug: networking-4-22-removing-pod
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/removing-pod
version: 4.22
family: networking
documentKind: "Documentation"
---

# Removing a pod from a secondary network

[id="removing-pod"]
= Removing a pod from a secondary network

[role="_abstract"]
To disconnect a pod from specific network configurations in OpenShift Container Platform, you can remove the pod from a secondary network. Delete the pod to remove its connection to the secondary network.

// Module included in the following assemblies:
//
// * networking/multiple_networks/removing-pod.adoc
// * microshift_networking/microshift_multiple_networks/microshift-cni-multus-using.adoc

[id="nw-multus-remove-pod_{context}"]
= Removing a pod from a secondary network

[role="_abstract"]
To disconnect a pod from specific network configurations in OpenShift Container Platform, you can remove the pod from a secondary network. Delete the pod using the `oc delete pod` command to remove its connection to the secondary network.

.Prerequisites

* A secondary network is attached to the pod.
* Install the OpenShift CLI (`oc`).
* Log in to the cluster.

.Procedure

* Delete the pod by entering the following command:
+
[source,terminal]
----
$ oc delete pod <name> -n <namespace>
----
+
--
where:

`<name>`:: Specifies the name of the pod.
`<namespace>`:: Specifies the namespace that contains the pod.
--
