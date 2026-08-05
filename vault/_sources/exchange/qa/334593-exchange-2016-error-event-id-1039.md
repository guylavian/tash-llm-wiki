---
title: "Exchange 2016 Error event ID 1039"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334593/exchange-2016-error-event-id-1039
question_id: 334593
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 Error event ID 1039

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334593/exchange-2016-error-event-id-1039 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using Remote Connectivity Analzer and my Exchange EWS test failed:

Exchange Web Services service account access verificationThe Microsoft Connectivity Analyzer failed to complete all tests with the service account.  

Test Steps  

  

The Microsoft Connectivity Analyzer is attempting to test Autodiscover for user@keyman  .com.Autodiscover was tested successfully.  

Test Steps  

  

A new mail item is being created.The attempt to create a mail item failed.  

Additional Details  

Exception details:

Message: The request failed. The remote server returned an error: (403) Forbidden.

Type: Microsoft.Exchange.WebServices.Data.ServiceRequestException

Stack trace:

at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.GetEwsHttpWebResponse(IEwsHttpWebRequest request)

at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.ValidateAndEmitRequest(IEwsHttpWebRequest& request)

at Microsoft.Exchange.WebServices.Data.MultiResponseServiceRequest`1.Execute()

at Microsoft.Exchange.WebServices.Data.ExchangeService.InternalCreateItems(IEnumerable`1 items, FolderId parentFolderId, Nullable`1 messageDisposition, Nullable`1 sendInvitationsMode, ServiceErrorHandling errorHandling)

at Microsoft.Exchange.WebServices.Data.Item.InternalCreate(FolderId parentFolderId, Nullable`1 messageDisposition, Nullable`1 sendInvitationsMode)

at Microsoft.Exchange.WebServices.Data.Item.Save(FolderId parentFolderId)

at Microsoft.M365.RCA.ConnectivityTests.CreateItemTest.PerformTestReally()

Exception details:

Message: The remote server returned an error: (403) Forbidden.

Type: System.Net.WebException

Stack trace:

at System.Net.HttpWebRequest.GetResponse()

at Microsoft.Exchange.WebServices.Data.EwsHttpWebRequest.Microsoft.Exchange.WebServices.Data.IEwsHttpWebRequest.GetResponse()

at Microsoft.Exchange.WebServices.Data.ServiceRequestBase.GetEwsHttpWebResponse(IEwsHttpWebRequest request)

Request information:  

Request URL: https://<hidden ip>:443/https:/219.93.105.212/owa/  

Request path: /https:/<hidden ip>/owa/  

User host address: <hidden ip>  

User:  

Is authenticated: False  

Authentication Type:  

Thread account name: NT AUTHORITY\SYSTEM

Thread information:  

Thread ID: 26  

Thread account name: NT AUTHORITY\SYSTEM  

Is impersonating: False  

Stack trace: at System.Web.HttpRequest.ValidateInputIfRequiredByConfig()  

at System.Web.HttpApplication.PipelineStepManager.ValidateHelper(HttpContext context)

Custom event details:

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="ASP.NET 4.0.30319.0" />  

<EventID Qualifiers="32768">1309</EventID>  

<Level>3</Level>  

<Task>3</Task>  

<Keywords>0x80000000000000</Keywords>  

<TimeCreated SystemTime="2021-03-28T08:17:42.761924400Z" />  

<EventRecordID>155012</EventRecordID>  

<Channel>Application</Channel>  

<Computer><hidden></Computer>  

<Security />  

</System>  

<EventData>  

<Data>3005</Data>  

<Data>An unhandled exception has occurred.</Data>  

<Data>28/3/2021 4:17:42 PM</Data>  

<Data>28/3/2021 8:17:42 AM</Data>  

<Data>466059b1d1de499db9e947d6e68391ed</Data>  

<Data>2</Data>  

<Data>1</Data>  

<Data>0</Data>  

<Data>/LM/W3SVC/1/ROOT-3-132613921170228973</Data>  

<Data>Full</Data>  

<Data>/</Data>  

<Data>C:\inetpub\wwwroot\</Data>  

<Data>TTMMXS201</Data>  

<Data>  

</Data>  

<Data>24380</Data>  

<Data>w3wp.exe</Data>  

<Data>NT AUTHORITY\SYSTEM</Data>  

<Data>HttpException</Data>  

<Data>A potentially dangerous Request.Path value was detected from the client (:).  

at System.Web.HttpRequest.ValidateInputIfRequiredByConfig()  

at System.Web.HttpApplication.PipelineStepManager.ValidateHelper(HttpContext context)

</Data>  

<Data>https://<hidden ip>:443/https:/<hidden ip>/owa/</Data>  

<Data>/https:/<hidden ip>/owa/</Data>  

<Data><hidden ip></Data>  

<Data>  

</Data>  

<Data>False</Data>  

<Data>  

</Data>  

<Data>NT AUTHORITY\SYSTEM</Data>  

<Data>26</Data>  

<Data>NT AUTHORITY\SYSTEM</Data>  

<Data>False</Data>  

<Data> at System.Web.HttpRequest.ValidateInputIfRequiredByConfig()  

at System.Web.HttpApplication.PipelineStepManager.ValidateHelper(HttpContext context)  

</Data>  

</EventData>  

</Event>

Can anyone advice what could be the problem here?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-03-29*

Hi @CK Chun  ,    

Aside from the failed Exchange EWS test, may I know what specific issue you are encountering so that we can understand better about the situation?    

Besides, based on my experience, the "(403) Forbidden" included in the error is usually related to the authentication type, so it's suggested to have a look at the authentication settings of EWS via IIS Manager for both the frontend and Back End virtual directory. and then compare the result with the default settings in this link.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
