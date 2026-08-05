---
title: "Configure the Exchange organization to use AD FS authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2007742/configure-the-exchange-organization-to-use-ad-fs-a
question_id: 2007742
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Configure the Exchange organization to use AD FS authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2007742/configure-the-exchange-organization-to-use-ad-fs-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. I am configuring ADFS + Exchange.

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019#step-6-configure-the-exchange-organization-to-use-ad-fs-authentication

I don't understand this step.

The instructions say that I have to find the ADFS Signing fingerprint:

Set-Location Cert:\LocalMachine\Root; Get-ChildItem | Sort-Object Subject

But Exchange doesn't know anything about this certificate.

It goes on to say that I can find this fingerprint on the ADFS server:

You can confirm this thumbprint value on the AD FS server in an elevated Windows PowerShell window by running the command Import-Module ADFS, and then running the command Get-AdfsCertificate -CertificateType Token-Signing.

`PS Cert:\LocalMachine\Root> Get-AdfsCertificate -CertificateType Token-Signing`

`Certificate     : [Subject]`

`                    CN=ADFS Signing - adfs.lab.com`

`                  [Issuer]`

`                    CN=ADFS Signing - adfs.lab.com`

`                  [Serial Number]`

`                    7B8A1B0D7FF00B8D44FDA36A3B4A4B6A`

`                  [Not Before]`

`                    01.08.2024 15:57:51`

`                  [Not After]`

`                    01.08.2025 15:57:51`

`                  [Thumbprint]`

`                    5A4AE6D2F2164DDCAB1C156828F2594845533213`

`CertificateType : Token-Signing`

`IsPrimary       : True`

`StoreLocation   : CurrentUser`

`StoreName       : My`

`Thumbprint      : 5A4AE6D2F2164DDCAB1C156828F2594845533213`

Questions:

-  Do I understand correctly that these certificates do not need to be replaced with a commercial certificate or a valid one from an internal certificate authority ?

-  Do I need to export the public part of this certificate, transfer to Exchange and install using Powershell ?

-  Please explain in detail, the instructions are not very detailed.

## Answers

_No answers on this thread._
