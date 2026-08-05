---
title: "Validating Hybrid Agent for Exchange usage fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1456943/validating-hybrid-agent-for-exchange-usage-fails
question_id: 1456943
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
---
# Validating Hybrid Agent for Exchange usage fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1456943/validating-hybrid-agent-for-exchange-usage-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I try to re-run the HCW because of changing certificates (Modern Hybrid) but at the Hybrid Setup page it gives an error at "Validating Hybrid Agent for Exchange usage".

And yes the credentials provided for the on-prem user are correct, and MRS is enabled on the EWS virtual directory.  

Sorry for the trouble, I have found what was wrong. It had to do with Extended Protection:  

https://learn.microsoft.com/nl-nl/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection?view=exchserver-2019#extended-protection-and-modern-hybrid-configuration

## Answers

_No answers on this thread._
