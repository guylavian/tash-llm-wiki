---
origin: eval-cohort
title: How does OSPFv2 routing work on IOS XE?
type: question
question_tier: conceptual
domain: cisco-ios-xe
slug: ospfv2-routing-ios-xe
summary: "OSPFv2 (RFC 2328) on IOS XE is a link-state IGP that floods LSAs within areas, runs SPF to build a loop-free shortest-path tree, uses cost (derived from bandwidth) for path selection, elects DR/BDR on multiaccess networks, and requires consistent hello/dead timers, authentication, and MTU for adjacency formation."
sources:
  - kb:cisco-ospf-configuring-ospf
  - kb:cisco-ospf-ospfv2-cryptographic-authentication
  - kb:cisco-ospf-ospf-shortest-path-first-throttling
  - kb:cisco-ospf-ospf-link-state-advertisement-throttling
  - kb:cisco-ospf-ospf-support-for-fast-hello-packets
  - kb:cisco-ospf-ospf-stub-router-advertisement
  - kb:cisco-ospf-enabling-ospfv2-on-an-interface-basis
  - kb:cisco-pi-default-passive-interfaces
provenance:
  extracted: 12
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-07-12
---

# How does OSPFv2 routing work on IOS XE?

**OSPFv2 (RFC 2328) is a link-state IGP. Each router floods its local link-state information (LSAs) within an area, building an identical link-state database (LSDB) on every router in that area. Each router then runs Dijkstra's SPF independently to compute a loop-free shortest-path tree, with itself as root, and installs the resulting routes in the routing table.**

## Core operation

1. **Neighbor discovery** — OSPF routers send multicast **Hello** packets (224.0.0.5) on each enabled interface to discover and maintain adjacencies. Hello/dead intervals default to 10s/40s on broadcast and point-to-point networks, 30s/120s on NBMA. These must match on both ends (`cisco-ospf-configuring-ospf.md:458-469`). **Fast hello** (`ip ospf dead-interval minimal hello-multiplier N`) sends hellos every <1s for sub-second failure detection (`cisco-ospf-ospf-support-for-fast-hello-packets`).

2. **Adjacency formation** — On broadcast/NBMA networks, routers elect a **Designated Router (DR)** and **Backup DR (BDR)** to reduce LSAs. All routers form FULL adjacency only with the DR/BDR (state remains 2-WAY with other DROTHERs). Point-to-point and point-to-multipoint networks skip the DR/BDR election (`cisco-ospf-configuring-ospf.md:89-105`). Adjacency advances through states: DOWN → ATTEMPT/INIT → 2-WAY → EXSTART → EXCHANGE → LOADING → FULL.

3. **LSA flooding** — Each router floods **Link-State Advertisements (LSAs)** describing its connected links, neighbors, and external routes. LSAs are aged (max 3600s), refreshed every 30 minutes, and group-paced default 240s to prevent CPU spikes (`cisco-ospf-configuring-ospf.md:281-334`). IOS XE paces update packets automatically at minimum 33ms intervals (`cisco-ospf-configuring-ospf.md:361-370`).

4. **SPF calculation** — When the LSDB changes, OSPF runs **Dijkstra's SPF** to recompute the shortest-path tree. SPF throttling (`timers throttle spf`) accepts **millisecond** values for initial delay, hold time, and max wait — a common misconfig is setting these as if they were seconds (`cisco-ospf-ospf-shortest-path-first-throttling`). **Incremental SPF** (iSPF) recalculates only the affected part of the SPT, reducing CPU on large networks. **LSA throttling** (`timers lsa throttle`) controls how fast LSAs are generated during instability (`cisco-ospf-ospf-link-state-advertisement-throttling`).

## Cost (metric)

`cost = reference-bandwidth ÷ interface-bandwidth`, set per interface or derived from `auto-cost reference-bandwidth`. The **default reference is 100 Mbps**, so every link ≥100 Mbps computes to cost 1 — raise it consistently across all routers (`cisco-ospf-configuring-ospf.md:236-242`). Override per interface with `ip ospf cost`.

## Router ID

The **highest loopback IP** wins; if no loopback, the **highest active interface IP**. A loopback guarantees stability — losing the interface that owns the router ID forces a full re-flood (`cisco-ospf-configuring-ospf.md:227-235`). Set explicitly with `router-id <x.x.x.x>`.

## LSA types

| Type | Name | Origin |
|---|---|---|
| 1 | Router LSA | Each router — describes its interfaces |
| 2 | Network LSA | DR on broadcast/NBMA — describes the segment |
| 3 | Summary LSA | ABR — routes from one area to another |
| 4 | ASBR-Summary LSA | ABR — how to reach an ASBR |
| 5 | AS-External LSA | ASBR — redistributed routes (flooded everywhere) |
| 7 | NSSA LSA | NSSA ASBR — redistributed routes in a stub area (translated to Type 5 by the ABR) |

Cisco does **not** support Type 6 (MOSPF); `ignore lsa mospf` suppresses log spam (`cisco-ospf-configuring-ospf.md:350-352`).

## Area types

- **Backbone (area 0)** — all inter-area traffic transits here; all non-backbone areas must connect to it (or via a virtual link)
- **Standard area** — no restrictions; carries all LSA types
- **Stub area** — no Type 5 externals; uses a default route instead; virtual links not allowed
- **Totally stubby** (Cisco proprietary) — no Type 3/4/5 summaries + no Type 5; only a default
- **NSSA** (RFC 3101) — stub area that allows redistribution via Type 7 LSAs, translated to Type 5 by the ABR. All routers in the area must agree it is NSSA (`cisco-ospf-configuring-ospf.md:161-177`)

