---
title: Port-channel with mixed 1G + 10G links — out-of-order packets and poor throughput
type: question
question_tier: support-kb
domain: cisco-ios-xe
slug: mixed-speed-port-channel
summary: "Mixing a 1G and a 10G link in the same LACP port-channel causes out-of-order packets and throughput degradation because (a) Cisco does not support mixed-speed EtherChannel members, and (b) flow-based load balancing distributes packets across links with ~10× serialization-delay difference, causing reordering at the receiver."
sources:
  - note:_sources/cisco-ios-xe/lan-switching.md
  - kb:cisco-lanswitch-etherchannel-flow-based-limited-1-1-redundancy
  - kb:cisco-lanswitch-flow-based-per-port-channel-load-balancing
provenance_extracted: 1
provenance_inferred: 5
provenance_ambiguous: 0
symptoms:
  - "Out-of-order packets / poor throughput on a port-channel"
  - "member port suspended or not-in-bundle"
  - "%EC_ERR_CFG"
status: draft
updated: 2026-07-02
---

# Why a mixed 1G + 10G LACP port-channel causes out-of-order packets and terrible throughput

⚠️ **Out of corpus coverage — `cisco-ios-xe` holds `conceptual` only; this is a `support-kb`/break-fix question and that tier is not ingested. The answer below rests on general networking principles and Cisco platform requirements that are not fully captured in the wiki's source notes. Verify against the primary Cisco documentation.**

## Short answer

**Cisco IOS XE does not support mixing link speeds in a single EtherChannel.** All members of a port-channel must have identical speed and duplex. Even if LACP negotiates and the port-channel comes up (behaviour varies by platform — some IOS versions allow it, some reject the mismatched member), the result is the exact symptoms you describe: terrible throughput and out-of-order packets.

Three mechanisms combine to produce the failure:

### 1. Speed mismatch violates the EtherChannel member-consistency rules
Cisco's EtherChannel requires all member links to be **same speed, same duplex, same VLAN membership, same trunk mode, and same allowed VLAN list**. This is a hardware forwarding requirement: the port-channel presents a single logical interface to the forwarding ASIC, and the ASIC expects every member to have identical egress characteristics. A 1G link and a 10G link have fundamentally different timing — the MAC layer, the FIFO depths, and the egress scheduler treat them differently. Most Cisco platforms enforce this at member-addition time (`%EC_ERR_CFG` or the member stays suspended/not-bundled), but some older or permissive trains allow the bundle to form — at which point the hardware cannot compensate for the asymmetry.

### 2. Flow-based load balancing sends packets across both links unequally
[[etherchannel]] explains how IOS XE hashes packet headers into **16 buckets** per port-channel, each bound to one active member link. With two active members (the 1G and the 10G), roughly half the hashed flows land on each link — but:

- **Serialization delay is ~10× higher on the 1G link.** A 1500-byte frame takes 12 μs to serialize at 1 Gbps but only 1.2 μs at 10 Gbps. Packets from the **same TCP flow** that hash onto the 1G link arrive at the receiver delayed relative to packets that hash onto the 10G link.
- **If the two links do not follow identical physical paths** (different linecards, different fabric paths, different cable lengths), propagation delay asymmetry adds further jitter.
- The receiver's TCP stack sees **out-of-order delivery**: packets arrive interleaved from the two paths with the slower link's packets lagging. TCP treats out-of-order delivery as packet loss (duplicate ACKs trigger fast retransmit), halving the congestion window repeatedly. The result is throughput that can be **worse than a single 1G link** alone.

### 3. LACP does not enforce speed matching at the control plane
LACP (IEEE 802.3ad / 802.1AX) exchanges LACPDUs carrying the actor/partner **system ID and priority, port key and port priority, and state flags** — there is **no explicit port-speed TLV** in an LACPDU (inferred — LACP frame contents are not described in the ingested IOS XE notes). Speed instead influences bundling indirectly: interfaces of different speeds derive a **different operational port key**, and platform member-consistency checks reject a member whose speed/duplex differs. Where a permissive platform still lets the aggregator form, the control plane has negotiated nothing about speed, and the forwarding plane cannot deliver in-order delivery — the IEEE standard is silent on speed enforcement, so Cisco (and most vendors) implement it as a software member-consistency check rather than in the LACPDU exchange.

## The fix

You have two options:

1. **Match the speeds** — replace the 1G link with a second 10G link (or the 10G with a second 1G if 10G isn't available), so both members are identical. This is the correct architecture.
2. **Separate port-channels** — put the 1G uplink in its own port-channel or leave it as a standalone routed link (if the topology supports it). Never bundle unequal-speed links.

## Verification commands

```cisco
show etherchannel summary
show etherchannel port-channel
show interfaces status           # check speed/duplex per member
show lacp neighbor               # LACP state per member
```

Look for a member port that is `suspended` or `not-in-bundle` — that is Cisco rejecting the mismatch. If all members are `in-bundle` but speeds differ, you are on a permissive train that allows the misconfiguration — fix it anyway.

## References

### RH ground-truth (note:)
- `note:_sources/cisco-ios-xe/lan-switching.md` — EtherChannel flow-based load balancing (16-bucket hash, 5-tuple, bucket-remap gotchas), LACP 1:1 redundancy requirements.

### Wiki
- [[etherchannel]] — flow-based load balancing mechanics and LACP redundancy constraints.
- [[cisco-ios-xe-overview]] — how EtherChannel fits into the IOS XE LAN switching model.
- [[cisco-ios-xe-implementation-review]] — EtherChannel health checklist (not yet covering mixed-speed bundles).

<!-- The mixed-speed EtherChannel failure mode is not covered in the wiki's cisco-ios-xe raw sources;
     this answer is synthesized from general networking knowledge. Per the confidence gate (H1),
     this is break-fix content outside the domain's ingested `conceptual` tier. -->

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[cisco-lanswitch-etherchannel-flow-based-limited-1-1-redundancy|EtherChannel Flow-Based Limited 1 1 Redundancy]]
- [[cisco-lanswitch-flow-based-per-port-channel-load-balancing|Flow-Based per Port-Channel Load Balancing]]
<!-- crosslink:end -->
