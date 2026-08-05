---
title: Why does the ConfigMgr console/client fail to connect remotely with "Access is denied" (0x80070005) after installing Windows updates?
type: question
domain: sccm
slug: sccm-remote-console-access-denied-dcom-hardening
summary: Remote console/remote-tools/remote-content-distribution connections that work locally but fail remotely with 0x80070005 (Access is Denied) or 0x800706ba (RPC server is unavailable) after the June 2022 Windows security updates are caused by DCOM authentication-level hardening (CVE-2021-26414) being active on one side of the connection but not the other; the fix is patching both ends to the same level and upgrading to ConfigMgr 2203+, with a registry key as a time-limited stopgap only until March 14, 2023.
sources:
  - kb:sccm-troubleshoot-mem-configmgr-p0081-0120
provenance_extracted: 8
provenance_inferred: 1
provenance_ambiguous: 0
question_tier: support-kb
tags: [security, troubleshooting, sccm-core]
status: draft
updated: 2026-07-23
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# Why does the ConfigMgr console/client fail to connect remotely with "Access is denied" after installing Windows updates?

**A local connection to the SMS Provider succeeds under any account, but the *same* account fails
remotely with `0x80070005` (Access is Denied) or `0x800706ba` (RPC server is unavailable) — for
the console, for remote client tools (Support Center, Policy Spy), and for content distribution to
a remote distribution point — because the June 2022 Windows security updates enabled DCOM
activation-authentication hardening (CVE-2021-26414) by default, and the two ends of the DCOM
connection are not patched to a matching hardening level (extracted,
`sccm-troubleshoot-mem-configmgr-p0081-0120.md:333-352,361-363`).**

## Body

### The observed signal

The note names the exact symptom pattern first: **local-vs-remote asymmetry.** After installing
the June 2022 Windows security updates or later, an admin sees one of: the console failing to
access the SMS Provider remotely under *any* user account (while the same credential works
locally); the same local-succeeds/remote-fails pattern for remote client tools like Support Center
or Policy Spy; or content failing to distribute to a remote distribution point
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:339-352`). The paired error codes are
`0x80070005` ("Access is Denied") and `0x800706ba` ("The RPC server is unavailable")
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:359-363`), and a concrete log excerpt is given for
the console case — `SmsAdminUI.log`:

```
Insufficient privilege to connect, error: 'Access is denied. (Exception from HRESULT:
0x80070005 (E_ACCESSDENIED))' System.UnauthorizedAccessException
```
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:367-372`)

### Root cause: DCOM hardening rollout, not a permissions bug

Configuration Manager uses DCOM at multiple points internally
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:333-334`). In 2021 Microsoft disclosed
**CVE-2021-26414** (DCOM Server Security Feature Bypass) and rolled out a **phased** hardening of
DCOM activation authentication, controlled by the `RequireIntegrityActivationAuthenticationLevel`
registry key, on this timeline
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:393-416`):

| Update release | Behavior |
|---|---|
| June 8, 2021 | Hardening available but **disabled by default** (enable via registry key) |
| June 14, 2022 | Hardening **enabled by default** (disable via registry key still possible) |
| March 14, 2023 | Hardening **enabled with no way to disable it** |

So the failure this question describes is exactly what happens when one side of a DCOM
connection (post-June-2022 patch level, hardening on) talks to a side that is unpatched or
configured differently — the levels don't match, and DCOM refuses the activation
(inferred — the note gives the timeline and the fix but doesn't restate "mismatch" as one
sentence; this is the direct reading of "install the update on **both** computers... to ensure the
**same level** of DCOM hardening").

### The actual fix (not just "disable the security control")

The documented resolution is **not** to leave hardening permanently disabled. It is: install the
latest Windows cumulative update on **both** computers in the connection — the one initiating it
(remote console or site server) and the one receiving it (SMS Provider, distribution point, or
remote client) — and upgrade to **Configuration Manager 2203 or later**
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:384-391`). To confirm this is really the cause
before you patch, check for time-correlated Event IDs in the System log (requires at least the
October 2021 CU installed to log them): server-side **Event ID 10036**, client-side **Event ID
10037 / 10038**, all naming the required minimum level `RPC_C_AUTHN_LEVEL_PKT_INTEGRITY`
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:421-463`).

The registry override — `HKLM\SOFTWARE\Microsoft\Ole\AppCompat!RequireIntegrityActivationAuthenticationLevel`
= `0` (DWORD) to disable, `1` to enable — is explicitly framed as **temporary**: it is ignored
entirely starting March 14, 2023, so an environment relying on it must resolve the underlying
compatibility gap (patch levels, or Configuration Manager version) before that date
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:465-479`).

## Contradictions / caveats

If the issue persists after patching both ends and confirming matching hardening state, the note
directs escalation to Microsoft Support rather than offering a further workaround
(`sccm-troubleshoot-mem-configmgr-p0081-0120.md:481`) — this page does not have a next step beyond
that. `tiers-covered: [conceptual, support-kb]` for `sccm` — this is a `support-kb` question and
that tier is covered, so no out-of-coverage banner is required.

## See also
- [[sccm-client-health]]
- [[sccm-admin-service]]
- [[sccm-distribution-points]]
- [[sccm-implementation-review]]

## References

**RH ground-truth:**
- `kb:sccm-troubleshoot-mem-configmgr-p0081-0120` — Configuration Manager troubleshooting, "Welcome — pages 81-120" (DCOM hardening / CVE-2021-26414 symptoms, cause, timeline, and fix)

**Wiki pages:**
- [[sccm-client-health]] — DCOM hardening as one of the three recurring client/console break-fix causes
- [[sccm-implementation-review]] — reverse index entries for `0x80070005`, `0x800706ba`, and Event IDs 10036–10038

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[sccm-troubleshoot-mem-configmgr-p0081-0120|Welcome — pages 81-120]]
<!-- crosslink:end -->
