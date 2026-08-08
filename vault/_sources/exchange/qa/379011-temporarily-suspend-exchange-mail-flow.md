---
title: "Temporarily suspend Exchange mail flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/379011/temporarily-suspend-exchange-mail-flow
question_id: 379011
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Temporarily suspend Exchange mail flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/379011/temporarily-suspend-exchange-mail-flow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey what is the best way to temporarily suspend Exchange mail flow?  The goal is for users to continue to stay "connected" to Exchange via Outlook and still be able to submit new email as if nothing was wrong.  I'd like the outbound email to sit in the Exchange queue until maintenance to our smart host is complete.  The smart host will go up and down multiple times during maintenance, ideally Exchange wouldn't start submitting outbound mail until we were ready.  So a manual suspend and resume operation.  Ideally users would not receive NDRs at all during this process.    

This is geared at Exchange 2010, but I'd be curious to know if the process is unique from Exchange 2013/2016 as well.    

The primary send connector smart host IP will also change during this process.  I did notice that the "Queue Viewer" utility has a "suspend" option when you right click.  There appears to be a queue for each mbx database, the current smart host, and Submission.  Perhaps simply suspending  the "submission" queue would do the trick?    

Regards,    

Adam Tyler

## Answers

_No answers on this thread._
