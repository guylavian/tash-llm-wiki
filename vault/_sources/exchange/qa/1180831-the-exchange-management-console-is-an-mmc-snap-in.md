---
title: "The exchange management console is an MMC snap-in that can perform most but not all exchange server 2016 administration using powershell. True of False?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180831/the-exchange-management-console-is-an-mmc-snap-in
question_id: 1180831
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# The exchange management console is an MMC snap-in that can perform most but not all exchange server 2016 administration using powershell. True of False?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180831/the-exchange-management-console-is-an-mmc-snap-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to find out the difference btw Micrisoft Managmnet Console uses the Powershell to perform exchange server 2016 administration.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-16*

Hi @Emeka Chukwukuba   ,

The Exchange admin center (EAC) is the web-based management console in Exchange Server that replaces the Exchange Management Console (EMC) and Exchange Control Panel (ECP) in Exchange 2010.

You can use the Exchange Management Shell to perform every task that's available in the Exchange graphical management tools, plus things that you can't do there (for example, bulk operations). In fact, when you do something in the Exchange admin center (EAC), the Exchange Control Panel (ECP), or the Exchange Management Console (EMC), it's the Exchange Management Shell that does the work behind the scenes.

For more information, please refer to follow link：

Exchange admin center in Exchange Server | Microsoft Learn

Exchange Server PowerShell (Exchange Management Shell) | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
