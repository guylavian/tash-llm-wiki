---
title: "[Migrated from MSDN Exchange Dev]the dynamic distribution group is corrupted in an earlier version of exchange server management shell to change the filter"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130722/migrated-from-msdn-exchange-dev-the-dynamic-distri
question_id: 130722
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]the dynamic distribution group is corrupted in an earlier version of exchange server management shell to change the filter

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130722/migrated-from-msdn-exchange-dev-the-dynamic-distri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi  

I have getting this issue please resolve this issue has been very helpful for me  

the dynamic distribution group is corrupted in an earlier version of exchange server management shell to change the filter  

Regards  

Sn

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

Hi,    

Is the dynamic distribution group migrated from a lower version of Exchange to a new version of Exchange?    

Please run the following command to check this problematic dynamic distribution group:    

```
Get-DynamicDistributionGroup -Identity <> | fl *version*,*filter*
```

If the Exchange version is not 0.10 (14.0.100.0), please try to re-create a new dynamic distribution group and see if the issue is resolved.    

For more information: Create a dynamic distribution group    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
