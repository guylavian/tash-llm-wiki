---
title: "Exchange 2019 on Premise OOF not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1351592/exchange-2019-on-premise-oof-not-working
question_id: 1351592
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 on Premise OOF not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1351592/exchange-2019-on-premise-oof-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys,

On an Exchange 2019 with CU 13, out of office messages work internally but not externally (outside the organisation).

What could be the reason for this?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-13*

Hello Guys,

sorry for the delay.

The problem exists with all mailboxes.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-01*

Hi @Early Bird  ,

I have also disabled and re-enabled the OOF for the mailbox.

Does this issue only affect this particular mailbox? If this is the case, please run the command below to check the OOF message settings for this mailbox:

```
Get-Mailbox  | fl ExternalOofOptions
```

If the returned output is not "External", run the command below to change it, then disable and re-enable OOF for the mailbox to check the result.

```
Set-Mailbox   -ExternalOofOptions External
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-30*

I have already tested the OOF with different mail addresses and no OOF message is generated.

I have also disabled and re-enabled the OOF for the mailbox.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-08-25*

Check this official documentation: Understand and troubleshoot Out of Office (OOF) replies - Exchange | Microsoft Learn

This document mentions that if automatic replies are enabled, only one reply is sent to each sender, even if a recipient receives multiple messages from a sender. 

If you want to send a response to the sender every time instead of only one time, you can apply the "have server reply using a specific message" mailbox server-side rule instead of using the OOF rule. This alternative rule sends a response every time that a message is received.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-08-25*

Hi @Early Bird Rotary  

Please check if this helps you.  

https://learn.microsoft.com/en-us/answers/questions/1274688/ms-exchange-2019-out-of-office-reply-doesnt-work-f

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
