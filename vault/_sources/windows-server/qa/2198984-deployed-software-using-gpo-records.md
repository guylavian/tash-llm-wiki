---
title: "Deployed Software Using GPO records"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198984/deployed-software-using-gpo-records
question_id: 2198984
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Deployed Software Using GPO records

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198984/deployed-software-using-gpo-records (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

We deployed Genian NAC from the GPO , During installation we found some users deployed Genian NAC successfully and some users failed to installed Genian NAC.

Now we need to install Genian NAC manually for that we need to users list which has successfully installed or which users failed to installed , is there any way to find these?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-19*

Dear Israr Ahmed,

did installation fail or not even occur? Because in the latter some users may have for some reason not have been included in the specific OU where the GPO has been linked to.

When it did fail; you could ask your users to run it and report back to you were they unsuccesfully. Or you would perhaps be able to see where the program connects centrally if it does so and then compare the connectivity to a list of all computers.

I will be around the coming couple of weeks to see and opinonate on what questions are brought here.
