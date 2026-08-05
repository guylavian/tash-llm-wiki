---
title: "Meeting request logs for exchange 2016 and O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430948/meeting-request-logs-for-exchange-2016-and-o365
question_id: 430948
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Meeting request logs for exchange 2016 and O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430948/meeting-request-logs-for-exchange-2016-and-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Wondering if someone can help here.  I inherited an Exchange 2010 and something was put in place to forward all meetings to a Corporate calendar. As a result any time a new meeting is setup "corpcal" is invited as optional.  

I have since moved to a hybrid config and replaced the 2010 with 2016.  

I have been ask to remove the auto-forwarding or inviting of "corpcal". I cannot find a single rule that pertains to this on Exchange 2016 or EOL  

Hoping someone can point me in the right direction.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

anonymous user-5548    

To narrow down this phenomenon, I would confirm with you that:    

-  Whether this phenomenon occurs on all mailboxes?     

 If there phenomenon only occurs one mailbox, I think this phenomenon may caused by client configuration. If this phenomenon occurs on all mailboxes on your Exchange server, it may related with server side configuration.    

-  Was this company account added when the meeting was created or after the meeting was sent?    

 Check from the  "Sent Items" folder from the sender mailbox, If this company account show in it, it means this account was added from client side. If this account wasn't show in the Sent Items email, it means this account was added by server side configure.    

If this account was added from client side, it may added with calendar template, whether your organization use related configration.    

If this account was added from Exchange side, you can use command below to check "Recipients" changed from which step:    

```
Get-TransportService | Get-MessageTrackingLog -Sender "******@yourDomain.com" -MessageSubject "TestMeeting1234"
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
