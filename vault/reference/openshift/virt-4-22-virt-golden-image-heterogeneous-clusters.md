---
title: "Heterogeneous cluster support"
type: reference
domain: openshift
slug: virt-4-22-virt-golden-image-heterogeneous-clusters
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-golden-image-heterogeneous-clusters
version: 4.22
family: virt
documentKind: "Documentation"
---

# Heterogeneous cluster support

[id="virt-golden-image-heterogeneous-clusters"]
= Heterogeneous cluster support

[role="_abstract"]
A heterogeneous cluster is a cluster where nodes have differing architectures. Heterogeneous clusters promote optimal compute resource usage by mixing different types of hardware in one cluster.

With heterogenous clusters, you can match workloads to hardware intended for the workload task instead of general purpose compute platforms. For example, GPU and general purpose compute resources could be combined and workloads assigned to the appropriate hardware.

[IMPORTANT]
====
If golden image support is disabled in a heterogeneous cluster, you can encounter inconsistencies between node and image architectures. This happens when images are used for virtual machine creation that do not match the node architecture. This can lead to the failure of virtual machine boot up or virtual machines that do not run as expected. The warning level alert `HCOMultiArchGoldenImagesDisabled` is produced when this feature is not enabled in a heterogeneous cluster.
====

If you have a heterogeneous cluster but do not want to enable multiple architecture support, you can modify the workloads node placement in the `HyperConverged` custom resource (CR) to include only nodes with a specific architecture.

Golden image support for heterogeneous clusters extends golden image support in the following areas:

* Enables VM creators to deploy persistent virtual machines with specific architectures.
* Enables VM creators to define custom golden images that support heterogenous clusters.

The same golden image can be used with nodes of different architectures if the boot image supports the required architectures. For example, a golden image that supports both ARM and AMD architectures can be used with both types of nodes.

Golden image support for heterogeneous clusters is not enabled by default. You can enable heterogenous cluster support by setting the feature gate in the `HyperConverged` CR.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-enabling-heterogeneous-clusters_{context}"]
= Enabling heterogeneous cluster support

[role="_abstract"]
You can enable golden image support for heterogeneous clusters by setting the `enableMultiArchBootImageImport` feature gate to `true` in the `HyperConverged` custom resource (CR).

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` permissions.
* You have installed the {oc-first}.

.Procedure

* Enable the `enableMultiArchBootImageImport` feature gate by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op":"replace","path":"/spec/featureGates/enableMultiArchBootImageImport", "value": true}]'
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-mod-golden-image-heterogeneous-clusters_{context}"]
= Modifying a common golden image source in a heterogeneous cluster

[role="_abstract"]
You can modify the image source of a common golden image in a heterogeneous cluster by specifying the supported architectures in the `ssp.kubevirt.io/dict.architectures` annotation in the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `HyperConverged` CR, adding the appropriate values for `ssp.kubevirt.io/dict.architectures` annotation in the `dataImportCronTemplates` section. For example:
+
[source,yaml]
----
#...
spec:
  dataImportCronTemplates:
  - metadata:
      name: kubevirt-hyperconverged
      annotations:
        ssp.kubevirt.io/dict.architectures: "<architecture_list>"
    spec:
      schedule: "0 */12 * * *"
      template:
        spec:
          source:
            registry:
                url: docker://my-private-registry/my-own-version-of-centos:8
      managedDataSource: centos-stream8
#...
----
+
where:
+
`ssp.kubevirt.io/dict.architectures`:: Specifies a comma-separated list of supported architectures for this image. For example, if the image supports `amd64` and `arm64` architectures, the value would be `"amd64,arm64"`.

. Save and exit the editor to update the `HyperConverged` CR.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-add-custom-golden-image-heterogeneous-cluster_{context}"]

= Adding a custom golden image in a heterogeneous cluster

[role="_abstract"]
Add a custom golden image in a heterogeneous cluster by setting the `ssp.kubevirt.io/dict.architectures` annotation in the `spec.dataImportCronTemplates.metadata.annotations` stanza of the `HyperConverged` custom resource (CR). This annotation lists the architectures supported by the image.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `HyperConverged` CR, to add the custom golden image. You must add the appropriate values for `ssp.kubevirt.io/dict.architectures` annotation in the `dataImportCronTemplates` section. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
  - metadata:
      name: custom-image1
      annotations:
        ssp.kubevirt.io/dict.architectures: "<architecture_list>"
    spec:
      schedule: "0 */12 * * *"
      template:
        spec:
          source:
            registry:
              url: docker://myprivateregistry/custom1
      managedDataSource: custom1
      retentionPolicy: "All"
#...
----
+
where:
+
`<architecture_list>`:: Specifies a comma-separated list of supported architectures for this image. For example, if the image supports `amd64` and `arm64` architectures, the value would be `"amd64,arm64"`.
+
[NOTE]
====
An image may support more architectures than you want to use in your cluster. You do not have to list all of the architectures an image supports, only those for which you want to create a boot source.
====
. Save and exit the editor to update the `HyperConverged` CR.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-modify-workload-node-heterogeneous-cluster_{context}"]

= Modifying workloads node placement in a heterogeneous cluster

[role="_abstract"]
If you have a heterogeneous cluster but do not want to enable multiple architecture support, you can modify the workloads node placement in the `HyperConverged` custom resource (CR) to include only nodes with a specific architecture.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `HyperConverged` CR, to modify the workloads node placement to include only nodes with a specific architecture. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
#...
  workloads:
    nodePlacement:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: kubernetes.io/arch
                    operator: In
                    values:
                      - <node_architecture>

----
+
where:
+
`<node_architecture>`:: Specifies the target architecture. For example, to limit placement to AMD nodes, use `amd64`.

. Save and exit the editor to update the `HyperConverged` CR.
