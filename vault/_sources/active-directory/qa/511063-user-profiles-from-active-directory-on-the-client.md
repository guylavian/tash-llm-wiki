---
title: "User profiles from Active Directory on the client for offline login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/511063/user-profiles-from-active-directory-on-the-client
question_id: 511063
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# User profiles from Active Directory on the client for offline login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/511063/user-profiles-from-active-directory-on-the-client (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

How to transfer user data from Active Directory via VPN to the client computer to be able to log in to offline user data when there is no VPN connection? Thank you in advance :) Sorry for my English.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-08-12*

The user will likely need to make an active online logon in order to used cached logon.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-16*

If I log in to every user online, will I be able to log in to every cached user?  

For a given pc yes that's how it works. The cached credentials are on pc and do not roam with user.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-16*

If I log in to every user online, will I be able to log in to every cached user? Because from what I can see, I can only log in to the last user. Others have a message that the domain is offline. Can I get around this?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-13*

How to make it possible for other cached users   

Each user needs to have logged on once active online in order to used cached logon.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-13*

After the tests, if I log in online, after restarting I can log in only for the same user. How to make it possible for other cached users without being online?
