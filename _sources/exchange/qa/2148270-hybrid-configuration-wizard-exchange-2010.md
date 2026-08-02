---
title: "Hybrid Configuration Wizard Exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2148270/hybrid-configuration-wizard-exchange-2010
question_id: 2148270
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hybrid Configuration Wizard Exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2148270/hybrid-configuration-wizard-exchange-2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to use the Hybrid Configuration Wizard on Exchange 2010; but, I ran into a Federation Trust Failed issue when trying to enable Federation Trust. 

It says Federation Trust Failed: Unable to access the Federation Metadata document from the federation partner.

I am on Exchange 2010 SP3, up to date on Server 2012, TLS 1.2, and .Netframework 4.5 / 3.5 

Any help would be much appreciated!

Anyone know how to resolve this?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-06*

Disabled TLS 1.0 and 1.1 worked; but, I had to enable TLS for .NETFramework 3.5 for our OWA to be fully functioning.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-17*

Hi Guan, Raymond

As per as research, you can try to run PowerShell as Administrator to update the FederationTrust with cmdlet:

```
Update-AdfsRelyingPartyTrust -TargetName "trustname" -Metadatafile FederationMetadata.xml.
```

Refence: https://learn.microsoft.com/en-us/powershell/module/adfs/update-adfsrelyingpartytrust?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

If it doesn't work, please run the Exchange Hybrid Wizard and make sure the federation metadata URL is accessible. If there are more error messages, please feel free to let us know.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
