---
title: "ADFS certficate export"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/26333/adfs-certficate-export
question_id: 26333
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS certficate export

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/26333/adfs-certficate-export (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello team  

we need to export ADFS token signing and token decrypting certificate with private key  

but when we do it export /copy do not get option to export keys  

Please advise

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-12*

Hello   

let me explain more in detail  

we have ADFS servers in two data-center  A & B on different region which load balanced with GTM.  

we are planning to re-build the ADFS servers on one region.  

DB server will get replicated from B , once we rebuild A.  

however the challenge is the certificate for ADFS servers on region A.  

Please advise

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-11*

The test environment could have a different cert then, if it has a different name, a different AD etc... And if that's the same "cloned" AD environment then just the snapshot you do will have the cert in it (although that's also not a supported way to backup/restore ADFS, recommendation for backup/restore is to use the Rapid Restore tool).    

Anyhow, I am afraid that doesn't seem to be a good reason. Besides, test environments are also usually not secured the same way as the production environments (more admins, no restrictions, no monitoring, etc...). So putting the actual keys in dev would considerably decrease your overall security posture.    

If the intent of the test environment is to create test relying party trusts (for example to check claim rules or access policies), you can do create a test RP with the Claim X-Ray.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-11*

we are building the test environment with the same ADFS farm, by taking vm snapshot

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-11*

Hello Piaudonn,  

Yes the self signed certficates which are auto rollover.  

there is a reason for exporting it, please let me if it is possible?  

Thanks  

Aamir Masthan

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-11*

Hello -  

Do you mean the self-signed certificates which are automatically generated? Why would you export them?  

You don't need them when you upgrade the farm as you upgrade by adding new nodes to an existing farm.  

They are in the backup when you use ADFS Rapid Restore and got restored with the same tool.  

You don't need them to create a trust neither with an IDP nor an SP.  

So I am curious :)
