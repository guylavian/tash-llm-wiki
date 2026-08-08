---
title: "Release notes"
type: reference
domain: openshift
slug: serverless-4-22-serverless-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-release-notes
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Release notes

[id="serverless-release-notes"]
= Release notes

[NOTE]
====
For additional information about the {ServerlessProductName} life cycle and supported platforms, refer to the Platform Life Cycle Policy.
====

Release notes contain information about new and deprecated features, breaking changes, and known issues. The following release notes apply for the most recent {ServerlessProductName} releases on OpenShift Container Platform.

For an overview of {ServerlessProductName} functionality, see About {ServerlessProductName}.

[NOTE]
====
{ServerlessProductName} is based on the open source Knative project.

For details about the latest Knative component releases, see the Knative blog.
====

// Module included in the following assemblies:
//
// * serverless/serverless-release-notes.adoc

[id="serverless-api-versions_{context}"]
= About API versions

API versions are an important measure of the development status of certain features and custom resources in {ServerlessProductName}. Creating resources on your cluster that do not use the correct API version can cause issues in your deployment.

The {ServerlessOperatorName} automatically upgrades older resources that use deprecated versions of APIs to use the latest version. For example, if you have created resources on your cluster that use older versions of the `ApiServerSource` API, such as `v1beta1`, the {ServerlessOperatorName} automatically updates these resources to use the `v1` version of the API when this is available and the `v1beta1` version is deprecated.

After they have been deprecated, older versions of APIs might be removed in any upcoming release. Using deprecated versions of APIs does not cause resources to fail. However, if you try to use a version of an API that has been removed, it will cause resources to fail. Ensure that your manifests are updated to use the latest version to avoid issues.
// Module included in the following assemblies:
//
// * serverless/serverless-release-notes.adoc

[id="serverless-tech-preview-features_{context}"]
= Generally Available and Technology Preview features

Features which are Generally Available (GA) are fully supported and are suitable for production use. Technology Preview (TP) features are experimental features and are not intended for production use. See the Technology Preview scope of support on the Red Hat Customer Portal for more information about TP features.

The following table provides information about which {ServerlessProductName} features are GA and which are TP:

// OCP + OSD table
.Generally Available and Technology Preview features tracker
[cols="2,1,1,1",options="header"]
|====
|Feature |1.26|1.27|1.28

|`kn func`
|GA
|GA
|GA

|Quarkus functions
|GA
|GA
|GA

|Node.js functions
|TP
|TP
|GA

|TypeScript functions
|TP
|TP
|GA

|Python functions
|-
|-
|TP

|Service Mesh mTLS
|GA
|GA
|GA

|`emptyDir` volumes
|GA
|GA
|GA

|HTTPS redirection
|GA
|GA
|GA

|Kafka broker
|GA
|GA
|GA

|Kafka sink
|GA
|GA
|GA

|Init containers support for Knative services
|GA
|GA
|GA

|PVC support for Knative services
|GA
|GA
|GA

|TLS for internal traffic
|TP
|TP
|TP

|Namespace-scoped brokers
|-
|TP
|TP

|`multi-container support`
|-
|-
|TP

|====

// ROSA table
.Generally Available and Technology Preview features tracker
[cols="2,1,1,1",options="header"]
|====
|Feature |1.26|1.27|1.28

|`kn func`
|GA
|GA
|GA

|Service Mesh mTLS
|GA
|GA
|GA

|`emptyDir` volumes
|GA
|GA
|GA

|HTTPS redirection
|GA
|GA
|GA

|Kafka broker
|GA
|GA
|GA

|Kafka sink
|TP
|TP
|TP

|Init containers support for Knative services
|GA
|GA
|GA

|PVC support for Knative services
|GA
|GA
|GA

|TLS for internal traffic
|TP
|TP
|TP

|Namespace-scoped brokers
|-
|TP
|TP

|`multi-container support`
|-
|-
|TP

|====
// Module included in the following assemblies:
//
// * serverless/serverless-release-notes.adoc

