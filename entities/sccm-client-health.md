---
title: SCCM Client Installation and Health
type: entity
domain: sccm
slug: sccm-client-health
summary: How Configuration Manager clients get installed (client push and alternatives), how the client keeps itself healthy, and the three most common break-fix causes for client install/connection failures — DCOM hardening mismatch, antivirus interference, and local database corruption.
sources:
  - kb:core-client-installation-methods
  - kb:core-client-health-checks
  - kb:core-client-health-dashboard
  - kb:sccm-troubleshoot-mem-configmgr-p0081-0120
  - kb:sccm-troubleshoot-mem-configmgr-p0281-0320
provenance_extracted: 12
provenance_inferred: 1
provenance_ambiguous: 0
symptoms:
  - "0x80070005.*Access is Denied"
  - "0x800706ba.*RPC server is unavailable"
  - "Database verification failed with result: 0x80004005"
  - "client push"
  - "10036|10037|10038"
tags: [sccm-core, security, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# SCCM Client Installation and Health

**The Configuration Manager client can be installed by several methods — client push is the most
automatic — and is kept healthy by scheduled self-checks; most real-world client-health tickets
trace back to DCOM-hardening version mismatch, antivirus interference, or a corrupted local
client database.**

## Body

### Installation methods

**Client push** installs to a single computer, a collection, or query results, and can
auto-install on every discovered computer. It requires a **client push installation account**
with administrative rights on the target and Windows Firewall exceptions on the client; it
cannot install to workgroup computers or computers ConfigMgr hasn't discovered, and once started
it can't be cancelled — Configuration Manager retries failures for up to **seven days**. Other
methods (software update point-based, GPO, logon script, manual, image-embedded via OSD) trade
off automation for less administrative overhead per client.

### Client health checks

The client runs scheduled checks and remediations: verifying it was installed correctly
(otherwise troubleshoot via `ccmsetup.log` and often just reinstall), verifying prerequisites
listed in `ccmsetup.xml` (default `C:\Windows\ccmsetup\ccmsetup.xml`) are present, and verifying
more than 1% free disk space remains on the system drive. The **client health dashboard**
(Monitoring workspace > Client status) surfaces online/recently-active clients, scenario health,
and common errors, filterable by OS/client version — it requires the **Read Client Status
Settings** permission on the Site object.

### DCOM hardening — remote console / client / DP connection failures

Windows security updates addressing **CVE-2021-26414** (DCOM Server Security Feature Bypass)
progressively hardened DCOM activation-authentication requirements: hardening was **available
but disabled** starting June 8, 2021; **enabled by default (disableable via registry)** starting
June 14, 2022; and **enabled with no ability to disable** starting March 14, 2023. If the site
server, SMS Provider, distribution point, or a client are not all patched to the same hardening
level, remote console connections, remote client tools, and remote content distribution can fail
with `0x80070005` (Access is Denied) or `0x800706ba` (RPC server is unavailable) — e.g.
`SmsAdminUI.log` logging `Insufficient privilege to connect, error: 'Access is denied.
(Exception from HRESULT: 0x80070005 (E_ACCESSDENIED))'`. Confirming events (need at least the
October 2021 CU installed to log them): server-side **Event ID 10036**, client-side **Event ID
10037 / 10038** — all naming the required minimum level `RPC_C_AUTHN_LEVEL_PKT_INTEGRITY`. Fix:
install the latest cumulative update on both ends and upgrade to Configuration Manager 2203+; the
registry override `HKLM\SOFTWARE\Microsoft\Ole\AppCompat!RequireIntegrityActivationAuthenticationLevel`
(DWORD `0`=disable / `1`=enable) is only a stopgap and is ignored entirely after March 14, 2023.

### Antivirus interference

Real-time antivirus protection without ConfigMgr exclusions is a recurring cause of a cluster of
symptoms: `0x80070005` in `SiteComp.log`/`Distmgr.log`/`hman.log`, client push installs that never
complete, stale/missing client inventory, inbox backlogs, Software Center failing to populate or
start (`CCMRepair.log`: `Database verification failed with result: 0x80004005 but DB:
C:\Windows\CCM\filename.sdf could be opened, skipping DB repair`), and deployed software that
won't install. Recommended exclusions cover the ConfigMgr install folder (`Inboxes`, `Logs`,
`EasySetupPayload`), the content library (`SCCMContentLib`), MP `OUTBOXES`, and — on clients —
`*.sdf` files, `ServiceData`, `ScriptStore`, `CCMCache`, `CCMSetup`, and the client `Logs` folder;
outgoing-file scanning should be disabled on management points.

## Contradictions / caveats

The DCOM-hardening and antivirus causes both surface overlapping `0x80070005` — distinguishing
them requires checking whether the error correlates with a *specific remote/DCOM* operation
(console, remote tools, remote DP) vs. a *local* client operation (push install completing,
Software Center) (inferred — a triage heuristic assembled from reading both troubleshoot chunks
side by side, not stated as a single rule in either source).

## See also
- [[sccm-overview]]
- [[sccm-site-hierarchy]]
- [[sccm-admin-service]]
- [[sccm-collections]]
- [[sccm-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[core-client-installation-methods|Client installation methods]]
- [[core-client-health-checks|Client health checks]]
- [[core-client-health-dashboard|Client health dashboard]]
- [[sccm-troubleshoot-mem-configmgr-p0081-0120|Welcome — pages 81-120]]
- [[sccm-troubleshoot-mem-configmgr-p0281-0320|Welcome — pages 281-320]]
<!-- crosslink:end -->
