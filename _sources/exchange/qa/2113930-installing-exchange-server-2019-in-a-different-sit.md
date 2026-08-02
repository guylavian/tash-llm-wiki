---
title: "Installing Exchange server 2019 in a different site but same Active directory domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2113930/installing-exchange-server-2019-in-a-different-sit
question_id: 2113930
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Installing Exchange server 2019 in a different site but same Active directory domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2113930/installing-exchange-server-2019-in-a-different-sit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Hyper-V VM installed Exchange Server 2016 CU23 in a hybrid setup on-prem which is, I'm trying install a Exchange Server 2019 on an Azure VM which is connect to our Active Directory domain, the schema master is on a DC located on our on-prem Hyper-V cluster. I've tried running setup specifying the /DomainController:<DomainControllerFQDN> switch but I'm still bumping into the same issue it keeps telling me the local computer isn't in the same domain and site, yes it not in the same site as the current Exchange server, but its definitely is in the same domain. If I move the schema master role to a DC in the Azure site would this get run this issue?

## Answers

_No answers on this thread._
