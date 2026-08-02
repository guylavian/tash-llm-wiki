---
title: "Get all active directory computers from all domains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/790901/get-all-active-directory-computers-from-all-domain
question_id: 790901
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Get all active directory computers from all domains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/790901/get-all-active-directory-computers-from-all-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I need to get all Active Directory computers from five different domains. The script below has executed without errors except for one domain. This is the code I am using:  

```
Get-ADComputer -Filter * -Properties * -Server "server.domain.com"  | Select-Object Name
```

This is the error I am seeing:  

```
Get-ADComputer : Directory object not found
At line:1 char:1
+ Get-ADComputer -Filter * -Properties * -Server "server.domain.com"   ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (:) [Get-ADComputer], ADIdentityNotFoundException
    + FullyQualifiedErrorId : ActiveDirectoryCmdlet:Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException,Microsoft.ActiveDirectory.Management.Comm 
   ands.GetADComputer
```

I get that the error message says the Directory object is not found but without changing anything but the server name, the script is working fine in the other domains.   

Thank you!  

Rob

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-28*

I made one change and it seems to be working now:  

```
Get-ADComputer -Filter * -Properties Name -Server "server.domain.com"  | Select-Object Name
```

I added in the name of a property before the pipe, Name.  

The other domains didn't need anything other than -Properties *. Why is this domain different?  

-Rob
