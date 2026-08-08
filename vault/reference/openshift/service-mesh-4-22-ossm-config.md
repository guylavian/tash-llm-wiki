---
title: "Configuring Service Mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-config
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Configuring Service Mesh

[id="ossm-config-v1x"]
= Configuring Service Mesh

After you create a `ServiceMeshControlPlane` resource, configure the resource to suit your environment and requirements.

This guide references the Bookinfo sample application to provide examples of security in an example application. Install the Bookinfo application to learn how these routing examples work.

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-config-security_{context}"]
= Security

If your service mesh application is constructed with a complex array of microservices, you can use {SMProductName} to customize the security of the communication between those services. The infrastructure of OpenShift Container Platform along with the traffic management features of {SMProductShortName} help you manage the complexity of your applications and secure microservices.

.Before you begin

If you have a project, add your project to the `ServiceMeshMemberRoll` resource.

[NOTE]
====
After you add the namespace to the `ServiceMeshMemberRoll`, services or pods in that namespace will not be accessible to callers outside the service mesh.
====

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-security.adoc

[id="ossm-security-mtls_{context}"]
= Enabling mutual Transport Layer Security (mTLS)

Mutual Transport Layer Security (mTLS) is a protocol where two parties authenticate each other. It is the default mode of authentication in some protocols (IKE, SSH) and optional in others (TLS).

mTLS can be used without changes to the application or service code. The TLS is handled entirely by the service mesh infrastructure and between the two sidecar proxies.

By default, {SMProductName} is set to permissive mode, where the sidecars in {SMProductShortName} accept both plain-text traffic and connections that are encrypted using mTLS. If a service in your mesh is communicating with a service outside the mesh, strict mTLS could break communication between those services. Use permissive mode while you migrate your workloads to {SMProductShortName}.

[id="ossm-security-enabling-strict-mtls_{context}"]
== Enabling strict mTLS across the mesh

If your workloads do not communicate with services outside your mesh and communication will not be interrupted by only accepting encrypted connections, you can enable mTLS across your mesh quickly. Set `spec.istio.global.mtls.enabled` to `true` in your `ServiceMeshControlPlane` resource. The operator creates the required resources.

[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
  istio:
    global:
      mtls:
        enabled: true
----

[id="ossm-security-mtls-sidecars-incoming-services_{context}"]
=== Configuring sidecars for incoming connections for specific services

You can also configure mTLS for individual services or namespaces by creating a policy.

[source,yaml]
----
apiVersion: "authentication.istio.io/v1alpha1"
kind: "Policy"
metadata:
  name: default
  namespace: <NAMESPACE>
spec:
  peers:
    - mtls: {}
----

[id="ossm-security-mtls-sidecars-outgoing_{context}"]
== Configuring sidecars for outgoing connections

Create a destination rule to configure {SMProductShortName} to use mTLS when sending requests to other services in the mesh.

[source,yaml]
----
apiVersion: "networking.istio.io/v1alpha3"
kind: "DestinationRule"
metadata:
  name: "default"
  namespace: <CONTROL_PLANE_NAMESPACE>>
spec:
  host: "*.local"
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
----

[id="ossm-security-min-max-tls_{context}"]
== Setting the minimum and maximum protocol versions

If your environment has specific requirements for encrypted traffic in your service mesh, you can control the cryptographic functions that are allowed by setting the `spec.security.controlPlane.tls.minProtocolVersion` or `spec.security.controlPlane.tls.maxProtocolVersion` in your `ServiceMeshControlPlane` resource. Those values, configured in your control plane resource, define the minimum and maximum TLS version used by mesh components when communicating securely over TLS.

[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
  istio:
    global:
      tls:
        minProtocolVersion: TLSv1_2
        maxProtocolVersion: TLSv1_3
----

The default is `TLS_AUTO` and does not specify a version of TLS.

.Valid values
|===
|Value|Description

|`TLS_AUTO`
| default

|`TLSv1_0`
|TLS version 1.0

|`TLSv1_1`
|TLS version 1.1

|`TLSv1_2`
|TLS version 1.2

|`TLSv1_3`
|TLS version 1.3
|===

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

[id="ossm-security-cipher_{context}"]
= Configuring cipher suites and ECDH curves

Cipher suites and Elliptic-curve Diffie–Hellman (ECDH curves) can help you secure your service mesh. You can define a comma separated list of cipher suites using `spec.security.controlplane.tls.cipherSuites` and ECDH curves using `spec.security.controlplane.tls.ecdhCurves` in your `ServiceMeshControlPlane` resource. If either of these attributes are empty, then the default values are used.

The `cipherSuites` setting is effective if your service mesh uses TLS 1.2 or earlier. It has no effect when negotiating with TLS 1.3.

Set your cipher suites in the comma separated list in order of priority. For example, `ecdhCurves: CurveP256, CurveP384` sets `CurveP256` as a higher priority than `CurveP384`.

[NOTE]
====
You must include either `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` or  `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` when you configure the cipher suite. HTTP/2 support requires at least one of these cipher suites.

====

The supported cipher suites are:

* TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
* TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
* TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
* TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
* TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
* TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
* TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
* TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
* TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
* TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
* TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
* TLS_RSA_WITH_AES_128_CBC_SHA256
* TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA

The supported ECDH Curves are:

* CurveP256
* CurveP384
* CurveP521
* X25519

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

[id="ossm-cert-manage_{context}"]
= Adding an external certificate authority key and certificate

By default, {SMProductName} generates a self-signed root certificate and key and uses them to sign the workload certificates. You can also use the user-defined certificate and key to sign workload certificates with user-defined root certificate. This task demonstrates an example to plug certificates and key into {SMProductShortName}.

.Prerequisites

* Install {SMProductName} with mutual TLS enabled to configure certificates.
* This example uses the certificates from the Maistra repository. For production, use your own certificates from your certificate authority.
* Deploy the Bookinfo sample application to verify the results with these instructions.
* OpenSSL is required to verify certificates.

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
