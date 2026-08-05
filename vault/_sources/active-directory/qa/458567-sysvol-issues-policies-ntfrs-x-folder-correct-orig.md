---
title: "Sysvol issues - Policies_NTFRS_xxxx folder correct - original policies folder has a lot of inaccessible folders?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/458567/sysvol-issues-policies-ntfrs-x-folder-correct-orig
question_id: 458567
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Sysvol issues - Policies_NTFRS_xxxx folder correct - original policies folder has a lot of inaccessible folders?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/458567/sysvol-issues-policies-ntfrs-x-folder-correct-orig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two Policies (and scripts) folders in our SYSVOL folder.  It stays in sync on all six of our DCs.  But I want to clean this up.  How do I get rid of the oddly named "Policies_NTFRS_xxxx" folder and only have "Policies" folder?  Same for Scripts as well...    

It seems there are a lot of inaccessible folders in my correctly named Policies folder.  I've tried running some icacls scripts I found in the forums here but it tells me it doesn't have permissions to run, even from an elevated PS prompt.  I cannot take ownership of the folders at all either.      

If I try to take ownership of the folders, it tells me I don't have permissions, even after attempting to take ownership with administrator permissions.      

    

    

The script I tried to run is this:    

```
$Policies = Get-ChildItem C:\Windows\SYSVOL\domain\Policies -Name -Filter "{*}"  
      
    foreach ($Policy in $Policies) {  
        icacls "C:\Windows\SYSVOL\domain\Policies\$policy" /remove:g "\Domain Admins"  
        icacls "C:\Windows\SYSVOL\domain\Policies\$policy" /grant "\Domain Admins:(OI)(CI)(F)"  
        icacls "C:\Windows\SYSVOL\domain\Policies\$policy"  
        }
```

It works for every folder in my oddly named Policies folder, but when I run it on my normally named Policies folder I get a bunch of inaccessible files errors.      

icacls : C:\Windows\SYSVOL\domain\Policies{2F8111C2-4632-4D12-B8BF-DFE08204C2DE}: Access is denied.    

I went through my excess GPOs we no longer use and removed them via group policy manager and replication appears to work across DCs as the count of GPOs has increased and decreased accordingly.  Just our ACL permissions are wrong according to GPMC.      

What is the proper way to fix this?  How can I take ownership, purge the bad folders, and get rid of the oddly named policies (and scripts) folders so I only have one main Policies and Scripts layout as intended with AD?      

Currently, we are on Server 2012 R2 with plans to upgrade in a few weeks to 2019 possibly if time permits and I can get this sorted out ;)    

Update: I also have tried to go into GPMC -> delegations -> advanced -> advanced -> restore defaults ... for each remaining GPO we have.  Yet the GPMC still reports ACLs errors...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-01*

Actually, I never went through a DFRS migration and I'm still on FRS.  I cannot take ownership of the folders either.  It's completely dead and inaccessible.  It appears to be all the old GPOs I have deleted from GPMC over the years that leave some garbage folders and mark them inaccessible.    

In the screenshots above - if I click on "change" to take ownership of the folder, it brings up the same next screenshot - no permission to do so.  

All of my replications are happening and functioning out of the _NTFRS_xxxx folders.  The properly named "Policies" folder is actually the "old" one that's not getting updated anymore...   

In the AD replication status tool, I have zero errors... it's amazing to look at.  But I really wish I could get the dumb folder naming fixed for my OCD.  Even though it's probably been like this since we upgraded to 2012 R2 seven years ago or so... :)  

In any case, I presume I need to upgrade to DFRS in order to upgrade to 2019... so what happens if there are folders that are inaccessible when this happens??

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-30*

You may have to take ownership of those you have no permissions to, but this also seems pretty risky especially since thing are working nicely. It may be something went wrong during the FRS->DFSR migration. I do still have domain that went through migration but I don't have the folders you spoke of. The article is about a complete rebuild of the sysvol  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

I appreciate the quick response - however, my replication is fine - it's strictly the inaccessible files that are the main issue.  I imagine the _NTFRS_xxx folders are being created because there are inaccessible folders back in the 2003/2008 DC days.  Even with your instructions I don't see how to clearly erase the folders that I do not have permission to access... ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-30*

May be a bit risky and somewhat involved. Make sure some good backups are in place before taking this on.  

https://gist.github.com/RavuAlHemio/00e51d3ea64731be9d43b01eda18734f  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
