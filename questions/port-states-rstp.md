---
origin: eval-cohort
title: What are the port states on RSTP?
type: question
domain: cisco-ios-xe
slug: port-states-rstp
tags: [cisco, spanning-tree]
status: draft
summary: "The vault documents IEEE 802.1D STP port states (blocking, disabled, forwarding, learning, listening) but contains no RSTP/802.1w material — RSTP port states cannot be answered from this corpus."
question_tier: conceptual
provenance_extracted: 0
provenance_inferred: 0
provenance_ambiguous: 0
updated: 2026-08-02
---

# What are the port states on RSTP?

> ⚠️ **Partial coverage.** The `cisco-ios-xe` corpus documents **classic IEEE 802.1D STP** port states only. It contains **no Rapid Spanning Tree Protocol (RSTP / 802.1w) material** — a case-insensitive search for `rstp`, `rapid spanning`, `802.1w`, and `rapid` across `reference/`, `_sources/`, `topics/`, and `entities/` returns zero RSTP hits. RSTP's own state model cannot be stated from this vault, and the classic 802.1D state set must **not** be transferred onto RSTP as if it were RSTP's.

## Port states the corpus *does* document (IEEE 802.1D STP, IOS XE EtherSwitch)

Per `cisco-lanswitch-spanning-tree-protocol.md`, each Layer 2 interface on an STP-enabled switch exists in **one of five states** (`reference/cisco-ios-xe/cisco-lanswitch-spanning-tree-protocol.md:75-81`):

- **Blocking** — does not participate in frame forwarding.
- **Disabled** — does not participate in spanning tree and is not forwarding frames.
- **Forwarding** — forwards frames.
- **Learning** — prepares to participate in frame forwarding.
- **Listening** — first transitional state after blocking, entered when STP determines the interface must participate in frame forwarding.

A port moves through the states as follows (`…:82-87`): initialization → blocking; blocking → listening **or** disabled; listening → learning **or** disabled; learning → forwarding **or** disabled; forwarding → disabled.

**Convergence timing** (`entities/spanning-tree-protocol.md:28`): each port moves **blocking → listening → learning → forwarding** (plus disabled). Listening and learning each last one forward-delay (default **15 s**), so a port takes ~ **30 s** to begin forwarding after a topology change; only learning and forwarding update the MAC table. This 30-second stall is the classic 802.1D "why is the port dead after link-up" symptom.

**Process to reach forwarding** (`…lanswitch-spanning-tree-protocol.md:93-110`): 1) port placed in the listening state while it waits for protocol information; 2) after the forward-delay timer expires it moves to learning and resets the timer; 3) in learning it still blocks frame forwarding while learning end-station locations into the forwarding database; 4) after the second forward-delay expiry it moves to forwarding, where both learning and frame forwarding are enabled.

Per-state behavior (`…118-174`): **blocking** and **listening** discard frames, do no MAC learning, receive and direct BPDUs; **learning** adds end-station addresses to the FDB but still discards frames; **forwarding** forwards frames, learns FDB, processes BPDUs; **disabled** is virtually nonoperational (discards frames, no FDB learning, does not receive BPDUs).

## RSTP difference
The vault does not cover RSTP (802.1w), which collapses the port state/role model (e.g. discarding / learning / forwarding states and root/designated/alternate/backup roles) differently from classic 802.1D. There is **no in-vault support** for stating RSTP port states; ingest a Cisco NX-OS or IOS XE *Rapid PVST+ / spanning-tree mode rapid-pvst* source before asserting RSTP specifics. Closest in-vault neighbors: `[[spanning-tree-protocol]]`, `[[vlans-and-trunking]]` (PVST+ interop is documented as per-VLAN trees interoperating with a Common Spanning Tree).

## References

### RH ground-truth
- `ref:cisco-lanswitch-spanning-tree-protocol` — Cisco IOS XE 16 — LAN Switching Configuration Guide (IEEE 802.1D port states, transitions, per-state behavior; no RSTP)
- `ref:cisco-ios-xe` — aggregate IOS XE corpus marker (no RSTP content)

### Wiki/`web:`
- [[spanning-tree-protocol]], [[vlans-and-trunking]], [[cisco-ios-xe-overview]]
- web:https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/srstp.html (Cisco RSTP — external, not cached in vault)