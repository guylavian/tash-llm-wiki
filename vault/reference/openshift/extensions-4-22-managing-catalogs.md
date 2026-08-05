---
title: "Managing catalogs"
type: reference
domain: openshift
slug: extensions-4-22-managing-catalogs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/managing-catalogs
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Managing catalogs

[id="managing-catalogs"]
= Managing catalogs

Cluster administrators can add _catalogs_, or curated collections of Operators and Kubernetes extensions, to their clusters. Operator authors publish their products to these catalogs. When you add a catalog to your cluster, you have access to the versions, patches, and over-the-air updates of the Operators and extensions that are published to the catalog.

You can manage catalogs and extensions declaratively from the CLI by using custom resources (CRs).

_File-based catalogs_ are the latest iteration of the catalog format in Operator Lifecycle Manager (OLM). It is a plain text-based (JSON or YAML) and declarative config evolution of the earlier SQLite database format, and it is fully backwards compatible.

[IMPORTANT]
====
Kubernetes periodically deprecates certain APIs that are removed in subsequent releases. As a result, Operators are unable to use removed APIs starting with the version of OpenShift Container Platform that uses the Kubernetes version that removed the API.
====

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-catalogd.adoc
// * extensions/arch/olmv1-catalogd.adoc

[id="olmv1-about-catalogs_{context}"]
= About catalogs in {olmv1}

You can discover installable content by querying a catalog for Kubernetes extensions, such as Operators and controllers, by using the catalogd component. Catalogd is a Kubernetes extension that unpacks catalog content for on-cluster clients and is part of the {olmv1-first} suite of microservices. Currently, catalogd unpacks catalog content that is packaged and distributed as container images.

[role="_additional-resources"]
.Additional resources
* File-based catalogs

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-catalogd.adoc
// * extensions/arch/olmv1-catalogd.adoc

[id="olmv1-red-hat-catalogs_{context}"]
= Red Hat-provided Operator catalogs in {olmv1}

{olmv1-first} includes the following Red Hat-provided Operator catalogs on the cluster by default. If you want to add an additional catalog to your cluster, create a custom resource (CR) for the catalog and apply it to the cluster. The following custom resource (CR) examples show the default catalogs installed on the cluster.

.Red{nbsp}Hat Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-redhat-operators
spec:
  priority: -100
  source:
    image:
      pollIntervalMinutes: <poll_interval_duration> <1>
      ref: registry.redhat.io/redhat/redhat-operator-index:v
    type: Image
----
<1> Specify the interval in minutes for polling the remote registry for newer image digests. To disable polling, do not set the field.

.Certified Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-certified-operators
spec:
priority: -200
  source:
    type: image
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/certified-operator-index:v
    type: Image
----

.Red{nbsp}Hat Marketplace catalog
[source,yaml,subs="attributes+"]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-redhat-marketplace
spec:
  priority: -300
  source:
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/redhat-marketplace-index:v
    type: Image
----

.Community Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-community-operators
spec:
  priority: -400
  source:
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/community-operator-index:v
    type: Image
----

The following command adds a catalog to your cluster:

.Command syntax
[source,terminal]
----
$ oc apply -f <catalog_name>.yaml <1>
----
<1> Specifies the catalog CR, such as `my-catalog.yaml`.

// Module included in the following assemblies:
//
// * extensions/catalogs/managing-catalogs.adoc

[id="olmv1-adding-a-catalog-to-a-cluster_{context}"]
= Adding a catalog to a cluster

To add a catalog to a cluster for {olmv1-first} usage, create a `ClusterCatalog` custom resource (CR) and apply it to the cluster.

.Procedure

. Create a catalog custom resource (CR), similar to the following example:
+
.Example `my-redhat-operators.yaml` file
[source,yaml,subs="attributes+"]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: my-redhat-operators <1>
spec:
  priority: 1000 <2>
  source:
    image:
      pollIntervalMinutes: 10 <3>
      ref: registry.redhat.io/redhat/community-operator-index:v <4>
    type: Image
----
<1> The catalog is automatically labeled with the value of the `metadata.name` field when it is applied to the cluster. For more information about labels and catalog selection, see "Catalog content resolution".
<2> Optional: Specify the priority of the catalog in relation to the other catalogs on the cluster. For more information, see "Catalog selection by priority".
<3> Specify the interval in minutes for polling the remote registry for newer image digests. To disable polling, do not set the field.
<4> Specify the catalog image in the `spec.source.image.ref` field.

