---
title: "checking sysvol replication type when there is only 1 DC in the domain!?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/121878/checking-sysvol-replication-type-when-there-is-onl
question_id: 121878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# checking sysvol replication type when there is only 1 DC in the domain!?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/121878/checking-sysvol-replication-type-when-there-is-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.  

I have a single DC, 2012 server R2.  I want to add a 2019 DC because I know it is not a best practice to only have 1 DC (just started this job . Trust me, I freaked when I discovered there was only 1 DC!!!!)  

Here is the problem. I have gone thru all the prerequisite steps on the 2012 DC and everything looks fine. What I can't figure out how to do is check the sysvol replication type because this DC has NEVER REPLICATED! I want to ensure when it starts replicating to the 2019 DC after I promote it, it is using  DFSR.  I have looked in the registry and ran the diagnostic that indicates what it's running but since it's not running either DFSR or FSR at the moment, I'm not sure how I can tell what it's going to run.  

When I run dfsrmig /getmigrationstate on the 2012 DC, I get this message:  

All Domain Controllers have migrated successfully to Global state (‘Eliminated’). Migration has reached a consistent state on all Domain Controllers. Succeeded.  

So does that mean the 2012DC is going to replicate to the 2019 DC using DFSR by default now? Ultimately this is what I want!  

Thanks in advance  

Sharyn

## Answers

_No answers on this thread._
