---
title: VLAN trunking mechanics on IOS XE routers
type: question
question_tier: conceptual
domain: cisco-ios-xe
slug: vlan-trunking-ios-xe
summary: How 802.1Q and ISL frame tagging work on IOS XE router subinterfaces for inter-VLAN routing, and the native-VLAN/PVID mismatch pitfall.
sources:
  - ref:reference/cisco-ios-xe/cisco-lanswitch-configuring-routing-between-vlans.md
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
provenance:
  extracted: 7
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-07-07
graph_community: "Cisco IOS XE — Implementation Review (Evaluation-Lens MOC)"
---

# VLAN trunking mechanics on IOS XE routers

**How 802.1Q and ISL frame tagging work on IOS XE router subinterfaces for inter-VLAN routing, and the native-VLAN/PVID mismatch pitfall.**

## 802.1Q encapsulation
The IEEE 802.1Q tag is 4 bytes inserted after the source MAC address: TPID (`0x8100`) + 3-bit 802.1p priority + CFI + 12-bit VLAN ID (VID, 1–4095). The tag causes the Frame Check Sequence to be recomputed. Supported on Fast Ethernet and Gigabit Ethernet interfaces; **not** supported on plain Ethernet interfaces (inferred — Cisco docs explicitly exclude Ethernet).

The `encapsulation dot1q vlan-id` command on a subinterface binds that subinterface to the given VLAN. Only one VLAN per subinterface; the physical interface carries all subinterfaces.

## ISL encapsulation (Cisco proprietary)
ISL prepends a 26-byte header containing a 10-bit VLAN ID (max 1000 VLANs) and reappends a new FCS, **encapsulating** the entire original frame. Supported only on Fast Ethernet. TRISL (Token Ring ISL) also exists for Token Ring VLANs. ISL and 802.1Q cannot be mixed on the same trunk link.

## Native VLAN / PVID
Every 802.1Q port has a **Port VLAN ID (PVID)** equal to its native VLAN — default VLAN 1. Untagged frames arriving on the port are assigned to the PVID. Frames egressing on the native VLAN are sent **untagged**. This allows VLAN-unaware devices to coexist on the same link. A **native-VLAN mismatch** between the two ends silently merges traffic across VLANs (a classic hard-to-diagnose fault).

## Router vs switch syntax
Critical distinction: on IOS XE **routers** (and EtherSwitch modules in router mode), VLAN trunking is configured on subinterfaces with `encapsulation dot1q vlan-id`. On **switches**, the equivalent is `switchport trunk allowed vlan ...` and `switchport mode trunk`. The wiki's [[vlans-and-trunking]] covers the router-side syntax.

## See also
- [[vlans-and-trunking]]
- [[cisco-ios-xe-overview]]
- [[spanning-tree-protocol]]
- [[etherchannel]]
