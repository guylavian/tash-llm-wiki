---
title: "Exchange 2013 CU + KB = dead OWA/ECP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/358676/exchange-2013-cu-kb-dead-owa-ecp
question_id: 358676
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 CU + KB = dead OWA/ECP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/358676/exchange-2013-cu-kb-dead-owa-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We had CU23 installed already, and installed KB5001779 recently. Since then, OWA and ECP show "400 Bad Request".    

When we run UpdateCas.ps1 we get an error about missing files:    

    

We've successfully removed and recreated the OWA and ECP virtual directories but still no luck.    

Any suggestions?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-21*

Hi @Lanky Doodle      

Any update here about this issue? According to the error you provided above, cannot find the file XXX, I would recommend you copy the file from another Exchange server to this one then verify the result again. In addition, check the application log to see if there is any other file lost.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

Hi @Lanky Doodle      

I want to confirm how you installed the security update? From GUI or run cmd as administrator and run MSP? If you installed the security update from GUI, uninstall and reinstall.    

We recommend restarting your computer before installing a security update. Then follow these steps:    

Disable the anti-virus software.    

Open an elevated Command Prompt window (not PowerShell) as an administrator, like this:    

Select Start and then enter cmd .    

Right-click Command Prompt in the results and select Run as administrator .    

If the User Account Control dialog box appears, select Yes and then Next .    

At the command prompt, enter the full path to the folder that contains the 'MSP file', then press 'Enter'.    

Note: Do not double-click the 'MSP file' to run it.    

When the installation is complete, re-enable the antivirus software and restart your computer. (The installation program may prompt you to restart.)    

If problems occur during or after this installation, please refer to Repair failed installations of Exchange Cumulative and Security updates before contacting Microsoft Support.    

Is this a newly installed Exchange server or you upgrade from previous CU?     

We will need to check whether the issue is related to the Exchange install or Security update install. Please check the Exchange setup log to see if there is any error when installing the server. In addition, take a look at the application log in event viewer to see if there is any related error information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
