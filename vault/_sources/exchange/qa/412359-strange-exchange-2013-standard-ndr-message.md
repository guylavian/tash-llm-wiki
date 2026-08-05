---
title: "Strange Exchange 2013 Standard  NDR message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412359/strange-exchange-2013-standard-ndr-message
question_id: 412359
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Strange Exchange 2013 Standard  NDR message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412359/strange-exchange-2013-standard-ndr-message (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our clients is running a single  Exchange 2013 Standard server. Everything is running fine except a handful of users sometimes get strange bounce messages.    

If they create a new email message using Outlook (2013, 2016 or 2019) they can send emails to external contacts without problems.  However, sometimes they send out a message and they immediately receive a bounce message that makes no sense and has no good information. The email bounces from an address unknown to us.     

 Here is an example:    

------------    

Undeliverable:  "Subject of email"    

Systemadministrator <IMCEASYSTEM-administrator@keyman  .com>    

Send:    Sa  26-05-2021  14:19    

To:    

Delivery has failed to these recipients or groups:    

'******@externaldomain.com'    

A problem occurred during the delivery of this message. Please try to resend the message later.    

Diagnostic information for administrators:    

Generating server:    

******@externaldomain.com    

Remote Server returned ''    

-------------    

That is all the message contains. No error information or anything. When they create a new email and resend the exact same message with or without attachments it goes out the door without any problems to the same recipient. This happens to just a few users within the company. This only happens sending outbound to external email addresses. Computers are Windows 10 with a mix of different Outlook versions.  Is this a known bug? I have found some online but no solution

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-01*

I have tried every message tracking option to find the messages but I cannot find any of them. All the other messages that were send that day are there to the message tracking on the server is working just fine. There is just no trace of these specific messages

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-28*

Hi,    

Search message tracking log on it, if you see it showing "SENDEXTERNAL", that would not be Exchange's problem, you should contact the company's IT guys:    

Use the Exchange Management Shell to search the message tracking logs    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-27*

I would wager that the external recipient is forwarding to another account that is rejecting it and that is what is bouncing back to the original sender.
