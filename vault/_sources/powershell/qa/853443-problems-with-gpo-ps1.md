---
title: "Problems with gpo & ps1 ..."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/853443/problems-with-gpo-ps1
question_id: 853443
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Problems with gpo & ps1 ...

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/853443/problems-with-gpo-ps1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an issue with a PowerShell script with GPO, my script:

Get-AppxPackage -AllUsers | where-object {$.name –notlike “*windowscalculator*”} | Remove-AppxPackage  

Get-appxprovisionedpackage –online | where-object {$.packagename –notlike “windowscalculator”} | Remove-AppxProvisionedPackage -online﻿

The idea is to delete all the applications provided by Microsoft in Windows 10.

I try to put it as a startup script, in the end, and don't work.

Do you have any idea why ???

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-23*

Hello  

Thank you for your question and reaching out. I can understand you are  having issues related  to related start-up script to remove app.  

Please try to put pause or Sleep before starting the script as running PowerShell script can be slow compared to .bat script and it requires to be in User-context mode after user profile is loaded.  

Please also put logging of errors to review any potential syntax or other errors  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-20*

Hi !!!  

I put it Start-Transcript when I run manually to create the log file, but when I run by the policy do anything !!!  

I'm really frustrating the PS1 doesn't run !!!  

Thanks so much ...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-18*

Add a Start-Transcript command to your .ps1. It will create a log of everything the script does.    

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-5.1    

If the commands don't generate any output at all, you may need to add -verbose to the commands to get additional info.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-05-18*

Hi @Carlos Arizmendi   a    

Thank you for asking this question on the **Microsoft Q&A Platform. **    

Try the recommendations of this post    

Sometimes you would need to automate an uninstall of an application through Group Policies (GPO). This can be done by running a PowerShell script. Firstly create a PowerShell script as below:    

```
$appplication = Get-WmiObject -Class Win32_Product | Where-Object  
{$_.Name -match "My Application Name"}  
$application.Uninstall()
```

Save the file and create a new GPO and set the script to load by setting up the Computer Configuration/ Policies/ Windows Settings/ Scripts/ Startup.    

Hope this helps,    

Carlos Solís Salazar    

----------    

Accept Answer and Upvote, if any of the above helped, this thread can help others in the community looking for remediation for similar issues.    

NOTE: To answer you as quickly as possible, please mention me in your reply.
