---
title: "active directory remove on old server 2012 R2 ( New server become master Windows 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/879118/active-directory-remove-on-old-server-2012-r2-new
question_id: 879118
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# active directory remove on old server 2012 R2 ( New server become master Windows 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/879118/active-directory-remove-on-old-server-2012-r2-new (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

We are facing an issue on the servers. As of now, both servers are running user profile loads on random servers.  

So I have GC/infrastructure master/pid/site active dc configured for the new server.  

So I can remove AD on the old server 2012 R2 either online or offline. Due to ad migration from the old to the new server, the Multiple GPO object is already visible on the new server.  

Can we offline remove windows 2012 r2 DC on the server or online?  

Give me suggestions for the same.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-08*

Simplest may be to demote the server. If that's not possible you can use the links I posted above to do metadata cleanup.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-08*

We can do offline or online server ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-07*

If you cannot demote it you can perform some cleanup to remove remnants of old one.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
