---
title: "Exchange 2019 CU9 Search not working (clean install)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/364485/exchange-2019-cu9-search-not-working-clean-install
question_id: 364485
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 CU9 Search not working (clean install)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/364485/exchange-2019-cu9-search-not-working-clean-install (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have clean install of Exchange2019 CU9 also with KB5001779 installed. All OS updates, system is uptodate.  

Search in OWA not working. In log I can see ID 1006 with message I copied down.  

Another Exchange 2019 server with CU 8 installed is OK.  

Can somebody help ? (I found "C:\Users\All Users\Microsoft\Crypto\RSA" solution with restart services, but it damage certs trustionship after server reboot)  

Thank you !  

An operation attempted against a FAST endpoint exprienced an exception. This operation may be retried. Error details: Microsoft.Exchange.Search.Fast.PerformingFastOperationException: An Exception was received during a FAST operation. ---> System.ServiceModel.CommunicationObjectAbortedException: The communication object, System.ServiceModel.Channels.ServiceChannel, cannot be used for communication because it has been Aborted.  

Server stack trace:   

   at System.ServiceModel.Channels.CommunicationObject.ThrowIfDisposedOrNotOpen()  

   at System.ServiceModel.Channels.ServiceChannel.EnsureOpened(TimeSpan timeout)  

   at System.ServiceModel.Channels.ServiceChannel.Call(String action, Boolean oneway, ProxyOperationRuntime operation, Object[] ins, Object[] outs, TimeSpan timeout)  

   at System.ServiceModel.Channels.ServiceChannelProxy.InvokeService(IMethodCallMessage methodCall, ProxyOperationRuntime operation)  

   at System.ServiceModel.Channels.ServiceChannelProxy.Invoke(IMessage message)  

Exception rethrown at [0]:   

   at System.Runtime.Remoting.Proxies.RealProxy.HandleReturnMessage(IMessage reqMsg, IMessage retMsg)  

   at System.Runtime.Remoting.Proxies.RealProxy.PrivateInvoke(MessageData& msgData, Int32 type)  

   at Microsoft.Ceres.ContentEngine.Admin.FlowService.IFlowServiceManagementAgent.GetFlows()  

   at Microsoft.Exchange.Search.Fast.FastManagementClient.PerformFastOperationTManagementAgent,TResult

## Answers

_No answers on this thread._
