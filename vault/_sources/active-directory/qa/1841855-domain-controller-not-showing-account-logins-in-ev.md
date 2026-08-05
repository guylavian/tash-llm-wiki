---
title: "Domain Controller not showing account logins in Event Viewer (auditing enabled)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841855/domain-controller-not-showing-account-logins-in-ev
question_id: 1841855
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Domain Controller not showing account logins in Event Viewer (auditing enabled)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841855/domain-controller-not-showing-account-logins-in-ev (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have several sites, each of which has a GC domain controller in it. Replication seems to be working fine.

I want to audit account logons and failures, so I enabled Success and Failure for Account Logon Events in group policy, but it doesn't seem to be working (this was in the Default Domain Policy). I then went to enable it in the Domain Controller policy but it was already enabled there.

I'm not sure why it doesn't appear to be capturing the authentication events. I ran auditpol /get /category:* and the only auditing it shows active is under Account Management (Security Group Management and User Account Management)--all of the other things I have enabled in either the Default Domain Policy or the Domain Controller policy show as "No Auditing."

What else should I be looking at?

## Answers

_No answers on this thread._
