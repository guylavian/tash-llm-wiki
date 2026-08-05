---
title: "Menu to add distribution group in Exchange Admin Center 2016 is missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384524/menu-to-add-distribution-group-in-exchange-admin-c
question_id: 384524
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Menu to add distribution group in Exchange Admin Center 2016 is missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384524/menu-to-add-distribution-group-in-exchange-admin-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Normally, one would go into the Exchange Admin Center, click Recipients, then click Groups and from within Groups, one would click on the + sign to select the type of mail enabled distribution group they want to create. When attempting to do so in EAC this evening, I noticed that the + sign is missing. I cannot select the menu that allows me to create the group. Now, I have not researched how to add the group using Powershell, but I'm sure there's a way to do it, however, the fact that the menu is missing in the GUI makes me concerned that my Exchange server isn't operating properly, perhaps due to a bug, bad update or improperly installed patch. How do I restore the GUI functionality?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

Eric, 2 things:

First, I had my IT teammate login into Exchange using his admin credentials and he was able to add the group within the GUI. So the problem may be with just my own admin credentials. Secondly, based on your examples, when I first tried to use PS to create the group, it failed, stating:

New-DistributionGroup : The term 'New-DistributionGroup' is not recognized as the name of a cmdlet, function, script  

file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct  

and try again.  

At line:1 char:1  

-  New-DistributionGroup -Name "grptest"

Next I tried loading the PSSnapin as you directed and after doing so, the commandlet to add the group worked. This was all done using my own admin credentials to the server. I was able to add the group, see it in the Exchange Admin Center under groups, and successfully email the group. However, that did not change the status of the GUI. The GUI was still missing the plus sign needed to add the group.

Finally, the commandlets to show rights did not return a summary:

[PS] C:\Windows\system32>$Perms = Get-ManagementRole -Cmdlet new-distributiongroup  

[PS] C:\Windows\system32>$Perms | foreach {Get-ManagementRoleAssignment -Role $_.Name -Delegating $false | Format-Table  

-Auto Role,RoleassigneeType,RoleAssigneeName

>  

>  

>  

>  

> ^C

[PS] C:\Windows\system32>

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Hi,    

1 Try if you can create a group via Exchange powershell:     

```
New-DistributionGroup -Name "ITDepartment" -Members ******@contoso.com,******@contoso.com,******@contoso.com,******@contoso.com
```

 2 If failed, load Exchange module in Windows powershell and try creating a group again:    

```
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn
```

 3 Check the account that you using have enough permission:    

    

 4 Have you found any other signs missing in your EAC?  Does it make a difference that you change the url to localhost/ecp or ex1.contoso.com/ecp or IPaddress/ecp?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
