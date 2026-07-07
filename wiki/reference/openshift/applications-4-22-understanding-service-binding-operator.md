---
title: "Understanding Service Binding Operator"
type: reference
domain: openshift
slug: applications-4-22-understanding-service-binding-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/understanding-service-binding-operator
version: 4.22
family: applications
documentKind: "Documentation"
---

# Understanding Service Binding Operator

[id="understanding-service-binding-operator"]
= Understanding Service Binding Operator

[role="_abstract"]
Application developers need access to backing services to build and connect workloads. Connecting workloads to backing services is always a challenge because each service provider suggests a different way to access their secrets and consume them in a workload. In addition, manual configuration and maintenance of this binding together of workloads and backing services make the process tedious, inefficient, and error-prone.

The {servicebinding-title} enables application developers to easily bind workloads together with Operator-managed backing services, without any manual procedures to configure the binding connection.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

[id="sbo-service-binding-terminology_{context}"]
= Service Binding terminology

This section summarizes the basic terms used in Service Binding.

[horizontal]
Service binding:: The representation of the action of providing information about a service to a workload. Examples include establishing the exchange of credentials between a Java application and a database that it requires.
Backing service:: Any service or software that the application consumes over the network as part of its normal operation. Examples include a database, a message broker, an application with REST endpoints, an event stream, an Application Performance Monitor (APM), or a Hardware Security Module (HSM).
Workload (application):: Any process running within a container. Examples include a Spring Boot application, a NodeJS Express application, or a Ruby on Rails application.
Binding data:: Information about a service that you use to configure the behavior of other resources within the cluster. Examples include credentials, connection details, volume mounts, or secrets.
Binding connection:: Any connection that establishes an interaction between the connected components, such as a bindable backing service and an application requiring that backing service.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

[id="sbo-about-service-binding-operator_{context}"]
= About {servicebinding-title}

The {servicebinding-title} consists of a controller and an accompanying custom resource definition (CRD) for service binding. It manages the data plane for workloads and backing services. The Service Binding Controller reads the data made available by the control plane of backing services. Then, it projects this data to workloads according to the rules specified through the `ServiceBinding` resource.

As a result, the {servicebinding-title} enables workloads to use backing services or external services by automatically collecting and sharing binding data with the workloads. The process involves making the backing service bindable and binding the workload and the service together.

[id="making-an-operator-managed-backing-service-bindable_{context}"]
== Making an Operator-managed backing service bindable
To make a service bindable, as an Operator provider, you need to expose the binding data required by workloads to bind with the services provided by the Operator. You can provide the binding data either as annotations or as descriptors in the CRD of the Operator that manages the backing service.

[id="binding-a-workload-together-with-a-backing-service_{context}"]
== Binding a workload together with a backing service
By using the {servicebinding-title}, as an application developer, you need to declare the intent of establishing a binding connection. You must create a `ServiceBinding` CR  that references the backing service. This action triggers the {servicebinding-title} to project the exposed binding data into the workload. The {servicebinding-title} receives the declared intent and binds the workload together with the backing service.

The CRD of the {servicebinding-title} supports the following APIs:

* *Service Binding* with the `binding.operators.coreos.com` API group.

* *Service Binding (Spec API)* with the `servicebinding.io` API group.

With {servicebinding-title}, you can:

* Bind your workloads to Operator-managed backing services.
* Automate configuration of binding data.
* Provide service operators with a low-touch administrative experience to provision and manage access to services.
* Enrich the development lifecycle with a consistent and declarative service binding method that eliminates discrepancies in cluster environments.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

[id="sbo-key-features_{context}"]
= Key features

* Exposal of binding data from services
** Based on annotations present in CRD, custom resources (CRs), or resources.
// ** Based on descriptors present in Operator Lifecycle Manager (OLM) descriptors.
// When the OLM descriptors are supported again, add this sentence.
* Workload projection
** Projection of binding data as files, with volume mounts.
** Projection of binding data as environment variables.
* Service Binding Options
** Bind backing services in a namespace that is different from the workload namespace.
** Project binding data into the specific container workloads.
** Auto-detection of the binding data from resources owned by the backing service CR.
** Compose custom binding data from the exposed binding data.
** Support for non-`PodSpec` compliant workload resources.
* Security
** Support for role-based access control (RBAC).

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

[id="sbo-api-differences_{context}"]
= API differences

The CRD of the {servicebinding-title} supports the following APIs:

* *Service Binding* with the `binding.operators.coreos.com` API group.
* *Service Binding (Spec API)* with the `servicebinding.io` API group.

Both of these API groups have similar features, but they are not completely identical. Here is the complete list of differences between these API groups:

[cols="1,1,1,1"]
|===
| Feature | Supported by the `binding.operators.coreos.com` API group | Supported by the `servicebinding.io` API group | Notes

| Binding to provisioned services
| Yes
| Yes
| Not applicable (N/A)

| Direct secret projection
| Yes
| Yes
| Not applicable (N/A)

| Bind as files
| Yes
| Yes
a| * Default behavior for the service bindings of the `servicebinding.io` API group
* Opt-in functionality for the service bindings of the `binding.operators.coreos.com` API group

| Bind as environment variables
| Yes
| Yes
a| * Default behavior for the service bindings of the `binding.operators.coreos.com` API group.
* Opt-in functionality for the service bindings of the `servicebinding.io` API group: Environment variables are created alongside files.

| Selecting workload with a label selector
| Yes
| Yes
| Not applicable (N/A)

| Detecting binding resources (`.spec.detectBindingResources`)
| Yes
| No
| The `servicebinding.io` API group has no equivalent feature.

| Naming strategies
| Yes
| No
| There is no current mechanism within the `servicebinding.io` API group to interpret the templates that naming strategies use.

| Container path
| Yes
| Partial
| Because a service binding of the `binding.operators.coreos.com` API group can specify mapping behavior within the `ServiceBinding` resource, the `servicebinding.io` API group cannot fully support an equivalent behavior without more information about the workload.

| Container name filtering
| No
| Yes
| The `binding.operators.coreos.com` API group has no equivalent feature.

| Secret path
| Yes
| No
| The `servicebinding.io` API group has no equivalent feature.

| Alternative binding sources (for example, binding data from annotations)
| Yes
| Allowed by {servicebinding-title}
| The specification requires support for getting binding data from provisioned services and secrets. However, a strict reading of the specification suggests that support for other binding data sources is allowed. Using this fact, {servicebinding-title} can pull the binding data from various sources (for example, pulling binding data from annotations). {servicebinding-title} supports these sources on both the API groups.
|===

[role="_additional-resources"]
[id="additional-resources_understanding-sbo"]
== Additional resources
* Getting started with service binding
