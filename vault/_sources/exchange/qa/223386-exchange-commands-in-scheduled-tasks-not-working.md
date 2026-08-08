---
title: "exchange commands in scheduled tasks not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/223386/exchange-commands-in-scheduled-tasks-not-working
question_id: 223386
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
---
# exchange commands in scheduled tasks not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/223386/exchange-commands-in-scheduled-tasks-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello,    

i have the bellow script that run some audit commands that needs to be run in a scheduled task for automation purposes. if i try to run it directly, it works without any problem, but if i try to run it in a scheduled task, it does nothing.    

Could you please, help me or tell me what i shoud do?    

thank you in advance.    

    #########username############  

    $username = "admin@keyman  .local"  

    $logfile = "L:\Script-AuditLog\adminmailbox.log"  

```
#########date today##########  
$dt = Get-Date -UFormat "%d%m%Y"  
$namecsv = "L:\Script-AuditLog\Results\adminmailbox-"+$dt+".csv"  
$namehtml = "adminmailbox-"+$dt+".html"  
echo "$dt : script settings retrieved" >> $logfile  
  
#########password############  
#echo "$dt : audit started" >> $logfile  
$encrypted = Get-Content L:\Script-AuditLog\Password.txt | ConvertTo-SecureString  
$UserCredential = New-Object System.Management.Automation.PsCredential($username, $encrypted)  
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://exc.domain.local/PowerShell/ -Authentication Kerberos -Credential $UserCredential  
  
Import-PSSession $Session -DisableNameChecking  
  
############audit############  
echo "$dt : script executed" >> $logfile  
  
#pour exporter csv  
Search-AdminAuditLog | where-object {($_.cmdletname -eq 'Add-Mailboxpermission') -or ($_.cmdletname -eq 'Add-AdPermission')} | .\Get-SimpleAuditLogReport.ps1 -agree | export-csv $namecsv -delimiter ';'  
#############################  
  
Remove-PSSession $Session
```

## Answers

_No answers on this thread._
