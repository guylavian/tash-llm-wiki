---
title: SCCM Task Sequences and OS Deployment (OSD)
type: entity
domain: sccm
slug: sccm-task-sequences-and-osd
summary: The task-sequence-driven OS deployment process in Configuration Manager — the steps every OSD method shares, the deployment scenarios available, and how task sequence variables parameterize the process.
sources:
  - kb:osd-introduction-to-operating-system-deployment
  - kb:osd-task-sequence-variables
  - "web:https://learn.microsoft.com/en-us/answers/questions/1009077/tpm-check-readiness-for-task-sequence-new-operatin (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1003093/sccm-driver-tab-is-missing-from-boot-image-after-a (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1003044/sccm-pxe-boot-ip-helper (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1009275/sccm-pxe-boot-from-dhcp-not-working (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 15
provenance_inferred: 1
provenance_ambiguous: 0
tags: [sccm-osd, troubleshooting]
status: draft
updated: 2026-07-25
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# SCCM Task Sequences and OS Deployment (OSD)

**Operating system deployment in Configuration Manager is driven by a task sequence — an ordered
set of steps that, regardless of the deployment method chosen, must identify drivers, a boot
image, and an OS image, distribute them to a distribution point, and then deploy the task
sequence to a collection.**

## Body

### The OSD process

Every OSD method shares the same backbone: identify the Windows device drivers the boot/OS image
needs, identify the boot image to start the destination computer, capture or select an OS image,
**distribute** the boot image, OS image, and any referenced content to a distribution point,
build a **task sequence** with the steps to deploy that content, deploy the task sequence to a
collection of computers, and monitor the deployment.

### Deployment scenarios

Configuration Manager supports multiple OSD scenarios depending on the target hardware and
starting state, including: upgrading Windows to the latest version, refreshing an existing
computer with a new Windows version, and installing a new Windows version on a new (bare-metal)
computer — the right scenario is chosen based on environment and purpose, not a one-size-fits-all
task sequence.

### Task sequence variables

Task sequences are parameterized by a large, documented set of **task sequence variables**
(alphabetical reference; e.g. `_OSDDetectedWinDir`/`_OSDDetectedWinDrive`, populated when WinPE
scans the computer for a prior OS installation so the new install can reuse the same location).
Custom task sequence steps should read/write these documented variables instead of hardcoding
drive letters or paths (inferred — the variable reference's own stated purpose implies this is
the point of exposing them, though it is not phrased as an explicit "don't hardcode" rule in the
source).

## Community Q&A (upstream)

> Microsoft Q&A community threads — not Microsoft support statements. Weighted by
> answerer role below.

### The built-in "Check Readiness" step does NOT validate TPM readiness
The stock **Check Readiness** task sequence step only checks that "TPM 2.0 or above is
enabled" and "TPM 2.0 or above is activated" — it does **not** check the actual
`TpmReady` property (`Win32_TPM` WMI class), which is the bit BitLocker
Pre-Provisioning/Enable BitLocker actually needs. Result: a client can sail through
"Check Readiness" with a success status and then fail later at the BitLocker step, and
the operator sees a generic failure with no TPM-specific warning pointing at the real
cause. A Microsoft-employee moderator confirmed **there is nothing built-in for this** —
the fix has to be a custom step, either scripting a direct `Win32_TPM` WMI/PowerShell
query, or adopting the community front-end tool **UI++**
(`uiplusplus.configmgrftw.com`); as of this thread (ConfigMgr 2207-era, Sept–Oct 2022) no
built-in option existed (thread:1009077). One community tester additionally reported
`Get-Tpm` isn't available in WinPE (module not present) and that `TpmReady` isn't
returned by a `wmic ... Win32_Tpm get /value` query in either WinPE or the installed OS —
that specific testing detail is a single user's own experiment, not vendor-confirmed, so
treat it as a starting point to verify in your own boot image rather than a documented
limitation.

### After an ADK upgrade, boot images lose the Driver tab in the console
Root cause (vendor-confirmed): ConfigMgr compares the **installed ADK version** against
the **boot image's WinPE version**, and hides the modification tabs (including Driver)
when they don't match — a boot image can only be edited in the console when it exactly
matches the ADK version installed on the site server/SMS Provider. Fix: right-click the
boot image and select **"Reload this boot image with current Windows PE version from the
Windows ADK"**; the thread's reporter confirmed this restored the Driver tab
(thread:1003093).

### PXE boot: use IP helpers per PXE-enabled DP, not DHCP options 60/66/67
Two independent threads reach the same vendor-aligned recommendation: configure an **IP
helper-address entry for each PXE-enabled distribution point** (in addition to the
existing DHCP IP helper), rather than relying on DHCP options 66/67 (boot server/boot
file) — a syntax the first thread's reporter (1009275) was mid-migration away from after
hitting exactly the intermittent symptoms this causes (client downloads the PXE image and
then hangs on a black screen; boots into PXE and restarts; boots, applies the OS, then
errors). DHCP options are unreliable across router/OS/firmware combinations and don't
support multiple coexisting PXE responders cleanly; IP helpers let each PXE server see
every client boot request and self-select whether to respond, and — when serviced by
WDS — auto-determine UEFI vs. BIOS and hand out the matching boot initiator and WIM. One
answer gives the concrete router-side config: `ip helper-address <DHCP server IP>` / `ip
helper-address <PXE server IP>` / `ip forward-protocol udp 4011` (vendor-confirmed,
thread:1003044; corroborated by community answer, thread:1009275).

## Contradictions / caveats

None noted in the ingested corpus; deployment-method-specific detail (PXE, multicast, bootable
media, prestaged/stand-alone media) lives in the individual `osd-*` reference notes under
`reference/sccm/` and is a natural next INGEST pass.

## See also
- [[sccm-overview]]
- [[sccm-distribution-points]]
- [[sccm-application-deployment]]
- [[sccm-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[osd-introduction-to-operating-system-deployment|Introduction to operating system deployment]]
- [[osd-task-sequence-variables|Task sequence variable reference]]
<!-- crosslink:end -->
