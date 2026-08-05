---
title: "Pod"
type: reference
domain: openshift
slug: reference-pod
tier: reference
source: https://kubernetes.io/docs/reference/glossary/pod
family: reference
documentKind: "doc"
---

# Pod

The smallest and simplest Kubernetes object. A Pod represents a set of running {{< glossary_tooltip text="containers" term_id="container" >}} on your cluster.

<!--more--> 

A Pod is typically set up to run a single primary container. It can also run optional sidecar containers that add supplementary features like logging. Pods are commonly managed by a {{< glossary_tooltip term_id="deployment" >}}.
