---
title: BGP (IOS XE)
type: entity
domain: cisco-ios-xe
slug: bgp
summary: "BGP-4 on IOS XE: the interdomain path-vector protocol over TCP/179 — AS_Path loop prevention, 2-byte/4-byte ASNs (asplain vs asdot), one best path per prefix, and the next-hop reachability rule that trips up iBGP."
sources:
  - note:_sources/cisco-ios-xe/bgp-routing.md
provenance:
  extracted: 8
  inferred: 1
  ambiguous: 0
tags: [routing-protocols, concept]
status: reviewed
updated: 2026-06-18
---

# BGP (IOS XE)

**The interdomain path-vector routing protocol: it exchanges loop-free reachability between autonomous systems over TCP port 179, carrying the AS_Path with every route.**

## Path-vector operation
Each route carries the ordered **AS_Path**; a router rejects any update whose AS_Path already contains its own AS (loop prevention). BGP installs **one best path** per prefix by default, and a device runs one BGP process / one AS but many address families. Crucially, a BGP **next hop must be reachable** (usually via the IGP) for a route to be usable.

## AS numbers
2-byte ASNs 1–65535; 4-byte 65536–4294967295. Two notations — **asplain** (default) and **asdot** (`bgp asnotation dot`). Under asdot, a 4-byte regex must escape the literal dot (`1\.14`) and switching notation needs `clear ip bgp *`. Private 2-byte range 64512–65534; Cisco does **not** strip private ASNs unless you configure `neighbor remove-private-as`.

## Next hop & peering
eBGP sets the next hop to the advertising peer's interface IP; **iBGP keeps that next hop unchanged**, so it must be reachable or rewritten (`next-hop-self` for non-reflected routes). eBGP peers are expected directly connected — `neighbor ebgp-multihop` + `update-source loopbackN` (and `disable-connected-check` for single-hop loopback eBGP) relax that for stable loopback peering.

## Scaling
Best-path is driven by **[[bgp-path-attributes]]**; iBGP avoids a full mesh with **[[bgp-route-reflector]]s** (or confederations). Flapping routes can be suppressed with route dampening (penalty 1000, suppress 2000, reuse 750, 15-min half-life — defaults can over-dampen a single reset).

## See also
- [[bgp-path-attributes]]
- [[bgp-route-reflector]]
- [[cisco-administrative-distance]]
- [[ospf]]
- [[cisco-ios-xe-overview]]
- [[cisco-ios-xe-implementation-review]]