. Add the catalog to your cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f my-redhat-operators.yaml
----
+
.Example output
[source,text]
----
clustercatalog.olm.operatorframework.io/my-redhat-operators created
----

.Verification

* Run the following commands to verify the status of your catalog:

.. Check if you catalog is available by running the following command:
+
[source,terminal]
----
$ oc get clustercatalog
----
+
.Example output
[source,text]
----
NAME                            LASTUNPACKED   SERVING   AGE
my-redhat-operators             55s            True      64s
openshift-certified-operators   83m            True      84m
openshift-community-operators   43m            True      84m
openshift-redhat-marketplace    83m            True      84m
openshift-redhat-operators      54m            True      84m
----

.. Check the status of your catalog by running the following command:
+
[source,terminal]
----
$ oc describe clustercatalog my-redhat-operators
----
+
.Example output
[source,text,subs="attributes+"]
----
Name:         my-redhat-operators
Namespace:
Labels:       olm.operatorframework.io/metadata.name=my-redhat-operators
Annotations:  <none>
API Version:  olm.operatorframework.io/v1
Kind:         ClusterCatalog
Metadata:
  Creation Timestamp:  2025-02-18T20:28:50Z
  Finalizers:
    olm.operatorframework.io/delete-server-cache
  Generation:        1
  Resource Version:  50248
  UID:               86adf94f-d2a8-4e70-895b-31139f2eeab7
Spec:
  Availability Mode:  Available
  Priority:           1000
  Source:
    Image:
      Poll Interval Minutes:  10
      Ref:                    registry.redhat.io/redhat/community-operator-index:v
    Type:                     Image
Status: <1>
  Conditions:
    Last Transition Time:  2025-02-18T20:29:00Z
    Message:               Successfully unpacked and stored content from resolved source
    Observed Generation:   1
    Reason:                Succeeded <2>
    Status:                True
    Type:                  Progressing
    Last Transition Time:  2025-02-18T20:29:00Z
    Message:               Serving desired content from resolved source
    Observed Generation:   1
    Reason:                Available
    Status:                True
    Type:                  Serving
  Last Unpacked:           2025-02-18T20:28:59Z
  Resolved Source:
    Image:
      Ref:  registry.redhat.io/redhat/community-operator-index@sha256:11627ea6fdd06b8092df815076e03cae9b7cede8b353c0b461328842d02896c5 <3>
    Type:   Image
  Urls:
    Base:  https://catalogd-service.openshift-catalogd.svc/catalogs/my-redhat-operators
Events:    <none>
----
<1> Describes the status of the catalog.
<2> Displays the reason the catalog is in the current state.
<3> Displays the image reference of the catalog.

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-deleting-catalog_{context}"]
= Deleting a catalog

You can delete a catalog by deleting its custom resource (CR).

.Prerequisites

* You have a catalog installed.

.Procedure

* Delete a catalog by running the following command:
+
[source,terminal]
----
$ oc delete clustercatalog <catalog_name>
----
+
.Example output
[source,text]
----
clustercatalog.olm.operatorframework.io "my-redhat-operators" deleted
----

.Verification

* Verify the catalog is deleted by running the following command:
+
[source,terminal]
----
$ oc get clustercatalog
----

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-disabling-a-default-catalog_{context}"]
= Disabling a default catalog

You can disable the Red{nbsp}Hat-provided catalogs that are included with OpenShift Container Platform by default.

.Procedure

* Disable a default catalog by running the following command:
+
[source,terminal]
----
$ oc patch clustercatalog openshift-certified-operators -p \
  '{"spec": {"availabilityMode": "Unavailable"}}' --type=merge
----
+
.Example output
[source,text]
----
clustercatalog.olm.operatorframework.io/openshift-certified-operators patched
----

.Verification

* Verify the catalog is disabled by running the following command:
+
[source,terminal]
----
$ oc get clustercatalog openshift-certified-operators
----
+
.Example output
[source,text]
----
NAME                            LASTUNPACKED   SERVING   AGE
openshift-certified-operators                  False     6h54m
----
