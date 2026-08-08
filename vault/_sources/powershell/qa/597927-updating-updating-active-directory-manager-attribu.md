---
title: "Updating Updating Active Directory Manager Attribute using PS from a CSV File"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/597927/updating-updating-active-directory-manager-attribu
question_id: 597927
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Updating Updating Active Directory Manager Attribute using PS from a CSV File

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/597927/updating-updating-active-directory-manager-attribu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to update the AD manager field using PS. We we're given a CSV file from HR with everyone's manager info. This is PS script.

Import-Module ActiveDirectory  

$Users = Import-Csv "C:\Users\Administrator.APC-SERVICES\Desktop\mngimport\Managers1.csv"  

ForEach ($User in $User)  

{  

$ADUser = Get-ADUser -Filter "displayname -eq '$($User.ProfessionalFullName)'"  

$manager = (Get-ADUser -Filter "displayname -eq '$($User.'ManagerFullName')'").distinguishedname

if ($ADUser -and $manager) {  

Set-ADUser -Identity $ADUser -Replace @{manager = $manager }  

}  

}

Nothing happens after running this. I keep checking the AD Users and the Manager attribute does not update. What am i missing?

CSV format:  

ProfessionalFullName,ManagerFullName  

Greg Brown,Jay Smith  

Jesus Lopez ,Jay Smith  

Stephen Jones,Jay Smith  

Scott Williams ,Roy Miller  

Jason Davis,Roy Miller

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-10-21*

Try it this way:  

```
Import-Csv "C:\Users\Administrator.APC-SERVICES\Desktop\mngimport\Managers1.csv" |
    ForEach-Object {
        $ADUser  =  Get-ADUser -Filter "displayname -eq '$($_.ProfessionalFullName)'"
        $manager = (Get-ADUser -Filter "displayname -eq '$($_.ManagerFullName)'").distinguishedname

        if ($ADUser -and $manager) {
            $ADUser | Set-ADUser -manager $manager
        }
    }
```

Two things:  

-  You don't have to explicitly import the ActiveDirectory module. PowerShell (since version 3) will do that automatically.  

-  Using the DisplayName to identify users is a little bit risky since a display name may not be unique in the AD forest. A samaccountname or primary email address is much better

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-22*

Hey,

Is look like half of my users failed to updated. I modified it for "sAMAccountName" and the "Name".

This is what I'm running:

Import-Csv "C:\Users\Administrator.APC-SERVICES\Desktop\mngimport\managers.csv" |  

ForEach-Object {  

$ADUser = Get-ADUser -Filter "Name -eq '$($.Name)'"  

$manager = (Get-ADUser -Filter "sAMAccountName -eq '$($.sAMAccountName)'").distinguishedname  

}  

if ($ADUser -and $manager) {  

$ADUser | Set-ADUser -manager $manager  

}

CSV File:  

Name,sAMAccountName  

Dipal Smith,VBell  

Dolly Ryan,VBell

Any thoughts?
