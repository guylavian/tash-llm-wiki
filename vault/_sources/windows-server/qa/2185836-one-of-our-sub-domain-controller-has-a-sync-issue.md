---
title: "One of our sub domain controller has a sync issue with the primary domain controller server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185836/one-of-our-sub-domain-controller-has-a-sync-issue
question_id: 2185836
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# One of our sub domain controller has a sync issue with the primary domain controller server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185836/one-of-our-sub-domain-controller-has-a-sync-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our sub domain controller has a sync issue with the primary domain controller server 2016

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-26*

Hello Akbar Sha,  

Thank you for posting in Microsoft Community forum.

1.How many Domain Controllers are there in your domain?  

2.What error message did you see about "One of our sub domain controller has a sync issue with the primary domain controller server 2016"?  

Or you can try to check the AD replication status between all DCs in the domain, please run commands bellow on PDC to check the result and/or error message.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

Based on the information or error message in the command result, let's troubleshoot the AD replication problem further.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
