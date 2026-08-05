---
title: Cisco IOS XE — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: cisco-ios-xe
slug: cisco-ios-xe-implementation-review
summary: "The evaluation lens and Map of Content for the cisco-ios-xe brain — a rule → anti-pattern → symptom checklist across OSPF, BGP, protocol-independent routing, and LAN switching, plus a symptom → likely-cause reverse index that turns a console/log signature into a cause page."
sources:
  - note:_sources/cisco-ios-xe/ospf-routing.md
  - note:_sources/cisco-ios-xe/bgp-routing.md
  - note:_sources/cisco-ios-xe/protocol-independent-routing.md
  - note:_sources/cisco-ios-xe/lan-switching.md
  - kb:cisco-ospf-configuring-ospf
  - kb:cisco-bgp-cisco-bgp-overview
  - kb:cisco-bgp-configuring-internal-bgp-features
  - kb:cisco-pi-basic-ip-routing
  - kb:cisco-lanswitch-spanning-tree-protocol
provenance_extracted: 11
provenance_inferred: 19
provenance_ambiguous: 0
tags: [troubleshooting, concept]
status: draft
updated: 2026-07-02
graph_community: "Cisco IOS XE — Implementation Review (Evaluation-Lens MOC)"
---

# Cisco IOS XE — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `cisco-ios-xe` domain.** It indexes the routing/switching pages into a forward checklist (rule → anti-pattern → symptom) and a reverse index (symptom → likely cause) so a console error or `show` output can be turned into a cause page. This is the IOS XE analogue of [[sso-implementation-review]] and [[active-directory-implementation-review]]; grow it as pages land via INGEST.

---

## How to use this page

Read each row left to right: the **Rule** states what a healthy config must do; the **Anti-pattern** is the common mistake; the **Symptom** is the observable fault; the **Page** links the cause page. To diagnose, jump to the [Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist

### OSPF

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Match hello/dead intervals, area type, MTU and authentication on every router of a segment | One side NSSA/stub, the other not; MD5 key-id/key mismatch; jumbo MTU on one end | Neighbors stuck INIT/EXSTART/2-WAY, never reach FULL | [[ospf]] |
| Raise `auto-cost reference-bandwidth` consistently so links ≥100 Mbps are differentiated | Default 100 Mbps reference left in place | All GigE/10GigE interfaces show OSPF cost 1; faster links not preferred | [[ospf]] |
| Anchor the router ID on a loopback for stability | Router ID taken from a physical interface | Router ID changes and all routes re-flood when the interface flaps | [[ospf]] |
| Put an ASBR in the NSSA and ensure the ABR is the Type-7→Type-5 translator | NSSA with no redistributing ASBR, or no forced translator | Redistributed externals don't enter the NSSA or don't reach the backbone | [[ospf]], [[ospf-nssa]] |
| Treat `timers throttle spf` values as milliseconds | Configured as if seconds | SPF runs far too rarely/often; sluggish or churning convergence | [[ospf]] |

### BGP

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Ensure every BGP next hop is reachable (IGP) or rewrite it; use `next-hop-self`/RR `set ip next-hop` | eBGP next hop carried unchanged into iBGP with no IGP route to it | iBGP routes not installed / next hop unreachable | [[bgp]] |
| For non-adjacent eBGP (loopbacks) configure `ebgp-multihop` + `update-source` | Plain `neighbor remote-as` between loopbacks | eBGP session never establishes | [[bgp]] |
| Decide MED policy explicitly (`missing-as-worst`, `always-compare-med`) | Relying on Cisco's missing-MED-as-0 default and same-AS-only comparison | A no-MED path wins, or a neighbor's MED appears ignored | [[bgp-path-attributes]] |
| Enable `neighbor send-community` wherever community policy is used | Community policy configured but `send-community` omitted | Downstream community-based policy never matches | [[bgp-path-attributes]] |
| On a route reflector rewrite next hop only via outbound `set ip next-hop` | Expecting other outbound route-map `set` clauses to apply on reflected routes | Outbound route-map `set` clauses silently ignored leaving the RR | [[bgp-route-reflector]] |
| Tune dampening for the environment; don't ship the defaults blindly | Default penalty 1000 / suppress 2000 / reuse 750 / 15-min half-life left on a clean network | Stable routes suppressed after **repeated** flaps (≥2 within a half-life — one flap's 1000 penalty never reaches the 2000 suppress limit; a peer reset adds no penalty) | [[bgp]], [[bgp-route-dampening]] |

