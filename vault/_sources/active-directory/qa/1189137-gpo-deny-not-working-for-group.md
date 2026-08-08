---
title: "GPO deny not working for group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189137/gpo-deny-not-working-for-group
question_id: 1189137
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO deny not working for group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189137/gpo-deny-not-working-for-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We want to deny a group policy for a group of computers.  If I add the computers individually to the delegation tab with deny read and deny apply, the group policy does not apply.  If I add an AD group with these computers as members, the policy still applies.

Is there a way to deny a group of computers from applying a GPO or do I have to add each computer manually?  Or maybe a better question is why does the deny work individually and not work at all for a group?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-13*

Hi @JustAnotherUser  

Did you try clear kerberos ticket in the cache by restarting computer ?

When you add or remove user or computer from a AD group , you should clear kerberos ticket in the cache to be taken in account.

Please don't forget to mark helpful answer as accepted
