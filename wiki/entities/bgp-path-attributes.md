---
title: BGP Path Attributes & Best-Path
type: entity
domain: cisco-ios-xe
slug: bgp-path-attributes
summary: "How BGP picks the best path — AS_Path, Local_Pref, MED, Next_Hop, Origin — and the two Cisco defaults that surprise people: missing-MED-as-0 and MED compared only within the same neighbor AS."
sources:
  - note:_sources/cisco-ios-xe/bgp-routing.md
provenance:
  extracted: 7
  inferred: 1
  ambiguous: 0
tags: [routing-protocols, concept]
status: reviewed
updated: 2026-06-18
---

# BGP Path Attributes & Best-Path

**The per-route attributes BGP weighs to choose one best path, and the knobs (route maps, well-known communities) used to steer that choice.**

## The attributes
- **AS_Path** — list of traversed ASes; **shorter preferred**. Lengthen with prepending to make a path less attractive to upstreams.
- **Local_Pref** — **highest preferred**; advertised only to iBGP peers and **never leaves the AS**, so it cannot influence an upstream AS.
- **MED (Multi_Exit_Discriminator)** — **lower preferred**; hints a neighbor AS which entry point to use. Reset to 0 when forwarded into an AS.
- **Next_Hop** — see [[bgp]] (iBGP keeps the eBGP next hop unchanged).
- **Origin** — IGP > EGP > Incomplete.

## The two Cisco surprises
- **Missing MED = 0 (most preferred)** on Cisco — the *inverse* of the IETF rule. Configure `bgp bestpath med missing-as-worst` to make a path with no MED least preferred.
- **MED is compared only between paths from the same neighbor AS** unless you set `bgp always-compare-med`.

## Communities
A **community** tags routes that share a policy, but it is **not sent unless `neighbor send-community`** is configured. Well-known values: `no-export` (don't advertise to eBGP), `no-advertise` (don't advertise to anyone), `local-as` (don't leave the AS/confederation). Extended communities **Route Target** and **Site of Origin** drive MPLS-VPN import and origin-loop prevention.

## See also
- [[bgp]]
- [[bgp-route-reflector]]
- [[route-redistribution-and-route-maps]]
- [[cisco-ios-xe-implementation-review]]
