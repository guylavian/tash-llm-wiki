---
title: "ElasticIndexedJob"
type: reference
domain: openshift
slug: reference-elasticindexedjob
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ElasticIndexedJob
family: reference
documentKind: "doc"
---

# ElasticIndexedJob

Enables Indexed Jobs to be scaled up or down by mutating both
`spec.completions` and `spec.parallelism` together such that `spec.completions == spec.parallelism`.
See docs on [elastic Indexed Jobs](/docs/concepts/workloads/controllers/job#elastic-indexed-jobs)
for more details.
