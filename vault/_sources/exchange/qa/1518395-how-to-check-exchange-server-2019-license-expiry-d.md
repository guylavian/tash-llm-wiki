---
title: "How to check exchange server 2019 license expiry date."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1518395/how-to-check-exchange-server-2019-license-expiry-d
question_id: 1518395
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to check exchange server 2019 license expiry date.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1518395/how-to-check-exchange-server-2019-license-expiry-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Get-ExchangeServerAccessLicense with this command display below info.
Product Name License Name Unit Label
Get-ExchangeServer ExServer01 | Format-Table Edition,Trial
Mailbox Server Name  Edition.
wants to know the expiry date 
Thanks in Advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-30*

Hi @Mohammed Salem  ,

I understand that you're looking to check the expiration date of your Exchange Server 2019 license.

The good news is that Exchange Server, including Exchange Server 2019, has a perpetual license, which means that your license doesn't have an expiration date. However, it's worth noting that the trial version of Exchange Server is only valid for 180 days. If you plan on using the server for more than 180 days, you will need to enter a product key. Otherwise, the Exchange admin center (EAC) will start displaying reminders to enter a product key to license the server.
To check the licensing status of a specific Exchange server, run the following command in the Exchange Management Shell:
Get-ExchangeServer Ex19 | Format-Table Edition,Trial

This command will display the version and trial status of the Exchange server.

Alternatively, you could use the command Get-ExchangeServer -Identity EX19 | Format-List to retrieve details about the Exchange server named EX19.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-30*

Product Name License Name Unit Label 
Mailbox Server Name Edition.
