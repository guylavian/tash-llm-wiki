---
title: "About OpenShift Service Mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-about
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-about
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# About OpenShift Service Mesh

[id="ossm-about"]
= About OpenShift Service Mesh

[NOTE]
====
Because {SMProductName} releases on a different cadence from OpenShift Container Platform and because the {SMProductName} Operator supports deploying multiple versions of the `ServiceMeshControlPlane`, the {SMProductShortName} documentation does not maintain separate documentation sets for minor versions of the product.  The current documentation set applies to the most recent version of {SMProductShortName} unless version-specific limitations are called out in a particular topic or for a particular feature.

For additional information about the {SMProductName} life cycle and supported platforms, refer to the Platform Life Cycle Policy.
====

Module included in the following assemblies:
* service_mesh/v2x/ossm-about.adoc

[id="ossm-servicemesh-overview_{context}"]
= Introduction to {SMProductName}

{SMProductName} addresses a variety of problems in a microservice architecture by creating a centralized point of control in an application. It adds a transparent layer on existing distributed applications without requiring any changes to the application code.

Microservice architectures split the work of enterprise applications into modular services, which can make scaling and maintenance easier. However, as an enterprise application built on a microservice architecture grows in size and complexity, it becomes difficult to understand and manage. {SMProductShortName} can address those architecture problems by capturing or intercepting traffic between services and can modify, redirect, or create new requests to other services.

{SMProductShortName}, which is based on the open source Istio project, provides an easy way to create a network of deployed services that provides discovery, load balancing, service-to-service authentication, failure recovery, metrics, and monitoring. A service mesh also provides more complex operational functionality, including A/B testing, canary releases, access control, and end-to-end authentication.

[NOTE]
====
{SMProductName} 3 is generally available. For more information, see {SMProductName} 3.0.
====

Module included in the following assemblies:
* service_mesh/v2x/servicemesh-release-notes.adoc

[id="ossm-core-features_{context}"]
= Core features

{SMProductName} provides a number of key capabilities uniformly across a network of services:

* *Traffic Management* - Control the flow of traffic and API calls between services, make calls more reliable, and make the network more robust in the face of adverse conditions.
* *Service Identity and Security* - Provide services in the mesh with a verifiable identity and provide the ability to protect service traffic as it flows over networks of varying degrees of trustworthiness.
* *Policy Enforcement* - Apply organizational policy to the interaction between services, ensure access policies are enforced and resources are fairly distributed among consumers. Policy changes are made by configuring the mesh, not by changing application code.
* *Telemetry* - Gain understanding of the dependencies between services and the nature and flow of traffic between them, providing the ability to quickly identify issues.
