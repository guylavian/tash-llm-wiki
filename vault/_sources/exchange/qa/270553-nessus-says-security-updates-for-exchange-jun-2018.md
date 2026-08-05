---
title: "Nessus Says \"Security Updates for Exchange (Jun 2018)\" in Exchange 2016 (CU17) High Vulnerability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/270553/nessus-says-security-updates-for-exchange-jun-2018
question_id: 270553
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Nessus Says "Security Updates for Exchange (Jun 2018)" in Exchange 2016 (CU17) High Vulnerability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/270553/nessus-says-security-updates-for-exchange-jun-2018 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

My Exchange Sever 2016 (CU17)  

When i run Nessus tool says that "Security Updates for Exchange (Jun 2018)"  

https://www.tenable.com/plugins/nessus/110642  

i was wondering when my Exchange Server is running 2016 CU17  

why does it appear in Nessus scan to install Exchange Old CUs?  

How to fix this issue to Nessus should not detect ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-15*

Hi @Sathishkumar Singh  ,    

According to this official document,  all previously released fixes for security and nonsecurity issues are included in Cumulative Update 17, so you can rest assured if the tool is asking to install earlier CUs:    

    

Regarding your concern about why the tool is asking to install old update, it's suggested to upgrade the tool to the latest version and see how it goes. If it persists, it'd be better to contact the Nessus support for further help.    

By the way, the most recent CU for Exchange 2016 is CU19, as is always highly recommended for all Exchange Server 2016 customers, you may consider applying the latest CU to make your Exchange server up-to-date.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
