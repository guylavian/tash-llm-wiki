---
title: "Disable Remote Powershell for Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1033895/disable-remote-powershell-for-exchange
question_id: 1033895
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Disable Remote Powershell for Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1033895/disable-remote-powershell-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm following the guidance for the Exchange zero-days (link below) and I'm curious how others are disabling remote PowerShell access for non-admin users.     

Is there a command to allow access for a specific ad group or local admins? Ideally we'd like to disable all of our standard users and allow just specific IT users.     

How are others accomplishing this?    

https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/     

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-06*

Microsoft tells us to disable remote powershell for non-admin account. OK, fine - but there appears to be no easy way to actually do that without risking getting locked out as the poster above has found. Given the vague and unhelpful documentation, I assume there is no straightforward way to block remote powershell for every account except those in a defined admins group?    

Given that users are created regularly, blocking a whole list of specific accounts isn't a lot of use as it will rapidly become out of date.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-06*

Here goes.    

I ran the short script imamitsingh wrote including excluding admins.    

Now I can't run EMS, it says "Your attempt to connect to this Exchange server was denied because your account isn't enabled for Remote PowerShell."    

Any ideas how to fix this please?    

Thanks    

IDAK

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

Hello,    

You can disable or enable the Remote Powershell using group policies and firewall settings. Bear in mind that this setting is oriented to target the systems that will allow/disallow but not the users.    

GPO1: Computer Configuration | Administrative Templates | Windows Components | Windows Remote Management (RM) | WinRM Service | Allow Remote Server Management Through WinRM    

GPO2: Computer Configuration | Windows Settings | Security Settings | System Services | Windows Remote Management (WS-Management)    

----------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

```
get-user -ResultSize unlimited |  
set-user -RemotePowerShellEnabled $false  
   
Get-aduser Admin1 |  
set-user -RemotePowerShellEnabled $true  
   
Get-aduser Admin2 |  
set-user -RemotePowerShellEnabled $true
```

Also, keep in mind, `RemotePowerShellEnabled` can not be set to false for the logged-in/running user.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

Hi @Richard Long      

Are you looking for this: Control remote PowerShell access to Exchange servers    

The parameter -RemotePowerShellEnabled in command Set-User specifies whether the user has access to remote PowerShell. Remote PowerShell access is required to open the Exchange Management Shell or the Exchange admin center (EAC), even if you're trying to open the Exchange Management Shell or the EAC on the local Mailbox server. Valid values are:    

$true: The user has access to remote PowerShell.    

$false: The user doesn't have access to remote PowerShell.    

```
Set-User "User" -RemotePowerShellEnabled $false
```

And we could use the Exchange Management Shell to disable remote PowerShell access for many users:    

    

And in Exchange 2019 you could use client access rule to meet this need:     

Blocking EAC / Remote PowerShell access in Exchange 2019.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Client Access Rules in Exchange 2019    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
