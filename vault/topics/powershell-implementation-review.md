---
title: PowerShell — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: powershell
slug: powershell-implementation-review
summary: The evaluation lens for the powershell brain — a rule → anti-pattern → symptom checklist across pipeline discipline, functions/modules, error handling, execution policy/security, remoting, and the Exchange/SharePoint cmdlet surfaces, plus a symptom → likely-cause reverse index.
sources:
  - kb:powershell-powershell-scripting-powershell-7-6-p0081-0120
  - kb:powershell-powershell-scripting-powershell-7-6-p0121-0160
  - kb:powershell-powershell-scripting-powershell-7-6-p0201-0240
  - kb:powershell-powershell-scripting-powershell-7-6-p0641-0680
  - kb:powershell-powershell-scripting-powershell-7-6-p0761-0800
  - kb:odps-connect-exchangeonline
  - kb:odps-app-only-auth-powershell-v2
  - kb:odps-control-remote-powershell-access-to-exchange-servers
  - kb:spps-connect-sharepoint-online
provenance_extracted: 0
provenance_inferred: 13
provenance_ambiguous: 0
tags: [ps-language, ps-modules, ps-remoting, troubleshooting, security]
status: draft
updated: 2026-07-23
graph_community: "PowerShell — Implementation Review (Evaluation-Lens MOC)"
---

# PowerShell — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `powershell` domain.** It indexes the domain's
entity pages into a forward checklist (rule → anti-pattern → symptom) and a reverse index
(symptom → likely cause), mirroring [[active-directory-implementation-review]]. Every row here
is synthesis (inferred) over the entity pages' extracted claims — read the linked entity for the
sourced quote.

---

## How to use this page

