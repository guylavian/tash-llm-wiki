---
title: "How to remove inactive Exchange Hybrid Agent if the local server does not exist anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1528526/how-to-remove-inactive-exchange-hybrid-agent-if-th
question_id: 1528526
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to remove inactive Exchange Hybrid Agent if the local server does not exist anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1528526/how-to-remove-inactive-exchange-hybrid-agent-if-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
i have the problem, that in our exchange hybrid environement there is an orphaned Exchange Hybrid Agent which i cannot remove. The agent is inactive because the old exchange server it belonged to does not exist anymore. Various tries with powershell show the problem:

Now when i try to remove the inactive agent with powershel, i get the 404 not found error:

The active agent is running on an Exchange 2016 server and is running fine. The inactive agent was running on an older Exchange version where the local server does not exist anymore. How can i remove the inactive agent?
Regards,
Jan

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-12*

Hi @Dowidat Jan  ,  

Please try using one of the following options and check if it can help:

-  Run the following `Remove-AzureADApplicationProxyApplication` command:

```
Remove-AzureADApplicationProxyApplication -ObjectId  -RemoveADApplication $true
```

-  Run the following command to get the application GUID, and then run the Remove-AzureADApplicationProxyApplication command to remove the application:

```
Get-AzureADServicePrincipal | where {$_.Tags -Contains "WindowsAzureActiveDirectoryOnPremApp"} | fl AppId, DisplayName
```

Reference: Can't register a Hybrid Agent in Exchange Server.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-02-11*

Hey @Dowidat Jan  
Have you tried the Remove-HybridConfiguration PowerShell cmdlet
Check out the below page for the reference
https://learn.microsoft.com/en-us/powershell/module/exchange/remove-hybridconfiguration?view=exchange-ps
