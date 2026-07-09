---
title: Catalyst 9500 StackWise Virtual ISSU — traffic blackhole and OSPF/BGP flap
type: question
question_tier: scenarios
domain: cisco-ios-xe
slug: c9500-issu-svl-blackhole-nsf-gr
summary: "On a Catalyst 9500 StackWise Virtual pair, ISSU caused ~90-second traffic blackhole and OSPF/BGP flapping despite the standby reloading and rejoining cleanly. The root cause is missing OSPF NSF and BGP Graceful Restart configuration, not an ISSU procedure error — the routing protocols tore down adjacencies during the control-plane switchover because no grace signal was sent."
sources:
  - note:_sources/cisco-ios-xe/ospf-routing.md
  - note:_sources/cisco-ios-xe/bgp-routing.md
  - kb:cisco-bgp-configuring-a-basic-bgp-network
  - kb:cisco-ospf-ospf-nonstop-routing
  - kb:cisco-bgp-bgp-nsf-awareness
  - kb:cisco-bgp-bgp-graceful-restart-per-neighbor
provenance_extracted: 4
provenance_inferred: 8
provenance_ambiguous: 0
symptoms:
  - "~90 s traffic blackhole during ISSU / SSO switchover"
  - "OSPF/BGP adjacencies flap during a StackWise Virtual switchover"
  - "routes withdrawn despite standby reloading and rejoining cleanly"
status: draft
updated: 2026-07-02
---

# Catalyst 9500 StackWise Virtual ISSU — why it blackholed traffic despite the standby joining cleanly

> ⚠️ **Out of corpus coverage** — the `cisco-ios-xe` domain holds `conceptual` config-guide
> material only; this is a **scenarios / break-fix** question and that tier is **not ingested**.
> The OSPF/BGP protocol mechanics below are grounded in the cited notes, but the ISSU / StackWise
> Virtual / NSF / SSO / Graceful Restart diagnosis and fix are **synthesis, not a confirmed
> root cause** — verify against the Cisco Catalyst 9500 Software Upgrade and Downgrade Guide
> for your IOS-XE release.

**You had an ISSU procedure issue *and* a configuration gap — but the *primary cause of the ~90 s blackhole* is that OSPF NSF and BGP Graceful Restart were not configured. The ISSU reload+switchover worked mechanically (the standby reloaded and rejoined), but without NSF/GR the routing protocols tore down adjacencies during the control-plane switchover, withdrawing all routes and blackholing traffic until reconvergence completed.**

## What happened

A Catalyst 9500 StackWise Virtual pair runs as a single logical chassis with two member switches (active and standby) connected via the SVL (StackWise Virtual Link). ISSU on this platform follows a specific workflow:

1. **`install add`** stages the new image on both members.
2. **`install activate`** triggers ISSU: the standby reloads with the new image and rejoins the stack.
3. A **controlled switchover** occurs — the standby becomes active, and the original active reloads with the new image to become the new standby.
4. **`install commit`** makes the upgrade permanent.

Your pair got through steps 1–2 cleanly (standby reloaded and rejoined). But during step 3 (the switchover), the `~90 s blackhole` and `OSPF/BGP flap` happened.

### The root mechanism

When the chassis roles swap (step 3), every routing-protocol process on the device restarts:

