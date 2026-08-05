---
title: "Backup recommendations for Exchange Server 2016 - What should be included and how to manage space?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1276405/backup-recommendations-for-exchange-server-2016-wh
question_id: 1276405
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Backup recommendations for Exchange Server 2016 - What should be included and how to manage space?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1276405/backup-recommendations-for-exchange-server-2016-wh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What backup strategy would you recommend for Exchange Server 2016, considering the large amount of space required for full database backups? Additionally, what essential data should be included in the backup? We are currently using Windows Server Backup for our Exchange Server backup needs.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-05*

Hello

Thank you for your question and reaching out.

Exchange Native Data Protection :

Exchange Native Data Protection is a notion that Microsoft's preferred design for Exchange Server 2016 and Exchange Server 2019 makes use of. Exchange Native Data Protection uses built-in Exchange features rather than backups to safeguard your mailbox data, though you are still able to use those functions and create backups. When deployed and configured properly, a number of capabilities in Exchange 2016 and Exchange 2019 can offer native data protection, obviating the need for manual data backups. 

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/disaster-recovery?view=exchserver-2019

https://techcommunity.microsoft.com/t5/exchange-team-blog/the-exchange-2016-preferred-architecture/ba-p/604024

--If the reply is helpful, please Upvote and Accept as answer--
