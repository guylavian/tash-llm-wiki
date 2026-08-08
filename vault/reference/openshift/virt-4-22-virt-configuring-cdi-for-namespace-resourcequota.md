---
title: "Configuring CDI to override CPU and memory quotas"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-cdi-for-namespace-resourcequota
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-cdi-for-namespace-resourcequota
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring CDI to override CPU and memory quotas

[id="virt-configuring-cdi-for-namespace-resourcequota"]
= Configuring CDI to override CPU and memory quotas

[role="_abstract"]
You can configure the Containerized Data Importer (CDI) to import, upload, and clone virtual machine disks into namespaces that are subject to CPU and memory resource restrictions.

// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-cdi-for-namespace-resourcequota.adoc

[id="virt-about-cpu-and-memory-quota-namespace_{context}"]
= About CPU and memory quotas in a namespace

[role="_abstract"]
A _resource quota_, defined by the `ResourceQuota` object, imposes restrictions on a namespace that limit the total amount of compute resources that can be consumed by resources within that namespace.

The `HyperConverged` custom resource (CR) defines the user configuration for the Containerized Data Importer (CDI). The CPU and memory request and limit values are set to a default value of `0`. This ensures that pods created by CDI that do not specify compute resource requirements are given the default values and are allowed to run in a namespace that is restricted with a quota.

// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-cdi-for-namespace-resourcequota.adoc

[id="virt-overriding-cpu-and-memory-defaults_{context}"]
= Overriding CPU and memory defaults

[role="_abstract"]
Modify the default settings for CPU and memory requests and limits for your use case by adding the `spec.resourceRequirements.storageWorkloads` stanza to the `HyperConverged` custom resource (CR).

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Edit the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `spec.resourceRequirements.storageWorkloads` stanza to the CR, setting the values based on your use case. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  resourceRequirements:
    storageWorkloads:
      limits:
        cpu: "500m"
        memory: "2Gi"
      requests:
        cpu: "250m"
        memory: "1Gi"
----

. Save and exit the editor to update the `HyperConverged` CR.

[id="{context}_additional-resources"]
[role="_additional-resources"]
== Additional resources
* Resource quotas per project
