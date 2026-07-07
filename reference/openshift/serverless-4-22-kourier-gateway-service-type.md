---
title: "Kourier Gateway service type"
type: reference
domain: openshift
slug: serverless-4-22-kourier-gateway-service-type
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kourier-gateway-service-type
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Kourier Gateway service type

[id="kourier-gateway-service-type"]
= Kourier Gateway service type

The Kourier Gateway is exposed by default as the `ClusterIP` service type. This service type is determined by the `service-type` ingress spec in the `KnativeServing` custom resource (CR).

.Default spec
[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: ClusterIP
...
----

// Kourier Gateway service type
// Module included in the following assemblies
//
// * serverless/knative-serving/external-ingress-routing/kourier-gateway-service-type.adoc

[id="serverless-kourier-gateway-service-type_{context}"]
= Setting the Kourier Gateway service type
// should probably be a procedure but this is out of scope for the abstracts PR

You can override the default service type to use a load balancer service type instead by modifying the `service-type` spec:

.LoadBalancer override spec
[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: LoadBalancer
...
----
