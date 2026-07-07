---
title: "SchedulerQueueingHints"
type: reference
domain: openshift
slug: reference-schedulerqueueinghints
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SchedulerQueueingHints
family: reference
documentKind: "doc"
---

# SchedulerQueueingHints

Enables scheduler [queueing hints](/docs/concepts/scheduling-eviction/scheduling-framework/#queueinghint),
which benefits to reduce the useless requeuing.
The scheduler retries scheduling pods if something changes in the cluster that could make the pod scheduled.
Queueing hints are internal signals that allow the scheduler to filter the changes in the cluster
that are relevant to the unscheduled pod, based on previous scheduling attempts.
