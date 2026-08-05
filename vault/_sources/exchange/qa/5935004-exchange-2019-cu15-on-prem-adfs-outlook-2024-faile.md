---
title: "Exchange 2019 CU15 On-Prem + ADFS + Outlook 2024 Failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5935004/exchange-2019-cu15-on-prem-adfs-outlook-2024-faile
question_id: 5935004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU15 On-Prem + ADFS + Outlook 2024 Failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5935004/exchange-2019-cu15-on-prem-adfs-outlook-2024-faile (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

We are configuring a pure on-premises Exchange 2019 CU15 environment to use Modern Authentication with a local ADFS server (not Office 365) using this link: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premises  

When a user launches Outlook on a computer connected to a domain, the Outlook startup process is visible, and then a window appears with the message: “There is a problem with your account. Please try again later.”

However, if you try to log in to Outlook from a non-domain machine whether the corporate VPN is enabled or disabled a window appears redirecting you to ADFS, where you can enter your username and password. After that, Outlook loads successfully, and the connection status displays as “Bearer.”In other words, on the test machines both those within the domain and those outside the domain all the necessary registry settings have been configured.

However, I am seeing the following errors in the AAD logs on the test machine:

`Error: 0x80070002 `

`Exception of type ‘class DSRegException’ at AcquireTokenContext.cpp, line: 239, method: AcquireTokenContext::GetFallbackDomain.`

`Log: 0xcaac03f1 Failed to get the DC registration data. Cannot get the domain name.`

`Logged at AcquireTokenContext.cpp, line: 239, method: AcquireTokenContext::GetFallbackDomain.`

And immediately following this error is the following error:

`Error: 0xCAA9001F Integrated Windows authentication is supported only in the federation flow.`

`Exception of type ‘class Exception’ at AggregatedTokenRequest.cpp, line: 171, method: AggregatedTokenRequest::UseWindowsIntegratedAuth.`

`Logged at AggregatedTokenRequest.cpp, line: 173, method: AggregatedTokenRequest::UseWindowsIntegratedAuth.`

`Request: authority: https://login.microsoftonline.com/organizations, client: ``[Moderator note: personal info removed]``, redirect URI: ms-appx-web://Microsoft.AAD. BrokerPlugin/ecd6b820-32c2-49b6-98a6-444530e5a77a, resource: , correlation ID (request): ``[Moderator note: personal info removed]`

As I understand it, WAM assumes that I’m working in a cloud environment, even though I don’t have one at all.

In other words, the broker is trying to retrieve registration data but can’t because it can’t find the domain, even though the command `nltest /dsgetdc:my domain` shows that the domain information and so on are set up correctly.

The ``` dsregcmd /status``` command shows that the device has a status of ```DomainJoined:YES` ``.

However, Diagnostic Data shows the following error: 

`Failed to schedule Diagnostics Task. Error: 0x80041326`

It seems like the broker doesn't understand that I have my own ADFS, which it needs to contact to obtain a token, but it isn't doing that.

Has anyone else encountered a similar problem?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2026-07-01*

Please note that Q&A forum is a public platform, and moderators will modify the question to hide personal information in the description. Kindly ensure that you hide any personal or organizational information the next time you post an error or other details to protect personal data.

Hi @User9183  

Based on your description, I understand that you are deploying pure On-Premises Modern Authentication for Exchange Server 2019 CU15 with a local ADFS server (completely bypassing Office 365/Entra ID). The core issue is that domain-joined machines fail during the Outlook startup process with the error "There is a problem with your account," while non-domain machines work perfectly, prompting the user with the ADFS login page and successfully establishing a connection using a "Bearer" token.

The specific error 0xCAA9001F (Integrated Windows Authentication is supported only in the federation flow) typically indicates that Windows is attempting Integrated Windows Authentication (IWA) against Microsoft Entra ID (Azure AD), but the domain is not configured for cloud federation.

Since your environment is strictly on-premises, seeing a request directed toward `https://login.microsoftonline.com/organizations` suggests that the Windows Web Account Manager (WAM) / AAD Broker Plugin is intercepting the request on domain-joined machines before Outlook can execute the expected local ADFS OAuth flow.

Why the non-domain machines work:

-  They do not attempt silent Integrated Windows Authentication.

-  Outlook immediately falls back to prompting the user, successfully rendering the local ADFS login page.

-  ADFS issues the OAuth token, Exchange accepts it, and Outlook connects via "Bearer." This proves your core Exchange OAuth configuration is working.

Please check the following configurations:

-Verify ADFS Global Authentication Policy

Integrated Windows Authentication behavior inside the corporate network can sometimes conflict with what WAM expects during on-premises modern auth. Please run the following command on your ADFS server:

```
Get-AdfsGlobalAuthenticationPolicy
```

Compare your results with Microsoft's recommended configuration for pure on-premises modern auth. In many hybrid/on-prem modern auth scenarios, ensuring FormsAuthentication is enabled for both Intranet and Extranet helps bypass silent IWA failures that trigger the AAD broker.

-Verify Outlook Build and Windows Updates

According to Microsoft documentation for on-premises modern authentication, Outlook requires a specific supported build version to natively handle the ADFS OAuth flow without trying to route through Entra ID. Please verify that your test clients are running a supported version of Outlook. Ensure the clients have installed KB5023706 (or newer cumulative updates). This update includes critical fixes for how the Windows Web Account Manager interacts with non-cloud endpoints.

-Registry Check for MAPI/HTTP and Exchange Modern Auth

Even though you mentioned registry settings are applied, ensure that `DisableADALatopWAMOverride` or `EnableADAL` are not inadvertently forcing cloud lookups. For Outlook 2016/2019/365 Apps connecting to on-prem Exchange via ADFS, ensure that MAPI/HTTP is explicitly enabled and that Outlook is explicitly told to look for your internal endpoint.

Please check these items and let me know the results of the `Get-AdfsGlobalAuthenticationPolicy` command so we can dig deeper.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click ""Comment"".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
