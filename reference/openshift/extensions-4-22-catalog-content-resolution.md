---
title: "Catalog content resolution"
type: reference
domain: openshift
slug: extensions-4-22-catalog-content-resolution
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/catalog-content-resolution
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Catalog content resolution

[id="catalog-content-resolution"]
= Catalog content resolution

When you specify the cluster extension you want to install in a custom resource (CR), {olmv1-first} uses catalog selection to resolve what content is installed.

You can perform the following actions to control the selection of catalog content:

* Specify labels to select the catalog.
* Use match expressions to perform complex filtering across catalogs.
* Set catalog priority.

If you do not specify any catalog selection criteria, {olmv1-first} selects an extension from any available catalog on the cluster that provides the requested package.

During resolution, bundles that are not deprecated are preferred over deprecated bundles by default.

// Module included in the following assemblies:
// * extensions/catalogs/olmv1-catalog-content-resolution.adoc

[id="olmv1-catalog-selection-by-name_{context}"]
= Catalog selection by name

When a catalog is added to a cluster, a label is created by using the value of the `metadata.name` field of the catalog custom resource (CR). In the CR of an extension, you can specify the catalog name by using the `spec.source.catalog.selector.matchLabels` field. The value of the `matchLabels` field uses the following format:

.Example label derived from the `metadata.name` field
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
  labels:
    olm.operatorframework.io/metadata.name: <example_extension> <1>
...
----
<1> A label derived from the `metadata.name` field and automatically added when the catalog is applied.

The following example resolves the `<example_extension>-operator` package from a catalog with the `openshift-redhat-operators` label:

.Example extension CR
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchLabels:
          olm.operatorframework.io/metadata.name: openshift-redhat-operators
----

// Module included in the following assemblies:
// * extensions/catalogs/olmv1-catalog-content-resolution.adoc

[id="olmv1-catalog-selection-by-labels-or-exp_{context}"]
= Catalog selection by labels or expressions

You can add metadata to a catalog by using labels in the custom resource (CR) of a cluster catalog. You can then filter catalog selection by specifying the assigned labels or using expressions in the CR of the cluster extension.

The following cluster catalog CR adds the `example.com/support` label with the value of `true` to the `catalog-a` cluster catalog:

.Example cluster catalog CR with labels
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: catalog-a
  labels:
    example.com/support: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-a:latest
----

The following cluster extension CR uses the `matchLabels` selector to select catalogs with the `example.com/support` label and the value of `true`:

.Example cluster extension CR with `matchLabels` selector
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchLabels:
          example.com/support: "true"
----

You can use the `matchExpressions` field to perform more complex filtering for labels. The following cluster extension CR selects catalogs with the `example.com/support` label and a value of `production` or `supported`:

.Example cluster extension CR with `matchExpression` selector
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: example.com/support
            operator: In
            values:
              - "production"
              - "supported"
----

[NOTE]
====
If you use both the `matchLabels` and `matchExpressions` fields, the selected catalog must satisfy all specified criteria.
====

// Module included in the following assemblies:
// * extensions/catalogs/catalog-content-resolution.adoc

[id="olmv1-catalog-exclusion-by-labels-or-expressions_{context}"]
= Catalog exclusion by labels or expressions

You can exclude catalogs by using match expressions on metadata with the `NotIn` or `DoesNotExist` operators.

The following CRs add an `example.com/testing` label to the `unwanted-catalog-1` and `unwanted-catalog-2` cluster catalogs:

.Example cluster catalog CR
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: unwanted-catalog-1
  labels:
    example.com/testing: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-a:latest
----

.Example cluster catalog CR
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: unwanted-catalog-2
  labels:
    example.com/testing: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-b:latest
----

The following cluster extension CR excludes selection from the `unwanted-catalog-1` catalog:

.Example cluster extension CR that excludes a specific catalog
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: olm.operatorframework.io/metadata.name
            operator: NotIn
            values:
              - unwanted-catalog-1
----

The following cluster extension CR selects from catalogs that do not have the `example.com/testing` label. As a result, both `unwanted-catalog-1` and `unwanted-catalog-2` are excluded from catalog selection.

.Example cluster extension CR that excludes catalogs with a specific label
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: example.com/testing
            operator: DoesNotExist
----

// Module included in the following assemblies:
// * extensions/catalogs/olmv1-catalog-content-resolution.adoc

[id="olmv1-catalog-exclusion-by-priority_{context}"]
= Catalog selection by priority

When multiple catalogs provide the same package, you can resolve ambiguities by specifying the priority in the custom resource (CR) of each catalog. If unspecified, catalogs have a default priority value of `0`. The priority can be any positive or negative 32-bit integer.

[NOTE]
====
* During bundle resolution, catalogs with higher priority values are selected over catalogs with lower priority values.
* Bundles that are not deprecated are prioritized over bundles that are deprecated.
* If multiple bundles exist in catalogs with the same priority and the catalog selection is ambiguous, an error is printed.
====

.Example cluster catalog CR with a higher priority
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: high-priority-catalog
spec:
  priority: 1000
  source:
    type: Image
    image:
      ref: quay.io/example/higher-priority-catalog:latest
----

.Example cluster catalog CR with a lower priority
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: lower-priority-catalog
spec:
  priority: 10
  source:
    type: Image
    image:
      ref: quay.io/example/lower-priority-catalog:latest
----

// Module included in the following assemblies:
// * extensions/catalogs/olmv1-catalog-content-resolution.adoc

[id="olmv1-troubleshooting-catalog-selection-errors_{context}"]
= Troubleshooting catalog selection errors

If bundle resolution fails because of ambiguity or because no catalog is selected, an error message is printed in the `status.conditions` field of the cluster extension.

Perform the following actions to troubleshoot catalog selection errors:

* Refine your selection criteria using labels or expressions.
* Adjust your catalog priorities.
* Ensure that only one bundle matches your package name and version requirements.
