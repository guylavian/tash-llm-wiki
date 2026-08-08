---
title: "JobTrackingWithFinalizers"
type: reference
domain: openshift
slug: reference-jobtrackingwithfinalizers
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/JobTrackingWithFinalizers
family: reference
documentKind: "doc"
---

# JobTrackingWithFinalizers

Enables tracking [Job](/docs/concepts/workloads/controllers/job)
completions without relying on Pods remaining in the cluster indefinitely.
The Job controller uses Pod finalizers and a field in the Job status to keep
track of the finished Pods to count towards completion.
