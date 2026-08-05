---
title: "The message could not be sent: bigpond.com server response: 550 5.1.0 Authentication Required"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2615522/the-message-could-not-be-sent-bigpond-com-server-r
question_id: 2615522
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# The message could not be sent: bigpond.com server response: 550 5.1.0 Authentication Required

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2615522/the-message-could-not-be-sent-bigpond-com-server-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have just downloaded your WL update to 12 from WL11, it will now not send messages, they are stuck in the Outbox, yes, I have tried all the above without  fix, see error below:

The message could not be sent because the server rejected the sender's email address. The sender's email address was '*** Email address is removed for privacy ***'.  

Subject 'Test'  

Server Error: 550  

Server Response: 550 5.1.0 Authentication Required  

Server: 'mail.bigpond.com'  

Windows Live Mail Error ID: 0x800CCC78  

Protocol: SMTP  

Port: 25  

Secure(SSL): No

I tried to send email to myself, obviously there should not be any issue with this, I can send emails on my smart phone also, so definitely not email adress.

Please help.

Phill

Split from an *unrelated thread*

## Answer (community) — community member

*upvotes: 2 · updated: 2014-02-23*

Server Response: 550 5.1.0 Authentication Required

Right-click on the account name in the folder pane and select Properties. On the
Servers tab, select My server requires authentication. Click Work offline and remove any unsent messages from the outbox (below the account folders in the folder pane). Compose a new test message and send it to yourself. Post any new error message in your reply.
