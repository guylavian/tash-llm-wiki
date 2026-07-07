---
title: "About the Cluster API"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-about
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-about
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# About the Cluster API

[id="cluster-api-about"]
= About the Cluster API

The Cluster API is an upstream project that is integrated into OpenShift Container Platform as a Technology Preview for {aws-first}, {gcp-first}, {azure-first}, {rh-openstack-first}, {vmw-first}, and bare metal.

//Cluster API overview
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-about.adoc

[id="cluster-api-overview_{context}"]
= Cluster API overview

You can use the Cluster API to create and manage compute machine sets and compute machines in your OpenShift Container Platform cluster.
This capability is in addition or an alternative to managing machines with the Machine API.

For OpenShift Container Platform  clusters, you can use the Cluster API to perform node host provisioning management actions after the cluster installation finishes.
This system enables an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

With the Cluster API Technology Preview, you can create compute machines and compute machine sets on OpenShift Container Platform clusters for supported providers.
You can also explore the features that are enabled by this implementation that might not be available with the Machine API.

//Cluster API benefits
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-about.adoc

[id="cluster-api-benefits_{context}"]
= Cluster API benefits

By using the Cluster API, OpenShift Container Platform users and developers gain the following advantages:

* The option to use upstream community Cluster API infrastructure providers that might not be supported by the Machine API.

* The opportunity to collaborate with third parties who maintain machine controllers for infrastructure providers.

* The ability to use the same set of Kubernetes tools for infrastructure management in OpenShift Container Platform.

* The ability to create compute machine sets by using the Cluster API that support features that are not available with the Machine API.

//Cluster API limitations
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-about.adoc

[id="capi-tech-preview-limitations_{context}"]
= Cluster API limitations

Using the Cluster API to manage machines is a Technology Preview feature and has the following limitations:

* To use this feature, you must enable the `TechPreviewNoUpgrade` feature set.
+
[IMPORTANT]
====
Enabling this feature set cannot be undone and prevents minor version updates.
====

* Only {aws-first}, {gcp-first}, {azure-first}, {rh-openstack-first}, {vmw-first}, and bare-metal clusters can use the Cluster API.

* You must manually create some of the primary resources that the Cluster API requires.
For more information, see "Getting started with the Cluster API".

* You cannot use the Cluster API to manage control plane machines.

* Migration of existing compute machine sets created by the Machine API to Cluster API compute machine sets is not supported.

* Full feature parity with the Machine API is not available.

* For clusters that use the Cluster API, {oc-first} commands prioritize Cluster API objects over Machine API objects.
This behavior impacts any `oc` command that acts upon any object that is represented in both the Cluster API and the Machine API.
+
For more information and a workaround for this issue, see "Referencing the intended objects when using the CLI" in the troubleshooting content.

[role="_additional-resources"]
.Additional resources
* Enabling features using feature gates

* Getting started with the Cluster API

* Referencing the intended objects when using the CLI

[id="cluster-api-architecture_{context}"]
== Cluster API architecture

The OpenShift Container Platform integration of the upstream Cluster API is implemented and managed by the {cluster-capi-operator}.
The {cluster-capi-operator} and its operands are provisioned in the `openshift-cluster-api` namespace, in contrast to the Machine API, which uses the `openshift-machine-api` namespace.

//The {cluster-capi-operator}
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-about.adoc

[id="capi-arch-operator_{context}"]
= The {cluster-capi-operator}

The {cluster-capi-operator} is an OpenShift Container Platform Operator that maintains the lifecycle of Cluster API resources.
This Operator is responsible for all administrative tasks related to deploying the Cluster API project within an OpenShift Container Platform cluster.

If a cluster is configured correctly to allow the use of the Cluster API, the {cluster-capi-operator} installs the Cluster API components on the cluster.

For more information, see the "{cluster-capi-operator}" entry in the _Cluster Operators reference_ content.

[role="_additional-resources"]
.Additional resources
* {cluster-capi-operator}

//Cluster API primary resources
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-about.adoc

[id="capi-arch-resources_{context}"]
= Cluster API primary resources

The Cluster API consists of the following primary resources. For the Technology Preview of this feature, you must create some of these resources manually in the `openshift-cluster-api` namespace.

Cluster:: A fundamental unit that represents a cluster that is managed by the Cluster API.

Infrastructure cluster:: A provider-specific resource that defines properties that all of the compute machine sets in the cluster share, such as the region and subnets.

Machine template:: A provider-specific template that defines the properties of the machines that a compute machine set creates.

Machine set:: A group of machines.
+
Compute machine sets are to machines as replica sets are to pods.
To add machines or scale them down, change the `replicas` field on the compute machine set custom resource to meet your compute needs.
+
With the Cluster API, a compute machine set references a `Cluster` object and a provider-specific machine template.

Machine:: A fundamental unit that describes the host for a node.
+
The Cluster API creates machines based on the configuration in the machine template.
