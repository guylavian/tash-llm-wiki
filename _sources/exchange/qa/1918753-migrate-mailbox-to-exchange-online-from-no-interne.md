---
title: "Migrate mailbox to exchange online from no internet access AD site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1918753/migrate-mailbox-to-exchange-online-from-no-interne
question_id: 1918753
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrate mailbox to exchange online from no internet access AD site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1918753/migrate-mailbox-to-exchange-online-from-no-interne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 2 AD site, both sites have exchange server 2019 (no DAG) and mount different DB. The primary site has internet access but the secondary site didn't.

Now we plan to migrate mailbox to Exchange Online and will setup the Exchange Hybrid in primary site. When we migrate the mailbox in secondary site, can it migrate to EXO directly? Or we need to move the mailbox to primary site Exchange first?

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-22*

Hello, @Chong,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you want to migrate mailboxes in a secondary site which does not have Internet access. It will have some impact on the direct migration to Exchange Online .

Direct migration to EXO may be limited if the secondary site does not have Internet access. Migration to EXO usually requires a stable Internet connection. Here are some solutions to your problem:

1.You can migrate mailboxes from the secondary site to the Exchange server at the primary site, and then migrate from the primary site to EXO; this method ensures that all mailboxes are migrated over the primary site's Internet connection.

2.You can use migration tools provided by Microsoft, such as the Hybrid Configuration Wizard (HCW) or other third-party tools that support multi-location environments to perform the migration.

Please feel free to contact me if you have any queries. If my reply is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

Best,

Alex Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-20*

It should work without moving the mailbox to the primary site since its one Exch Org.
