---
title: "MemoryQoS"
type: reference
domain: openshift
slug: reference-memoryqos
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/MemoryQoS
family: reference
documentKind: "doc"
---

# MemoryQoS

Enable memory protection and usage throttle on pod / container using
cgroup v2 memory controller. Sets `memory.high` for throttling on Burstable
pods, and optionally sets `memory.min` / `memory.low` for tiered memory
protection when `memoryReservationPolicy` is set to `TieredReservation`.
