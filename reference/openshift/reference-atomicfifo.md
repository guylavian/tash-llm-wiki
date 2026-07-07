---
title: "AtomicFIFO"
type: reference
domain: openshift
slug: reference-atomicfifo
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/AtomicFIFO
family: reference
documentKind: "doc"
---

# AtomicFIFO

A client-go implementation of a FIFO queue that uses atomic operations to ensure events that come in
batches, such as those from a ListAndWatch call, are processed in a single chunk. This is in contrast to
the previous implementation which would process these events one by one, potentially causing the internal
cache to become temporarily inconsistent with the API server. This feature gate can be toggled in the
kube-controller-manager and any client-go based controller.
