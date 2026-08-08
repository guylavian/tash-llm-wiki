---
title: "Why did every mailbox database in my DAG dismount at once after a brief network blip?"
type: question
domain: exchange
slug: exchange-dag-quorum-loss-dismount
summary: A DAG's databases all dismount simultaneously when the underlying Windows failover cluster loses quorum (e.g. witness server unreachable during a network partition) — this is by design, not corruption, and recovery requires restoring quorum before any database remounts.
sources:
  - kb:exchange-exchange-servertoc-p2601-2640
  - kb:exchange-exchange-servertoc-p2681-2720
provenance:
  extracted: 5
  inferred: 2
  ambiguous: 0
question_tier: support-kb
tags: [exchange-ha, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "Exchange Server — Implementation Review (Evaluation-Lens MOC)"
---

# Why did every mailbox database in my DAG dismount at once after a brief network blip?

⚠️ Out of corpus coverage — `exchange` holds `conceptual` only; this is a
`support-kb` question and that tier is not ingested; verify against the primary
source before treating this as a confirmed fix.

## Answer

**This is expected clustering behavior, not database corruption: the DAG's
underlying Windows failover cluster lost quorum, and Exchange is required to
terminate all DAG operations and dismount every mounted database in the DAG until
quorum is restored.**

**Why quorum governs this.** Every DAG runs on a Windows failover cluster
underneath it, and failover clusters use **quorum** — "a consensus of voters to
ensure that only one subset of the cluster members ... is functioning at one
time." The documentation states this outcome explicitly: **"If the cluster loses
quorum, all DAG operations terminate and all mounted databases hosted in the DAG
dismount. In this event, administrator intervention is required to correct the
quorum problem and restore DAG operations"**
(`exchange-exchange-servertoc-p2601-2640.md:440-454`, extracted). Quorum exists to
guarantee consistency (a shared, agreed-upon view of cluster state), act as a
tie-breaker to avoid the cluster splitting into two conflicting halves
("partitioning"), and keep the cluster responsive
(`exchange-exchange-servertoc-p2601-2640.md:456-459`, extracted — the section is
truncated in the read range but the three stated purposes are explicit).

**Why a "brief" blip caused a full outage rather than a graceful failover.** A
short network partition is exactly the scenario quorum voting is designed to
react to conservatively: if enough voters (nodes and/or the witness) can't reach
each other, the cluster cannot safely determine which side, if either, should
keep running — so it fails closed (dismounts) rather than risk two sides both
believing they're authoritative (inferred synthesis of the quorum-purpose
statement above; the read range doesn't give a worked "witness unreachable" trace,
so verify the specific witness/voter state against `Get-DatabaseAvailabilityGroup`
output and the cluster event log before writing an incident report).

**What determines *how* the cluster reacts / how fast databases remount.** Two
configuration points from the DAG lifecycle discussion govern remount behavior
after quorum is restored:

- The DAG's **witness server** (configured at `New-DatabaseAvailabilityGroup
  -WitnessServer <server>`) is a voter outside the DAG membership itself — if it's
  unreachable during a network event, that's one fewer vote available toward
  quorum (`exchange-exchange-servertoc-p2601-2640.md:412-415, 351-361`, extracted).
- **`AutoDatabaseMountDial`** on `Set-MailboxServer` controls whether a database
  auto-mounts based on activation preference (`GoodAvailability`, the default) or
  waits for stricter replication-catch-up guarantees once the cluster is healthy
  again (`exchange-exchange-servertoc-p2681-2720.md:10-34`, extracted).

**Recovery steps implied by the source:** restore connectivity/voter availability
first (network path to the witness server and/or the other DAG members), confirm
the underlying Windows failover cluster reports healthy quorum, and only then
expect Exchange to remount databases per each one's `AutoDatabaseMountDial`
setting — this is "administrator intervention," per the source, not an automatic
Exchange-side retry (`exchange-exchange-servertoc-p2601-2640.md:452-454`,
extracted).

## Contradictions / caveats
The two source notes don't disagree, but the exact witness-vote arithmetic (how
many total voters, what fraction constitutes majority for a given DAG size) is
**not** in the ranges read here — that's standard Windows failover clustering
quorum math applied to a DAG, and should be verified against a dedicated
clustering/quorum-modes note in `reference/exchange/` before being cited as a
specific threshold.

## References

**RH ground-truth (kb:)**
- `exchange-exchange-servertoc-p2601-2640` — "Database availability groups"
  (lifecycle, witness server, quorum)
- `exchange-exchange-servertoc-p2681-2720` — `AutoDatabaseMountDial` reference

**Wiki**
- [[exchange-database-availability-groups]] — DAG, Active Manager, quorum,
  activation preference
- [[exchange-client-access-namespace]] — why Windows NLB can't run alongside a
  DAG's clustering services
- [[exchange-implementation-review]] — HA rule/anti-pattern/symptom table

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[exchange-exchange-servertoc-p2601-2640|Exchange Server — pages 2601-2640]]
- [[exchange-exchange-servertoc-p2681-2720|Exchange Server — pages 2681-2720]]
<!-- crosslink:end -->
