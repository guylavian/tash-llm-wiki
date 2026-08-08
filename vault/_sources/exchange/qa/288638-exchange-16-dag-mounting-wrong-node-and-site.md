---
title: "Exchange 16 DAG mounting wrong node and site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/288638/exchange-16-dag-mounting-wrong-node-and-site
question_id: 288638
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 16 DAG mounting wrong node and site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/288638/exchange-16-dag-mounting-wrong-node-and-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have 4 exchange 2016(A, B, C, D), 2 in main site (A and B) and the other 2 in DR (C and D).  

All DBs are mounted on B. I have 2 scenarios that occurred.  

Please note that the preference of the DBs are B, A, C, D and nothing on the network happened to justify this behavior for both scenarios  

When B was turned off,  

1st scenario:  

the DBs got mounted on D and DAG IP was brought online in DR site.  

2nd scenario:  

the DBs got mounted on A which is correct but DAG IP was brought online in DR site.  

Can someone help why this behavior is happening?  

Thanks,  

Chris

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-09*

No, it doesnt work that way  :)  

the PAM doesnt have any idea what a DR site is It can be held by any member in the quorum that is available.   

If you do not want the PAM to move to a server in the DR site, then pause the cluster service on the servers in that DR site.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

Hello,  

Sorry i haven't replied earlier, got a bit busy with the security patch released and had to upgrade all my clients to the latest CU then apply the patch.  

To get back to the matter at hand. My main issue is that the PAM role instead of going to A, it went to D. Shouldn't it search for a member in the same site before switching to the DR site?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

Hi @Christian Abou Haidar   ,    

Agree with what Andy said.    

The DAG member that holds the PAM role is always the member that currently owns the cluster quorum resource (default cluster group). If the server that owns the cluster quorum resource fails, the PAM role automatically moves to a surviving server that takes ownership of the cluster quorum resource.     

By default Exchange establishes the desired settings on the cluster core resource group.  Modifying these settings is typically not necessary and can sometimes cause undesired results. Therefore, it is not recommended that you manually organize a specific server to become a cluster owner.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-25*

the DAG IP (PAM - Cluster Owner) can be owned by any mailbox in the quorum.     

The only way to prevent any single server from becoming the cluster owner would be to pause the cluster service on that server. Not something I would do unless I was performing maintenance. Exchange itself doesn't care where the PAM is - and really you shouldn't either  :)     

More info:    

https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/active-manager?view=exchserver-2019
