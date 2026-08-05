---
title: "move mailbox to new exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2134567/move-mailbox-to-new-exchange-server
question_id: 2134567
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# move mailbox to new exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2134567/move-mailbox-to-new-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,

now i have a dag with 2 exchange server 2016 (also windows is 2016).

next year with new server hardware i want to install new exchange server (the exchange version doesn't change) but i want to use windows 2022 or 2025.

so, i know that on windows cluster i can't mix different OS version, so how can i add on my exchange farm these new server, create new database and move the mailbox? obviously in the meantime the email routing must work on all servers (old and new)

thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-20*

Create a new DAG of the new version servers only.

Apply the certificates to the new servers with the correct subject names.

Set the autodiscover settings on the new servers to the valid URLs and SCP.

Recreate and custom receive connectors on the new servers

Add the new servers to any send connectors

Ensure you can send mail from the new servers to the internet and to other internal mailboxes with a test mailbox. 

Then move the existing mailboxes to the new servers. 

Once all moves are complete and things are working, remove the mailbox servers from the old DAG, remove Exchange from the servers, delete the old DAG and you are done.
