---
title: "How to get user ID by using exchangeguid? Exchange account issue."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664895/how-to-get-user-id-by-using-exchangeguid-exchange
question_id: 1664895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# How to get user ID by using exchangeguid? Exchange account issue.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664895/how-to-get-user-id-by-using-exchangeguid-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I have encountered an error in the Active Users tab from the Admin Microsoft portal:

Exchange: An unknown error has occurred. Refer to correlation ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.;

I have found the root cause which is as follows:

The value "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx" of property "ExchangeGuid" is used by another recipient object. Please specify a unique value.

What command I should use in order to obtain that other recipient object, most preferably its UPN or SAM account name? Where I should execute it, in the ExchangeOnline module via PowerShell or ExchangePowerShell in the on-premises Exchange server?

I am in hybrid environment with Azure and with on-premises server.

Best regards and thanks!

## Answers

_No answers on this thread._
