---
title: "Can on-premises Exchange users in Hybrid MS 365 environment receive emails without AD Synced ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2041633/can-on-premises-exchange-users-in-hybrid-ms-365-en
question_id: 2041633
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can on-premises Exchange users in Hybrid MS 365 environment receive emails without AD Synced ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2041633/can-on-premises-exchange-users-in-hybrid-ms-365-en (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We have Hybrid Exchange 2010 and Exchange 2016, and are going to Migrate to MS 365.

What happen if we only sync 30 users out of 100 users using Azure AD Connect to sync hash password to MS 365?

We plan to use Exchange Online Protection server as mail gateway (through an Exchange 2016 Edge on-premises). Can the left over 70 users receive emails from Internet ?

If we want those 70 users to be able to use MS 365 apps (Outlook, Teams, Words ...), we will have to create 70 "online users" with same name and email address ( *@OurDomain.Com) and assign license to those "online users". In that case, does email flows still work correctly? Can those 70 on-premises users still receive incoming emails from Internet ?

Thanks a lot for helping.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-05*

Yes, as long as you have a mail connector to on-prem address space and the accepted domain in 365 is set to "InternalRelay" , mail will flow from 356 to on-prem
