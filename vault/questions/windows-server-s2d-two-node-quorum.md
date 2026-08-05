---
title: "Do we need a quorum witness for a 2-node Storage Spaces Direct cluster, and what happens when we reboot one node?"
type: question
question_tier: conceptual
domain: windows-server
slug: windows-server-s2d-two-node-quorum
summary: Yes — a 2-node Storage Spaces Direct cluster needs a witness (a file share witness, since S2D has no shared disk) because with only 2 node votes, rebooting either node leaves exactly 1 of 2 votes and the cluster stops; the witness supplies the tie-breaking third vote.
sources:
  - kb:failover-clustering-what-is-quorum-witness
  - kb:failover-clustering-deploy-quorum-witness
  - kb:storage-storage-spaces-direct-overview
  - kb:storage-storage-spaces-direct-hardware-requirements
provenance:
  extracted: 5
  inferred: 1
  ambiguous: 0
tags: [win-storage, failover-clustering]
status: draft
updated: 2026-07-23
graph_community: "Windows Server — Overview"
---

# Do we need a quorum witness for a 2-node Storage Spaces Direct cluster, and what happens when we reboot one node?

**Yes. A 2-node Storage Spaces Direct (S2D) cluster with no witness has exactly 2
quorum votes; taking either node down for a reboot or patching leaves 1 of 2 votes
active, which is not a strict majority, so the cluster stops.**

## Body

Failover Clustering requires **more than half** of the total configured quorum
votes to be active for the cluster to keep running; if the count drops below that
threshold the cluster service stops to avoid a split-brain scenario
(`reference/windows-server/failover-clustering-what-is-quorum-witness.md:17-19`).
With only 2 nodes and no witness, each node holds one vote — 2 total votes — so
losing (or rebooting) one node leaves exactly 1 active vote, which is **not** more
than half of 2, and the cluster goes offline
(`reference/windows-server/failover-clustering-what-is-quorum-witness.md:19,31`,
the "Node majority (no witness)" quorum-mode row).

**The fix is a quorum witness**, which adds a third, tie-breaking vote so the
cluster tolerates one node going down: "As a best practice, configure the quorum
to have an odd number of voting elements. If the cluster has an even number of
voting nodes, add a disk witness or a file share witness"
(`reference/windows-server/failover-clustering-what-is-quorum-witness.md:31`).

**Which witness type for S2D specifically?** A **disk witness** requires a shared
disk all nodes can reach — Storage Spaces Direct clusters explicitly **don't have**
one (the whole point of S2D is that storage is direct-attached, not shared), so the
documented guidance is a **file share witness** instead: "A disk witness can't be
used because there aren't any shared drives to use for a disk witness. For example,
a Storage Spaces Direct cluster... None of these types of clusters use shared disks"
(`reference/windows-server/failover-clustering-what-is-quorum-witness.md:87-89`). A
**cloud witness** (Azure Blob Storage) is also viable and is explicitly called out
as suited to "small branch-office clusters, which are even two-node clusters"
(`reference/windows-server/failover-clustering-deploy-quorum-witness.md:51`).

**What actually happens on a planned single-node reboot with a witness
configured:** with the witness supplying the third vote, the surviving node (1
vote) plus the witness (1 vote) = 2 of 3 votes, a strict majority, so the cluster
keeps running while the rebooted node is down (extracted mechanically from the
majority-vote rule above; the source doesn't narrate this specific 2-node-plus-
witness arithmetic verbatim, so this restatement is **(inferred)** from the general
quorum-vote formula).

**Distinct but related ceiling:** even *with* dynamic quorum management enabled,
"In clusters with Storage Spaces Direct enabled, the cluster can only tolerate up
to two node failures" (`reference/windows-server/failover-clustering-what-is-quorum-witness.md:121`)
— so on a larger S2D cluster, a witness prevents the *2-node-specific* single-vote
problem above, but does not raise S2D's separate, hard 2-node-failure tolerance
ceiling.

### What was asked vs. the correct approach

The question assumes a witness is optional "nice to have" for small clusters; the
corpus is explicit that it's required best practice for **any even node count**,
and the "obvious" 2-node case is the textbook example the docs use to justify the
rule.

## Contradictions / caveats

None found — the disk-witness-unavailable-for-S2D point and the odd-vote-count
best practice are stated consistently across both quorum-witness reference notes.

## See also
- [[failover-cluster-quorum]]
- [[storage-spaces-direct]]
- [[windows-server-implementation-review]]

## References

**RH ground-truth — n/a (Microsoft Learn corpus, not Red Hat)**

**Microsoft Learn reference tier (`kb:`)**
- `kb:failover-clustering-what-is-quorum-witness` — "What is a failover cluster quorum witness in Windows Server?"
- `kb:failover-clustering-deploy-quorum-witness` — "Deploy a quorum witness for a failover cluster in Windows Server"
- `kb:storage-storage-spaces-direct-overview` — "Storage Spaces Direct overview"
- `kb:storage-storage-spaces-direct-hardware-requirements` — "Storage Spaces Direct Hardware Requirements in Windows Server"

**Wiki**
- [[failover-cluster-quorum]]
- [[storage-spaces-direct]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[failover-clustering-what-is-quorum-witness|What is a failover cluster quorum witness in Windows Server?]]
- [[failover-clustering-deploy-quorum-witness|Deploy a quorum witness for a failover cluster in Windows Server]]
- [[storage-storage-spaces-direct-overview|Storage Spaces Direct overview]]
- [[storage-storage-spaces-direct-hardware-requirements|Storage Spaces Direct Hardware Requirements in Windows Server]]
<!-- crosslink:end -->
