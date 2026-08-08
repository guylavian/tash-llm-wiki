---
title: "Powershell command Connect-ExchangeOnline failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3972610/powershell-command-connect-exchangeonline-failed
question_id: 3972610
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Powershell command Connect-ExchangeOnline failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3972610/powershell-command-connect-exchangeonline-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am trying to get space used by mailboxes of users in exchange.

I tried to connect to Exchange Online using powershel command Connect-ExchangeOnline.

I failed with message :

New-ExoPSSession : La connexion au serveur distant outlook.office365.com a échoué avec le message d’erreur suivant: Le client WinRM a reçu un statut d’erreur du serveur HTTP (500), mais le service distant n’a pas inclus

d’autres informations sur la cause de l’échec. Pour plust d'informations, voir la rubrique d'aide about_Remote_Troubleshooting.

Au caractère C:\Users\guytr\OneDrive\EspaceSingulier\Sauvegardes\Documents\WindowsPowerShell\Modules\ExchangeOnlineManagement\2.0.5\netFramework\ExchangeOnlineManagement.psm1:475 : 30

+ ... PSSession = New-ExoPSSession -ExchangeEnvironmentName $ExchangeEnviro ...

+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ CategoryInfo          : ResourceUnavailable: (:) [New-ExoPSSession], PSRemotingTransportException

+ FullyQualifiedErrorId : System.Management.Automation.Remoting.PSRemotingDataStructureException,Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession

Opened a support ticket, but they couldn't solve the problem. 

It seems to be a Windows , or account problem.

Has anyone encountered the same problem and/or have a solution to offer me ?

Thanking you in  advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-18*

Hi Guy,

Thank you for reaching out to the Microsoft Community , I'm kishen an Independent Advisor and a Microsoft user like you. 

I'll be glad to assist you today. As this is not a live chat, Kindly expect some delay in response.

Sorry, the Microsoft Community is a forum for home users. Due to the scope of your question, I suggest you access the link below, which will direct you to the Microsoft Q&A IT Pro forum.

https://learn.microsoft.com/en-us/answers/quest...

Microsoft Q&A has IT Pros and system administrators who can best help with this question.

You may also try this question on StackOverflow.

https://stackoverflow.com/

Standard Disclaimer: This is a non-Microsoft website. The page appears to be providing accurate, safe information. Watch out for ads on the site that may advertise products frequently classified as a PUP (Potentially Unwanted Products). Thoroughly research any product advertised on the site before you decide to download and install it.

NOTE: The page is in English. Use your browser's automatic translator to translate the page.

Regards,

Kishen :)
