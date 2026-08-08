---
title: "PodAndContainerStatsFromCRI"
type: reference
domain: openshift
slug: reference-podandcontainerstatsfromcri
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/PodAndContainerStatsFromCRI
family: reference
documentKind: "doc"
---

# PodAndContainerStatsFromCRI

Configure the kubelet to gather container and pod stats from the CRI container runtime rather than gathering them from cAdvisor.
As of 1.26, this also includes gathering metrics from CRI and emitting them over `/metrics/cadvisor` (rather than having cAdvisor emit them directly).
