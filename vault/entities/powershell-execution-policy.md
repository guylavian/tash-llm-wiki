---
title: PowerShell Execution Policy
type: entity
domain: powershell
slug: powershell-execution-policy
summary: PowerShell's execution policy controls whether scripts are allowed to run — it is a safety feature against accidental script execution, explicitly not a security boundary, and Microsoft classifies it as a defense-in-depth mitigation that AppLocker/App Control rules take precedence over.
sources:
  - kb:powershell-powershell-scripting-powershell-7-6-p0081-0120
  - kb:powershell-powershell-scripting-powershell-7-6-p0761-0800
tags: [security, ps-language, troubleshooting]
provenance_extracted: 8
provenance_inferred: 0
provenance_ambiguous: 0
symptoms:
  - "running scripts is disabled on this system"
  - "PSSecurityException"
  - "Access to the registry key.*is denied"
  - "PermissionDenied.*Set-ExecutionPolicy"
status: draft
updated: 2026-07-23
graph_community: "PowerShell — Implementation Review (Evaluation-Lens MOC)"
---

# PowerShell Execution Policy

**Execution policy is a safety feature that controls whether PowerShell will run script files —
by design it is not a security boundary, and a determined user can bypass it; Microsoft
classifies it as a defense-in-depth mitigation, not a security-boundary feature.**

## Body

### What it controls, and what it doesn't

"The execution policy in PowerShell is a safety feature designed to help prevent the
unintentional execution of malicious scripts. However, it's not a security boundary because it
can't stop determined users from deliberately running scripts."
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:339-344`).
It can be set per local computer, per current user, per PowerShell session, or via Group Policy
for computers/users, and it **only affects scripts** — any command still runs fine when typed
interactively regardless of the policy
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:345-368`).

### Defaults and errors

| OS | Default execution policy |
|---|---|
| Windows Server 2022 / 2019 / 2016 | `RemoteSigned` |
| Windows 11 / Windows 10 | `Restricted` |

(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:355-367`).
Running a `.ps1` script under `Restricted` fails with:

```
.\Get-TimeService.ps1 : File C:\tmp\Get-TimeService.ps1 cannot be loaded because running
scripts is disabled on this system. ...
+ CategoryInfo          : SecurityError: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
```

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` fixes it for the machine (requires an
elevated/administrator PowerShell — `LocalMachine` is the default scope), or
`-Scope CurrentUser` fixes it for the current user without elevation. Running
`Set-ExecutionPolicy` without elevation and without `-Scope CurrentUser` fails with:

```
Set-ExecutionPolicy : Access to the registry key 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
PowerShell\1\ShellIds\Microsoft.PowerShell' is denied. ...
+ CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], UnauthorizedAccessException
```

(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:395-499`).
`RemoteSigned` (rather than `AllSigned`/`Unrestricted`/`Bypass`) is the recommended everyday
policy unless you sign your own scripts — it blocks unsigned scripts *downloaded* from the
internet while still allowing locally-authored ones to run
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:442-444`).

### Security-boundary classification (defense-in-depth vs. security boundary)

Microsoft's own Security Servicing Criteria splits PowerShell's protections into two tiers:
**security boundary** features (fixed as reported vulnerabilities) — "System Lockdown with App
Control for Business" and "Constrained language mode with App Control for Business" — versus
**defense-in-depth** features, which "may have by-design limitations that prevent them from
fully mitigating a threat": "Constrained language mode with AppLocker …", "System Lockdown
with AppLocker", and **"Execution Policy"** itself
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0761-0800.md:1130-1152`).
Concretely, PowerShell 7.2 changed AppLocker Deny-only rule enforcement to take precedence
over `Set-ExecutionPolicy -ExecutionPolicy Bypass`
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0761-0800.md:1245-1252`).

## Contradictions / caveats
Execution policy "only applies to the Windows platform" per the security-features summary
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0761-0800.md:990-991`);
elsewhere the corpus notes `Get-ExecutionPolicy` returns `Unrestricted` on Linux/macOS
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0721-0760.md:245`) —
consistent readings of the same fact, not a real contradiction: execution policy is a no-op
outside Windows.

## See also
- [[powershell-overview]]
- [[powershell-error-handling]]
- [[powershell-remoting]]
- [[powershell-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[powershell-powershell-scripting-powershell-7-6-p0081-0120|How to use this documentation — pages 81-120]]
- [[powershell-powershell-scripting-powershell-7-6-p0761-0800|How to use this documentation — pages 761-800]]
<!-- crosslink:end -->
