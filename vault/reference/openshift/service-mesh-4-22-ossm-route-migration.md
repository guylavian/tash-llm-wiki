---
title: "Route migration"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-route-migration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-route-migration
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Route migration

[id="ossm-route-migration"]
= Route migration

Automatic route creation, also known as Istio OpenShift Routing (IOR), is a deprecated feature that is disabled by default for any `ServiceMeshControlPlane` resource that was created using {SMProductName} 2.5 and later. Migrating from IOR to explicitly-managed routes provides a more flexible way to manage and configure ingress gateways. When route resources are explicitly created they can be managed alongside the other gateway and application resources as part of a GitOps management model.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-route-migration.adoc

[id="ossm-migrating-from-ior-to-explicitly-managed-routes_{context}"]
= Migrating from Istio OpenShift Routing to explicitly-managed routes

This procedure explains how to disable Istio OpenShift Routing (IOR) in {SMProductName}, and how to continue to use and manage Routes that were originally created using IOR. This procedure also provides an example of how to explicitly create a new Route targeting an existing gateway `Service` object.

.Prerequisites

* Before migrating to explicitly-managed routes, export the existing route configurations managed by Istio OpenShift Routing (IOR) to files. Save the files so that in the future you can recreate the route configurations without requiring IOR.

.Procedure

* Modify the `ServiceMeshControlPlane` resource to disable IOR:
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  gateways:
    openshiftRoute:
      enabled: false
----
+
You can continue to use the old routes that were previously created using IOR or you can create routes that explicitly target the ingress gateway `Service` object. The following example specifies how to create routes that explicitly target the ingress gateway `Service` object:
+
[source,yaml]
----
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  name: example-gateway
  namespace: istio-system <1>
spec:
  host: www.example.com
  to:
    kind: Service
    name: istio-ingressgateway <2>
    weight: 100
  port:
    targetPort: http2
  wildcardPolicy: None
----
<1> Specify new routes in the same namespace as the ingress gateway `Service` object.
<2> Use the name of ingress gateway `Service` object that is the target.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Creating an HTTP-based Route
* Understanding automatic routes
