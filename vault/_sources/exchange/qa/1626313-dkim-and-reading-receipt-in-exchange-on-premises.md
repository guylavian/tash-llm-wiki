---
title: "DKIM and reading receipt in exchange on-premises"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1626313/dkim-and-reading-receipt-in-exchange-on-premises
question_id: 1626313
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# DKIM and reading receipt in exchange on-premises

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1626313/dkim-and-reading-receipt-in-exchange-on-premises (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a singular problem.

I've Exchange 2016 CU23.

I have installed DKIM signature on my server and create pertinent DNS record; at this moment I have a key of only 1024bit but I don't think that this is the cause of the problem; both header and body canonicalization are in relaxed mode. All works fine and all mail send from my domain to external of my organization correctly pass dkim verification, except for mail send for reading receipt. If a user (obviously from external organization) flag the function "Request read receipt", when my server send mail of receipt, this mail ever fails check for dkim verification.

I attach screenshot of error in header of mail in this situation.

can you help me for resolve this issue?

Thanks in advance.

Roberto

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-22*

Hi @Roberto Loria  

Since the error "body hash did not verify" may often indicate that after the DKIM signature was stamped on the message, something in between the sender and recipient modified the body, will this issue occur to another sender using other email service if he also requests for a read receipt?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
