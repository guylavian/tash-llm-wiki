---
title: "Best practise event forwarding with multiple GPOs and event collectors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/286351/best-practise-event-forwarding-with-multiple-gpos
question_id: 286351
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Best practise event forwarding with multiple GPOs and event collectors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/286351/best-practise-event-forwarding-with-multiple-gpos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We've been using event collectors for some time now and we've installed more over time to balance workload an divide into tiers.  

We have specified the URL to our "main" event collector which collects all system logs from all server high up in our OU structure and further down, for our important database servers, we have specified another URL to the event collector for database audits.   

In order of precedence, the URL gets overwritten (not appended) and the further down we go in the OU structure we have to specify all the other event collectors URLs again to not overwrite them.  

How should you we this? Should we just specify the URLs to all event collectors high up in the structure to avoid the risk of having a URL get overwritten? This puts a little more load on the event collectors when all our servers and clients checks in with all of them on a regular basis to see if there is a subscription for that particular client or server.  

Thanks  

/Daniel

## Answers

_No answers on this thread._
