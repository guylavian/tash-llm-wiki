---
title: "Groupwise to Exchange migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430584/groupwise-to-exchange-migration
question_id: 430584
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Groupwise to Exchange migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430584/groupwise-to-exchange-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of migrating my user mailboxes using imap migration. But I'm stuck on creating a CSV batch file. I'm trying to migrate mailboxes using admin credentials, but I cannot find how UserName column for a Micro Focus GroupWise system suppose to look like. Anyone know how I can do this? I already tried different solutions from this website:    

https://learn.microsoft.com/en-us/Exchange/mailbox-migration/migrating-imap-mailboxes/migrate-other-types-of-imap-mailboxes#UseAdminCredentials

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-06-11*

Hi @Patryk Kluczewski  ，    

I'm trying to migrate mailboxes using admin credentials, but I cannot find how UserName column for a Micro Focus GroupWise system suppose to look like.     

I tried searching around on the username format for Micro Focus GroupWise but hardly find useful information either. Given this situation, I'd recommend considering the alternative option as mentioned in the documentation you shared, that is, using the user credentials:     

"We provide the format used by Exchange, Dovecot, and Mirapoint IMAP servers. If your source email system isn't listed here and you don't know the correct format, you still have the option of resetting user passwords. Skip this task and go to Create the list of user mailboxes when you know the user passwords, or you'll reset the passwords."    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
