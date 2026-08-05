---
title: "Exchange Hybrid Wizard Error (413)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2202144/exchange-hybrid-wizard-error-413
question_id: 2202144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid Wizard Error (413)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2202144/exchange-hybrid-wizard-error-413 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

we are running into issues with the Hybrid Wizard. On the last point validation, we always getting the same error and dont know what to do, cuz it says the external server is responding with....

See Log attached.

2025.03.05 08:43:02.035 ERROR 10349 [Client=UX, Page=HybridConnectorInstall, Thread=8]                                        The connection to the server '6499703f-91f1-4369-a729-b40098fdd276.resource.mailboxmigration.his.msappproxy.net' could not be completed., The call to 'https://6499703f-91f1-4369-a729-b40098fdd276.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' failed. Error details: The remote server returned an unexpected response: (413) RequestEntityTooLarge.., The remote server returned an unexpected response: (413) RequestEntityTooLarge.                                       OriginalFailureType: ProtocolException, WellKnownException: MRSRemote None MRSRemote                                        Remote stack trace:                                       Remote trace:                                          at System.ServiceModel.Channels.HttpResponseMessageHelper.ValidateResponseStatusCode()                                          at System.ServiceModel.Channels.HttpResponseMessageHelper.ParseIncomingResponse(TimeoutHelper timeoutHelper)                                          at System.ServiceModel.Channels.HttpChannelFactory`1.HttpClientRequestChannel.HttpClientChannelAsyncRequest.ReceiveReplyAsync(TimeoutHelper timeoutHelper)                                          at System.ServiceModel.Channels.RequestChannel.RequestAsync(Message message, TimeSpan timeout)                                          at System.ServiceModel.Channels.ClientReliableChannelBinder`1.RequestAsync(Message message, TimeSpan timeout, MaskingMode maskingMode)                                          at System.ServiceModel.Channels.RequestReliableRequestor.OnRequestAsync(Message request, TimeSpan timeout, Boolean last)                                          at System.ServiceModel.Channels.ReliableRequestor.RequestAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.ClientReliableSession.OpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.ReliableRequestSessionChannel.OnOpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.ReliableRequestSessionChannel.OnOpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.CommunicationObject.OnOpenAsyncInternal(TimeSpan timeout)                                          at System.ServiceModel.Channels.CommunicationObject.System.ServiceModel.IAsyncCommunicationObject.OpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.ServiceChannel.OnOpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.CommunicationObject.OnOpenAsyncInternal(TimeSpan timeout)                                          at System.ServiceModel.Channels.CommunicationObject.System.ServiceModel.IAsyncCommunicationObject.OpenAsync(TimeSpan timeout)                                          at System.ServiceModel.Channels.ServiceChannel.CallOpenOnce.System.ServiceModel.Channels.ServiceChannel.ICallOnce.Call(ServiceChannel channel, TimeSpan timeout)                                          at System.ServiceModel.Channels.ServiceChannel.CallOnceManager.CallOnce(TimeSpan timeout, CallOnceManager cascade)                                          at System.ServiceModel.Channels.ServiceChannel.Call(String action, Boolean oneway, ProxyOperationRuntime operation, Object[] ins, Object[] outs, TimeSpan timeout)                                          at System.ServiceModel.Channels.ServiceChannelProxy.Invoke(MethodInfo targetMethod, Object[] args)                                          at generatedProxy_3.ExchangeVersionInformation(VersionInformation, VersionInformation&)                                          at Microsoft.Exchange.Connections.Common.WcfClientWithFaultHandling`2.<>c__DisplayClass4_0.<CallService>b__0() in \_\sources\dev\common\src\Connections\Common\WcfClientWithFaultHandling.cs:line 76                                          at Microsoft.Exchange.Net.WcfClientBase`1.CallService(Action serviceCall, String context)

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-07*

Hi,@Ella Taylor

Thanks for posting your question in the Microsoft Q&A forum.

It looks like you're encountering an error related to the size of a request when using the Hybrid Wizard, indicating the `RequestEntityTooLarge` error (HTTP status code 413). This typically means that the request payload exceeds the configured or allowed size limits on the server.

IIS has a limit for the size of the files users can upload to an application. If the file size exceeds the limit, the application will throw “Error in HTTP request, received HTTP status 413 (Request Entity Too Large)” error.

Regarding the problem of “Request Entity Too Large”, Microsoft has provided an official solution, you can refer to this link:https://techcommunity.microsoft.com/blog/iis-support-blog/solution-for-%e2%80%9crequest-entity-too-large%e2%80%9d-error/501134

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
