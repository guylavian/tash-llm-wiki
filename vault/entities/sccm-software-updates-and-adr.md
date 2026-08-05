---
title: SCCM Software Updates and Automatic Deployment Rules (ADR)
type: entity
domain: sccm
slug: sccm-software-updates-and-adr
summary: How software update synchronization, compliance scanning, and deployment work in Configuration Manager, and how Automatic Deployment Rules (ADR) automate recurring update cycles like Patch Tuesday.
sources:
  - kb:sum-software-updates-introduction
  - kb:sum-automatically-deploy-software-updates
  - "web:https://learn.microsoft.com/en-us/answers/questions/100121/beyond-post-installation-task-wsus-sccm (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1009541/sccm-2207-adr-0x00000000 (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1008406/sccm-failed-to-get-the-software-upates-package-wit (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1009283/mecm-2107-violation-of-primary-key-constraint-ci-d (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1007437/sccm-2207-and-update-the-windows-server-2019-2022 (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1374259/gpo-wsus-in-windows-11-not-is-applied (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 14
provenance_inferred: 4
provenance_ambiguous: 0
tags: [sccm-updates, troubleshooting]
status: draft
updated: 2026-07-25
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# SCCM Software Updates and Automatic Deployment Rules (ADR)

**Software updates in Configuration Manager synchronize metadata from Microsoft Update at the
top-tier site, propagate it through the hierarchy, get scanned for compliance on clients, and are
deployed either manually or through an Automatic Deployment Rule (ADR) for recurring cycles.**

## Body

### Synchronization and compliance

The top-level site (a CAS or stand-alone primary site) synchronizes with Microsoft Update on a
schedule or on demand; when synchronization finishes there, it cascades to child sites, and each
primary/secondary site publishes a site-wide policy telling clients where the software update
points are. Software updates are enabled by default in client settings — if **"Enable software
updates on clients"** is set to **No** for a collection, clients in it never receive the update
point location. Once a client has the policy, it scans for compliance and writes results to WMI,
which flow up through the management point to the site server.

### Automatic Deployment Rules (ADR)

An ADR automates approving and deploying updates that match defined criteria, adding matched
updates either to a **new** software update group each run, or to an existing group (in which
case the rule *removes all updates* from that group first, then re-adds whatever currently
matches). ADRs are the recommended way to handle recurring cycles — monthly "Patch Tuesday"
updates and Endpoint Protection definition updates — rather than manually adding updates to a
group every cycle. Built-in templates (e.g. **Patch Tuesday**, **Office 365 Client Updates**)
seed common ADR settings.

**Critical prerequisite:** verify the site has completed **software updates synchronization**
before creating the first ADR — this matters especially on a non-English site, because update
classifications display in English until the first sync completes and then switch to the
localized strings. An ADR authored against the pre-sync English strings can fail to match
anything once synchronization has run and the display switches (inferred — the source states the
mismatch mechanism; the "fail to match anything" consequence is derived from it, not spelled out
verbatim).

## Community Q&A (upstream)

> Microsoft Q&A community threads — not Microsoft support statements. Weighted by
> answerer role below; treat unconfirmed community diagnoses as hypotheses, not fixes.

### WSUS post-installation task is a hard prerequisite for the SUP role
Before a Software Update Point can be installed, the underlying WSUS server must have
completed its **post-installation task** — it creates the SUSDB database, the WSUS
content directories, the IIS application pool, and imports the publisher info (Windows,
Office, SQL, etc.) that ConfigMgr needs to recognize WSUS as ready for synchronization.
If this task hasn't run, **the SUP role installation itself fails**, because the SUP role
has a hard dependency on WSUS being configured — this is not a "sync will just be
degraded" situation. Separately, the **WSUS Configuration Wizard** that launches after
post-install (or on first console open) should be **cancelled, not completed** — ConfigMgr
manages products/classifications and similar settings itself. Both points confirmed independently by
a Microsoft-employee moderator and an MVP (thread:100121).

