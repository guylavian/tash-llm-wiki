---
title: "Migrate  1K mailbox to 365 Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161831/migrate-1k-mailbox-to-365-exchange
question_id: 1161831
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrate  1K mailbox to 365 Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161831/migrate-1k-mailbox-to-365-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello , 

i have 1K mailbox working on-prmies with icewarp product  , we planing migrate to 365 , already user synced , already have license , and no issue to migrate mailboxes from IMAP to 365 , 

but the issue is that gab from currently email still receiving and if go to change mx record and full dns migrate will interrupted the company issues which it's critical ,  

is there any solution or recommendation to fill gab and migrate without lose any email or service interrupted while migration , like keep receiving and sending email for both environment until finish the migration 

 thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-20*

Hi S.zw, I am interest to know what was driving your decision to migrate from IceWarp. Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-19*

Please check this article for more insight - https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrating-imap-mailboxes

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-19*

Hi @S.zw，

Before you delete the migration batch, the source email system is synchronized with Microsoft 365 or Office 365.Therefore, you don't have to worry about losing messages after MX points to M365.

For more information, please refer to steps 5 and 6 in this link:

Migrate other types of IMAP mailboxes to Microsoft 365 or Office 365 | Microsoft Learn

Hope it helps you!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
