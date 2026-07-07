---
title: "Network observability per-tenant model"
type: reference
domain: openshift
slug: observability-4-22-network-observability-per-tenant-model
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-per-tenant-model
version: 4.22
family: observability
documentKind: "Documentation"
---

# Network observability per-tenant model

[id="network-observability-per-tenant-model_{context}"]
= Network observability per-tenant model

[role="_abstract"]
Use the `FlowCollectorSlice` resource to delegate network traffic analysis management to project administrators while maintaining global cluster governance.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

[id="network-observability-per-tenant-hierarchical-governance-and-tenant-autonomy_{context}"]
= Per-tenant hierarchical governance and tenant autonomy

[role="_abstract"]
Cluster administrators can maintain global governance while allowing project administrators to manage network traffic observability within their specific namespaces.

The Network Observability Operator uses a hierarchical configuration model to support multitenancy. This architecture is beneficial for large-scale deployments and {hcp} environments where individual teams require self-service visibility without cluster administrator intervention.

The hierarchical model consists of the following components:

Global governance:: The cluster administrator manages the global `FlowCollector` resource. This resource defines the observability infrastructure and determines if per-tenant configuration is permitted.
Tenant autonomy:: The project administrator manages the `FlowCollectorSlice` resource. This namespace-scoped custom resource (CR) allows teams to define specific observability settings for their workloads.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

[id="network-observability-per-tenant-flowcollector-slice-granular-flow-collection_{context}"]
= FlowCollectorSlice resource for granular flow collection

[role="_abstract"]
The `FlowCollectorSlice` is a custom resource definition (CRD) that enables granular, multi-tenant network flow collection. By defining logical slices based on namespaces or subnets, you can selectively collect traffic and apply custom sampling to specific workloads rather than the entire cluster.

It complements the existing `FlowCollector` custom resource by enabling granular, selective, and multi-tenant-aware flow collection, instead of a single global configuration that applies uniformly to all traffic.

When slice-based collection is enabled, only traffic that matches at least one `FlowCollectorSlice` is collected, allowing administrators to precisely control which network flows are observed.

[id="benefits-of-flowcollector-slice_{context}"]
== Benefits of FlowCollectorSlice

By default, network flow collection applies uniformly to all traffic in the cluster. This can result in excessive data volume and limited flexibility.

Using `FlowCollectorSlice` provides the following benefits:

* Enables selective flow collection for specific namespaces or workloads.
* Supports multi-tenant and environment-based observability.
* Reduces storage and processing costs by filtering irrelevant traffic.
* Preserves backward compatibility through opt-in configuration.

[id="relationship-flowcollector-flowcollector-slice_{context}"]
== Relationship between FlowCollector and FlowCollectorSlice

While the `FlowCollector` resource defines global flow collection behavior for the cluster, the `FlowCollectorSlice` resource defines which traffic is eligible for collection when slice-based filtering is enabled.

The `FlowCollector.spec.slicesConfig` field controls how slice definitions are applied.

[id="collection-modes_{context}"]
== Collection modes

Slice behavior is governed by the `FlowCollector.spec.slicesConfig.collectionMode` field. Set the field to one of the following collection modes:

AlwaysCollect::
* Collects network flows from all cluster namespaces.
* Applies the subnet and sampling configurations defined in `FlowCollectorSlice` resources.
* Ignores the namespace selection logic in `FlowCollectorSlice` resources.
* Maintains the default collection behavior for backward compatibility.

AllowList::
* Collects only traffic that matches at least one `FlowCollectorSlice` resource.
* An optional namespace allow list includes selected namespaces in the collection.

[id="flowcollector-slice-status_{context}"]
== FlowCollectorSlice status

Each `FlowCollectorSlice` resource exposes a `status` subresource that reports:

* Validation results.
* Reconciliation state.
* Whether the slice is successfully applied.

This status allows administrators to verify that slice definitions are active and functioning as expected.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

[id="network-observability-per-tenant-flowcollector-slice-enable_{context}"]
= Enable the Network Observability Operator FlowCollectorSlice

[role="_abstract"]
Enabling the `FlowCollectorSlice` feature in the `FlowCollector` resource allows cluster administrators to delegate flow collection and data enrichment management to specific namespaces.

Before project administrators can manage their own settings, a cluster administrator must enable the `FlowCollector` custom resource to watch for the `FlowCollectorSlice` custom resource.

.Prerequisites

* The Network Observability Operator is installed.
* A `FlowCollector` custom resource exists in the cluster.
* You have `cluster-admin` privileges.

.Procedure
. Edit the `FlowCollector` custom resource by running the following command:
+
[source,terminal]
----
$ oc edit flowcollector cluster
----

. Configure the `spec.processor.slicesConfig` field to define which namespaces are permitted to use slices:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    slicesConfig:
      enable: true
      collectionMode: AllowList
      namespacesAllowList:
       - /openshift-.*|netobserv.*/
----
+
where:

