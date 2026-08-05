---
title: "OWA/ECP Exchange Server site error after configuring AD FS as an authentication method"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2132769/owa-ecp-exchange-server-site-error-after-configuri
question_id: 2132769
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-other-l1"]
---
# OWA/ECP Exchange Server site error after configuring AD FS as an authentication method

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2132769/owa-ecp-exchange-server-site-error-after-configuri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day! 

Given: 

Hyper-V VM running Windows Server 2022 

Exchange Server 2019 CU9 

is installed on it The SSL certificate is universal: *.chuc228.ru 

Addresses: 

https://mail.chuc228.ru/owa/ 

https://mail.chuc228.ru/ecp/ 

I have configured AD FS as an authentication method. After configuring and restarting the Web Server, the following error is displayed when logging in to the site, including localhost: 

Server error in the application '/owa'. 

Encryption certificate is absent 

Description: An unhandled exception when executing the current web request. Examine the stack trace for more information about this error and the code snippet that caused it. 

Information about the exception: Microsoft.Exchange.Security.Authentication.AdfsConfigurationException: Encryption certificate is absent 

Source error: An unhandled exception when executing the current web request. Information about the origin and location of the exception can be obtained using the following exception stack trace. 

Stack Tracing: [AdfsConfigurationException: Encryption certificate is absent] Microsoft.Exchange.Security.Authentication.Utility.GetCertificates() +3405252 Microsoft.Exchange.Security.Authentication.AdfsSessionSecurityTokenHandler.CreateTransforms() +13 Microsoft.Exchange.Security.Authentication.AdfsFederationAuthModule.FederatedAuthentication_ServiceConfigurationCreated(Object sender, ServiceConfigurationCreatedEventArgs e) +155 Microsoft.IdentityModel.Web.FederatedAuthentication.get_ServiceConfiguration() +184 Microsoft.IdentityModel.Web.HttpModuleBase.Init(HttpApplication context) +18 System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers) +587 System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context) +173 System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context) +255 System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext) +347 [HttpException (0x80004005): Encryption certificate is absent] System.Web.HttpRuntime.FirstRequestInit(HttpContext context) +552 System.Web.HttpRuntime.EnsureFirstRequestInit(HttpContext context) +122 System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context) +737 

Version Information: The Microsoft platform .NET Framework, version:4.0.30319; ASP.NET , version:4.8.4770.0 

I've tried everything: changing the certificate, and so on, nothing helps, everything is useless . 

I don't understand what kind of certificate he wants from me, there are several of them. 

I did it according to the instructions: Using authentication based on AD FS claims with Outlook Web App and the Exchange Administration Center | Microsoft Learn

## Answers

_No answers on this thread._
