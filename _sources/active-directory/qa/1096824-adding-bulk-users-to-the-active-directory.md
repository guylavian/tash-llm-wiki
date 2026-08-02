---
title: "Adding Bulk Users To The Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1096824/adding-bulk-users-to-the-active-directory
question_id: 1096824
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Adding Bulk Users To The Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1096824/adding-bulk-users-to-the-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
./Bulk_Users1.psi  

           I put the "./" to indicate that it's a script
```

I am adding a bunch of users from a excel spreadsheet .csv to AD from a vm admin work station. I keep getting the error:

New-ADUser : The object name has bad syntax  

At C:\IT\bulk_users1.ps1:41 char:3  

-  New-ADUser `  

-  ~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (CN=William Jime...qafzal,DC=LOCAL:String) [New-ADUser], ADException  

-  FullyQualifiedErrorId : ActiveDirectoryServer:8335,Microsoft.ActiveDirectory.Management.Commands.NewADUser

I am running the PowerShell from a domain controller as a session from the Admin Workstation because it has RSAT tools.

Not sure what is wrong..

and this is the bulk user script am running that runs its info such as name, surname from the excel spreadsheet then to the excel spreadsheet:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-20*

What is the distinguishedName of the OU in the AD? Is it the same as the distinguisheName in the "OU" column of the CSV?    

Please don't post screenshots. If you post code, use the "Code Sample" icon on the Fromat Bar (it's the 5th on from the left). If you have an error message, copy the text from the screen an post that.    

Also, you haven't shown the contents of your CSV (or at least the first few lines of it, including the header). And we have no idea what the name of the target OU is.
