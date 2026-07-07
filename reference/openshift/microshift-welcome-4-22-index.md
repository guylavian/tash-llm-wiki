---
title: "Understanding {product-title}"
type: reference
domain: openshift
slug: microshift-welcome-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_welcome/index
version: 4.22
family: microshift_welcome
documentKind: "Documentation"
---

# Understanding {product-title}

[id="microshift-understanding"]
= Understanding OpenShift Container Platform

[.lead]

[role="_abstract"]
Welcome to the official OpenShift Container Platform  documentation, where you can learn about {microshift-short} and start exploring its features.

[id="microshift-product-documentation_{context}"]
== {microshift-short} product documentation

To browse the {microshift-short}  documentation, use one of the following methods:

* Use the navigation bars and links to browse.
* Select the task that interests you from the contents of this Welcome page.

To get started with {microshift-short}, use the following links:

//text is in main assembly for the sake of cross references
//* OpenShift Container Platform release notes
* Getting ready to install MicroShift

For related information, use the following links:

* Red Hat Device Edge overview
* Using image mode for RHEL to build, deploy, and manage operating systems
* {OCP} documentation

// Module included in the following assemblies:
//
// microshift_welcome/index.adoc

[id="con-about-microshift_{context}"]
= About OpenShift Container Platform

[role="_abstract"]
Working with resource-constrained field environments and hardware presents many challenges not experienced with cloud computing. {microshift-short} enables you to solve problems for edge devices by:

* Running the same Kubernetes workloads you run in the cloud, but at the edge.
* Overcoming the operational challenge of minimal system resources.
* Addressing the environmental challenges of severe networking constraints such as low or no connectivity.
* Meeting the physical constraint of hard-to-access locations by installing your system images directly on edge devices.
* Building on and integrating with edge-optimized operating systems such as {op-system-ostree-first}.

{microshift-short} has the simplicity of single-node deployment with the functions and services you need for computing in resource-constrained locations. You can have many deployments on different hosts, creating the specific system image needed for each of your applications.

// Module included in the following assemblies:
//
// microshift_welcome/index.adoc

[id="microshift-architectural-design_{context}"]
= Architectural design

[role="_abstract"]
{microshift-short} is a single-node container orchestration runtime designed to extend the benefits of using containers for running applications to low-resource edge environments. Because {microshift-short} is primarily a platform for deploying applications, only the APIs and features essential to operating in edge and small form factor computing environments are included.

For example, {microshift-short} has only the following Kubernetes node capabilities:

* Networking
* Ingress
* Storage

{microshift-short} also provides the following Kubernetes functions:

* Orchestration
* Security

To optimize your deployments, use {microshift-short} with a compatible operating system, such as {op-system-ostree-first}. Using {microshift-short} and {op-system-ostree-first} together forms {op-system-bundle}. Virtual machines are handled by the operating system in {microshift-short} deployments.

.OpenShift Container Platform as part of {op-system-bundle}.
image::311_RHDevice_Edge_Overview_0223_1.png[<OpenShift Container Platform is tasked with only the Kubernetes node services networking, ingress, storage, helm, with additional Kubernetes functions of orchestration and security, as the following diagram illustrates.>]

The following operational differences from {oke} can help you understand where you can deploy {microshift-short}:

[id="microshift-differences-oke_{context}"]
== Key differences from {oke}

* Devices with {microshift-short} installed are self-managing
* Compatible with `rpm-ostree`-based systems
* Uses only the APIs needed for essential functions, such as security and runtime controls
* Enables a subset of commands from the {oc-first} tool
* Does not support workload high availability (HA) or horizontal scalability with the addition of worker nodes

.OpenShift Container Platform differences from {oke}.
image::311_RHDevice_Edge_Overview_0223_2.png[<{microshift-short} is tasked with only the Kubernetes node capabilities of networking, ingress, storage, helm, with the additional Kubernetes functions of orchestration and security, as the following diagram illustrates.>]

The figure "OpenShift Container Platform differences from {oke}" shows that {oke} has the same cluster capabilities as a OpenShift Container Platform node, and adds the following information:

* Install
* Over-the-air updates
* Operators
* Operator Lifecycle Manager
* Monitoring
* Logging
* Registry
* Authorization
* Console
* Cloud Integration
* Virtual Machines (VMs) through {VirtProductName}

In {oke} and other {OCP} deployments, all of the components from the operating system through the cluster capabilities work as one comprehensive unit, with full cluster services for a multi-node Kubernetes workload. With {microshift-short}, functions such as over-the-air-updates, monitoring, and logging, are performed by the operating system.

[id="microshift-openshift-apis_{context}"]
== {microshift-short} OpenShift APIs

In addition to standard Kubernetes APIs, {microshift-short} includes a small subset of the APIs supported by {OCP}.

[cols="1,1",options="header"]
|===
^| API ^| API group
| Route
| route.openshift.io/v1
| SecurityContextConstraints
| security.openshift.io/v1
|===

// Module included in the following assemblies:
//
// // microshift_welcome/index.adoc

[id="microshift-k8s-apis_{context}"]
= {microshift-short} Kubernetes APIs

[role="_abstract"]
The Kubernetes API is fully accessible within {microshift-short} and can be managed with the `kubectl` command-line tool or the {OCP} CLI tool (`oc`), which is compatible with `kubectl` and offers a set of features that can be used with {microshift-short}. Using these command-line tools with {microshift-short} can help you access all of the resources you need to work with your deployments.

[id="additional-resources_microshift-welcome-index"]
[role="_additional-resources"]
== Additional resources
* API index
* {oke}
