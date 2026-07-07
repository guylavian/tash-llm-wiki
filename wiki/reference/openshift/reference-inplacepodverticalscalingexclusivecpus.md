---
title: "InPlacePodVerticalScalingExclusiveCPUs"
type: reference
domain: openshift
slug: reference-inplacepodverticalscalingexclusivecpus
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingExclusiveCPUs
family: reference
documentKind: "doc"
---

# InPlacePodVerticalScalingExclusiveCPUs

Enable resource resizing for containers in Guaranteed pods with integer CPU requests.
It applies only in nodes with `InPlacePodVerticalScaling` and `CPUManager` features enabled,
and the CPUManager policy set to `static`.
