---
title: How should an unattended script authenticate to Exchange Online PowerShell?
type: question
question_tier: conceptual
domain: powershell
slug: exchange-online-unattended-script-authentication
summary: Unattended Exchange Online PowerShell scripts should use certificate-based (app-only) authentication with an installed thumbprint, a remotely-fetched certificate object, or managed identity — storing a local certificate's password for automation is explicitly called out as having no fully secure, fully automated option.
sources:
  - kb:odps-connect-exchangeonline
  - kb:odps-app-only-auth-powershell-v2
tags: [ps-modules, security]
provenance_extracted: 5
provenance_inferred: 1
provenance_ambiguous: 0
status: draft
updated: 2026-07-23
graph_community: "PowerShell — Implementation Review (Evaluation-Lens MOC)"
---

# How should an unattended script authenticate to Exchange Online PowerShell?

**Use certificate-based (app-only) authentication with an installed certificate thumbprint, or a
certificate object fetched at runtime (e.g. from Azure Key Vault), or managed identity — not an
interactive credential, and not a locally-stored certificate password.** (extracted —
`reference/powershell/odps-connect-exchangeonline.md:83-104`)

## What the docs actually recommend

`Connect-ExchangeOnline` documents three supported patterns for scripting/automation:

1. **Certificate thumbprint** — `-AppId <app_id> -CertificateThumbprint <thumbprint>
   -Organization "contoso.onmicrosoft.com"` — "connects to Exchange Online PowerShell in an
   unattended scripting scenario using a certificate thumbprint" (extracted —
   `reference/powershell/odps-connect-exchangeonline.md:83-88`).
2. **Certificate object** — `-AppId <app_id> -Certificate <X509Certificate2 object>
   -Organization "contoso.onmicrosoft.com"` — "best suited for scenarios where the certificate is
   stored in remote machines and fetched at runtime. For example, the certificate is stored in
   the Azure Key Vault" (extracted — `reference/powershell/odps-connect-exchangeonline.md:90-95`).
3. **Managed identity** — `-ManagedIdentity` with `-Organization` (and
   `-ManagedIdentityAccountId` for a user-assigned identity) — but this is restricted to specific
   Azure resource types: Azure Automation runbooks, Azure Virtual Machines, Azure Virtual
   Machine Scale Sets, and Azure Functions (extracted —
   `reference/powershell/odps-connect-exchangeonline.md:649-664`).

Mechanically, certificate-based auth (CBA) works by fetching an app-only OAuth token via the
Active Directory Authentication Library, using the application ID, tenant ID, and certificate
thumbprint; the Microsoft Entra application's assigned directory role comes back in the token
and drives the session's role-based access control (extracted —
`reference/powershell/odps-app-only-auth-powershell-v2.md:58-61`).

## Is storing a local certificate's password safe for automation?

**No — the docs say directly that there is no fully secure, fully automated way to do this.** A
fourth connection option exists — a local `.pfx` file plus `-CertificatePassword` — but both ways
of supplying that password defeat the purpose:

- `ConvertTo-SecureString -String '<password>' -AsPlainText -Force` stores the password in
  plaintext somewhere the script can read it, "which defeats the purpose of a secure connection
  method for automation scenarios."
- `(Get-Credential).password` prompts interactively, which "isn't ideal for automation
  scenarios."

"In other words, there's really no automated *and* secure way to connect using a local
certificate." (extracted — `reference/powershell/odps-connect-exchangeonline.md:407-415`)

This is why the thumbprint (certificate already installed in the local machine/user certificate
store, no password needed at connect time) and remote-certificate-object patterns are the ones
actually recommended for unattended scripts — they avoid ever needing a locally-stored
password (inferred — the source states the three preferred patterns and separately flags the
local-file-plus-password pattern's weakness, but doesn't explicitly rank the four options against
each other in a single sentence).

One more constraint worth knowing before generating the certificate: **CNG (Cryptography: Next
Generation) certificates — the default in modern Windows versions — are not supported** for
this app-only authentication; the certificate must come from a CSP key provider instead
(extracted — `reference/powershell/odps-app-only-auth-powershell-v2.md:154-163`).

## Contradictions / caveats
None — all four connection patterns come from the same `Connect-ExchangeOnline` reference
and the same app-only-auth guide, and they agree on the local-certificate-password weakness.

## References

### RH ground-truth (kb:)
- [[odps-connect-exchangeonline]] — Connect-ExchangeOnline (Exchange Online PowerShell module cmdlet reference)
- [[odps-app-only-auth-powershell-v2]] — App-only authentication for unattended scripts in the Exchange Online PowerShell module

### Wiki
- [[exchange-online-powershell-cmdlets]] — full entity page on the Exchange Online/Server cmdlet surface
- [[powershell-execution-policy]] — related security-model entity (defense-in-depth vs. security boundary)
- [[powershell-overview]] — domain primer

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[odps-connect-exchangeonline|Connect-ExchangeOnline]]
- [[odps-app-only-auth-powershell-v2|App-only authentication in Exchange Online PowerShell and Security & Compliance PowerShell]]
<!-- crosslink:end -->
