---
title: "How to fix mailbox server service down?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1601528/how-to-fix-mailbox-server-service-down
question_id: 1601528
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to fix mailbox server service down?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1601528/how-to-fix-mailbox-server-service-down (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-28*

Hi @Naomi Nilla,

Please have a check of the network connection between your Exchange server and your domain controllers and make sure there is no firewall or other devices blocking ports or requests.

Also make sure only the ip address of the domain controller is configured as the preferred DNS server on the Exchange server, the alternative DNS server is left blank.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
