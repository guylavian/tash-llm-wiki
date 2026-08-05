---
title: "[Migrated from MSDN Exchange Dev] Exchange Hybrid behavior"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144144/migrated-from-msdn-exchange-dev-exchange-hybrid-be
question_id: 144144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Exchange Hybrid behavior

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144144/migrated-from-msdn-exchange-dev-exchange-hybrid-be (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/dca8a26e-e645-4269-970e-2559e700de57/exchange-hybrid-behavior?forum=exchangesvrdevelopment   

MS articles suggest "mail disabling" an account in the Exchange Hybrid server will remove all exchange attributes, delete the mailbox, but retain the AD account that is in On-Prem AD. They also suggest this action removes the exchange online mailbox as well but this is not the case after testing.   

Shared mailbox is in cloud (migrated from on-prem).  In the exchange hybrid server i mail disable it and it removes the mbx listing from exchange on-prem but the corresponding mailbox in the cloud stays (although the PrimarySmtpAddress changes to an @onmicrosoft address).   

Is this behavior normal?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-29*

Does "mail disabling" mean Disable-RemoteMailbox?     

If it's convenient, please provide the article you referred to.    

Do you just want to remove the online mailbox?     

If so, we first need to remove the Exchange Online license for the mailbox. You can check this for more detail: Disable-RemoteMailbox Description.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
