---
title: "Duplicate Exchange 2016 Database No Longer Needed - but can't remove from EAC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1291535/duplicate-exchange-2016-database-no-longer-needed
question_id: 1291535
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Duplicate Exchange 2016 Database No Longer Needed - but can't remove from EAC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1291535/duplicate-exchange-2016-database-no-longer-needed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning.

We have had a Exchange 2010 hybird setup for a while.  Been working/planning on the migration to 2016.  (Last 2008R2 server remaining)

During the first attempt installing 2016 it didn't go as smooth as I hoped.  HyperV issues and the VM was gone.   Removed from AD, recreated the VM and continued with a fresh install.   Well now there is a lingering irrelevant Exchange 2016 database which I can't get rid of and I do need some guidance.

The new 2016 install / database is ready to go - before I update dns and move mailboxes I would love for this orphaned, irrelevant database to be gone.

TIA

Terry

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-25*

Andy I have followed similar articles using adsiedit.  I could not find the exchange server in question under CN=Microsoft Exchange.

Also that link is not opening up at this moment for me

Terry
