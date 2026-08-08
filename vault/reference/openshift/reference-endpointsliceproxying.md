---
title: "EndpointSliceProxying"
type: reference
domain: openshift
slug: reference-endpointsliceproxying
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/EndpointSliceProxying
family: reference
documentKind: "doc"
---

# EndpointSliceProxying

When enabled, kube-proxy running
 on Linux will use EndpointSlices as the primary data source instead of
 Endpoints, enabling scalability and performance improvements. See
 [Enabling Endpoint Slices](/docs/concepts/services-networking/endpoint-slices/).
