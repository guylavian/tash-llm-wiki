---
title: "Users Cannot Connect Outlook 2021 to Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1804611/users-cannot-connect-outlook-2021-to-exchange-2019
question_id: 1804611
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Users Cannot Connect Outlook 2021 to Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1804611/users-cannot-connect-outlook-2021-to-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Every time a user tries to connect a new account to Outlook via Exchange, the following event occurs:  

SERVERNAME	3002	Error	MsExchange BackEndRehydration	Application	7/8/2024 9:55:11 AM  

Protocol /Autodiscover failed to process request from identity NT AUTHORITY\SYSTEM. Exception: System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceStaticConfig' threw an exception. ---> System.TypeInitializationException: The type initializer for 'Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceHelper' threw an exception. ---> System.OutOfMemoryException: Exception of type 'System.OutOfMemoryException' was thrown.

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.LiveIdBasicAuthenticationCountersInstance..ctor(String instanceName, LiveIdBasicAuthenticationCountersInstance autoUpdateTotalInstance)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.LiveIdBasicAuthenticationCounters.CreateInstance(String instanceName, PerformanceCounterInstance totalInstance)

   at Microsoft.Exchange.Diagnostics.PerformanceCounterMultipleInstance.GetInstance(String instanceName, PerformanceCounterInstance totalInstance)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.LiveIdBasicAuthenticationCounters.GetInstance(String instanceName)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceHelper..cctor()

   --- End of inner exception stack trace ---

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceHelper.get_PerformanceCounters()

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceStaticConfig..cctor()

   --- End of inner exception stack trace ---

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthServiceStaticConfig.get_Config()

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.CacheReader..ctor(ConfigWrapper authConfig, RootOrgContainerIdWrapper rootOrgWrapper)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.CacheReader.GetInstance(ConfigWrapper authConfig, RootOrgContainerIdWrapper rootOrgWrapper)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthPolicyRepo.GetUserPolicy(String userKey, Int32 traceId, Int32& userPolicy, HttpApplication httpApplication, IRecipientSession recipientSession, IConfigurationSession configSession, ConfigWrapper config, RootOrgContainerIdWrapper rootOrgWrapper)

   at Microsoft.Exchange.Security.Authentication.FederatedAuthService.AuthPolicyEvaluator.IsBasicAuthAllowed(String userKey, String protocolName, Int32 traceId, HttpApplication httpApplication, IRecipientSession recipientSession, IConfigurationSession configSession, ConfigWrapper config, RootOrgContainerIdWrapper rootOrgWrapper)

   at Microsoft.Exchange.Security.Authentication.BackendRehydrationModule.IsLegacyAuthAllowed(HttpContext httpContext)

   at Microsoft.Exchange.Security.Authentication.BackendRehydrationModule.OnAuthenticateRequest(Object source, EventArgs args).

Can someone please assist with what's going on? We haven't applied any new updates nor do we appear to be out of memory.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-09*

Hi,

Welcome to the Microsoft Q&A forum.

Typically, this issue occurs if Exchange Server computer is added to a group that's denied the user right. By default, the following groups are denied the user right:

-  Domain Admins

-  Schema Admins

-  Enterprise Admins

-  Organization Management

To resolve the issue, you can remove the Exchange Server computer from these groups. You can check this via running the following command:

`gpresult /scope computer /r`

Also, you can check and change the configuration in ADUC:

And restart the Exchange Server after removing.

Please feel free to contact me for any updates. And if this helps, don’t forget to mark it as an answer.
