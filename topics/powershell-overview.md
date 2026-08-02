---
title: PowerShell — Language, Shell, and Automation Platform Overview
type: topic
domain: powershell
slug: powershell-overview
summary: PowerShell is an object-pipeline shell and scripting language that ships in two lines — Windows PowerShell 5.1 (Windows-only, WinRM remoting) and cross-platform PowerShell 7+ (side-by-side with 5.1, adds SSH remoting) — extended by a huge module ecosystem of per-product cmdlet surfaces (Exchange, SharePoint, Teams/Skype for Business, ConfigMgr).
sources:
  - kb:powershell-powershell-scripting-powershell-7-6-p0081-0120
  - kb:powershell-powershell-scripting-powershell-7-6-p0121-0160
  - kb:powershell-powershell-scripting-powershell-7-6-p0161-0200
  - kb:odps-connect-exchangeonline
  - kb:spps-connect-sposervice
provenance_extracted: 5
provenance_inferred: 3
provenance_ambiguous: 0
tags: [ps-language, ps-modules, concept]
status: draft
updated: 2026-07-23
graph_community: "PowerShell — Implementation Review (Evaluation-Lens MOC)"
---

# PowerShell — Language, Shell, and Automation Platform Overview

**PowerShell is an object-pipeline command shell and scripting language: cmdlets exchange
typed .NET objects rather than text, and the same engine backs both interactive administration
and unattended automation.**

## Body

### Two product lines, side by side

**Windows PowerShell 5.1** and **PowerShell 7** are two different products that install
side-by-side rather than one replacing the other — PowerShell 6 ("PowerShell Core") is no
longer supported, and PowerShell 7 is the actively developed cross-platform line
(`reference/powershell/powershell-powershell-scripting-powershell-7-6-p0081-0120.md:330-337`).
Default execution policy differs by OS/edition: `RemoteSigned` on Windows Server 2016/2019/2022,
`Restricted` on Windows 10/11 client — see [[powershell-execution-policy]] for the full policy
model (it is a safety feature, not a security boundary).

### The object pipeline

Cmdlets pass live .NET objects between each other, not formatted text — piping to `Get-Member`
reveals the exact `TypeName` flowing through, and a downstream parameter binds a piped object
either **ByValue** (type match, tried first) or **ByPropertyName**. "Filter left" — filtering as early
in a pipeline as possible with a cmdlet's own parameters rather than a downstream
`Where-Object` — is the standing performance discipline. See [[powershell-pipeline-and-objects]]
for the mechanics.

### Writing and packaging logic

A function becomes an "advanced function" (gaining the common parameters and, with
`SupportsShouldProcess`, `-WhatIf`/`-Confirm`) the moment its `param()` block carries
`[CmdletBinding()]` — see [[powershell-functions]]. Functions ship for reuse as **modules**,
which PowerShell 3+ autoloads from `$env:PSModulePath` when the containing folder's name
matches the `.psm1` base name, and which should carry a `.psd1` manifest — see
[[powershell-modules]]. `try`/`catch`/`finally` only intercepts **terminating** errors, so a cmdlet
call inside `try` typically needs `-ErrorAction Stop` before `catch` will ever run — see
[[powershell-error-handling]]. The `class` keyword (reserved since PowerShell 5.0, alongside
`using`) defines real .NET types inline, including static methods convertible to a delegate — see
[[powershell-classes]] (this corpus's coverage of classes is thin; see that page's caveats).
Sessions can be customized at startup with a **profile script** (`$PROFILE`), and non-filesystem
data — the registry, certificates, environment variables, even third-party stores like Active
Directory — is exposed the same way the filesystem is, through **PSProviders/PSDrives** — see
[[powershell-profiles-and-providers]].

### Reaching other machines

**PowerShell remoting** runs commands on remote computers over one of two transports:
**WS-Management (WinRM)**, the Windows PowerShell 5.1 default, or **SSH-based remoting**
(PowerShell 6+, `-HostName`/`-UserName`/`-KeyFilePath`), added specifically to reach
non-Windows and mixed-OS targets. See [[powershell-remoting]].

### The module ecosystem: per-product cmdlet surfaces

Beyond the core language, PowerShell's module system is how huge per-product admin surfaces
ship: Exchange Online / Exchange Server (`Connect-ExchangeOnline`, `Connect-IPPSSession` for
Security & Compliance / Purview — see [[exchange-online-powershell-cmdlets]]), SharePoint
Online / Server (`Connect-SPOService` and the `Get`/`New`/`Set-SPO*` cmdlets — see
[[sharepoint-powershell-cmdlets]]), and — per this domain's `ps-modules` area (`_meta/taxonomy.md`)
— Teams/Skype for Business and ConfigMgr, whose cmdlet references also live in
`reference/powershell/` alongside the Exchange and SharePoint ones (inferred: this page only
synthesizes the Exchange and SharePoint surfaces so far; the Teams/Skype for Business and
ConfigMgr cmdlet references are ingested into the reference tier but not yet distilled into their
own entity pages). Across every one of these product modules, the recurring theme for
unattended/automation scenarios is the same: prefer certificate-based (app-only) or
managed-identity authentication over a stored interactive credential (inferred — the pattern
repeats across Exchange Online, Security & Compliance, and SharePoint Online connection
cmdlets).

## Contradictions / caveats
This is a **corpus-backed** domain: `reference/powershell/` holds the harvested PowerShell 7.6
scripting PDF (chunked, `powershell-powershell-scripting-powershell-7-6-p*` stems) plus the
Exchange (`odps-*`) and SharePoint (`spps-*`) cmdlet-reference sets — all tagged `domain:
powershell` regardless of which product they document, per `_meta/taxonomy.md`'s `ps-modules`
area ("module system + per-product cmdlet references (Exchange, SharePoint, Teams,
ConfigMgr)"). `tiers-covered: [conceptual]` only — no support-kb/break-fix tier is ingested yet,
so a break-fix question against this domain should carry the H1 out-of-coverage banner (see
[[powershell-implementation-review]]).

## See also
- [[powershell-implementation-review]]
- [[powershell-pipeline-and-objects]]
- [[powershell-functions]]
- [[powershell-modules]]
- [[powershell-error-handling]]
- [[powershell-classes]]
- [[powershell-remoting]]
- [[powershell-execution-policy]]
- [[powershell-profiles-and-providers]]
- [[exchange-online-powershell-cmdlets]]
- [[sharepoint-powershell-cmdlets]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[powershell-powershell-scripting-powershell-7-6-p0081-0120|How to use this documentation — pages 81-120]]
- [[powershell-powershell-scripting-powershell-7-6-p0121-0160|How to use this documentation — pages 121-160]]
- [[powershell-powershell-scripting-powershell-7-6-p0161-0200|How to use this documentation — pages 161-200]]
- [[odps-connect-exchangeonline|Connect-ExchangeOnline]]
- [[spps-connect-sposervice|Connect-SPOService]]
<!-- crosslink:end -->
