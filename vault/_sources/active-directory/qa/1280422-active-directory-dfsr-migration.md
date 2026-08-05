---
title: "active directory DFSR migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1280422/active-directory-dfsr-migration
question_id: 1280422
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# active directory DFSR migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1280422/active-directory-dfsr-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, i have a this question/doubt

in my environment I have 3 domain controller, Friday I performed the first 2 migration steps, today I wanted to perform the last step (Dfsrmig /setglobalstate 3) but yesterday one of the domain controllers shut down 3 times due to BSODin the DFSR logs I have no errors, but in the File replication services logs I have this

```

```

by the way this domain controller will be deleted. Do you think I can proceed with the last step of the DFSR migration ignoring the FSR error?

thanks

Andrea

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-10*

Hi,

I think I wasn't clear, the migration to the prepared state was successful, the DC problem happened later.

in fact the replication of the sysvol_dfsr folder works correctly, I created a gpo after the migration in the "redirected" state and it is replicated on all domain controllers

I have no errors with dcdiag, the replica works fine on all domain controller

I know the prerequisites

thanks

cheers

Andrea

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

I'd remove the problematic or failed one before making any changes or doing the FRS->DFSR migration, then confirm health is 100% via dcdiag, repadmin tools and by checking the System and FRS Replication event logs are free of all errors.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-09*

ok, but i rollback the dfsr migration? or i can fix it? now the dfsr migration is on state 2 - Redirected.

or other way, can i demote the domain controller before? so this server it must still be removed. I I have to add a domain controller with windows 2019 instead of 2012 R2.

thanks

Andrea

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

No you should cancel the migration and fix what's broken before proceeding. You can follow along here with a nonauthoritative restore

https://learn.microsoft.com/en-us/services-hub/health/remediation-steps-ad/investigate-file-replication-service-frs-journal-wrap-conditions-on-domain-controllers#suggested-actions  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-09*

sorry missing the event error

```
The File Replication Service has detected that the replica set "DOMAIN SYSTEM VOLUME (SYSVOL SHARE)" is in JRNL_WRAP_ERROR. 
 
 Replica set name is    : "DOMAIN SYSTEM VOLUME (SYSVOL SHARE)" 
 Replica root path is   : "c:\windows\sysvol\domain" 
 Replica root volume is : "\\.\C:" 
 A Replica set hits JRNL_WRAP_ERROR when the record that it is trying to read from the NTFS USN journal is not found.  This can occur because of one of the following reasons. 
 
 [1] Volume "\\.\C:" has been formatted. 
 [2] The NTFS USN journal on volume "\\.\C:" has been deleted. 
 [3] The NTFS USN journal on volume "\\.\C:" has been truncated. Chkdsk can truncate the journal if it finds corrupt entries at the end of the journal. 
 [4] File Replication Service was not running on this computer for a long time. 
 [5] File Replication Service could not keep up with the rate of Disk IO activity on "\\.\C:". 
 Setting the "Enable Journal Wrap Automatic Restore" registry parameter to 1 will cause the following recovery steps to be taken to automatically recover from this error state. 
 [1] At the first poll, which will occur in 5 minutes, this computer will be deleted from the replica set. If you do not want to wait 5 minutes, then run "net stop ntfrs" followed by "net start ntfrs" to restart the File Replication Service. 
 [2] At the poll following the deletion this computer will be re-added to the replica set. The re-addition will trigger a full tree sync for the replica set. 
 
WARNING: During the recovery process data in the replica tree may be unavailable. You should reset the registry parameter described above to 0 to prevent automatic recovery from making the data unexpectedly unavailable if this error condition occurs again. 
 
To change this registry parameter, run regedit. 
 
Click on Start, Run and type regedit. 
 
Expand HKEY_LOCAL_MACHINE. 
Click down the key path: 
   "System\CurrentControlSet\Services\NtFrs\Parameters" 
Double click on the value name 
   "Enable Journal Wrap Automatic Restore" 
and update the value. 
 
If the value name is not present you may add it with the New->DWORD Value function under the Edit Menu item. Type the value name exactly as shown above.
```
