---
title: "Nessus Says \"Web Server Generic XSS\" in Exchange 2016 (CU17) High Vulnerability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/270580/nessus-says-web-server-generic-xss-in-exchange-201
question_id: 270580
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Nessus Says "Web Server Generic XSS" in Exchange 2016 (CU17) High Vulnerability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/270580/nessus-says-web-server-generic-xss-in-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support,  

My Exchange Sever 2016 (CU17)  

When i run Nessus tool says that "Web Server Generic XSS"  

https://www.tenable.com/plugins/nessus/10815  

How to fix this issue without any impact

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-15*

Hi,@Sathishkumar Singh      

This warning indicates that your server may suffer from cross-site scripting attack.    

To fix it, you need to install the security updates on your server.    

While,this vulnerability should have already been fixed in the security update for Microsoft Exchange Server 2019 and 2016: March 10, 2020.    

If your current CU version is CU17, you might have installed the security updates as it is for Exchange CU14 and CU15.    

    

To confirm that you are using CU17, please run this command via EMS:    

```
Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion
```

Check if the results matches 15.1.2044.4.    

If you are on CU17, the problem may be with the Nessus tool.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
