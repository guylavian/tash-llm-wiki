---
title: "Nov 21 Cumulative Patch causes issue with LDAPS authentication for Linux and some appliance"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/651161/nov-21-cumulative-patch-causes-issue-with-ldaps-au
question_id: 651161
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Nov 21 Cumulative Patch causes issue with LDAPS authentication for Linux and some appliance

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/651161/nov-21-cumulative-patch-causes-issue-with-ldaps-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We will like to know how should we proceed from here?  

We are using an isolated on-prem environment.  

The patch we used is   

https://www.catalog.update.microsoft.com/Search.aspx?q=KB5007192  

(For windows server)  

Do we need to install a KB5008601 on top of this patch to fix this?  

Some articles:  

https://dirteam.com/sander/2021/11/16/you-may-encounter-authentication-issues-after-installing-the-november-2021-cumulative-updates/  

https://borncity.com/win/2021/11/11/november-2021-patchday-probleme-wsus-dc-events/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-06*

Hello,  

Microsoft released a standalone update as an out-of-band patch to fix this issue:  

https://support.microsoft.com/en-us/topic/november-14-2021-kb5008602-os-build-17763-2305-out-of-band-8583a8a3-ebed-4829-b285-356fb5aaacd7  

Hope this helps with your query,  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-03*

This update is not known to cause issues with LDAPs but with Kerberos constraint delegation. Are you sure that the problem you are sseing is LDAPs related? Can you explain what is the issue in your case?
