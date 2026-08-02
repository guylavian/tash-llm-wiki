---
title: "Add a new server 2019 domain controller to an existing domain failed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/133551/add-a-new-server-2019-domain-controller-to-an-exis
question_id: 133551
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Add a new server 2019 domain controller to an existing domain failed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/133551/add-a-new-server-2019-domain-controller-to-an-exis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There are 3 server 2012R2 domain controllers, forest and domain function level both are 2012, FRS migrated to DFSR successfully.    

DC2 was demoted and removed from domain, then installed 2019 on it, everything seems normal untill excute adprep script step.    

33838-adprep.jpg    

33845-adprep.txt

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-22*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-22*

Also check the log file ADPrep.log in the C:\Windows\debug\adprep\logs\20201020184444 directory for more information.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-21*

Hi,    

Adprep requires access to existing domain-wide information from the infrastructure master in order to complete this operation.    

Following to the error above ,there is a issue to contact infrastructure master.     

Try to launch Adprep manually from CD installation of WIndows 2019 on the domain controller with infrastructure master role.    

```
#Prepare forest  
adprep /forestprep  
  
#Prepare domain  
  
adprep /domainprep
```

dd464018(v=ws.10)    

Please don't forget to mark this reply as answer if it help you to fix your issue
