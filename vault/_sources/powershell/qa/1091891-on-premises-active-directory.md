---
title: "On-premises Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1091891/on-premises-active-directory
question_id: 1091891
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# On-premises Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1091891/on-premises-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

Can you please provide me a script to get all users information with all attributes from Active directory and wants to save it in CSV file.     

Also need to get information about OUs and Groups memberships.      

thanks    

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-17*

Hi!    

I just added the requested content above (members of a group). If you also need to see the dependencies (Member of section of groups) let me know.    

If it helps, please accept the answer and upvote.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

Hi    

Setting group list    

$groupslist = Get-adgroup -Filter * -SearchBase "DC=test,DC=local" -Properties SamAccountName, whenCreated, ObjectClass | select SamAccountName, whenCreated, ObjectClass    

It will also extract the group members and group memberships? If not, then what parameters will be used in this script?    

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

Hi!

I wrote this just now, you could look into the OU using the parameter Distinguished name, I am not sure of the right cmdlet to extract the details (filtered through) to solely get the OU's

Setting export file names

$mainpath = "C:\temp\"  

$usersexportpath = "$mainpath\userslist.csv"  

$groupsexportpath = "$mainpath\groupslist.csv"  

$groupmemberexportpath = "$mainpath\groupmembers.csv"

Setting user list

$userslist = Get-ADUser -Filter * -SearchBase "DC=test,DC=local" -Properties SamAccountName,DisplayName,givenName,LastLogonDate,mail,Enabled,whenCreated, ObjectClass | select SamAccountName,DisplayName,givenName,UserPrincipalName,ProxyAddress,LastLogonDate,mail,Enabled,whenCreated, ObjectClass

Setting group list (Specific)

$groupslist = Get-adgroup -Filter * -SearchBase "DC=test,DC=local" -Properties SamAccountName, whenCreated, ObjectClass | select SamAccountName, whenCreated, ObjectClass

Setting group list (overall)

$groupslist = Get-adgroup -Filter * -SearchBase "DC=test,DC=local"

Setting output with foreach loop to get the members of each group.

$groupmember= foreach($group in $grouplist){  

Get-adgroup $group | get-adgroupmember  

}  

$groupmember | Export-Csv $groupmemberexportpath -encoding "unicode" -NoTypeInformation

Writing ifstatement for users export, just solely confirming that the object class stored in $userslist matches the user type

if($userslist.objectclass -eq "user"){  

$userslist | Export-Csv $usersexportpath -encoding "unicode" -NoTypeInformation  

}  

else{  

write-host "Something went wrong"  

}

Writing ifstatement for groups export, just solely confirming that the object class stored in $groupslist matches the group type

if($groupslist.objectclass -eq "group"){  

$groupslist | Export-Csv $groupsexportpath -encoding "unicode" -NoTypeInformation  

}  

else{  

write-host "Something went wrong"  

}

Hope it helps!

(If it does feel free to accept the answer and upvote ;) )

For reference:

https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroupmember?view=windowsserver2022-ps

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

I m already using this script:    

Get-ADUser -Filter * -SearchBase  "DC=test,DC=local" -Properties SamAccountName,DisplayName,givenName,LastLogonDate,mail,Enabled,whenCreated | select SamAccountName,DisplayName,givenName,UserPrincipalName,ProxyAddress,LastLogonDate,mail,Enabled,whenCreated | Export-Csv "C:\temp\Users.csv" -encoding "unicode" -NoTypeInformation    

This is working fine But this scripts does not retrieve the OU and group informaion. I am not femilier with Powershell. Anybody can modify it according to my requirement.    

Thanks in Advance.    

Regards
