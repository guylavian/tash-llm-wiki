# BGP — raw notes

**Source:** Cisco *IP Routing: BGP Configuration Guide*, Cisco IOS XE 16 (`irg-xe-16-book`).
Distilled/paraphrased. BGP-4 is the interdomain path-vector protocol over TCP/179.

## Path-vector fundamentals
- Exchanges loop-free reachability between autonomous systems; each route carries the ordered **AS_Path**, and a router rejects any update whose AS_Path already contains its own AS (loop prevention). Runs over **TCP port 179**; installs **one best path** per prefix by default. A device runs one BGP process / one AS but many address families. A BGP next hop must be reachable (usually via the IGP) for the route to be usable.

## AS numbers
- 2-byte ASNs 1–65535; 4-byte 65536–4294967295 (RFC 4893 transition). Notations **asplain** (default, e.g. 234567) vs **asdot** (1.169031) via `bgp asnotation dot`. Private 2-byte 64512–65534. Reserved private 23456 can't be configured. Under asdot, 4-byte regexes must escape the dot (`1\.14`) and switching notation needs `clear ip bgp *`. Cisco does **not** strip private ASNs by default (`neighbor remove-private-as`).

## Path attributes & best-path
- **AS_Path** (shorter preferred), **Local_Pref** (highest preferred; iBGP-only, never sent to eBGP, never leaves the AS), **MED** (lower preferred; hints a neighbor AS which entry to use), **Next_Hop**, **Origin** (IGP > EGP > Incomplete).
- **MED is compared only between paths from the same neighbor AS** unless `bgp always-compare-med`. **Cisco treats a missing MED as 0 (most preferred)** — the inverse of IETF; `bgp bestpath med missing-as-worst` to conform.
- Influence with route maps: `set local-preference`, `set metric` (MED), AS-path prepend.

## Next_Hop & eBGP multihop
- eBGP next hop = advertising peer's interface IP; **iBGP keeps the eBGP-learned next hop unchanged** → that next hop must be reachable or rewritten. eBGP peers are expected directly connected; `neighbor ebgp-multihop [ttl]` relaxes that. Loopback peering needs `neighbor update-source loopbackN` (and `disable-connected-check` for single-hop loopback eBGP). Use `next-hop-self` for non-reflected routes; on an RR use an outbound route-map `set ip next-hop` instead.

## Communities (and RT/SoO extended)
- A community tags routes sharing a policy; **not sent unless `neighbor send-community`** is configured. Well-known: `no-export` (don't advertise to eBGP), `no-advertise` (don't advertise to anyone), `local-as` (don't leave the local AS/confed), `internet`, `gshut`. Extended (MPLS-VPN): **Route Target** (which VRFs import) and **Site of Origin** (prevents re-advertising a route back to its origin site).

## Route reflectors
- iBGP normally needs a full mesh (an iBGP speaker won't re-advertise iBGP-learned routes to another iBGP peer). An **RR** reflects, so clients needn't be meshed. RR+clients = a cluster (`bgp cluster-id`, shared 4-byte ID for multiple RRs). Loop avoidance via **Originator-ID** (originator drops its own route) and **Cluster-list** (RR drops an update carrying its own cluster ID). On reflected routes only `set ip next-hop` is honored; disable client-to-client reflection if clients are already meshed.

## Route dampening
- Suppresses flapping routes: each flap adds penalty **1000**; **suppress 2000**, **reuse 750**, **half-life 15 min**, max-suppress 4× half-life. A peer reset adds no penalty, but cumulative flaps do. eBGP routes learned via iBGP aren't dampened. Defaults can over-dampen a single reset → tune.

## Confederations & AS migration
- **Confederation**: split one AS into sub-ASes that look like one (the confederation identifier) externally; sub-AS sessions run eBGP but preserve next-hop/MED/Local_Pref like iBGP.
- **AS migration**: `neighbor local-as` makes a router appear (to an eBGP peer) as a member of an old AS to merge a purchased AS without disrupting peering; `dual-as` lets the peer use either ASN during transition. High loop risk — true eBGP only, filter the transitional AS, deconfigure after.

## Troubleshooting (symptom → cause)
- 4-byte ASN regex stops matching after asdot → escape the dot (`1\.14`) and `clear ip bgp *`.
- eBGP session won't form over loopbacks → needs `ebgp-multihop` + `update-source loopback` (+ `disable-connected-check` single-hop).
- iBGP routes not installed / next hop unreachable → eBGP next hop kept unchanged into iBGP; make it reachable or rewrite it.
- Path with no MED beats one with MED → Cisco missing-MED-as-0 default; `bgp bestpath med missing-as-worst`.
- Neighbor's MED ignored → MED compared only within same neighbor AS; `bgp always-compare-med`.
- Community policy never matches → `neighbor send-community` not set, or a transit device dropped the attribute.
- Outbound route-map `set` ignored leaving an RR → only `set ip next-hop` honored on reflected routes.
- Stable routes suppressed after one reset → dampening defaults too aggressive; tune.
- Loops during AS merge → misconfigured local-as/dual-as; filter the transitional AS, true eBGP only.
