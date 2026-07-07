---
title: "SchedulerAsyncPreemption"
type: reference
domain: openshift
slug: reference-schedulerasyncpreemption
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SchedulerAsyncPreemption
family: reference
documentKind: "doc"
---

# SchedulerAsyncPreemption

Enable running some expensive operations within the scheduler, associated with
[preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/), asynchronously.
Asynchronous processing of preemption improves overall Pod scheduling latency.
