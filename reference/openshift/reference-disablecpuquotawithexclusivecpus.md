---
title: "DisableCPUQuotaWithExclusiveCPUs"
type: reference
domain: openshift
slug: reference-disablecpuquotawithexclusivecpus
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/DisableCPUQuotaWithExclusiveCPUs
family: reference
documentKind: "doc"
---

# DisableCPUQuotaWithExclusiveCPUs

When the feature gate `DisableCPUQuotaWithExclusiveCPUs` is enabled (the default), then Kubernetes
does **not** enforce CPU quota for Pods that use the [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
{{< glossary_tooltip text="QoS class" term_id="qos-class" >}}.

You can disable the `DisableCPUQuotaWithExclusiveCPUs` feature gate to restore the legacy behavior.
