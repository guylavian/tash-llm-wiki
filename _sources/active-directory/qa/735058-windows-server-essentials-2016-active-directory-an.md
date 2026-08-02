---
title: "Windows Server Essentials 2016  Active Directory and Sql Server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/735058/windows-server-essentials-2016-active-directory-an
question_id: 735058
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server Essentials 2016  Active Directory and Sql Server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/735058/windows-server-essentials-2016-active-directory-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a Dell Server that has WSE26016 installed as a Domain Controller with AD. There are (6) of us in the office. There is also a training computer and a plotter computer connected.   

We have an SQL server running two databases for two different software packages. One is for the estimators and the other is for the accounting software. A couple weeks ago tech support for the accounting software was making some modifications in SMSS and the SQL quit running and we decided to restart the server. When we did, the WSE server would no longer boot with error code 0xc0002e2. I spent a week trying to correct this. But have been unsuccessful. I am now thinking about starting from scratch.   

Files are temporarily being served from Synology boxes and SQL is being run on desktops.   

I have started to read some posts that are discouraging our original setup, recommending a separate Domain Controller from a SQL Server.   

Question 1. Is using a domain controller overkill for a small office like ours?   

Question 2. Are we asking for more trouble by having a single machine server running both AD and SQL Server Express?   

Question 3. If I move to a second server to separate DC and SQL, does that mean I can no longer use WSE2016 and need to move to a full blown server?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-17*

If that is the case, then I guess I really need to figure out why  my DC will not boot. What failsafe method should be used to protect the DC so that if it fails I can get it going again. I tried everything I could to repair the 0x0c000e2e error and nothing has worked. I would have thought that doing a server restore from backup would have got us going. But it doesn't either. I tried booting into Directory Services Repair Mode. I made it through repairing the DC and rebooted only to be brought right back to the error screen.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-17*

Essentials 2016 cannot be configured in a workgroup environment and domain environment is necessary. In addition, the built-in client backup of WSE is also based on domain environment.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-17*

Looks like maybe my best bet is to run my SQL Server and Client Backups on the server. Then use my NAS for file share and document backups. Can I use the Client Backups without promoting the server to an DC with AD?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-14*

SQL on a domain controller is not a good practice no matter the edition. Another option with a standard server could be to install the hyper-v role (as only role) on host, then stand up two virtual machines. One for active directory domain services and another as the application server. As to SQL on a member server in essentials domain; that should be fine to do.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
