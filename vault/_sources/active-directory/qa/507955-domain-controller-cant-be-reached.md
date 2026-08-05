---
title: "Domain Controller Can't Be Reached"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/507955/domain-controller-cant-be-reached
question_id: 507955
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Can't Be Reached

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/507955/domain-controller-cant-be-reached (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm working with two new servers, both have Windows Server 2019 Standard installed. The servers are being added into a work environment that's never had servers before. I installed ADDS and DNS to SERVER-01 then promoted it to the PDC. That seemed to go perfectly. I installed ADDS and DNS on SERVER-02, but then when I attempt to add SERVER-02 to the new domain and promote it to BDC, I get an error message that says, "Server can't be reached."  

I can ping SERVER-01 from SERVER-02, and ping SERVER-02 from SERVER-01.  

The servers are on the same subnet.  

SERVER-01 IP is 10.1.10.51.  

SERVER-02 IP is 10.1.10.55.  

I've tried turning off the Windows firewall but that doesn't help.  

Any thoughts on why I can't add SERVER-02 to the domain that resides on SERVER-01?  

Or why I can't promote SERVER-02 to a BDC?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-10*

Glad to hear, you're quite welcome.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-10*

@Anonymous  , that did the trick!!!!!  Thank you, thank you, THANK YOU!!! I removed the public DNS and disabled IPV6,  ran the DNS and netlogon commands and then everything just worked!!!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-10*

@Anonymous  , thank you for your reply!!  Here's the link:    

https://1drv.ms/u/s!AgjYARWVQc2igidot29yVMycZcP4?e=Udefff

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-10*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
