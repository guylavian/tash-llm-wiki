---
title: "GPO issue apply on pc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2084559/gpo-issue-apply-on-pc
question_id: 2084559
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# GPO issue apply on pc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2084559/gpo-issue-apply-on-pc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have apply on the GPO for an OU, but it isn’t applying to users or computers. The dc is on windows server 2016 std with two domain controllers. The GPO is linked, and they’ve tried gpupdate with /force, but no changes are seen. The windows pc are win11 and win10. Please I need your help...

Event ID: 1058 Source: Group Policy Level: Error

The processing of Group Policy failed. Windows attempted to read the file \dcgroup\SysVol\dcgroup\Policies{PolicyGUID}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved.

Error: The network path was not found.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-10-03*

thank you for your answer it was a network issue
