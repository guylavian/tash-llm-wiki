# OSPF — raw notes

**Source:** Cisco *IP Routing: OSPF Configuration Guide*, Cisco IOS XE 16 (`iro-xe-16-book`).
Distilled/paraphrased — provenance, not transcript. OSPFv2 is a link-state IGP per RFC 2328.

## Network / media types
- Three types: **broadcast** (Ethernet/FDDI), **NBMA** (Frame Relay, X.25, SMDS), **point-to-point** (HDLC, PPP). Type is auto-classified but overridable with `ip ospf network {broadcast | non-broadcast | point-to-point | point-to-multipoint [non-broadcast]}`.
- **Broadcast and NBMA elect a DR/BDR; point-to-point and point-to-multipoint do not.**
- **point-to-multipoint** treats a partial-mesh/hub-spoke NBMA cloud as numbered P2P links on one subnet — avoids a full mesh and DR election. The `non-broadcast` variant needs explicit `neighbor ip-address [cost n]` statements (no dynamic discovery) and is the only way to set per-neighbor cost. Frame Relay/X.25 maps need `broadcast` for OSPF to flood.

## Cost metric
- cost = `auto-cost reference-bandwidth` / interface-bandwidth; or set explicitly `ip ospf cost`.
- **Default reference bandwidth = 10^8 (100 Mbps).** So 64 kbps→~1562, T1→64, and **every link ≥100 Mbps (GigE/10GigE) computes to cost 1** and becomes indistinguishable. Raise `auto-cost reference-bandwidth` consistently on all routers to differentiate high-speed links.

## Administrative distance
- Three independent OSPF distances, **all default 110**: intra-area, inter-area, external. `distance ospf {intra-area | inter-area | external} dist`. Changing one leaves the others at 110; 255 = ignore.

## Router ID
- 32-bit ID: **highest loopback IP if any loopback exists, else highest active interface IP.** If the interface owning the ID goes down, OSPF recomputes the ID and re-floods everything (disruptive) → always configure a loopback for a stable ID.

## NSSA (Not-So-Stubby Area)
- Stub-like area that forbids Type-5 external LSAs but allows an NSSA ASBR to originate **Type-7** LSAs; the NSSA ABR translates Type-7→Type-5 into the backbone. Cisco follows RFC 3101 (backward-compatible with RFC 1587; `compatible rfc1587` to fall back).
- `area id nssa [no-redistribution] [default-information-originate] [no-summary] [nssa-only]`; `area id nssa translate type7 always` forces this ABR as translator; `suppress-fa` drops the forwarding address. All routers in the area must agree it is NSSA or adjacency fails.

## Interface timers & authentication
- `ip ospf hello-interval`, `dead-interval` (**defaults to 4× hello**), `retransmit-interval`, `priority` (0 = never DR/BDR). hello/dead must match on a segment or neighbors never reach FULL.
- Auth: plaintext `ip ospf authentication-key` + `area id authentication`; MD5 `ip ospf message-digest-key key-id md5 key` + `area id authentication message-digest`. Key-id and key must match exactly on both ends. On simplex Ethernet set the sending side `passive-interface`.

## LSA pacing, refresh, SPF throttle
- LSA max-age **3600 s**, refresh every **30 min**, checksum every **10 min**. **Group pacing default 240 s** (range 10–1800, randomized) — shorten for very large DBs (~10k LSAs), lengthen for tiny ones. `timers pacing lsa-group`. Cisco doesn't support Type-6 MOSPF → `ignore lsa mospf` to silence log noise. `ip ospf flood-reduction` sets DoNotAge in stable topologies.
- SPF throttle `timers throttle spf spf-start spf-hold spf-max-wait` — **values are milliseconds, not seconds** (common misconfig); exponential backoff up to max-wait.

## Troubleshooting (symptom → cause)
- Neighbors stuck INIT/EXSTART/2-WAY, never FULL → mismatched hello/dead, area-type disagreement, MTU mismatch, or auth mismatch (type/key/key-id).
- All ≥100 Mbps links show cost 1 → default reference-bandwidth clips them; raise it consistently.
- Router ID keeps changing + full re-flood after a flap → ID came from a physical interface; add a loopback.
- External routes don't enter/leave an NSSA → no ASBR redistributing Type-7, or the ABR isn't the (forced) Type-7→Type-5 translator.
- Excessive MOSPF (Type-6) syslog → neighbor sending unsupported Type-6; `ignore lsa mospf`.
- Router-LSA too large → too many OSPF interfaces overflow the huge buffer; reduce links or `buffers huge size`.
