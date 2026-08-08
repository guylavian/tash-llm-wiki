---
title: "Exchange Powershell to manage SendAs permissions not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1572696/exchange-powershell-to-manage-sendas-permissions-n
question_id: 1572696
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Exchange Powershell to manage SendAs permissions not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1572696/exchange-powershell-to-manage-sendas-permissions-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to manage sendAs permissions on a SharedMail box using Powershell.  

The commands execute OK but results are not shown in the EAC or from a Get command even when I wait until the next day.
If I run the add-recipientpermission once there are not errors but re-running gives an error that the appropriate access control is already present.
If I then run the remove-recipientPermission once it runs with no errors but twice I get the error that the ACE is not present.
This looks like the add and remove are doing something, but the changes are not shown when I look in the EAC or run the Get-EXORecipient Permissions.
Any help much appreciated.

```
Connect-ExchangeOnline 
$SMB= "testshared@mydomain"
$UPN = "account@mydomain"
#  Get Permissions
Get-EXORecipientPermission -UserPrincipalName $SMB -ResultSize Unlimited| ? {$_.Trustee -Like "*@*" }
# Get-RecipientPermission  $smb -ResultSize Unlimited| ? {$_.Trustee -Like "*@*" }
#### Set SendAs
Add-RecipientPermission -Identity $UPN -AccessRights SendAs –Trustee $SMB -Confirm:$false 
###  Remove SendAs
Remove-RecipientPermission -Identity $UPN -AccessRights SendAs –Trustee $SMB -Confirm:$false
```

## Answers

_No answers on this thread._
