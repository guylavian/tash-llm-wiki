---
title: "Exchange Distribution Group Info Field Not Mapped Correctly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202882/exchange-distribution-group-info-field-not-mapped
question_id: 202882
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Distribution Group Info Field Not Mapped Correctly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202882/exchange-distribution-group-info-field-not-mapped (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

Migrating from Exchange on-premises to Exchange Online and noticed that after migration the "info" or "Notes" field is now mapped to the AD description instead of the "info" data. Unsure why this has changed but would like to know if there is any way to resolve this issue?   

Thanks,  

Mike.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-19*

I see the info field populated for 365 Groups and DLs which are 365 mastered.   

I do not see that for standard Distribution Groups synced from on-prem.  

Someone hasnt done some thing crazy and mapped info to Description in AADConnect have they?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi Ashok,   

Thanks for the reply, however it is strange that the in on-premises Exchange the info attribute appears in Notes in Exchange for DL's, however in Exchange Online it seems to map to the description field instead.   

Michael.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-18*

Hi @Mike00  ,    

Based on my research, "Notes" field on "Telephone" tab of ADUC is "Info" and that attribute is currently not consumed for groups using the Azure AD Connect Synchronization.    

    

https://learn.microsoft.com/en-us/azure/active-directory/hybrid/reference-connect-sync-attributes-synchronized#exchange-online    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
