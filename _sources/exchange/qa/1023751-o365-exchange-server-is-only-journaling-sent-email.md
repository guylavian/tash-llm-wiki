---
title: "O365 Exchange Server is only journaling sent emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1023751/o365-exchange-server-is-only-journaling-sent-email
question_id: 1023751
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# O365 Exchange Server is only journaling sent emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1023751/o365-exchange-server-is-only-journaling-sent-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've created a Journal Rule that applies to all messages, but I only get journal reports for emails sent FROM my office.com address - I'm not getting journal reports for emails sent TO my office.com address.  There are only 4 settings on the Journal Rule editor - is there another setting I need to change on another screen to enable journaling of received emails?    

Here's how my Journal Rule is set up, and it's the only rule that I have set:

## Answer (community) — community member

*upvotes: 1 · updated: 2022-09-27*

I have figured it out and it is working.    

TLDR: Email sent to the NDR mailbox will have sent emails journaled, but not received emails.    

My problem was that since I was testing, I had set the NDR to my email address to be notified of any problems.  Also while testing, I was sending to and from my address.  Sent emails were journaled, but received emails were not. I believe that is because my address was the NDR.    

I set the NDR to another mailbox, and journaling is now working as expected.
