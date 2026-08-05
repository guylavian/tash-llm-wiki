---
title: "Intermittent NullReferenceException in EWS Nuget Package"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1833128/intermittent-nullreferenceexception-in-ews-nuget-p
question_id: 1833128
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Intermittent NullReferenceException in EWS Nuget Package

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1833128/intermittent-nullreferenceexception-in-ews-nuget-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

In my .NET application I use Microsoft.Exchange.WebServices 2.2.0 package to interact with the Exchange Server.

I create the ExchangeService class and call the method: 

Folder.Bind(exchangeService, WellKnownFolderName.Inbox). 

Most of the time the call is successful. But once in a while I am getting an exception: 

System.NullReferenceException: Object reference not set to an instance of an object. at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.WrapStream(Stream responseStream, String contentEncoding) at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.GetResponseStream(IEwsHttpWebResponse response) at Microsoft.Exchange.WebServices.Data.SimpleServiceRequestBase.ReadResponse(IEwsHttpWebResponse response) at Microsoft.Exchange.WebServices.Data.SimpleServiceRequestBase.InternalExecute() at Microsoft.Exchange.WebServices.Data.MultiResponseServiceRequest`1.Execute() at Microsoft.Exchange.WebServices.Data.ExchangeService.BindToFolder(FolderId folderId, PropertySet propertySet) at Microsoft.Exchange.WebServices.Data.ExchangeService.BindToFolder[TFolder] at Microsoft.Exchange.WebServices.Data.Folder.Bind(ExchangeService service, FolderId id, PropertySet propertySet) at Microsoft.Exchange.WebServices.Data.Folder.Bind(ExchangeService service, WellKnownFolderName name)...

The exception occurs sporadically.

Does anyone know how to tackle this issue?

Thank you in advance!

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-07-22*

I've found out how to resolve the problem. The solution was built on ASP.NET Core 3.1.

After updating to .NET 8.0 the exception was gone.

However, the same code in another application (WPF) with much older .NET version 4.6.1 works smoothly.

Hope this information will be helpful to somebody.
