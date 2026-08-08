---
title: "Public folders - Exchange server 2019 Extended Protection enabled in coexistence with Exchange server 2013 EP disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1571164/public-folders-exchange-server-2019-extended-prote
question_id: 1571164
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Public folders - Exchange server 2019 Extended Protection enabled in coexistence with Exchange server 2013 EP disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1571164/public-folders-exchange-server-2019-extended-prote (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of migrating to Exchange 2019 CU 14, from Exchange 2013 (yes I know but I am honest at least).

I am reading the Extended Protection part:
Extended Protection can't be enabled on Exchange Server 2013 servers with Public Folders in a coexistence environment

Extended Protection can't be enabled on Exchange Server 2013 servers with Public Folders in a coexistence environment> To enable Extended Protection on Exchange Server 2013, ensure that you don't have any Public Folders that are hosted on Exchange Server 2013. If you have coexistence of Exchange Server 2013 with Exchange Server 2016 or Exchange Server 2019, you must migrate your Public Folders to Exchange Server 2016 or Exchange Server 2019 before enabling Extended Protection. After Extended Protection was enabled and there are Public Folders on Exchange Server 2013, they'll no longer appear to end users!

It clearly states that by enabling EP on Exchange 2013, public folders will be no more available to end users. Ok.

What it is not clear to me is, what happens if during the coexistence and until I will not migrate the public folders I leave EP enabled on Exchange 2019 and disabled on exchange 2013? Will the PF reamain available?

Thank you,

## Answers

_No answers on this thread._
