---
title: "how to combine 2 ForEach in exchange shell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374531/how-to-combine-2-foreach-in-exchange-shell
question_id: 1374531
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-powershell"]
---
# how to combine 2 ForEach in exchange shell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374531/how-to-combine-2-foreach-in-exchange-shell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone. 

Can you help me combine 2 scripts in one powershell command

-  export mailbox from csv

-  in status completed - disable user

-  clean username from all distributiongroups

all my scripts is working, but i need in 1 task. Thank you

i think this script need to be out-file with sAMAccountName of users, but i don't know how) 

$users = import-csv "C:\csv\СписокУволенныхСотрудников.csv"
$Data = @()
Import-Module ActiveDirectory
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn
foreach ($user in $users){  

$UserName = $user.name +" "+$user.Surname  

$temp = Get-ADUser -Filter 'Name -eq $UserName' | select sAMAccountName

and then

-  starts from export mailbox from csv script, 

$users = import-csv "C:\csv\СписокУволенныхСотрудников.csv"
$Data = @()
Import-Module ActiveDirectory
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn
foreach ($user in $users){  

New-MailboxExportRequest -Mailbox $temp.sAMAccountName -Name $user -FilePath \exchange\fired$user.pst   } 

then need  disable mailbox and remove completed list

Import-Module ActiveDirectory
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn  

foreach ($user in $users){  

Disable-ADAccount -Identity $($sAMAccountName)  

Get-ADUser -Identity $sAMAccountName | Move-ADObject -TargetPath "OU=DisabledAcounts,DC=next,DC=local"      If ((Get-MailboxExportRequest $fileName).Status -eq "Completed"){  

Disable-Mailbox -Identity $sAMAccountName -confirm:$false  

Get-MailboxExportRequest -Status Completed | Remove-MailboxExportRequest -Confirm:$false  

}  

}   

and combine in 1 powershell with finish script remove from all distribgroups by list

```
ForEach ($Group in $DistributionGroups)
    {
        If ((Get-DistributionGroupMember $Group.Name | Select -Expand PrimarySmtpAddress) -contains $($sAMAccountName))
        {
            Remove-DistributionGroupMember -Identity $Group.Name -Member $($sAMAccountName) -Confirm:$false
            Write-host "Removed user from group '$Group'" -f Green
        }
    }
```

IF anyone can help me - i'll answer immediately.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-19*

all working. thanks !!!
