---
title: "PodObservedGenerationTracking"
type: reference
domain: openshift
slug: reference-podobservedgenerationtracking
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/PodObservedGenerationTracking
family: reference
documentKind: "doc"
---

# PodObservedGenerationTracking

Enables the kubelet to set `observedGeneration` in the Pod `.status`, and enables other components to set `observedGeneration` in pod conditions.
This feature allows reflecting the `.metadata.generation` of the Pod at the time that the overall status, or some specific condition, was being recorded.
Storing it helps avoid risks associated with _lost updates_.
