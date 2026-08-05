---
title: "Roles in Active Directory server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1080374/roles-in-active-directory-server-2019
question_id: 1080374
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Roles in Active Directory server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1080374/roles-in-active-directory-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I need to assign admins in our AD DC the needed roles e.g. admin1 can make and edit users ... but I can't find Administration In the Service Manager console to select and configure. Can anyone guide me how to get to this menu in Service Manager?    

Thanks,    

Kevin

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-11-08*

You can use Active Directory Users and Computers snap-in for this purpose. Found in Administrative Tools.  dsa.msc    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-08*

You can follow along here.    

https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/perf-test/rsat/rsat-configure-nonadmin#enable-non-administrator-rsat-use    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-11-08*

Hi    

You need to use the Active Directory Users and Computers applet.    

You can install it on their computer to manage the remote server if you install the RSAT tool.    

A small guide there
