---
title: "KubeletTracing"
type: reference
domain: openshift
slug: reference-kubelettracing
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/KubeletTracing
family: reference
documentKind: "doc"
---

# KubeletTracing

Add support for distributed tracing in the kubelet.
When enabled, kubelet CRI interface and authenticated http servers are instrumented to generate
OpenTelemetry trace spans.
See [Traces for Kubernetes System Components](/docs/concepts/cluster-administration/system-traces) for more details.
