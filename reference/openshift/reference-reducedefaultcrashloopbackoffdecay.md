---
title: "ReduceDefaultCrashLoopBackOffDecay"
type: reference
domain: openshift
slug: reference-reducedefaultcrashloopbackoffdecay
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ReduceDefaultCrashLoopBackOffDecay
family: reference
documentKind: "doc"
---

# ReduceDefaultCrashLoopBackOffDecay

Enabled reduction of both the initial delay and the maximum delay accrued
between container restarts for a node for containers in `CrashLoopBackOff`
across the cluster to `1s` initial delay and `60s` maximum delay.
