---
title: "DelegateFSGroupToCSIDriver"
type: reference
domain: openshift
slug: reference-delegatefsgrouptocsidriver
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/DelegateFSGroupToCSIDriver
family: reference
documentKind: "doc"
---

# DelegateFSGroupToCSIDriver

If supported by the CSI driver, delegates the
role of applying `fsGroup` from a Pod's `securityContext` to the driver by
passing `fsGroup` through the NodeStageVolume and NodePublishVolume CSI calls.
