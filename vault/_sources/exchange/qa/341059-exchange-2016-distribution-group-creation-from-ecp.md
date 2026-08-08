---
title: "Exchange 2016 Distribution group creation from ECP appending numbers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341059/exchange-2016-distribution-group-creation-from-ecp
question_id: 341059
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Distribution group creation from ECP appending numbers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341059/exchange-2016-distribution-group-creation-from-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we recently migrated to Exchange 2016 (cu19) from Exchange 2013.   

When an admin uses the ECP to create a group, the group is created with a set of numbers appended to the end of the name.   

Example:   New Group Name = "Test Group"  The group will be named "Test-Group-123456789"  

This is due to a group not being created with the SamAccountName. There isn't an option in the ECP to specify the SamAccountName.   

This was never an issue in any version of the ECP with Exchange 2007, 2010, or 2013.  Why is this now an issue with 2016?  

I am aware of the alternative methods to create / repair the groups with powershell.   

Powershell works for my powershell admins but not the Help Desk or any exchange support staff that create groups exclusively through the ECP.   

Repair the group powershell command.   

Get-DistributionGroup | foreach {Set-DistributionGroup $.name -SamAccountName $.name}  

Again, This was never an issue in any version of the ECP with Exchange 2007, 2010, or 2013.  Why is this now an issue with 2016?   

Can this please be reverted back to how it functioned in prior installments of exchange?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-02*

Hi,    

New Group Name = "Test Group" The group will be named "Test-Group-123456789"    

-Which name do you mean that will be renamed automatically? I checked all values in my test, one is Samaccountname, another one is Group name(pre-Windows2000) in ADUC. Do you really use this group name?     

In Exchange 2010, there's only EMC for GUI, and you can specify the name when creating DG, so it's not an issue.    

    

In Exchange 2013, it will specify samaccount name automatically, so it's not an issue:    

    

In Exchange 2016&2019, it behaves as you said, I think that's what Microsoft want it to be.    

For a workround but not recommended, I've tested it works:    

1 On all Exchange Server 2016, find the %ExchangeInstallPath%Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml.sample file, rename it to ScriptingAgentConfig.xml (Backup the original file)    

2 Open renamed file, remove all the content and add the following script.    

3 Enables the cmdlet extension agent named Scripting Agent: Enable-CmdletExtensionAgent "Scripting Agent"    

4 Restart IE and try to create a new security group via EAC.    

Script:    

```
  
  
  
  
     
  
       
  
       If($succeeded) {  
  
         $mbx = $provisioningHandler.UserSpecifiedParameters["Alias"]  
  
  
     Set-DistributionGroup $mbx -SamAccountName $mbx  
  
       }  
  
       
  
     
  

```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