`spec.processor.sliceConfig.enable`:: Specifies if the `FlowCollectorSlice` feature is enabled. If not, all resources of kind `FlowCollectorSlice` are ignored.
`spec.processor.sliceConfig.collectionMode`:: Specifies how the `FlowCollectorSlice` custom resources impacts the flow collection process. When set to `AlwaysCollect`, all flows are collected regardless of the presence of `FlowCollectorSlice`. When set to `AllowList`, only the flows related to namespaces where a `FlowCollectorSlice` resource is present, or configured via the global `namespacesAllowList`, are collected.
`spec.processor.sliceConfig.namespacesAllowList`:: Specifies a list of namespaces for which flows are always collected, regardless of the presence of `FlowCollectorSlice` in those namespaces.
+
[NOTE]
====
The `namespacesAllowList` field supports regular expressions, such as `/openshift-.*/` to capture multiple namespaces, or strict equality, such as `netobserv`, to match a specific namespace.
====

. Save the changes and exit the editor.

.Verification
* Verify that only network flows from the `netobserv` namespace and namespaces starting with `openshift-` are displayed in the *Network Traffic* page of the web console.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

[id="network-observability-per-tenant-flowcollector-slice-disable_{context}"]
= Disable the Network Observability Operator FlowCollectorSlice

[role="_abstract"]
Disable slice-based filtering in the Network Observability Operator to resume global flow collection while preserving existing `FlowCollectorSlice` resources.

.Procedure

. Edit the `FlowCollector` resource by running the following command:
+
[source,terminal]
----
$ oc edit flowcollector cluster
----

. Set the `spec.processor.slicesConfig.collectionMode` field to `AlwaysCollect`:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    slicesConfig:
      enable: true
      collectionMode: AlwaysCollect
      ...
----

. Save the changes.
+
Flow collection resumes for all traffic, and existing `FlowCollectorSlice` resources remain available for future use.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

[id="network-observability-per-tenant-flowcollector-slice-configure-project-administrator_{context}"]
= Configure the FlowCollectorSlice as a project administrator

[role="_abstract"]
Project administrators can manage flow collection and data enrichment within their own namespaces by configuring a `FlowCollectorSlice` custom resource for decentralized network traffic analysis.

.Prerequisites

* The Network Observability Operator is installed.
* You have `project-admin` permissions for the namespace.

.Procedure

. Create a YAML file named `flowCollectorSlice.yaml`:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollectorSlice
metadata:
  name: flowcollectorslice-sample
  namespace: my-app
spec:
  sampling: 1
  subnetLabels:
    - name: EXT:Database
      cidrs:
        - 192.168.50.0/24
----

. Apply the configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f flowCollectorSlice.yaml
----

.Verification

. In the OpenShift Container Platform console, navigate to *Observe* -> *Network Traffic*.
. Ensure flows to `192.168.50.0/24` subnet are observed with the `EXT:Database` label.

//Module included in the following assemblies:
//
// network_observability/network-observability-per-tenant-model.adoc

// Automatically generated by 'openshift-apidocs-gen'. Do not edit.
[id="flowcollectorslice-flows-netobserv-io-v1alpha1_{context}"]
= FlowCollectorSlice [flows.netobserv.io/v1alpha1]

Description::
+
--
FlowCollectorSlice is the API allowing to decentralize some of the FlowCollector configuration per namespace tenant.
--

Type::
  `object`

[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `apiVersion`
| `string`
| APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

| `kind`
| `string`
| Kind is a string value representing the REST resource this object represents. Servers might infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

| `metadata`
| `object`
| Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

| `spec`
| `object`
| FlowCollectorSliceSpec defines the desired state of FlowCollectorSlice

|===
== .metadata
Description::
+
--
Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
--

Type::
  `object`

== .spec
Description::
+
--
FlowCollectorSliceSpec defines the desired state of FlowCollectorSlice
--

Type::
  `object`

[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `sampling`
| `integer`
| `sampling` is an optional sampling interval to apply to this slice. For example, a value of `50` means that 1 matching flow in 50 is sampled.

| `subnetLabels`
| `array`
| `subnetLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services.
External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided. +

Beware that the subnet labels configured in FlowCollectorSlice are not limited to the flows of the related namespace: any flow
in the whole cluster can be labeled using this configuration. However, subnet labels defined in the cluster-scoped FlowCollector take
precedence in case of conflicting rules.

|===
== .spec.subnetLabels
Description::
+
--
`subnetLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services.
External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided. +

Beware that the subnet labels configured in FlowCollectorSlice are not limited to the flows of the related namespace: any flow
in the whole cluster can be labeled using this configuration. However, subnet labels defined in the cluster-scoped FlowCollector take
precedence in case of conflicting rules.
--

Type::
  `array`

== .spec.subnetLabels[]
Description::
+
--
SubnetLabel allows to label subnets and IPs, such as to identify cluster-external workloads or web services.
--

Type::
  `object`

Required::
  - `cidrs`
  - `name`

[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `cidrs`
| `array (string)`
| List of CIDRs, such as `["1.2.3.4/32"]`.

| `name`
| `string`
| Label name, used to flag matching flows.
External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided. +

|===

[id="additional-resources-per-tenand-configuration_{context}"]
[role="_additional-resources"]
== Additional resources

* FlowCollector API reference
