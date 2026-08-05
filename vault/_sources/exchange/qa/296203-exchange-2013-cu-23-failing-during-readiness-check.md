---
title: "Exchange 2013 CU 23 failing during readiness checks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/296203/exchange-2013-cu-23-failing-during-readiness-check
question_id: 296203
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 CU 23 failing during readiness checks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/296203/exchange-2013-cu-23-failing-during-readiness-check (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have run prepschema and adprep, installation of CU23 fails every time during readiness checks (see attached picture)![73539-exchangecu23.png][1] [1]: /api/attachments/73539-exchangecu23.png?platform=QnA

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-03*

Hi @Ryan Wilderman   ,    

Based on my research, it looks like issue with WMI process on the Windows OS. Please perform a clean boot of the machine and try again. Also, you could try running sfc /scannow and uninstall unwanted software's. Also, try building windows with a new image or ISO if its a new installation.    

Make sure to meet the system requirements    

https://learn.microsoft.com/en-us/exchange/exchange-2013-system-requirements-exchange-2013-help#hardware    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
