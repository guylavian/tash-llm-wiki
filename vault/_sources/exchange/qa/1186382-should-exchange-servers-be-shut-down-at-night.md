---
title: "Should Exchange Servers be shut down at night"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186382/should-exchange-servers-be-shut-down-at-night
question_id: 1186382
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Should Exchange Servers be shut down at night

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186382/should-exchange-servers-be-shut-down-at-night (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are shutting down our Exchange servers in Azure at night to save money.  Should they be shut down or should they be left on to avoid possible corruption?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-03-04*

Hi

if you are going to shut the servers down every night, then you need to follow a defined shutdown procedure to ensure a graceful shutdown of Exchange Services. This will help ensure that there is no corruption in your databases. The thread here outlines the procedures:

https://learn.microsoft.com/en-us/answers/questions/549775/exchange-turn-off

The question for me though is around running Exchange Servers in Azure - is there any reason not to move to Exchange Online/Office365? This would take away the management overhead of the Exchange Servers and may also cost less money in the long run.

Hope this helps,

Thanks

Michael Durkan

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!
