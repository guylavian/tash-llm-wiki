---
title: "MSExchange RBAC (258) and MSExchange RBAC (80) Errors Since CU23 Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368708/msexchange-rbac-258-and-msexchange-rbac-80-errors
question_id: 368708
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# MSExchange RBAC (258) and MSExchange RBAC (80) Errors Since CU23 Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368708/msexchange-rbac-258-and-msexchange-rbac-80-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

after installed CU 23  

Microsoft Exchange Service Host start and stop immediately

check eventlog had two error

First Error

記錄檔名稱: Application  

來源: MSExchange RBAC  

日期:  

事件識別碼: 80  

工作類別: RBAC  

層級: 錯誤  

關鍵字: 傳統  

使用者: 不適用  

電腦: mx.abc.com  

描述:  

(處理序 w3wp.exe，PID 8668)「Exchange AuthZPlugin 無法完成方法 GetApplicationPrivateData，因為發生嚴重錯誤: System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder' threw an exception. ---> System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries' threw an exception. ---> System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.MailboxReplicationService.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. 系統找不到指定的檔案。  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries.PopulateISSCmdletConfigurationEntries()  

--- End of inner exception stack trace ---  

at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)  

at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)  

at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)  

at System.Reflection.MethodBase.Invoke(Object obj, Object[] parameters)  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder.Build(List`1 allCmdlets, List`1 allScripts, ExchangeRunspaceConfiguration runspaceConfig)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeRunspaceConfiguration.CreateInitialSessionState()  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.GetInitialSessionStateCore(PSSenderInfo senderInfo)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.<>c__DisplayClass4.<GetApplicationPrivateData>b__3()  

at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.HandleExceptionAndRetry[T](String methodName, Func`1 func, Boolean throwException, T defaultReturnValue)。」 事件 Xml: <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">   <System>     <Provider Name="MSExchange RBAC" />     <EventID Qualifiers="49152">80</EventID>     <Level>2</Level>     <Task>2</Task>     <Keywords>0x80000000000000</Keywords>     <TimeCreated SystemTime="2021-04-23T00:27:16.000000000Z" />     <EventRecordID>13897615</EventRecordID>     <Channel>Application</Channel>     <Computer>mx.abc.com</Computer>     <Security />   </System>   <EventData>     <Data>w3wp.exe</Data>     <Data>8668</Data>     <Data>GetApplicationPrivateData</Data>     <Data>System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder' threw an exception. ---&gt; System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---&gt; System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries' threw an exception. ---&gt; System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.MailboxReplicationService.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. 系統找不到指定的檔案。    at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries..cctor()    --- End of inner exception stack trace ---    at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries.PopulateISSCmdletConfigurationEntries()    --- End of inner exception stack trace ---    at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)    at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)    at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)    at System.Reflection.MethodBase.Invoke(Object obj, Object[] parameters)    at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder..cctor()    --- End of inner exception stack trace ---    at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder.Build(List`1 allCmdlets, List`1 allScripts, ExchangeRunspaceConfiguration runspaceConfig)    at Microsoft.Exchange.Configuration.Authorization.ExchangeRunspaceConfiguration.CreateInitialSessionState()    at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.GetInitialSessionStateCore(PSSenderInfo senderInfo)    at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.&lt;&gt;c__DisplayClass4.&lt;GetApplicationPrivateData&gt;b__3()    at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.HandleExceptionAndRetry[T](String methodName, Func`1 func, Boolean throwException, T defaultReturnValue)</Data>  

</EventData>

</Event>

Second Error

記錄檔名稱: Application  

來源: MSExchange RBAC  

日期: 2021/4/23 上午 08:27:16  

事件識別碼: 258  

工作類別: RBAC  

層級: 錯誤  

關鍵字: 傳統  

使用者: 不適用  

電腦: mx.abc.com.tw  

描述:  

(處理序 8668，PID w3wp.exe)「RemotePS 公用 API Func GetApplicationPrivateData throws Exception System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder' threw an exception. ---> System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries' threw an exception. ---> System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.MailboxReplicationService.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. 系統找不到指定的檔案。  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries.PopulateISSCmdletConfigurationEntries()  

--- End of inner exception stack trace ---  

at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)  

at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)  

at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)  

