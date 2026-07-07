---
title: "Managing data volume annotations"
type: reference
domain: openshift
slug: virt-4-22-virt-managing-data-volume-annotations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-managing-data-volume-annotations
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing data volume annotations

[id="virt-managing-data-volume-annotations"]
= Managing data volume annotations

[role="_abstract"]
Data volume (DV) annotations allow you to manage pod behavior. You can add one or more annotations to a data volume, which then propagates to the created importer pods.

// Module included in the following assemblies:
//
// * virt/storage/virt-managing-data-volume-annotations.adoc

[id="virt-dv-annotations_{context}"]
= Example: Data volume annotations

[role="_abstract"]
This example shows how you can configure data volume (DV) annotations to control which network the importer pod uses. The `v1.multus-cni.io/default-network: bridge-network` annotation causes the pod to use the Multus network named `bridge-network` as its default network.

If you want the importer pod to use both the default network from the cluster and the secondary Multus network, use the `k8s.v1.cni.cncf.io/networks: <network_name>` annotation.

Multus network annotation example:

[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: datavolume-example
  annotations:
    v1.multus-cni.io/default-network: bridge-network
# ...
----

The `v1.multus-cni.io/default-network` annotation specifies the Multus network name.
