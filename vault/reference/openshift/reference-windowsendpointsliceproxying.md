---
title: "WindowsEndpointSliceProxying"
type: reference
domain: openshift
slug: reference-windowsendpointsliceproxying
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/WindowsEndpointSliceProxying
family: reference
documentKind: "doc"
---

# WindowsEndpointSliceProxying

When enabled, kube-proxy running on Windows will use
EndpointSlices as the primary data source instead of Endpoints, enabling scalability and
performance improvements. See
[Enabling Endpoint Slices](/docs/concepts/services-networking/endpoint-slices/).
