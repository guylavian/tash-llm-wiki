---
title: "Active Directory Group Membership Change Auditing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189690/active-directory-group-membership-change-auditing
question_id: 2189690
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory Group Membership Change Auditing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189690/active-directory-group-membership-change-auditing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone.

I am trying to figure out how to audit where group changes are initiated in AD.  Auditing is enabled and aggregates in a SIEM.

When a change occurs I see this chain of event IDs:

4662 - An operation was performed on an object.

4732 - A member was added to a security-enabled local group.

4735 - A security-enabled local group was changed.

I can tell what domain controller is processing the change, and the credential used, but I cannot see the workstation / device triggering the change, only the DC processing the change.

My issue is that I am trying to track down where a benign script is running.

## Answers

_No answers on this thread._
