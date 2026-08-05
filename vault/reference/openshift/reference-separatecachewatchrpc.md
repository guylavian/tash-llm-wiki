---
title: "SeparateCacheWatchRPC"
type: reference
domain: openshift
slug: reference-separatecachewatchrpc
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SeparateCacheWatchRPC
family: reference
documentKind: "doc"
---

# SeparateCacheWatchRPC

Allows the API server watch cache to create a watch on a dedicated RPC.
This prevents watch cache from being starved by other watches.
