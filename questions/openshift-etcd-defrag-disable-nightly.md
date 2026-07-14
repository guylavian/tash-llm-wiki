---
title: "OpenShift etcd: don't disable automatic defrag to dodge nightly sluggishness"
type: question
question_tier: support-kb
domain: openshift
slug: openshift-etcd-defrag-disable-nightly
summary: "The 'OpenShift defrags all etcd members simultaneously on a fixed daily schedule' premise is wrong on both counts — auto-defrag is threshold-driven (>=45% fragmentation) and runs one member at a time. Disabling it to run manually is not documented/recommended and risks a quota-alarm maintenance-mode outage; the 1 GB / 7200-RPM timing example in the docs (~1m40s per member) is exactly your case."
sources:
  - ref:etcd-4-22-etcd-overview
  - ref:etcd-4-22-etcd-performance
  - ref:post-installation-configuration-4-22-cluster-tasks
  - ref:etcd-4-22-etcd-practices
provenance:
  extracted: 9
  inferred: 4
  ambiguous: 0
status: draft
updated: 2026-07-12
---

> ⚠️ Out of corpus coverage — `openshift` holds `conceptual` only; this is a `support-kb` question and that tier is not ingested; verify against the primary source.

# OpenShift etcd: don't disable automatic defrag to dodge nightly sluggishness

Short answer: **yes, there are real reasons not to do this** — and two of your premises about how OpenShift defrags etcd are incorrect, which changes the diagnosis entirely.

## Your premise is wrong on two facts

1. **OpenShift does NOT defrag all members simultaneously.** The docs are explicit: *"OpenShift Container Platform automatically runs the etcd defragmentation on one etcd member at a time"* (`etcd-4-22-etcd-overview.md:146`, also `etcd-4-22-etcd-performance.md:905`). One member at a time means the *other* two keep serving; the cluster stays available.
2. **It is NOT a fixed daily schedule.** Auto-defrag is *threshold-driven*: it triggers *"when it detects at least 45% fragmentation"* (`etcd-4-22-etcd-overview.md:146`). History **compaction** runs automatically every five minutes and leaves gaps (`etcd-4-22-etcd-performance.md:557`), but compaction ≠ defragmentation. So a *fixed nightly* pattern is not the auto-defrag cron firing — it's far more likely that a nightly workload pushes fragmentation across the 45% line at roughly the same time each night, and only then does OpenShift defrag (one member at a time). **Verify before acting** (see below).

## Your exact 1 GB / spinning-disk case is documented

The docs give a worked example that matches your environment almost exactly:

> *"writing an etcd database of 1 GB to a slow 7200 RPMs disk at 80 Mb per second takes about 1 minute and 40 seconds. In such a scenario, the defragmentation process takes at least this long."* (`etcd-4-22-etcd-overview.md:154`)

That ~1m40s is the **blocking window per member**, because *"During the defragmentation process, the etcd member cannot process any requests"* (`etcd-4-22-etcd-overview.md:146`). Crucially, because OpenShift already does this **one member at a time**, only one member is blocked at any moment — the control plane stays up. The larger point the docs make: *"With larger etcd databases, the disk latency directly impacts the fragmentation time"* (`etcd-4-22-etcd-overview.md:146`).

## Why disabling automatic defrag is a bad idea

- **It isn't the recommended posture, and there's no supported "off switch" in the corpus.** The guidance is the opposite: *"Automatic defragmentation is good for most cases, because the etcd operator uses cluster information to determine the most efficient operation for the user"* (`etcd-4-22-etcd-performance.md:563`) and *"The etcd Operator automatically defragments disks. No manual intervention is needed"* (`etcd-4-22-etcd-performance.md:569`). The disable procedures that *do* exist in the corpus cover etcd **encryption**, **KMS**, and the **quorum guard during disaster recovery** (`etcd-4-22-etcd-encrypt.md:181`, `etcd-4-22-kms-disabling.md:19`, `etcd-4-22-etcd-disaster-recovery.md:377`) — **not** automatic defragmentation. (inferred) There is no documented knob to turn automatic defrag off; if you somehow suppress it, you own the entire failure mode below.
- **Skipping defrag risks a far worse outage than a ~1m40s blip.** If fragmentation is left to accumulate, *"etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode that accepts only key reads and deletes"* (`etcd-4-22-etcd-performance.md:547`). That is a control-plane-wide freeze — orders of magnitude worse than one member blocking for ~1m40s while the other two serve.
- **Manual defrag does not remove the blocking — it relocates it, and must still be sequential.** The manual procedure is itself a blocking, one-at-a-time operation: *"wait at least one minute between defragmentation actions on each of the pods… Always defragment the leader last"* (`etcd-4-22-etcd-performance.md:610`, `:712-714`). If you "run it manually during maintenance windows" by hitting all three members at once, you block the whole quorum and take the control plane down. So disabling auto-defrag buys you nothing on the latency front and adds operational risk.
- **The restart you may be seeing is the documented benign side effect, not a defect.** *"Automatic defragmentation can cause leader election failure in various OpenShift core components, such as the Kubernetes controller manager, which triggers a restart of the failing component. The restart is harmless"* (`etcd-4-22-etcd-performance.md:579`). That harmless restart is expected behavior of *automatic* defrag — not evidence it should be disabled.

## What to actually do

1. **Confirm it's really defrag.** Check the etcd metrics and logs at the sluggish time:
   - Freeable space: `(etcd_mvcc_db_total_size_in_bytes - etcd_mvcc_db_total_size_in_use_in_bytes)/1024/1024` (`etcd-4-22-etcd-performance.md:606`).
   - Look for `etcd member has been defragmented: <member_name>` in etcd / cluster-etcd-operator logs (`etcd-4-22-etcd-performance.md:586`). If defrag *is* firing nightly, fragmentation is crossing 45% then — find the nightly workload (backups, batch jobs, reconcile storms) causing the churn.
2. **Keep automatic defrag ON.** It is already doing the safe thing (threshold-triggered, one member at a time). (inferred)
3. **Attack the root cause / the disk, not the defragger.** The docs state disk latency drives defrag duration and explicitly recommend *"Prefer high-bandwidth writes for faster compactions and defragmentation"* (`etcd-4-22-etcd-practices.md:45`). For a 1 GB DB on 7200-RPM spinning disks, moving etcd onto faster storage (SSD / higher-IOPS) would cut that ~1m40s window dramatically — that's the real fix for the sluggishness. (inferred)
4. **If you still want manual control**, the supported path is to *trigger* defrag on demand when the Prometheus alert fires (etcd using >50% of available space for >10 min, or actively using <50% of total DB size for >10 min — `etcd-4-22-etcd-performance.md:601-604`), and to do it **sequentially** (≥1 min apart, leader last) — never by disabling the automatic mechanism.

## See also
- [[openshift-architecture-kubernetes-relationship]]
- [[openshift-implementation-review]]

## References

### RH ground-truth
- `ref:etcd-4-22-etcd-overview` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-overview
- `ref:etcd-4-22-etcd-performance` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-performance
- `ref:post-installation-configuration-4-22-cluster-tasks` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/cluster-tasks
- `ref:etcd-4-22-etcd-practices` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-practices
- `ref:etcd-4-22-etcd-encrypt` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-encrypt
- `ref:etcd-4-22-kms-disabling` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/disabling-kms
- `ref:etcd-4-22-etcd-disaster-recovery` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-disaster-recovery

### Wiki
- [[openshift-architecture-kubernetes-relationship]]
- [[openshift-implementation-review]]
