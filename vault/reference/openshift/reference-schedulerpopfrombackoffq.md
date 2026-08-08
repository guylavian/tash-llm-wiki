---
title: "SchedulerPopFromBackoffQ"
type: reference
domain: openshift
slug: reference-schedulerpopfrombackoffq
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SchedulerPopFromBackoffQ
family: reference
documentKind: "doc"
---

# SchedulerPopFromBackoffQ

Improves scheduling queue behavior by popping pods from the backoffQ when the activeQ is empty.
This allows to process potentially schedulable pods ASAP, eliminating a penalty effect of the backoff queue.
