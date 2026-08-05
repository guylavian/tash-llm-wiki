---
title: "Upgrade Exchange 2013 Standard from CU16 to CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310631/upgrade-exchange-2013-standard-from-cu16-to-cu23
question_id: 310631
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Upgrade Exchange 2013 Standard from CU16 to CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310631/upgrade-exchange-2013-standard-from-cu16-to-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to upgrade an Exchange 2013 Standard server from CU16 to CU23. Can I directly upgrade or do I need to do it in steps? How would I get the older CU's? My Exchange box has all roles on one server and I'm not doing any DAG's or anything complicated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi @Jeff Curtiss      

Yes, Andy has provided very complete steps to perform the upgrade.    

Each CU is a full installation of Exchange that includes all updates and changes from previous CUs. When installing a new Exchange server using the latest released CU, you don't need to install Exchange RTM or any previously released CU.    

.NET Framework 4.8 supports for Exchange 2013 CU23, you could just continue.     

Make sure you have meet all the Exchange 2013 prerequisites list in the official document    

And the guide here: Upgrade Exchange 2013 to the latest cumulative update or service pack    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
