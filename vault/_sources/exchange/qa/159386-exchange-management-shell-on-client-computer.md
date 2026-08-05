---
title: "Exchange Management Shell on client computer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159386/exchange-management-shell-on-client-computer
question_id: 159386
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# Exchange Management Shell on client computer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159386/exchange-management-shell-on-client-computer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I want to run exchange cmdlets on exchange management shell (on client computer). Will it require PS remoting to be enabled on the Exchange Server machine?  

Thanks,  

Sambhav

## Answer (community) — community member

*upvotes: 2 · updated: 2020-11-12*

Hi @Anonymous   ,  

Did you installed the Exchange management shell on client computer?  

-  If you install the Exchange management shell, according to my test, you could directly open EMS and run Exchange cmdlets. In addition, please make sure that the computer where you install Exchange Management Shell meets the system requirements of the corresponding Exchange version and has installed the required prerequisites.  

For more information: Exchange Server PowerShell (Exchange Management Shell) and Exchange Server prerequisites

2.If not, you could following steps to connect to Exchange server using remote Powershell:  

-  Open the Windows Powershell on client computer, then run the following command and enter your credential:    $UserCredential = Get-Credential  

2) Run the following commands and then you could run the Exchange cmdlet in Powershell:

```
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http:///PowerShell/ -Authentication Kerberos -Credential $UserCredential  
Import-PSSession $Session -DisableNameChecking
```

3) When you are finished using, please remember to run the following command line to disconnect, instead of closing the powershell window directly:

```
Remove-PSSession $Session
```

Below screenshot is my test in me lab environment:  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 1 · updated: 2020-11-11*

please check step by step guide    

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-servers-using-remote-powershell?view=exchange-ps    

Hope answer the question if issue resolve don't forget to accept answer
