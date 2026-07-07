---
title: "Distributed tracing"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-distr-tracing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-distr-tracing
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Distributed tracing

[id="ossm-dist-trac"]
= Distributed tracing

#DRAFT ASSEMBLY - Not currently listed on the Topic Map#
//All of this content currently resides in the Observability Assembly

Distributed Tracing is the process of tracking the performance of individual services in an application by tracing the path of the service calls in the application. Each time a user takes action in an application, a request is executed that might require many services to interact to produce a response. The path of this request is called a distributed transaction.

As a developer, you can use the {JaegerShortName} to visualize call flows in a microservice application with {SMProductName}.

This module is included in the following assemblies:
* service_mesh/v2x/ossm-observability.adoc
[id="ossm-config-sampling_{context}"]
= Adjusting the sampling rate

A trace is an execution path between services in the service mesh. A trace is comprised of one or more spans. A span is a logical unit of work that has a name, start time, and duration. The sampling rate determines how often a trace is persisted.

The Envoy proxy sampling rate is set to sample 100% of traces in your service mesh by default. A high sampling rate consumes cluster resources and performance but is useful when debugging issues. Before you deploy {SMProductName} in production, set the value to a smaller proportion of traces. For example, set `spec.tracing.sampling` to `100` to sample 1% of traces.

Configure the Envoy proxy sampling rate as a scaled integer representing 0.01% increments.

In a basic installation, `spec.tracing.sampling` is set to `10000`, which samples 100% of traces. For example:

* Setting the value to 10 samples 0.1% of traces.
* Setting the value to 500 samples 5% of traces.

[NOTE]
====
The Envoy proxy sampling rate applies for applications that are available to a Service Mesh, and use the Envoy proxy. This sampling rate determines how much data the Envoy proxy collects and tracks.

The Jaeger remote sampling rate applies to applications that are external to the Service Mesh, and do not use the Envoy proxy, such as a database. This sampling rate determines how much data {DTProductName} collects and stores.
====

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and select the project where you installed the control plane, for example *istio-system*.

. Click the {SMProductName} Operator. In the *Istio Service Mesh Control Plane* column, click the name of your `ServiceMeshControlPlane` resource, for example `basic`.

. To adjust the sampling rate, set a different value for `spec.tracing.sampling`.
+
.. Click the *YAML* tab.
+
.. Set the value for `spec.tracing.sampling` in your `ServiceMeshControlPlane` resource. In the following example, set it to `100`.
+
.Jaeger sampling example
[source,yaml]
----
spec:
  tracing:
    sampling: 100
----
+
.. Click *Save*.

. Click *Reload* to verify the `ServiceMeshControlPlane` resource was configured correctly.

This module is included in the following assemblies:
* service_mesh/v2x/ossm-observability.adoc

[id="ossm-config-external-jaeger_{context}"]
= Connecting an existing distributed tracing Jaeger instance

If you already have an existing {JaegerName} instance in OpenShift Container Platform, you can configure your `ServiceMeshControlPlane` resource to use that instance for {DTShortName}.

[IMPORTANT]
====
Starting with {SMProductName} 2.5, {JaegerName} and {es-op} are deprecated and will be removed in a future release. Red{nbsp}Hat will provide bug fixes and support for these features during the current release lifecycle, but these features will no longer receive enhancements and will be removed. As an alternative to {JaegerName}, you can use {TempoName} instead.
====

.Prerequisites

* {DTProductName} instance installed and configured.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Installed Operators*.

. Click the *Project* menu and select the project where you installed the {SMProductShortName} control plane, for example *istio-system*.

. Click the {SMProductName} Operator. In the *Istio Service Mesh Control Plane* column, click the name of your `ServiceMeshControlPlane` resource, for example `basic`.

. Add the name of your {JaegerShortName} instance to the `ServiceMeshControlPlane`.
+
.. Click the *YAML* tab.
+
.. Add the name of your {JaegerShortName} instance to `spec.addons.jaeger.name` in your `ServiceMeshControlPlane` resource. In the following example, `distr-tracing-production` is the name of the {JaegerShortName} instance.
+
.Example distributed tracing configuration
[source,yaml]
----
spec:
  addons:
    jaeger:
      name: distr-tracing-production
----
+
.. Click *Save*.

. Click *Reload* to verify the `ServiceMeshControlPlane` resource was configured correctly.
