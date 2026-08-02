---
title: "ADFS Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/105896/adfs-migration
question_id: 105896
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/105896/adfs-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My existing ADFS farm was setup by others who left. The OS is 2012R2. So I assume I am on ADFS 3.0. My DC is still on 2008R2. Both Forest Functional Level & Domain Functional Level are still on 2008R2.    

I want to migrate to a new ADFS farm to 2016.    

I read for 2012 R2 ADFS 3.0 farm, I can join ADFS nodes setup on 2016 to the farm before I promote the new 2016 nodes to primary and remove the old 2012R2 nodes.    

When I was checking the current ADFS farm. I am not able to get current farm behavior.    

I ran the following PS script.    

Get-AdfsProperities | Select CurrentFarmBehavior    

    

Does it mean my existing ADFS farm is < ADFS 3.0? The only way for me to migrate is to export and import to change over? Any other way to confirm my existing ADFS version?

## Answers

_No answers on this thread._
