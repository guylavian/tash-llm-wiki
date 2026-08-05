---
title: "Manage Exchange 2016 from a Windows 2019 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1132007/manage-exchange-2016-from-a-windows-2019-server
question_id: 1132007
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor"]
---
# Manage Exchange 2016 from a Windows 2019 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1132007/manage-exchange-2016-from-a-windows-2019-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We run On-prem Exchange 2016 in our air-gapped environment.    

I have a need to create user mailboxes as part of an account creation Powershell script.     

This script must be run from a Windows 2019 Server.    

For reasons of security Winrm is disabled on our servers.    

I'm at a loss as to how I can achieve this (what I thought would be a) simple task and therefore am turning to you good folk for help.    

Am I missing something obvious?    

Kind regards,    

Kev

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-12-20*

Exchange PowerShell remoting has nothing to do with base Windows remoting.  Totally separate.      

There is the /PowerShell vDir and that's what the Exchange management tools use over TCP 80.    

Have you done something like force TLS on that that vDir?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-20*

Additional info:     

"Test-WsMan <FQDN>" works a treat.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-20*

Hi aholicliang-msft,    

Thanks for your response.    

Unfortunately, I still can't get it to work. I have followed your steps but now, when I run the New-PSsession command, it returns the following:    

"Connecting to remote server <FQDN> failed with the following error message : WinRM cannot complete the operation. Verify that the specified compiuer name is valid, that the computer is accessible over the network, and that a firewall exception for the WinRM service is enable and allows access from this computer."    

I have verified from the server on which I'm running the script that I can access the Exchange server on port 5985 (using test-netconnection) and that the Windows Remote Management service is running on the Exchange server.     

What else should I be looking for?    

Your help is very much appreciated.    

Regards,    

Kev

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-19*

Hi @Kevin Mullan   ,    

According to my tests, if I disable the WinRM service on the exchange server, I still can connect to the exchange remotely through PowerShell on Win 10.    

You could refer to the following link to connect to Exchange servers using remote PowerShell:    

Connect to Exchange servers using remote PowerShell | Microsoft Learn    

(Kindly note: Please add the Windows 2019 server to the intranet. )    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
