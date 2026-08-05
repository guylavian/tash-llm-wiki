---
title: "SchedulerAsyncAPICalls"
type: reference
domain: openshift
slug: reference-schedulerasyncapicalls
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SchedulerAsyncAPICalls
family: reference
documentKind: "doc"
---

# SchedulerAsyncAPICalls

Change the kube-scheduler to make the entire scheduling cycle free of blocking requests to the Kubernetes API server.
Instead, interact with the Kubernetes API using asynchronous code.
