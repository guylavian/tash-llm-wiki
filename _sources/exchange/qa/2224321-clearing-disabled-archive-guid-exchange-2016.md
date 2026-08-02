---
title: "Clearing Disabled Archive GUID Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2224321/clearing-disabled-archive-guid-exchange-2016
question_id: 2224321
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Clearing Disabled Archive GUID Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2224321/clearing-disabled-archive-guid-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Exchange 2016 server with very large mailboxes, greater than 100GB.

I have created online archives of 45GB and run a retention policy to move all emails older than 7 days to this online archive, which I then export to a PST file.  I dont want to create an online archive larger than 45GB, since it may cause PST corruption.

Once I have exported the archive to a pst, i then disable the archive, but by default Exchange retains the archive for 30days, so if I enable an archive it attaches the archive that I previously disabled.

Can I clear the DisabledArchiveGUID so I can force the creation of a new online archive?

## Answers

_No answers on this thread._