- **OSPF** — the new active's OSPF process comes up and sends Hellos with an empty neighbor list. Without OSPF NSF configured, neighbors see their own Router ID missing from the Hello's neighbor list and immediately declare the adjacency DOWN (they don't wait for the dead interval — this is a non-NSF restart detection behavior). All routes learned from this router are flushed. (Inferred — see [[ospf]] for OSPF adjacency mechanics.)

- **BGP** — the TCP session (port 179) drops when the control plane restarts. Without BGP Graceful Restart, the neighbor immediately withdraws all routes received from this peer. Note the IOS-XE defaults are a 60 s keepalive and a 180 s hold timer (kb:cisco-bgp-configuring-a-basic-bgp-network) — so a ~90 s outage is *shorter* than hold-timer expiry: it is consistent with the neighbor detecting the TCP session drop at switchover (immediate withdrawal) followed by tens of seconds of session re-establishment and full table exchange, not with waiting out the hold time. (Inferred — see [[bgp]] for BGP session mechanics.)

- **Traffic blackhole** — once the routing table entries pointing to this device are withdrawn by neighbors, traffic transiting the pair has no valid forwarding entry. Forwarding resumes only after OSPF adjacencies reach FULL and BGP sessions re-exchange the full table — a process that takes tens of seconds on a non-trivial network.

## The fix: configure NSF and Graceful Restart, then verify before ISSU

### 1. OSPF NSF

Enable NSF support under each OSPF process. Cisco NSF (the default mode) uses LLS (Link-Local Signaling) to advertise the restart to neighbors. IETF NSF (`nsf ietf`) uses the Grace LSA mechanism instead — prefer IETF for multi-vendor interop, but either is far better than no NSF:

```
router ospf 1
 nsf                          ! Cisco NSF (LLS-based — Cisco proprietary)
 ! or
 nsf ietf                     ! IETF RFC 3623 Grace-LSA mechanism — multi-vendor
```

What this does: when OSPF restarts during switchover, the restarting router sends Hellos with the "R-bit" set in the LLS block (Cisco NSF) or originates a Grace LSA (IETF NSF). Neighbors that support NSF continue forwarding traffic using the stale routes during a configurable grace period (default 60–120 s depending on the implementation). After the restart, the router performs an NSF-restart sync (no full re-flood needed).

### 2. BGP Graceful Restart

```
router bgp <ASN>
 bgp graceful-restart
 bgp graceful-restart restart-time 120        ! how long neighbor waits to re-establish
 bgp graceful-restart stalepath-time 360      ! how long stale routes are kept
```

What this does: the BGP OPEN message now includes the Graceful Restart capability. When the TCP session drops, neighbors keep forwarding using stale routes during the restart time window and only flush them if the session doesn't come back up in time.

### 3. SSO verification (pre-ISSU)

StackWise Virtual requires SSO (Stateful Switchover) to be operational for hitless switchover. Verify before running ISSU:

```
show redundancy states
```

Look for `Mode = SSO` and `Current active = <member-id>`. If the mode is not SSO, ISSU cannot be hitless — resolve the redundancy state first.

### 4. OSPF/BGP NSF verification (pre-ISSU)

```
show ip ospf
show ip ospf nsf
show bgp <ASN>
```

The OSPF output should say something like `NSF support enabled` or `IETF NSF support enabled`. BGP should show Graceful Restart information under `show bgp <ASN>` output, and the BGP capabilities exchanged with each neighbor should include `Graceful Restart`.

## Why it wasn't just a procedure issue

The standby reloaded and rejoined cleanly — the ISSU mechanics worked. A pure ISSU-procedure failure would show a different symptom (one member stuck in `install` state, an `install` activation failure, or a member that never rejoins). The 90-second blackhole plus OSPF/BGP flap is the textbook signature of *routing-protocol restart without grace signaling* during an otherwise-successful switchover.

**However**, if you ran `install activate` on the *active* directly (instead of using the proper SVL ISSU workflow), the device may have reloaded both members more aggressively. Check your exact procedure against the documentation for `install activate` on StackWise Virtual — the proper method is to stage via `install add` on the active and then `install activate` triggers the sequential reload. On some IOS-XE versions, the SVL ISSU procedure first preps the standby, then performs the controlled switchover — but if the `install activate` was run with `-c` (copy config) and the packages.conf was not consistent, or if the ISSU was attempted on a non-ISSU-supporting train, the behavior may have been a disruptive reload rather than an ISSU.

## What to verify next time

Pre-ISSU checklist:

| Check | Command | Must show |
|-------|---------|-----------|
| Redundancy mode | `show redundancy states` | `Mode = SSO` |
| Stack status | `show switch` | Both members present, standby hot |
| ISSU readiness | `show issu state detail` (inferred — not in ingested sources) | ISSU-compatible state |
| OSPF NSF | `show ip ospf` | `NSF support enabled` or equivalent |
| BGP GR | `show bgp <ASN> neighbors` | Graceful Restart capability in the exchanged capabilities |
| Install state | `show install summary` | Clean state (no stuck activation) |

## Contradictions / caveats

- This wiki's `cisco-ios-xe` domain covers OSPF and BGP protocol mechanics but has not yet been extended to cover ISSU, StackWise Virtual, NSF/SSO, or Graceful Restart. The behavioral analysis above is based on IOS-XE design documentation and is directionally correct, but the exact NLR and feature-name surface can vary between IOS-XE releases (16.x vs 17.x). Always consult the **Cisco Catalyst 9500 Software Upgrade and Downgrade Guide** for your specific release.
- Some early Catalyst 9500 IOS-XE releases (particularly early 16.x trains) had platform ISSU limitations that may not be present on 17.x. Verify ISSU support with `show issu state detail` before the upgrade (inferred — ISSU commands are not in this wiki's ingested sources; confirm against the upgrade guide).
- If you are running a `Cisco Catalyst 9500-32C` or the earlier 9500 series hardware, there are specific ISSU caveats around stack (StackWise-480 vs StackWise Virtual) — StackWise Virtual requires a Network Advantage license, not a separate add-on SKU (inferred), and ISSU behavior on specific hardware SKUs varies.

## See also

- [[ospf]] — OSPF on IOS XE: adjacencies, timers, cost (NSF/GR not yet covered there)
- [[bgp]] — BGP on IOS XE: session establishment, next-hop, ASNs (Graceful Restart not yet covered there)
- [[cisco-ios-xe-overview]] — the IOS XE routing/switching spine page
- [[cisco-ios-xe-implementation-review]] — the symptom→cause MOC (no ISSU/stack-virtual entries yet)

## References

### RH ground-truth (`kb:` / `guide:` / `ref:` / `note:`)

| ID | Title |
|----|-------|
| `note:_sources/cisco-ios-xe/ospf-routing.md` | IP Routing: OSPF Configuration Guide (IOS XE 16) — OSPF adjacency mechanics used to infer restart-detection behavior |
| `note:_sources/cisco-ios-xe/bgp-routing.md` | IP Routing: BGP Configuration Guide (IOS XE 16) — BGP session mechanics used to infer withdrawal behavior |
| `kb:cisco-bgp-configuring-a-basic-bgp-network` | Configuring a Basic BGP Network — default BGP timers (60 s keepalive / 180 s hold) |

### Wiki

| Page | Type | Summary |
|------|------|---------|
| [[ospf]] | entity | OSPFv2 adjacencies, timers, cost — adjacency-restart mechanism used in the analysis |
| [[bgp]] | entity | BGP session mechanics, hold timer — session-drop analysis |
| [[cisco-ios-xe-overview]] | topic | The spine of the cisco-ios-xe brain |
| [[cisco-ios-xe-implementation-review]] | topic | Symptom→cause MOC for IOS XE routing/switching issues |

**Caveat:** The `cisco-ios-xe` domain does not yet have synthesis pages covering ISSU, StackWise Virtual, NSF/SSO, or Graceful Restart. The protocol-level analysis is grounded in the existing OSPF/BGP pages and the underlying source notes; the ISSU/NSF/GR procedural guidance draws on IOS-XE platform documentation that has not yet been ingested into this wiki. Verify all ISSU-specific commands against the **Cisco Catalyst 9500 Software Upgrade and Downgrade Guide** for your IOS-XE release.

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[cisco-bgp-configuring-a-basic-bgp-network|Configuring a Basic BGP Network]]
- [[cisco-ospf-ospf-nonstop-routing|OSPF Nonstop Routing]]
- [[cisco-bgp-bgp-nsf-awareness|BGP NSF Awareness]]
- [[cisco-bgp-bgp-graceful-restart-per-neighbor|BGP Graceful Restart per Neighbor]]
<!-- crosslink:end -->
