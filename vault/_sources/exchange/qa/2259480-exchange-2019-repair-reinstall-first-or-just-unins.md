---
title: "Exchange 2019 - repair reinstall first or just uninstall?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2259480/exchange-2019-repair-reinstall-first-or-just-unins
question_id: 2259480
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 - repair reinstall first or just uninstall?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2259480/exchange-2019-repair-reinstall-first-or-just-unins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019.

2 servers. 1 old and 1 new. Old server encountered an error where the filtering service would not start, meaning the transport service would not start.

The new server was then created, mailboxes were moved to the new server, and the old server was powered off.

I would like to decommission the old server. Should I do a repair install on a new box and then uninstall it or would a simple uninstall proceed without issue? 

ECP does load on the old server but takes 45 minutes until the filter service times out before it works, it has an older certificate compared to the new server now. 

Main goal is to decommission the old server without issue. Assuming everything is good on the new server since the new server works while the old one is powered off. 

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-21*

Hi @Susan Dodds  , 

Thank you for posting your question in the Microsoft Q&A forum.

Currently, we cannot sure that if any other issues on your old Exchange server and if they would affect the uninstallation. We can perform the following actions and try to decommission the old server directly.

Decommissioning Exchange Server 2013 | Microsoft Community Hub 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
