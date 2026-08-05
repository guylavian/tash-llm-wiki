---
title: "Not able to add pc to domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/661533/not-able-to-add-pc-to-domain-controller
question_id: 661533
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Not able to add pc to domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/661533/not-able-to-add-pc-to-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently have installed DHCP, DNS, and ADDC controllers on windows server 2012.    

I can ping domain controller IP correctly, domain controller hostname correctly, but cannot ping the domain name, and thereby not allowing any pcs to join domain controller.    

Additional note, all above server services are running on the same server windows 2012    

please any one with the knowledge to this kind may kindly respond me  here

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-13*

Hello @sonamttobden       

If your DNS is working properly, the most obvious reason would be that whatever device your pinging from is not referencing that DNS server. If it is, then the DNS server must not be working properly.    

You give few details. Is this Windows? Try nslookup and see what DNS server you are using. Also ipconfig to see what DNS servers are specified. Next step would be to see if you can actually reach the DNS server itself and if it can talk back.     

Hope this helps with your query,    

---------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-13*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