[id="serverless-deprecated-removed-features_{context}"]
= Deprecated and removed features

Some features that were Generally Available (GA) or a Technology Preview (TP) in previous releases have been deprecated or removed. Deprecated functionality is still included in {ServerlessProductName} and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

For the most recent list of major functionality deprecated and removed within {ServerlessProductName}, refer to the following table:

// OCP + OSD table
.Deprecated and removed features tracker
[cols="3,1,1,1,1,1",options="header"]
|====
|Feature |1.20|1.21|1.22 to 1.26|1.27|1.28

|`KafkaBinding` API
|Deprecated
|Deprecated
|Removed
|Removed
|Removed

|`kn func emit` (`kn func invoke` in 1.21+)
|Deprecated
|Removed
|Removed
|Removed
|Removed

|Serving and Eventing `v1alpha1` API
|-
|-
|-
|Deprecated
|Deprecated

|`enable-secret-informer-filtering` annotation
|-
|-
|-
|-
|Deprecated

|====

// ROSA table
.Deprecated and removed features tracker
[cols="3,1,1,1",options="header"]
|====
|Feature |1.23 to 1.26|1.27|1.28

|`KafkaBinding` API
|Removed
|Removed
|Removed

|`kn func emit` (`kn func invoke` in 1.21+)
|Removed
|Removed
|Removed

|Serving and Eventing `v1alpha1` API
|-
|Deprecated
|Deprecated

|====

// Release notes included, most to least recent
// OCP + OSD + ROSA
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-28-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.28

{ServerlessProductName} 1.28 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-28-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.7.
* {ServerlessProductName} now uses Knative Eventing 1.7.
* {ServerlessProductName} now uses Kourier 1.7.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.7.
* {ServerlessProductName} now uses Knative broker implementation for Apache Kafka 1.7.
* The `kn func` CLI plug-in now uses `func` 1.9.1 version.

* Node.js and TypeScript runtimes for {ServerlessProductName} Functions are now Generally Available (GA).

* Python runtime for {ServerlessProductName} Functions is now available as a Technology Preview.

* Multi-container support for Knative Serving is now available as a Technology Preview. This feature allows you to use a single Knative service to deploy a multi-container pod.

* In {ServerlessProductName} 1.29 or later, the following components of Knative Eventing will be scaled down from two pods to one:
+
--
* `imc-controller`
* `imc-dispatcher`
* `mt-broker-controller`
* `mt-broker-filter`
* `mt-broker-ingress`
--

* The `serverless.openshift.io/enable-secret-informer-filtering` annotation for the Serving CR is now deprecated. The annotation is valid only for Istio, and not for Kourier.
+
With {ServerlessProductName} 1.28, the {ServerlessOperatorName} allows injecting the environment variable `ENABLE_SECRET_INFORMER_FILTERING_BY_CERT_UID` for both `net-istio` and `net-kourier`.
+
If you enable secret filtering, all of your secrets need to be labeled with  `networking.internal.knative.dev/certificate-uid: "<id>"`. Otherwise, Knative Serving does not detect them, which leads to failures. You must label both new and existing secrets.
+
In one of the following {ServerlessProductName} releases, secret filtering will become enabled by default. To prevent failures, label your secrets in advance.

[id="known-issues-1-28-0_{context}"]
== Known issues

* Currently, runtimes for Python are not supported for {ServerlessProductName} Functions on {ibm-power-name}, {ibm-z-name} Systems, and {ibm-linuxone-name}.
+
Node.js, TypeScript, and Quarkus functions are supported on these architectures.

* On the Windows platform, Python functions cannot be locally built, run, or deployed using the Source-to-Image builder due to the `app.sh` file permissions.
+
To work around this problem, use the Windows Subsystem for Linux.

// OCP + OSD + ROSA
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-27_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.27

{ServerlessProductName} 1.27 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[IMPORTANT]
====
{ServerlessProductName} 1.26 is the earliest release that is fully supported on OpenShift Container Platform 4.12. {ServerlessProductName} 1.25 and older does not deploy on OpenShift Container Platform 4.12.

