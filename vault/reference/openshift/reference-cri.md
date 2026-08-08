---
title: "Container Runtime Interface (CRI)"
type: reference
domain: openshift
slug: reference-cri
tier: reference
source: https://kubernetes.io/docs/reference/glossary/cri
family: reference
documentKind: "doc"
---

# Container Runtime Interface (CRI)

The main protocol for the communication between the {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} and Container Runtime.

<!--more-->

The Kubernetes Container Runtime Interface (CRI) defines the main
[gRPC](https://grpc.io) protocol for the communication between the
[node components](/docs/concepts/architecture/#node-components)
{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} and
{{< glossary_tooltip text="container runtime" term_id="container-runtime" >}}.
