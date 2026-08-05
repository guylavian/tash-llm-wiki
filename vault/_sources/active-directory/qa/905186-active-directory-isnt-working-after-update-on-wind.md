---
title: "Active Directory isn't working after update on Windows Server 2016  2022/06"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/905186/active-directory-isnt-working-after-update-on-wind
question_id: 905186
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory isn't working after update on Windows Server 2016  2022/06

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/905186/active-directory-isnt-working-after-update-on-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recent updates are killed my Active Directory. These updates were normal: Security def. updates and a "summary" update for 2022.06. Since that, my AD is not working. Error codes are the following:    

13 VSS    

12292 VSS    

1030 Microsoft-Windows-GroupPolicy    

10016 Microsoft-Windows-DistributedCOM    

454 ESENT    

490 ESENT    

6038 Microsoft-Windows-LSA    

10154 MS-Windows-Windows Remote Management    

1014 MS-DNS Client Events    

How can I fix my server? It's a virtual WS2016

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-28*

Thank You for the help. Problem is solved by update removal.    

Have a nice day!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-27*

Ok, sounds good, Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

`ipconfig /all > C:\problemworkstation.txt`    

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-27*

Two VMs on a host machine: One DC and a data server with shared folders. Issues: the whole domain. ~150 users. Every authentication is off since AD Users and computers is EMPTY. I can't name the exact updates now bc I was busy with saving and now I'm not at the office. I'll check it tomorrow.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-27*

Any details? How many domain controllers? How many have issues? What updates were installed?
