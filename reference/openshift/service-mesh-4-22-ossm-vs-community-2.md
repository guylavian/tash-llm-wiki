---
title: "Service Mesh and Istio differences"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-vs-community-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-vs-community
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Service Mesh and Istio differences

[id="ossm-vs-community-v1x"]
= Service Mesh and Istio differences

An installation of {SMProductName} differs from upstream Istio community installations in multiple ways. The modifications to {SMProductName} are sometimes necessary to resolve issues, provide additional features, or to handle differences when deploying on OpenShift Container Platform.

The current release of {SMProductName} differs from the current upstream Istio community release in the following ways:

// The following include statements pull in the module files that comprise the assembly.

Module included in the following assemblies:
-ossm-vs-community.adoc

[id="ossm-multitenant-install_{context}"]
= Multitenant installations

Whereas upstream Istio takes a single tenant approach, {SMProductName} supports multiple independent control planes within the cluster. {SMProductName} uses a multitenant operator to manage the control plane lifecycle.

{SMProductName} installs a multitenant control plane by default. You specify the projects that can access the {SMProductShortName}, and isolate the {SMProductShortName} from other control plane instances.

[id="ossm-mt-vs-clusterwide_{context}"]
== Multitenancy versus cluster-wide installations

The main difference between a multitenant installation and a cluster-wide installation is the scope of privileges used by istod. The components no longer use cluster-scoped Role Based Access Control (RBAC) resource `ClusterRoleBinding`.

Every project in the `ServiceMeshMemberRoll` `members` list will have a `RoleBinding` for each service account associated with the control plane deployment and each control plane deployment will only watch those member projects. Each member project has a `maistra.io/member-of` label added to it, where the `member-of` value is the project containing the control plane installation.

{SMProductName} configures each member project to ensure network access between itself,
the control plane, and other member projects by creating  a `NetworkPolicy` resource in each
member project allowing ingress to all pods from the other members and the control plane. If you remove a member from {SMProductShortName}, this `NetworkPolicy` resource is deleted
from the project.

[NOTE]
====
This also restricts ingress to only member projects. If you require ingress from non-member
projects, you need to create a `NetworkPolicy` to allow that traffic through.
====

[id="ossm-cluster-scoped-resources_{context}"]
== Cluster scoped resources

Upstream Istio has two cluster scoped resources that it relies on. The `MeshPolicy` and the `ClusterRbacConfig`. These are not compatible with a multitenant cluster and have been replaced as described below.

* _ServiceMeshPolicy_ replaces MeshPolicy for configuration of control-plane-wide authentication policies. This must be created in the same project as the control plane.
* _ServicemeshRbacConfig_ replaces ClusterRbacConfig for configuration of control-plane-wide role based access control. This must be created in the same project as the control plane.

Module included in the following assemblies:
-service_mesh/v1x/ossm-vs-community.adoc

[id="ossm-vs-istio_{context}"]
= Differences between Istio and {SMProductName}

An installation of {SMProductName} differs from an installation of Istio in multiple ways. The modifications to {SMProductName} are sometimes necessary to resolve issues, provide additional features, or to handle differences when deploying on OpenShift Container Platform.

[id="ossm-cli-tool_{context}"]
== Command-line tool

The command-line tool for {SMProductName} is oc.  {SMProductName}  does not support istioctl.

[id="ossm-automatic-injection_{context}"]
== Automatic injection

The upstream Istio community installation automatically injects the sidecar into pods within the projects you have labeled.

{SMProductName} does not automatically inject the sidecar to any pods, but requires you to opt in to injection using an annotation without labeling projects. This method requires fewer privileges and does not conflict with other OpenShift capabilities such as builder pods. To enable automatic injection you specify the `sidecar.istio.io/inject` annotation as described in the Automatic sidecar injection section.

[id="ossm-rbac_{context}"]
== Istio Role Based Access Control features

Istio Role Based Access Control (RBAC) provides a mechanism you can use to control access to a service. You can identify subjects by user name or by specifying a set of properties and apply access controls accordingly.

The upstream Istio community installation includes options to perform exact header matches, match wildcards in headers, or check for a header containing a specific prefix or suffix.

{SMProductName} extends the ability to match request headers by using a regular expression. Specify a property key of `request.regex.headers` with a regular expression.

.Upstream Istio community matching request headers example
[source,yaml]
----
apiVersion: "rbac.istio.io/v1alpha1"
kind: ServiceRoleBinding
metadata:
  name: httpbin-client-binding
  namespace: httpbin
spec:
  subjects:
  - user: "cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account"
    properties:
      request.headers[<header>]: "value"
----

.{SMProductName} matching request headers by using regular expressions
[source,yaml]
----
apiVersion: "rbac.istio.io/v1alpha1"
kind: ServiceRoleBinding
metadata:
  name: httpbin-client-binding
  namespace: httpbin
spec:
  subjects:
  - user: "cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account"
    properties:
      request.regex.headers[<header>]: "<regular expression>"
----

[id="ossm-openssl_{context}"]
== OpenSSL

