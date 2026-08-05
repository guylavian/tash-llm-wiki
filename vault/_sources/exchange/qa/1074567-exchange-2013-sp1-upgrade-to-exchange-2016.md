---
title: "Exchange 2013 sp1 upgrade to Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074567/exchange-2013-sp1-upgrade-to-exchange-2016
question_id: 1074567
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 sp1 upgrade to Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074567/exchange-2013-sp1-upgrade-to-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a direct upgrade path from Exchange Server 2013 SP1 15.00.0847.032 to exchange 2016. Looking for some detailed steps on how to upgrade with the least amount of downtime.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-04*

Hi @Deen Uthman   ,    

You could use Exchange Deployment Assistant. It could help you evaluate your system and guide you through the steps.    

For upgrading from Exchange 2013 to Exchange 2016, we have to install Exchange 2016 firstly to coexist with Exchange 2013. After the configuration and testing in Exchange 2016, we can migrate mailboxes from Exchange 2013 to Exchange 2016.    

You need to consider the system requirements needed to install Exchange 2016 and Exchange Server prerequisites    

For details, you can refer to this case:    

https://social.technet.microsoft.com/Forums/en-US/04f7fcbd-b1cf-4ac5-bfad-168976a0b816/upgrade-exchange-2013-to-2016    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-04*

For detailed steps on migrating from Exchange 2013 to Exchange 2016, please follow the guide from Exchange Deployment Assistant.    

In general, you need first to install Exchange 2016, have it co-exist with Exchange 2013, then configure settings like SCP, DNS records, and virtual directory URLs to point to Exchange 2016 and migrate mailboxes.    

Consider removing the Exchange 2013 server if everything works fine after the migration.
