---
title: "Clients not loggin in to new Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/555525/clients-not-loggin-in-to-new-domain-controllers
question_id: 555525
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Clients not loggin in to new Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/555525/clients-not-loggin-in-to-new-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we had 3 Windows 2012 Domain Controllers serving many window 7 and windows 10 clients.  

I have created 2 more domain controllers recently and notice no users are logging in to new DCs. Even local Users to these DCs are logging in to remote location Domain controllers. new DCs are already added to AD Site & Services. How I can force users to logon local DCs ? is there any metrics I need to change OR How can I setup priority/weight in AD for these DCs to change logon priorities ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-16*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\dc4.txt`  

`ipconfig /all > C:\dc5.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-09-16*

Hi  

The local PC got what DNS listed ? Put the new server first into their PC to test out.  

Check too the DNS to be sure all DC are listed into your NS record for your domain.
