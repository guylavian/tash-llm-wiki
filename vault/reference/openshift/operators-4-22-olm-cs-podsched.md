---
title: "Catalog source pod scheduling"
type: reference
domain: openshift
slug: operators-4-22-olm-cs-podsched
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-cs-podsched
version: 4.22
family: operators
documentKind: "Documentation"
---

# Catalog source pod scheduling

[id="olm-cs-podsched"]
= Catalog source pod scheduling

When an Operator Lifecycle Manager (OLM) catalog source of source type `grpc` defines a `spec.image`, the Catalog Operator creates a pod that serves the defined image content. By default, this pod defines the following in its specification:

* Only the `kubernetes.io/os=linux` node selector.
* The default priority class name: `system-cluster-critical`.
* No tolerations.

As an administrator, you can override these values by modifying fields in the `CatalogSource` object's optional `spec.grpcPodConfig` section.

[IMPORTANT]
====
The Marketplace Operator, `openshift-marketplace`, manages the default `OperatorHub` custom resource's (CR). This CR manages `CatalogSource` objects. If you attempt to modify fields in the `CatalogSource` object's `spec.grpcPodConfig` section, the Marketplace Operator automatically reverts these modifications. By default, if you modify fields in the `spec.grpcPodConfig` section of the   `CatalogSource` object, the Marketplace Operator automatically reverts these changes.

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object.
====

[role="_additional-resources"]
.Additional resources

* OLM concepts and resources -> Catalog source

// Module included in the following assemblies:
//
// * admin/olm-cs-podsched.adoc

[id="disabling-catalogsource-objects_{context}"]
= Disabling default CatalogSource objects at a local level

You can apply persistent changes to a `CatalogSource` object, such as catalog source pods, at a local level, by disabling a default `CatalogSource` object. Consider the default configuration in situations where the default `CatalogSource` object's configuration does not meet your organization's needs. By default, if you modify fields in the `spec.grpcPodConfig` section of the   `CatalogSource` object, the Marketplace Operator automatically reverts these changes.

The Marketplace Operator, `openshift-marketplace`, manages the default custom resources (CRs) of the `OperatorHub`. The `OperatorHub` manages `CatalogSource` objects.

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object.

.Procedure

* To disable all the default `CatalogSource` objects at a local level, enter the following command:
+
[source,terminal]
----
$ oc patch operatorhub cluster -p '{"spec": {"disableAllDefaultSources": true}}' --type=merge
----
+
[NOTE]
====
You can also configure the default `OperatorHub` CR to either disable all `CatalogSource` objects or disable a specific object.
====

[role="_additional-resources"]
.Additional resources

* OperatorHub custom resource

* Disabling the default OperatorHub catalog sources

// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

[id="olm-node-selector_{context}"]
= Overriding the node selector for catalog source pods

.Prerequisites

* A `CatalogSource` object of source type `grpc` with `spec.image` is defined.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:
+
[source,yaml]
----
  grpcPodConfig:
    nodeSelector:
      custom_label: <label>
----
+
where `<label>` is the label for the node selector that you want catalog source pods to use for scheduling.

[role="_additional-resources"]
.Additional resources

* Placing pods on specific nodes using node selectors

// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

[id="olm-priority-class-name_{context}"]
= Overriding the priority class name for catalog source pods

.Prerequisites

* A `CatalogSource` object of source type `grpc` with `spec.image` is defined.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:
+
[source,yaml]
----
  grpcPodConfig:
    priorityClassName: <priority_class>
----
+
where `<priority_class>` is one of the following:
+
--
* One of the default priority classes provided by Kubernetes: `system-cluster-critical` or `system-node-critical`
* An empty set (`""`) to assign the default priority
* A pre-existing and custom defined priority class
--

[NOTE]
====
Previously, the only pod scheduling parameter that could be overriden was `priorityClassName`. This was done by adding the `operatorframework.io/priorityclass` annotation to the `CatalogSource` object. For example:

[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: example-catalog
  namespace: {global_ns}
  annotations:
    operatorframework.io/priorityclass: system-cluster-critical
----

If a `CatalogSource` object defines both the annotation and `spec.grpcPodConfig.priorityClassName`, the annotation takes precedence over the configuration parameter.
====

[role="_additional-resources"]
.Additional resources

* Pod priority classes

// Module included in the following assemblies:
//
// * operators/admin/olm-cs-podsched.adoc

[id="olm-tolerations_{context}"]
= Overriding tolerations for catalog source pods

.Prerequisites

* A `CatalogSource` object of source type `grpc` with `spec.image` is defined.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:
+
[source,yaml]
----
  grpcPodConfig:
    tolerations:
      - key: "<key_name>"
        operator: "<operator_type>"
        value: "<value>"
        effect: "<effect>"
----

// The following xref points to a topic that is not included in the OSD or
// ROSA docs.
[role="_additional-resources"]
.Additional resources

* Understanding taints and tolerations
