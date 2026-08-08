---
title: "Demote Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1512087/demote-domain-controller
question_id: 1512087
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Demote Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1512087/demote-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,
I have the following question. We began a couple months ago with one domain controller but with the time, we've added 2 more. Now, I want to demote the first domain controller, I already moved FSMO roles to other servers, now the question is, how to be sure that there no LDAP or similar request to the old server and everything is running over the 2 new. I know that I could just shut down the old server and see if it works but I want to check before doing it. We have SQL, VCS, RightsManagement etc. and would like to avoid checking everywhere what is set. Is it possible somehow to get this information maybe events in logs?
Thanks in advance

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-25*

Hi @Borislav Vitanov  

Even if you shut down the DC, clients will continue to try to contact it because its DNS records Type A and SRV  still exist and the client relies on DNS to identify the closest controller through the DClocator process.

On the other hand, when you demote it, its SRV and A DNS entries will be automatically deleted and the clients will no longer try to contact it and they will contact the new DCs.

In my opinion, check if there is no client still the old DC as DNS resolver after that you can demote it and  in case of issue you can promote it again.

Please don't forget to accept helpful answer
