---
title: "All User Locked out of Exchange Management Shell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1036462/all-user-locked-out-of-exchange-management-shell
question_id: 1036462
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
---
# All User Locked out of Exchange Management Shell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1036462/all-user-locked-out-of-exchange-management-shell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

To get around the recent security issue with remote access to Exchange Management Shell I ran the following command.      

get-user -ResultSize unlimited |    

set-user -RemotePowerShellEnabled $false    

This command should have removed access for all users except the logged in user.  This did not happen and now everyone is locked out of EMC.  I tried creating a new admin thinking this would get around the issue since it should have been given the default of having access but it did not work.  We always run the EMC as administrator and this could have been what caused some of these problem.      

Before the changes I had taken a snapshot, so I reverted back to it, but we still have no access.  Is there anything I can do at this point to regain access?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

Thank you so much.  This worked with a slight tweak.  We did not have the admin version of the snap-in so the syntax changed a bit:    

get-pssnapin -registered    

Name        : Microsoft.Exchange.Management.PowerShell.SnapIn    

PSVersion   : 1.0    

Description : Admin Tasks for the Exchange Server    

We ran the command for this version    

Add-PSSnapIn Microsoft.Exchange.Management.PowerShell.Snapin    

 set-user <user> -RemotePowerShellEnabled $true    

I was able to add our admin users and we once again gained the ability to use the EMC.
