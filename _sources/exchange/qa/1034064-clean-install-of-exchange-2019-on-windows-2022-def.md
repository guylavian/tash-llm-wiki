---
title: "Clean install of Exchange 2019 on Windows 2022 defaults to WAC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034064/clean-install-of-exchange-2019-on-windows-2022-def
question_id: 1034064
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Clean install of Exchange 2019 on Windows 2022 defaults to WAC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034064/clean-install-of-exchange-2019-on-windows-2022-def (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have just installed and patched Exchange 2019 onto a windows server 2022 server.  When I launch Exchange Admin center Windows admin center appears.  When i type in the ip and /ecp WAC still opens.  Any suggestions?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

I  uninstalled WAC rebooted and used solution # 7 listed here: https://www.stellarinfo.com/blog/exchange-server-http-500-error-ecp/    

The fact that this happens is really a crazy over sight.  WAC and Exchange should have better integration.  I hope this post helps others!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

My install was performed using the CU12 download which is listed as supported.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

Windows Server 2022 is officially listed as "not supported" for Exchange 2019 CU11 and earlier versions.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019
