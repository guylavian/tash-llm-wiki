---
title: "MSExchange Common 6003"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1803024/msexchange-common-6003
question_id: 1803024
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchange Common 6003

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1803024/msexchange-common-6003 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Exchange 2016 on-premise.

Enterprise Version 15.1 (Build 2507.6)

I got error:

RpsCmdletLogs: Failed to create the log directory: C:\Program Files\Microsoft\Exchange Server\V15\Logging\CmdletInfra\LocalPowerShell\Cmdlet because of the error: Access to the path 'C:\Program Files\Microsoft\Exchange Server\V15\Logging\CmdletInfra' is denied.. Logs will not be generated until the problem is corrected.

I found something like this. https://support.microsoft.com/en-us/topic/fix-logs-will-not-be-generated-until-the-problem-is-corrected-error-in-an-exchange-server-2016-environment-26556396-1d4b-7e81-9a8d-9b0fcb6f4571

But it doesn't work for me. My CU: Exchange Server 2016 CU23 (2022H1)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-08*

Hi,

Thanks for posting your question in Microsoft Q&A Community.

I suggest you check if the Exchange Administrators group has “Full Control” permission. If not, add it.

-  Navigate to “C:\Program Files\Microsoft\Exchange Server\V15\Logging”.

-  Right-click the “CmdletInfra” directory and select “Properties”.

-  Go to the “Security” tab.

And it might be helpful to enforce inheritance of permissions to child directories.

In the Logging  “Security” tab, click “Advanced”. Make sure that the “Inheritance” is enabled for the parent directory (“Logging”).

Please feel free to contact me for any updates. And don't forget to mark it as an answer if this helps.