at System.Reflection.MethodBase.Invoke(Object obj, Object[] parameters)  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder.Build(List`1 allCmdlets, List`1 allScripts, ExchangeRunspaceConfiguration runspaceConfig)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeRunspaceConfiguration.CreateInitialSessionState()  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.GetInitialSessionStateCore(PSSenderInfo senderInfo)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.<>c__DisplayClass4.<GetApplicationPrivateData>b__3()  

at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.HandleExceptionAndRetry[T](String methodName, Func`1 func, Boolean throwException, T defaultReturnValue)    at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.<>c__DisplayClassc`1.<ExecuteWSManPluginAPI>b__8()  

at Microsoft.Exchange.Diagnostics.CmdletInfra.Diagnostics.ExecuteAndLog[T](String funcName, Boolean missionCritical, LatencyTracker latencyTracker, ExEventLog eventLog, EventTuple eventTuple, Trace tracer, IsExceptionInteresting isExceptionInteresting, Action`1 onError, T defaultReturnValue, Func`1 func). 失敗，發生例外狀況 %4。」  

事件 Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="MSExchange RBAC" />  

<EventID Qualifiers="49152">258</EventID>  

<Level>2</Level>  

<Task>2</Task>  

<Keywords>0x80000000000000</Keywords>  

<TimeCreated SystemTime="2021-04-23T00:27:16.000000000Z" />  

<EventRecordID>13897616</EventRecordID>  

<Channel>Application</Channel>  

<Computer>mx.abc.com.tw</Computer>  

<Security />  

</System>  

<EventData>  

<Data>8668</Data>  

<Data>w3wp.exe</Data>  

<Data>Func GetApplicationPrivateData throws Exception System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder' threw an exception. ---> System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries' threw an exception. ---> System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.MailboxReplicationService.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. 系統找不到指定的檔案。  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Management.PowerShell.CmdletConfigurationEntries.PopulateISSCmdletConfigurationEntries()  

--- End of inner exception stack trace ---  

at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)  

at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)  

at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)  

at System.Reflection.MethodBase.Invoke(Object obj, Object[] parameters)  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder..cctor()  

--- End of inner exception stack trace ---  

at Microsoft.Exchange.Configuration.Authorization.InitialSessionStateBuilder.Build(List`1 allCmdlets, List`1 allScripts, ExchangeRunspaceConfiguration runspaceConfig)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeRunspaceConfiguration.CreateInitialSessionState()  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.GetInitialSessionStateCore(PSSenderInfo senderInfo)  

at Microsoft.Exchange.Configuration.Authorization.ExchangeAuthorizationPlugin.<>c__DisplayClass4.<GetApplicationPrivateData>b__3()  

at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.HandleExceptionAndRetry[T](String methodName, Func`1 func, Boolean throwException, T defaultReturnValue)    at Microsoft.Exchange.Configuration.Authorization.AuthZLogHelper.&lt;&gt;c__DisplayClassc`1.<ExecuteWSManPluginAPI>b__8()  

at Microsoft.Exchange.Diagnostics.CmdletInfra.Diagnostics.ExecuteAndLog[T](String funcName, Boolean missionCritical, LatencyTracker latencyTracker, ExEventLog eventLog, EventTuple eventTuple, Trace tracer, IsExceptionInteresting isExceptionInteresting, Action`1 onError, T defaultReturnValue, Func`1 func).</Data>  

</EventData>

</Event>

How can i fix this issue  

Somebody Help Me . PLEASE!!!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

Hi @資訊室-林秉穎  

Is this a newly installed Exchange server or you upgrade from a previous CU version? Is there any error during the installation. Please check the ExchangeSetupLog as well.

Have you rebooted your server after the installation?

Refer to the introduction in official document for Microsoft Exchange Service Host

Which provides a host for several Exchange services. On internal server roles, this service is dependent upon the Microsoft Exchange Active Directory Topology service.

To resolve the issue not starting the MS Exchange service host, try the below steps as well:

-   Please check logon account for Microsoft Exchange Service Host.

-   Please restart Microsoft Exchange Active Directory Topology service and then try to restart Microsoft Exchange Service Host.

-   If your login account is correct, and you will still get an error after restarting the service, please try to delete and re-create the MS Exchange service host service.

1) Opening the Registry Editor window and navigate to: HKEY_LOCAL_MACHINE > SYSTEM > CurrentControlSet > Services, then find the service and right-click on it, click Export to save it.

2) Delete the service, run CMD as administrator and run sfc / scannow.

3) Restart your computer. Then, find the backup of the registry key you have saved, right-click on it and choose Merge.

4) Then start the service, and set the startup type to automatically.

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
