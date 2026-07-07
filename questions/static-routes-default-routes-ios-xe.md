---
title: What are static routes and default routes on IOS XE?
type: question
domain: cisco-ios-xe
slug: static-routes-default-routes-ios-xe
summary: "Static routes are user-defined paths with AD 1; default routes set the gateway of last resort via one of three mechanisms. Key traps: interface-pointing statics behave as connected, and 0.0.0.0/0 statics don't propagate into OSPF/IS-IS."
sources:
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
provenance:
  extracted: 5
  inferred: 0
  ambiguous: 0
status: reviewed
updated: 2026-07-07
---

# What are static routes and default routes on IOS XE?

**Static routes** are manually defined paths in the RIB, configured with `ip route prefix mask {next-hop-ip | interface [next-hop]} [distance] [name] [permanent | track n] [tag]`. They have a **default administrative distance of 1** (highest trust), and up to 6 parallel paths are supported per prefix. A static route is removed when its outbound interface goes down or its next hop becomes unreachable.

Two traps:

- A static pointing to an **interface** (not a next-hop IP) is treated as *connected* and gets advertised by RIP/EIGRP even without `redistribute static`.
- A **floating static** (distance raised above the dynamic protocol, e.g. `ip route … 110`) only wins when the dynamic route disappears — see [[cisco-administrative-distance]].

**Default routes / gateway of last resort** define where traffic goes when no specific route matches. Three approaches, different scopes:

| Command | Scope |
|---|---|
| `ip default-gateway` | Only when IP routing is **disabled** (boot/host mode) |
| `ip default-network` | Routing enabled; flags a known network as the default candidate |
| `ip route 0.0.0.0 0.0.0.0 next-hop` | A static default route — works in most protocols |

**Propagation differs by protocol:** IGRP doesn't recognize `0.0.0.0/0` statics (use `ip default-network`); EIGRP propagates `0.0.0.0` only if the static is explicitly redistributed; **OSPF and IS-IS do not advertise or redistribute a `0.0.0.0/0` static — inject it with `default-information originate`**.

## References

**Source notes:**
- `note:_sources/cisco-ios-xe/protocol-independent-routing.md` — Static & floating static routes, default routes / gateway of last resort, per-protocol propagation

**Wiki pages:**
- [[static-and-default-routes]]
- [[cisco-administrative-distance]]
