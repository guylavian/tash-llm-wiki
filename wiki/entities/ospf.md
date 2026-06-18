---
title: OSPF (IOS XE)
type: entity
domain: cisco-ios-xe
slug: ospf
summary: "OSPFv2 on IOS XE: a link-state IGP — network types and DR/BDR, cost from a tunable reference bandwidth, loopback-stable router ID, NSSA Type-7↔Type-5 translation, and the matched hello/dead/auth that adjacency depends on."
sources:
  - note:_sources/cisco-ios-xe/ospf-routing.md
provenance:
  extracted: 9
  inferred: 1
  ambiguous: 0
tags: [routing-protocols, security, concept]
status: reviewed
updated: 2026-06-18
---

# OSPF (IOS XE)

**A link-state interior gateway protocol (RFC 2328) that floods LSAs within areas and runs SPF to build a loop-free routing table.**

## Network types & DR/BDR
OSPF auto-classifies media into **broadcast**, **NBMA**, and **point-to-point**; `ip ospf network {broadcast | non-broadcast | point-to-point | point-to-multipoint [non-broadcast]}` overrides it. **Broadcast and NBMA elect a DR/BDR; point-to-point and point-to-multipoint do not.** Point-to-multipoint models a partial-mesh/hub-spoke cloud as numbered P2P links on one subnet — no full mesh, no DR; its `non-broadcast` variant needs explicit `neighbor` statements and is the only way to set per-neighbor cost.

## Cost
cost = `auto-cost reference-bandwidth` ÷ interface-bandwidth (or set with `ip ospf cost`). The **default reference is 100 Mbps**, so every GigE/10GigE link computes to cost 1 and becomes indistinguishable — raise the reference *consistently on all routers*.

## Router ID
Chosen as the **highest loopback IP**, else the highest active interface IP. Losing the interface that owns the ID forces a recompute and a full re-flood — always configure a loopback for a stable ID.

## NSSA
A Not-So-Stubby Area forbids Type-5 externals but lets an NSSA ASBR originate **Type-7** LSAs; the NSSA ABR translates Type-7→Type-5 into the backbone (`area id nssa …`, `translate type7 always`). All routers in the area must agree it is NSSA or adjacency fails.

## Timers & authentication
`ip ospf hello-interval` / `dead-interval` (**defaults to 4× hello**) must match on a segment, or neighbors never reach FULL. Authentication is plaintext (`authentication-key`) or **MD5** (`message-digest-key key-id md5 key`), matched exactly on both ends; `ip ospf priority 0` makes a router ineligible for DR/BDR. SPF throttle `timers throttle spf` takes **millisecond** values (a common misconfig).

## See also
- [[cisco-administrative-distance]]
- [[route-redistribution-and-route-maps]]
- [[bgp]]
- [[cisco-ios-xe-overview]]
- [[cisco-ios-xe-implementation-review]]
