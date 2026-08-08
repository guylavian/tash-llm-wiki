---
title: "Exchange Online Cutover Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1394360/exchange-online-cutover-migration
question_id: 1394360
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Online Cutover Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1394360/exchange-online-cutover-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

I am researching a cutover migration from exchange on premise to exchange online. I am trying to understand what happens after the migration batch has completed and the MX records updated to point to Exchange Online. Do the users need to have their mailboxes setup again in Outlook or will their existing mailbox seamlessly link to the Exchange Online mailbox?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-18*

Hi @ Ian，

I revisited the official documentation, which states that users must recreate outlook profiles to connect to M365 after completing the cutover migration.

 

 

Migrate email to Exchange Online using the Exchange cutover method in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-17*

Be sure to set the autodiscover record to  Exchange Online so any client can find the new mailbox location:

https://learn.microsoft.com/en-us/exchange/mailbox-migration/cutover-migration-to-office-365#complete-post-migration-tasks

However, there is no guarantee this will work seamlessly for all clients. Some may need to create new profiles to connect to the new mailbox
