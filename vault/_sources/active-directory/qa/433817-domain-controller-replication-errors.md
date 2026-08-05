---
title: "Domain Controller replication errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/433817/domain-controller-replication-errors
question_id: 433817
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller replication errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/433817/domain-controller-replication-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I ran the repadmin /replsummary command and get the below:  

Destination DSA     largest delta    fails/total %%   error  

 HH11PDC                   58m:25s    0 /  10    0  

 HH11VDC                   55m:15s    0 /   5    0  

 HH21VDC                   09m:01s    0 /   5    0  

 HH31VDC          >60 days            1 /  15    6  (8606) Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.  

 HH51VDC          >60 days           10 /  10  100  (8614) The directory service cannot replicate with this server because the time since the last replication with this server has exceeded the tombstone lifetime.  

What are the steps to fix this? I'm not a guru in Active Directory so i can use some help!  

Thanks in Advance

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-18*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-14*

Hi @Kenny Cowart  ,    

Thank you so much for posting here.    

As for the AD Replication status 8606, it means that lingering objects are present on the source DC (destination DC is operating in Strict Replication Consistency mode). We could refer to the below article to do the troubleshooting.    

Active Directory Replication Error 8606: Insufficient attributes were given to create an object    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8606    

Error 8614 is logged when a destination DC has not replicated with a source DC over an existing replication connection for longer than tombstone lifetime.  The following official documentation provides the steps for the troubleshooting. Hope it will be helpful to you.     

Troubleshoot Active Directory replication error 8614    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8614    

Thanks. For any questions or concerns, please feel free to ask here.    

Best regards,    

Hannah Xiong

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-13*

You should perform cleanup of tombstoned domain controllers     

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

then confirm health is 100% and rebuild them from scratch.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can move on to next one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