Read each row left to right: **Rule** states what a healthy PowerShell script/environment does;
**Anti-pattern** states the common mistake; **Symptom** names the observable fault it produces;
**Page** links the entity with the sourced detail. To diagnose from an observed error, jump to the
[Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist

### Pipeline and objects

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Filter as early in the pipeline as possible ("filter left") using a cmdlet's own filter parameters | Retrieving the full unfiltered result set and piping to `Where-Object` downstream | Scripts that are slow only at scale (e.g. thousands of objects), not in small tests | [[powershell-pipeline-and-objects]] |
| Put `Where-Object` before `Select-Object` when chaining both | `Select-Object` trims properties first, then `Where-Object` tries to filter on a property that's no longer present | Filter silently returns nothing, or errors referencing a missing property | [[powershell-pipeline-and-objects]] |

### Functions and modules

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Give functions a unique `Verb-Noun` name (e.g. prefix the noun with your initials) and add `[CmdletBinding()]` | Reusing a common name with no prefix; omitting `[CmdletBinding()]` | Function shadows/collides with an existing cmdlet or function already in scope; no `-Verbose`/`-Debug`/common parameters | [[powershell-functions]] |
| Ship a script module in a `$env:PSModulePath` folder whose name matches the `.psm1` base name, with a `.psd1` manifest | Module folder name doesn't match the `.psm1` file; no manifest ever created | `CommandNotFoundException` / "is not recognized as the name of a cmdlet" when autoloading fails; `Get-Module` reports version `0.0` | [[powershell-modules]] |

### Error handling

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use `try`/`catch` with `-ErrorAction Stop` on the specific call whose errors must be caught | Wrapping a cmdlet call in `try`/`catch` without `-ErrorAction Stop`, relying on the cmdlet's default (non-terminating) behavior | `catch` block never runs; the "handled" error still surfaces as an unhandled exception | [[powershell-error-handling]] |

### Execution policy and security

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Treat execution policy as a safety net only; pair it with AppLocker/App Control for real enforcement against a determined attacker | Assuming `Set-ExecutionPolicy` alone stops malicious script execution | Microsoft's own servicing criteria lists Execution Policy as defense-in-depth, not a security boundary — a determined user bypasses it | [[powershell-execution-policy]] |
| Set the execution policy at the correct scope — elevate for `LocalMachine`, or use `-Scope CurrentUser` without elevation | Running `Set-ExecutionPolicy` without elevation and without `-Scope CurrentUser` | `Access to the registry key '...' is denied` / `PermissionDenied: (:) [Set-ExecutionPolicy]` | [[powershell-execution-policy]] |
| Enable scripts to run at all before assuming a script "just doesn't work" | Running a `.ps1` under the client-OS `Restricted` default without changing the policy | `running scripts is disabled on this system` / `PSSecurityException` / `UnauthorizedAccess` | [[powershell-execution-policy]] |

### Remoting

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use SSH-based remoting (`-HostName`/`-UserName`/`-KeyFilePath`) for non-Windows or mixed-OS targets; WinRM/WS-Management for Windows-only fleets | Assuming `Enter-PSSession`/`Invoke-Command` always uses WinRM regardless of the target OS | Remoting to a Linux/macOS target fails without the SSH parameter set; WinRM-only targets reject SSH-style connections | [[powershell-remoting]] |

### Exchange Online / Security & Compliance PowerShell

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use certificate-based (app-only) authentication or managed identity for unattended scripts | Storing a `Get-Credential`/`ConvertTo-SecureString` password locally "for automation" | No automated *and* secure local-certificate connection exists — password material ends up on disk or in the script | [[exchange-online-powershell-cmdlets]] |
| Scope any `Set-User -RemotePowerShellEnabled $false` change to exclude admin/service/monitoring accounts | Running `Get-User \| Set-User -RemotePowerShellEnabled $false` organization-wide | Administrators lock themselves out of remote PowerShell; recovery requires the discouraged `Add-PSSnapIn` workaround | [[exchange-online-powershell-cmdlets]] |

### SharePoint Online PowerShell

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use `-ModernAuth`/`-AuthenticationUrl` (or certificate/managed-identity auth) for MFA-enabled admin accounts | `Connect-SPOService` called with only `-Credential` against an MFA-enabled account | `Could not connect to SharePoint Online` | [[sharepoint-powershell-cmdlets]] |
| Uninstall the SharePoint Client Components SDK if the SharePoint Online Management Shell module must load in the same session | Both the SDK and the Management Shell module installed on the same computer | SharePoint Online Management Shell module fails to load | [[sharepoint-powershell-cmdlets]] |

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `running scripts is disabled on this system` / `PSSecurityException` / `UnauthorizedAccess` | Execution policy at its default (`Restricted` on client OS) and never changed | [[powershell-execution-policy]] |
| `Access to the registry key '...' is denied` / `PermissionDenied: (:) [Set-ExecutionPolicy]` | `Set-ExecutionPolicy` for `LocalMachine` run without an elevated prompt | [[powershell-execution-policy]] |
| `CommandNotFoundException` / "is not recognized as the name of a cmdlet, function, script file" | Function/module never imported, or module autoloading failed (folder name ≠ `.psm1` base name) | [[powershell-modules]], [[powershell-functions]] |
| `Get-Module` reports version `0.0` | Module has no `.psd1` manifest | [[powershell-modules]] |
| `try`/`catch` doesn't intercept a failing cmdlet call | Missing `-ErrorAction Stop` — the error is non-terminating by default | [[powershell-error-handling]] |
| `Could not connect to SharePoint Online` | `Connect-SPOService` used bare `-Credential` against an MFA-enabled account instead of `-ModernAuth`/`-AuthenticationUrl` | [[sharepoint-powershell-cmdlets]] |
| Admins/service accounts locked out of remote PowerShell fleet-wide | Blanket `Get-User \| Set-User -RemotePowerShellEnabled $false` with no exclusion list | [[exchange-online-powershell-cmdlets]] |
| `AppLocker` Deny rule bypassed by `Set-ExecutionPolicy -ExecutionPolicy Bypass` (pre-7.2) | Execution policy treated as if it were a security boundary rather than defense-in-depth | [[powershell-execution-policy]] |
| Local certificate password stored in a script "for automation" | No automated-and-secure local-certificate connection path exists for Exchange Online CBA | [[exchange-online-powershell-cmdlets]] |
| `Enter-PSSession`/`Invoke-Command` fails against a non-Windows host | WinRM-only remoting attempted against a target that needs the SSH parameter set (`-HostName`/`-UserName`/`-KeyFilePath`) | [[powershell-remoting]] |

---

## Domain map — pages by area

### Language
- [[powershell-overview]] — spine: object pipeline, two product lines, module ecosystem
- [[powershell-pipeline-and-objects]] — object binding, ByValue/ByPropertyName, filter left
- [[powershell-functions]] — CmdletBinding, common parameters, SupportsShouldProcess
- [[powershell-modules]] — autoloading, `$env:PSModulePath`, manifests
- [[powershell-error-handling]] — try/catch/finally, terminating vs. non-terminating errors
- [[powershell-classes]] — the `class` keyword, static methods, delegate conversion
- [[powershell-profiles-and-providers]] — `$PROFILE`, PSProviders/PSDrives

### Remoting and security
- [[powershell-remoting]] — WS-Management (WinRM) vs. SSH-based remoting
- [[powershell-execution-policy]] — safety feature vs. security boundary, defaults, errors

### Per-product cmdlet surfaces
- [[exchange-online-powershell-cmdlets]] — Connect-ExchangeOnline, Connect-IPPSSession, CBA, managed identity, on-prem RemotePowerShellEnabled
- [[sharepoint-powershell-cmdlets]] — Connect-SPOService, modern auth/MFA, site-collection cmdlets

## See also
- [[active-directory-implementation-review]] — sibling MOC in a different domain, same shape
- [[powershell-overview]] — domain primer

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[powershell-powershell-scripting-powershell-7-6-p0081-0120|How to use this documentation — pages 81-120]]
- [[powershell-powershell-scripting-powershell-7-6-p0121-0160|How to use this documentation — pages 121-160]]
- [[powershell-powershell-scripting-powershell-7-6-p0201-0240|How to use this documentation — pages 201-240]]
- [[powershell-powershell-scripting-powershell-7-6-p0641-0680|How to use this documentation — pages 641-680]]
- [[powershell-powershell-scripting-powershell-7-6-p0761-0800|How to use this documentation — pages 761-800]]
- [[odps-connect-exchangeonline|Connect-ExchangeOnline]]
- [[odps-app-only-auth-powershell-v2|App-only authentication in Exchange Online PowerShell and Security & Compliance PowerShell]]
- [[odps-control-remote-powershell-access-to-exchange-servers|Control remote PowerShell access to Exchange servers]]
- [[spps-connect-sharepoint-online|Get started with the SharePoint Online Management Shell]]
<!-- crosslink:end -->
