---
title: "Server 2008 R2 to Server 2019 Active Directory Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/480042/server-2008-r2-to-server-2019-active-directory-mig
question_id: 480042
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Server 2008 R2 to Server 2019 Active Directory Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/480042/server-2008-r2-to-server-2019-active-directory-mig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working on migrating my old Server 2008 R2 AD to a 2019 Server. I found out that I could run PowerShell on the 2019 to get the forest to the same version as the 2008 R2. I found a video on YouTube (https://www.youtube.com/watch?v=vuzrihbet1E&t=1515s&ab_channel=MSFTWebCast)  

He has a several step process. I downloaded the Server 2019 ISO and then used the files from it to run the PowerShell commands for the forest. If you look at his steps, his step 4 references to make sure that replication is happening. I checked and it is. The downside is that now no one can log into the network without typing their username along with their domain name. They can no longer use their username (example - doejohn). They now have to login with the domain name attached to it (example - doejohn@ssss  .local). Both ADs are still active at this time (Server 2008 R2 and Server 2019). Keep in mind that the Forest Level of the 2019 is 2008 R2. If someone tries to login such as doejohn, it says that the account has been disabled and to contact System Admin. My main Administrator account that I was using prior to the migration no longer works as an admin. I can log in, but it has no admin rights. When I log into the Active Directory Users and Groups, the Account information is changed. The User logon name is still set at doejohn and out to the right it has our @ssss  .local domain. In User login name (pre-Windows 2000) it has our "domainname\" there and then to the right of it, it has the user with alot of characters after it such as doejohnddiwoe34ougnd When I try to change that to just doejohn, it states "The specified account already exists." I don't know if this will help out, but I did try to use the Storage Migration Service through the Windows Admin Center. Thing is, I started the transfer and it moved 1 file over and nothing since. In the General tab of the account in Active Directory it states Description "Storage Migration Service renamed doejohn to doejohn2t2vzivnbc. Storage Migration Service renamed doejohn2t2vzivnbc to doejohn2t2en0rpujnty renamed doejohn to doejohn2t2vzivnbc. Storage Migration Service renamed doejohn2t2vzivnbc to doejohn2t2en0rpujnty". Needless to say, I'm at a loss now. Any help in figuring this out would greatly be appreciated. Thanks in advance.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-18*

You may need to restore from a recent backup and try again. The steps I would have followed are below.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

The other option may be to start a case here with product support.    

https://support.serviceshub.microsoft.com/supportforbusiness    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-26*

Hi,    

It is suggested to check the following points:    

1, If the logon name is the same as the UPN .    

    

2, If there are any machines have the same name with the domain.    

3, We may try to capture a network package to get more details.    

Best Regards,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-19*

Hi,  

Based on my understanding, now you had added the 2019 server ad a domain controller, and transfer the FSMO roles, and the old one still act as a DC, right?  

Before adding the new one, we should at least meet the following requirements:  

The old DC is working well  

The forest level is 2008R2 or higher, and the DFS-R is used for the sysvol replication.  

For now, do you have a domain account which can log on and runs normally?  

What's the result if shut down the new server, if the old one still works?  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-18*

From PowerShell  

`Get-ADForest`

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-18*

Hard to tell here but it sounds like a new domain might have been created? From PowerShell  

`Get-ADForest`
