---
title: "can ADMT migrate active directory users into a new domain keeping the same GUIDs from the old domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/647995/can-admt-migrate-active-directory-users-into-a-new
question_id: 647995
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# can ADMT migrate active directory users into a new domain keeping the same GUIDs from the old domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/647995/can-admt-migrate-active-directory-users-into-a-new (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My IT department has recently migrated active directory into a new domain but this brought as a consequence that All the GUIDs where re-created and now all of the relationships I have in my tables using that GUID are broken. I was just wondering if ADMT will help me keep the old GUIDs.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-12-02*

Hi,  

 I was just wondering if ADMT will help me keep the old GUIDs.  

ADMT help to keep permission using SID history option. but it doesn't keep the old GUID.  

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-02*

Hello JavierPerez    

Object GUID is exclusively for a forest. When you migrate an object it receives a new SID and GUID. So I believe it is not possible to migrate it AFAIK. However you can keep the old SID using ADMT migration.    

There is an option which is to use the SID History as explained here: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/inter-forest-sidhistory-migration-with-admt    

-------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
