---
title: How does Active Directory multi-master replication converge across domain controllers?
type: question
domain: active-directory
slug: ad-multi-master-replication-convergence
summary: AD DS uses a state-based replication engine — USN counters, InvocationID-scoped write tracking, the up-to-dateness vector, and high-water-mark filtering — built on a KCC-generated topology — to converge any write from any DC across the forest.
sources:
  - kb:ad-ds-active-directory-replication-concepts
  - kb:ad-ds-introduction-to-active-directory-replication-and-topology-management-using-windows-powershell-level-100
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controllers-hyper-v
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts (Microsoft Learn — Active Directory Replication Concepts, fetched 2026-06-18)
provenance:
  extracted: 8
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# How does Active Directory multi-master replication converge across domain controllers?

Active Directory Domain Services converges writes across domain controllers through a **state-based replication engine** built on three tracking data structures, a self-healing topology, and last-writer-wins conflict resolution.

## The convergence machinery

### 1. USN (Update Sequence Number)

Every DC assigns a **monotonically increasing USN** to each write transaction (`ad-ds-virtualized-domain-controllers-hyper-v.md:289-291`). This is a *local* counter — each DC maintains its own USN independently; there is no global USN across the forest.

### 2. InvocationID

Each DC's database instance is identified by an **InvocationID** (a GUID stored in the `NTDS Settings` object). When the database is restored or rolled back, the InvocationID resets. Together, `(InvocationID, USN)` uniquely identifies every originating write in the forest (`ad-ds-virtualized-domain-controllers-hyper-v.md:300-313`).

### 3. High-Water Mark (HWM)

The destination DC tracks the **highest USN received from each specific source DC** per directory partition. When a source DC offers changes, the destination responds "I already have everything through USN X from you" — the source skips those (`ad-ds-virtualized-domain-controllers-hyper-v.md:297`). The HWM prevents re-sending the same changes from the same source.

### 4. Up-to-Dateness Vector (UDV)

The UDV tracks the **highest originating write USN seen from *every* DC in the forest**, not just direct partners. When destination DC-A requests changes from source DC-B, it sends its UDV. DC-B compares every pending change's `(originating DC InvocationID, USN)` to the UDV — if DC-A already knows a change through a transitive partner, DC-B skips it (`ad-ds-virtualized-domain-controllers-hyper-v.md:293-295`). This is **propagation dampening**: a change written on DC-1 converges once and does not loop.

### 5. Pull-based replication

Replication is **pull**, not push. At each scheduled interval, the destination DC calls the source, sends its HWM + UDV, and the source returns only the changes the destination has not yet seen.

### 6. Conflict resolution — last-writer-wins

When two DCs independently modify the same attribute before converging, AD uses the **originating timestamp** (from the DC that received the write) as the tiebreaker — later timestamp wins. If timestamps are identical, the higher DC-object-GUID breaks the tie (the canonical MS Learn rule; a rare edge case in practice).

## The topology that carries it

The [[knowledge-consistency-checker]] (KCC) builds inbound connection objects on every DC:

- **Intra-site**: a bidirectional ring with shortcut connections to keep latency ≤3 hops (`ad-ds-active-directory-replication-concepts.md:49`).
- **Inter-site**: a spanning tree over [[site-links-and-replication-schedule]] — one connection between any two sites per directory partition, with cost/interval/schedule set per site link (`ad-ds-active-directory-replication-concepts.md:49-51`).

The KCC runs at intervals, detects failed DCs, and re-routes around them (`ad-ds-active-directory-replication-concepts.md:71`).

## Why it converges (and when it doesn't)

The UDV + HWM pair guarantees **propagation dampening** (no infinite loops) and **eventual convergence**: every DC's UDV eventually reflects every originating write. The topology ensures every DC has a path to every other DC for each partition.

Convergence fails when a DC is restored from a snapshot without VM-GenerationID protection — a **USN rollback** scenario where the old USNs are reused for different writes, creating divergence that the UDV cannot detect because `(InvocationID, USN)` pairs collide (`ad-ds-virtualized-domain-controller-architecture.md:170-183`). Windows Server 2012+ VM-GenerationID safeguards prevent this by resetting the InvocationID on any snapshot restore.

## See also
- [[ad-replication]]
- [[knowledge-consistency-checker]]
- [[site-links-and-replication-schedule]]
- [[active-directory-overview]]
- [[fsmo-roles]]
- [[virtualized-domain-controllers]]

## References
**RH ground-truth (`kb:`)**:
- `ad-ds-active-directory-replication-concepts` — connection objects, KCC topology, site links/bridges/transitivity
- `ad-ds-introduction-to-active-directory-replication-and-topology-management-using-windows-powershell-level-100` — up-to-dateness vector table
- `ad-ds-virtualized-domain-controller-architecture` — USN rollback, VM-GenerationID safeguards
- `ad-ds-virtualized-domain-controllers-hyper-v` — USN, InvocationID, HWM, UDV mechanics

**Wiki pages**:
- [[ad-replication]]
- [[knowledge-consistency-checker]]
- [[site-links-and-replication-schedule]]
- [[active-directory-overview]]
- [[fsmo-roles]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-active-directory-replication-concepts|Active Directory Replication Concepts]]
- [[ad-ds-introduction-to-active-directory-replication-and-topology-management-using-windows-powershell-level-100|Introduction to Active Directory Replication and Topology Management Using Windows PowerShell (Level 100)]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-virtualized-domain-controllers-hyper-v|Virtualizing domain controllers with Hyper-V]]
<!-- crosslink:end -->
