---
title: "Routing overview"
type: reference
domain: openshift
slug: serverless-4-22-routing-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/routing-overview
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Routing overview

[id="routing-overview"]
= Routing overview

Knative leverages OpenShift Container Platform TLS termination to provide routing for Knative services. When a Knative service is created, an OpenShift Container Platform route is automatically created for the service. This route is managed by the {ServerlessOperatorName}. The OpenShift Container Platform route exposes the Knative service through the same domain as the OpenShift Container Platform cluster.

You can disable Operator control of OpenShift Container Platform routing so that you can configure a Knative route to directly use your TLS certificates instead.

Knative routes can also be used alongside the OpenShift Container Platform route to provide additional fine-grained routing capabilities, such as traffic splitting.

[id="additional-resources_serverless-configuring-routes"]
[role="_additional-resources"]
== Additional resources
* Route-specific annotations
