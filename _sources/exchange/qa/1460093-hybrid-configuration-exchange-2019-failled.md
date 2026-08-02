---
title: "Hybrid Configuration Exchange 2019 failled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1460093/hybrid-configuration-exchange-2019-failled
question_id: 1460093
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Hybrid Configuration Exchange 2019 failled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1460093/hybrid-configuration-exchange-2019-failled (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community,

Hybrid configuration wizard on Exchange 2019 is not working for me. I selected Full Hybrid Configuration for Hybrid Features and Exchange Classic Hybrid Topology for Hybrid Topology. After I have completed the process, I get this error message and these logs. Can someone please help me.

thx

Regards

```
2023.1x.0x xx:xx:xx.xxx *ERROR* 10203 [Client=UX, Page=Configuring, fn=RunWorkflow, Thread=12] 
                                      System.NotImplementedException: Die Methode oder der Vorgang ist nicht implementiert.
                                         bei Microsoft.Online.CSE.Hybrid.Common.MSALAuthProvider.Result.Microsoft.Online.CSE.Hybrid.Common.Abstract.IAuthenticationResult.get_RefreshToken()
                                         bei Microsoft.Online.CSE.Hybrid.Common.BaseAuthCredential.GetAuthenticationResultFromCache(String authority, String resource, String clientId)
                                         bei Microsoft.Online.CSE.Hybrid.Common.BaseAuthCredential.AcquireToken(String authority, String resource, String clientId, Uri redirectUri, Boolean promptMode)
                                         bei Microsoft.Online.CSE.Hybrid.Provider.AdminApi.AdminApiProvider.Connect()
                                         bei Microsoft.Online.CSE.Hybrid.Host.Environment.CreateSession[T](ILogger logger, IPowerShellLogger psiLogger, ICredential credential, String powerShellHost)
                                         bei Microsoft.Online.CSE.Hybrid.App.AppData.CreateTenantSession()
                                         bei Microsoft.Online.CSE.Hybrid.App.AppData.RunWorkflow(ILogger logger, WorkflowType workflowType, IEngineUserInterface userInterface, Boolean postSessionData)
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-12-11*

Run this, and it’ll fix your problem:

https://techcommunity.microsoft.com/t5/exchange-team-blog/deprecation-of-remote-powershell-in-exchange-online-re-enabling/ba-p/3779692

Also, you can check this article for more insight - Testing a New Exchange Hybrid Configuration with Office 365

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-12-10*

Hi @Son2020 

Please take a look at this link , it should help you to fix the issue:

Modern HCW (Hybrid Agent): troubleshooting like a pro

Please don't forget to accept helpful answer
