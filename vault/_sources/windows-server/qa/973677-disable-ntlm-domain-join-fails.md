---
title: "Disable NTLM - Domain Join fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/973677/disable-ntlm-domain-join-fails
question_id: 973677
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Disable NTLM - Domain Join fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/973677/disable-ntlm-domain-join-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we're trying to implement NTLM blocking (yes, this article is from 2009) and have enabled the relevant GPOs both on DCs and all member systems.     

    

surprisingly enough most things work just fine, which is good. but joining new computers to the domain doesn't.    

we receive "The request is not supported"    

    

Any guidance on how to make this work?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-19*

Hello there,    

If the issue happens for multiple PCs when joining the domain , it is suggested to check the status of the DCs and the replication among DCs, DNS configuration.    

Run command the DCs and confirm if there are any errors:    

Dcdiag /v >c:\dcdiag1.log    

Repadmin /syncall /APeD    

Repadmin /showrepl >C:\repl.txt    

Repadmin /showreps *     

Ipconfig /all > C:\dc.txt    

Hope this resolves your Query !!    

--If the reply is helpful, please Upvote and Accept it as an answer–
