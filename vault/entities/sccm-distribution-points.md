---
title: SCCM Distribution Points and the Content Library
type: entity
domain: sccm
slug: sccm-distribution-points
summary: Distribution points host the content Configuration Manager deploys, deduplicated by the single-instance content library, and matched to clients through boundary groups; content-distribution failures are a common break-fix source.
sources:
  - kb:core-install-and-configure-distribution-points
  - kb:core-the-content-library
  - kb:core-boundary-groups-distribution-points
  - kb:sccm-troubleshoot-mem-configmgr-p0121-0160
  - "web:https://learn.microsoft.com/en-us/answers/questions/1005525/sccm-2207-and-secondary-site-or-dp-role-create-new (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1001484/load-balance-between-distribution-point-servers (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 15
provenance_inferred: 1
provenance_ambiguous: 0
symptoms:
  - "CSendFileAction::SendContent failed; 0x8007052e"
  - "CContentDefinition::TotalFileSizes failed; 0x8007052e"
  - "event 4625"
tags: [sccm-core, troubleshooting]
status: draft
updated: 2026-07-25
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# SCCM Distribution Points and the Content Library

**Distribution points host the content files Configuration Manager deploys (applications, OS
images, software updates); the content library deduplicates that content, and boundary groups
determine which distribution point(s) a given client uses.**

## Body

### The content library

The content library is a single-instance store: before copying a content file to a site server or
distribution point, Configuration Manager checks whether it's already in the library, and if so
associates the existing file with the new application/package instead of copying it again. On a
distribution point you configure one or more disk drives for the library plus a priority per
drive — content fills the highest-priority drive until it drops below a configured minimum free
space, and these drive settings can only be set during DP install, not edited afterward (the
**Content Library Transfer** tool exists to move the library later).

### Installing distribution points

You install a new DP via the installation wizard, and can group DPs into **distribution point
groups** to simplify managing/distributing to many at once. Most settings are configurable either
at install or after via DP properties, but a few — like whether ConfigMgr installs IIS on the DP,
and drive-space settings — are install-time only.

### Boundary groups

When a client needs content, Configuration Manager returns the site systems (DPs or peer-cache
sources) associated with boundary groups that include the client's current network location. If
the client's boundary group has no available content source, it retries within that boundary
group until a configured fallback period elapses, then expands the search to neighbor boundary
groups (and, for on-demand content, may trigger a transfer to the originally-requested DP while
the client is still searching). OSD clients use the same boundary-group behavior for state
migration and content retrieval as software distribution does.

### Content distribution failures

A DP content-distribution failure shows in `distmgr.log` as `CContentDefinition::TotalFileSizes
failed; 0x8007052e` followed by `CSendFileAction::SendFiles failed; 0x8007052e` and
`CSendFileAction::SendContent failed; 0x8007052e`, typically paired with **Event ID 4625** (a
logon failure) recorded on the server hosting the content library — pointing at a permissions or
authentication problem reaching that share rather than a content-corruption issue.

## Community Q&A (upstream)

> Microsoft Q&A community threads — not Microsoft support statements. Weighted by
> answerer role below.

### Planning a new DP: prerequisites, the ~4,000-client guideline, and HA
When deciding whether to add another distribution point (as a site system role on a new
server, vs. a secondary site), a community answer lays out the concrete prerequisites
and planning rules:
- **Roles/features required before installing the DP role**: Remote Differential
  Compression; IIS Configuration (Application Development > ISAPI Extensions; Security >
  Windows Authentication); IIS 6 Management Compatibility (both IIS 6 Metabase
  Compatibility and IIS 6 WMI Compatibility); and the Visual C++ Redistributable.
- **To support PXE or multicast on that DP**: either enable the DP's own PXE responder
  *without* WDS, or install and configure the Windows Deployment Services role — these
  are the two supported paths, not a hard WDS requirement — and for a
  multicast-enabled DP, the SQL Server Native Client must be installed and current.
- Before running **Create Site System Server**, add the site server's
  computer account to the **Local Administrators** group on the new DP server.
- A **rough per-DP capacity guideline** offered from the answerer's own experience: each
  distribution point supports roughly up to **4,000 client connections**; past that,
  consider adding another DP directly rather than pushing more clients onto one. This is
  an informal community rule of thumb (1 upvote, no Microsoft/MVP confirmation), not a
  published Microsoft sizing spec — validate against your own DP's IIS/content-library
  load before treating it as a hard ceiling.
- **HA constraint**: on an active/passive high-availability site-server pair, the
  distribution point role cannot be installed on *both* nodes.

(community answer, thread:1005525)

### Measuring per-DP client load: `smsdpusage.exe`
To decide how to load-balance clients across distribution points, Configuration Manager
ships a built-in executable, **`smsdpusage.exe`** (default path
`C:\Program Files\Microsoft Configuration Manager\bin\i386\smsdpusage.exe`), that reads
the *previous day's* IIS logs on each DP, computes usage, and sends the resulting report
to the management point for processing into the site database — this is the mechanism
behind any "which clients use which DP" reporting (vendor-confirmed, thread:1001484).

## Contradictions / caveats

None noted in the ingested corpus. The ~4,000-client-per-DP figure above is a single
community member's informal guideline, not a documented Microsoft capacity limit — treat
it as a planning heuristic to verify locally, not a hard cutover threshold.

## See also
- [[sccm-overview]]
- [[sccm-site-hierarchy]]
- [[sccm-task-sequences-and-osd]]
- [[sccm-application-deployment]]
- [[sccm-client-health]]
- [[sccm-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[core-install-and-configure-distribution-points|Manage distribution points]]
- [[core-the-content-library|The content library]]
- [[core-boundary-groups-distribution-points|Boundary groups and distribution points]]
- [[sccm-troubleshoot-mem-configmgr-p0121-0160|Welcome — pages 121-160]]
<!-- crosslink:end -->