## Network types

| Network type | DR/BDR? | Neighbor discovery |
|---|---|---|
| Broadcast | Yes | Multicast (224.0.0.5/6) |
| Non-broadcast (NBMA) | Yes | Static `neighbor` statements |
| Point-to-point | No | Multicast |
| Point-to-multipoint | No | Multicast (broadcast variant) or static `neighbor` (non-broadcast variant) |

Override auto-classification: `ip ospf network {broadcast | non-broadcast | point-to-point | point-to-multipoint [non-broadcast]}`. On point-to-multipoint, per-neighbor cost is set via `neighbor <ip> cost <value>` (`cisco-ospf-configuring-ospf.md:107-158`).

## Authentication

- **Type 0** — none (default)
- **Type 1** — plaintext (`ip ospf authentication-key <key>`)
- **Type 2** — MD5 (`ip ospf message-digest-key <key-id> md5 <key>` + `ip ospf authentication message-digest`)

Keys and key-IDs must match on both ends (`cisco-ospf-configuring-ospf.md:64-65`). For stronger integrity: **OSPFv2 Cryptographic Authentication** (RFC 5709) adds SHA-256/SHA-512 (`cisco-ospf-ospfv2-cryptographic-authentication`).

## Key IOS XE specifics

- **Administrative distance**: OSPF defaults to 110 for intra-area, interarea, and external routes (`cisco-ospf-configuring-ospf.md:243-249`). Configurable per route type via `distance ospf`.
- **Passive interface**: `passive-interface default` + `no passive-interface <int>` is the standard pattern. A passive OSPF interface appears as a stub network in the LSDB — no hellos sent, no adjacencies formed (`cisco-pi-default-passive-interfaces.md:78-80`).
- **MTU check**: OSPF checks the DBD interface MTU field; a mismatch keeps the adjacency stuck in EXSTART. Override with `ip ospf mtu-ignore`.
- **Stub router**: `max-metric router-lsa` advertises all links with infinity cost, telling neighbors not to transit through this router — useful during boot or maintenance (`cisco-ospf-ospf-stub-router-advertisement`).
- **Graceful shutdown**: `shutdown` under `router ospf` preserves the config but tears down all adjacencies gracefully.
- **Per-interface OSPFv2**: `ip ospf <process-id> area <id>` enables OSPF on a single interface instead of using `network` statements (`cisco-ospf-enabling-ospfv2-on-an-interface-basis`).

## Basic configuration

```
router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.255.255.255 area 0
 network 192.168.1.0 0.0.0.255 area 1
 passive-interface default
 no passive-interface GigabitEthernet0/0
!
interface GigabitEthernet0/1
 ip ospf cost 100
 ip ospf hello-interval 10
 ip ospf dead-interval 40
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 mykey
```

## See also

- [[ospf]] — OSPF entity page
- [[cisco-ios-xe-overview]] — IOS XE routing & switching spine
- [[cisco-ios-xe-implementation-review]] — symptom→cause checklist (OSPF adjacency issues)
- [[cisco-administrative-distance]] — how IOS XE arbitrates between routing sources
- [[route-redistribution-and-route-maps]] — redistributing OSPF routes
- [[bgp]] — BGP, the companion interdomain protocol

## References

**RH ground-truth (notes-first domain — IOS XE reference tier)**
- `kb:cisco-ospf-configuring-ospf` — Configuring OSPF (IOS XE 16 IP Routing: OSPF Configuration Guide)
- `kb:cisco-ospf-ospfv2-cryptographic-authentication` — OSPFv2 Cryptographic Authentication
- `kb:cisco-ospf-ospf-shortest-path-first-throttling` — OSPF SPF Throttling
- `kb:cisco-ospf-ospf-link-state-advertisement-throttling` — OSPF LSA Throttling
- `kb:cisco-ospf-ospf-support-for-fast-hello-packets` — OSPF Fast Hello Packets
- `kb:cisco-ospf-ospf-stub-router-advertisement` — OSPF Stub Router Advertisement
- `kb:cisco-ospf-enabling-ospfv2-on-an-interface-basis` — Enabling OSPFv2 on an Interface Basis
- `kb:cisco-pi-default-passive-interfaces` — Default Passive Interfaces

**Wiki**
- [[ospf]] — OSPF on IOS XE (entity)
- [[cisco-ios-xe-overview]] — IOS XE routing & switching overview
- [[cisco-ios-xe-implementation-review]] — evaluation lens MOC
- [[cisco-administrative-distance]] — route preference across protocols

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[cisco-ospf-configuring-ospf|Configuring OSPF]]
- [[cisco-ospf-ospfv2-cryptographic-authentication|OSPFv2 Cryptographic Authentication]]
- [[cisco-ospf-ospf-shortest-path-first-throttling|OSPF Shortest Path First Throttling]]
- [[cisco-ospf-ospf-link-state-advertisement-throttling|OSPF Link-State Advertisement Throttling]]
- [[cisco-ospf-ospf-support-for-fast-hello-packets|OSPF Support for Fast Hello Packets]]
- [[cisco-ospf-ospf-stub-router-advertisement|OSPF Stub Router Advertisement]]
- [[cisco-ospf-enabling-ospfv2-on-an-interface-basis|Enabling OSPFv2 on an Interface Basis]]
- [[cisco-pi-default-passive-interfaces|Default Passive Interfaces]]
<!-- crosslink:end -->
