---
title: "Monitor PowerShell Exchange online limits"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/418965/monitor-powershell-exchange-online-limits
question_id: 418965
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "windows-business-windows-server-user-experience-powershell"]
---
# Monitor PowerShell Exchange online limits

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/418965/monitor-powershell-exchange-online-limits (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I'm trying to use PowerShell to extract large amount of data from Exchange Online.   

I'm using Get-MessageTrace cmdlet.   

As expected I started hitting limits and getting errors like this one:  

This operation exceeds the throttling budget for policy part 'LocalTime',  

policy value '6000000',  Budget type: 'PowerShell'.  Suggested backoff time  

299912 ms.  

Whilst the error is not a surprise I'd like to make sure I'm protected against this type of error and in order to do this and to scale the script dynamically I'd like to be able to monitor usage against existing quotas and suspend/resume the process when it approaches the limit.   

Is there a way to check current consumption of resources along with their limits?   

There's also a bonus question - is there a better was to extract email metadata from Exchange Online?   

(I'm interested in just a basic information like sender, recipient, subject, timestamp, etc.)  

Many Thanks,  

Lukasz

## Answers

_No answers on this thread._
