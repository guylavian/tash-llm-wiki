---
title: "Batch file of a scheduled task through GPO not working, it works when launched manually"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/540494/batch-file-of-a-scheduled-task-through-gpo-not-wor
question_id: 540494
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Batch file of a scheduled task through GPO not working, it works when launched manually

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/540494/batch-file-of-a-scheduled-task-through-gpo-not-wor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have setup a GPO to deploy a scheduled task which runs a batch file available at server level.    

The batch has been saved in both these locations:    

I first tried with this:    

\servername\shared_folder\scripts    

then this:    

\servername\SYSVOL\domain_name\scripts    

The task is available at the domain computer client after the `gpupdate /force` command. Unfortunately, it doesn't work, I mean either at the scheduled time or by running it manually through the RUN button in the scheduler task app.    

But... If I launch manually the batch file through the file explorer app, it works.    

I cannot understand which kind of errors there are.    

Here are the task details:    

    

    

NT AUTHORITY\SYSTEM has FULL CONTROL at the folder (and file) where the batch file is stored.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-08*

no luck getting this to work, nothing shows under scheduled task

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-06*

If the script is local to the machine, don't use a UNC path (\server\share), point directly to the drive. C:\MyData\Scripts\myScript.bat.  

If you are trying to run a task on a workstation, and pull the script from a server over the network, then you will need to insure that the AD account for the machine (YourDomain\WorkStation1$) has access on both the share permissions and file permissions on the server since you are running the task as SYSTEM.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-06*

Hello R99photography

The default locations should be:

%SystemRoot%\SYSVOL\sysvol\<domain DNS name>\scripts.

or

%SystemRoot%\SYSVOL_DFSR\sysvol\<domain DNS name>\scripts (for DFS-Based FRS since as is recommended from Server 2012R2 and avobe)

If still don't run I would try to enable the synchronous load in the GPO:  

"User Configuration -> Policies -> Administrative Templates -> System -> Scripts" to "Enabled

Also the logon delay settings at: Configure Logon Script Delay setting to Disabled in the Computer Configuration ->Administrative Templates ->System ->Group Policy
