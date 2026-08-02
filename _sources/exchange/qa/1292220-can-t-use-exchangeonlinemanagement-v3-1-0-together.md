---
title: "Can’t use ExchangeOnlineManagement V3.1.0 together with Microsoft.Graph.Authentication V1.27.0 in powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1292220/can-t-use-exchangeonlinemanagement-v3-1-0-together
question_id: 1292220
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can’t use ExchangeOnlineManagement V3.1.0 together with Microsoft.Graph.Authentication V1.27.0 in powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1292220/can-t-use-exchangeonlinemanagement-v3-1-0-together (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can’t use ExchangeOnlineManagement V3.1.0 together with Microsoft.Graph.Authentication V1.27.0 in powershell

I’m having some trouble with using the ExchangeOnlineManagement V3.1.0 together with Microsoft.Graph.Authentication V1.27.0 in powershell. Both modules work perfectly independent from eachother, but when I want to use them both in the same script, the following error occurs:  

`“Could not load file or assembly 'System.IdentityModel.Tokens.Jwt, Version=6.22.1.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35'. Could not find or load a specific file. (0x80131621)”.`

The exception occurs when I try to use the following cmdlet from the ExchangeOnlineManagement v3.1.0 module:

`” Connect-ExchangeOnline -Organization $VerifiedDefaultDomain -AppId $AppId -Certificate $CertObject”`

As you can see, I am using app only authentication using certificates. This command does work with the 2.0.5 version of ExchangeOnlineManagement in combination with Microsoft.graph.authentication, but as soon as I try to use the 3.1.0 version of the  ExchangeOnlineManagement, it stops working.

I think there is an version conflict between the two assemblies, because when the error occurs, and I run this command:  

`“[System.AppDomain]::CurrentDomain.GetAssemblies() | Where-Object Location | Sort-Object -Property FullName | Select-Object -Property FullName, Location, GlobalAssemblyCache, IsFullyTrusted | Out-GridView”`  

then I can see that the version of 'System.IdentityModel.Tokens.Jwt that is actually used, is 5.6.0.0 but the ExchangeOnlineManagement 3.1.0 module requires 6.22.1.0.  

So what do we have now? We have 2 modules that both require different versions of the same code assembly in order for certificate authentication to work.

`ExchangeOnlineManagement V3.1.0 = System.IdentityModel.Tokens.Jwt V6.22.1.0`

`Microsoft.Graph V.1.27.0 = System.IdentityModel.Tokens.Jwt V5.6.0.0`

Ofcourse you can’t use both assemblies in the same environment, because the runtime wouldn’t know which one to use when. I think this is something that Microsoft should fix in their Microsoft.Graph.Authentication module. I believe they should update the System.IdentityModel.Tokens.Jwt assembly in their module.  

Can someone tell me how to fix this, or can Microsoft acknowledge this issue and confirm that they are working on it? Feel free to contact me!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-14*

I've just struck the same issue. The comments from the Graph team on Vincent's issue indicate that the ExchangeOnlineManagment module needs to isolate its dependencies into an Assembly Loading Context to prevent this issue.

How do we log an issue with the EXO module team?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-26*

Best open an issue over at Github for the Graph module (the Exchange module one is not open-sourced): https://github.com/microsoftgraph/msgraph-sdk-powershell/issues
