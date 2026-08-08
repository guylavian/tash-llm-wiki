---
title: "Question about on premise exchange to the cloud"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2155833/question-about-on-premise-exchange-to-the-cloud
question_id: 2155833
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Question about on premise exchange to the cloud

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2155833/question-about-on-premise-exchange-to-the-cloud (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I'm hosting an exchange server with 150 mailboxes with 20 different clients.

I've done in the past exchange migrations to 365 with minimal hybrid but it is out of the question here.

-  I cannot do AAD sync - because you cannot do it 20 times (20 clients)

-  Tried cutover, but it looks it will migrate all mailboxes at once.

Can I do a manual migration specifying a CSV without hybrid at all?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-10*

Hi,@sharon mutzafi

According to your description, you have multiple customers and need a more granular approach to migrate mailboxes to M365.

First I will analyze multiple migration methods:

1.Cutover Migration is designed for organizations where you want to move everyone at once. When running a Cutover Migration, Office 365 fetches every mailbox on that server/organization and you cannot selectively choose only a subset of mailboxes in this way.

2.When migrating using IMAP, you can provide a CSV file containing a list of mailboxes and credentials. This gives you fine-grained control over which mailboxes to migrate. However, IMAP migration extracts only emails. It does not migrate calendar items, contacts or other mailbox folders of the Exchange server. If your customers need their entire mailbox (email plus calendar/contacts), IMAP will not be a complete solution.

3.Hybrid migration provides complete mailbox movement (email, calendar, contacts, etc.) but requires a hybrid Exchange configuration. In your case, using 20 hybrid clients (each associated with AAD synchronization) is not feasible.

Therefore, you might consider exporting user mailboxes to a PST file and then extracting them to the target mailboxes. Given that you have 20 different clients to manage and you want granular control, the native migration options for Office 365 will be limited without a hybrid configuration.

Additionally, you can either turn to a third-party migration solution (which can be configured to use CSV file input to get an accurate list of mailboxes) or perform a PST-based migration for each client.

More information can be found CSV files for mailbox migration: Exchange 2013 Help | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
