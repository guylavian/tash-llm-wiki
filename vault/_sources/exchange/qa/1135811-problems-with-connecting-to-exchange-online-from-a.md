---
title: "Problems with connecting to Exchange Online from azure automation using managed identity."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1135811/problems-with-connecting-to-exchange-online-from-a
question_id: 1135811
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["azure-automation", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Problems with connecting to Exchange Online from azure automation using managed identity.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1135811/problems-with-connecting-to-exchange-online-from-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I would like to run from Azure Automation Get-UnifiedGroup.    

To do this I use code:    

```
Connect-ExchangeOnline -ManagedIdentity -Organization atlastechnicalab.onmicrosoft.com  
Get-UnifiedGroup
```

Unfortunately Connect-ExchangeOnline crashes with error ‘UnAuthorized’.    

To grant access to managed identity used by my Azure Automation I used code:    

```
Connect-MgGraph -Scopes RoleManagement.ReadWrite.Directory  
$RoleID = (Get-MgRoleManagementDirectoryRoleDefinition -Filter "DisplayName eq 'Exchange Administrator'").Id  
#$PrincipalId I take from my automation > identity > system assigned > object (principal) ID   
New-MgRoleManagementDirectoryRoleAssignment -PrincipalId $PrincipalId -RoleDefinitionId $RoleID -DirectoryScopeId "/"
```

I followed this guide to grant permissions and this guide to connect to Exchange Online.    

My runbook based on PS runtime v7.1 and use module ‘ExchangeOnlineManagement‘ 3.0.0 for runtime 7.1.    

Also, would be very thankful if someone can help to figure out minimal permissions, I need to grant to my Azure Automation to connect to Exchange Online and run command Get-UnifiedGroup.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-11*

Make sure to use the object (principal) id and not the clientID of the managed identity
