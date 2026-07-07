---
title: "Red Hat-provided Operator catalogs"
type: reference
domain: openshift
slug: operators-4-22-olm-rh-catalogs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-rh-catalogs
version: 4.22
family: operators
documentKind: "Documentation"
---

# Red Hat-provided Operator catalogs

[id="olm-rh-catalogs"]
= Red Hat-provided Operator catalogs

Red Hat provides several Operator catalogs that are included with OpenShift Container Platform by default.

[IMPORTANT]
====
As of OpenShift Container Platform 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format.

The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.

Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format.
For more information about working with file-based catalogs, see Managing custom catalogs,
Operator Framework packaging format, and Mirroring images for a disconnected installation using the oc-mirror plugin.
For more information about working with file-based catalogs, see Managing custom catalogs, and
Operator Framework packaging format.
====

// Module included in the following assemblies:
//
// * operators/understanding/olm-rh-catalogs.adoc

[id="olm-about-catalogs_{context}"]
= About Operator catalogs

An Operator catalog is a repository of metadata that Operator Lifecycle Manager (OLM) can query to discover and install Operators and their dependencies on a cluster. OLM always installs Operators from the latest version of a catalog.

An index image, based on the Operator bundle format, is a containerized snapshot of a catalog. It is an immutable artifact that contains the database of pointers to a set of Operator manifest content. A catalog can reference an index image to source its content for OLM on the cluster.

As catalogs are updated, the latest versions of Operators change, and older versions may be removed or altered. In addition, when OLM runs on
an OpenShift Container Platform
a OpenShift Container Platform
cluster in a restricted network environment, it is unable to access the catalogs directly from the internet to pull the latest content.

As a cluster administrator, you can create your own custom index image, either based on a Red Hat-provided catalog or from scratch, which can be used to source the catalog content on the cluster. Creating and updating your own index image provides a method for customizing the set of Operators available on the cluster, while also avoiding the aforementioned restricted network environment issues.

[IMPORTANT]
====
Kubernetes periodically deprecates certain APIs that are removed in subsequent releases. As a result, Operators are unable to use removed APIs starting with the version of OpenShift Container Platform that uses the Kubernetes version that removed the API.
====

[NOTE]
====
Support for the legacy _package manifest format_ for Operators, including custom catalogs that were using the legacy format, is removed in OpenShift Container Platform 4.8 and later.

When creating custom catalog images, previous versions of OpenShift Container Platform 4 required using the `oc adm catalog build` command, which was deprecated for several releases and is now removed. With the availability of Red Hat-provided index images starting in OpenShift Container Platform 4.6, catalog builders must use the `opm index` command to manage index images.
====
//Check on pulling this note during the 4.10 to 4.11 version scrub.

[role="_additional-resources"]
.Additional resources

* Managing custom catalogs
* Packaging format
* Using Operator Lifecycle Manager in disconnected environments

// Module included in the following assemblies:
//
// * operators/understanding/olm-rh-catalogs.adoc

[id="olm-rh-catalogs_{context}"]
= About Red Hat-provided Operator catalogs

The Red Hat-provided catalog sources are installed by default in the `{global_ns}` namespace, which makes the catalogs available cluster-wide in all namespaces.

The following Operator catalogs are distributed by Red Hat:

[cols="20%,55%,25%",options="header"]
|===
|Catalog
|Index image
|Description

|`redhat-operators`
|`registry.redhat.io/redhat/redhat-operator-index:{tag}`
|Red Hat products packaged and shipped by Red Hat. Supported by Red Hat.

|`certified-operators`
|`registry.redhat.io/redhat/certified-operator-index:{tag}`
|Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV.

// |`redhat-marketplace`
// |`registry.redhat.io/redhat/redhat-marketplace-index:{tag}`
// |Certified software that can be purchased from Red Hat Marketplace.

|`community-operators`
|`registry.redhat.io/redhat/community-operator-index:{tag}`
|Software maintained by relevant representatives in the redhat-openshift-ecosystem/community-operators-prod/operators GitHub repository. No official support.
|===

During a cluster upgrade, the index image tag for the default Red Hat-provided catalog sources are updated automatically by the Cluster Version Operator (CVO) so that Operator Lifecycle Manager (OLM) pulls the updated version of the catalog. For example during an upgrade from OpenShift Container Platform 4.8 to 4.9, the `spec.image` field in the `CatalogSource` object for the `redhat-operators` catalog is updated from:

[source,terminal]
----
registry.redhat.io/redhat/redhat-operator-index:v4.8
----

to:

[source,terminal]
----
registry.redhat.io/redhat/redhat-operator-index:v4.9
----
