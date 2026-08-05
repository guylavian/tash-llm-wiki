---
title: "StaleControllerConsistencyStatefulSet"
type: reference
domain: openshift
slug: reference-stalecontrollerconsistencystatefulset
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/StaleControllerConsistencyStatefulSet
family: reference
documentKind: "doc"
---

# StaleControllerConsistencyStatefulSet

Enables behavior within the StatefulSet controller to ensure that prior writes to
the API server are observed before proceeding with additional reconciliation for the same StatefulSet.
This is to prevent stale cache from causing incorrect or spurious updates to the StatefulSet.
