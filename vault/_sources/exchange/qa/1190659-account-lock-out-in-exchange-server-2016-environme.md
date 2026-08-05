---
title: "Account lock out in Exchange Server 2016 environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190659/account-lock-out-in-exchange-server-2016-environme
question_id: 1190659
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Account lock out in Exchange Server 2016 environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190659/account-lock-out-in-exchange-server-2016-environme (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Active Directory and Exchange Server 2016 DAG with 4 members 

Accounts are continuously locked out . When we try to find the error it gives the originating Name of traffic to Exchange Servers. Why this is happening and how it can be resolved

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-20*

Hi @azhar Nasim  ,

 

By research, there are many possible reasons for account lockout, to narrow the scope, please clarify the following confusion:

 

`“Accounts are continuously locked out”`

-  Is it that some specific accounts are locked out and there is no problem with other accounts?

 

`“When we try to find the error it gives the originating Name of traffic to Exchange Servers”`

-  Where you get this info and can you provide the detailed message of this?

 

Based on my experience, if they are some specific accounts, it may be related to mobile devices. You can check which devices are connected to the account through ActiveSync through the following command:

```
Get-ActiveSyncDeviceStatistics -Mailbox  |ft DeviceType， DeviceUserAgent， LastSuccesSync
```

 

Additionally, you can try to remove the local Windows credentials and see if the problem persists.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
