---
title: "Active Directory refusing to start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/969695/active-directory-refusing-to-start
question_id: 969695
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
---
# Active Directory refusing to start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/969695/active-directory-refusing-to-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a testing environment with 2 Domain Controllers, if possible i want to avoid setting everything up again as that is quite complicated and also i want to use this as learning experience in disaster recovery.    

The two Domain Controllers seem to have had sync problems for several months, witch i didn't notice.    

After shutting both down(to move some hardware) the Active Directory Web Services is refusing to start on both DCs    

    

Because of this, DNS is also refusing to start on both DCs    

    

So the two DCs can't communicate at all to solve the Sync issue, this is a chicken-egg problem.    

Ive tried to move the FSMO roles back and forth but still cant get anything to start.    

Does anyone have any suggestions on how to force AD or DNS to start?    

Or altrenatively, since i wanted to upgrade both DCs anyway, would it be a good idea to eject one DC, replace it with a new one then demote the old one and replace that as well?

## Answers

_No answers on this thread._
