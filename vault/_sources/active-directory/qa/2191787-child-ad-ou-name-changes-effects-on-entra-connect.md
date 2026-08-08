---
title: "Child AD Ou name changes effects on Entra connect not synchronized"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191787/child-ad-ou-name-changes-effects-on-entra-connect
question_id: 2191787
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Child AD Ou name changes effects on Entra connect not synchronized

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191787/child-ad-ou-name-changes-effects-on-entra-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Child AD Ou name changes effects on Entra connect not synchronized

Hi

I have a question related to Entra connect and AD OU change.

So, we have an Entra connect in usage, and we are making some organizational branding changes, which is why we want to change the AD Ou names. So here are my worries.

As we have several Child AD Ou that we are not synchronizing to Entra for several reasons.

I am fully aware that with an AD Ou that is synchronized with Entra connect we need to reconfigure them after the name change and we have a plan for this. As we are a large organization it is not possible for now that we monitor the entra connect setting 24/7 if we do changes to the child ad ou as we operate 24/7.

Can somebody explain to me what is going to happen to the childadou that is not synchronized. If we rename them from ChildADOU1 example XChildADOUX1  they are suddenly synchronized with Entra connect?

Example setup:

AD Ou (Sync)

-          ChildADOU1  (No)

-          ChildADOU2 (Sync)

-          ChildADOU3 (No)

-          ChildADOU4 (Sync)

Explanation:

(Sync) = Synchronized with Entra connect (previously named Azure AD connect)

(NO) = Not Synchronized

Can I kindly have Microsoft documentation for this, that is specific for Child AD ou rename?

## Answers

_No answers on this thread._
