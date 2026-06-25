---
title: Administrative Distance (IOS XE)
type: entity
domain: cisco-ios-xe
slug: cisco-administrative-distance
summary: "The 0–255 trust rating IOS XE uses to pick between routes to the same prefix learned from different sources — lowest wins, 255 means ignore — and the basis of the floating-static trick."
sources:
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
  - note:_sources/cisco-ios-xe/ospf-routing.md
provenance_extracted: 7
provenance_inferred: 1
provenance_ambiguous: 0
tags: [ip-routing, concept]
status: reviewed
updated: 2026-06-18
---

# Administrative Distance (IOS XE)

**A 0–255 rating of how trustworthy a routing source is; when several protocols offer the same prefix, the route with the lowest administrative distance is installed, and 255 means "never use".**

## The default table
| Source | AD | | Source | AD |
|---|---|---|---|---|
| Connected | 0 | | IS-IS | 115 |
| Static | 1 | | RIP | 120 |
| EIGRP summary | 5 | | EGP | 140 |
| eBGP | 20 | | ODR | 160 |
| internal EIGRP | 90 | | external EIGRP | 170 |
| IGRP | 100 | | iBGP | 200 |
| OSPF | 110 | | Unknown | 255 |

## Using it
- **Floating static:** give a static route a distance *higher* than the dynamic protocol that should normally win, so the static only takes over when the protocol's route disappears — e.g. `ip route 10.0.0.0 255.0.0.0 172.18.3.4 110`.
- **Per-source:** `distance ip-address wildcard-mask [acl]` under the routing process. Rating routes from devices running the *same* protocol is discouraged — it can create forwarding loops (inferred: the guide warns against same-protocol distance manipulation).
- OSPF keeps **three** independent distances (intra-area / inter-area / external, all default 110) — see [[ospf]].

## See also
- [[static-and-default-routes]]
- [[route-redistribution-and-route-maps]]
- [[ospf]]
- [[bgp]]
- [[cisco-ios-xe-overview]]
