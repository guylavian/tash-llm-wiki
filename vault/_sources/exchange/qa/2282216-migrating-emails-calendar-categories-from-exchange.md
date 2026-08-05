---
title: "Migrating emails/calendar categories from Exchange On-prem to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2282216/migrating-emails-calendar-categories-from-exchange
question_id: 2282216
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Migrating emails/calendar categories from Exchange On-prem to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2282216/migrating-emails-calendar-categories-from-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi just a few things I need clarification on with migration in a hybrid environment:

-  When migrating will categories be migrated.

-  If I backup and restore the categories, will be everything be restored, for example:

If a meeting/email has a custom category for example 'Offshore', once the categories are restored, will the meeting/email with this custom category applied will be restored back to 'Offshore'?

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-10*

Hi @Raymond Brooks  , I agree with Jade-T and wanted to add that when migrating mailboxes from Exchange On-Premises to Exchange Online in a hybrid setup, categories (including custom ones like "Offshore") are migrated along with emails and calendar items. If a message or meeting had a category applied before the move, it will still have that category after migration.   

However, if the category list isn't visible in Outlook after the move, you can restore it, and the tagged items will correctly show their categories again. So yes, categories are preserved, and restoring the list ensures they display properly.  

You can go through this guide while migration.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
