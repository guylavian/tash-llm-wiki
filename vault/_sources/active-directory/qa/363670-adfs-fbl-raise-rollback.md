---
title: "ADFS FBL Raise Rollback"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/363670/adfs-fbl-raise-rollback
question_id: 363670
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS FBL Raise Rollback

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/363670/adfs-fbl-raise-rollback (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a WID DB ADFS Farm (all nodes on WS2016 but FBL is 1 i.e. WS2012R2)    

I want to raise the FBL to 3. I know I can use invoke-adfsfarmbehaviorlevelraise command    

https://learn.microsoft.com/en-us/powershell/module/adfs/invoke-adfsfarmbehaviorlevelraise?view=windowsserver2019-ps    

But is raising of FBL reversible?    

I know there is a restore-adfsfarmbehaviorlevel command    

https://learn.microsoft.com/en-us/powershell/module/adfs/restore-adfsfarmbehaviorlevel?view=windowsserver2019-ps    

I can't find much information on this. Like under what scenarios can I use this restore FBL command? Is there a time limit after I raise the FBL before this restore FBL command stop working? I mean after I raise the FBL, I would think the WID DB will be updated and replicated to the secondary nodes.

## Answers

_No answers on this thread._
