---
title: "Operator Lifecycle Manager architecture"
type: reference
domain: openshift
slug: operators-4-22-olm-arch
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-arch
version: 4.22
family: operators
documentKind: "Documentation"
---

# Operator Lifecycle Manager architecture

[id="olm-arch"]
= Operator Lifecycle Manager architecture

This guide outlines the component architecture of Operator Lifecycle Manager (OLM) in OpenShift Container Platform.

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/operator-reference.adoc

[id="olm-architecture_{context}"]
= Component responsibilities

= CRDs

Operator Lifecycle Manager (OLM) is composed of two Operators: the OLM Operator and the Catalog Operator.

The OLM and Catalog Operators are responsible for managing the custom resource definitions (CRDs) that are the basis for the OLM framework:

.CRDs managed by OLM and Catalog Operators
[cols="2a,1a,1a,8a",options="header"]
|===
|Resource |Short name |Owner |Description

|`ClusterServiceVersion` (CSV)
|`csv`
|OLM
|Application metadata: name, version, icon, required resources, installation, and so on.

|`InstallPlan`
|`ip`
|Catalog
|Calculated list of resources to be created to automatically install or upgrade a CSV.

|`CatalogSource`
|`catsrc`
|Catalog
|A repository of CSVs, CRDs, and packages that define an application.

|`Subscription`
|`sub`
|Catalog
|Used to keep CSVs up to date by tracking a channel in a package.

|`OperatorGroup`
|`og`
|OLM
|Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.
|===

Each of these Operators is also responsible for creating the following resources:

.Resources created by OLM and Catalog Operators
[options="header"]
|===
|Resource |Owner

|`Deployments`
.4+.^|OLM

|`ServiceAccounts`
|`(Cluster)Roles`
|`(Cluster)RoleBindings`

|`CustomResourceDefinitions` (CRDs)
.2+.^|Catalog
|`ClusterServiceVersions`
|===

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-olm-operator_{context}"]
= OLM Operator

The OLM Operator is responsible for deploying applications defined by CSV resources after the required resources specified in the CSV are present in the cluster.

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application.

The OLM Operator uses the following workflow:

. Watch for cluster service versions (CSVs) in a namespace and check that requirements are met.
. If requirements are met, run the install strategy for the CSV.
+
[NOTE]
====
A CSV must be an active member of an Operator group for the install strategy to run.
====

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-operator_{context}"]
= Catalog Operator

The Catalog Operator is responsible for resolving and installing cluster service versions (CSVs) and the required resources they specify. It is also responsible for watching catalog sources for updates to packages in channels and upgrading them, automatically if desired, to the latest available versions.

To track a package in a channel, you can create a `Subscription` object configuring the desired package, channel, and the `CatalogSource` object you want to use for pulling updates. When updates are found, an appropriate `InstallPlan` object is written into the namespace on behalf of the user.

The Catalog Operator uses the following workflow:

. Connect to each catalog source in the cluster.
. Watch for unresolved install plans created by a user, and if found:
.. Find the CSV matching the name requested and add the CSV as a resolved resource.
.. For each managed or required CRD, add the CRD as a resolved resource.
.. For each required CRD, find the CSV that manages it.
. Watch for resolved install plans and create all of the discovered resources for it, if approved by a user or automatically.
. Watch for catalog sources and subscriptions and create install plans based on them.

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-registry_{context}"]
= Catalog Registry

The Catalog Registry stores CSVs and CRDs for creation in a cluster and stores metadata about packages and channels.

A _package manifest_ is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version.
