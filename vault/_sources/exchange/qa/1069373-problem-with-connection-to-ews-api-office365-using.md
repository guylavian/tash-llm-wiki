---
title: "Problem with connection to EWS API office365 using ews-java-api - HTTP/401"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1069373/problem-with-connection-to-ews-api-office365-using
question_id: 1069373
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Problem with connection to EWS API office365 using ews-java-api - HTTP/401

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1069373/problem-with-connection-to-ews-api-office365-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Referring to the topic I have a problem to connect to EWS API exposed by Office365 (https://outlook.office365.com/EWS/Exchange.asmx) using ews-java-api 2.0. Until Friday everything was fine, but today the server returns error 401. Is something changed in authorization or maybe java-ews-api is deprecated or is it an temporary service problem? Mailbox credentials is okay. Stack-trace below:    

Caused by: microsoft.exchange.webservices.data.core.exception.service.remote.ServiceRequestException: The request failed. The request failed. The remote server returned an error: (401)    

	at microsoft.exchange.webservices.data.core.request.SimpleServiceRequestBase.internalExecute(SimpleServiceRequestBase.java:74)    

	at microsoft.exchange.webservices.data.core.request.MultiResponseServiceRequest.execute(MultiResponseServiceRequest.java:158)    

	at microsoft.exchange.webservices.data.core.ExchangeService.bindToFolder(ExchangeService.java:504)    

	at microsoft.exchange.webservices.data.core.ExchangeService.bindToFolder(ExchangeService.java:523)    

	at microsoft.exchange.webservices.data.core.service.folder.Folder.bind(Folder.java:98)    

	at microsoft.exchange.webservices.data.core.service.folder.Folder.bind(Folder.java:147)    

	at org.apache.nifi.customprocessor.SensEWS.validateAndInitEWS(SensEWS.java:1296)    

	... 13 common frames omitted    

Caused by: microsoft.exchange.webservices.data.core.exception.service.remote.ServiceRequestException: The request failed. The remote server returned an error: (401)    

	at microsoft.exchange.webservices.data.core.request.ServiceRequestBase.validateAndEmitRequest(ServiceRequestBase.java:644)    

	at microsoft.exchange.webservices.data.core.request.SimpleServiceRequestBase.internalExecute(SimpleServiceRequestBase.java:62)    

	... 19 common frames omitted    

Caused by: microsoft.exchange.webservices.data.core.exception.http.HttpErrorException: The remote server returned an error: (401)    

	at microsoft.exchange.webservices.data.core.request.ServiceRequestBase.getEwsHttpWebResponse(ServiceRequestBase.java:723)    

	at microsoft.exchange.webservices.data.core.request.ServiceRequestBase.validateAndEmitRequest(ServiceRequestBase.java:639)    

	... 20 common frames omitted    

Best Regards,    

Kamil

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-01*

Have you modified the code to use oAuth, basic authentication had been depreciated https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online and is the most likely cause of the problem