{SMProductName} replaces BoringSSL with OpenSSL. OpenSSL is a software library that contains an open source implementation of the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols. The {SMProductName} Proxy binary dynamically links the OpenSSL libraries (libssl and libcrypto) from the underlying Red Hat Enterprise Linux operating system.

[id="ossm-component-modifications_{context}"]
== Component modifications

* A _maistra-version_ label has been added to all resources.
* All Ingress resources have been converted to OpenShift Route resources.
* Grafana, Tracing (Jaeger), and Kiali are enabled by default and exposed through OpenShift routes.
* Godebug has been removed from all templates
* The `istio-multi` ServiceAccount and ClusterRoleBinding have been removed, as well as the `istio-reader` ClusterRole.

[id="ossm-envoy-sds-ca_{context}"]
== Envoy, Secret Discovery Service, and certificates

* {SMProductName} does not support QUIC-based services.
* Deployment of TLS certificates using the Secret Discovery Service (SDS) functionality of Istio is not currently supported in {SMProductName}. The Istio implementation depends on a nodeagent container that uses hostPath mounts.

[id="ossm-cni_{context}"]
== Istio Container Network Interface (CNI) plugin

{SMProductName} includes CNI plugin, which provides you with an alternate way to configure application pod networking. The CNI plugin replaces the `init-container` network configuration eliminating the need to grant service accounts and projects access to Security Context Constraints (SCCs) with elevated privileges.

[id="ossm-routes-gateways_{context}"]
== Routes for Istio Gateways

OpenShift routes for Istio Gateways are automatically managed in {SMProductName}. Every time an Istio Gateway is created, updated or deleted inside the service mesh, an OpenShift route is created, updated or deleted.

A {SMProductName} control plane component called Istio OpenShift Routing (IOR) synchronizes the gateway route.  For more information, see Automatic route creation.

[id="ossm-catch-all-domains_{context}"]
=== Catch-all domains
Catch-all domains ("\*") are not supported. If one is found in the Gateway definition, {SMProductName} _will_ create the route, but will rely on OpenShift to create a default hostname. This means that the newly created route will __not__ be a catch all ("*") route, instead it will have a hostname in the form `<route-name>[-<project>].<suffix>`. See the OpenShift documentation for more information about how default hostnames work and how a cluster administrator can customize it.

[id="ossm-subdomains_{context}"]
=== Subdomains
Subdomains (e.g.: "*.domain.com") are supported. However this ability does not come enabled by default in OpenShift Container Platform. This means that {SMProductName} _will_ create the route with the subdomain, but it will only be in effect if OpenShift Container Platform is configured to enable it.

[id="ossm-tls_{context}"]
=== Transport layer security
Transport Layer Security (TLS) is supported. This means that, if the Gateway contains a `tls` section, the OpenShift Route will be configured to support TLS.
[discrete]
[id="additional-resources_ossm-vs-istio-v1x"]
[role="_additional-resources"]
==== Additional resources

* Automatic route creation

This CONCEPT module included in the following assemblies:
-service_mesh/v1x/ossm-vs-community.adoc
-service_mesh/v2x/ossm-vs-community.adoc
[id="ossm-kiali-service-mesh_{context}"]
= Kiali and service mesh

Installing Kiali via the Service Mesh on OpenShift Container Platform differs from community Kiali installations in multiple ways. These modifications are sometimes necessary to resolve issues, provide additional features, or to handle differences when deploying on OpenShift Container Platform.

* Kiali has been enabled by default.
* Ingress has been enabled by default.
* Updates have been made to the Kiali ConfigMap.
* Updates have been made to the ClusterRole settings for Kiali.
* Do not edit the ConfigMap, because your changes might be overwritten by the {SMProductShortName} or Kiali Operators. Files that the Kiali Operator manages have a `kiali.io/` label or annotation. Updating the Operator files should be restricted to those users with `cluster-admin` privileges. If you use {product-dedicated}, updating the Operator files should be restricted to those users with `dedicated-admin` privileges.

This CONCEPT module included in the following assemblies:
-service_mesh/v1x/ossm-vs-community.adoc
-service_mesh/v2x/ossm-vs-community.adoc

[id="ossm-jaeger-service-mesh_{context}"]
= Distributed tracing and service mesh

Installing the {JaegerShortName} with the Service Mesh on OpenShift Container Platform differs from community Jaeger installations in multiple ways. These modifications are sometimes necessary to resolve issues, provide additional features, or to handle differences when deploying on OpenShift Container Platform.

* Distributed tracing has been enabled by default for {SMProductShortName}.
* Ingress has been enabled by default for {SMProductShortName}.
* The name for the Zipkin port name has changed to `jaeger-collector-zipkin` (from `http`)
* Jaeger uses Elasticsearch for storage by default when you select either the `production` or `streaming` deployment option.
* The community version of Istio provides a generic "tracing" route. {SMProductName} uses a "jaeger" route that is installed by the {JaegerName} Operator and is already protected by OAuth.
* {SMProductName} uses a sidecar for the Envoy proxy, and Jaeger also uses a sidecar, for the Jaeger agent.
These two sidecars are configured separately and should not be confused with each other. The proxy sidecar creates spans related to the pod's ingress and egress traffic. The agent sidecar receives the spans emitted by the application and sends them to the Jaeger Collector.
