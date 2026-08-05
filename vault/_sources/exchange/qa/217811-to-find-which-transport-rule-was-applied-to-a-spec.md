---
title: "to find which transport rule was applied to a specific message, Get-MessageTrackingLog returned no RuleID in EventData"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/217811/to-find-which-transport-rule-was-applied-to-a-spec
question_id: 217811
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# to find which transport rule was applied to a specific message, Get-MessageTrackingLog returned no RuleID in EventData

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/217811/to-find-which-transport-rule-was-applied-to-a-spec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,  

I need help to find which transport rule was applied to a specific message, the following Get-MessageTrackingLog returned but no RuleID in EventData field.  

Get-MessageTrackingLog -Start (Get-Date).AddDays(-2) -ResultSize Unlimited -EventId Fail | Where -Property Recipients -Like "******@mydomain.com" |FL  

EventData:  {[E2ELatency, 0.813], [DeliveryPriority, Normal], [AccountForest, mydomain.local]}  

what else can I do to find out which rule delete the email message?   

{[{LED=550 5.2.1 Message deleted by the transport rules agent};{MSG=};{FQDN=};{IP=};{LRT=}]}  

Thanks for your help!  

pingatwork

## Answers

_No answers on this thread._
