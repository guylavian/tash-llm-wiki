---
title: "Automate connect to exchange online (with a scheduled task) to run set-mailbox command"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/369520/automate-connect-to-exchange-online-with-a-schedul
question_id: 369520
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Automate connect to exchange online (with a scheduled task) to run set-mailbox command

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/369520/automate-connect-to-exchange-online-with-a-schedul (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,    

please help me automate the connection via PS-Session to exchange online.    

If you have a better solution, please share it with me.    

Set-ExecutionPolicy Unrestricted    

Read-Host "Enter Password" -AsSecureString |  ConvertFrom-SecureString | Out-File "C:\Temp\Password.txt"      

$User = "serviceuser@xxxxxxxxxxxxx  "    

$File = "C:\Temp\Password.txt"    

$MyCredential=New-Object -TypeName System.Management.Automation.PSCredential ` -ArgumentList $User, (Get-Content $File | ConvertTo-SecureString)    

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $MyCredential -Authentication Basic -AllowRedirection    

  Import-PSSession $Session -DisableNameChecking -AllowClobber -WarningAction SilentlyContinue    

------------    

The Error:---------------    

Access Denied

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-23*

Yea, you dont want to use that  :)    

Use the  certificate based EXo Module and add it the Exchange Admin Role Group    

https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps    

https://www.youtube.com/watch?v=wIxOW6nZ5OU
