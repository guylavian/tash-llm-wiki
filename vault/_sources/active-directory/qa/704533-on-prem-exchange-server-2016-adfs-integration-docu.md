---
title: "On-Prem Exchange Server 2016 ADFS Integration Document or Steps"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/704533/on-prem-exchange-server-2016-adfs-integration-docu
question_id: 704533
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# On-Prem Exchange Server 2016 ADFS Integration Document or Steps

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/704533/on-prem-exchange-server-2016-adfs-integration-docu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI Team ,   

I am attempting integration of MFA with On-Prem Exchange server for rich clients and mobile clients as well. ADFS is integrated for OWA and working well. Only issue is for rich client how should I get the AUTH request on ADFS from exchange server? Any steps or document will help

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-01-27*

Yes, you can use the Hybrid Modern Auth that is available via Azure/365    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-01-21*

Outlook Windows clients and such are not supported with ADFS and on-prem Exchange. I believe that is what you are asking?
