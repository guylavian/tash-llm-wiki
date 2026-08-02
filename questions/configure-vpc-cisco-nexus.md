---
origin: eval-cohort
title: How do you configure vPC (Virtual Port Channel) on Cisco Nexus?
type: question
domain: cisco-ios-xe
slug: configure-vpc-cisco-nexus
tags: [cisco]
status: draft
summary: "Out of corpus coverage — the vault holds no Cisco Nexus or virtual Port-Channel (vPC) material; only AWS VPC peering (OpenShift/ROSA) and IOS XE EtherChannel/VLAN/STP content."
question_tier: conceptual
provenance_extracted: 0
provenance_inferred: 0
provenance_ambiguous: 0
updated: 2026-08-02
---

# How do you configure vPC (Virtual Port Channel) on Cisco Nexus?

> ⚠️ **Out of corpus coverage.** The `cisco-ios-xe` domain holds IOS XE routing/switch material (BGP, OSPF, protocol-independent routing, LAN switching: VLAN, STP, EtherChannel) — it contains **no Nexus** and **no virtual Port-Channel (vPC)** page. A character-for-character and semantic search of `reference/`, `_sources/`, `topics/`, and `entities/` returned zero Nexus/vPC hits. The only "vpc" strings in the vault are **AWS VPC** peering pages in the OpenShift/ROSA domain (e.g. `rosa-cluster-admin-4-22-dedicated-aws-peering.md`) — a different concept (cloud VPC), not Cisco Nexus vPC.

**Cisco Nexus vPC** is a proprietary Multi-Chassis LAG technology (the same links appear as one logical Port-Channel to downstream peers by establishing a vPC domain, vPC peer link, and peer-keepalive to synchronize between the two Nexus switches). Because the configured corpus does not cover the Nexus platform or this feature, no defaults, command syntax, or step-by-step procedure can be stated here without fabricating them.

## What the vault *does* cover (closest neighbors — Layer-2 bonding on a router/EtherSwitch)

- **EtherChannel / Port-Channel** — flow-based balancing (16 buckets), LACP, and 1:1 redundancy / fast-switchover: [[etherchannel]], [[etherchannel-load-balancing]], [[lacp-fast-switchover-prereqs]], [[mixed-speed-port-channel]]
- **VLANs & trunking** — 802.1Q / ISL, native VLAN/PVID, subinterface `encapsulation` (no `switchport trunk` on this router-oriented guide): [[vlans-and-trunking]], [[vlan-trunking-ios-xe]]
- **Spanning Tree Protocol** — root election, convergence, prevention of Layer-2 loops: [[spanning-tree-protocol]]
- Ground truth file: `ref:cisco-lanswitch-*` (e.g. `cisco-lanswitch-etherchannel-flow-based-limited-1-1-redundancy.md`, `cisco-lanswitch-flow-based-per-port-channel-load-balancing.md`, `cisco-lanswitch-spanning-tree-protocol.md`)

None of these == Nexus vPC. To answer the actual vPC config question inside the wiki, ingest a Nexus (NX-OS) raw source (e.g. Cisco "Nexus 9000 Series NX-OS Interfaces Configuration Guide — Configuring vPC") into the vault first; the synthesis layer will not invent vPC commands.

## References

### RH ground-truth
- `ref:cisco-lanswitch-etherchannel-flow-based-limited-1-1-redundancy` — Cisco IOS XE 16 — LAN Switching Configuration Guide (EtherChannel 1:1 redundancy / fast switchover)
- `ref:cisco-lanswitch-flow-based-per-port-channel-load-balancing` — Cisco IOS XE 16 — LAN Switching Configuration Guide (flow-based Port-Channel load balancing)
- `ref:cisco-lanswitch-spanning-tree-protocol` — Cisco IOS XE 16 — LAN Switching Configuration Guide (STP loop prevention)
- `ref:cisco-ios-xe` — aggregate IOS XE corpus marker (no Nexus device)

### Wiki/`web:`
- [[cisco-ios-xe-overview]], [[cisco-ios-xe-implementation-review]], [[etherchannel]], [[vlans-and-trunking]], [[spanning-tree-protocol]]
- web:https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/9-x/interfaces/configuration/guide/b_Cisco_Nexus_9000_NX-OS_Interfaces_Configuration_Guide_9x/b_Cisco_Nexus_9000_NX-OS_Interfaces_Configuration_Guide_9x_chapter_01100.html (Cisco NX-OS vPC config — external, not cached in vault)