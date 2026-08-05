---
title: "[Migrated from MSDN Exchange Dev]meta cache database (mcdb) Local Storage and SAN Storage??!!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/163871/migrated-from-msdn-exchange-dev-meta-cache-databas
question_id: 163871
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]meta cache database (mcdb) Local Storage and SAN Storage??!!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/163871/migrated-from-msdn-exchange-dev-meta-cache-databas (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Dears,  

Suppose I have 2 physical servers without SSD drives but I have SSD SAN disks, Can I use the new exchange 2019 feature meta cache database (mcdb) using SAN SSD Disks knowing that my physical exchange servers has no SSD disks?  

Thanks in advance  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

Hi ,    

Due to the limitations of the laboratory environment, I cannot directly test the applicable SSD SAN Disk to configure the MCDB function in Exchange 2019. But based on my research on official articles, the article clearly states that SSDs need to be used to set up, and each server needs to have the same number, same size and type of SSD. And we need to run the following command to set up the MCDB, so it's suggest you using the SSD to configure the MCDB.    

```
Manage-MCDB -DagName <> -ConfigureMCDBPrerequisite -SSDSizeInBytes <> -SSDCountPerServer <>
```

For more information you could refer to: MetaCacheDatabase (MCDB) setup    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
