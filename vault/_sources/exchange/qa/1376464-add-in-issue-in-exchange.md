---
title: "Add-in issue in Exchange."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1376464/add-in-issue-in-exchange
question_id: 1376464
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Add-in issue in Exchange.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1376464/add-in-issue-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Getting below error while accessing Add-ins under organization in Exchange on prim console.

Method not found: 'Microsoft.Exchange.WebServices.Data.GetClientExtensionResponse Microsoft.Exchange.WebServices.Data.ExchangeService.GetClientExtension(Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean, System.String, Microsoft.Exchange.WebServices.Data.StringList, Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean)'.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-27*

Hi @Microsoft Q & A ,

Is it a suddenly occurred issue? If so, have you made any changes to the Exchange organization right prior to the occurrence of this issue?

Please run the command below to check the service status on the server and see if there's any service needs to be started:

```
Test-servicehealth -server 
```

It's also recommended to run the HealthChecker script to check if the Exchange server is missing any CU or SUs. 

In case the error persists, I'd suggest also having a look at the Event Viewer and see if there's any potentially relevant event recorded out there.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
