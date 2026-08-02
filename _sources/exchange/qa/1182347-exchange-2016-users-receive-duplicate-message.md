---
title: "Exchange 2016 users receive duplicate message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182347/exchange-2016-users-receive-duplicate-message
question_id: 1182347
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2016 users receive duplicate message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182347/exchange-2016-users-receive-duplicate-message (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dear experts, 

here is the problem:

1.one user sent a message on 09/02/2023 to 43 users and they all received the message.

-  all the the above 43 users received the same message again on 20/02/2023

what I have checked:

1.check the user mailbox and confirmed that he didn't send the message again. I checked sent items, deleted items, recoverableitems, only found message with the same subject sent on 09/02/2023

2.checked the message tracking log and found that the messageId of the them are different. Both of the two messages looks good in the log, there is no fail or differ related event in the tracking log. 

3.check the application log on the server, there is no email submition related info

I just wondering how the second message was generated and how can I check it further?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-10*

Hi,

I have excatly the same probleme, but the message id is different do u find a solution ?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-21*

Hi @xhope,

Could you share the message tracking logs of the two emails you got?

You can use the known message id and the following command to display the timestamps of the two emails under each event. If it is convenient to you, share the full log after hiding personal information, it will help us to check the sending time and transmission status of the two emails.

```
Get-MessageTrackingLog -MessageId  | Select-Object Timestamp,ServerHostname,ClientHostname,Source,EventId,Recipients | Sort-Object -Property Timestamp
```

Another idea is to check if there are third-party transport agents or virus scanners installed on the Exchange server, which in some cases also scan outgoing emails.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
