---
title: "Adding an Exchange Edge server, transferring transport rules and agents"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1363853/adding-an-exchange-edge-server-transferring-transp
question_id: 1363853
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Adding an Exchange Edge server, transferring transport rules and agents

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1363853/adding-an-exchange-edge-server-transferring-transp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. There are three Exchange servers 2019 in DAG. If I add Exchange Edge to the perimeter of the organization by setting up unidirectional synchronization with AD:

-  Should I (can I) disable all anti-spam agents running on one of the Mailbox servers (mail only went through it) and activate them all only on Edge? would it be more correct and rational?

-  A similar question about transport rules - can I transfer all the rules to Exchange Edge? or is it still better to leave the rules on Mailbox servers, and add them to Edge only if necessary (as for spam protection). If I understand, by setting up the rules on Mailbox, I get some kind of fault tolerance (if one mailbox fails, the rules will not be lost). Or should I transfer it to the Edge? Is it possible to use the rules both.

## Answers

_No answers on this thread._
