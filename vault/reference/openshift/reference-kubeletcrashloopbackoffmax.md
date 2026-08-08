---
title: "KubeletCrashLoopBackOffMax"
type: reference
domain: openshift
slug: reference-kubeletcrashloopbackoffmax
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/KubeletCrashLoopBackOffMax
family: reference
documentKind: "doc"
---

# KubeletCrashLoopBackOffMax

Enables support for configurable per-node backoff maximums for restarting
containers in the `CrashLoopBackOff` state.
For more details, check the `crashLoopBackOff.maxContainerRestartPeriod` field in the
[kubelet config file](/docs/reference/config-api/kubelet-config.v1beta1/).
