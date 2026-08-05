---
title: "In my Active Directory Window Server 2019 Datacenter, the NPS register and server is grayed out, how to fix it?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182173/in-my-active-directory-window-server-2019-datacent
question_id: 1182173
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# In my Active Directory Window Server 2019 Datacenter, the NPS register and server is grayed out, how to fix it?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182173/in-my-active-directory-window-server-2019-datacent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to Register the server in NPS when its grayed out? How to fix this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-19*

Hi @TechQ  

According to Microsoft link below , you have to use a account memberof domain administrators.

Try to use admin account member of domain administrators as mentioned in Microsoft article:

Register an NPS in an Active Directory Domain

Please don't forget to mark helpful answer as accepted

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-19*

Has it been domain joined? Also try from an elevated cmd.exe

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754878(v=ws.11)?redirectedfrom=MSDN#to-register-the-nps-server-in-the-default-domain-using-the-netsh-command  

```
netsh ras add registeredserver
```

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
