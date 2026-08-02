---
title: "Exchange: IMAP Migration without public mailserver (only locally accessible)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367703/exchange-imap-migration-without-public-mailserver
question_id: 1367703
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management"]
---
# Exchange: IMAP Migration without public mailserver (only locally accessible)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367703/exchange-imap-migration-without-public-mailserver (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to migrate emails from a linux IMAP mail server to exchange (365). However, this is not an easy task since the mail server is not available from outside the company (no public IP).

How mails are stored currently: Mail -> Public Mailserver -> transfer to local mailserver via POP3.

So there is no way to access mails from the outside. All mails will be directly transferred from the public mailserver to the local mailserver inside the company.

My question is if there is a possibility or tool to migrate the mails from inside the company to Microsoft 365 Exchange. Like the IMAPSYNC tool.

What I've tried: Copy/Sync all mails from inside the company to a public accessible mailserver. Then create the migration batch. However, this does not work since the public accessible mailserver does not have the same mailbox name. This will end in a MigrationRecipientNotFoundException error.  

Any ideas or workaround?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-13*

Update: Solved. You can migrate from another domains, you just need to fill out the .csv correctly. The first part needs to be the account on exchange side (destination), not the source
