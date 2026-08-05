---
title: "domain SYSVOL folder replication issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/424323/domain-sysvol-folder-replication-issue
question_id: 424323
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# domain SYSVOL folder replication issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/424323/domain-sysvol-folder-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have 3 DC as below details:  

-  Microsoft windows server2012 standard as root domain controller (DC01)  

-  Server 2012 R2 secondary domain controller (DC02)  

-  Server 2012 R2 secondary domain controller (DC03)  

we found that gpupdate command is giving error and some gpo are not replicating to DC02 and DC03 from DC01.  

Kindly assist us to fix this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Hi,  

Repadmin.exe examines AD replication status instead of file replication status, and file replication service is used for replicating SYSVOL on Domain Controllers and Distributed File System (DFS) shared folders.  

I suggest you refer to this troubleshooting link below to troubleshoot event 13568:  

Troubleshooting File Replication Service  

http://technet.microsoft.com/en-us/library/bb727056.aspx#EBAA  

If the issue still persists after you have gone through all troubleshooting steps, you can perform a non-authoritative store on the problematic Domain Controller to fix the issue:  

How to force an authoritative and non-authoritative synchronization for DFSR-replicated SYSVOL (like "D4/D2" for FRS)  

http://support.microsoft.com/kb/2218556  

How to rebuild the SYSVOL tree and its content in a domain  

http://support.microsoft.com/kb/315457  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Hi  

Do I have to stop FRS service on all DCs or only for DC01.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-07*

Looks like the Fortinet is badly broken so you may need to deal with that error. As to FRS you could try a nonauthoritative restore  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
