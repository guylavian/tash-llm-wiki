---
title: "Exchange 2016 w3wp.exe crash repeatedly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1043386/exchange-2016-w3wp-exe-crash-repeatedly
question_id: 1043386
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-development-iis"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 w3wp.exe crash repeatedly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1043386/exchange-2016-w3wp-exe-crash-repeatedly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We have a problem since several month with Exchange and Outlook.    

Several user get randomly disconnected from Exchange with Outlook.    

After looking on Exchange server, we've found that w3wp.exe crash a lot    

Nom de l’application défaillante w3wp.exe, version : 10.0.14393.0, horodatage : 0x57899b8a    

Nom du module défaillant : ntdll.dll, version : 10.0.14393.5006, horodatage : 0x621ef21b    

Code d’exception : 0xc0000374    

Décalage d’erreur : 0x00000000000f7143    

ID du processus défaillant : 0x1afc    

Heure de début de l’application défaillante : 0x01d8dd5895504e12    

Chemin d’accès de l’application défaillante : c:\windows\system32\inetsrv\w3wp.exe    

Chemin d’accès du module défaillant: C:\Windows\SYSTEM32\ntdll.dll    

ID de rapport : f61a047f-9fd1-4c46-a327-2b13cfc13d82    

Nom complet du package défaillant :     

ID de l’application relative au package défaillant :     

Exchange 2016 and Windows Server 2016 are up to date.    

Using HealthCheker for Exchange doesn't show IIS problem...    

TY for your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-13*

w3wp.exe is an Internet Information Services (IIS) worker process that runs Web applications and is responsible for handling requests sent to a Web Server for a specific application pool. You could recycle the application pool for testing. Meanwhile, you can create recycle settings when reaching the maximum used memory. More reference: https://sysadminguides.org/2017/04/21/fix-exchange-server-high-cpu-memory/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-12*

Hi @Guilhaume  ,    

For w3wp.exe crash and exception code 0xc0000374, it is recommended that you run the DebugDiag tool to collect a crash dump.    

I noticed that you have done some troubleshooting and you are right.    

Besides, do you have any antivirus software on your server? It is recommended that you temporarily disable or uninstall all antivirus software and monitor the system.    

Details: w3wp.exe crashes periodically (Error 0xc0000374) (microsoft.com)    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
