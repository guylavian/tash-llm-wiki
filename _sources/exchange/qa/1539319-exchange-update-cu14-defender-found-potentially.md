---
title: "Exchange Update CU14, Defender found potentially"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1539319/exchange-update-cu14-defender-found-potentially
question_id: 1539319
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Update CU14, Defender found potentially

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1539319/exchange-update-cu14-defender-found-potentially (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

since update to CU14 Defender found potentially unwanted software.
Microsoft Defender Antivirus has detected malware or other potentially unwanted software.
https://go.microsoft.com/fwlink/?linkid=37020&name=Exploit:Script/ExchgProxyRequest.A!gen&threatid=2147834423&enterprise=0
                Name: Exploit:Script/ExchgProxyRequest.A!gen  

                ID: 2147834423  

                Severity: Severe  

                Category: Exploit  

                Path: amsi:_\Device\HarddiskVolume4\Windows\System32\inetsrv\w3wp.exe  

                Detection Origin: Unknown  

                Detection Type: Concrete  

                Detection Source: AMSI  

                User: NT AUTHORITY\SYSTEM  

                Process Name: C:\Windows\System32\inetsrv\w3wp.exe  

                Security intelligence Version: AV: 1.405.278.0, AS: 1.405.278.0, NIS: 1.405.278.0  

                Engine Version: AM: 1.1.24010.10, NIS: 1.1.24010.10

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-21*

Hi @Franky  ,

since update to CU14 Defender found potentially unwanted software.

Sounds might be related to CVE-2024-21410. Please follow the guidance in the blog to enable Extended Protection (EP) on Exchange 2019 servers:  

Released: 2024 H1 Cumulative Update for Exchange Server  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
