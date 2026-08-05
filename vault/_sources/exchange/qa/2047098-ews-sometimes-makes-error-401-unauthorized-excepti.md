---
title: "EWS sometimes makes Error 401 Unauthorized exception"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2047098/ews-sometimes-makes-error-401-unauthorized-excepti
question_id: 2047098
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# EWS sometimes makes Error 401 Unauthorized exception

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2047098/ews-sometimes-makes-error-401-unauthorized-excepti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I'm working on an api with exchange web service (ews) to handle new accounts and activation emails for a website.

It's deployed and it works but not all the time !

Sometimes, can be many times per week, i have this exception

StackTrace: 

   at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.GetEwsHttpWebResponse(IEwsHttpWebRequest request)
   at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.ValidateAndEmitRequest(IEwsHttpWebRequest& request)
   at Microsoft.Exchange.WebServices.Data.SimpleServiceRequestBase.InternalExecute()
   at Microsoft.Exchange.WebServices.Data.MultiResponseServiceRequest`1.Execute()    at Microsoft.Exchange.WebServices.Data.ExchangeService.InternalFindFolders(IEnumerable`1 parentFolderIds, SearchFilter searchFilter, FolderView view, ServiceErrorHandling errorHandlingMode)
   at Microsoft.Exchange.WebServices.Data.ExchangeService.FindFolders(FolderId parentFolderId, FolderView view)

Message:

The request failed. The remote server returned an error: (401) Unauthorized.

Then my customers are stucked without the activation link. 

Can anyone help me understand how to avoid this exception that seems random for me ?

Regards,

Jean-Michel

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-12*

Well this site looks usefull to test the services, i'll try to understand more with that. 

Thanks
