---
title: "Active Directory user unable to connect to computer connected to the domain."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/889308/active-directory-user-unable-to-connect-to-compute
question_id: 889308
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory user unable to connect to computer connected to the domain.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/889308/active-directory-user-unable-to-connect-to-compute (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

In one of the offices of our firm we are experiencing issues with I suppose the Domain Controller.     

On one of the computers User 1 is unable to sign in with their AD account on PC 1. User 2 has no issues logging in. At the same time User 1 has no issues logging in on PC 2. Not every computer in the office has this issue and not every AD user. All computers are connected in the same network and the same Domain. All users are Members Of the DomainUser group we have.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-15*

Hello    

Thank you for your question and reaching out. I can understand you are  having issues related  to  computers unable to connect to the domain.    

-  Please ensure on your User computers DNS ip should be of your Domain controller.    

-   Disable any Antivirus program or Windows firewall you may have for temporary purpose.    

-  Please verify date and time should  be same on Client and Domain controller.     

-  On your Domain controller make sure DNS service is running and DC ip should be static and not DHCP ip.    

------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-14*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log` <- run on any domain controller    

`repadmin /showrepl >C:\repl.txt` <- run on any domain controller    

`ipconfig /all > C:\dc1.txt` <- run on domain controller 1    

`ipconfig /all > C:\dc2.txt` <- run on domain controller 2    

`ipconfig /all > C:\dc3.txt` <- run on domain controller 3    

`ipconfig /all > C:\problemworkstation.txt` <- run on problem member    

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-14*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

`ipconfig /all > C:\dc3.txt`    

`ipconfig /all > C:\problemworkstation.txt`    

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-14*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
