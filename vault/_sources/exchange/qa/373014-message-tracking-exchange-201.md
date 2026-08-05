---
title: "Message Tracking Exchange 201"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373014/message-tracking-exchange-201
question_id: 373014
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Message Tracking Exchange 201

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373014/message-tracking-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Message Tracking Exchange 2013    

I would like to get the number of emails sent by a user between November 2019 - April 2021. Unfortunately, the Exchange admin before had set the MessageTrackingLogMaxAge to 45 days. So when I run the command below, I only get logs in the last 45 days only.    

Get-MessageTrackingLog -ResultSize Unlimited -Start "11/19/2019 00:00:00" -End "04/05/2021 23:00:00" -Sender "user@keyman  .com" -EventID SEND    

Is there any way possible to get these logs or just get the number of emails sent by this user within that period. Appreciate any response

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-28*

Hi @Dennis Ratemo   ,    

As Andy said, the answer for both the questions is no.    

    

You may want to set a larger number for that value to avoid this:      

```
Set-TransportService Mailbox01 -MessageTrackingLogMaxAge 180.00:00:00
```

Also you could mark the reply that helped you out as an Accepted Answer to close this thread :)    

Regards,    

Lou
