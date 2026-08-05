---
title: "Active Directory - List all Groups and its Members"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/927542/active-directory-list-all-groups-and-its-members
question_id: 927542
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Active Directory - List all Groups and its Members

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/927542/active-directory-list-all-groups-and-its-members (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I'm new to PowerShell and would like to get assistance on the following: Get the list of all Active Directory groups, their associated members along with information such as windows login, name, and last logon. I would also like all this to be exported to csv.

The script I have been using is (without the export part):  

$group = Get-ADGroup -Filter *|select -ExpandProperty name

> foreach($g in $group){Get-ADGroupMember $g|where{$_.ObjectClass -eq "User"}|Get-ADUser -Properties *|select Displayname,Manager,SamAccountName,@{n="GroupName";e={$g}},@{

n="lastlogontime";e={[DateTime]::FromFileTime($_.lastlogon)}}}

This is how one part of the output looks like (which is exactly what i need) without including the export part:  

Displayname : "It displays the name of the person"  

Manager :  

SamAccountName : "It displays it correct"  

GroupName : Domain Admins  

lastlogontime : 8/31/2020 11:32:01 AM

When I try to run the script with the export part, it exports everything, but the security groups (like the one above "Domain Admins"), but exports the rest of the groups and it's members without issues.

This is the script i run when I want the output exported"

$group = Get-ADGroup -Filter *|select -ExpandProperty name

> foreach($g in $group){Get-ADGroupMember $g|where{$_.ObjectClass -eq "User"}|Get-ADUser -Properties *|select Displayname,Manager,SamAccountName,@{n="GroupName";e={$g}},@{

n="lastlogontime";e={[DateTime]::FromFileTime($_.lastlogon)}}} $Results| Export-csv -path c:\xxx\xxx\test.csv -NoTypeInformation

Can someone help me with this? Why would it leave the sec groups out when trying to export the results where it did print out all of the groups including the sec groups?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-15*

Have a look at the following.  (This does not resolve the LastLogon issue I mentioned earlier).    

This gets all of the groups and users first and then reuses that list of users.    

It only gets the attributes you need.  SamAccountName is a default attribute and you don't need to specifically include it.    

I would recommend including a -searchbase in the Get-ADUser to improve the performance of that element.    

It may take a while to initially retrieve the users, but after this, all of the user processing is local.    

```
$groups = (Get-ADGroup -Filter *).Name  
$users = Get-ADUser -Filter * -properties DisplayName, Manager, LastLogon  
  
      
 foreach ($group in $groups){  
    Get-ADGroupMember $group | Where {$_.objectClass -eq "User"} |   
        ForEach {  
            $searchTerm = $_.SamAccountName  
            $user = ($users | Where-Object {$_.SamAccountName -eq $searchTerm} | Select-Object DisplayName, Manager, SamAccountName, LastLogon)  
            $props = [ordered]@{    
                DisplayName = $user.DisplayName    
                Manager = $user.Manager                 
                SamAccountName = $user.SamAccountName  
                GroupName = $group  
                LastLogontime = [DateTime]::FromFileTime($user.LastLogon)}         
            [PSCustomObject]$props  
    }  
} Export-CSV export-filename.csv -NoTypeInformation
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-15*

@{n="GroupName";e={$g.Name}}    

btw, current logic will throw several ADSI calls to Domain controllers.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-14*

@TSHINDAYE    

@annaWY
