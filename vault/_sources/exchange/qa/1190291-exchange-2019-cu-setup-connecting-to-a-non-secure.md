---
title: "Exchange 2019 CU Setup connecting to a non secure endpoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190291/exchange-2019-cu-setup-connecting-to-a-non-secure
question_id: 1190291
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 CU Setup connecting to a non secure endpoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190291/exchange-2019-cu-setup-connecting-to-a-non-secure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a failed CU update and had to look at the setup log file. I found that setup is trying to connect to a strange MSN endpoint that's not even secure. Is this normal? And what's this endpoint supposed to do?

[09.07.2020 11:05:59.0506] [2] Beginning processing Write-ExchangeSetupLog 

[09.07.2020 11:05:59.0507] [2] Adding endpoint from variable RoleDatacenterServiceEndpointABCHContactService [09.07.2020 11:05:59.0508] 

[2] Ending processing Write-ExchangeSetupLog [09.07.2020 11:05:59.0550] 

[2] Beginning processing Write-ExchangeSetupLog [09.07.2020 11:05:59.0550] 

[2] Calling New-ServiceEndPoint for endpoint ABCHContactService with URL http://pvt-contacts.msn.com/abservice/abservice.asmx, URL template , Token  and certificate subject  [09.07.2020 11:05:59.0551] 

[2] Ending processing Write-ExchangeSetupLog

## Answers

_No answers on this thread._
