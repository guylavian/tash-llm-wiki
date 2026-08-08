---
title: "How to replicate deleted Active Directory objects when Recycle Bin is enabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/190269/how-to-replicate-deleted-active-directory-objects
question_id: 190269
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to replicate deleted Active Directory objects when Recycle Bin is enabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/190269/how-to-replicate-deleted-active-directory-objects (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to replicate a number of AD objects to a domain controller in a remote site using the replicateSingleObject ldap operation. However, I am having issues with replicating deleted groups when Active Directory Recycle Bin is enabled.  In order to demonstrate the issue, I created the following simplified powershell script that works in Active Directory environments without Recycle Bin enabled:    

```
$SrcDC = "DC01"  # local site  
$DestDC = "DC02" # remote site  
  
# Delete testgroup if it currently exists  
if($group = Get-ADGroup -Identity testgroup) {  
    Remove-ADGroup -Server $SrcDC -Confirm:$false -Identity testgroup  
      
    # replicate group deletion to remote site  
    Sync-ADObject -Source $SrcDC -Destination $DestDC -Object  (Get-ADObject -Server $SrcDC -Filter {Deleted -eq $true -and ObjectGUID -eq $group.ObjectGUID} -IncludeDeletedObjects)  
}  
  
# Recreate testgroup  
New-ADGroup -Server $SrcDC -GroupScope Global -Path "OU=replication,DC=test,DC=lab" -Name testgroup  
  
# Add to testgroup to rolegroup  
Add-ADGroupMember -Server $SrcDC -Identity rolegroup -Members testgroup  
  
# Sync group creation and membership to remote site  
Sync-ADObject -Source $SrcDC -Destination $DestDC -Object (Get-ADGroup testgroup)  
Sync-ADObject -Source $SrcDC -Destination $DestDC -Object (Get-ADGroup rolegroup)
```

When the above script is executed twice within short time span (before the next AD replication cycle) in Active Directory environments with Recycle Bin enabled, the script fails during the second execution on:    

```
Sync-ADObject -Source $SrcDC -Destination $DestDC -Object (Get-ADGroup rolegroup)
```

The function returns the following error from ldap:    

The replication operation failed because the target object referred by a link value is recycled    

By enabling Active Directory diagnostic event logging on the remote DC (DC02), I also found a more detailed message in the event log:    

The destination Active Directory Domain Controller logging this event processed a link value update on the source object below. The link value refers to a target object that is in the recycled state on the destination Active Directory Domain Controller.     

To correct this condition, the destination Active Directory Domain Controller will re-request a re-ordered list of updates from the source Active Directory Domain Controller. If this corrective step fails, event [Task Category: Replication, EventId: 2914] will be logged, referencing the same source and target object DN's and GUIDS's as below.     

Source Object DN:    

CN=rolegroup,OU=replication,DC=test,DC=lab     

Source Object GUID:    

40153236-3e8b-461b-92ae-d72c890f88ac     

Attribute:    

member     

Target Object DN:    

CN=testgroup\0ADEL:2609900c-567e-4f2d-ae1f-31acd243bd90,CN=Deleted Objects,DC=test,DC=lab     

Target Object GUID:    

2609900c-567e-4f2d-ae1f-31acd243bd90     

Source Active Directory Domain Controller:    

808fea83-5fac-4d0a-a5cd-73f948859b07._msdcs.test.lab    

The error message links to the ERROR_DS_DRA_RECYCLED_TARGET error code. The only place that I could find where this error is referred is the ProcessLinkValue procedure, which is called in ProcessGetNCChangesReply in order to apply replicated updates of the link values after updating the replicated object.    

According to the snippet in ProcessLinkValue:    

```
if ((IsRecycleBinEnabled() and targetObject!isRecycled) or  
       (not IsRecycleBinEnabled() and targetObject!isDeleted)) then  
      if (DRS_GET_TGT in ulMoreFlags) then   
         /* nothing to do */  
         return 0  
      else  
         return ERROR_DS_DRA_RECYCLED_TARGET  
   endif
```

When Recycle Bin is enabled, this error code should only be reached when the targetObject is isRecycled. I'm assuming the TargetObject is the deleted group (CN=testgroup\0ADEL:2609900c-567e-4f2d-ae1f-31acd243bd90,CN=Deleted Objects,DC=test,DC=lab) that was deleted less then 15 minutes ago. This TargetObject is not (and should not be?) recycled yet, so why am I receiving the ERROR_DS_DRA_RECYCLED_TARGET error?    

I am understanding this incorrectly / did I miss some documentation?    

Or is there a bug in the ProcessLinkValue procedure when Recycle Bin is enabled?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-09*

Hi,  

Thanks for sharing here!  

Sorry for not familiar with the powershell script.  

Hope the following article will be helpful.  

https://blog.iisreset.me/replicate-a-single-object-without-repadmin/  

Best Regards,
