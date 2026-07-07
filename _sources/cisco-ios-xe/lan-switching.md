# LAN switching — raw notes

**Source:** Cisco *LAN Switching Configuration Guide*, Cisco IOS XE (`lanswitch-xe-16-book`).
Distilled/paraphrased. This is a **router/EtherSwitch-side** guide: VLAN tagging is on
subinterfaces via `encapsulation`, not `switchport trunk`.

## VLAN encapsulation on subinterfaces (802.1Q / ISL)
- Inter-VLAN routing by carving a physical interface into subinterfaces, one VLAN each: `interface fa slot/port.sub` + `encapsulation dot1q vlan-id` (or `encapsulation isl vlan-id`) + `ip address`.
- **802.1Q**: 4-byte tag after source MAC, TPID 0x8100, 3 priority bits + CFI + **12-bit VID (4096 VLANs)**. **ISL**: Cisco-proprietary 26-byte wrapper, 10-bit VID (≤1000 VLANs), Fast Ethernet only. 802.1Q only on Fast/Gigabit Ethernet (not plain Ethernet). ISL and 802.1Q can't be mixed on one trunk.

## Native VLAN / PVID
- Each 802.1Q port has a **PVID = native VLAN (default VLAN 1)**. Untagged ingress frames → native VLAN; native-VLAN egress frames are sent **untagged** (so VLAN-aware and unaware devices share a link). A native-VLAN mismatch silently merges traffic.

## PVST+ (per-VLAN STP ↔ CST interop)
- Interoperates per-VLAN spanning trees with the single **Common Spanning Tree (CST)** of 802.1Q/MST regions. At the PVST+/MST boundary the MST tree maps to the **CST = PVST of VLAN 1 (native)**; other per-VLAN trees are tunneled (BPDUs flooded). CST BPDUs use the IEEE multicast address; others use the SSTP address. SSTP BPDU whose VID ≠ embedded TLV PVID → port blocked for inconsistency.

## STP port states & timers (IEEE 802.1D)
- Five states: **blocking → listening → learning → forwarding**, plus disabled. Listening and learning each last one **forward-delay (default 15 s)** → ~**30 s** to reach forwarding; only learning/forwarding update the MAC table.
- Root = lowest **bridge ID (priority + MAC)**. Defaults: **priority 32768, hello 2 s, forward-delay 15 s, max-age 20 s, port-priority 128.** Short-mode port cost: 10 Mbps=100, 100 Mbps=19, GigE=4. `spanning-tree vlan id root primary` sets priority 8192 (or 1 below the current lowest) and auto-derives timers from diameter — don't hand-tune timers after. Configure root only on a backbone/distribution device, never an access switch.

## EtherChannel (Gigabit EtherChannel)
- **Flow-based load balancing**: header hash → one of **16 buckets** per port channel, each bound to one active member. Default global is flow-based; per-port-channel overrides global. Up to 64 GEC interfaces, 14 members each. Default L3 hash = src/dst IP; 5-tuple (16.4.1+) adds L4 ports/proto. Changing the method (or losing the port channel / last member) **deletes the bucket→link mappings**; on a link failure its buckets are redistributed round-robin. MPLS balances on src/dst IP only (no 5-tuple).
- **LACP 1:1 redundancy** (active/standby, 2 ports): `lacp max-bundle 1` + `lacp fast-switchover` keep one link bundled; the higher port priority (**lower numeric value**) is active; equal priorities = no revert on recovery. Must be enabled on **both ends** or fast switchover fails. `carrier-delay` tunes link-down propagation speed.

## Troubleshooting (symptom → cause)
- Two VLANs merge / untagged hosts land in the wrong VLAN across a trunk → native-VLAN (PVID) mismatch; native frames are untagged and reassigned to each side's native VLAN.
- 802.1Q rejected on plain Ethernet → supported only on Fast/Gigabit Ethernet subinterfaces.
- Port stuck ~30 s before passing traffic → normal 802.1D listening+learning (2× forward-delay).
- Wrong switch became root → lowest bridge ID wins; at default priority the lowest MAC wins. Use `spanning-tree vlan root primary`.
- Trunk port blocked/inconsistent by PVST+ → SSTP BPDU VID didn't match the embedded TLV PVID.
- EtherChannel not balancing after a change → changing the method deletes bucket→member mappings.
- 1:1 redundant bundle won't fast-switch → feature not enabled on both ends, or `max-bundle` ≠ 1.
- Wrong active link / unexpected revert → LACP port priority (lower wins); equal priorities mean no revert.