### Protocol-independent routing

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Point statics at a next-hop IP (not an interface) unless you intend connected-like behavior | Static pointed at an interface on a multiaccess segment | Statics advertised into RIP/EIGRP without `redistribute static`; unexpected ARP load | [[static-and-default-routes]] |
| Inject defaults the way each protocol expects | `ip route 0.0.0.0 0.0.0.0` expecting OSPF/IS-IS to propagate it | Default route not propagated into OSPF/IS-IS | [[static-and-default-routes]] |
| Supply a metric on every redistribution and filter to prevent loops | `redistribute` with no metric / no inbound filter | Redistributed routes ignored, or a redistribution loop | [[route-redistribution-and-route-maps]] |
| Know that `no redistribute` is protocol-specific | Assuming it only subtracts a keyword | `no redistribute isis`/`eigrp` wipes the entire statement | [[route-redistribution-and-route-maps]] |
| Use `set ip next-hop verify-availability` where a PBR next hop can fail | PBR with a single unverified next hop | Device ARPs forever / blackholes policy-routed traffic when the next hop is down | [[policy-based-routing]] |

### LAN switching

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep the native VLAN identical on both ends of a trunk | Mismatched native VLAN/PVID | Two VLANs silently merge; untagged hosts land in the wrong VLAN | [[vlans-and-trunking]] |
| Set the root bridge deliberately on a backbone device with `root primary` | All switches at default priority 32768 | Lowest-MAC switch (often an access switch) becomes root | [[spanning-tree-protocol]] |
| Expect ~30 s 802.1D convergence; use edge features for host ports | Treating a 30-second post-link stall as a fault | Port "dead" for ~30 s after link-up (normal listening+learning) | [[spanning-tree-protocol]] |
| Enable EtherChannel 1:1 redundancy / fast-switchover on **both** ends | Configured on one end only, or `max-bundle` ≠ 1 | 1:1 redundant bundle won't fast-switch on link failure | [[etherchannel]] |
| Re-verify load balancing after changing the hash method | Changing flow↔vlan method on a live channel | EtherChannel stops balancing (bucket→member mappings deleted) | [[etherchannel]] |

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| OSPF neighbors stuck INIT/EXSTART/2-WAY, never FULL | hello/dead, area-type, MTU, or authentication mismatch on the segment | [[ospf]] |
| All ≥100 Mbps interfaces show OSPF cost 1 | Default `auto-cost reference-bandwidth` (100 Mbps) clips them | [[ospf]] |
| OSPF router ID changes + full re-flood after a flap | Router ID taken from a physical interface; no loopback | [[ospf]] |
| Externals missing from an NSSA / not reaching the backbone | No ASBR in the NSSA, or ABR isn't the Type-7→Type-5 translator | [[ospf]], [[ospf-nssa]] |
| Excessive MOSPF (Type-6 LSA) syslog | Neighbor sending unsupported Type-6; `ignore lsa mospf` | [[ospf]] |
| iBGP routes not installed / BGP next hop unreachable | eBGP next hop kept unchanged into iBGP; make reachable or rewrite | [[bgp]] |
| eBGP session never establishes over loopbacks | Missing `ebgp-multihop` / `update-source` (+ `disable-connected-check`) | [[bgp]] |
| A no-MED path wins, or a neighbor's MED is ignored | Cisco missing-MED-as-0 default; MED compared only within same neighbor AS | [[bgp-path-attributes]] |
| Community-based policy never matches downstream | `neighbor send-community` not configured, or a transit device dropped it | [[bgp-path-attributes]] |
| Outbound route-map `set` ignored leaving a route reflector | Only `set ip next-hop` is honored on reflected routes | [[bgp-route-reflector]] |
| Stable routes suppressed after repeated flaps | BGP dampening defaults too aggressive (penalty 1000/flap, suppress 2000 — takes ≥2 flaps; a single flap or a peer reset never suppresses) | [[bgp]], [[bgp-route-dampening]] |
| 4-byte ASN regex stops matching after asdot | Literal dot is a regex metachar; escape it and `clear ip bgp *` | [[bgp]] |
| Static ignored; dynamic path used instead | Static's AD set higher than the protocol (floating static — intended) | [[cisco-administrative-distance]], [[static-and-default-routes]] |
| `0.0.0.0/0` static not propagated into OSPF/IS-IS | OSPF/IS-IS don't redistribute a default static; use `default-information originate` | [[static-and-default-routes]] |
| Statics advertised into RIP/EIGRP without `redistribute static` | They point to an interface (treated as connected) | [[static-and-default-routes]] |
| `no redistribute …` wiped the whole statement | IS-IS / EIGRP-rel5 remove the entire command, not just a keyword | [[route-redistribution-and-route-maps]] |
| Router-sourced TCP fails under local policy while UDP/ICMP work | Local PBR TCP needs a RIB/FIB entry for the remote host | [[policy-based-routing]] |
| Device ARPs forever / blackholes policy-routed traffic | No `set ip next-hop verify-availability` on the PBR next hop | [[policy-based-routing]] |
| Two VLANs merge / untagged hosts in the wrong VLAN across a trunk | Native-VLAN (PVID) mismatch between the link ends | [[vlans-and-trunking]] |
| 802.1Q rejected on a plain Ethernet interface | dot1q supported only on Fast/Gigabit Ethernet subinterfaces | [[vlans-and-trunking]] |
| Port "dead" ~30 s after link-up | Normal 802.1D listening+learning (2× forward-delay) | [[spanning-tree-protocol]] |
| Wrong switch became root bridge | Lowest bridge ID wins; at default priority the lowest MAC wins | [[spanning-tree-protocol]] |
| Trunk port blocked/inconsistent by PVST+ | SSTP BPDU VLAN ID ≠ embedded TLV PVID | [[spanning-tree-protocol]] |
| EtherChannel stops balancing after a config change | Changing the hash method deletes bucket→member mappings | [[etherchannel]] |
| 1:1 redundant EtherChannel won't fast-switch | Feature not enabled on both ends, or `max-bundle` ≠ 1 | [[etherchannel]] |

