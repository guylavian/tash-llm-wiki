---
title: "\"Invalid OS\" during Readiness Check Exchange 2016 Upgrade to CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/174007/invalid-os-during-readiness-check-exchange-2016-up
question_id: 174007
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# "Invalid OS" during Readiness Check Exchange 2016 Upgrade to CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/174007/invalid-os-during-readiness-check-exchange-2016-up (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 CU18 (upgrade!) says: "No supported OS" .   

I have a "windows server 2016 standard edition" running. "WINVER" shows: Windows Server 2016 version 1607 (Build 14393.4046).   

According to Microsoft information it should be suited. On this server I have already an Exchange 2016 CU7 running whithout problems.  

Any idea ? Thanks in advance!  

Thomas

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-25*

Hi @Thomas Pfaff  ,    

According to Microsoft information it should be suited.     

Yes, according to Supported operating systems for Exchange 2016, it's supported to install Exchange 2016 CU3 or later on Windows Server 2016 Standard or Datacenter:    

    

Given current situation, please run the following command in either powershell or command prompt and check the version show at the Name field:    

```
slmgr -dli
```

    

Furthermore, it's suggested to go through the link below and make sure all the required prerequisites for Exchange 2016 have been installed at your end:    

Windows Server 2016 prerequisites for Exchange 2016    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
