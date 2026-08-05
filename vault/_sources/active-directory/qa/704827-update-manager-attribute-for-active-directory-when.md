---
title: "Update \"Manager\" attribute for Active Directory when importing from a CSV"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/704827/update-manager-attribute-for-active-directory-when
question_id: 704827
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# Update "Manager" attribute for Active Directory when importing from a CSV

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/704827/update-manager-attribute-for-active-directory-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a weird issue regards updating the "manager" field when importing from a CSV.  

The following works when updating one at a time:  

$user = "fred.smith"  

$manager = "jane.doe"  

$SamAccountName = $user   

$GADuser = Get-ADUser -Filter {SamAccountName -eq $SamAccountName} -ErrorAction Stop  

$GADuser | Set-ADuser -Manager $Manager -ErrorAction Stop  

However, the following errors out when updating and I don't know why:  

$File = "C:\temp\dr.csv"  

$theuser = Import-Csv -Path $File  

foreach ($user in $theuser) {  

$SamAccountName = $user.Name   

$manager = $user.newmanager  

Try {  

$GADuser = Get-ADUser -Filter {SamAccountName -eq $SamAccountName} -ErrorAction Stop  

$GADuser | Set-ADuser -Manager $manager -ErrorAction Stop   

}  

catch {  

Write-Error -Message "$SamAccountName or its manager does not exist please check in Active Directory"  

}  

}  

Contents of the dr.csv file are:  

name,newmanager  

fred.smith,jane.doe  

joe.smythe,jane.doe  

helen.smith,jane.doe  

As very similar commands to the update one at a time section but doesn't like it.  

Any help would be appreciated.  

Many thanks

## Answers

_No answers on this thread._
