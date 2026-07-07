---
title: "Managing resources from custom resource definitions"
type: reference
domain: openshift
slug: operators-4-22-crd-managing-resources-from-crds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/crd-managing-resources-from-crds
version: 4.22
family: operators
documentKind: "Documentation"
---

# Managing resources from custom resource definitions

[id="crd-managing-resources-from-crds"]
= Managing resources from custom resource definitions

This guide describes how developers can manage custom resources (CRs) that come from custom resource definitions (CRDs).

// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-custom-resource-definitions_{context}"]
= Custom resource definitions

In the Kubernetes API, a _resource_ is an endpoint that stores a collection of API objects of a certain kind. For example, the built-in `Pods` resource contains a collection of `Pod` objects.

A _custom resource definition_ (CRD) object defines a new, unique object type, called a _kind_, in the cluster and lets the Kubernetes API server handle its entire lifecycle.

_Custom resource_ (CR) objects are created from CRDs that have been added to the cluster by a cluster administrator, allowing all cluster users to add the new resource type into projects.

When a cluster administrator adds a new CRD to the cluster, the Kubernetes API server reacts by creating a new RESTful resource path that can be accessed by the entire cluster or a single project (namespace) and begins serving the specified CR.

Cluster administrators that want to grant access to the CRD to other users can use cluster role aggregation to grant access to users with the `admin`, `edit`, or `view` default cluster roles. Cluster role aggregation allows the insertion of custom policy rules into these cluster roles. This behavior integrates the new resource into the RBAC policy of the cluster as if it was a built-in resource.

Operators in particular make use of CRDs by packaging them with any required RBAC policy and other software-specific logic.
Cluster administrators can also add CRDs manually to the cluster outside of the lifecycle of an Operator, making them available to all users.

[NOTE]
====
While only cluster administrators can create CRDs, developers can create the CR from an existing CRD if they have read and write permission to it.
====

// Useful paired with modules/crd-inspecting-custom-resources.adoc
//
// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-creating-custom-resources-from-file_{context}"]
= Creating custom resources from a file

After a custom resource definition (CRD) has been added to the cluster, custom resources (CRs) can be created with the CLI from a file using the CR specification.

.Prerequisites

- CRD added to the cluster by a cluster administrator.

.Procedure

. Create a YAML file for the CR. In the following example definition, the `cronSpec` and `image` custom fields are set in a CR of `Kind: CronTab`. The `Kind` comes from the `spec.kind` field of the CRD object:
+
.Example YAML file for a CR
[source,yaml]
----
apiVersion: "stable.example.com/v1" <1>
kind: CronTab <2>
metadata:
  name: my-new-cron-object <3>
  finalizers: <4>
  - finalizer.stable.example.com
spec: <5>
  cronSpec: "* * * * /5"
  image: my-awesome-cron-image
----
+
<1> Specify the group name and API version (name/version) from the CRD.
<2> Specify the type in the CRD.
<3> Specify a name for the object.
<4> Specify the finalizers for the object, if any. Finalizers allow controllers to implement conditions that must be completed before the object can be deleted.
<5> Specify conditions specific to the type of object.

. After you create the file, create the object:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

// Useful paired with modules/crd-creating-custom-resources-from-file.adoc
//
// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-inspecting-custom-resources_{context}"]
= Inspecting custom resources

You can inspect custom resource (CR) objects that exist in your cluster using the CLI.

.Prerequisites

* A CR object exists in a namespace to which you have access.

.Procedure

. To get information on a specific kind of a CR, run:
+
[source,terminal]
----
$ oc get <kind>
----
+
For example:
+
[source,terminal]
----
$ oc get crontab
----
+
.Example output
[source,terminal]
----
NAME                 KIND
my-new-cron-object   CronTab.v1.stable.example.com
----
+
Resource names are not case-sensitive, and you can use either the singular or plural forms defined in the CRD, as well as any short name. For example:
+
[source,terminal]
----
$ oc get crontabs
----
+
[source,terminal]
----
$ oc get crontab
----
+
[source,terminal]
----
$ oc get ct
----

. You can also view the raw YAML data for a CR:
+
[source,terminal]
----
$ oc get <kind> -o yaml
----
+
For example:
+
[source,terminal]
----
$ oc get ct -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: v1
items:
- apiVersion: stable.example.com/v1
  kind: CronTab
  metadata:
    clusterName: ""
    creationTimestamp: 2017-05-31T12:56:35Z
    deletionGracePeriodSeconds: null
    deletionTimestamp: null
    name: my-new-cron-object
    namespace: default
    resourceVersion: "285"
    selfLink: /apis/stable.example.com/v1/namespaces/default/crontabs/my-new-cron-object
    uid: 9423255b-4600-11e7-af6a-28d2447dc82b
  spec:
    cronSpec: '* * * * /5' <1>
    image: my-awesome-cron-image <1>
----
<1> Custom data from the YAML that you used to create the object displays.
