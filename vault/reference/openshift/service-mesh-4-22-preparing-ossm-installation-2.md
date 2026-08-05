---
title: "Preparing to install Service Mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-preparing-ossm-installation-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/preparing-ossm-installation
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Preparing to install Service Mesh

[id="preparing-ossm-installation-v1x"]
= Preparing to install Service Mesh

Before you can install {SMProductName}, review the installation activities, ensure that you meet the prerequisites:

== Prerequisites

* Possess an active OpenShift Container Platform subscription on your Red Hat account. If you do not have a subscription, contact your sales representative for more information.

* Review the OpenShift Container Platform  overview.
* Install OpenShift Container Platform .
** Install OpenShift Container Platform  on AWS
** Install OpenShift Container Platform  on AWS with user-provisioned infrastructure
** Install OpenShift Container Platform  on bare metal
** Install OpenShift Container Platform  on vSphere
+
[NOTE]
====
If you are installing {SMProductName} on a restricted network, follow the instructions for your chosen OpenShift Container Platform infrastructure.
====
+

* Install the version of the OpenShift Container Platform command-line utility (the `oc` client tool) that matches your OpenShift Container Platform version and add it to your path.

** If you are using OpenShift Container Platform , see About the OpenShift CLI.

// Module included in the following assemblies:
//
// * service_mesh/v1x/preparing-ossm-install.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * post_installation_configuration/network-configuration.adoc

[id="ossm-supported-configurations-v1x_{context}"]
= {SMProductName} supported configurations

The following are the only supported configurations for the {SMProductName}:

* OpenShift Container Platform version 4.6 or later.

[NOTE]
====
OpenShift Online and {product-dedicated} are not supported for {SMProductName}.
====

* The deployment must be contained within a single OpenShift Container Platform cluster that is not federated.
* This release of {SMProductName} is only available on OpenShift Container Platform x86_64.
* This release only supports configurations where all {SMProductShortName} components are contained in the OpenShift Container Platform cluster in which it operates. It does not support management of microservices that reside outside of the cluster, or in a multi-cluster scenario.
* This release only supports configurations that do not integrate external services such as virtual machines.

For additional information about {SMProductName} lifecycle and supported configurations, refer to the Support Policy.

[id="ossm-supported-configurations-kiali_{context}"]
== Supported configurations for Kiali on {SMProductName}

* The Kiali observability console is only supported on the two most recent releases of the Chrome, Edge, Firefox, or Safari browsers.

[id="ossm-supported-configurations-adapters_{context}"]
== Supported Mixer adapters

* This release only supports the following Mixer adapter:
** 3scale Istio Adapter

// Module included in the following assemblies:
//
// * service_mesh/v1x/preparing-ossm-installation.adoc
// * service_mesh/v2x/preparing-ossm-installation.adoc

[id="ossm-installation-activities_{context}"]
= Service Mesh Operators overview

{SMProductName} requires the use of the {SMProductName} Operator which allows you to connect, secure, control, and observe the microservices that comprise your applications. You can also install other Operators to enhance your service mesh experience.

[WARNING]
====
Do not install Community versions of the Operators. Community Operators are not supported.
====

The following Operator is required:

{SMProductName} Operator:: Allows you to connect, secure, control, and observe the microservices that comprise your applications. It also defines and monitors the `ServiceMeshControlPlane` resources that manage the deployment, updating, and deletion of the {SMProductShortName} components. It is based on the open source Istio project.

The following Operators are optional:

{KialiProduct}:: Provides observability for your service mesh. You can view configurations, monitor traffic, and analyze traces in a single console. It is based on the open source Kiali project.
{TempoName}:: Provides distributed tracing to monitor and troubleshoot transactions in complex distributed systems. It is based on the open source Grafana Tempo project.

The following optional Operators are deprecated:

[IMPORTANT]
====
Starting with {SMProductName} 2.5, {JaegerName} and {es-op} are deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for these features during the current release lifecycle, but these features will no longer receive enhancements and will be removed. As an alternative to {JaegerName}, you can use {TempoName} instead.
====

{JaegerName}:: Provides distributed tracing to monitor and troubleshoot transactions in complex distributed systems. It is based on the open source Jaeger project.
{es-op}:: Provides database storage for tracing and logging with the {JaegerShortName}. It is based on the open source Elasticsearch project.

== Next steps

* Install {SMProductName} in your OpenShift Container Platform environment.
