---
title: "Exchange2016(CU18) Shared Mailbox mails are not receiving it"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301035/exchange2016-cu18-shared-mailbox-mails-are-not-rec
question_id: 301035
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange2016(CU18) Shared Mailbox mails are not receiving it

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301035/exchange2016-cu18-shared-mailbox-mails-are-not-rec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support,    

My Exchange Server 2016 (CU18) is running.    

Shared Mailbox mails are not receiving it. User Mailbox mails are working fine, Only Shared Mailbox not receiving it      

There is no NDR reports received.    

Below updates:-    

    

Please advise

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Hi,    

1 .Would you search the message tracking log and post the results with personal information covered:    

```
Get-MessageTrackingLog -ResultSize Unlimited -Start "3/28/2015 8:00AM" -End "3/28/2015 5:00PM" -Sender "******@contoso.com"|fl
```

2 .Do you mean all shared mailboxes in your Exchange server could not receive mails? When you create a new shared mailbox, same issue?    

3 . Go to EAC-Mail flow-rules and make sure no transport rules have affected the mails.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
