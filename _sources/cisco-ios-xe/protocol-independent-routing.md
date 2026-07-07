# Protocol-independent IP routing — raw notes

**Source:** Cisco *IP Routing: Protocol-Independent Configuration Guide*, Cisco IOS XE 3S
(`iri-xe-3s-book`). Distilled/paraphrased. These are the protocol-agnostic mechanics under
any routing protocol.

## Administrative distance (the canonical table)
- 0–255 trust rating; lowest wins; 255 = ignore. Defaults: **Connected 0, Static 1, EIGRP summary 5, eBGP 20, internal EIGRP 90, IGRP 100, OSPF 110, IS-IS 115, RIP 120, EGP 140, ODR 160, external EIGRP 170, iBGP 200, Unknown 255.**
- Make a dynamic protocol override a static by giving the static a **higher** distance (floating static, e.g. `ip route … 110`). Per-source distance via `distance ip-address wildcard [acl]`; rating same-protocol peers can cause loops.

## Static & floating static routes
- `ip route prefix mask {next-hop-ip | interface [next-hop]} [distance] [name] [permanent | track n] [tag]`. **Default AD = 1.** Up to 6 parallel static paths.
- **Static routes pointing to an INTERFACE** (not a next-hop IP) are treated as connected and are **advertised by RIP/EIGRP even without `redistribute static`** — losing their static nature. Next-hop-IP statics in a `network`-covered range aren't advertised unless redistributed.
- A static is pulled when its outbound interface goes down or its next hop can't be resolved.

## Default routes / gateway of last resort
- `ip default-gateway` (only when IP routing is **disabled**), `ip default-network` (when routing enabled; flags a known net as default candidate), or static default `ip route 0.0.0.0 0.0.0.0 next-hop`.
- **Propagation differs by protocol:** IGRP doesn't recognize a 0.0.0.0/0 static (use `ip default-network`); EIGRP propagates 0.0.0.0 only if the static is redistributed; **OSPF/IS-IS don't advertise or redistribute a 0.0.0.0/0 static — use `default-information originate`.**

## Redistribution & route maps
- Re-advertise one protocol's routes into another, filtered/modified by a **route map** (permit/deny by sequence, with `match`/`set`). **Metrics don't translate across protocols** → supply one via `default-metric` or `redistribute … metric` (the redistribute metric supersedes default-metric).
- `route-map tag [permit|deny] [seq]`; `match ip address {acl|prefix-list}`, `match metric`, `match route-type`; `set metric`, `set metric-type`. A no-match route map matches everything.
- **`no redistribute` is protocol-specific:** subtractive under BGP/OSPF/RIP, but `no redistribute isis` (and `no redistribute eigrp` from EIGRP rel5) removes the **entire** command. Redistributing between two OSPF processes does not preserve OSPF metrics.

## Policy-Based Routing (PBR)
- Forward by a route map on an interface instead of destination longest-prefix: `ip policy route-map tag` (transit) / `ip local policy route-map tag` (router-originated). Match by `match ip address` ACL/prefix or `match length`; act via `set ip next-hop`, `set interface`, `set ip precedence`.
- **Enabling `ip policy` disables fast switching on that interface.** Local PBR: router-sourced **TCP** needs a RIB/FIB entry for the remote host or it fails (UDP/ICMP still follow policy).
- **`set ip next-hop verify-availability`** checks the next hop is a CDP neighbor before policy-routing (prevents blackhole/ARP loop); requires CDP, a directly-connected Cisco next hop, and doesn't work with distributed CEF.

## Recursive static route
- `ip route static install-routes-recurse-via-nexthop [vrf name] [route-map map]` installs a static even when its next hop is reachable only via another learned route. **Only one route map per VRF/topology** (a second overwrites the first); without `vrf` it applies to the global topology.

## SGT-based PBR
- PBR keyed by Cisco TrustSec **Security Group Tag** instead of IP/ACL (`match security-group source|destination tag`). Number-based tags only; not for IPv6 on IOS XE. A dynamic (SGT) route-map overrides a static route-map on the same interface (with a warning) — disassociate a route-map from the interface before deleting it.

## Troubleshooting (symptom → cause)
- Static ignored, dynamic path used → static AD set higher than the protocol (floating static; intended).
- Static disappears after a link event → outbound interface down, or next hop unresolved.
- Statics advertised into RIP/EIGRP without `redistribute static` → they point to an interface (treated as connected).
- `0.0.0.0/0` static not propagated into OSPF/IS-IS → use `default-information originate`.
- IGRP/EIGRP don't propagate the default network → the named network isn't a known route / not redistributed (IGRP ignores 0.0.0.0 statics).
- `no redistribute …` wipes the whole statement → IS-IS / EIGRP-rel5 remove the entire command, not just a keyword.
- Router-sourced TCP fails under local policy while UDP/ICMP work → local PBR TCP needs a RIB/FIB entry for the remote host.
- Device ARPs forever / blackholes policy-routed traffic → no `set ip next-hop verify-availability`.
- Only one set of recursive statics applies → one route map per VRF; the second overwrote the first.
