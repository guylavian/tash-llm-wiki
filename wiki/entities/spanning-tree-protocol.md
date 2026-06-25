---
title: Spanning Tree Protocol (IOS XE)
type: entity
domain: cisco-ios-xe
slug: spanning-tree-protocol
summary: "802.1D STP on IOS XE EtherSwitch: five port states with ~30 s convergence, root election by lowest bridge ID, the default timers/priority/cost, and PVST+ interop with the Common Spanning Tree."
sources:
  - note:_sources/cisco-ios-xe/lan-switching.md
provenance_extracted: 7
provenance_inferred: 1
provenance_ambiguous: 0
tags: [spanning-tree, concept]
status: reviewed
updated: 2026-06-18
---

# Spanning Tree Protocol (IOS XE)

**A Layer-2 loop-prevention protocol (IEEE 802.1D) that elects a root bridge and blocks redundant ports so the switched topology is a loop-free tree, one instance per VLAN by default.**

## Port states & convergence
Each port moves **blocking → listening → learning → forwarding** (plus disabled). **Listening and learning each last one forward-delay (default 15 s)**, so a port takes ~**30 s** to begin forwarding after a topology change; only learning and forwarding update the MAC table. This 30-second stall is the single most common "why is the port dead after link-up" symptom.

## Root election & defaults
The root is the bridge with the **lowest bridge ID (priority + MAC)**. With everything at default **priority 32768**, the lowest MAC wins. Defaults: **hello 2 s, forward-delay 15 s, max-age 20 s, port-priority 128**; short-mode port cost 10 Mbps=100, 100 Mbps=19, GigE=4. `spanning-tree vlan id root primary` sets priority 8192 (or one below the current lowest) and **auto-derives timers from the network diameter** — don't hand-tune hello/forward-delay/max-age afterward. Set the root only on a backbone/distribution device, never an access switch.

## PVST+ interop
PVST+ lets per-VLAN spanning trees interoperate with the single **Common Spanning Tree (CST = the PVST of VLAN 1 / native)** of an 802.1Q/MST region; other per-VLAN trees are tunneled. An SSTP-addressed BPDU whose VLAN ID doesn't match its embedded TLV PVID causes the port to be **blocked for inconsistency**.

## See also
- [[vlans-and-trunking]]
- [[etherchannel]]
- [[cisco-ios-xe-overview]]
- [[cisco-ios-xe-implementation-review]]
