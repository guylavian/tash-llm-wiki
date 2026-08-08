---
title: "Exchange - Messages encoding error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/394418/exchange-messages-encoding-error
question_id: 394418
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange - Messages encoding error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/394418/exchange-messages-encoding-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,   

I have an external sender disclaimer message defined to my exchange users.   

This message is an HTML format code that is injected into the received message when the external to organization sender is verified.   

Some messages, mainly newsletters, are received with mismatched characters.   

After some investigations, I verify that some newsletters are predifined with charset UTF-8 encoding, and on this case, when message arrives from an external source, Exhange add the predifined warning message, and then encoding message with iso-8859-1. Once the message is injected, the original encoding UTF-8 is changed to iso-8859-, and a mismatch cahrset occours.   

In resume, at the end of this proccess, messages with original encoding UTF-8, they get mismach charateres, once the warning message is injected by Exchange and re-encode the original email with iso-8859-1.  

Does anyone with a similar error?

## Answers

_No answers on this thread._
