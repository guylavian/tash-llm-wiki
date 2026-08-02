---
title: "Event id 37 Kerberos-Key-Distribution-Center (Windows 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/670128/event-id-37-kerberos-key-distribution-center-windo
question_id: 670128
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Event id 37 Kerberos-Key-Distribution-Center (Windows 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/670128/event-id-37-kerberos-key-distribution-center-windo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have some warnings, and everybody ask me to install updates over Windows Update catalog. But i can't do this, because  i have an error when i try to import Updates to my local WSUS.  

Tell me, please, another method  to install updates and remove warnings with id37 on my DC?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-21*

Patch all the domain controllers as first step then it looks like you may get one warning for every user.  

https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041  

Adds the new PAC to users who authenticated using an Active Directory domain controller that has the November 9, 2021 or later updates installed. When authenticating, if the user has the new PAC, the PAC is validated.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-21*

I already have this updates on my DС, but error is stil in event viewer  

Other solution?
