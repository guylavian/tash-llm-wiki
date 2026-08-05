---
title: "Is it possivle to have a domain controller with an internal (domain CA) and external (Digicert) cert?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327801/is-it-possivle-to-have-a-domain-controller-with-an
question_id: 327801
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Is it possivle to have a domain controller with an internal (domain CA) and external (Digicert) cert?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327801/is-it-possivle-to-have-a-domain-controller-with-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Like the question says, is this possible? We are on a 2012 R2 functional level. And our domain is .local.  

If we import an external cert, will that overwrite the Domain cert all together? In which case, I would think that information would propagate out the all the devices. But I would also think that an external cert that is not .local would cause issues with trust in the domain?  

We have a vendor that wants to use ldaps for user permissions in their application. I'm trying to get all the info I can before I make any suggestions or decisions.  

Charles

## Answers

_No answers on this thread._
