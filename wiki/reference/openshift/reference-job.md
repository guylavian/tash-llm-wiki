---
title: "Job"
type: reference
domain: openshift
slug: reference-job
tier: reference
source: https://kubernetes.io/docs/reference/glossary/job
family: reference
documentKind: "doc"
---

# Job

A finite or batch task that runs to completion.

<!--more--> 

Creates one or more {{< glossary_tooltip term_id="pod" >}} objects and ensures that a specified number of them successfully terminate. As Pods successfully complete, the Job tracks the successful completions.
