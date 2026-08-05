---
title: "How do you back up drives in domain controller into another physical back up server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189071/how-do-you-back-up-drives-in-domain-controller-int
question_id: 2189071
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# How do you back up drives in domain controller into another physical back up server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189071/how-do-you-back-up-drives-in-domain-controller-int (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys 

This is an understanding issue and suggestion. 

At work, we have domain controller server 2012 R2. Luckily nothing has happened to it so far that will put the data at a loss. 

It has not been backed up in over a year some shares need to be backed up regularly and I have been given the task of finding a way or system to go back to back the drives. 

Before I started with the business they had backup software CloudBerry backup. 

It is my first time dealing with a backup, if you can suggest articles links videos that explain the process I would be grateful 

Thank you for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-27*

Hello Yusuf Abaguben,  

Good day!   

What script did you use? CMD script or PowerShell script?  

how do I check if it works or not?  

A: After you run the script, does the thing below work as expected?  

I want to back those folders in particular into another backup server that has its IP address. so from the main domain server where the files currently reside to be backed up into another server that has a different IP address.

By the way, why do not you copy the folders manually?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-26*

Hi Daisy 

Thank you for your reply. 

I am new to scripts, how do I check if it works or not?

Thank you so much for your support

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-26*

Hello Yusuf Abaguben,  

Good day!  

You can copy the drive\folders that are accessed by employees to a removable storage drive, and then copy it from the removable storage drive to a specified route on the destination server manually.  

Please check if the script itself work or not.  

If the script itself does not work, it will not work via Task schedule. Please check the script.  

If the script itself does work, the Task Schedule does not work. Please check the task schedule configuration.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-23*

Hi Daisy 

Thank you so much for your detailed instructions. much appreciated. 

 My predecessor already has set up the  Windows server backup.

What I want to achieve is in the domain controller we have drive\folders that are accessed by employees, I want to back those folders in particular into another backup server that has its IP address. so from the main domain server where the files currently reside to be backed up into another server that has a different IP address. 

I have tried to script in Task scheduler to start back up at a certain time but it did not run at all    

The script

My question is how can I back up from the main server to a backup server that has its IP address?

Thank you 

Yusuf

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-23*

Hello Yusuf Abaguben,  

Thank you for posting in Microsoft Community forum.  

Based on the description above, do you mean you want to back up the domain controller in the domain\forest? If so, you can back up a full server of the domain controller or back up the system status of the domain controller.  

Before you back up a full server of the domain controller or back up the system status of the domain controller, you should install the built-in Windows backup role on Domain Controller.

Back up steps :  

-  Install Windows Server Backup (open Server Manager-> Add roles and features->Features -> Windows Server Backup)

-  Start->Server Manager->tools-> Windows Server Backup->Local Backup->Action->Backup once

-  Back up options: Scheduled backup options or Different options

-  Select backup configuration: Full server (recommended) or Custom

-  Select items to back up: System state

-  Specify destination type: Local drive or remote shared folder

-  On the confirmation screen, click Backup.  

AD Forest Recovery - Backing up a full server | Microsoft Learn

Considerations for Active Directory Domain Services Backup - Win32 apps | Microsoft Learn

Backing Up and Restoring an Active Directory Server - Win32 apps | Microsoft Learn

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
