---
title: "how frequently does a windows domain controller authenticate a windows client while on lan in any typical domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1012285/how-frequently-does-a-windows-domain-controller-au
question_id: 1012285
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# how frequently does a windows domain controller authenticate a windows client while on lan in any typical domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1012285/how-frequently-does-a-windows-domain-controller-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In a local area network while the user logs on to the domain, will there be a log for the client showing that it had attempted to log on to the domain or it will log the client from the client cache without even connecting the domain controller?    

If the user's laptop was already logged in and he then connects to the network, will there be any logs showing any login attempts while rentering the password when his computer gets locked?    

Is there a process initiated by the client or the DC and any frequency while on a local area network where it periodically checks and sees if a client /member is connected and logged in and what is that event log on the DC?    

Have seen when a user's password is about to expire even if he had previously logged in from home while not connected to LAN and now when he comes to the office and connects to the network it attempts to tell him that his windows password has to be changed mandatorily without which it can't log in. So there is some kind of checks which is done via the domain controller while the user is on LAN on a daily basis.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-17*

You'll probably only see an event at logon. You can setup auditing here.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events    

Credentials Processes in Windows Authentication    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
