---
title: EtherChannel (IOS XE)
type: entity
domain: cisco-ios-xe
slug: etherchannel
summary: "Bonding links into one logical channel: flow-based 16-bucket load balancing (and its bucket-remap gotchas) plus LACP flow-based 1:1 active/standby redundancy that must be enabled on both ends."
sources:
  - note:_sources/cisco-ios-xe/lan-switching.md
provenance:
  extracted: 6
  inferred: 1
  ambiguous: 0
tags: [etherchannel, concept]
status: reviewed
updated: 2026-06-18
---

# EtherChannel (IOS XE)

**Aggregating several physical links into one logical port channel for more bandwidth and link redundancy, with traffic spread across members by a hash.**

## Flow-based load balancing
On Gigabit EtherChannel, packet-header keys are hashed into one of **16 buckets** per port channel, each bound to one active member link. Flow-based is the global default (`load-balancing flow`), and the **per-port-channel setting overrides the global** one. Default L3 hash is src/dst IP; the 5-tuple hash (16.4.1+) adds L4 ports/protocol. Up to 64 GEC interfaces, 14 members each.

**Gotchas:** changing the load-balancing method — or losing the port channel or its last member link — **deletes the bucket→member mappings**; when a link fails, its buckets are redistributed round-robin to survivors. MPLS traffic balances on src/dst IP only (5-tuple unsupported for MPLS).

## LACP 1:1 redundancy
A two-port LACP channel — one active, one hot-standby — that protects upper layers from a single-link failure with fast switchover: `lacp max-bundle 1` + `lacp fast-switchover`. The link with **higher port priority (lower numeric value)** is active; **equal priorities mean no revert** on recovery. It **must be enabled on both ends** or fast switchover fails; `carrier-delay` tunes how fast link-down is propagated.

## See also
- [[vlans-and-trunking]]
- [[spanning-tree-protocol]]
- [[cisco-ios-xe-overview]]
- [[cisco-ios-xe-implementation-review]]
