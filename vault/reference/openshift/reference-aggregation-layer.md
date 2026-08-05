---
title: "Aggregation Layer"
type: reference
domain: openshift
slug: reference-aggregation-layer
tier: reference
source: https://kubernetes.io/docs/reference/glossary/aggregation-layer
family: reference
documentKind: "doc"
---

# Aggregation Layer

The aggregation layer lets you install additional Kubernetes-style APIs in your cluster.

<!--more-->

When you've configured the {{< glossary_tooltip text="Kubernetes API Server" term_id="kube-apiserver" >}} to [support additional APIs](/docs/tasks/extend-kubernetes/configure-aggregation-layer/), you can add `APIService` objects to "claim" a URL path in the Kubernetes API.
