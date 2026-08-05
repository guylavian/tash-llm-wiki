---
title: "Exclude several domain controller for Exchange 2019 servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/734667/exclude-several-domain-controller-for-exchange-201
question_id: 734667
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exclude several domain controller for Exchange 2019 servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/734667/exclude-several-domain-controller-for-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

Is that possible to exclude to use several dc, that we used on remote branch?   

Priority in srv records is not set, so all dc's are equal, but when one of exch server choose remote branch dc, he cannot process that much of work.  

Only thing, that i found, is use StaticExcludedDomainControllers in Set-ExchangeServer.   

Is that normal practice? Why exchange start of use such a remote dc?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-02-15*

Hi @Roman Havryliuk      

Yes, you could use the command to exclude DC.    

```
set-exchangeserver exchangesrv1.domain.com -StaticExcludedDomainControllers OldDc1,OldDC2
```

And the command below to determine which domain controller is used    

```
Get-ExchangeServer -Status | FL name,StaticDomain*,CurrentDomain*,Static*
```

Details: Set-ExchangeServer    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
