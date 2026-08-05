---
title: "GPO DOMAIN - local users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/940602/gpo-domain-local-users
question_id: 940602
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO DOMAIN - local users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/940602/gpo-domain-local-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I Got GPO that removes all local users in Admin groups of windows and set only specific users    

this also delete Remote Desktop Users from PC    

How to fix this that it will not be deleted also Remote Desktop users from PC     

Thanks, Gil

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-27*

Hi,    

If your Remote Desktop users are administrators then they will be removed too. Please ensure that your RDP user accounts are not administrators and that will prevent this issue.     

I hope this answers your question.    

---------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-26*

It sound like you may be using Restricted Groups... Have you also looked at Group Policy Preference to control group memberships?    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/using-group-policy-preferences-to-manage-the-local-administrator/ba-p/259223
