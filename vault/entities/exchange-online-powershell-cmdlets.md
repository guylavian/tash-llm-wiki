---
title: Exchange Online / Exchange Server PowerShell Cmdlet Surface
type: entity
domain: powershell
slug: exchange-online-powershell-cmdlets
summary: Connect-ExchangeOnline (mail/admin cmdlets) and Connect-IPPSSession (Security & Compliance / Purview cmdlets) are the two entry points into the Exchange Online PowerShell module; unattended scripts should authenticate with certificate-based (app-only) auth or managed identity rather than a stored credential, and on-premises Exchange gates remote PowerShell per-user via RemotePowerShellEnabled.
sources:
  - kb:odps-connect-exchangeonline
  - kb:odps-connect-to-exchange-online-powershell
  - kb:odps-connect-ippssession
  - kb:odps-app-only-auth-powershell-v2
  - kb:odps-control-remote-powershell-access-to-exchange-servers
tags: [ps-modules, security]
provenance_extracted: 9
provenance_inferred: 1
provenance_ambiguous: 0
status: draft
updated: 2026-07-23
graph_community: "PowerShell — Implementation Review (Evaluation-Lens MOC)"
---

# Exchange Online / Exchange Server PowerShell Cmdlet Surface

**`Connect-ExchangeOnline` (mail/admin cmdlets) and `Connect-IPPSSession` (Security &
Compliance / Purview cmdlets) are the two Exchange Online PowerShell module entry points;
on-premises Exchange instead gates remote PowerShell access per mailbox/user account.**

## Body

### Connecting interactively vs. unattended

`Connect-ExchangeOnline` "creates a PowerShell connection to your Exchange Online
organization" using modern authentication, with or without MFA
(`reference/powershell/odps-connect-exchangeonline.md:14-19,69-70`). Interactive connection
is as simple as `Connect-ExchangeOnline -UserPrincipalName chris@contoso.com`
(`reference/powershell/odps-connect-exchangeonline.md:76-81`). For **unattended scripts**,
the module supports certificate-based authentication (CBA, `-AppId`/`-CertificateThumbprint` or
`-AppId`/`-Certificate`), device-code login (`-Device`), or **managed identity**
(`-ManagedIdentity`, restricted to Azure Automation runbooks, Azure VMs/VMSS, and Azure
Functions, and requiring `-Organization`)
(`reference/powershell/odps-connect-exchangeonline.md:83-104,649-666`). The legacy
`-UseRPSSession` remote-PowerShell mode is **deprecated as of module 3.9.2** — REST API
connections replaced it in Exchange Online PowerShell in October 2023
(`reference/powershell/odps-connect-exchangeonline.md:922-926`).

To reach **Security & Compliance PowerShell** (Purview) instead of mail/admin cmdlets, use
`Connect-IPPSSession`, not `Connect-ExchangeOnline`
(`reference/powershell/odps-connect-exchangeonline.md:21`,
`reference/powershell/odps-connect-ippssession.md:16-19`).

### Certificate-based (app-only) authentication

CBA fetches an app-only OAuth token using the application ID, tenant ID, and a certificate
thumbprint via the Active Directory Authentication Library; the Microsoft Entra app's assigned
directory role is returned in the token and drives the session's RBAC
(`reference/powershell/odps-app-only-auth-powershell-v2.md:58-61`). Three ways to supply the
certificate: an installed thumbprint, an in-memory certificate object (e.g. fetched from Azure Key
Vault at runtime), or a local `.pfx` file with `-CertificatePassword`. The docs explicitly call out
that the local-file option has **no fully automated *and* secure story**: storing the password
with `ConvertTo-SecureString` defeats the point of certificate auth for automation, and
prompting with `Get-Credential` isn't viable unattended either — "there's really no automated
*and* secure way to connect using a local certificate"
(`reference/powershell/odps-connect-exchangeonline.md:401-415`,
`reference/powershell/odps-app-only-auth-powershell-v2.md:88-126`). CNG certificates (the
Windows default in modern versions) are **not supported** for this — a certificate from a CSP
key provider is required
(`reference/powershell/odps-app-only-auth-powershell-v2.md:154-163`).

### On-premises: gating remote PowerShell access

On-premises Exchange controls remote PowerShell per user via the `RemotePowerShellEnabled`
property on `Get-User`/`Set-User`, defaulting to enabled for every account. The docs carry an
explicit warning against a blanket
`Get-User | Set-User -RemotePowerShellEnabled $false` — it can lock out admin accounts,
service accounts, or health-monitoring mailboxes along with everyone else; recovery from a
full lockout requires the "otherwise highly discouraged" `Add-PSSnapIn
Microsoft.Exchange.Management.PowerShell.SnapIn` workaround
(`reference/powershell/odps-control-remote-powershell-access-to-exchange-servers.md:25-30`).

## Contradictions / caveats
The `-UseRPSSession` remote-PowerShell connection mode is deprecated in the cloud module
(3.9.2+, October 2023) but the same remote-PowerShell model is still how **on-premises**
Exchange is managed — the two `odps-*` documents describe different products (cloud vs.
on-prem) that happen to share a cmdlet-naming convention (inferred: the corpus doesn't state
this contrast directly, but the two source documents describe non-overlapping products).

## See also
- [[powershell-overview]]
- [[powershell-modules]]
- [[powershell-execution-policy]]
- [[sharepoint-powershell-cmdlets]]
- [[powershell-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[odps-connect-exchangeonline|Connect-ExchangeOnline]]
- [[odps-connect-to-exchange-online-powershell|Connect to Exchange Online PowerShell]]
- [[odps-connect-ippssession|Connect-IPPSSession]]
- [[odps-app-only-auth-powershell-v2|App-only authentication in Exchange Online PowerShell and Security & Compliance PowerShell]]
- [[odps-control-remote-powershell-access-to-exchange-servers|Control remote PowerShell access to Exchange servers]]
<!-- crosslink:end -->
