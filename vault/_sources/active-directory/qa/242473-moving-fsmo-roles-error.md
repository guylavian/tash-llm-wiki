---
title: "Moving FSMO roles Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/242473/moving-fsmo-roles-error
question_id: 242473
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Moving FSMO roles Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/242473/moving-fsmo-roles-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

I have active directory 2012r2 forest\ domain function level 2008r2, i added addition domain controller 2019 forest\ domain function level is 2008r2. i moved FSMO role "NTDSUTIL" to 2019 and i run netdom query fsmo and i moved to AD 2019. then i check FSMO role holder from ADSIEDIT but it still poitng to the old DC "2012r2", i tried to modified it manually but i got the following error:    

    

operation failed. error code 0x20ae the role owner could not be read.    

And i noticed that group policy management console is not opening. When i moved FSMO roles i used sizing command not transferred command.    

What else can i do to move FSMO roles with no error and demote the old DC.    

Thank You

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-28*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-27*

@Anonymous       

I moved FSMO role successfully. what i did is:    

1- I moved FSMO back to the old DC "2012r2"    

2- then i raised forest\ domain function level to 2012r    

3 then i forced replication    

4- then move FSMO to the new DC 2019 "again"    

5 but the FSMO role holder was still pointing to the old DC, so i change it manually    

6- then forced replication    

7- i demote the old DC

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-23*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
