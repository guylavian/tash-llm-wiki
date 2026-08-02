---
title: "Child Domain Controller with no Parent Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1048963/child-domain-controller-with-no-parent-domain-cont
question_id: 1048963
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Child Domain Controller with no Parent Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1048963/child-domain-controller-with-no-parent-domain-cont (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Evening!    

I'm in a bit of a conundrum. I have singular forest with a parent and child domain:    

It's in a closed network with not connectivity to the internet    

Parent domain: Mullis.com    

Child: Training.Mullis.com    

I inherited this from my predecessor who is no longer here.    

The forest had a single DC for the parent domain (MullisDC) and a single DC for the child domain TrainingDC    

The MullisDC server died along with its drives, but the TrainingDC is still active.    

Is there a way to create a new parent DC? Or am I looking at a full domain/forest rebuild?    

If I can salvage this domain, I would like to keep the current names if possible.    

v/r    

Joe

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-20*

Sorry for the delay. I'm still working the issue. It's a major PITA.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-18*

Should be Ok, you should have one PDC Emulator for each domain. These ones could help.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-perform-initial-recovery    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-reset-trust    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

Thanks for the answers above. They would be the correct answer, but I hope I have some good news.    

I found a backup of the parent domain controller MullisDC.    

It's about a year old, so I had to do some meta-data cleanup.    

So now I have this:    

MullisDC (old)    

TrainingDC (current)    

They both think that they have all 5 FSMO roles and they do not trust each other.    

How do I re-establish the trust between the child and parent.    

I'm pretty sure the child has the most accurate info.    

v/r    

Joe

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-14*

If you lost the only DC in parent domain then there nothing you can do really but start over.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
