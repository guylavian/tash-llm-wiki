---
title: "Exchange 2016 CU 23/SU Update Build Mismatch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1016525/exchange-2016-cu-23-su-update-build-mismatch
question_id: 1016525
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU 23/SU Update Build Mismatch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1016525/exchange-2016-cu-23-su-update-build-mismatch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After updating to Exchange CU 23 and applying the Aug22SU the build number reported by the PowerShell command Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion is Build 2507.6 while one would expect to receive 2507.12.  Running the Get-Command Exsetup.exe | ForEach {$_.FileVersionInfo} provides the expected results.  Is this mismatch something we should be concerned about?

## Answers

_No answers on this thread._
