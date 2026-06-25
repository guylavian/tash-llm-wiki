---
title: Cisco IOS XE — routing & switching overview
type: topic
domain: cisco-ios-xe
slug: cisco-ios-xe-overview
summary: "The spine of the Cisco IOS XE brain: how dynamic routing (OSPF, BGP), protocol-independent forwarding (administrative distance, static/default routes, redistribution, PBR), and LAN switching (VLANs, spanning tree, EtherChannel) fit together on IOS XE routers and EtherSwitch platforms."
sources:
  - note:_sources/cisco-ios-xe/ospf-routing.md
  - note:_sources/cisco-ios-xe/bgp-routing.md
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
  - note:_sources/cisco-ios-xe/lan-switching.md
provenance_extracted: 9
provenance_inferred: 4
provenance_ambiguous: 0
tags: [routing-protocols, ip-routing, lan-switching, concept]
status: reviewed
updated: 2026-06-18
---

# Cisco IOS XE — routing & switching overview

**How IOS XE builds the forwarding table: a protocol-independent core (administrative distance, static/default routes, redistribution, policy routing) fed by dynamic routing protocols (OSPF, BGP) above, and Layer-2 LAN switching (VLANs, spanning tree, EtherChannel) below.**

## The protocol-independent core
Every routing source competes to install routes, and IOS XE arbitrates with **[[cisco-administrative-distance]]** — a 0–255 trust rating where the lowest wins (Connected 0, Static 1, eBGP 20, OSPF 110, RIP 120, iBGP 200). That single table explains most "why did it pick *that* route" questions and the **floating static** trick (give a static a higher distance than the protocol that should override it). On top of it sit **[[static-and-default-routes]]** (including the gateway of last resort, whose propagation differs sharply by protocol), **[[route-redistribution-and-route-maps]]** (metrics don't translate across protocols, so you must supply one), and **[[policy-based-routing]]** (forward by a route map on an interface instead of by destination).

## Dynamic routing
- **[[ospf]]** — a link-state IGP: areas/LSAs, DR/BDR by network type, cost from a tunable reference bandwidth, a loopback-stable router ID, NSSA Type-7↔Type-5 translation, and matched hello/dead/auth for adjacency.
- **[[bgp]]** — the interdomain path-vector protocol over TCP/179, with **[[bgp-path-attributes]]** driving best-path (AS_Path, Local_Pref, MED, Origin) and **[[bgp-route-reflector]]s** scaling iBGP without a full mesh.

These feed the protocol-independent core: a learned route only matters once its next hop is reachable and its administrative distance wins.

## LAN switching
On the Layer-2 side, **[[vlans-and-trunking]]** segments the broadcast domain (802.1Q/ISL, native VLAN/PVID), **[[spanning-tree-protocol]]** keeps it loop-free (root election by bridge ID, ~30 s 802.1D convergence, PVST+ interop), and **[[etherchannel]]** bonds links (flow-based 16-bucket load balancing, LACP 1:1 redundancy). On this router-side guide VLAN tagging is configured on **subinterfaces** with `encapsulation`, not `switchport trunk` (inferred — it is an EtherSwitch/router-oriented guide).

## Evaluation lens
For the symptom→cause lookup surface over these features (stuck OSPF adjacencies, missing-MED best-path surprises, 30-second STP stalls, EtherChannel that won't balance), see **[[cisco-ios-xe-implementation-review]]**.

## Scope / caveats
- Distilled from the IOS XE 16 / 3S **OSPF, BGP, Protocol-Independent, and LAN Switching** configuration guides; behavior can differ on other trains/platforms — confirm against the matching guide for your release.
- Wireless LAN Controller (AireOS) system-management material that arrived with these guides is a **different product** and is intentionally not part of this brain.

## See also
- [[cisco-administrative-distance]]
- [[ospf]]
- [[bgp]]
- [[vlans-and-trunking]]
- [[spanning-tree-protocol]]
- [[etherchannel]]
- [[cisco-ios-xe-implementation-review]]
