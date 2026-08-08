---
title: "Extend Idle Timeout for Exchange Online Powershell Module"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/195338/extend-idle-timeout-for-exchange-online-powershell
question_id: 195338
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Extend Idle Timeout for Exchange Online Powershell Module

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/195338/extend-idle-timeout-for-exchange-online-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning,     

We are currently using Exchange online powershell module as a shortcut on my desktop.     

When I launch the shortcut, it opens to a Powershell window, then I type in Connect-EXOPSSession and login, then it connects me to the Exchange Online.     

Problem is that when I am running a script that takes a while to complete, the session will time out after 15 minutes.    

Get-IPSSession shows the timeout is 900000 milliseconds/15 minutes.    

I looked at the below article, but I am not putting in the variables in manually.      

https://social.msdn.microsoft.com/Forums/en-US/a5eae821-bed2-4cb1-8965-ff09261312c9/increase-online-powershell-module-session-time?forum=onlineservicesexchange    

Is there a way to change this somewhere?     

Tried Connect-EXOPSSession -UserPrincipalName (LoginName) -IdleTimeout, but that errored out.     

Looks like all the variables are being run and configured from a powershell file.     

that is attached to this question as a text file47492-createexopssession.txt    

If I can either extend that IdleTimeout to hours or just to 0 that would be immensely helpful.    

Thank You    

Brian Dougherty

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-16*

Just in case this helps someone   

```
$pso = new-PSSessionOption -IdleTimeout 43200000 
Connect-ExchangeOnline -UserPrincipalName  -PSSessionOption $pso
```

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-14*

@Brian Dougherty       

Based on my knowledge, IdleTimeout works for New-PSSessionOption cmdlet. You can try to use the parameter -PSSessionOption with the configuration:    

```
New-PSSessionOption -IdleTimeout "a value in milliseconds"
```

If if still doesn't work, you can use EXO V2 module and the following command to connect:    

```
Connect-ExchangeOnline -PSSessionOption IdleTimeout  -UserPrincipalName  -ShowProgress $true
```

Please check this for more details: Connect to Exchange Online PowerShell.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
