---
title: "disbale Network session enumeration by gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187330/disbale-network-session-enumeration-by-gpo
question_id: 1187330
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# disbale Network session enumeration by gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187330/disbale-network-session-enumeration-by-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;

Kindly i need the assistance  

By default, Windows computers allow any authenticated user to enumerate network sessions to it. Disabling Net Session Enumeration removes the capability for any user to enumerate net session info.

regards

Yazan MAhsal

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-07*

hi

thank you, i found this article is it correct or i need to use your solution.

https://answers.microsoft.com/en-us/windows/forum/all/network-session-enumeration/ecc80fd3-4584-4f6d-b20b-93cc82cdee28

thnaks

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-03-07*

@Yazan M. Mashal  check this GPO settings and test in a Dev/Test Environment before you implement on the prod env - https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares

Also there will be implications on the Domain Trusts so test accordingly.

Hope this helps.

JS

==

Please accept as answer and do a Thumbs-up to upvote this response if you are satisfied with the community help. Your upvote will be beneficial for the community users facing similar issues.