### ADR status `0x00000000` means success — a recurring false-alarm pattern
`0x00000000` in the ADR/rule-engine log is the generic Windows success code, not an error —
it means the Software Update Group was created and deployed to the target collection
successfully. If clients still show **zero updates installed**, the ADR isn't broken; the
matched updates are simply **not "Required"** on those clients, or the client scan
itself isn't completing successfully. Diagnose by opening the deployed Software
Update Group, clicking **Show Members**, and checking each client's Required/Not Required
compliance state, rather than re-authoring the ADR (vendor-confirmed, thread:1009541).
This directly extends the existing ADR-prerequisite caveat above (inferred — neither thread
makes this cross-reference) — a mis-timed ADR and a
"successful but nothing-to-deploy" ADR produce the same symptom (client gets nothing) from
two different root causes, so check compliance state before assuming a sync/timing bug.

### "Failed to get the software updates package with ID X"
This ADR/deployment error traces to the **Deployment Package** referenced by the rule
being missing. Fix: open the ADR's Properties >
**Deployment Packages** tab, confirm the package still exists and its source path is
valid (Software Library > Deployment Packages > Properties > General); if it's gone,
create a new deployment package and re-point the rule at it (community answers, thread
unresolved/no accepted answer — no Microsoft-employee or MVP participation, weaker
evidence than the other entries here; thread:1008406).

### MECM 2107 WSUS sync abort — `PRIMARY KEY constraint 'CI_DocumentStore_PK'` (inferred/community, unconfirmed)
A community member self-diagnosed a WSUS sync that aborts with "Too many consecutive
failures" after repeated `Violation of PRIMARY KEY constraint 'CI_DocumentStore_PK'`
errors in `wsyncmgr.log`. Their finding: the built-in `spCheckReseedIdentity` stored
procedure was resetting the `CI_DocumentStore` table's identity seed back down to
`16777215` (the value returned by `dbo.fnGetSiteRangeEnd`) even though the table's real
current max value was much higher (~33.5M), so the next insert collided with an existing
row. Their workaround: `DBCC CHECKIDENT('CI_DocumentStore', RESEED)` to reseed the
identity to the actual current max, — but the thread's own log shows
`spCheckReseedIdentity` reset the seed again on the very next sync and the identical
`CI_DocumentStore_PK` primary-key violation recurred immediately; the reporter never
confirmed a lasting fix.
**This is a single community member's own diagnosis with 1 upvote and zero Microsoft or
MVP confirmation** — a genuine root cause, not a documented Microsoft fix (thread:1009283).
See caveat below before applying a direct `DBCC CHECKIDENT` write against the CM database.

### Controlling ADR-driven reboots on servers
To let an ADR patch servers without an uncontrolled reboot: put the target servers in a
collection with a configured **maintenance window**, and set **"suppress restart"** in
the ADR's deployment settings — updates then only install during the maintenance window,
and the server is not rebooted until an admin does so manually (vendor-confirmed,
thread:1007437). This is the concrete mechanism behind the sync/timing caveat in the
prerequisite section above: even a correctly-timed ADR still needs restart behavior
constrained separately, or a maintenance-window-driven install can leave a server
"successfully patched but pending reboot" indefinitely.

### GPO-delivered WSUS policy not applying on a Windows 11 client
When a client isn't picking up its WSUS-related Group Policy, the recurring diagnosis in
this thread is a **GPO precedence/order problem** among existing GPOs, not an SCCM- or
WSUS-side bug. Troubleshoot with `gpresult /h <file>.html` (produces an RSOP report
showing exactly which GPO won and why) and by checking the applied registry state at
`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` — confirmed
independently by an MVP ("you likely have an ORDER problem with existing GPOs") and a
vendor-affiliated support answer (same `gpresult` + registry-key approach; thread:1374259).
One user's own resolution in the same thread was simply reformatting the server from
scratch — an anecdotal last resort, not a generalizable fix.

## Contradictions / caveats

The `CI_DocumentStore` identity-reseed workaround above is **not** a Microsoft-documented
fix — directly reseeding an identity column in the ConfigMgr site database with `DBCC
CHECKIDENT` is a database-level intervention Microsoft doesn't publish guidance for, and
the reporting community member noted the underlying stored procedure could reset the seed
again afterward. Treat it as a diagnosed-but-unresolved workaround: verify against a test
site or open a support case before running it against production, and re-check
`wsyncmgr.log` after synchronization to confirm the reseed actually held.

## See also
- [[sccm-overview]]
- [[sccm-collections]]
- [[sccm-compliance-baselines]]
- [[sccm-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[sum-software-updates-introduction|Introduction to software updates]]
- [[sum-automatically-deploy-software-updates|Automatically deploy software updates]]
<!-- crosslink:end -->
