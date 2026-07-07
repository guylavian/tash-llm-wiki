---
title: "DRADeviceTaintRules"
type: reference
domain: openshift
slug: reference-dradevicetaintrules
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/DRADeviceTaintRules
family: reference
documentKind: "doc"
---

# DRADeviceTaintRules

Enables support for
[tainting devices through DeviceTaintRule objects](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#device-taints-and-tolerations)
when using dynamic resource allocation to manage devices.

This feature gate has no effect unless you also enable the `DRADeviceTaint` feature gate.
