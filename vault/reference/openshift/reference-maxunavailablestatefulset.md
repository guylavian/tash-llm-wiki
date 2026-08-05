---
title: "MaxUnavailableStatefulSet"
type: reference
domain: openshift
slug: reference-maxunavailablestatefulset
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/MaxUnavailableStatefulSet
family: reference
documentKind: "doc"
---

# MaxUnavailableStatefulSet

Enables setting the `maxUnavailable` field for the
[rolling update strategy](/docs/concepts/workloads/controllers/statefulset/#rolling-updates)
of a StatefulSet. The field specifies the maximum number of Pods
that can be unavailable during the update.
