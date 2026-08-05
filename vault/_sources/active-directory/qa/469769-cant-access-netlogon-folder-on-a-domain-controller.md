---
title: "Can't access netlogon folder on a domain controller that has DFSR"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/469769/cant-access-netlogon-folder-on-a-domain-controller
question_id: 469769
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-high-availability-storage-other"]
answer_author_affiliations: ["Mvp"]
---
# Can't access netlogon folder on a domain controller that has DFSR

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/469769/cant-access-netlogon-folder-on-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I have been troubleshooting a group policy issue and it has led to me realise that I can't access the netlogon folder on one of our dc's.

When running Get-ADReplicationFailure -Target DC1

I get the following error:

PS C:\Users> Get-ADReplicationFailure -Target DC1  

Get-ADReplicationFailure : Unable to contact the server. This may be because this server does not exist, it is currently down, or it does not have the Active Directory Web Services running.  

At line:1 char:1  

-  Get-ADReplicationFailure -Target DC1  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : ResourceUnavailable: (DC1:String) [Get-ADReplicationFailure], ADServerDownException  

-  FullyQualifiedErrorId : ActiveDirectoryServer:0,Microsoft.ActiveDirectory.Management.Commands.GetADReplicationFailure

If I run the same command on any other dc, connection is fine.

When trying to access the netlogon folder. I receive the message 'Network access is denied' (I'm logged on as domain admin)

At dc1 I have the following folder:

\dc1\c$\Windows\SYSVOL_DFSR

But for the other 3 dc's they have:

\dc2\c$\Windows\SYSVOL

It appears that DC1 has distributed file system replication enabled but I inherited this set-up and have no idea what has been configured. I'll be honest and say I know very little about how this even works. Can someone point me in the right direction of what the implications of having DFSR enabled on a sysvol and why I can't access the netlogon folder. The server in question is our oldest running Server 2012 standard. I plan to retire it in the near future but for now, would like to have healthy replication.

Many Thanks in advance for any help with this matter.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-09*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-09*

-  The underlying folder on the DCs that were migrated (FRS to DFSR) will be Sysvol_DFSR but the share name for all is SYSVOL    

-  The folder name and share name for new DCs will be SYSVOL    

    

The simplest solution may be to move roles off, demote the problematic one, reboot, promo again.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-09*

The first command fails to connect to the server that has issues:

Command Line: "dcdiag.exe  

/v /c /d /e /s:dc1"

Directory Server Diagnosis

Performing initial setup:

-    Connecting to directory service on server dc1.    Ldap search capability attribute search failed on server dc1, return value =    81  

    DcDiag: uncaught exception raised, continuing search

Do you want me to run the same command on the others? if so, just one of them are all 3?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-09*

Hi,  

Thanks for the quick reply, very much appreciated.   

Does it defiantly imply there is  a problem if I cant access dc1\sysvol ? Should I be able to?  

We do use DFS name Space. Could it be the DC has been configured with DFSR to accommodate this? (sorry, I don't know)  

I'm trying to avoid anything unless absolutely essential. I don't actually know id this is an issue at the moment,. group Policy generally seems to be working ok but I'm just mindful that I should be able to access the sysvol.  

Thanks again for your help.
