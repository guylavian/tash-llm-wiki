---
title: "Windows Server 2022 Domain Controller Losing Disk Space On Logs Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164556/windows-server-2022-domain-controller-losing-disk
question_id: 1164556
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server 2022 Domain Controller Losing Disk Space On Logs Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164556/windows-server-2022-domain-controller-losing-disk (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

We have a Windows Server2022 Data Center environment with 3 domain controllers with different roles. We have 2 DCs losing free disk space (shrinks about 1 GIG a week) and I cannot locate any files that could be using space.  I will just note the following for one DC with the hope someone here can shine some light on how to troubleshoot and identify what is going on with the logical drive losing space.  

(Logical Volume for logs directory)

E= Logs (Total volume = 19.9 GIG. Free space =13.3GIG)

-  If I check the properties of the drive it displays used space=6.66GB

-  If I expand the folder and navigate to the logs directory, all logs combined are 110MB

-  I've unhidden system files and hidden files, folders, and drives, but cannot find any files that would be using over 6GIG

-  I installed a Windirstat program that scans the directory and lists all files, but even with this program, there is nothing displaying additional files.

I'm at a loss and can't find any KB article anywhere that could help me identify the issues. I'm assuming there is some orphaned or phantom file somewhere that maybe a PowerShell command can be run to find what is eating up the space.

Any help would be appreciated.

Thanks in advance,

Bob

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-01-26*

3 domain controllers with different roles  

What roles? Generally speaking, it isn't recommended to install other roles / applications on a domain controller. You may want to consider standing up a new dedicated virtual machine for active directory domain services.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-26*

Dave,

I appreciate your input, but this is a last resort that I don't want to entertain.  Also, I never said I couldn't find the log files. The log files are there (they are only 110MEG combined). The problem is the partition is using over 6GIG of space and I can't find what is using that space. There are no issues with active directory or replication and no event viewer errors for any AD-specific issues. 

I will defer to Microsoft and post back the solution so you will have (as well as myself) a better understanding of what the issue is.

Thanks,

Bob

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-26*

Since you can't find the log files or the source of disk space usage the simplest thing to do may be to stand up a new one for replacement. 

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
