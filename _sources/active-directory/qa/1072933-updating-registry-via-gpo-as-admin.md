---
title: "Updating registry via GPO as admin"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1072933/updating-registry-via-gpo-as-admin
question_id: 1072933
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Updating registry via GPO as admin

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1072933/updating-registry-via-gpo-as-admin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am looking for a way to import a registry setting as admin via GPO on Windows PCs.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-02*

GPO is not working. Even when I log into PC with an account that has admin access.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-02*

Since it under user, should the GPO still be signed to OU with PCs or does it need to be assigned to an user OU?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-02*

am trying to update a reg key under HKEY_CURRENT_USER    

Make sure the gpo applies to user and not the machine.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-02*

I have tried that, however the user logging in on the PC does not have admin access, so the registry does not get updated. I am trying to update a reg key under HKEY_CURRENT_USER

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-02*

You can follow along here.    

http://woshub.com/how-to-create-modify-and-delete-registry-keys-using-gpo/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
