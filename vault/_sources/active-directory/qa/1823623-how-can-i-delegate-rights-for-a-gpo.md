---
title: "How can I delegate rights for a GPO?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1823623/how-can-i-delegate-rights-for-a-gpo
question_id: 1823623
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How can I delegate rights for a GPO?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1823623/how-can-i-delegate-rights-for-a-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. 

How can I delegate to have a new group added here ?

Why I need it and what I'm trying to solve:

I'm looking into the AGPM service. I want to give a minimum of account rights. AGPM cannot control policies without domain administrator rights.

By default, we have no such rights. The documentation does not say anything about it. 

But if I manually add the permissions, everything is fine.

I found a solution, but it's using Powershell. We give each policy permissions. But if I create a new policy, I have to run this script every time to grant permissions to the new policy.

Can I do this using aduc GUI ? I don't really understand what parameters I need there. The Powershell solution has no automation and this would be hard to maintain.

https://archive.z-nerd.com/blog/2016/12/24-gpos-screw-it-well-do-it-live-iv/

## Answers

_No answers on this thread._
