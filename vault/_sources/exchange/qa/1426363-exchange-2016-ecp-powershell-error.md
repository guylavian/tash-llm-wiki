---
title: "Exchange 2016 ECP / Powershell Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1426363/exchange-2016-ecp-powershell-error
question_id: 1426363
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 ECP / Powershell Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1426363/exchange-2016-ecp-powershell-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Evening Everyone

I am having some issues in my Exchange 2016 CU23 instance that were discovered after users reported not being able to search on the server side.  I am in the process of rebuilding the server side index but wanted to see if anyone saw any correlation between that and two other issues i noticed (Especially #2)  today along with getting some guidance on the best way to address them.

-  Clicking View Details for a user in the ECP creates the error message:  Could not load file or assembly 'Microsoft.Exchange.OfficeGraph.GrainTransactionStorage, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. Access is denied.

-  EMS is giving the following error when using the Get-MailboxDatabaseCopyStatus commandlet and also produces the same error when running it standalone without parameters: 

```
[PS] C:\Windows\system32>Get-MailboxDatabaseCopyStatus * | sort name | Select name,status,contentindexstate
WARNING: An unexpected error has occurred and a Watson dump is being generated: The type initializer for
'Microsoft.Exchange.Cluster.Shared.RegistryParameters' threw an exception.
The type initializer for 'Microsoft.Exchange.Cluster.Shared.RegistryParameters' threw an exception.
    + CategoryInfo          : NotSpecified: (:) [Get-MailboxDatabaseCopyStatus], TypeInitializationException
    + FullyQualifiedErrorId : System.TypeInitializationException,Microsoft.Exchange.Management.SystemConfigurationTask
   s.GetMailboxDatabaseCopyStatus
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-16*

Check the Service Health Portal:

https://admin.microsoft.com/Adminportal/Home?source=applauncher#/servicehealth

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-16*

This turned out to be corruption related and fixing that resolved all my issues along with rebuilding the index to resolve the original issue.  It's always easy to overlook that and i wanted to share the solution incase it helps anyone else.
