---
title: "\"Active Directory Domain Services could not transfer the remaining data in directory partition.....\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195707/active-directory-domain-services-could-not-transfe
question_id: 1195707
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# "Active Directory Domain Services could not transfer the remaining data in directory partition....."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195707/active-directory-domain-services-could-not-transfe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I`m facing problems to demote domain CTRL. "Uninstall-ADDSDomainController -LastDomainControllerInDomain" gives me the bellow error  message. 

Uninstall-ADDSDomainController : The operation failed because:
**Active Directory Domain Services could not transfer the remaining data in directory partition **CN=Schema,CN=Configuration,DC=Office-1,DC=local to
Active Directory Domain Controller DC-2.office-2.local.
"The RPC server is unavailable."
At line:1 char:1

-  Uninstall-ADDSDomainController -LastDomainControllerInDomain

- 

```
+ CategoryInfo          : NotSpecified: (:) [Uninstall-ADDSDomainController], DCPromoExecutionException
    + FullyQualifiedErrorId : DCPromo.General.54,Microsoft.DirectoryServices.Deployment.PowerShell.Commands.UninstallADDSDomainCommand
```

I found this artile https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcpromo-demotion-fails. It matches my problem. The solution provided is as fallow:

1.Use ADSIEDIT.MSC to assign the DN path for the fsMORoleOwner attribute to a live DC that was a direct replication partner of the original FSMO role owner. Then wait for that change to inbound-replicate to the DC that's being demoted.

2.Run the script in the Resolution section of KB949257 for the partition in question.

3.If the DC that's being demoted can't inbound-replicate changes for the directory partition in question, run the DCPROMO /FORCEREMOVAL command to forcefully demote the domain controller.

The server does not have a GUI so I dont know how to apply step 1. I tried with DCPROMO /FORCEREMOVAL but it failed with below message.

"This domain controller holds operations master roles, is a global catalog server or is a DNS server."

Any advice?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-05*

Ok, we did not know it was a child domain.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/remove-orphaned-domains  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-04*

Hi Dave, as I said the domain controller is Windows Server Core Edition. In other words there is no GUI.  Thus I can not perform the solution described in "Step-By-Step: Manually Removing A Domain Controller Server". Can it be performed via powershell/cms?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-03*

You can follow along here to cleanup and remove remnants of failed one from active directory

Clean up Active Directory Domain Controller server metadata  

Step-By-Step: Manually Removing A Domain Controller Server    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
