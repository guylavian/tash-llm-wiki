---
title: How to redistribute OSPF routes into eBGP on IOS XE
type: question
question_tier: support-kb
domain: cisco-ios-xe
slug: redistribute-ospf-into-ebgp
summary: "Redistribute OSPFv2 routes into an eBGP process on Cisco IOS XE — the `redistribute ospf` command under `router bgp`, controlling which routes are injected with a route map, setting the MED, and the key gotchas (metric translation, eBGP next-hop reachability, static default caveat)."
sources:
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
  - note:_sources/cisco-ios-xe/bgp-routing.md
  - note:_sources/cisco-ios-xe/ospf-routing.md
  - kb:cisco-pi-basic-ip-routing
  - kb:cisco-bgp-configuring-a-basic-bgp-network
  - kb:cisco-bgp-cisco-bgp-overview
provenance_extracted: 7
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "Redistributed OSPF routes not advertised (missing metric)"
  - "Redistributed routes have Origin incomplete / empty AS_Path"
tags: [routing-protocols, ip-routing, concept, procedure]
status: draft
updated: 2026-07-02
---

# How to redistribute OSPF routes into eBGP on IOS XE

> ⚠️ Out of corpus coverage — `cisco-ios-xe` holds `conceptual` only; this is a `support-kb` question and that tier is not ingested; verify against the primary source.

**Configure `redistribute ospf <pid>` under `router bgp <asn>` to inject OSPF-learned routes into the BGP table, optionally filtered and rewritten by a route map — then BGP advertises them to eBGP peers subject to standard BGP export policy.**

## Basic configuration

Enter `router bgp` for your AS, then issue the `redistribute ospf` subcommand:

```
router bgp 65000
 redistribute ospf 1 metric 10
```

This takes routes from OSPF process 1 (internal routes by default — see below), assigns them a BGP MED of 10 (`set metric` in route-map terms), and places them in the BGP table. From there they are eligible for advertisement to eBGP neighbors (subject to outbound policy and reachability).

## Filtering with a route map

When redistributing OSPF into BGP, only OSPF **internal** (intra-area + inter-area) routes are redistributed by default — external (Type‑5/‑7) routes require an explicit `match external 1 external 2` on the `redistribute` line or a route map matching `route-type external` (inferred — the ingested guide shows only the `match internal` form; confirm against the `redistribute` command reference for your release). Use a route map to control *which* OSPF routes are injected:

```
router bgp 65000
 redistribute ospf 1 route-map OSPF-TO-BGP
!
route-map OSPF-TO-BGP permit 10
 match route-type internal          ! only intra-area + inter-area, not external
 set metric 10
!
route-map OSPF-TO-BGP permit 20
 match route-type external
 match tag 100                      ! only external routes tagged 100
 set metric 50
```

The example above redistributes OSPF intra-area/inter-area routes with MED 10, and OSPF external (Type‑5/‑7) routes tagged 100 with MED 50. A route map with no `match` clause matches everything; with no `set` clause it modifies nothing.

## The canonical Cisco example

From the IOS XE 3S *Protocol-Independent Configuration Guide*, redistributing OSPF intra-area and inter-area routes with next hops on a specific serial interface into BGP with an INTER_AS metric of 5:

```
router bgp 50000
 redistribute ospf 1 route-map 10
!
route-map 10 permit
 match route-type internal
 match interface serial 0/0/0
 set metric 5
```

(kb:cisco-pi-basic-ip-routing)

## How eBGP handles redistributed OSPF routes

- **Origin attribute**: Routes redistributed into BGP (including OSPF) have Origin set to **incomplete** by default — not IGP. This affects best-path selection (the AS_Path length comparision). A route map can `set origin igp` to override.
- **Next hop**: BGP keeps the IGP next hop for redistributed routes. For eBGP advertisements, check that the next hop is **reachable** from the eBGP peer and that `next-hop-self` is configured on the neighbor if the OSPF next hop isn't on a directly connected subnet (inferred).
- **MED**: The metric you set via `redistribute ... metric` or `set metric` in the route map becomes the **MULTI_EXIT_DISC** (MED) attribute, compared only between paths from the same neighbor AS unless `bgp always-compare-med` is configured. Cisco's default treats a missing MED as 0 (most preferred) — use `bgp bestpath med missing-as-worst` to conform to IETF behavior.
- **AS_Path**: Redistributed OSPF routes have an **empty AS_Path** (they originate in your AS). They carry no AS to prepend unless you use `set as-path prepend ...` in the route map.

