---
title: "get Archive policy, and delete policy from EWS services api & graph Api"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191411/get-archive-policy-and-delete-policy-from-ews-serv
question_id: 1191411
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# get Archive policy, and delete policy from EWS services api & graph Api

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191411/get-archive-policy-and-delete-policy-from-ews-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After connecting to exchange online using powershell I am able to get result by using  

Get-EXOMailboxFolderStatistics <Identity> | FT DeletePolicy,ArchivePolicy,FolderPath  

need a way to find similar result from EWS service api for exchange online & from graphApi  

tried some of the ways but all are throwing error "The property ArchiveTag is valid only for Exchange Exchange2013 or later versions."

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-27*

For EWS   

get policy properties from Microsoft.Exchange.WebServices.Data.Folder object  

then map with Microsoft.Exchange.WebServices.Data.ExchangeService.GetUserRetentionPolicyTags().RetentionPolicyTags

```
userRetentationPolicyResponse = m_service.GetUserRetentionPolicyTags();
```

but to have these values we need to have object of Microsoft.Exchange.WebServices.Data.ExchangeService with requestedServerVersion greater then or equal Microsoft.Exchange.WebServices.Data.ExchangeVersion.Exchange2013_SP1

```
m_service = new ExchangeService(ExchangeVersion.Exchange2013_SP1);
```

and to get folders with those properties, we need to pass propertySets of needed properties while retrieving

```
propertySet = new PropertySet(
                ...,
                FolderSchema.ArchiveTag,
                FolderSchema.PolicyTag);
```