For this reason, before upgrading OpenShift Container Platform to version 4.12, first upgrade {ServerlessProductName} to version 1.26 or 1.27.
====

[id="new-features-1-27_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.6.
* {ServerlessProductName} now uses Knative Eventing 1.6.
* {ServerlessProductName} now uses Kourier 1.6.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.6.
* {ServerlessProductName} now uses Knative Kafka 1.6.
* The `kn func` CLI plug-in now uses `func` 1.8.1.

* Namespace-scoped brokers are now available as a Technology Preview. Such brokers can be used, for instance, to implement role-based access control (RBAC) policies.

* `KafkaSink` now uses the `CloudEvent` binary content mode by default. The binary content mode is more efficient than the structured mode because it uses headers in its body instead of a `CloudEvent`. For example, for the HTTP protocol, it uses HTTP headers.

* You can now use the gRPC framework over the HTTP/2 protocol for external traffic using the OpenShift Route on OpenShift Container Platform 4.10 and later. This improves efficiency and speed of the communications between the client and server.

* API version `v1alpha1` of the Knative Operator Serving and Eventings CRDs is deprecated in 1.27. It will be removed in future versions. Red Hat strongly recommends to use the `v1beta1` version instead. This does not affect the existing installations, because CRDs are updated automatically when upgrading the Serverless Operator.

* The delivery timeout feature is now enabled by default. It allows you to specify the timeout for each sent HTTP request. The feature remains a Technology Preview.

[id="fixed-issues-1-27_{context}"]
== Fixed issues

* Previously, Knative services sometimes did not get into the `Ready` state, reporting waiting for the load balancer to be ready. This issue has been fixed.

[id="known-issues-1-27_{context}"]
== Known issues

* Integrating {ServerlessProductName} with {SMProductName} causes the `net-kourier` pod to run out of memory on startup when too many secrets are present on the cluster.

* Namespace-scoped brokers might leave `ClusterRoleBindings` in the user namespace even after deletion of namespace-scoped brokers.
+
If this happens, delete the `ClusterRoleBinding` named `rbac-proxy-reviews-prom-rb-knative-kafka-broker-data-plane-{{.Namespace}}` in the user namespace.

* If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.
+
To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.

// OCP + OSD + ROSA
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-26_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.26

{ServerlessProductName} 1.26 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1.26_{context}"]
== New features

* {FunctionsProductName} with Quarkus is now GA.
* {ServerlessProductName} now uses Knative Serving 1.5.
* {ServerlessProductName} now uses Knative Eventing 1.5.
* {ServerlessProductName} now uses Kourier 1.5.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.5.
* {ServerlessProductName} now uses Knative Kafka 1.5.
* {ServerlessProductName} now uses Knative Operator 1.3.
* The `kn func` CLI plugin now uses `func` 1.8.1.

* Persistent volume claims (PVCs) are now GA. PVCs provide permanent data storage for your Knative services.

* The new trigger filters feature is now available as a Developer Preview. It allows users to specify a set of filter expressions, where each expression evaluates to either true or false for each event.
+
To enable new trigger filters, add the `new-trigger-filters: enabled` entry in the section of the `KnativeEventing` type in the operator config map:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
...
...
spec:
  config:
    features:
      new-trigger-filters: enabled
...
----

* Knative Operator 1.3 adds the updated `v1beta1` version of the API for `operator.knative.dev`.
+
To update from `v1alpha1` to `v1beta1` in your `KnativeServing` and `KnativeEventing` custom resource config maps, edit the `apiVersion` key:
+
.Example `KnativeServing` custom resource config map
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
...
----
+
.Example `KnativeEventing` custom resource config map
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
...
----

[id="fixed-issues-1.26_{context}"]
== Fixed issues

* Previously, Federal Information Processing Standards (FIPS) mode was disabled for Kafka broker, Kafka source, and Kafka sink. This has been fixed, and FIPS mode is now available.

[id="known-issues-1.26_{context}"]
== Known issues

* If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.
+
To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.
// 1.26.0 additional resources
[role="_additional-resources"]
.Additional resources
* Knative documentation on new trigger filters

// OCP + OSD + ROSA
// Module included in the following assemblies
//
// * serverless/serverless-release-notes.adoc

[id="serverless-rn-1-25-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.25.0

{ServerlessProductName} 1.25.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1.25.0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.4.
* {ServerlessProductName} now uses Knative Eventing 1.4.
* {ServerlessProductName} now uses Kourier 1.4.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.4.
* {ServerlessProductName} now uses Knative Kafka 1.4.
* The `kn func` CLI plugin now uses `func` 1.7.0.

* Integrated development environment (IDE) plugins for creating and deploying functions are now available for Visual Studio Code and IntelliJ.
* Knative Kafka broker is now GA. Knative Kafka broker is a highly performant implementation of the Knative broker API, directly targeting Apache Kafka.
+
It is recommended to not use the MT-Channel-Broker, but the Knative Kafka broker instead.
* Knative Kafka sink is now GA. A `KafkaSink` takes a `CloudEvent` and sends it to an Apache Kafka topic. Events can be specified in either structured or binary content modes.

* Enabling TLS for internal traffic is now available as a Technology Preview.

[id="fixed-issues-1.25.0_{context}"]
== Fixed issues

* Previously, Knative Serving had an issue where the readiness probe failed if the container was restarted after a liveness probe fail. This issue has been fixed.

[id="known-issues-1.25.0_{context}"]
== Known issues

* The Federal Information Processing Standards (FIPS) mode is disabled for Kafka broker, Kafka source, and Kafka sink.

* The `SinkBinding` object does not support custom revision names for services.

* The Knative Serving Controller pod adds a new informer to watch secrets in the cluster. The informer includes the secrets in the cache, which increases memory consumption of the controller pod.
+
If the pod runs out of memory, you can work around the issue by increasing the memory limit for the deployment.

* If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.
+
To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.
// 1.25.0 additional resources, OCP docs
[role="_additional-resources"]
.Additional resources
* Configuring TLS authentication

// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-24-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.24.0

{ServerlessProductName} 1.24.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1.24.0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.3.
* {ServerlessProductName} now uses Knative Eventing 1.3.
* {ServerlessProductName} now uses Kourier 1.3.
* {ServerlessProductName} now uses Knative `kn` CLI 1.3.
* {ServerlessProductName} now uses Knative Kafka 1.3.
* The `kn func` CLI plugin now uses `func` 0.24.

* Init containers support for Knative services is now generally available (GA).

* {ServerlessProductName} logic is now available as a Developer Preview. It enables defining declarative workflow models for managing serverless applications.

* You can now use the cost management service with {ServerlessProductName}.

[id="fixed-issues-1.24.0_{context}"]
== Fixed issues

* Integrating {ServerlessProductName} with {SMProductName} causes the `net-istio-controller` pod to run out of memory on startup when too many secrets are present on the cluster.
+
It is now possible to enable secret filtering, which causes `net-istio-controller` to consider only secrets with a `networking.internal.knative.dev/certificate-uid` label, thus reducing the amount of memory needed.

* The {FunctionsProductName} Technology Preview now uses Cloud Native Buildpacks by default to build container images.

[id="known-issues-1-24-0_{context}"]
== Known issues

* The Federal Information Processing Standards (FIPS) mode is disabled for Kafka broker, Kafka source, and Kafka sink.

* In {ServerlessProductName} 1.23, support for KafkaBindings and the `kafka-binding` webhook were removed. However, an existing `kafkabindings.webhook.kafka.sources.knative.dev MutatingWebhookConfiguration` might remain, pointing to the `kafka-source-webhook` service, which no longer exists.
+
For certain specifications of KafkaBindings on the cluster, `kafkabindings.webhook.kafka.sources.knative.dev MutatingWebhookConfiguration` might be configured to pass any create and update events to various resources, such as Deployments, Knative Services, or Jobs, through the webhook, which would then fail.
+
To work around this issue, manually delete `kafkabindings.webhook.kafka.sources.knative.dev MutatingWebhookConfiguration` from the cluster after upgrading to {ServerlessProductName} 1.23:
+
[source,terminal]
----
$ oc delete mutatingwebhookconfiguration kafkabindings.webhook.kafka.sources.knative.dev
----

* If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.
+
To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-23-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.23.0

{ServerlessProductName} 1.23.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-23-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.2.
* {ServerlessProductName} now uses Knative Eventing 1.2.
* {ServerlessProductName} now uses Kourier 1.2.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.2.
* {ServerlessProductName} now uses Knative Kafka 1.2.
* The `kn func` CLI plugin now uses `func` 0.24.

* It is now possible to use the `kafka.eventing.knative.dev/external.topic` annotation with the Kafka broker. This annotation makes it possible to use an existing externally managed topic instead of the broker creating its own internal topic.

* The `kafka-ch-controller` and `kafka-webhook` Kafka components no longer exist. These components have been replaced by the `kafka-webhook-eventing` component.

* The {FunctionsProductName} Technology Preview now uses Source-to-Image (S2I) by default to build container images.

not identified yet

[id="fixed-issues-1-23-0_{context}"]
== Fixed issues

[id="known-issues-1-23-0_{context}"]
== Known issues

* The Federal Information Processing Standards (FIPS) mode is disabled for Kafka broker, Kafka source, and Kafka sink.

* If you delete a namespace that includes a Kafka broker, the namespace finalizer may fail to be removed if the broker's `auth.secret.ref.name` secret is deleted before the broker.

* Running {ServerlessProductName} with a large number of Knative services can cause Knative activator pods to run close to their default memory limits of 600MB. These pods might be restarted if memory consumption reaches this limit. Requests and limits for the activator deployment can be configured by modifying the `KnativeServing` custom resource:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  deployments:
  - name: activator
    resources:
    - container: activator
      requests:
        cpu: 300m
        memory: 60Mi
      limits:
        cpu: 1000m
        memory: 1000Mi
----

* If you are using Cloud Native Buildpacks as the local build strategy for a function, `kn func` is unable to automatically start podman or use an SSH tunnel to a remote daemon. The workaround for these issues is to have a Docker or podman daemon already running on the local development computer before deploying a function.

* On-cluster function builds currently fail for Quarkus and Golang runtimes. They work correctly for Node, Typescript, Python, and Springboot runtimes.

* If you use `net-istio` for Ingress and enable mTLS via SMCP using `security.dataPlane.mtls: true`, Service Mesh deploys `DestinationRules` for the `*.local` host, which does not allow `DomainMapping` for {ServerlessProductName}.
+
To work around this issue, enable mTLS by deploying `PeerAuthentication` instead of using `security.dataPlane.mtls: true`.

// 1.23.0 additional resources, OCP docs
[role="_additional-resources"]
.Additional resources
* Source-to-Image

// OSD + OCP
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-22-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.22.0

{ServerlessProductName} 1.22.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-22-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.1.
* {ServerlessProductName} now uses Knative Eventing 1.1.
* {ServerlessProductName} now uses Kourier 1.1.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.1.
* {ServerlessProductName} now uses Knative Kafka 1.1.
* The `kn func` CLI plugin now uses `func` 0.23.
* Init containers support for Knative services is now available as a Technology Preview.
* Persistent volume claim (PVC) support for Knative services is now available as a Technology Preview.
* The `knative-serving`, `knative-serving-ingress`, `knative-eventing` and `knative-kafka` system namespaces now have the `knative.openshift.io/part-of: "openshift-serverless"` label by default.
* The *Knative Eventing - Kafka Broker/Trigger* dashboard has been added, which allows visualizing Kafka broker and trigger metrics in the web console.
* The *Knative Eventing - KafkaSink* dashboard has been added, which allows visualizing KafkaSink metrics in the web console.
* The *Knative Eventing - Broker/Trigger* dashboard is now called *Knative Eventing - Channel-based Broker/Trigger*.
* The `knative.openshift.io/part-of: "openshift-serverless"` label has substituted the `knative.openshift.io/system-namespace` label.
* Naming style in Knative Serving YAML configuration files changed from camel case (`ExampleName`) to hyphen style (`example-name`). Beginning with this release, use the hyphen style notation when creating or editing Knative Serving YAML configuration files.

[id="known-issues-1-22-0_{context}"]
== Known issues

* The Federal Information Processing Standards (FIPS) mode is disabled for Kafka broker, Kafka source, and Kafka sink.
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-21-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.21.0

{ServerlessProductName} 1.21.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-21-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.0
* {ServerlessProductName} now uses Knative Eventing 1.0.
* {ServerlessProductName} now uses Kourier 1.0.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.0.
* {ServerlessProductName} now uses Knative Kafka 1.0.
* The `kn func` CLI plugin now uses `func` 0.21.
* The Kafka sink is now available as a Technology Preview.

* The Knative open source project has begun to deprecate camel-cased configuration keys in favor of using kebab-cased keys consistently. As a result, the `defaultExternalScheme` key, previously mentioned in the {ServerlessProductName} 1.18.0 release notes, is now deprecated and replaced by the `default-external-scheme` key. Usage instructions for the key remain the same.

[id="fixed-issues-1-21-0_{context}"]
== Fixed issues

* In {ServerlessProductName} 1.20.0, there was an event delivery issue affecting the use of `kn event send` to send events to a service. This issue is now fixed.

* In {ServerlessProductName} 1.20.0 (`func` 0.20), TypeScript functions created with the `http` template failed to deploy on the cluster. This issue is now fixed.

* In {ServerlessProductName} 1.20.0 (`func` 0.20), deploying a function using the `gcr.io` registry failed with an error. This issue is now fixed.

* In {ServerlessProductName} 1.20.0 (`func` 0.20), creating a Springboot function project directory with the `kn func create` command and then running the `kn func build` command failed with an error message. This issue is now fixed.

* In {ServerlessProductName} 1.19.0 (`func` 0.19), some runtimes were unable to build a function by using podman. This issue is now fixed.

[id="known-issues-1-21-0_{context}"]
== Known issues

* Currently, the domain mapping controller cannot process the URI of a broker, which contains a path that is currently not supported.
+
This means that, if you want to use a `DomainMapping` custom resource (CR) to map a custom domain to a broker, you must configure the `DomainMapping` CR with the broker's ingress service, and append the exact path of the broker to the custom domain:
+
.Example `DomainMapping` CR
[source,yaml]
----
apiVersion: serving.knative.dev/v1alpha1
kind: DomainMapping
metadata:
  name: <domain-name>
  namespace: knative-eventing
spec:
  ref:
    name: broker-ingress
    kind: Service
    apiVersion: v1
----
+
The URI for the broker is then `<domain-name>/<broker-namespace>/<broker-name>`.
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-20-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.20.0

{ServerlessProductName} 1.20.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-20-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 0.26.
* {ServerlessProductName} now uses Knative Eventing 0.26.
* {ServerlessProductName} now uses Kourier 0.26.
* {ServerlessProductName} now uses Knative (`kn`) CLI 0.26.
* {ServerlessProductName} now uses Knative Kafka 0.26.
* The `kn func` CLI plugin now uses `func` 0.20.

* The Kafka broker is now available as a Technology Preview.
+
[IMPORTANT]
====
The Kafka broker, which is currently in Technology Preview, is not supported on FIPS.
====

* The `kn event` plugin is now available as a Technology Preview.

* The `--min-scale` and `--max-scale` flags for the `kn service create` command have been deprecated. Use the `--scale-min` and `--scale-max` flags instead.

[id="known-issues-1-20-0_{context}"]
== Known issues

* {ServerlessProductName} deploys Knative services with a default address that uses HTTPS. When sending an event to a resource inside the cluster, the sender does not have the cluster certificate authority (CA) configured. This causes event delivery to fail, unless the cluster uses globally accepted certificates.
+
For example, an event delivery to a publicly accessible address works:
+
[source,terminal]
----
$ kn event send --to-url https://ce-api.foo.example.com/
----
+
On the other hand, this delivery fails if the service uses a public address with an HTTPS certificate issued by a custom CA:
+
[source,terminal]
----
$ kn event send --to Service:serving.knative.dev/v1:event-display
----
+
Sending an event to other addressable objects, such as brokers or channels, is not affected by this issue and works as expected.

* The Kafka broker currently does not work on a cluster with Federal Information Processing Standards (FIPS) mode enabled.

* If you create a Springboot function project directory with the `kn func create` command, subsequent running of the `kn func build` command fails with this error message:
+
[source,terminal]
----
[analyzer] no stack metadata found at path ''
[analyzer] ERROR: failed to : set API for buildpack 'paketo-buildpacks/ca-certificates@3.0.2': buildpack API version '0.7' is incompatible with the lifecycle
----
+
As a workaround, you can change the `builder` property to `gcr.io/paketo-buildpacks/builder:base` in the function configuration file `func.yaml`.

* Deploying a function using the `gcr.io` registry fails with this error message:
+
[source,terminal]
----
Error: failed to get credentials: failed to verify credentials: status code: 404
----
+
As a workaround, use a different registry than `gcr.io`, such as `quay.io` or `docker.io`.

* TypeScript functions created with the `http` template fail to deploy on the cluster.
+
As a workaround, in the `func.yaml` file, replace the following section:
+
[source,terminal]
----
buildEnvs: []
----
+
with this:
+
[source,terminal]
----
buildEnvs:
- name: BP_NODE_RUN_SCRIPTS
  value: build
----

* In `func` version 0.20, some runtimes might be unable to build a function by using podman. You might see an error message similar to the following:
+
[source,terminal]
----
ERROR: failed to image: error during connect: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.40/info": EOF
----
+
** The following workaround exists for this issue:

.. Update the podman service by adding `--time=0` to the service `ExecStart` definition:
+
.Example service configuration
[source,terminal]
----
ExecStart=/usr/bin/podman $LOGGING system service --time=0
----
.. Restart the podman service by running the following commands:
+
[source,terminal]
----
$ systemctl --user daemon-reload
----
+
[source,terminal]
----
$ systemctl restart --user podman.socket
----

** Alternatively, you can expose the podman API by using TCP:
+
[source,terminal]
----
$ podman system service --time=0 tcp:127.0.0.1:5534 &
export DOCKER_HOST=tcp://127.0.0.1:5534
----

// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-19-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.19.0

{ServerlessProductName} 1.19.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-19-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 0.25.
* {ServerlessProductName} now uses Knative Eventing 0.25.
* {ServerlessProductName} now uses Kourier 0.25.
* {ServerlessProductName} now uses Knative (`kn`) CLI 0.25.
* {ServerlessProductName} now uses Knative Kafka 0.25.
* The `kn func` CLI plugin now uses `func` 0.19.

* The `KafkaBinding` API is deprecated in {ServerlessProductName} 1.19.0 and will be removed in a future release.

* HTTPS redirection is now supported and can be configured either globally for a cluster or per each Knative service.

[id="fixed-issues-1-19-0_{context}"]
== Fixed issues

* In previous releases, the Kafka channel dispatcher waited only for the local commit to succeed before responding, which might have caused lost events in the case of an Apache Kafka node failure. The Kafka channel dispatcher now waits for all in-sync replicas to commit before responding.

[id="known-issues-1-19-0_{context}"]
== Known issues

* In `func` version 0.19, some runtimes might be unable to build a function by using podman. You might see an error message similar to the following:
+
[source,terminal]
----
ERROR: failed to image: error during connect: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.40/info": EOF
----
+
** The following workaround exists for this issue:

.. Update the podman service by adding `--time=0` to the service `ExecStart` definition:
+
.Example service configuration
[source,terminal]
----
ExecStart=/usr/bin/podman $LOGGING system service --time=0
----
.. Restart the podman service by running the following commands:
+
[source,terminal]
----
$ systemctl --user daemon-reload
----
+
[source,terminal]
----
$ systemctl restart --user podman.socket
----

** Alternatively, you can expose the podman API by using TCP:
+
[source,terminal]
----
$ podman system service --time=0 tcp:127.0.0.1:5534 &
export DOCKER_HOST=tcp://127.0.0.1:5534
----
// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

[id="serverless-rn-1-18-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.18.0

{ServerlessProductName} 1.18.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on OpenShift Container Platform are included in this topic.

[id="new-features-1-18-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 0.24.0.
* {ServerlessProductName} now uses Knative Eventing 0.24.0.
* {ServerlessProductName} now uses Kourier 0.24.0.
* {ServerlessProductName} now uses Knative (`kn`) CLI 0.24.0.
* {ServerlessProductName} now uses Knative Kafka 0.24.7.
* The `kn func` CLI plugin now uses `func` 0.18.0.
* In the upcoming {ServerlessProductName} 1.19.0 release, the URL scheme of external routes will default to HTTPS for enhanced security.
+
If you do not want this change to apply for your workloads, you can override the default setting before upgrading to 1.19.0, by adding the following YAML to your `KnativeServing` custom resource (CR):
+
[source,yaml]
----
...
spec:
  config:
    network:
      defaultExternalScheme: "http"
...
----
+
If you want the change to apply in 1.18.0 already, add the following YAML:
+
[source,yaml]
----
...
spec:
  config:
    network:
      defaultExternalScheme: "https"
...
----

* In the upcoming {ServerlessProductName} 1.19.0 release, the default service type by which the Kourier Gateway is exposed will be `ClusterIP` and not `LoadBalancer`.
+
If you do not want this change to apply to your workloads, you can override the default setting before upgrading to 1.19.0, by adding the following YAML to your `KnativeServing` custom resource (CR):
+
[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: LoadBalancer
...
----

* You can now use `emptyDir` volumes with {ServerlessProductName}. See the {ServerlessProductName} documentation about Knative Serving for details.

* Rust templates are now available when you create a function using `kn func`.

[id="fixed-issues-1-18-0_{context}"]
== Fixed issues

* The prior 1.4 version of Camel-K was not compatible with {ServerlessProductName} 1.17.0. The issue in Camel-K has been fixed, and Camel-K version 1.4.1 can be used with {ServerlessProductName} 1.17.0.

* Previously, if you created a new subscription for a Kafka channel, or a new Kafka source, a delay was possible in the Kafka data plane becoming ready to dispatch messages after the newly created subscription or sink reported a ready status.
+
As a result, messages that were sent during the time when the data plane was not reporting a ready status, might not have been delivered to the subscriber or sink.
+
In {ServerlessProductName} 1.18.0, the issue is fixed and the initial messages are no longer lost. For more information about the issue, see Knowledgebase Article #6343981.

[id="known-issues-1-18-0_{context}"]
== Known issues

* Older versions of the Knative `kn` CLI might use older versions of the Knative Serving and Knative Eventing APIs. For example, version 0.23.2 of the `kn` CLI uses the `v1alpha1` API version.
+
On the other hand, newer releases of {ServerlessProductName} might no longer support older API versions. For example, {ServerlessProductName} 1.18.0 no longer supports version `v1alpha1` of the `kafkasources.sources.knative.dev` API.
+
Consequently, using an older version of the Knative `kn` CLI with a newer {ServerlessProductName} might produce an error because the `kn` cannot find the outdated API. For example, version 0.23.2 of the `kn` CLI does not work with {ServerlessProductName} 1.18.0.
+
To avoid issues, use the latest `kn` CLI version available for your {ServerlessProductName} release. For {ServerlessProductName} 1.18.0, use Knative `kn` CLI 0.24.0.
