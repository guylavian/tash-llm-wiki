---
title: "ExecProbeTimeout"
type: reference
domain: openshift
slug: reference-execprobetimeout
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ExecProbeTimeout
family: reference
documentKind: "doc"
---

# ExecProbeTimeout

Ensure kubelet respects exec probe timeouts.
This feature gate exists in case any of your existing workloads depend on a
now-corrected fault where Kubernetes ignored exec probe timeouts. See
[readiness probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).