---

## Domain map — pages by area

### Routing protocols
- [[ospf]] — link-state IGP: network types, cost, router ID, NSSA, timers, auth
- [[bgp]] — interdomain path-vector: ASNs, next hop, dampening
- [[bgp-path-attributes]] — AS_Path / Local_Pref / MED / Origin, communities, best-path
- [[bgp-route-reflector]] — iBGP scaling, Originator-ID / Cluster-list

### Protocol-independent IP routing
- [[cisco-administrative-distance]] — the AD table and floating statics
- [[static-and-default-routes]] — statics, floating statics, gateway of last resort
- [[route-redistribution-and-route-maps]] — cross-protocol redistribution + route maps
- [[policy-based-routing]] — PBR, verify-availability, SGT-based PBR

### LAN switching
- [[vlans-and-trunking]] — 802.1Q/ISL encapsulation, native VLAN/PVID
- [[spanning-tree-protocol]] — 802.1D states/timers, root election, PVST+
- [[etherchannel]] — flow-based load balancing, LACP 1:1 redundancy

## See also
- [[cisco-ios-xe-overview]] — the brain's spine
- [[sso-implementation-review]] — Keycloak/SSO equivalent of this MOC
- [[active-directory-implementation-review]] — Active Directory equivalent

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[cisco-ospf-configuring-ospf|Configuring OSPF]]
- [[cisco-bgp-cisco-bgp-overview|Cisco BGP Overview]]
- [[cisco-bgp-configuring-internal-bgp-features|Configuring Internal BGP Features]]
- [[cisco-pi-basic-ip-routing|Basic IP Routing]]
- [[cisco-lanswitch-spanning-tree-protocol|Spanning Tree Protocol]]
<!-- crosslink:end -->
