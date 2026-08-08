---
title: "MS Exchange 2019 send delivery report to each email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189095/ms-exchange-2019-send-delivery-report-to-each-emai
question_id: 1189095
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MS Exchange 2019 send delivery report to each email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189095/ms-exchange-2019-send-delivery-report-to-each-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, my exchange server sends delivery reports to one of the admin accounts for any emails that come through even an external address.

How can I stop this behavior?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-03-14*

Hi @Sem Anikin  ,

 

I've had the same problem before. According to my experiment, in the EAC left panel, please locate compliance management>journal rules, check if the admin account in question is set as a Journaling mailbox in a journal rule. If yes, uncheck the rule or change the journaling mailbox to another mailbox instead and then try again.

 

Reference link: Journaling in Exchange Server | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-15*

Hi @Jarvis Sun-MSFT  , thanks for your reply. I have checked journal rules in EAC and with powershell. There is no rules in my configuration.

But when I created new journal rule and then disabled it, everythings become normal.
