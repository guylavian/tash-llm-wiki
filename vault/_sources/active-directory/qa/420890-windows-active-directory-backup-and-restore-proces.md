---
title: "Windows Active Directory backup and restore process to another server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/420890/windows-active-directory-backup-and-restore-proces
question_id: 420890
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Windows Active Directory backup and restore process to another server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/420890/windows-active-directory-backup-and-restore-proces (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,  

We have a scenario, where my security team asking us for BCP (Business Continuity Plan). For this, they are asking us to restore the Production AD backup to another server and share the evidence that it got successful.  

We have taken the system state backup. but my doubt does we need to promote the DC for (New Server) before we restore ?  

Any suggestions. Please help.  

Regards,  

Ram

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-04*

Hi，  

Thank you for posting in our forum  

You can restore the Microsoft Windows operating system from a system state backup. You can restore a system state backup to the same physical computer from which the system state backup was created, or to a different physical computer that has the same make, model, and configuration (identical hardware).  

However, we do not support restoring a system state backup from one computer to a second computer of a different make, model, or hardware configuration. We only provide commercially reasonable efforts to support this process. Even if the source and destination computers seem to be identical makes and models, the source computers may have different drivers, hardware, or firmware than the destination computers.  

The related KB:  

How to restore a Windows installation or move it to different hardware  

http://support.microsoft.com/kb/249694/EN-US  

There have an example AD backup and restore article you can refer first.  

Active Directory Backup and Restore in Windows Server 2008  

http://technet.microsoft.com/en-us/magazine/2008.05.adbackup.aspx  

More information:  

Useful shelf life of a system-state backup of Active Directory  

http://support.microsoft.com/kb/216993  

I’m glad to be of help to you!  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-03*

Something here may help.  

http://woshub.com/restore-active-directory-dc-from-backup/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
