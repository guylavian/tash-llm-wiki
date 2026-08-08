---
title: "Upgrade of Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2114268/upgrade-of-exchange-server-2016
question_id: 2114268
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Upgrade of Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2114268/upgrade-of-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear team,

I have the following scenario: 3 Exchange 2016 servers, with DAG configured. There is a plan to upgrade to Exchange 2019. Is it recommended to create new servers with 2019 version, migrate the mailboxes and then decommission the 2016 servers? Or an in-place upgrade is possible directly on the 2016 servers?

Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-05*

In-Place can be riskier because it might affect your entire setup, if something goes wrong during the upgrade.

Side-by-Side migration is generally the safer and more reliable approach. Follow the steps to do-

1.       Firstly, setup the new servers with Exchange 2019.

2.       By using the mailbox migration feature, move the mailboxes from the Exchange 2016 server to the new Exchange 2019 servers.

3.       Check the mail flow and client access.

4.       After this you can decommission the old Exchange 2016 servers.

Let me know if you any query in above steps.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-01*

In-place is not possible. You have build new servers and move the mailboxes to the new ones.

You can follow:

https://learn.microsoft.com/en-us/exchange/exchange-deployment-assistant?view=exchserver-2019
