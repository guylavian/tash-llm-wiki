---
title: "Exchange 2019 CU15 On-Prem + ADFS Modern Auth: Outlook Desktop Client Fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5929843/exchange-2019-cu15-on-prem-adfs-modern-auth-outloo
question_id: 5929843
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU15 On-Prem + ADFS Modern Auth: Outlook Desktop Client Fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5929843/exchange-2019-cu15-on-prem-adfs-modern-auth-outloo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

We are configuring a pure on-premises Exchange 2019 CU15 environment to use Modern Authentication with a local ADFS server (not Office 365) using this link: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premisesWhen a user launches Outlook on a computer connected to a domain, the Outlook startup process is visible, and then a window appears with the message: “There is a problem with your account. Please try again later.”

However, if you try to log in to Outlook from a non-domain machine whether the corporate VPN is enabled or disabled a window appears redirecting you to ADFS, where you can enter your username and password. After that, Outlook loads successfully, and the connection status displays as “Bearer.”In other words, on the test machines both those within the domain and those outside the domain all the necessary registry settings have been configured using these commands:

```
New-Item -Path “HKLM:\SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains” -Force
(Get-Item HKLM:).OpenSubKey(“SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains”, $true).CreateSubKey(“https://your-ADFS-domain/”)
(Get-Item HKLM:).OpenSubKey(“SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains”, $true).CreateSubKey(“https://your-ADFS-domain”)
Set-ItemProperty -Path “HKCU:\SOFTWARE\Microsoft\Office\16.0\Common\Identity\” -Name “EnableExchangeOnPremModernAuth” -Value 1 -Type DWord
```

However, this only helped machines that are not in the domain.

For machines that are in the domain, the following keys were also added:

```
Set-ItemProperty -Path “HKCU:\SOFTWARE\Microsoft\Office\16.0\Common\Identity\” -Name “EnableExchangeOnPremModernAuth” -Value 1 -Type DWord
Set-ItemProperty -Path “HKCU:\SOFTWARE\Microsoft\Office\16.0\Common\Identity\” -Name “DisableAADWAM” -Value 0 -Type DWord
```

However, this did not help either.

An attempt was also made to re-register the broker using this command:

```
Add-AppxPackage -Register “$env:windir\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy\Appxmanifest.xml” -DisableDevelopmentMode -ForceApplicationShutdown
```

That didn’t help either.

As a result, we’ve reached a dead end and are asking for your help in trying to resolve this issue.

Thank you!

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2026-06-25*

Hello Aleksandr Aleksandr 

When launching Outlook on a domain-joined machine, does it fail before showing any ADFS login page, or does the ADFS prompt appear but then fail? To help narrow it down, please check the following in order:

1> On one affected machine, set these two registry keys:

```
PowerShellSet-ItemProperty -Path "HKCU:\Software\Microsoft\Exchange\" -Name "AlwaysUseMSOAuthForAutoDiscover" -Value 1 -Type DWord
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Office\16.0\Common\Identity\" -Name "EnableADAL" -Value 1 -Type DWord
```

Restart Outlook and test. Let me know if the behavior changes.

2> Please run the following commands on your Exchange server and share the output:

```
PowerShellGet-OrganizationConfig | fl OAuth2ClientProfileEnabled
Get-AuthServer | fl Name, Type, AuthMetadataUrl, IsDefaultAuthorizationEndpoint
Get-MapiVirtualDirectory | fl Server, *AuthenticationMethods*
Get-WebServicesVirtualDirectory | fl Server, *AuthenticationMethods*
```

We need to confirm:

-  OAuth2ClientProfileEnabled is $true

-  An AuthServer of type ADFS exists and is set as default

-  OAuth is listed in the authentication methods for MAPI and EWS

3> On your ADFS server, please verify:

-  The Relying Party Trust created for Outlook has proper claims rules (UPN or Email Address)

-  -The token-signing certificate is valid and not expired

-   Clients can reach the CRL distribution point of the token-signing certificate

4> If the above doesn’t help, please try:

-  Create a new Outlook profile on a failing machine and test.

-  Clear any cached credentials in Credential Manager related to your Exchange or ADFS server.

-  On the ADFS server, ensure Forms Authentication is also enabled under Service > Authentication Methods > Primary Authentication > Intranet as a fallback.

-  Recheck Outlook version, refer this section: https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premises?view=exchserver-2019#outlook-on-windows

Reference: https://learn.microsoft.com/en-us/answers/questions/5514248/problem-exchange-2019-cu15-modern-auth-through-on?page=1#answers

Hope this info helpful, looking forward to your reply.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