## Key gotchas

1. **Metric translation**: Metrics don't translate across protocols — OSPF cost has no meaning to BGP. You **must** supply a metric value (either via `redistribute ... metric <n>` or `default-metric <n>` under `router bgp`). A missing metric produces an incomplete configuration and may cause the route to not be advertised.
2. **The 0.0.0.0/0 default route**: A static default (`ip route 0.0.0.0 0.0.0.0 <next-hop>`) is **not** automatically redistributed into BGP — you must `redistribute static` or originate via `network 0.0.0.0`. For OSPF routes specifically, a default learned from OSPF `default-information originate` *can* be redistributed into BGP via `redistribute ospf` when it exists in the routing table (inferred).
3. **eBGP multihop**: If the eBGP peer is **not** directly connected (common when advertising redistributed routes to a neighbour at a data-centre exchange), the eBGP multihop hop-count must permit it: `neighbor <ip> ebgp-multihop 2` and `neighbor <ip> update-source loopback<N>`.
4. **`no redistribute` is subtractive under BGP**: Removing a `redistribute ospf 1 route-map FOO` with `no redistribute ospf 1 route-map FOO` removes just the named keyword (additive removal). Using `no redistribute ospf 1` removes the entire redistribute statement.
5. **Route-map modification after redistribution**: If you later remove the route-map (`no route-map OSPF-TO-BGP`), redistribution continues **without** the filter — which may flood unexpected routes. Always pair the removal with `no redistribute ospf ...` or replace the route-map with a deny-all variant.

## Contradictions / caveats

This guide covers **Cisco IOS XE 16 / 3S** behavior. Other platforms (NX-OS, IOS-XR, Catalyst 9000 switch stacks) or other trains may differ slightly in syntax (e.g., address-family config is required in NX-OS). Always confirm against the matching configuration guide for your release.

## References

**RH ground-truth:**
- `kb:cisco-pi-basic-ip-routing` — *IP Routing: Protocol-Independent Configuration Guide*, Cisco IOS XE 3S (contains the canonical redistribution example at §"Examples: Redistribution With and Without Route Maps")
- `kb:cisco-bgp-configuring-a-basic-bgp-network` — *Configuring a Basic BGP Network*, Cisco IOS XE 16 (covers `redistribute static` into BGP, BGP aggregation)
- `kb:cisco-bgp-cisco-bgp-overview` — *Cisco BGP Overview* (BGP redistribution into other protocols)
- `note:_sources/cisco-ios-xe/protocol-independent-routing.md` — distilled redistribution/route-map mechanics (hand note)

**Wiki pages:**
- [[route-redistribution-and-route-maps]] — route-map mechanics, `no redistribute` protocol-specific traps, metric translation (cites `note:_sources/cisco-ios-xe/protocol-independent-routing.md`)
- [[bgp]] — BGP path-vector fundamentals, eBGP next-hop rule, origin attribute (cites `note:_sources/cisco-ios-xe/bgp-routing.md`)
- [[bgp-path-attributes]] — MED, AS_Path, Origin, best-path selection (cites `note:_sources/cisco-ios-xe/bgp-routing.md`)
- [[ospf]] — OSPFv2 network types, cost, LSA types (cites `note:_sources/cisco-ios-xe/ospf-routing.md`)
- [[cisco-ios-xe-overview]] — the routing architecture overview
- [[cisco-ios-xe-implementation-review]] — symptom-to-cause lookup for redistribution faults

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[cisco-pi-basic-ip-routing|Basic IP Routing]]
- [[cisco-bgp-configuring-a-basic-bgp-network|Configuring a Basic BGP Network]]
- [[cisco-bgp-cisco-bgp-overview|Cisco BGP Overview]]
<!-- crosslink:end -->
