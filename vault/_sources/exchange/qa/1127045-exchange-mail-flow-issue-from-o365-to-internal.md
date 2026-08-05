---
title: "Exchange Mail flow issue from O365 to internal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1127045/exchange-mail-flow-issue-from-o365-to-internal
question_id: 1127045
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Mail flow issue from O365 to internal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1127045/exchange-mail-flow-issue-from-o365-to-internal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one Exchange Server 2019 and most of mailboxes on Exchange Online (Exchange Hybrid Configured).    

When send email from internal mailbox to O365 mailbox, email sent and received with no issue    

When send email from O365 mailboxes to internal mailboxes, not received and not even appear in Exchange Server queue    

When send email from External mailbox (outside organization) to internal mailboxes, not received and not even appear in Exchange Server queue    

Network Team says port 25 opened bi-directional on Exchange Server.    

Any thoughts?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-12-14*

Hi @Khaled El Gazzar  ,    

When send email from O365 mailboxes to internal mailboxes, not received and not even appear in Exchange Server queue    

When send email from External mailbox (outside organization) to internal mailboxes, not received and not even appear in Exchange Server queue    

By "internal mailboxes", you mean the On-premises mailboxes which are still hosted on Exchange 2019, right?    

Aside from the message trace as mentioned above by Adny, did the O365 or external sender receive any Nondelivery report (NDR) error message after sending out the messages?     

How about mails sent from internal mailboxes to external mailboxes outside organization, can they be received without issue?    

Besides, I'd recommend going through the article below. If the symptoms described there match what your users are experiencing, you may try setting up the domain as an internal relay domain in Microsoft 365 and see if it can help.    

On-premises users can't get email messages from Microsoft 365 users in an Exchange hybrid deployment    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
