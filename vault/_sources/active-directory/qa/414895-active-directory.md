---
title: "Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/414895/active-directory
question_id: 414895
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/414895/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Kindly advice for the below issue  

I am using windows 2016 server getting below error in event viewer 1168   

Internal error: An Active Directory Domain Services error has occurred.   

Additional Data   

Error value (decimal):  

8995   

Error value (hex):  

2323   

Internal ID:  

1240628  

Internal ID:  

1240454  

Internal ID:  

124013b

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-03*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-31*

It seems to be AD database related issue.I would recommend to check the integrity of AD database and perfrom semantic database check.Also run chkdsk in read only mode to check for any error on drive and exclude the ntds/sysvol/ntfrs folder from AV scan.  

Reference link:  

http://support.microsoft.com/kb/826892/en-us  

http://support.microsoft.com/kb/315136  

http://technet.microsoft.com/en-us/library/cc961819.aspx  

Similar thread regarding the same  

http://social.technet.microsoft.com/Forums/en/winserverDS/thread/62394928-2c05-4589-aea4-dae472948005  

http://social.technet.microsoft.com/Forums/pl/winserverDS/thread/0ac81514-3fb0-4936-972e-0ae2d9c4474c  

Directory Services cannot start" error message when you start your Windows-based or SBS-based domain controller  

http://support.microsoft.com/kb/258062  

Hope this helps  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-30*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
