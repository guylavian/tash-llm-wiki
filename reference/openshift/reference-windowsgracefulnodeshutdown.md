---
title: "WindowsGracefulNodeShutdown"
type: reference
domain: openshift
slug: reference-windowsgracefulnodeshutdown
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/WindowsGracefulNodeShutdown
family: reference
documentKind: "doc"
---

# WindowsGracefulNodeShutdown

Enables support for windows node graceful shutdown in kubelet.
During a system shutdown, kubelet will attempt to detect the shutdown event
and gracefully terminate pods running on the node. See
[Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
for more details.
