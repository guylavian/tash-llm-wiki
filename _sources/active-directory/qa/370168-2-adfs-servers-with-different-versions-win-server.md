---
title: "2 ADFS servers with different versions Win Server 2012 R2 and 2016 coexisting in the same forest ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/370168/2-adfs-servers-with-different-versions-win-server
question_id: 370168
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# 2 ADFS servers with different versions Win Server 2012 R2 and 2016 coexisting in the same forest ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/370168/2-adfs-servers-with-different-versions-win-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

We currently have one forest with several Active Directory domains and an ADFS server in Windows Server 2012R2.  

Due to applications compatibilities issues, we must add a new ADFS server in Windows Server 2016 in our Infrastructure.  

Is it possible to have 2 ADFS servers (with different versions Win Server 2012 R2 and 2016) coexisting in the same forest?   

What are the necessary prerequisites in order to avoid any conflicts?  

Important: The ADFS server in 2016 will not be in the same domain as the current 2012R2 server, but the users will be the same.  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-04-25*

You can add as many ADFS farm as you want in an Active Directory forest as long as they have different names and identifiers. The only caveat is that they will all use the same Device Registration configuration container (as it is a forest wide setting). But that's a feature that is very rarely used with ADFS anyways, so you might be just fine.  

Also, ideally use a different account for the service that you don't have dependencies between to the two farms.  

Out of curiosity, what are those "incompatibilities issues" you are referring to?
