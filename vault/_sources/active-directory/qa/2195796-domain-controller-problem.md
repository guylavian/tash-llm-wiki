---
title: "Domain Controller Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195796/domain-controller-problem
question_id: 2195796
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Domain Controller Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195796/domain-controller-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This one might be a little convoluted, so I apologize for that.

We have been running on a Samba based DC setup. For compatibility, I am migrated that to a Windows DC.

First we attached a Windows 2008R2 server to the Samba DCs, and migrated all of the fsmo roles to it. That seems to work, and when I do netdom /query fsmo it shows that server (DC-11) as being the FSMO operational master for everything.   

Then I made sure we were on DFS replication. dfsrmig /getglobalstate shows "Eliminated", so we're tracking there. 

I have added a Windows 2016 server to the mix, and intend to make that the fsmo operational master before standing up a Windows 2022 server to take over ad the PDC Emulator and will then add a second Windows 2022 server to be the secondary. 

However, when I point DNS at the 2016 server, no one can log in. DNS appears to be good, but dcdiag shows it cannot find the PDC Emulator on the 2016 server even though the 2016 server is the PDC operational master.   

I'm spinning my wheels and losing my mind. Anyone got any ideas?

## Answers

_No answers on this thread._
