---
title: Route Redistribution & Route Maps (IOS XE)
type: entity
domain: cisco-ios-xe
slug: route-redistribution-and-route-maps
summary: "Re-advertising routes between protocols through a route map — metrics don't translate so you must supply one — and the protocol-specific 'no redistribute' behavior that removes the whole statement for IS-IS/EIGRP."
sources:
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
provenance_extracted: 6
provenance_inferred: 1
provenance_ambiguous: 0
tags: [routing-protocols, ip-routing, concept]
status: reviewed
updated: 2026-06-18
---

# Route Redistribution & Route Maps (IOS XE)

**Injecting routes learned by one routing protocol into another, optionally filtered and rewritten by a route map.**

## Route maps
A **route map** is an ordered permit/deny policy keyed by sequence number, with `match` (e.g. `match ip address {acl|prefix-list}`, `match metric`, `match route-type`) and `set` (e.g. `set metric`, `set metric-type`) clauses. A route map with **no match clause matches everything**; with no set clause it modifies nothing.

## Redistribution
Because **metrics don't translate across protocols** (RIP hop count vs EIGRP composite), you must supply one via `default-metric` or `redistribute … metric` (the redistribute metric supersedes `default-metric`). Apply redistribution consistently and filter inbound to avoid loops; redistributing between two OSPF processes does not preserve OSPF metrics.

## The `no redistribute` trap
`no redistribute` is **protocol-specific**: it is *subtractive* under BGP/OSPF/RIP (removes only the named keyword), but **`no redistribute isis`, and `no redistribute eigrp` from EIGRP rel5 onward, remove the entire command.** Likewise `no redistribute connected` is subtractive under BGP/OSPF but a full removal under IS-IS/EIGRP.

## See also
- [[cisco-administrative-distance]]
- [[static-and-default-routes]]
- [[policy-based-routing]]
- [[ospf]]
- [[bgp-path-attributes]]
- [[cisco-ios-xe-implementation-review]]
