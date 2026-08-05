---
title: "Active Directory no internet access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/553051/active-directory-no-internet-access
question_id: 553051
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory no internet access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/553051/active-directory-no-internet-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, the problem is as follows, after a few days of not logging into the computer, the domain user loses access to the Internet and the domain administrator must log in to the computer to return Internet access. What to do?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-09-15*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-24*

@Anonymous       

Internet Work    

    

Internet don't work
