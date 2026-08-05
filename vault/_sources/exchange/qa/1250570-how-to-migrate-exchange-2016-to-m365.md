---
title: "How to migrate exchange 2016 to M365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1250570/how-to-migrate-exchange-2016-to-m365
question_id: 1250570
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to migrate exchange 2016 to M365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1250570/how-to-migrate-exchange-2016-to-m365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have on-premise exchange 2016 server and I want to migrate it to office 365, I want to know the required checklist needed because this is my first time doing exchange migration.
Thanks,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-21*

Here are two decent articles for Exchange 2016 to M365 Migration - https://www.infosecurity-magazine.com/blogs/best-migration-exchange-office-365/
https://community.spiceworks.com/how_to/170553-exchange-migration-checklist-and-guide

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-21*

Hi @Ahmed Essam,
 

Microsoft 365 and Office 365 provide a mail migration advisor to help you move mailboxes from your current on-premises Exchange server to Exchange Online in Microsoft 365 and Office 365 with automated tools and step-by-step guidance.
Use the Microsoft 365 and Office 365 mail migration advisor | Microsoft Learn
 

Since you have Exchange 2016 server, if your on-premises Exchange organization has fewer than 2,000 mailboxes. you could use the cutover migration method.

Please note that if you have turned on directory synchronization, you need to turn it off before you can perform a cutover migration. You can do this by using PowerShell. For instructions, see Turn off directory synchronization.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
