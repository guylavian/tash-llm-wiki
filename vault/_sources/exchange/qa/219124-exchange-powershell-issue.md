---
title: "exchange powershell issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/219124/exchange-powershell-issue
question_id: 219124
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# exchange powershell issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/219124/exchange-powershell-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello ,  I have a tricky issue with exchange management shell.  

I have MBX1 ,MBX2, MBX3, MBX4 TOTAL 4 exchange 2016 servers.  

MBX1 and MBX2 have a dag  

MBX3 has all the shared mailbox so it doesn't with dag.  

MBX4 has no mailbox on it, it only for the connect with exchange online (for hybrid deployment)  

my laptop installed exchange management tools, and working fine (I often use my laptop to manage exchange with exchange management powershell)  

today I discover I get no result when I runnging below command on my laptop.  

But I get the expect result if I run the command on MBX 1 OR 2 OR 3 OR 4 (no matter which server)  

Get-MailboxDatabase | Get-MailboxStatistics | Where{$_.DisconnectReason -eq "Disabled"}  

anyone knows why ? thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

halo,     

I discover if change the operator from -eq to -like, it can get the output:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-06*

Instead of importing a PowerShell session or running the command on your laptop, try running this on your laptop:  

```
$MyExchangeServer = (Get-ExchangeServer | Where-Object {$_.IsMailboxServer})[0]
$d = Invoke-Command -Computer $MyExchangeServer -ScriptBlock {
            Get-MailboxDatabase | Get-MailboxStatistics | 
                Where-Object {$_.DisconnectReason -eq "Disabled"} 
        }
$d | FormatTable DisplayName,DisconnectReason
```

You can eliminate the 1st line if you know the name of an Exchange server. Then just use that name instead of the "$MyExchangeServer" variable on the Invoke-Command cmdlet.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

anonymous userDavid @Rich Matheisen       

Interesting . the filter the DisconnectReasonwith not null and Disabled, and get different output    

I believe 2 command is same:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-05*

Hi @Jerry Su   ,    

Could you please let us know the below,    

Any error message while executing that command?    

Are you using the same admin account? Have you tried with a different admin account    

Are you able to rum Get-MailboxDatabase and Get-MailboxStatistics separately    

Can you try the below,    

Launch Windows powershell using administrator    

Set-ExecutionPolicy RemoteSigned    

$UserCredential = Get-Credential (Provide the administrator credentials)    

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://<ServerFQDN>/PowerShell/ -Authentication Kerberos -Credential $UserCredential     

(Replace the MBX1 FQDN)    

Import-PSSession $Session -DisableNameChecking    

Then try running Get-MailboxDatabase | Get-MailboxStatistics | Where{$_.DisconnectReason -eq "Disabled"}    

If it works, try re-installing Exchange management tools on your laptop.     

If the above suggestion helps, please click on "Accept Answer" and upvote it
