---
title: "ECP exchange can't access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367587/ecp-exchange-cant-access
question_id: 1367587
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# ECP exchange can't access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367587/ecp-exchange-cant-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My exchange 2016 Admin Center is accessible from the internet using https:\mail.mydomain.com\ecp, but I am trying to log in inside the ECP, and it's not logging

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-20*

Hello 

the problem still persists I started again nothing is solved

Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-14*

Hi @Abdelilllah SAIH  

Are you using the same url (https:\mail.mydomain.com\ecp) to login ECP in internal network?

If yes, what is the error message?

And if you are using internal DNS server in your internal network, please make sure you have created an A or CNAME record to resolve mail.mydomain.com to the internal ip address of your Exchange server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
