---
title: "Understanding the software catalog"
type: reference
domain: openshift
slug: operators-4-22-olm-understanding-software-catalog
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-understanding-software-catalog
version: 4.22
family: operators
documentKind: "Documentation"
---

# Understanding the software catalog

[id="olm-understanding-software-catalog"]
= Understanding the software catalog

// Module included in the following assemblies:
//
// * operators/understanding/olm-understanding-software-catalog.adoc

[id="olm-software-catalog-overview_{context}"]
= About the software catalog

The _software catalog_ is the web console interface in OpenShift Container Platform that cluster administrators use to discover and install Operators. With one click, an Operator can be pulled from its off-cluster source, installed and subscribed on the cluster, and made ready for engineering teams to self-service manage the product across deployment environments using Operator Lifecycle Manager (OLM).

Cluster administrators can choose from catalogs grouped into the following categories:

[cols="2a,8a",options="header"]
|===
|Category |Description

|Red Hat Operators
|Red Hat products packaged and shipped by Red Hat. Supported by Red Hat.

|Certified Operators
|Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV.

// |Red Hat Marketplace
// |Certified software that can be purchased from Red Hat Marketplace.

|Community Operators
|Optionally-visible software maintained by relevant representatives in the redhat-openshift-ecosystem/community-operators-prod/operators GitHub repository. No official support.

|Custom Operators
|Operators you add to the cluster yourself. If you have not added any custom Operators, the *Custom* category does not appear in the web console software catalog.
|===

Operators in the software catalog are packaged to run on OLM. This includes a YAML file called a cluster service version (CSV) containing all of the CRDs, RBAC rules, deployments, and container images required to install and securely run the Operator. It also contains user-visible information like a description of its features and supported Kubernetes versions.

// Module included in the following assemblies:
//
// * operators/understanding/olm-understanding-software-catalog.adoc

[id="olm-software-catalog-arch_{context}"]
= Software catalog architecture

The software catalog UI component is driven by the Marketplace Operator by default on OpenShift Container Platform in the `openshift-marketplace` namespace.

[id="olm-software-catalog-arch-operatorhub-crd_{context}"]
== OperatorHub custom resource

The Marketplace Operator manages an `OperatorHub` custom resource (CR) named `cluster` that manages the default `CatalogSource` objects provided with the software catalog.
You can modify this resource to enable or disable the default catalogs, which is useful when configuring OpenShift Container Platform in restricted network environments.

.Example `OperatorHub` custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OperatorHub
metadata:
  name: cluster
spec:
  disableAllDefaultSources: true <1>
  sources: [ <2>
    {
      name: "community-operators",
      disabled: false
    }
  ]
----
<1> `disableAllDefaultSources` is an override that controls availability of all default catalogs that are configured by default during an OpenShift Container Platform installation.
<2> Disable default catalogs individually by changing the `disabled` parameter value per source.

[id="olm-understanding-software-catalog-resources"]
[role="_additional-resources"]
== Additional resources

* Catalog source
* Operator installation and upgrade workflow in OLM
* Red Hat Partner Connect
// * Red Hat Marketplace
