---
title: "incorrect password to my server1 domain controller/dns"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1420034/incorrect-password-to-my-server1-domain-controller
question_id: 1420034
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# incorrect password to my server1 domain controller/dns

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1420034/incorrect-password-to-my-server1-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there.

So i run few VM on my VMware and i have a domain with 2 controllers server1 and server2.  Before everything was great until now when i try to login to server1. I cant login since it says "password is incorrect" but im 100% sure its fine. And i realized that it accepts password only when second controller - server2 is on. Not even login but just turned on. 

do you know why it happens ? Maybe you have some ideas where to look for it ? Some kind of authentication ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-09*

Hello Kamil Wielgus,  

Thank you for posting in Q&A forum.  

1.Have you made any changes before the issue occurs? For example: Change the password or change the DNS setting or other changes?  

2.Which server is PDC (server1 or server2)?  

3.Are server1 and server2 both DNS server? If so, please check if the DNS server of server1 is itself and /or the IP address of server2.  

Please check AD replication between server1 and server2. Run commands below on PDC.  

repadmin /showrepl >C:\rep1.txt

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-11-08*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)   

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)   

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)   

then put `unzipped` text files up on OneDrive and share a link.
