---
title: "How to disable adfs relying party trust revocation settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/288879/how-to-disable-adfs-relying-party-trust-revocation
question_id: 288879
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to disable adfs relying party trust revocation settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/288879/how-to-disable-adfs-relying-party-trust-revocation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, all  

I need to disable a relying party trust revocation settings.   

I have found this command  

Get-AdfsRelyingPartyTrust -Identifier | Set-AdfsRelyingPartyTrust -SigningCertificateRevocationCheck None -EncryptionCertificateRevocationCheck None  

if the identifier is  

sydle  

How do I use the command I have tried "syde", sydle,  but none of them works.   

Thank you

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-02-25*

```
Get-AdfsRelyingPartyTrust -Identifier sydle | Set-AdfsRelyingPartyTrust -SigningCertificateRevocationCheck None -EncryptionCertificateRevocationCheck None
```

Should work just fine. Maybe that's not the actual identifier but the name. Try the following:  

```
Get-ADFSRelyingPartyTrust | Select-Object name,Identifier | Out-GridView -Title "Select a relying party" -PassThru | %{ Set-AdfsRelyingPartyTrust -TargetIdentifier ([string] $_.Identifier) -SigningCertificateRevocationCheck None -EncryptionCertificateRevocationCheck None }
```

It will all your relying party trusts in a graphical table, you select one or more and click OK. Then it will disable the checks for all selected relying party trusts.
