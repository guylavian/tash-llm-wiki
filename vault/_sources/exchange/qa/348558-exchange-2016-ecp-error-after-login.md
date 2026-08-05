---
title: "Exchange 2016 ECP error after login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348558/exchange-2016-ecp-error-after-login
question_id: 348558
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 ECP error after login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348558/exchange-2016-ecp-error-after-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,  

My Exchange 2016 CU10 ECP have these error after login to the site.

Server Error in '/ecp' Application.  

Object reference not set to an instance of an object.  

Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.

Exception Details: System.NullReferenceException: Object reference not set to an instance of an object.

Source Error:

The source code that generated this unhandled exception can only be shown when compiled in debug mode. To enable this, please follow one of the below steps, then request the URL:

-   Add a "Debug=true" directive at the top of the file that generated the error. Example:    <%@ Page Language="C#" Debug="true" %>

or:

2) Add the following section to the configuration file of your application:

<configuration>  

<system.web>  

<compilation debug="true"/>  

</system.web>  

</configuration>

Note that this second technique will cause all files within a given application to be compiled in debug mode. The first technique will cause only that particular file to be compiled in debug mode.

Important: Running applications in debug mode does incur a memory/performance overhead. You should make sure that an application has debugging disabled before deploying into production scenario.

Stack Trace:

[NullReferenceException: Object reference not set to an instance of an object.]  

Microsoft.Exchange.Management.ControlPanel.Global..cctor() +119

[TypeInitializationException: The type initializer for 'Microsoft.Exchange.Management.ControlPanel.Global' threw an exception.]  

ASP.global_asax..ctor() +28

[TargetInvocationException: Exception has been thrown by the target of an invocation.]  

System.RuntimeTypeHandle.CreateInstance(RuntimeType type, Boolean publicOnly, Boolean noCheck, Boolean& canBeCached, RuntimeMethodHandleInternal& ctor, Boolean& bNeedSecurityCheck) +0  

System.RuntimeType.CreateInstanceSlow(Boolean publicOnly, Boolean skipCheckThis, Boolean fillCache, StackCrawlMark& stackMark) +142  

System.Activator.CreateInstance(Type type, Boolean nonPublic) +107  

System.RuntimeType.CreateInstanceImpl(BindingFlags bindingAttr, Binder binder, Object[] args, CultureInfo culture, Object[] activationAttributes, StackCrawlMark& stackMark) +1476  

System.Activator.CreateInstance(Type type, BindingFlags bindingAttr, Binder binder, Object[] args, CultureInfo culture, Object[] activationAttributes) +186  

System.Activator.CreateInstance(Type type, BindingFlags bindingAttr, Binder binder, Object[] args, CultureInfo culture) +28  

System.Web.HttpRuntime.CreateNonPublicInstance(Type type, Object[] args) +82  

System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context) +174  

System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext) +347

[HttpException (0x80004005): Exception has been thrown by the target of an invocation.]  

System.Web.HttpRuntime.FirstRequestInit(HttpContext context) +552  

System.Web.HttpRuntime.EnsureFirstRequestInit(HttpContext context) +122  

System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context) +737

Version Information: Microsoft .NET Framework Version:4.0.30319; ASP.NET Version:4.8.4210.0

Is there any fix or remediation for the issue.

Thanks.  

Azanne

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

Hi @Mohd Azrul Kusrin   ,  

Have you changed any setting of Exchange before this issue occurred?  

Could you login to OWA normally?  

1.What's the version of the .Net framework? Please note that Exchange 2016 CU10 only supports .NET Framework 4.7.1. Please refer to: Microsoft .NET Framework

2.Please try to restart the Exchange server and check the Service to make sure all services required by Exchange are running.

3.Please check the certificate setting in IIS for default website and backend site.  

  

4.Please run the "IISREST" in the CMD started as Administrator to reset the IIS.

5.Please run the following command to check the settings of ECP virtual directory:

```
Get-ECPVirtualDirectory | fl *url*,*auth*
```

In addition, are there have any related error log in the Event Viewer? If so, please sharing with us, and please pay attention to covering your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
