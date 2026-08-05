---
title: "ADFS clarifications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/223753/adfs-clarifications
question_id: 223753
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS clarifications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/223753/adfs-clarifications (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I have Exchange 2016 onprimse and i have MS Teams from O365 , my calendar is not consistence in Exchange and Teams so i have advice to implement HMA.  

also i have to configure MFA for my Exchange users  

I will configure 2 WAP and 2 ADFS then i will enable hybrid configuration for Exchange.  

My internal domain different than External domain  

For example:  

Internal domain : floot.net  

External domain: morefloot.com  

WAP server will be located on DMZ  

ADFS SERVERS:  

ADFS1.floot.net  

ADFS2.floot.net  

ADFS porta: sts.floot.net  

Questions  

I want to buy certificate from 3rd part but i want to know the names should included to this certificate considering the internal domain name different than the external domain as i mention above.  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-08*

Hi @yasser Mohamed AbdelMoneim   , I would use the external domain. More information can be found here. I hope this helps! If so, please mark this answer as verified so other users can reference it.    

Thank you,    

James
