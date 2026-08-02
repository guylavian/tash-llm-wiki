---
title: "How to monitor my Active Directory Window Server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187324/how-to-monitor-my-active-directory-window-server
question_id: 1187324
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to monitor my Active Directory Window Server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187324/how-to-monitor-my-active-directory-window-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have window server actives directory, how should I monitor it? I wanna see if anything causing error or if any computer does not receive the  group policed, or getting attack from hacker? What are some best option to prevent hacker from doing something, how to monitor this so I can also try to stop the hacker?

what do I need to do save my active directory with security?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-07*

Hi @TechQ  

The best tools to monitoring active directory service is SCOM. there is pack management for active directory which let you monitoring active directory health : Microsoft System Center Management Pack for ADDS

Regarding security alert , you should install antivirus , and you can also use one of third party tools to monitoring securrity heath: 

LogSentinel SIEM for ActiveDirectory Security Monitoring

Monitoring Active Directory for Signs of Compromise

Please don't forget to mark helpful answer as accepted
