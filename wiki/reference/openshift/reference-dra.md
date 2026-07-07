---
title: "Dynamic Resource Allocation"
type: reference
domain: openshift
slug: reference-dra
tier: reference
source: https://kubernetes.io/docs/reference/glossary/dra
family: reference
documentKind: "doc"
---

# Dynamic Resource Allocation

A Kubernetes feature that lets you request and share resources among Pods.
These resources are often attached
{{< glossary_tooltip text="devices" term_id="device" >}} like hardware
accelerators.

<!--more-->

With DRA, device drivers and cluster admins define device _classes_ that are
available to _claim_ in workloads. Kubernetes allocates matching devices to
specific claims and places the corresponding Pods on nodes that can access the
allocated devices.
