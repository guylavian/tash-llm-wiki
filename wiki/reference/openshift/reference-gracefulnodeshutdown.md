---
title: "GracefulNodeShutdown"
type: reference
domain: openshift
slug: reference-gracefulnodeshutdown
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/GracefulNodeShutdown
family: reference
documentKind: "doc"
---

# GracefulNodeShutdown

Enables support for graceful shutdown in kubelet.
During a system shutdown, kubelet will attempt to detect the shutdown event
and gracefully terminate pods running on the node. See
[Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
for more details.
