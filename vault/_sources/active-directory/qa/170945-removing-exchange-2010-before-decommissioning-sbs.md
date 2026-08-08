---
title: "Removing Exchange 2010 before decommissioning SBS 2011 lost access to Active Directory on both servers."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/170945/removing-exchange-2010-before-decommissioning-sbs
question_id: 170945
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Removing Exchange 2010 before decommissioning SBS 2011 lost access to Active Directory on both servers.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/170945/removing-exchange-2010-before-decommissioning-sbs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to decommission an SBS 2011 server and promote my Server 2019 to take over all roles.  The 2019 server is a domain controller but does not yet hold any FSMO roles.  The email has long been moved and I'm just trying to remove Exchange 2010, transfer roles, and demote the server.  Well I kept getting an error when removing the Mailbox role from within the EMC.  So I'm trying just to remove the few mailboxes that were in there as well as both the Public and Private databases.  It seems like shortly after I removed the Admin mailbox from the Exchange Management Console, not active directory or the SBS Console "explorer" locked up and restarted.  Then I started receiving new errors when finishing removing the mailboxes.  Basically I couldn't do anything and started getting user errors.  So thinking it's just Exchange being jacked up because this was the last role to remove I rebooted the SBS server.  

Now I cannot remotely access the SBS server with the Admin logon, I get a user account error.  I'm still remoted into the 2019 server but getting user account permission errors when trying to access anything inside the Administrative Tools.  I don't need anything off of this SBS server but I do need access to Active Directory so I can finish my my deployment.  I'm definitely afraid to disconnect form the 2019 server as it seems the user account is hosed and yes it's the only domain admin account.  The last thing I expected to happen.  How does removing the Admin mailbox hose the entire user account?  Anyone have any ideas on what I can do?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-22*

I'm thinking I just need to remove the SBS from the network totally, restore the RegBackup files on the 2019 server to restore my Admin user account and the registry to 8 hours before and then seize the FSMO roles and manually remove the SBS server from Active Directory and DNS. Unless however I can do an easy or similar repair on the SBS which I won't know until I am onsite.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-22*

Sounds like a fatal error. I'd probably look at restoring the SBS to a known good point. Then start the migration over.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-22*

trying to repair or replace the domain admin account  

Sounds like you'll need to use a backup domain admin account if the main account is somehow broken.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-22*

test all failed  

Sounding like health may not have been 100% before beginning migration. You may need to start the migration over if things we broken before starting.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-22*

I don't need anything off of this SBS server but I do need access to Active Directory    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

If you cannot demote the SBS2011 gracefully then you can remove it from network and perform cleanup to remove remnants from active directory.     

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
