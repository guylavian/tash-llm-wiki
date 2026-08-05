---
title: Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: sccm
slug: sccm-implementation-review
summary: The evaluation lens and Map of Content for the sccm brain — a rule → anti-pattern → symptom checklist across site hierarchy, client health, collections, application deployment, content/distribution points, OSD, software updates/ADR, compliance baselines, and co-management, plus a symptom → likely-cause reverse index built from the troubleshoot-mem-configmgr break-fix corpus.
sources:
  - kb:core-fundamentals-of-sites-and-hierarchies
  - kb:core-client-installation-methods
  - kb:core-client-health-checks
  - kb:core-best-practices-for-collections
  - kb:apps-error-messages
  - kb:core-boundary-groups-distribution-points
  - kb:osd-task-sequence-variables
  - kb:sum-automatically-deploy-software-updates
  - kb:compliance-create-configuration-baselines
  - kb:comanage-workloads
  - kb:sccm-troubleshoot-mem-configmgr-p0081-0120
  - kb:sccm-troubleshoot-mem-configmgr-p0121-0160
  - kb:sccm-troubleshoot-mem-configmgr-p0281-0320
provenance_extracted: 0
provenance_inferred: 28
provenance_ambiguous: 0
tags: [sccm-core, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `sccm` domain.** It indexes SCCM health areas
into a forward checklist (rule → anti-pattern → symptom) and a reverse index (symptom → likely
cause) so an alert or log line can be turned into a cause page. This is the SCCM analogue of
[[active-directory-implementation-review]]; grow it as more of `reference/sccm/` is synthesized.

---

## How to use this page

Read each row left to right: the **Rule** column states what a healthy ConfigMgr deployment must
do; the **Anti-pattern** column states the common misconfiguration; the **Symptom** column names
the observable ticket it produces; the **Page** column links the cause page. To diagnose, jump to
the [Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist

### Site hierarchy and site systems

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Choose CAS-first only when the deployment genuinely needs multi-primary-site scale; a CAS cannot manage clients directly | Standing up a CAS for a single-site deployment "for future growth" | Extra site-to-site replication overhead and administration with no primary site doing client management yet | [[sccm-site-hierarchy]] |
| Each site system role on a site system server must belong to a single site | Reusing one server for site-system roles from two different sites | Role install fails / role behaves inconsistently across the hierarchy | [[sccm-site-hierarchy]] |
| Extend the AD schema and publish site data once per forest so clients can securely discover sites via AD DS | Skipping AD DS publishing, relying only on DNS/WINS discovery | Clients fall back to slower discovery paths; site assignment issues in multi-domain forests | [[sccm-site-hierarchy]] |

### Client installation and health

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Client push requires an account with local admin rights on the target and Windows Firewall exceptions | Client push installation account under-privileged or firewall blocking | Client push retries silently for up to 7 days without ever succeeding | [[sccm-client-health]] |
| Keep every site system and client on the same DCOM-hardening cumulative-update level (post CVE-2021-26414) | Console/site server patched past March 2023 while a remote client or DP is not | `0x80070005` (Access is Denied) / `0x800706ba` (RPC server unavailable) on remote console or client connections | [[sccm-client-health]] |
| Add ConfigMgr installation/client folders to antivirus real-time-protection exclusions | No AV exclusions for `CCM`, `CCMSetup`, `SCCMContentLib`, MP outboxes | Client push fails, Software Center doesn't populate, `CCMRepair.log` shows `0x80004005` | [[sccm-client-health]] |
| Monitor the client health dashboard (Monitoring > Client status) for failed/inactive clients | Dashboard never reviewed; "failed" clients accumulate silently | Compliance and inventory reporting under-counts real managed population | [[sccm-client-health]] |

### Collections

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Scale back collection evaluation schedules in a deep collection tree; a limiting collection's update cascades to every collection it limits | Frequent incremental/scheduled evaluation on many nested collections | Elevated `colleval.log` activity, collection evaluation performance degradation | [[sccm-collections]] |
| Size maintenance windows to the update's max run time + 5 minutes for restart | Maintenance window shorter than the default 60-minute update run time + restart buffer | Updates fail to complete inside the maintenance window, leaving clients unpatched | [[sccm-collections]] |
| Use custom collections for targeting, not the built-in All Systems | Deploying directly to All Systems as a shortcut | Unintended software/updates pushed to out-of-scope devices | [[sccm-collections]] |

### Application deployment

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Give every deployment type a correct detection method before deploying | Detection method missing/wrong, or copied from an unrelated app | Application shows as "unknown"/re-installs repeatedly; simulated deployment mismatches real result | [[sccm-application-deployment]] |
| Use application supersedence to retire old versions instead of ad hoc uninstall scripts | Old and new application revisions deployed to overlapping collections | Conflicting install/uninstall actions on the same client | [[sccm-application-deployment]] |
| Check `PCMtrace.log`/`SMSProv.log` verbosity 4 when Package Conversion Manager conversion fails | Ignoring PCM error dialogs, retrying blind | "Application creation failed" / "Conversion Error" with no root-cause investigation | [[sccm-application-deployment]] |

### Content and distribution points

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Ensure the content-library service account/permissions and network path to the DP are healthy before large content distributions | Permission or connectivity issue on the DP's content-library share | `CSendFileAction::SendContent failed; 0x8007052e` in `distmgr.log`, paired Event ID 4625 (logon failure) on the DP | [[sccm-distribution-points]] |
| Design boundary groups so every client site has a local, in-scope content source | Boundary groups missing a site's subnet, or DPs not associated with the right boundary group | Clients fall back across the network to a neighbor boundary group / fail to find content | [[sccm-distribution-points]] |

### Task sequences and OSD

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Distribute boot image, OS image, and referenced content to a DP *before* deploying the task sequence | Task sequence deployed while referenced content is still distributing | Task sequence fails at content-download steps; devices stall in WinPE | [[sccm-task-sequences-and-osd]] |
| Use documented task sequence variables (`_OSDDetectedWinDir`, etc.) instead of hardcoding paths | Hardcoded drive letters/paths in custom steps | Task sequence breaks on hardware with a different partition layout | [[sccm-task-sequences-and-osd]] |

### Software updates and ADR

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Complete an initial software updates synchronization before creating the first ADR | ADR authored immediately after site install, before first sync | ADR criteria silently fail to match because classification/product strings are still in English pre-sync | [[sccm-software-updates-and-adr]] |
| Let the top-tier site synchronize with Microsoft Update on schedule; don't disable the client setting that ships update-point location | "Enable software updates on clients" set to No on a target collection | Clients never receive the software update point location; scan/compliance data stays empty | [[sccm-software-updates-and-adr]] |

### Compliance baselines

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Don't assume configuration-item evaluation order inside a baseline — it's explicitly non-deterministic | Baseline design that depends on one CI running before another | Intermittent, hard-to-reproduce compliance results across otherwise-identical clients | [[sccm-compliance-baselines]] |
| Deploy the baseline to a collection before expecting compliance data | Baseline created but never deployed | No compliance results reported anywhere | [[sccm-compliance-baselines]] |

### Co-management

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Pilot a workload switch on a small collection before switching org-wide | Switching a workload to Intune for all devices on day one | Widespread policy conflicts if the Intune-side policy isn't ready | [[sccm-co-management]] |
| Know that switching a workload back to ConfigMgr can leave state behind (e.g. Windows/Office versions installed by Intune stay at that version) | Switching workloads back and forth without accounting for one-way side effects | Version drift between devices that never explains itself from ConfigMgr alone | [[sccm-co-management]] |

---

## Reverse index — symptom → likely cause

Each signature is drawn from the `symptoms:` frontmatter of the referenced page and the
`sccm-troubleshoot-mem-configmgr-*` break-fix corpus.

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `CSendFileAction::SendContent failed; 0x8007052e` / `CContentDefinition::TotalFileSizes failed` + Event ID 4625 on the content-library host | Permission or authentication failure reaching the distribution point's content library share | [[sccm-distribution-points]] |
| `0x80070005` (Access is Denied) / `0x800706ba` (RPC server is unavailable) on remote console, remote client tools, or remote content distribution | DCOM hardening (CVE-2021-26414) applied on one side (console/site server/client) but not the other; mismatched cumulative-update level | [[sccm-client-health]], [[sccm-admin-service]] |
| Event ID 10036 (server-side) / 10037, 10038 (client-side) DCOM authentication-level events | Same DCOM hardening mismatch — application/service activating a DCOM server below `RPC_C_AUTHN_LEVEL_PKT_INTEGRITY` | [[sccm-client-health]] |
| `0x80070005` in `SiteComp.log` / `Distmgr.log` / `hman.log`; client push installation never completes; Software Center stops populating | Antivirus real-time protection blocking ConfigMgr install/content folders (no exclusions configured) | [[sccm-client-health]] |
| `CCMRepair.log`: "Database verification failed with result: 0x80004005 but DB: ...ccm\filename.sdf could be opened, skipping DB repair" | Local client SDF database corruption, often surfaced alongside AV interference | [[sccm-client-health]] |
| Client push retries for days without success | Client push installation account lacks local admin rights, or Windows Firewall blocks the push | [[sccm-client-health]] |
| ADR runs but adds zero updates to the deployment | ADR authored/run before the site's first software updates synchronization completed | [[sccm-software-updates-and-adr]] |
| Application shows "unknown" detection state or reinstalls on every cycle | Deployment type detection method missing or incorrect | [[sccm-application-deployment]] |
| Baseline shows no compliance data for any device | Baseline created but not deployed to a collection | [[sccm-compliance-baselines]] |
| Clients repeatedly fetch content from a neighbor site over the WAN instead of a local DP | Boundary group missing the client's subnet, or DP not linked to the right boundary group | [[sccm-distribution-points]] |

---

## Domain map — pages by area

- [[sccm-overview]] — spine: hierarchy, client lifecycle, four core workloads, extensibility
- [[sccm-site-hierarchy]] — CAS/primary/secondary, site systems, AD DS publishing
- [[sccm-client-health]] — install methods, health checks/dashboard, DCOM hardening, AV exclusions
- [[sccm-collections]] — targeting unit, evaluation graph, best practices
- [[sccm-application-deployment]] — applications, deployment types, supersedence, PCM errors
- [[sccm-distribution-points]] — content library, boundary groups, content distribution failures
- [[sccm-task-sequences-and-osd]] — task sequences, boot/OS images, deployment scenarios
- [[sccm-software-updates-and-adr]] — synchronization, deployment, automatic deployment rules
- [[sccm-compliance-baselines]] — configuration items/baselines, deployment, evaluation
- [[sccm-co-management]] — workloads, pilot groups, cloud attach
- [[sccm-admin-service]] — REST API over the SMS Provider
- [[sccm-powershell-module]] — `ConfigurationManager` module, cmdlets, site PSDrive

## See also
- [[active-directory-implementation-review]] — Active Directory domain equivalent of this MOC
- [[sccm-overview]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[core-fundamentals-of-sites-and-hierarchies|Fundamentals of sites and hierarchies]]
- [[core-client-installation-methods|Client installation methods]]
- [[core-client-health-checks|Client health checks]]
- [[core-best-practices-for-collections|Collections best practices]]
- [[apps-error-messages|Error messages]]
- [[core-boundary-groups-distribution-points|Boundary groups and distribution points]]
- [[osd-task-sequence-variables|Task sequence variable reference]]
- [[sum-automatically-deploy-software-updates|Automatically deploy software updates]]
- [[compliance-create-configuration-baselines|Create configuration baselines]]
- [[comanage-workloads|Co-management workloads]]
- [[sccm-troubleshoot-mem-configmgr-p0081-0120|Welcome — pages 81-120]]
- [[sccm-troubleshoot-mem-configmgr-p0121-0160|Welcome — pages 121-160]]
- [[sccm-troubleshoot-mem-configmgr-p0281-0320|Welcome — pages 281-320]]
<!-- crosslink:end -->
