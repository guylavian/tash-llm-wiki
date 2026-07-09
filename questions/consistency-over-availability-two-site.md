---
title: "Why Red Hat's HA guide prefers consistency over availability — and what it means for a two-site setup"
type: question
question_tier: conceptual
domain: keycloak
slug: consistency-over-availability-two-site
summary: "Red Hat's HA guide explicitly prioritizes consistency over availability to prevent stale data (old passwords, invalid sessions) during failures. For a two-site Active/Passive setup this means synchronous DB + Data Grid replication, a FAIL failure policy that errors rather than serves stale data, low-latency requirement, fencing to resolve split-brain, and mandatory manual re-sync after any partition."
sources:
  - guide:high_availability_guide
  - kb:multi-cluster-introduction
  - kb:concepts-multi-site
  - kb:deploy-aws-accelerator-fencing-lambda
source_notes:
  - "[[rhbk-26-4-multi-cluster-introduction]]"
  - "[[rhbk-26-2-concepts-multi-site]]"
  - "[[rhbk-26-0-deploy-aws-accelerator-fencing-lambda]]"
provenance:
  extracted: 7
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# Why Red Hat's HA guide prefers consistency over availability — and what it means for a two-site setup

**The multi-cluster HA guide chooses synchronous replication for both the database and Data Grid, and configures a FAIL failure policy — both are deliberate consistency-first decisions that sacrifice availability during network failures to prevent data corruption.**

## The core tradeoff

The guide states it plainly: *"Therefore, tradeoffs exist between high availability and consistency. The focus of this topic is to prioritize consistency over availability with Red Hat build of Keycloak."* (rhbk-26-4-multi-cluster-introduction.md:115)

The alternative would be **asynchronous** replication: writes return immediately without waiting for the peer site. During a network partition, the two sites would each keep serving requests independently. The guide rejects this because it leads to data loss (rhbk-26-4-multi-cluster-introduction.md:112-114):
- Users could log in with an **old password** after a password change — the DB change never reached the other site before the link died.
- **Stale caches** — an invalidation sent from site A never arrives at site B, so site B continues serving revoked sessions or outdated state.
- **Shadow accounts** — parallel writes at both sites produce conflicting records that are unrecoverable without forensic reconciliation.

So the guide chooses the opposite: **synchronous** replication of both the database (Aurora across AZs) and Data Grid caches (Cross-DC). Every write waits for an acknowledgment from the peer site. If the peer cannot be reached, the **FAIL failure policy** kicks in (rhbk-26-4-multi-cluster-introduction.md:904-905):

> *"The Data Grid is configured with a FAIL failure policy, which ensures consistency over availability. Consequently, all user requests are served with an error message until the failure is resolved, either by restoring the network connection or by disabling cross-site replication."*

## What this means concretely for a two-site setup

| Property | What the consistency-first choice means |
|---|---|
| **Topology** | **Active/Passive only** — not Active/Active. Only one site serves live traffic at a time; the passive site is ready but idle. |
| **DB replication** | **Synchronous** across both sites. No write is considered complete until both sites confirm it. This is why RPO = 0: no committed data is lost on a site failure. |
| **Data Grid replication** | **Synchronous Cross-DC** via external Data Grid. Cached sessions, authentication sessions, login failures, and the `work` invalidation cache are mirrored in real time. |
| **Partition behavior** | **Fail-closed.** When cross-site replication breaks, the FAIL policy returns errors to users — the site will **not** serve degraded traffic with potentially stale data. A **fencing Lambda** then removes one site from the load balancer so the surviving site can resume serving. |
| **Latency requirement** | **< 5 ms suggested / < 10 ms required** round-trip between sites (two AZs in one AWS region). Synchronous replication amplifies every millisecond of inter-site latency into user-facing response-time delay. |
| **Recovery** | After any partition, the sites diverge. A **manual re-sync** procedure is mandatory: take the offline site offline in Data Grid, clear its caches (`actionTokens`, `authenticationSessions`, `loginFailures`, `work`), bring replication back online, then restart RHBK. This triggers a full state transfer ([[site-synchronization]]). |
| **Two-site limit** | Exactly two sites only. More sites increase the probability of a network failure, and with synchronous replication, one slow site would degrade every write across all sites. |
| **Downtime** | Site failover targets **< 2 min** RTO for clean failovers; some scenarios incur **up to 5 min** of downtime, plus the manual re-sync window. |

## In practice: a partition walkthrough

1. The link between site A and site B breaks.
2. Synchronous Data Grid writes from A to B fail.
3. The **FAIL failure policy** makes site A return errors to its users — it will **not** continue serving with stale or incomplete state.
4. A Prometheus alert fires; the **fencing Lambda** detects the cross-site connectivity loss (via Data Grid metrics).
5. The Lambda removes **the partition's other side** (or a quorum-decided victim) from the AWS Global Accelerator endpoint group and **disables cross-site replication** on the surviving site (rhbk-26-4-multi-cluster-introduction.md:906-908).
6. Site A can now serve requests independently.
7. Once the link is restored, a human must run the [[site-synchronization]] procedure — **fencing does not auto-rejoin sites**. The offline site's caches are cleared and populated from the active site via full state transfer.
8. Only then is the offline site re-added to the load balancer.

This is the price of the consistency guarantee: **you never serve stale data, but you need human involvement after every partition** (inferred — the guide describes the fencing + manual re-sync as separate steps; the implication that no auto-rejoin exists is drawn from the chapter's failure-and-recovery flow).

## References
**RH ground-truth (`kb:` / `guide:` / `ref:`)**
- `kb:multi-cluster-introduction` — rhbk-26-4-multi-cluster-introduction.md, Chapter 3 (Multi-cluster deployments concepts and architecture, including the consistency-vs-availability tradeoff, FAIL policy, the two-site limit, and the explainer on synchronous vs asynchronous replication)
- `kb:concepts-multi-site` — rhbk-26-2-concepts-multi-site.md, Chapter 2 (Concepts for multi-site deployments, same tradeoff language for 26.0/26.2)
- `kb:deploy-aws-accelerator-fencing-lambda` — rhbk-26-0-deploy-aws-accelerator-fencing-lambda.md / rhbk-26-4-multi-cluster-introduction.md §3.17 (FAIL policy detail + fencing procedure)

**Wiki**
- [[rhbk-ha-architectures]] — two HA shapes, consistency-first design, naming changes across versions
- [[ha-cross-site]] — Active/Passive building blocks overview
- [[site-synchronization]] — manual re-sync procedure after split-brain
- [[ha-load-balancer-failover]] — AWS Global Accelerator + fencing Lambda
- [[session-persistence-volatile]] — DB-backed vs volatile sessions (the durability tradeoff)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
- [[rhbk-26-2-deploy-aws-accelerator-fencing-lambda|Chapter 12. Deploying an AWS Lambda to disable a non-responding site]]
<!-- crosslink:end -->
