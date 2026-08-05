---
title: "NodeSwap"
type: reference
domain: openshift
slug: reference-nodeswap
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/NodeSwap
family: reference
documentKind: "doc"
---

# NodeSwap

Enable the kubelet to allocate swap memory for Kubernetes workloads on a node.
Must be used with `KubeletConfiguration.failSwapOn` set to false.
For more details, please see [swap memory](/docs/concepts/architecture/nodes/#swap-memory)
