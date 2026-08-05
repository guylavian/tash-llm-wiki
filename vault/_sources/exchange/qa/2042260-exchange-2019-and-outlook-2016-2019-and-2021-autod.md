---
title: "Exchange 2019 and Outlook 2016, 2019 and 2021 Autodiscover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2042260/exchange-2019-and-outlook-2016-2019-and-2021-autod
question_id: 2042260
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 and Outlook 2016, 2019 and 2021 Autodiscover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2042260/exchange-2019-and-outlook-2016-2019-and-2021-autod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Community,

I have Exchange 2019 CU12 running on Windows Server 2022. All my Outlook 2013 clients are able to autoconfigure their email profile through Autodiscover without any problem, however, my newer clients, Office 2016 and above, are prompted for credentials in order to configure their profile; however, even after providing credentials, I'm prompted again for credentials.

The Autodiscover URI is pointing to the rights URL. 

Can anyone advise why my Outlook 2013 works as they should, and new clients don't?

Thank you

b.l

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-06*

Hi Andy,

The following authentication is configured under Autodiscover:

InternalAuthenticationMethods : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth} ExternalAuthenticationMethods : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}

Thank you

b.l

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-06*

Dear Jake and Amit,

Firstly,, I would like to thank you both for your time and help, I have commented your posts.

I would like to add that I did another test with the Edge browser.

When I open try to open https://mail.XXX.XX/autodiscover/autodiscover.xml from a workgroup computer I'm receiving a successful login and the XML as it should, as shown below. However, when I try from a domain joined machine, I get constant prompt for password, even though the password is the right one.

Any idea why is this happening?

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-06*

There might be several possibilities that this issue you are facing.

Outlook 2016 and newer clients use Modern Authentication and if it is not enabled or configured properly on your Exchange server, it might be asking for credentials.

You can enable this by PowerShell command- Set-OrganizationConfig -OAuth2ClientProfileEnabled $true Check Virtual directory settings using PowerShell Get-AutodiscoverVirtualDirectory | FL InternalAuthenticationMethods,ExternalAuthenticationMethods Please feel free to ask any query. And if this helps, don't forget to mark it as an answer.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-06*

Hi @Bujar Lushta  ,

Welcome to the Microsoft Q&A platform!

It sounds like you’re experiencing a common issue with Autodiscover in Exchange 2019 CU12, especially with newer Outlook clients. Here are a few steps you can try to resolve this:

-  Check Autodiscover Settings: Ensure that the Autodiscover service is correctly configured and that the Service Connection Point (SCP) is pointing to the correct URL. You can verify this by running the `Test Email AutoConfiguration` tool in Outlook (hold down the CTRL key and right-click the Outlook icon).

-  Update Outlook Clients: Make sure that your Outlook 2016 and newer clients are fully updated. Sometimes, updates can resolve compatibility issues with Autodiscover.

-  Registry Settings: There might be a need to adjust some registry settings on the client machines. Specifically, you can try adding or modifying the `ExcludeExplicitO365Endpoint` DWORD value in the registry under `HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\AutoDiscover` and set it to `1`

-  Check Authentication Settings: Ensure that the authentication settings on your Exchange server are correctly configured. Sometimes, mismatched authentication settings can cause repeated credential prompts.

-  Recreate Autodiscover Virtual Directory: If the issue persists, you might need to recreate the Autodiscover virtual directory on your Exchange server. This can be done using the Exchange Management Shell with the following commands:

```
Remove-AutodiscoverVirtualDirectory -Identity "Autodiscover (Default Web Site)"
   New-AutodiscoverVirtualDirectory -WebSiteName "Default Web Site" -ExternalUrl "https://autodiscover.yourdomain.com/autodiscover/autodiscover.xml"
```

-  DNS Configuration: Verify that your DNS settings are correctly configured and that the Autodiscover DNS records are pointing to the correct IP address of your Exchange server.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
